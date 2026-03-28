---
globs: ["sources/**"]
---

# Source Quality Rules

These rules apply to all files in `sources/`.

## Acceptance Criteria

- Only retain sources scoring 3+ on the credibility rubric (see source-analysis skill)
- Score-1 sources are discarded unless they are the sole source for a critical claim (flag this explicitly)
- Score-2 sources may be used for supporting evidence but never as the sole basis for a key finding

## Recency

- For technology, AI, startups: maximum 6 months old
- For policy, regulation, economics: maximum 12 months old
- For science, medicine: maximum 2 years (unless foundational research)
- For history, established facts: no age limit
- Always prefer the most recent credible source when multiple exist

## Deduplication

- If two sources report the same claim, trace to the original and cite that instead
- If a finding appears in 5+ sources, it's likely well-established — cite the 2 strongest and note broad consensus
- Never count copies of the same wire report (AP, Reuters) as independent sources

## Conflicts

- When sources disagree, document both positions with their respective sources
- Never silently pick one side without acknowledging the conflict
- If a conflict cannot be resolved, mark it "unresolved" and present both sides in the report
