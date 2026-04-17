# Research & Report Agent

A research agent harness for Claude Code.  
Provide a topic and it automatically performs web research → source evaluation → report writing.

## Quick Start

```bash
# 1. Copy to your project
cp -r research-agent/ ~/my-project/
cd ~/my-project

# 2. Launch Claude Code
claude

# 3. Start researching
> /research [topic]
> /quick-brief [question]
```

## Structure

| Component | Location | Role |
|-----------|----------|------|
| CLAUDE.md | `./CLAUDE.md` | Project rules (loaded every session) |
| Subagents | `.claude/agents/` | 4 specialized agents with isolated context |
| Skills | `.claude/skills/` | 3 on-demand workflow orchestrators |
| Commands | `.claude/commands/` | 2 slash command entry points |
| Rules | `.claude/rules/` | 3 auto-applied rules by file pattern |

See [docs/architecture.md](docs/architecture.md) for detailed architecture documentation.

## License

MIT
