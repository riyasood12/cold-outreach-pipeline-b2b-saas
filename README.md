# Cold Outreach Pipeline for B2B SaaS

## What This Is

This repository documents how 10 practicing B2B SaaS outbound experts approach cold outreach through LinkedIn content, YouTube videos, podcast appearances, newsletters, and public educational material.

The goal of this project is to identify recurring patterns in modern outbound systems and build a research foundation for a future B2B SaaS cold outreach playbook.

---

## Why These 10 Experts

I selected practitioners rather than commentators — people who actively run outbound campaigns, build outbound software, train sales teams, or operate agencies generating real pipeline through cold outreach.

The experts were grouped into three research pillars:

| Pillar                       | Experts                                                    | Why                                                                                                              |
| ---------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| **Technical Infrastructure** | Eric Nowoslawski, Nick Abraham, Jeremy Chatelaine          | Focus on deliverability, inbox infrastructure, data enrichment, outbound tooling, and scalable campaign systems. |
| **Behavioral Psychology**    | Josh Braun, Will Allred, Florin Tatulea                    | Focus on messaging, prospect psychology, personalization, and response generation.                               |
| **Operational Execution**    | Nick Cegelski, Armand Farrokh, Jason Bay, Morgan J. Ingram | Focus on prospecting systems, cold calling, multichannel outreach, SDR workflows, and pipeline generation.       |

Full rationale for each expert is documented in `research/sources.md`.

---

## Repository Structure

```text
research/

├── sources.md
│   └── Expert selection rationale, roles, platforms, and research pillars

├── linkedin-posts/
│   └── LinkedIn research organized by author
│      (post summaries, dates, URLs, and key takeaways)

├── youtube-transcripts/
│   └── Video and podcast research organized by expert
│      (transcript summaries, URLs, dates, and key insights)

├── other/
│   └── Supplementary research materials
│      (books, newsletters, blogs, and supporting references)

└── insights.md
    └── Synthesized findings across all experts

Scripts/

├── pull_transcripts.py
│   └── Retrieves YouTube transcripts using youtube-transcript-api

└── raw_transcripts/
    └── Transcript files collected from selected YouTube videos
```

---

## Research Methodology

### 1. Expert Selection

Experts were selected based on demonstrated outbound experience rather than audience size. Priority was given to practitioners who:

* Run outbound programs
* Build outbound software
* Train SDR and AE teams
* Publish detailed frameworks and case studies
* Share real-world examples rather than generic advice

### 2. Content Collection

Content was collected from publicly available sources including:

* LinkedIn posts
* YouTube videos
* Podcast appearances
* Newsletters
* Company blogs

Each entry preserves the original source URL so claims can be independently verified.

For YouTube research, transcripts were retrieved using the `youtube-transcript-api` Python library. The repository includes transcript collection scripts and transcript files used to support and validate video research summaries.

### 3. Content Analysis

Each source was reviewed and summarized to capture:

* Outreach frameworks
* Prospecting systems
* Deliverability practices
* Messaging approaches
* Personalization strategies
* Cold calling techniques
* AI and automation workflows

Research was organized by expert to preserve context and make cross-comparison easier.

### 4. Synthesis

Findings were consolidated into recurring themes documented in `research/insights.md`.

The objective was not to collect the most content, but to identify the highest-signal ideas that repeatedly appeared across experienced outbound practitioners.

---

## Research Coverage

### Experts Researched

* 10 outbound practitioners

### LinkedIn Research

* Research completed for all 10 experts
* 50+ LinkedIn post summaries
* Source URLs preserved for verification
* Organized by author

### Video & Podcast Research

* Transcript-supported YouTube and podcast research
* Structured summaries and key insights
* Organized by expert
* Transcript collection performed using `youtube-transcript-api`
* Source URLs preserved for verification

While all 10 experts were researched through LinkedIn content, transcript-based YouTube and podcast research was focused on experts with the strongest availability of long-form educational content.

Several experts on this list primarily publish insights through LinkedIn rather than YouTube or podcast appearances. For those experts, LinkedIn research serves as the primary source of analysis.

Transcript research therefore focuses on:

* Eric Nowoslawski
* Nick Abraham
* Jason Bay
* Josh Braun
* Morgan J. Ingram
* 30MPC (Nick Cegelski & Armand Farrokh)

This approach prioritizes depth and source quality while maintaining coverage across all 10 experts.

### Synthesized Research

* Cross-expert themes
* Common mistakes
* Playbook foundations
* Practical outbound recommendations

---

## Key Findings

A consistent pattern emerged across all 10 experts:

**Cold outreach success is not primarily a copywriting problem.**

The strongest operators treat outbound as a system composed of:

* Deliverability infrastructure
* ICP definition and targeting
* Signal identification
* Offer positioning
* Messaging frameworks
* Multichannel execution
* Continuous testing and optimization

Several experts independently emphasized that poor offers, weak targeting, or broken infrastructure cannot be fixed by better copy alone.

Eight major themes were synthesized and documented in `research/insights.md`.

---

## Key Themes Identified

* Deliverability is infrastructure, not setup
* ICP quality matters more than list size
* Offer quality matters more than copy quality
* Relevance beats superficial personalization
* Signals improve timing and prioritization
* AI should support human judgment
* Multichannel outreach outperforms single-channel outreach
* Successful outbound systems prioritize process over tactics

---

## Status

- Expert selection completed

- LinkedIn research completed

- YouTube and podcast research completed

- Transcript collection implemented using `youtube-transcript-api`

- Research synthesis completed

- Repository organization completed

This repository serves as a research foundation for building a practical B2B SaaS cold outreach playbook.

---

## Future Work

* Expand transcript coverage across additional videos and podcasts
* Re-validate highly specific statistics against source transcripts
* Compare outreach frameworks across industries
* Build a structured outbound playbook
* Create reusable messaging frameworks
* Map expert recommendations into an end-to-end outbound operating system

---

## Acknowledgements

Research synthesized from public content produced by:

* Eric Nowoslawski
* Nick Abraham
* Jeremy Chatelaine
* Josh Braun
* Will Allred
* Florin Tatulea
* Nick Cegelski
* Armand Farrokh
* Jason Bay
* Morgan J. Ingram

All source links are preserved within the repository for verification and further study.