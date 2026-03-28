---
globs: ["output/**"]
---

# Output Formatting Rules

These rules apply to all files in `output/`.

## Structure

- Every report must include: title, date, executive summary, at least one findings section, and a sources list
- Executive summary must stand alone — a reader who stops there should still be informed
- No section heading without at least one paragraph beneath it
- Heading hierarchy must be strict: H1 > H2 > H3, never skip levels

## Prose

- Write in paragraphs, not bullet-point lists
- Active voice by default
- Concrete language: numbers, dates, names — not vague qualifiers
- No filler phrases: "It is important to note", "It should be mentioned", "Interestingly"
- No padding with obvious statements

## Formatting

- Use `---` horizontal rules only to separate the metadata block from the body
- Bold only for the report metadata fields (Date, Confidence, Scope)
- No excessive bold, italic, or emphasis in the body text
- Tables only when comparing 3+ items across 3+ dimensions

## Confidence Statement

Every report must include a confidence level (high / medium / low) based on:
- **High:** Multiple independent, high-credibility sources agree; recent data available
- **Medium:** Sources are credible but limited in number or recency; some gaps exist
- **Low:** Few sources available, significant conflicts, or topic is too recent for reliable data
