#!/usr/bin/env python3
"""
AIONUS Apify Mass Lead & Phone Number Scraper (macOS, Linux & Windows)
Uses APIFY_TOKEN from .env to scrape Google Maps / Business Directories or Google Search
via Apify REST API (pure Python stdlib, zero external packages required).
Extracts company names, websites, phone numbers, and locations for cold calling & outreach.
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request


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


def run_apify_google_places(token: str, query: str, location: str, max_results: int = 15) -> list[dict]:
    """
    Calls compass~crawler-google-places synchronously via Apify API to pull
    commercial businesses with phone numbers and websites for cold calling.
    """
    actor_id = "compass~crawler-google-places"
    url = f"https://api.apify.com/v2/acts/{actor_id}/run-sync-get-dataset-items?token={urllib.parse.quote(token)}"
    payload = {
        "searchStringsArray": [query],
        "locationQuery": location,
        "maxCrawledPlacesPerSearch": max_results,
        "language": "en",
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=180) as resp:
        items = json.loads(resp.read().decode("utf-8"))
        results = []
        for item in items:
            if not isinstance(item, dict):
                continue
            website = item.get("website") or ""
            phone = item.get("phone") or item.get("phoneUnformatted") or ""
            if not website and not phone:
                continue
            results.append({
                "title": item.get("title", ""),
                "category": item.get("categoryName", ""),
                "phone": phone,
                "website": website,
                "address": item.get("address", ""),
                "city": item.get("city", ""),
                "rating": item.get("totalScore", ""),
                "reviewsCount": item.get("reviewsCount", 0),
            })
        return results


def main():
    parser = argparse.ArgumentParser(description="Mass-scrape B2B leads, websites, and phone numbers via Apify.")
    parser.add_argument("--query", required=True, help="Search query (e.g. 'luxury interior design studio', 'dermatology clinic', 'designer boutique')")
    parser.add_argument("--location", default="Mumbai, India", help="Location (e.g. 'Mumbai, India', 'Bengaluru, India', 'Delhi, India')")
    parser.add_argument("--limit", type=int, default=10, help="Max leads to pull (default 10)")
    args = parser.parse_args()

    env = load_env()
    token = env.get("APIFY_TOKEN", "")
    if not token or token == "YOUR_APIFY_API_TOKEN":
        print("ERROR: APIFY_TOKEN is not set in .env yet.")
        print("Get your free $5/month Apify token at: https://console.apify.com/sign-up")
        sys.exit(1)

    print(f"Scraping up to {args.limit} leads for '{args.query}' in '{args.location}' via Apify...")
    try:
        leads = run_apify_google_places(token, args.query, args.location, args.limit)
    except Exception as e:
        print(f"Apify scrape error: {e}")
        sys.exit(1)

    print(f"\nFound {len(leads)} commercial leads with phone/website:\n")
    for idx, lead in enumerate(leads, 1):
        print(f"{idx}. {lead['title']} ({lead['category']})")
        print(f"   Phone:   {lead['phone'] or 'N/A'}")
        print(f"   Website: {lead['website'] or 'N/A'}")
        print(f"   City:    {lead['city']} | Reviews: {lead['reviewsCount']} ({lead['rating']}*)")
        print()
    print("NEXT STEP FOR AI: Visit each company's website (/about or LinkedIn) to verify the Founder/CEO's name before presenting 1 lead at a time!")


if __name__ == "__main__":
    main()
