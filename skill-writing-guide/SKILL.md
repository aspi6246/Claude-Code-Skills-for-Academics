---
name: skill-writing-guide
description: >
  Reference for writing and improving Claude Code skills. Use when
  the user asks to create a new skill, improve an existing skill,
  turn a conversation workflow into a reusable skill, or says anything
  like "make this a skill", "save this as a skill", or "let's capture this."
---

# Skill Writing Conventions

## Structure checklist

Every skill needs:
- A folder with a descriptive kebab-case name (e.g., `r-empirical-finance`)
- A `SKILL.md` file inside that folder
- YAML frontmatter with `name` and `description` fields

Optional supporting files go in subfolders:
- `scripts/` — code Claude can execute (R, Python, shell)
- `references/` — documentation Claude reads into context as needed
- `assets/` — templates, fonts, or other files used in output

## Writing the description

The description is the single most important line. Claude uses it to decide
whether to load the skill. Claude tends to under-trigger, so be explicit:

**Weak:**
```yaml
description: Helps with R code.
```

**Strong:**
```yaml
description: >
  Conventions for writing empirical finance R code with data.table, fixest,
  arrow, and ggplot2. Use this skill whenever writing, reviewing, or debugging
  R scripts for panel data, regressions, or data pipelines — even if the user
  doesn't explicitly mention these packages.
```

Rules of thumb:
- Keep under 200 characters if possible, but clarity beats brevity
- List the phrases a user would actually type that should activate this skill
- Include "even if the user doesn't explicitly mention X" language
- Name the specific packages, tools, or frameworks involved

## Writing the body

### Use examples, not just rules

Claude learns patterns from examples more reliably than from abstract
instructions. Always show what you want, not just describe it.

**Weak:**
```
Use proper regression syntax.
```

**Strong:**
```
## Panel regressions
est <- feols(y ~ x1 + x2 | firm_id + year, data = dt, vcov = "cluster")
```

### Encode your corrections

If you've corrected Claude 3+ times on the same thing across sessions,
that correction belongs in a skill. Common examples:
- "Never use tidyverse, always use data.table"
- "Always compile with pdfLaTeX, never XeLaTeX"
- "Always cluster standard errors on panel regressions"

### Use clear constraint language

- **"Always"** and **"never"** for hard constraints
- **"Prefer"** and **"avoid"** for soft preferences
- **"Warn if"** for things Claude should flag but not block

### Include "what NOT to do"

Negative instructions are surprisingly effective when Claude has known
defaults you want to override:
```
Do NOT use dplyr or any tidyverse package for data manipulation.
Do NOT use lm() for panel regressions — always use fixest::feols().
Do NOT use fontspec — it is incompatible with pdfLaTeX.
```

## When to split a skill

- If a SKILL.md exceeds ~200 lines, move reference material into
  a `references/` subfolder and point to it from SKILL.md
- If two workflows only sometimes overlap, they should be two separate skills
- If a skill tries to cover both "how to write code" and "how to review code",
  those are different tasks and deserve separate skills

## Iteration workflow

1. Write the skill (start small — one page is fine)
2. Test with a natural prompt (not "use skill X to..." — test with
   what you'd actually type, like "write me a DiD regression script")
3. Note what Claude gets wrong or ignores
4. Update the skill with corrections
5. Repeat until the skill is stable across 3-4 different prompts
6. Commit and push to the repo
