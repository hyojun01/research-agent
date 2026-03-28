---
name: deep-research
description: Orchestrates a full research-and-report workflow. Use when the user asks to "research", "investigate", "write a report on", "deep dive into", "analyze the landscape of", or any request requiring multi-source research and a written deliverable. Also trigger when user says "find out about", "what's the state of", or "give me a comprehensive overview of".
---

# Deep Research Skill

Orchestrate a complete research workflow from topic to finished report.

## Workflow

### Phase 1: Planning
Invoke the `@research-planner` subagent with the user's topic. The planner produces a research plan in `research-plans/`.

Before proceeding, review the plan. If the topic is too broad, surface this to the user and recommend narrowing.

### Phase 2: Research
For each sub-question in the plan, invoke `@web-researcher` with:
- The specific sub-question
- The suggested search queries from the plan
- The preferred source types

Save results to `sources/sq-{N}-{slug}.md`.

Update `research-progress.json` after each sub-question:
```json
{
  "topic": "...",
  "status": "researching",
  "plan": "research-plans/plan-{slug}.md",
  "sub_questions_total": 5,
  "sub_questions_completed": 3,
  "current_step": "SQ4: ...",
  "sources_collected": 12
}
```

### Phase 3: Evaluation
Once all sub-questions are researched, invoke `@source-evaluator` to:
- Score all collected sources
- Resolve conflicts
- Produce `sources/evidence-summary.md`

If the evaluator flags low overall confidence, consider running additional searches on weak areas before proceeding.

### Phase 4: Writing
Invoke `@report-writer` with:
- The evidence summary
- The user's requested format (default: markdown)
- The scope (brief/standard/deep)

The writer produces the final report in `output/`.

### Phase 5: Delivery
Present the finished report to the user. Offer:
- DOCX conversion (via docx skill if available)
- PDF conversion (via pdf skill if available)
- Scope adjustment (deeper or narrower)

## Scope Calibration

| User Signal | Scope | Expected Time |
|-------------|-------|---------------|
| Simple factual question | Brief | 2-3 min |
| "Write me a report on X" | Standard | 5-10 min |
| "Deep dive" / "comprehensive" / "thorough" | Deep | 10-20 min |

## Error Handling

- If web search returns no useful results for a sub-question, log it and move on. Don't block the entire workflow.
- If more than half the sub-questions yield no results, alert the user that the topic may be too niche or recent for web research.
- If a fetch fails (paywall, 404), note the failure and try alternative sources.
