# AIONUS Autonomous Sales & Growth Agent Setup (`aionus-growth-agent`)

Welcome to the official **AIONUS** Growth & Sales AI Workspace for **Google Antigravity 2.0**.

If you are a human team member, you do **not** need to set this up manually. Simply open Google Antigravity, paste the one-sentence command below into chat, and let your AI set everything up for you:

```text
Clone https://github.com/Hashim1404/aionus-growth-agent into my workspace, read README.md, and run the interactive setup wizard for me.
```

---

## Instructions for the Antigravity AI Agent (Run This Automatically)

When the user asks you to set up this repository, **execute the 5 steps below interactively**. Do not skip any step, and do not guess the user's answers.

### Phase 1: Interactive Personalization Interview (Ask the User First)
Greet the user warmly and ask them these **6 quick questions** (wait for their reply before proceeding to Phase 2):

1. **Your Name & My AI Name:** *"What is your full name, and what would you like to name me (your AI partner)?"*
2. **Your AIONUS Role Title:** *"What title should appear in your outreach signature (e.g., Growth Partner at AIONUS, Business Development Executive at AIONUS, Founder's Office at AIONUS)?"*
3. **Your Contact Details:** *"What phone number and email address should go in your outreach signatures?"*
4. **Your Operating System:** *"Are you running macOS, Windows, or Linux?"*
5. **Your Focus Channels:** *"Which outreach channels will you use most (Cold Calling, Cold Email, LinkedIn, Instagram DMs)?"*
6. **Personal Goals & Preferences:** *"Alongside our main AIONUS outreach and cold calling work, how do you like to communicate, and what personal skills, daily tasks, or growth areas would you like me to help you with?"*

---

### Phase 2: Free-Tier Scraping & Reporting API Keys Setup
Once the user answers Phase 1, ask them to share any of the following **free API keys** they have (if they do not have one yet, give them the direct signup link and help them grab it in 60 seconds, or set up what they have now and add the rest anytime):

1. **Apify API Token (`APIFY_TOKEN`) - Compulsory for Mass Scraping & Cold-Call Phone Numbers:**
   * Free $5/month credit (no credit card required): `https://console.apify.com/sign-up` (Settings -> Integrations -> API Token).
   * Used for mass-scraping Google Maps, company directories, phone numbers, and LinkedIn posts/comments/engagers.
2. **AgentMail API Key (`AGENTMAIL_API_KEY`) - For Automatic Email Handoffs to Rias (`rias@agentmail.to`):**
   * Free signup: `https://console.agentmail.to`
   * Allows your AI to automatically email Warm Lead Handoffs and End-of-Day summaries straight to **Rias** (`rias@agentmail.to`), Hashim's Executive AI Partner. *(Alternatively, you can also use a Gmail App Password via `SMTP_EMAIL` and `SMTP_APP_PASSWORD` in `.env`.)*
3. **Tavily Search API Key (`TAVILY_API_KEY`):**
   * Free 1,000 searches/month: `https://app.tavily.com`
4. **Exa Search API Key (`EXA_API_KEY`):**
   * Free $10 credit: `https://dashboard.exa.ai`
5. **Firecrawl API Key (`FIRECRAWL_API_KEY`):**
   * Free 500 website scrapes: `https://www.firecrawl.dev`
6. **Optional LinkedIn Auto-Poster (`PUBLORA_API_KEY`):**
   * Free 15 LinkedIn posts/month: `https://app.publora.com/signup` *(Not required if pasting LinkedIn drafts manually).*

**Action for AI in Phase 2:**
* Save the user's keys into `.env` in the workspace root (`APIFY_TOKEN`, `AGENTMAIL_API_KEY`, `AGENTMAIL_INBOX_ID`, `TAVILY_API_KEY`, `EXA_API_KEY`, `FIRECRAWL_API_KEY`, `PUBLORA_API_KEY`).
* Read `mcp_config.template.json`, insert the user's API keys, and write it to the Antigravity MCP config path:
  * **macOS / Linux:** `~/.gemini/antigravity/mcp_config.json`
  * **Windows:** `%USERPROFILE%\.gemini\antigravity\mcp_config.json`

---

### Phase 3: Personalize `AGENTS.md` & Sync Global Rules
1. Open `AGENTS.md` in this workspace and replace all placeholders (`{{AI_NAME}}`, `{{USER_NAME}}`, `{{USER_ROLE}}`, `{{USER_PHONE}}`, `{{USER_EMAIL}}`, `{{USER_OS}}`, `{{PERSONAL_GOALS}}`) with the user's exact answers from Phase 1.
2. Copy the personalized `AGENTS.md` to the global Antigravity rules folder so your identity is active everywhere:
   * **macOS / Linux:** `~/.gemini/config/rules/AGENTS.md`
   * **Windows:** `%USERPROFILE%\.gemini\config\rules\AGENTS.md`

---

### Phase 4: Verify Scripts & Dependencies
1. Test the lead validator script to confirm DNS/MX lookup works on the user's OS:
   ```bash
   python3 scripts/verify_outreach_leads.py --email founder@shopify.com
   ```
2. Install the lightweight Python `requests` package if needed by the LinkedIn helper scripts:
   ```bash
   pip install requests
   ```

---

### Phase 5: AIONUS 60-Second Briefing & Ready Check
Once Phases 1 to 4 are complete, read `AIONUS_KNOWLEDGE_BASE.md` and give the user a crisp **60-second welcome briefing**:
1. Introduce yourself by your new name (`{{AI_NAME}}`).
2. Summarize what **AIONUS** does in plain English, who we target (**Founders, Co-Founders, CEOs, Owners, and Managing Directors ONLY** at 5 to 50 employee commercial businesses), and remind them that **all pricing questions are escalated to a 10-minute call with Hashim**.
3. Explain that they **never need to write prompts**: they can just talk to you naturally:
   * *"Find me a lead to call in [industry]"*
   * *"Give me a cold call script for this company"*
   * *"Draft a cold email / Instagram DM / LinkedIn message for this founder"*
   * *"Practice a 2-minute mock cold call with me"*
   * *"This founder is interested!"* (automatically emails Rias at `rias@agentmail.to` + makes a WhatsApp card for Hashim)
   * *"Wrap up my day"* (automatically emails the daily report to `rias@agentmail.to` + makes a 4-line WhatsApp summary)
4. Ask them: *"Would you like to do a quick 2-minute mock cold call roleplay to warm up, or should we scrape your first live lead right now?"*
