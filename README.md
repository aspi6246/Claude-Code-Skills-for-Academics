# Claude Code Skills

Personal skills repo for academic empirical finance research workflows.

## Setup

### Fresh install (empty `~/.claude/skills/`)

Clone this repo directly into the Claude Code global skills directory:

```powershell
git clone https://github.com/aspi6246/Claude-Code-Skills-for-Academics.git "$HOME\.claude\skills"
```

### Selective install (skills directory already exists)

If `~/.claude/skills/` already contains other skills, do **not** clone
on top of it — it will fail. Instead, clone into a temporary location
and copy only the skills you want:

```powershell
git clone https://github.com/aspi6246/Claude-Code-Skills-for-Academics.git "$HOME\claude-skills-tmp"
Copy-Item "$HOME\claude-skills-tmp\wrap-up" "$HOME\.claude\skills\" -Recurse
# repeat for each desired skill, then remove the temp dir
Remove-Item "$HOME\claude-skills-tmp" -Recurse -Force
```

## Updating

After editing skills on GitHub or locally:

```powershell
cd "$HOME\.claude\skills"
git pull
```

## Skills

| Skill | Purpose |
|---|---|
| `r-empirical-finance` | R code conventions for panel data, causal inference, and data pipelines (data.table, fixest, arrow) |
| `beamer-slides-teaching` | LaTeX Beamer slide generation with pdfLaTeX and UTS house style |
| `beamer-check` | Compile → inspect → fix → verify audit loop for Beamer decks |
| `code-audit` | Two-phase code review for research scripts, with safeguards for licensed data |
| `data-profiler` | Systematic dataset profiling protocol — unit of observation, panel structure, data quality |
| `paper-editor` | Seven-audit editorial review protocol for academic finance working papers |
| `paper-review` | Structured summary template for academic papers |
| `canvas-lms-api` | Canvas LMS REST API conventions for course sync scripts (modules, pages, file uploads) |
| `wrap-up` | End-of-session cleanup — log, memory, pinboard, session-scoped git commit |
| `skill-writing-guide` | Reference for writing and improving skills |
| `pinboard` | Taking notes/reminders |

## Adding a new skill

1. Create a new folder with a descriptive name
2. Add a `SKILL.md` file with YAML frontmatter (`name` and `description`)
3. Test with a natural prompt in Claude Code
4. Iterate until stable
5. Commit and push

## Notes

- Skills are plain Markdown
- The `description` field is the most important line in any skill — Claude uses it to decide whether to load the skill
- GitHub is the cloud backup
