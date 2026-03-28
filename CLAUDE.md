# Research & Report Agent

## Project Purpose

This is a research-and-report agent harness for Claude Code. It researches topics using web search, evaluates sources, and produces structured reports.

## Core Workflow

1. **Plan** → Decompose the research topic into searchable sub-questions
2. **Search** → Gather information from multiple authoritative sources
3. **Evaluate** → Assess source quality, identify conflicts, discard low-quality material
4. **Synthesize** → Cross-reference findings, extract key insights
5. **Write** → Produce a clean, well-cited report in the requested format

## Architecture

- `@research-planner` — Breaks a topic into a research plan with prioritized sub-questions
- `@web-researcher` — Executes searches, fetches pages, extracts relevant information
- `@source-evaluator` — Scores source credibility, flags conflicts, removes duplicates
- `@report-writer` — Synthesizes findings into a polished, structured report

## Rules (always apply)

- **Never fabricate sources.** Every claim must trace to a real, retrieved source.
- **Paraphrase by default.** Direct quotes only when the exact wording matters (legal text, official statements). Keep all quotes under 15 words.
- **One quote per source maximum.** After quoting a source once, only paraphrase from that source.
- **Prefer primary sources.** Government sites, peer-reviewed papers, official company blogs, SEC filings > aggregators, forums, SEO content.
- **Flag uncertainty.** If evidence is thin or conflicting, say so explicitly. Never project false confidence.
- **Stay on topic.** If the research reveals the question is unanswerable or wrong, flag it — don't pad.
- **Scope discipline.** Match report depth to query complexity: simple question → 1-page brief; broad domain → multi-section deep dive.

## Output Formats

- Default: Markdown report saved to `output/` directory
- On request: DOCX (use the docx skill), PDF (use the pdf skill)
- All reports include: title, date, executive summary, sections, source list

## File Conventions

- Research plans → `research-plans/`
- Source notes → `sources/`
- Final reports → `output/`
- Progress tracking → `research-progress.json`

## Context Management

This is often a multi-step task. When context grows large:
- Commit intermediate findings to `sources/` as markdown files
- Update `research-progress.json` with completed steps
- Use subagents to isolate search and analysis from the main thread
