# Eric Nowoslawski

Eric Nowoslawski runs Growth Engine X, one of the highest-volume cold email agencies in the market. His SmartLead account alone sent 5.2M emails in a single month; total across all clients approaches 6M/month. He was ranked in the top 3 most-replied-to accounts across SmartLead's entire 90,000+ user base.

---

## Video 1

**Title:** EP 02 Eric Nowoslawski (Growth Engine X): The Ultimate Cold Email Tech Stack (ft. Clay & Smartlead)

**URL:** https://www.youtube.com/watch?v=7ttZEC6khZ0

**Channel:** Smartlead — Behind the Agency Podcast

**Date:** September 19, 2025

### Transcript Summary

- Eric's agency is purely top-of-funnel outbound — sending cold emails at scale and generating hand-raisers. He does not use CRM in the traditional sense; CRM is passed to clients. The entire operation is built around Clay (enrichment + personalisation) and SmartLead (sending + deliverability management), in sequence.

- **Actual volume:** Eric's SmartLead account sent **5.2M emails in a single month**. Across all clients, the total approaches **6M emails/month**. (The 1.5M figure in earlier summaries was outdated or referred to a subset.)

- **Three-stage data pipeline at scale:**
  1. **Staging** — a $15/month HubSpot account acts as a data warehouse. For large clients with 800K+ potential contacts, data from Apollo or LinkedIn scrapes is loaded into HubSpot first (up to 15M contacts allowed). A property marks whether each contact has been processed. Clay's automated scheduling pulls batches of 50,000 records from HubSpot for enrichment.
  2. **Enrichment** — Clay processes the staged data: company enrichment first (to avoid redundant lookups), then people enrichment. Clay's derived data points (pricing structure, B2B/B2C classification, company description) are often more accurate for targeting than Apollo's native filters.
  3. **Production** — SmartLead handles all sending, inbox rotation, and deliverability management.

- **Superbase caching layer:** All enrichment and email verification data is cached in a Superbase (Postgres) database. This prevents paying for the same lookups repeatedly. Before verifying any email, Eric's system first checks Superbase: "Have we verified this email in the last 90 days? Does the domain still match?" If yes, skip the verification cost. If no, run the waterfall. This is one of the biggest cost and efficiency unlocks for high-volume agencies.

- **Email verification waterfall (full sequence):**
  1. Check Superbase cache (has this been verified recently?)
  2. **Lead Magic** (fastest, best outputs) — uses a "get cell status" Clay formula to handle failures without re-running the same step
  3. **Prospeo** (OG provider, reliable)
  4. **Million Verifier** (cheap, has top-ups — always the final fallback)
  - If Lead Magic fails due to credit exhaustion, move to Prospeo. If Prospeo fails, move to Million Verifier. The conditional formula is essential — without it, failed steps just loop and burn credits.
  - A separate email-finding waterfall runs for contacts without an Apollo email: Lead Magic → Prospeo → ICPS → Try Kit → Million Verifier final pass.
  - All verified data is written back to Superbase with today's date.

- **AI snippet approach — static prefix + dynamic variable:**
  Eric never generates full emails with AI. Instead, he uses a **static prefix + AI-generated suffix**:
  - Static: *"I saw on your website that you help people with [X]."*
  - The AI only generates the specific variable phrase after the static anchor.
  - He also prompts the AI: *"Do not change this prefix — start your output from this exact phrase."* This controls the sentence shape and improves AI output quality significantly.
  - The more words AI generates freely, the more risk. Keep the AI's generation window as small as possible.

- **Deliverability monitoring system:**
  - Pull any inbox from all campaigns immediately when its SmartLead warm-up reputation score drops below 98%.
  - Every Thursday or Friday, turn on open tracking for all campaigns. Review open rates on Saturday.
  - Target: **above 40% open rate**. If an inbox is getting 15% open rate while others get 60%, pull the 15% inboxes — they're going to spam. Reply rates consistently go up after purging low open-rate inboxes.
  - Rationale for tracking opens despite the Google spam-flag grey bar: the open rate signal is reliable enough — every time Eric has purged low-performing inboxes after open-rate checks, reply rates have improved.

- **Error handling — the #1 thing most agencies miss:**
  In Make.com and n8n workflows, always branch for errors. When a step fails:
  - Pause the entire workflow for 30 seconds
  - Retry the same step
  - On success, continue
  - This prevents silent failures and missing data at scale. Eric says this is the single biggest lesson from building at volume — everything else can be optimised later, but error handling must be built from day one.

- **Domain/inbox rotation at scale:**
  - Aged domains are increasingly important for deliverability.
  - Keep a pool of domains perpetually warming — if things go well, you never need them; if something burns, you have pre-aged replacements ready immediately.
  - Eric does not treat email sequences as sacred. If an inbox gets pulled mid-sequence, he accepts that those leads are lost from that sequence. They will be re-contacted in a future campaign. Getting perfect sequence continuity is not worth the engineering complexity.

### Key Insights

- The HubSpot staging + Clay enrichment + SmartLead sending pipeline is Eric's core architecture — three distinct layers with distinct roles, not interchangeable tools.
- Superbase caching is the primary cost reduction lever at scale — don't pay for the same enrichment twice.
- The static prefix + AI variable technique (not full AI emails) is how Eric achieves personalisation at 6M emails/month without the copy degrading.
- Error handling in automation workflows is the most underrated infrastructure discipline — silent failures compound at volume.
- Open rate monitoring (weekly, inbox-level, with a 40% floor) is his primary deliverability health signal, not bounce rate alone.

---

## Video 2

**Title:** EP04 Eric Nowoslawski (Growth Engine X): What Actually Works — Campaign Breakdowns

**URL:** https://www.youtube.com/watch?v=WmrYeN3GE3w

**Channel:** Smartlead — Behind the Agency Podcast

**Date:** October 14, 2025

### Transcript Summary

- **Core campaign philosophy:** The only thing that reliably boosts reply rates is a **demand-generating offer**. Demand capture offers work but require volume and creativity. If you can frame the offer so that reading it makes someone think "I need this" without already looking for it, everything else gets easier.

- **Demand capture vs. demand generation:**
  - *Demand capture example:* "Do you need bookkeeping services?" Only works for the small % who decided this morning they hate their accountant.
  - *Demand generation example:* "I know you have a bookkeeper, but this new tax bill just changed everything — when did you last get a second opinion on your tax plan?" This creates a reason to act even for people who weren't looking.
  - Some offers are pure demand capture and shouldn't pretend otherwise (e.g., "would you like to sell your business?" — just run volume and find the people who already want to sell).
  - One Schema case study: Eric found that simply saying "you shouldn't need a support page for CSV imports" + linking to their actual support page + offering to remove the need entirely got leads every day — a straight demand-capture offer that worked because the framing was extremely clear and specific.

- **ICP list cleaning — four categories that always sneak in:**
  When targeting any industry, these types of companies will contaminate the list and should be proactively excluded:
  1. Staffing and recruiting firms that list the target industry as their specialty
  2. Management consulting firms serving that industry
  3. SaaS companies serving that industry
  4. Software development agencies serving that industry
  - Additional example: targeting cleaning companies always pulls in property management companies. Targeting banks pulls in fintech vendors. Build exclusion logic before the first send.

- **AI for list cleaning — where it works and where it doesn't:**
  - Works well: classifying whether a company sells a physical product (e.g., "does this website sell an e-commerce product?")
  - Doesn't work well: fine-grained industry classification ("is this a jewelry company vs. a retail store vs. a coffee brand?") — keyword search is faster and more accurate for that
  - Tool workflow: Zenrows or Janie to pull website markdown → 03-mini or OSS-20B via Open Router to answer a binary classification question

- **Three starter campaigns Eric runs for every new client:**
  1. **Creative ideas campaign:** Three bullet-point ideas showing specifically how you could help their company. Gives you three shots at different value propositions and surfaces which angle resonates.
  2. **Lookalike campaign:** Reference a strong case study from a company similar to theirs. *"We just placed [person] at [company] — they were the first non-Korean executive in the C-suite. We're reaching out to similar companies."* Lookalike relevance transfers.
  3. **New hire / new role campaign:** Target recently hired leaders who are looking to make changes and try new things. Highly reliable trigger — new hires are specifically motivated to demonstrate value.

- **Campaign onboarding questions — the three Eric always asks:**
  1. *"If you researched a prospect for 10 minutes, what would you be looking for — and how would it change your messaging?"*
  2. *"What can you say in an outbound email that your competitors can't say?"*
  3. *"If you were at a conference with your perfect ICP and could capture them with one feature or insight, what would make their ears perk up?"*

- **Secureframe case study (persona-specific messaging):**
  Same product, three completely different campaign opening arguments:
  - CTO → speed to compliance
  - CFO → cost of hiring an internal compliance team vs. using Secureframe
  - VP of Engineering → integration depth and engineering lift
  None of the three emails mentioned the product name. Each started from a different buyer problem, not a shared company description.

- **Website Closers case study (spam filter diagnosis):**
  A competitor keyword in the subject line was triggering spam filters. Switching to a problem-led subject line — no competitor mention, same email body — reduced spam placement by 60% with no other changes.

- **QA checklist before every campaign launches:**
  - Deliverability score per inbox
  - Spam-word scan on all copy
  - Preview text rendering check in both Gmail and Outlook
  - Manual review of 10 randomly sampled personalised emails — this catches AI output errors that aggregate dashboards never surface (e.g., wrong company name, hallucinated detail, broken sentence)

- **A/B testing priority order:**
  1. Offer angle first (minimum 500 sends before concluding)
  2. Subject line
  3. Opening sentence
  4. CTA last
  - Testing copy before the offer is proven optimises the wrong layer. If the offer is wrong, the best subject line in the world won't save the campaign.

- **Compliance approach:**
  Eric follows the client's compliance framework exactly, without giving legal opinions. One area of nuance: he argues that including an unsubscribe link in cold email is counterproductive because enterprise IT departments train employees never to click links in unsolicited emails — so the "opt-out link" is itself a spam signal. If a client insists on the link, Eric complies and explains his reasoning once.

- **Content marketing as the primary agency growth lever:**
  Eric gets most of his inbound through LinkedIn content — 100K+ impressions per week, posting twice daily, scheduling in 90-minute Friday batches. He considers it ironic that an outbound agency grows through inbound, but reputation matters in a market where the barrier to entry is zero. Content is the differentiation.

### Key Insights

- Campaign architecture is a ranked hierarchy: ICP/list → offer → copy → test. Collapsing stages makes failure variables unknowable.
- The three starter campaigns (creative ideas, lookalike, new hire) are repeatable for any client in any vertical — they're Eric's default starting point, not edge cases.
- Persona-specific messaging is structural (different opening argument per buyer type), not just tonal (same message, different adjectives).
- The four ICP list contamination categories are consistent across industries — build exclusion logic into every campaign from day one.
- Manual QA of 10 randomly sampled personalised emails before launch is the only reliable way to catch AI personalisation errors at scale.

---

## Why These Two?

Video 1 covers the technical infrastructure that makes scale possible: the three-stage pipeline (HubSpot staging → Clay enrichment → SmartLead sending), Superbase caching, the email verification waterfall, the static-prefix AI approach, deliverability monitoring, and error handling. Video 2 covers what to put through that infrastructure: demand gen vs. capture framing, starter campaign types, ICP exclusion logic, persona-specific messaging, QA checklists, and A/B testing sequencing. Together they give a complete picture of how Eric builds and runs cold email systems that produce results at 6M emails/month.