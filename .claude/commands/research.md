---
name: research
description: Run a full research-and-report workflow on a given topic
argument-hint: [topic]
---

# /research Command

Execute the full research-and-report pipeline.

## Steps

1. Create working directories if they don't exist: `research-plans/`, `sources/`, `output/`
2. Initialize `research-progress.json` with the topic and timestamp
3. Invoke the `deep-research` skill to orchestrate the full workflow
4. Present the finished report to the user
5. Offer format conversion (DOCX, PDF) if requested

## Usage Examples

```
/research the current state of nuclear fusion energy
/research AI regulation in the European Union 2025
/research competitive landscape for cloud GPU providers
```

## Notes

- For quick, single-question lookups, use `/quick-brief` instead
- The full pipeline typically takes 5-15 minutes depending on scope
- Progress is tracked in `research-progress.json` so work can resume if interrupted
