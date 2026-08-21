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
| `edmans-audit` | Pre-submission paper audit against Edmans' (2025) three-part framework: Contribution, Execution, Exposition |
| `canvas-lms-api` | Canvas LMS REST API conventions for course sync scripts (modules, pages, file uploads) |
| `spin-up` | Start-of-session briefing — git state, last log, pinboard, active output style, project state synthesis |
| `wrap-up` | End-of-session cleanup — log, memory, pinboard, session-scoped git commit |
| `script-registry` | Track R Markdown script dependencies, inputs/outputs, and paper targets via per-script YAML metadata |
| `code-sweep` | End-of-milestone audit of the Code/ folder for drift between scripts, registry, outputs, and paper — propose-and-confirm fixes |
| `skill-writing-guide` | Reference for writing and improving skills |
| `pinboard` | Quick-capture pinboard for to-dos, paper leads, data issues, and ideas |
| `glossary` | Per-project glossary of definitions, abbreviations, and command-phrases, loaded adaptively at session start |
| `wtf` | Type "wtf" to get the previous response again in ASD-STE100 Simplified Technical English — jargon out, technical names kept |

## Output styles

The `output-styles/` folder holds copies of my Claude Code output styles.
They are **not skills** and Claude Code does not load them from this repo —
they are kept here so one repo holds the whole setup. A skill loads for a
specific task; an output style changes role, tone, and response format for
every turn of a session.

| File | Name | Purpose |
|---|---|---|
| `output-styles/eli5.md` | `ELI5` | Plain language for the end of a long day — short sentences, at most two options with a recommendation |
| `output-styles/phdadvisor.md` | `PhDAdvisor` | Short, sharp intuition for a 2nd-year finance PhD — intuition, then formalism, then the catch |

Install and activation instructions are in
[`output-styles/README.md`](output-styles/README.md). These are copies; the
live files live in `~/.claude/output-styles/` and do not sync automatically.

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
