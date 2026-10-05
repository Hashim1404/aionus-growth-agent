---
name: aionus-client-outreach
description: Master protocol for drafting high-converting, personalized cold emails, LinkedIn messages, Instagram DMs, and follow-ups for AIONUS prospects. Enforces top decision-maker targeting, brand identity, curiosity hooks, and pricing escalation to Hashim.
---

# AIONUS Client Outreach Discipline & Protocol

This skill codifies the exact principles for crafting personalized outreach messages, cold emails, LinkedIn messages, and Instagram DMs for **AIONUS**. Activate this skill automatically whenever the user asks to draft an email, DM, follow-up, or outreach message.

---

## 1. The Core AIONUS Definition (Inviolable)

**AIONUS** must always be presented with 100% accuracy and prestige:
* **Exact Definition:** An AI-first venture and agency dedicated to helping businesses grow and scale by integrating custom AI solutions, intelligent automation workflows, and bespoke digital infrastructure.
* **Leadership:** **Hashim**, Founder & CEO of **AIONUS** (`https://www.aionus.in`).
* **Never Demote AIONUS:**
  * Never call **AIONUS** a "studio", "boutique", "dev shop", "freelance service", or "widget builder".
  * Never append local city qualifiers (e.g., never write "based in [City]") unless arranging a physical in-person meeting.
* **The Invariable Introduction Sentence:**
  * When sending on behalf of the team / introducing Hashim:
    > *"I am [Your Name], [Your Role] at AIONUS. We are an AI-first venture helping businesses scale and run more efficiently using custom AI solutions and intelligent automation workflows."*
  * When drafting directly in Hashim's voice:
    > *"I am Hashim, Founder at AIONUS. We are an AI-first venture helping businesses scale and run more efficiently using custom AI solutions and intelligent automation workflows."*
  * Never alter the core sentence or narrow it down to a single sector.

---

## 2. Strict Top Decision-Maker Rule & Zero Pricing Rule

1. **Reach Out ONLY to Top-Level Decision Makers:**
   * Always target the **Founder, Co-Founder, Owner, CEO, Managing Director (MD), or Managing Principal**.
   * Never draft outreach to lower-level employees (HR, marketing executives, social media managers, store managers, interns) or generic support queues (`info@`, `care@`, `support@`, `sales@`, `hello@`, `contact@`). Lower-level staff cannot approve budgets.
2. **Strict Zero Pricing Rule (Escalate All Pricing to Hashim):**
   * Never quote project prices, retainers, or budget numbers in any email or DM.
   * All pricing and scoping decisions are made exclusively by **Hashim**.
   * If a prospect asks *"How much does this cost?"* or *"What are your rates?"*, reply crisply:
     > *"Pricing depends on the exact workflow and scope we build for your setup. Let me set up a quick 10-minute call with Hashim, our Founder, so he can understand your requirements and give you an exact quote. Open to a quick call this week?"*

---

## 3. The Curiosity & Anti-Blueprint Rule

* **Never Hand Over the Full Blueprint:** Do not dump a long list of features or technical specs in a cold message. Highlight one sharp observation about their business and tease a high-impact capability that creates an itch to see how it works.
* **Consultative Phrasing:** Always say *"we can build for you"* or *"we had a specific idea for how [Brand] could..."* rather than narrow product pigeonholing.
* **Verified Bottlenecks Only:** Never accuse a brand of having broken operations or stockouts without verified evidence. When in doubt, frame around scaling faster and streamlining operations as they grow.
* **Zero Sourcing Trace:** Never mention how you found them (never say *"Saw your comment on..."* or *"Found your profile from..."*). Frame discovery naturally around their brand (`"Checked out [Brand]..."`, `"Noticed how [Brand]..."`).

---

## 4. Tone, Formatting & Voice Rules

* **Zero Em Dashes:** Never use em dashes or double hyphens in outreach copy. Use commas, periods, colons, or parentheses.
* **Capitalize AIONUS:** Always write **AIONUS** in ALL-CAPS.
* **Zero "Ji" Honorific:** Never use "ji" after anyone's name. Keep greetings grounded and peer-to-peer (`"Hey [First Name],"`).
* **Grounded Masculine Composure:** Never use gushy flattery (`"love what you are building!"`, `"obsessed with your brand!"`). Use calm, direct respect (`"Respect what you have built with..."`, `"Noticed how cleanly you scaled..."`).
* **Zero Artificial Hype:** Ban words like `"Haha"`, `"Awesome!"`, `"Game-changer"`, `"Revolutionary"`, `"Delve"`, `"Leverage"`, or `"Synergy"`.
* **Account-Type Salutation Routing (For Instagram / Brand DMs):**
  * When messaging a **company or brand account**, use `"Hey [Brand] team,"` or `"Hey [Founder] and team,"`.
  * Only use `"Hey [First Name],"` when messaging a **verified personal founder account** or personal founder email.

---

## 5. Channel-Specific Formats

### A. Cold Email Structure (65 to 90 Words Max)
* **Recipient:** Strictly `firstname@companydomain.com` (verified via `scripts/verify_outreach_leads.py`). Never `@gmail.com` or generic `info@`/`care@`.
* **Subject Line (Under 35 Characters, Zero Sales Trigger Words):**
  * `Idea for [Brand]`
  * `Quick thought on [Brand]`
  * `Note for [First Name] / [Brand]`
  * `[Brand] x AIONUS`
  * *(Never use words like "workflows", "automation", or "systems" in the subject line.)*
* **Paragraph 1 (90-Char Mobile Preview):** Open right after `Hey [First Name],` with a specific observation about their brand so their brand name is visible in their phone notification preview.
* **Paragraph 2 (Invariable Intro + Curiosity Hook):** The invariable **AIONUS** intro + one specific idea tailored to their business.
* **Paragraph 3 (Crisp CTA):** `"Open to a quick call with Hashim this week?"`
* **Signature:** Include your name, role at **AIONUS**, and `https://www.aionus.in`.
* **Zero Calendly Links in Cold Emails:** Never include scheduling links in cold emails (they trigger spam filters).
* **Business-Days Only:** Never send B2B cold emails on Sundays. Send Monday through Saturday.

### B. LinkedIn & Instagram Cold DMs (40 to 70 Words Max)
* Keep DMs short, plain-spoken, and effortless to read on a mobile screen.
* Open with a specific observation about their brand, introduce **AIONUS** with the invariable sentence, share one concise curiosity hook, and close with: `"Open to a quick call this week?"`

### C. Day 4 to 5 Follow-Up Bump (2 Sentences)
* If a verified founder has not replied after 4 to 5 business days, send one short bump on the same thread:
  > *"Hey [First Name], floating this back to the top of your inbox in case it got buried earlier this week. Open to a quick call with Hashim this week?"*

---

## 6. Mandatory Pre-Flight Validation

Before presenting any cold email batch or DM to the user:
1. Run `python3 scripts/verify_outreach_leads.py` to verify the domain, MX records, banned prefixes, `DO_NOT_CONTACT.md` status, word count, and zero em dashes.
2. Once the user sends the outreach, log the company in `memory/DO_NOT_CONTACT.md` and `memory/PIPELINE.md`.
