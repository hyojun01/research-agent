# Research & Report Agent — Claude Code Harness

An agent harness for Claude Code that researches topics using web search, evaluates sources, and produces structured reports.

## Architecture Overview

```
research-agent/
├── CLAUDE.md                          # Project-level system prompt (loaded every session)
├── research-progress.json             # Work state tracker (cross-session continuity)
├── .claude/
│   ├── settings.json                  # Permissions and tool configuration
│   ├── agents/                        # Subagents (isolated context windows)
│   │   ├── research-planner.md        # Topic → research plan decomposition
│   │   ├── web-researcher.md          # Web search and source collection
│   │   ├── source-evaluator.md        # Source credibility scoring and conflict resolution
│   │   └── report-writer.md           # Evidence → polished report
│   ├── skills/                        # Skills (on-demand prompt expansion)
│   │   ├── deep-research/             # Full research pipeline orchestration
│   │   │   ├── SKILL.md
│   │   │   ├── scripts/
│   │   │   │   └── extract_sources.py # Source extraction/deduplication utility
│   │   │   └── references/
│   │   │       └── report-template.md # Report templates (Brief/Standard/Deep)
│   │   ├── source-analysis/           # Source credibility evaluation framework
│   │   │   └── SKILL.md
│   │   └── report-formatting/         # Output formatting and style guide
│   │       ├── SKILL.md
│   │       └── references/
│   │           └── style-guide.md     # Prose quality standards
│   ├── commands/                      # Slash commands (entry points)
│   │   ├── research.md                # /research — full pipeline
│   │   └── quick-brief.md            # /quick-brief — fast summary
│   └── rules/                         # Reference rule documents (loaded as project instructions)
│       ├── citation-standards.md      # Cited by agents writing to output/**, sources/**
│       ├── source-quality.md          # Cited by agents writing to sources/**
│       └── output-formatting.md       # Cited by agents writing to output/**
├── research-plans/                    # Research plan storage
├── sources/                           # Collected source notes
├── output/                            # Final report output
└── docs/
    └── architecture.md                # Architecture design document
```

## Key Concepts

### 1. CLAUDE.md — Always-loaded project context

Loaded into the system prompt at the start of every session. Defines the project's purpose, core rules, workflow, and file conventions. Kept concise at under 200 lines.

### 2. Subagents — Isolated context windows

Each subagent runs in its own separate context window:
- **research-planner**: Decomposes a topic into searchable sub-questions
- **web-researcher**: Executes web searches, collects sources, writes structured notes
- **source-evaluator**: Scores source credibility, resolves conflicts, consolidates evidence
- **report-writer**: Transforms the evidence summary into a polished report

Why subagents:
- Preserves main context (isolates exploration/analysis noise)
- Restricts tool access (only web-researcher uses WebSearch/WebFetch)
- Enables parallel processing

### 3. Skills — On-demand prompt expansion

Only the `name` and `description` from SKILL.md are pre-loaded into the system prompt. The actual content loads only when a relevant task triggers it (Progressive Disclosure).

- **deep-research**: Full pipeline orchestration (Planning → Research → Evaluation → Writing)
- **source-analysis**: Source credibility evaluation framework (5-tier scoring)
- **report-formatting**: Output format conversion and audience-specific styling

### 4. Commands — User entry points

```bash
/research AI regulation in the European Union
/quick-brief latest Fed interest rate decision
```

### 5. Rules — Reference constraints

Rule files under `.claude/rules/` are loaded as project instructions alongside `CLAUDE.md` at session start. They are not glob-scoped — Claude Code does not provide that mechanism — but the rule text specifies the directories each rule applies to, and the agents honor those scopes when writing:
- `citation-standards.md` → applies to `output/**`, `sources/**`
- `source-quality.md` → applies to `sources/**`
- `output-formatting.md` → applies to `output/**`

If stricter enforcement is needed, add a `PreToolUse` hook in `settings.json` that inspects the target path.

### 6. research-progress.json — Cross-session continuity

Tracks work state in JSON format. Even when context resets between sessions, the next session can pick up where the previous one left off. JSON is used instead of Markdown because the model is less likely to inappropriately modify or overwrite JSON files.

## Usage

### Installation

```bash
# Extract into your project directory
unzip research-agent.zip -d ~/your-project/

# Or copy only the .claude/ folder into an existing project
cp -r research-agent/.claude ~/your-project/
cp research-agent/CLAUDE.md ~/your-project/
```

### Running

```bash
# Start Claude Code
cd ~/your-project
claude

# Run full research
> /research the current state of quantum computing

# Quick summary
> /quick-brief NVIDIA earnings Q4 2025

# Directly invoke a specific subagent
> @research-planner break down the topic of AI safety regulation
```

## Design Principles

1. **Simple agent, rich context**: Single agent loop + rich context engineering
2. **Progressive disclosure**: Load only the context needed, when it's needed
3. **Incremental progress**: Process one sub-question at a time, save state after each step
4. **Verification loop**: Search → Evaluate → Write → Quality check
5. **Context isolation**: Subagents isolate exploration/analysis noise from the main thread

## Reference Materials

- [Effective Harnesses for Long-Running Agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) — Anthropic
- [Building Agents with the Claude Agent SDK](https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk) — Anthropic
- [Equipping Agents for the Real World with Agent Skills](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) — Anthropic
- [Skill Authoring Best Practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) — Anthropic Platform Docs
- [Claude Code Subagents](https://code.claude.com/docs/en/sub-agents) — Claude Code Docs
