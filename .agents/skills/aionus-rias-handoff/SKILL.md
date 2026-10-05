---
name: aionus-rias-handoff
description: Automated Agent-to-Agent bridge that emails Rias (rias@agentmail.to) and generates a WhatsApp summary card whenever a founder is interested/books a call (Warm Lead Handoff) or when the user wraps up their workday (End-of-Day Report).
---

# AIONUS Agent-to-Agent Handoff & Daily Reporting Protocol (`rias@agentmail.to`)

Activate this skill **immediately and automatically** in two situations:
1. **Warm Lead / Interested Founder Handoff:** Whenever the user says anything like *"We got this"*, *"This founder is interested"*, *"He agreed to a call"*, *"She wants to talk to Hashim"*, *"Book this lead"*, or *"Send handoff"*.
2. **End-of-Day Activity Summary:** Whenever the user says *"Wrap up my day"*, *"Send daily report"*, *"Done for today"*, or *"Send EOD summary"*.

---

## 1. Recipient Details (Rias - Executive AI Partner to Hashim)

* **Destination Email:** `rias@agentmail.to`
* **Purpose:** Rias monitors `rias@agentmail.to` directly inside Hashim's command center. The moment your AI sends an email to `rias@agentmail.to`, Rias receives it, parses the structured data, updates Hashim's master pipeline, and briefs Hashim immediately.

---

## 2. Mode A: Instant Warm Lead Handoff (`--mode handoff`)

The moment a Founder/CEO shows interest, asks for a call with Hashim, or replies positively:

1. **Gather the 6 Core Handoff Fields** (ask the user if any detail is missing):
   * **Company Name & Website:** e.g., `Acme Studio (https://acmestudio.in)`
   * **Decision Maker Name & Title:** e.g., `Rohan Mehta, Founder & CEO`
   * **Direct Contact Info:** Direct Phone Number + Verified Email + LinkedIn/Instagram URL
   * **Channel Used:** Cold Call / Cold Email / LinkedIn DM / Instagram DM
   * **Context & Bottleneck Discussed:** Exactly what was discussed, what caught their interest, and any questions they asked
   * **Proposed Call Time with Hashim:** Date/time window the founder prefers

2. **Dispatch the Automated Email to `rias@agentmail.to`:**
   * If the `agentmail` MCP tool is connected, call `send_message` to `rias@agentmail.to` with Subject `[AIONUS HANDOFF] {Company Name} - {Founder Name} (via {Operator Name})`.
   * Or run the built-in Python dispatcher:
     ```bash
     python3 scripts/report_to_rias.py --mode handoff \
       --operator "YOUR_NAME" \
       --company "COMPANY_NAME" \
       --website "https://..." \
       --founder "FOUNDER_NAME_AND_ROLE" \
       --contact "PHONE / EMAIL / LINKEDIN" \
       --channel "Cold Call / Email / LinkedIn / IG" \
       --notes "EXACT_CONTEXT_AND_PAIN_POINTS" \
       --call-time "PROPOSED_TIME"
     ```

3. **Update Local Pipeline:**
   * Update the lead's status in `memory/PIPELINE.md` to `WARM - HANDED OFF TO RIAS & HASHIM`.

4. **Display the Backup WhatsApp Card for Hashim:**
   * Always output the clean copy-paste WhatsApp card in chat as well so the user can drop it in Hashim's WhatsApp if urgent:
     ```text
     *AIONUS WARM LEAD HANDOFF*
     • *Company:* [Company Name] ([Website])
     • *Founder:* [Name], [Title]
     • *Direct Contact:* [Phone] | [Email]
     • *Channel:* [Channel]
     • *Context / Interest:* [Summary of what they want & why they agreed]
     • *Proposed Call Time:* [Day & Time]
     *(Full context also emailed to Rias at rias@agentmail.to)*
     ```

---

## 3. Mode B: End-of-Day Activity Summary (`--mode eod`)

When the user finishes their work session or says *"Wrap up my day"*:

1. **Read `memory/PIPELINE.md` & Today's Session Activity:**
   * Count total leads scraped/verified today.
   * Count total cold calls dialed, emails sent, LinkedIn comments/DMs, and Instagram DMs sent.
   * List every company contacted today, their decision-maker name, channel, status, and any warm replies or follow-ups scheduled.

2. **Dispatch the Automated EOD Email to `rias@agentmail.to`:**
   * Send via `agentmail` MCP (`send_message` to `rias@agentmail.to`) or run:
     ```bash
     python3 scripts/report_to_rias.py --mode eod \
       --operator "YOUR_NAME" \
       --scraped 15 \
       --calls 10 \
       --messages 12 \
       --warm 2 \
       --details "FULL_MARKDOWN_TABLE_OR_LIST_OF_TODAYS_LEADS"
     ```

3. **Display the 4-Line WhatsApp Summary Card:**
   * Provide a crisp 4-line summary the user can optionally paste on WhatsApp:
     ```text
     *AIONUS Daily Growth Wrap ([Date] - [Operator Name])*
     • Leads Verified: [X] | Calls Dialed: [Y] | Emails/DMs Sent: [Z]
     • Warm Replies / Booked Calls: [W]
     • Full lead log emailed to Rias (rias@agentmail.to).
     ```
