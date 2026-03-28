---
name: source-analysis
description: Evaluates the credibility and relevance of research sources. Use when the user asks to "check sources", "verify claims", "assess credibility", "fact-check", or when source quality needs evaluation before report writing. Also triggers on "is this reliable" or "can I trust this source".
---

# Source Analysis Skill

Evaluate sources for credibility, bias, recency, and relevance.

## Credibility Assessment Framework

### Tier 1 — Primary Sources (Score 5)
Government statistical agencies, central bank data, peer-reviewed journals, court filings, SEC filings, patent records, official specifications, direct participant testimony.

**Signal:** The source generated or collected the data itself.

### Tier 2 — Authoritative Secondary (Score 4)
Major news outlets with original reporting (Reuters, AP, Bloomberg, NYT, WSJ), established research firms (Gartner, McKinsey, Pew), recognized industry analysts, university research reports.

**Signal:** Professional editorial standards, named authors, cited sources within their reporting.

### Tier 3 — Reputable Aggregator (Score 3)
Well-known publications summarizing others' work, expert blogs with citations, trade press with editorial oversight, Wikipedia (for non-controversial topics with good citations).

**Signal:** Aggregates but adds analysis; traceable to primary sources.

### Tier 4 — Mixed Quality (Score 2)
Trade publications without clear sourcing, company blogs mixing data with marketing, survey-based content with unclear methodology, opinion pieces presented as analysis.

**Signal:** Some useful data but motivations are mixed or unclear.

### Tier 5 — Unreliable (Score 1)
Anonymous blogs, SEO-optimized content farms, undated articles, press releases without independent verification, social media posts, forums, AI-generated content without attribution.

**Signal:** No editorial oversight, no cited sources, possible financial motivation.

## Bias Indicators

Check for these red flags:
- Source is funded by an entity with a stake in the conclusion
- Language is promotional rather than analytical
- Counterarguments are absent or dismissed without engagement
- Data is cherry-picked (narrow date ranges, selective metrics)
- The same claim appears across many sites but traces to a single origin

## Recency Rules

| Topic Type | Maximum Source Age |
|------------|-------------------|
| Technology, startups, AI | 6 months |
| Policy, regulation | 12 months |
| Market data, economics | 12 months |
| Science, medicine | 2 years (unless foundational) |
| History, established facts | No limit |

## Conflict Resolution Checklist

When sources disagree:
1. Which source is closer to the primary data?
2. Which is more recent?
3. How many independent sources support each side?
4. Is the disagreement factual or interpretive?
5. Does either source have a clear conflict of interest?
6. Can both be true (different methodologies, definitions, or time periods)?

Document the resolution or mark as "unresolved — present both sides."
