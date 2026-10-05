---
name: aionus-lead-scraper
description: Waterfall B2B lead discovery, Apify mass-scraping, Founder/CEO contact verification, ROI sanity check, and 1-at-a-time lead presentation for AIONUS.
---

# AIONUS Lead Scraping & Decision-Maker Discovery Protocol

Activate this skill automatically whenever the user asks to find leads, scrape companies, pull phone numbers for cold calling, extract founder emails, or research a prospect.

---

## 1. Strict Target Profile (Who to Scrape)

1. **Top-Level Decision Makers ONLY:**
   * Every lead **must** include the verified name and direct contact channel of the **Founder, Co-Founder, Owner, CEO, Managing Director (MD), or Managing Principal**.
   * **Never** scrape or present lower-level employees (marketing managers, HR, store managers, social media managers, executives, or interns). They have zero budget authority.
2. **Right-Sized Commercial Businesses (5 to 50 Employees):**
   * Target commercial, revenue-generating businesses where the Founder makes direct budget decisions.
   * **70%+ Commercial Mix:** Growing D2C brands (apparel, bespoke fashion, jewelry, beauty, specialty F&B, home/lifestyle), multi-outlet clinics (dental, dermatology, aesthetics, wellness), luxury hospitality, and real estate developers.
   * **Up to 30% Design-Build Mix:** Tech-forward architecture, interior design, and turnkey design-build studios.
   * **Automatic Disqualification:** Skip ₹500Cr+ conglomerates, public companies, heavily funded unicorns with large in-house engineering teams, zero-budget student ideas, and "looking for unpaid co-founder" posts.

---

## 2. The Outreach ROI Sanity Gate (Before Presenting Any Lead)

Before presenting a lead to the user, verify:
1. **Is this company already in `memory/DO_NOT_CONTACT.md`?** If yes, skip immediately.
2. **Does this business have clear revenue and commercial activity?**
3. **Do we have a direct path to the Founder/CEO** (verified `firstname@companydomain.com` email, direct mobile/office number, or active personal LinkedIn/Instagram)?
4. **3 Founder Inbox Signals (For Cold Email):**
   * Custom corporate domain backed by live MX records (Google Workspace, Microsoft 365, or Zoho).
   * Active founder presence on LinkedIn or public channels.
   * Clear commercial growth signal (multi-product storefront, custom orders, multi-outlet expansion, or high-ticket services).

---

## 3. Waterfall Scraping Arsenal (How to Find Leads Fast)

Use your connected MCP tools and APIs in this exact sequence:

1. **Broad Discovery (`tavily` / `exa` / `apify`):**
   * Search for founder-led businesses by niche, growth signal, or directory.
   * When mass-scraping phone numbers or regional business directories (for cold calling clinics, hospitality, real estate, design firms, or retail brands), use **Apify** (`APIFY_TOKEN` via `@apify/actors-mcp-server` or Python scripts) to pull structured business listings, websites, and phone numbers.
2. **LinkedIn Warm Lead & Engager Scraping (`linkedin-engager-analytics` + `apify`):**
   * Use Apify no-cookie actors (`scraping_solutions/linkedin-posts-engagers-likers-and-commenters-no-cookies`) to extract Founders and CEOs actively engaging on industry posts.
3. **Website & Storefront Deep-Dive (`firecrawl` / `playwright`):**
   * Scrape the company's `/about`, `/pages/about-us`, `/contact`, and main storefront to identify:
     * Exact Founder / Co-Founder full names.
     * Specific observation about their product craft, custom ordering flow, booking system, or operations.
4. **Automated Email & MX Verification (`scripts/verify_outreach_leads.py`):**
   * Test the founder's custom-domain work email (`firstname@domain.com`) with `python3 scripts/verify_outreach_leads.py` to confirm live MX records and zero banned prefixes (`info@`, `care@`, `support@`, `sales@`, `@gmail.com`).

---

## 4. The One-at-a-Time Lead Presentation Protocol

During live cold calling or outreach sprints:
* **Present strictly ONE lead at a time** unless the user explicitly asks for a batch CSV/table.
* Format each lead card cleanly:
  * **Brand & Website:** `[Brand Name] (https://...)`
  * **Decision Maker:** `[Founder Full Name] - [Exact Title: Founder / CEO / MD]`
  * **Verified Contact:** `[Direct Phone / Verified Custom-Domain Email / LinkedIn URL]`
  * **Why They Fit (Specific Observation):** 1 sentence on how their business operates and where **AIONUS** can add value.
  * **Ready-to-Use Opener / Draft:** Provide the exact phone opener script or validated email/DM draft right below so the user can dial or send immediately.
* Wait for the user to finish calling/messaging that lead and log the result before presenting the next lead.
