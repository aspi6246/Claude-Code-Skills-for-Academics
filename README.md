# Claude Code Skills

Personal skills repo for academic empirical finance research workflows.

## Setup

Clone this repo directly into the Claude Code global skills directory:

```powershell
git clone https://github.com/aspi6246/claude-skills.git "$HOME\.claude\skills"
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
| `skill-writing-guide` | Reference for writing and improving skills |
| `r-empirical-finance` | R code conventions for panel data / causal inference |
| `beamer-slides` | LaTeX Beamer slide generation with UTS house style |
| `code-audit` | Two-phase code review for research scripts |

## Adding a new skill

1. Create a new folder with a descriptive name
2. Add a `SKILL.md` file with YAML frontmatter (`name` and `description`)
3. Test with a natural prompt in Claude Code
4. Iterate until stable
5. Commit and push

## Notes

- Skills are plain Markdown, not LaTeX — don't try to compile them
- The `description` field is the most important line in any skill — Claude uses it to decide whether to load the skill
- GitHub is the cloud backup; this repo should NOT live inside Dropbox
