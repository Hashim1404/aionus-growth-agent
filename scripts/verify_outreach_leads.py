#!/usr/bin/env python3
"""
AIONUS Pre-Flight Lead & Outreach Validator (macOS, Linux & Windows)
Enforces decision-maker custom domains, live MX verification, DO_NOT_CONTACT checks,
and outreach copy guardrails before any cold email or DM is sent.
"""
import argparse
import os
import re
import subprocess
import sys

BANNED_PREFIXES = {
    "care", "support", "customercare", "wecare", "help", "info", "hello",
    "contact", "online", "connect", "sales", "grievance", "hr", "careers",
    "jobs", "recruitment", "hiring", "office", "admin", "enquiry", "inquiry",
    "marketing", "pr", "media", "press", "team", "orders", "billing", "accounts",
    "reception", "frontdesk", "service", "feedback", "legal", "compliance"
}

CONSUMER_DOMAINS = {
    "gmail.com", "googlemail.com", "yahoo.com", "yahoo.co.in", "outlook.com",
    "hotmail.com", "live.com", "icloud.com", "me.com", "aol.com", "proton.me",
    "protonmail.com", "rediffmail.com", "ymail.com", "mail.com", "zohomail.in"
}

BANNED_SUBJECT_WORDS = {"workflow", "workflows", "automation", "automations", "systems", "operations"}


def load_do_not_contact(dnc_path: str) -> set:
    blocked = set()
    if not os.path.exists(dnc_path):
        return blocked
    with open(dnc_path, "r", encoding="utf-8") as f:
        for line in f:
            clean = line.strip().lower()
            if not clean or clean.startswith("#"):
                continue
            for token in re.findall(r"[a-z0-9._-]+\.[a-z]{2,}", clean):
                blocked.add(token.lstrip("www."))
    return blocked


def check_mx_record(domain: str) -> tuple[bool, str]:
    try:
        res = subprocess.run(
            ["dig", "+short", "MX", domain],
            capture_output=True, text=True, timeout=6
        )
        out = res.stdout.strip()
        if out:
            return True, out.splitlines()[0]
    except (FileNotFoundError, subprocess.SubprocessError):
        pass

    try:
        res = subprocess.run(
            ["nslookup", "-type=mx", domain],
            capture_output=True, text=True, timeout=6
        )
        out = (res.stdout + "\n" + res.stderr).lower()
        if "mail exchanger" in out or "mx preference" in out:
            return True, "MX verified via nslookup"
    except (FileNotFoundError, subprocess.SubprocessError):
        return False, "Neither dig nor nslookup available"

    return False, "No MX records found"


def validate_lead(email: str, subject: str = "", body: str = "", dnc_path: str = "memory/DO_NOT_CONTACT.md") -> list[str]:
    errors = []
    email = email.strip().lower()
    if "@" not in email:
        return [f"Invalid email format: {email}"]

    local_part, domain = email.split("@", 1)
    domain = domain.lstrip("www.")

    if domain in CONSUMER_DOMAINS:
        errors.append(f"FAIL [Consumer Domain]: '{domain}' is a personal consumer inbox. Use the founder's custom company domain.")

    clean_local = re.sub(r"[^a-z]", "", local_part.split(".")[0])
    if local_part in BANNED_PREFIXES or clean_local in BANNED_PREFIXES:
        errors.append(f"FAIL [Role/Lower-Level Inbox]: '{local_part}@' is a generic or lower-level inbox. Strictly target the Founder/CEO's personal work email.")

    blocked_domains = load_do_not_contact(dnc_path)
    if domain in blocked_domains:
        errors.append(f"FAIL [Do Not Contact]: '{domain}' is already listed in {dnc_path}. Never double-pitch.")

    has_mx, mx_info = check_mx_record(domain)
    if not has_mx:
        errors.append(f"FAIL [MX Record]: Domain '{domain}' has no valid mail server ({mx_info}).")

    if subject:
        if len(subject) > 35:
            errors.append(f"FAIL [Subject Length]: Subject is {len(subject)} chars (max 35 chars).")
        subj_words = set(re.findall(r"[a-z]+", subject.lower()))
        triggered = subj_words.intersection(BANNED_SUBJECT_WORDS)
        if triggered:
            errors.append(f"FAIL [Subject Trigger Words]: Remove sales trigger words from subject: { sorted(triggered) }")

    if body:
        if "\u2014" in body or "\u2013" in body or "--" in body:
            errors.append("FAIL [Em Dash Detected]: Remove all em dashes, en dashes, or double hyphens from the message.")
        if "Aionus" in body or "aionus " in body:
            errors.append("FAIL [Brand Capitalization]: Always write AIONUS in ALL-CAPS (except inside the URL aionus.in).")
        words = len(body.split())
        if words > 95:
            errors.append(f"FAIL [Word Count]: Message is {words} words (keep cold emails under 90 words and DMs under 70 words).")

    return errors


def main():
    parser = argparse.ArgumentParser(description="Validate AIONUS outreach lead email and copy.")
    parser.add_argument("--email", required=True, help="Founder work email to validate (e.g., founder@brand.com)")
    parser.add_argument("--subject", default="", help="Optional cold email subject line")
    parser.add_argument("--body", default="", help="Optional outreach message body")
    parser.add_argument("--dnc", default="memory/DO_NOT_CONTACT.md", help="Path to DO_NOT_CONTACT.md")
    args = parser.parse_args()

    errors = validate_lead(args.email, args.subject, args.body, args.dnc)
    if errors:
        print(f"VALIDATION FAILED for {args.email}:")
        for err in errors:
            print(f"  - {err}")
        sys.exit(1)
    else:
        print(f"PASS: {args.email} verified (custom domain, live MX, decision-maker prefix, copy compliant).")
        sys.exit(0)


if __name__ == "__main__":
    main()
