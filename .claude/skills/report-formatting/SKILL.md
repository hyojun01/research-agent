---
name: report-formatting
description: Formats research reports for different output types and styles. Use when the user requests a specific format like "make it a Word doc", "export as PDF", "format for a presentation", or wants the report restyled for a particular audience (executive, technical, general). Also trigger on "clean up the report" or "make it more professional".
---

# Report Formatting Skill

Transform research reports into different formats and styles.

## Supported Output Formats

### Markdown (default)
No conversion needed. Ensure proper heading hierarchy and clean formatting.
Read `references/style-guide.md` for prose and formatting standards.

### DOCX (Word Document)
Delegate to the project's docx skill or use python-docx.
Apply professional formatting: proper margins, heading styles, page numbers, and a cover page.

### PDF
Delegate to the project's pdf skill.
Ensure clean typography and proper page breaks between major sections.

## Audience Adaptation

### Executive
- Lead with the bottom line in the executive summary
- Minimize jargon; define any technical terms used
- Emphasize implications and recommended actions
- Keep total length under 2,000 words when possible
- Use concrete numbers and comparisons

### Technical
- Include methodology details
- Preserve data precision (don't round aggressively)
- Technical terms are fine without definitions
- Include caveats and confidence intervals
- Longer reports are acceptable

### General / Public
- Write at a 10th-grade reading level
- Use analogies and concrete examples
- Avoid acronyms or expand them on first use
- Shorter paragraphs, more whitespace
- Lead with "why should I care" framing

## Quality Checklist (run before delivery)

1. Every section heading is descriptive, not generic
2. Executive summary stands alone — a reader can stop there and be informed
3. No orphan claims — every factual statement has an inline citation
4. No bullet-point lists in the report body (use prose)
5. Sources section is complete and consistently formatted
6. Confidence level and limitations are stated honestly
7. The report answers the original question, not a different one
8. No placeholder text remains
9. Date is correct and prominently placed
