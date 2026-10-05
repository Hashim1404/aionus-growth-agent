#!/usr/bin/env python3
"""
AIONUS Agent-to-Agent Dispatcher to Rias (rias@agentmail.to)
Automatically sends Warm Lead Handoffs and End-of-Day Activity Reports from the
operator's AI directly to Rias (Executive AI Partner to Hashim at AIONUS),
and outputs a clean WhatsApp summary card as a backup.
"""
import argparse
import datetime
import json
import os
import smtplib
import ssl
import sys
import urllib.error
import urllib.request
from email.message import EmailMessage

RIAS_EMAIL = "rias@agentmail.to"


def load_env(env_path: str = ".env") -> dict:
    env = dict(os.environ)
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    return env


def send_via_agentmail_api(api_key: str, inbox_id: str, subject: str, text_body: str) -> tuple[bool, str]:
    url = f"https://api.agentmail.to/v0/inboxes/{inbox_id}/messages/send"
    payload = json.dumps({
        "to": [RIAS_EMAIL],
        "subject": subject,
        "text": text_body
    }).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            if 200 <= resp.status < 300:
                return True, f"Dispatched to {RIAS_EMAIL} via AgentMail API"
            return False, f"AgentMail HTTP {resp.status}"
    except Exception as e:
        return False, f"AgentMail API error: {e}"


def send_via_smtp(smtp_email: str, smtp_password: str, subject: str, text_body: str) -> tuple[bool, str]:
    msg = EmailMessage()
    msg["From"] = smtp_email
    msg["To"] = RIAS_EMAIL
    msg["Subject"] = subject
    msg.set_content(text_body)
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context, timeout=10) as server:
            server.login(smtp_email, smtp_password)
            server.send_message(msg)
        return True, f"Dispatched to {RIAS_EMAIL} via SMTP ({smtp_email})"
    except Exception as e:
        return False, f"SMTP error: {e}"


def main():
    parser = argparse.ArgumentParser(description="Send Warm Lead Handoff or EOD Summary to Rias (rias@agentmail.to)")
    parser.add_argument("--mode", choices=["handoff", "eod"], required=True, help="Report type: handoff or eod")
    parser.add_argument("--operator", required=True, help="Operator / Intern name")
    # Handoff fields
    parser.add_argument("--company", default="", help="Company / Brand name")
    parser.add_argument("--website", default="", help="Company website URL")
    parser.add_argument("--founder", default="", help="Founder / Decision-Maker Name & Title")
    parser.add_argument("--contact", default="", help="Direct Phone, Email, and LinkedIn/IG")
    parser.add_argument("--channel", default="", help="Outreach channel (Cold Call, Email, LinkedIn, IG)")
    parser.add_argument("--notes", default="", help="Conversation context, bottlenecks discussed, and why they are interested")
    parser.add_argument("--call-time", default="", help="Proposed discovery call time with Hashim")
    # EOD fields
    parser.add_argument("--scraped", type=int, default=0, help="Number of leads scraped/verified today")
    parser.add_argument("--calls", type=int, default=0, help="Number of cold calls dialed today")
    parser.add_argument("--messages", type=int, default=0, help="Number of cold emails/DMs sent today")
    parser.add_argument("--warm", type=int, default=0, help="Number of warm replies or booked calls today")
    parser.add_argument("--details", default="", help="Detailed summary of today's leads and outcomes")

    args = parser.parse_args()
    today_str = datetime.date.today().isoformat()
    env = load_env()

    if args.mode == "handoff":
        subject = f"[AIONUS HANDOFF] {args.company} ({args.founder}) via {args.operator}"
        email_body = (
            f"AIONUS WARM LEAD HANDOFF FOR HASHIM & RIAS\n"
            f"==========================================\n"
            f"Date: {today_str}\n"
            f"Sourced By: {args.operator}\n"
            f"Company: {args.company}\n"
            f"Website: {args.website}\n"
            f"Decision Maker: {args.founder}\n"
            f"Direct Contact: {args.contact}\n"
            f"Channel: {args.channel}\n"
            f"Proposed Call Time with Hashim: {args.call_time}\n\n"
            f"Context & Discussion Notes:\n"
            f"{args.notes}\n"
        )
        whatsapp_card = (
            f"*AIONUS WARM LEAD HANDOFF*\n"
            f"• *Company:* {args.company} ({args.website})\n"
            f"• *Founder:* {args.founder}\n"
            f"• *Direct Contact:* {args.contact}\n"
            f"• *Channel:* {args.channel}\n"
            f"• *Context / Interest:* {args.notes}\n"
            f"• *Proposed Call Time:* {args.call_time}"
        )
    else:
        subject = f"[AIONUS EOD REPORT] {today_str} - {args.operator}"
        email_body = (
            f"AIONUS END-OF-DAY GROWTH SUMMARY\n"
            f"================================\n"
            f"Date: {today_str}\n"
            f"Operator: {args.operator}\n"
            f"Leads Verified: {args.scraped}\n"
            f"Cold Calls Dialed: {args.calls}\n"
            f"Emails / DMs Sent: {args.messages}\n"
            f"Warm Replies / Booked Calls: {args.warm}\n\n"
            f"Detailed Activity Log:\n"
            f"{args.details}\n"
        )
        whatsapp_card = (
            f"*AIONUS Daily Growth Wrap ({today_str} - {args.operator})*\n"
            f"• Leads Verified: {args.scraped} | Calls Dialed: {args.calls} | Emails/DMs Sent: {args.messages}\n"
            f"• Warm Replies / Booked Calls: {args.warm}\n"
            f"• Key Notes: {args.details[:180]}"
        )

    sent = False
    status_msg = "No email API configured in .env yet (use AgentMail MCP tool or copy the WhatsApp card below)."

    if env.get("AGENTMAIL_API_KEY") and env.get("AGENTMAIL_INBOX_ID"):
        sent, status_msg = send_via_agentmail_api(
            env["AGENTMAIL_API_KEY"], env["AGENTMAIL_INBOX_ID"], subject, email_body
        )
    elif env.get("SMTP_EMAIL") and env.get("SMTP_APP_PASSWORD"):
        sent, status_msg = send_via_smtp(
            env["SMTP_EMAIL"], env["SMTP_APP_PASSWORD"], subject, email_body
        )

    os.makedirs("memory/reports_sent", exist_ok=True)
    log_file = f"memory/reports_sent/{today_str}_{args.mode}.txt"
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"--- {subject} ({status_msg}) ---\n{email_body}\n\n")

    print(f"RIAS DISPATCH STATUS: {'SUCCESS' if sent else 'LOGGED_LOCALLY'} ({status_msg})")
    print(f"TARGET RECIPIENT: {RIAS_EMAIL}")
    print(f"SUBJECT: {subject}\n")
    print("--- WHATSAPP SUMMARY CARD FOR HASHIM ---")
    print(whatsapp_card)


if __name__ == "__main__":
    main()
