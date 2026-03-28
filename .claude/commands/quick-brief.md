---
name: quick-brief
description: Fast research producing a 1-page brief on a focused question
argument-hint: [question]
---

# /quick-brief Command

Produce a short research brief without the full multi-agent pipeline.

## Steps

1. Run 3-5 web searches on the topic directly (no planning subagent needed)
2. Fetch the 2-3 most promising sources for full-page reading
3. Write a brief report (500-1,000 words) directly to `output/brief-{slug}.md`
4. Include an executive summary, key findings (prose, not bullets), and source list

## When to Use

- Simple factual questions: "What is the current market cap of NVIDIA?"
- Narrow topics: "What did the Fed decide at their last meeting?"
- Quick context: "Give me a brief on the CHIPS Act implementation status"

## When NOT to Use

- Broad topics requiring multiple angles → use `/research` instead
- Topics needing source verification → use `/research` instead
- Anything the user calls "deep dive", "comprehensive", or "thorough" → use `/research`

## Quality Bar

Even though this is fast, the brief must:
- Cite every claim with a source
- Use only sources scored 3+ on the credibility rubric
- Flag if the topic is too complex for a brief and suggest `/research`
