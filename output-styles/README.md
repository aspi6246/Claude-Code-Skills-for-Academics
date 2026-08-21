# Output Styles

Output styles are **not skills**. They are kept here so this repo holds one
copy of the whole Claude Code setup, but Claude Code does not read them from
this folder — nothing in here loads automatically.

A skill is task-specific instructions that load when relevant. An output style
modifies the system prompt for **every** turn of a session: role, tone, and
default response format. Project conventions belong in `CLAUDE.md`, not here.

## Styles in this folder

| File | Name | Purpose |
|---|---|---|
| `eli5.md` | `ELI5` | Plain language for the end of a long day. Short sentences, at most two options with a recommendation, exact paths and commands. |
| `phdadvisor.md` | `PhDAdvisor` | Short, sharp intuition pitched at a 2nd-year finance PhD — intuition, then formalism, then the catch. Toy numerical examples and TikZ diagrams where they earn their place. |

Both set `keep-coding-instructions: true`, so they change how Claude explains
things without changing how it writes code.

## Install

Copy the style into the global output-styles directory:

```powershell
New-Item -ItemType Directory -Force "$HOME\.claude\output-styles"
Copy-Item "$HOME\.claude\skills\output-styles\phdadvisor.md" "$HOME\.claude\output-styles\"
```

Then activate it by setting `outputStyle` in a settings file. The first file
that sets it wins:

1. `<project>/.claude/settings.local.json` — that project, just you
2. `<project>/.claude/settings.json` — that project, anyone who clones it
3. `~/.claude/settings.json` — every project

```json
{
  "outputStyle": "PhDAdvisor"
}
```

In the terminal you can instead run `/config` and pick **Output style**, which
writes the same setting. The standalone `/output-style` command was removed in
v2.1.91.

Two gotchas:

- The value must match the `name:` in the style's frontmatter (`PhDAdvisor`),
  not the filename. A name that matches nothing is ignored silently.
- The style is baked into the system prompt at session start, so a change only
  takes effect after `/clear` or a new session.

## Keeping these in sync

These are **copies**. The live files are in `~/.claude/output-styles/`. Editing
one does not update the other — copy the change across in both directions.

## Credit

`ELI5` is not original to this repo. It was shared by Lydia Hallie
([post](https://x.com/lydiahallie/status/2080378470111256907)) and published in
full at
[hctor.com](https://hctor.com/guides/change-claude-code-output-style), which
credits Hector Cuevas as its author. The attribution between the two is
unresolved; the credit line is kept in the file header.

`PhDAdvisor` is original.
