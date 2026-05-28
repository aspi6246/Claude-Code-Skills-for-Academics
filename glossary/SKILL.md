---
name: glossary
description: >
  Per-project glossary of key definitions, abbreviations, and command-phrases,
  stored in `GLOSSARY.md` at the project root. Use this skill when the user
  defines or asks about a project-specific term — variable names, dataset or
  database names, acronyms — or sets up a command-phrase (a phrase that maps to
  an action, e.g. "push" = commit and push the paper to GitHub). Triggers
  include "add to glossary", "glossary: X means Y", "define X for this project",
  "what does X mean here", "what does X stand for", "from now on X means Y",
  "show the glossary", "what's in our glossary", and "remove X from glossary".
  Also use proactively: offer to capture a term when the user defines one in
  passing, or when you hit an undefined abbreviation or variable name in their
  code or data. Loaded at session start by `/spin-up` so command-phrases stay active.
---

# Glossary: Per-Project Terms & Command-Phrases

A project-local dictionary of the definitions, abbreviations, and command-phrases
that matter for *this* project. Stored in `GLOSSARY.md` at the project root, so
each project keeps its own. The skill definition is global; the data is
per-project — the same split as `pinboard` and `script-registry`.

Three categories:

- **Definitions** — variable names, dataset/database names, key concepts.
  *(e.g. `ret` = monthly stock return; `WellDatabase` = the licensed well-level dataset)*
- **Abbreviations** — acronyms and short forms used in the project.
  *(e.g. `WRDS` = Wharton Research Data Services)*
- **Command-Phrases** — phrases the user says that map to an **action** Claude
  should perform. *(e.g. "push" = commit and push the paper to its GitHub repo)*

Definitions and abbreviations are **reference** — read to understand the project.
Command-phrases are **behavioral** — read to act.

## How the glossary is used

The glossary is loaded **adaptively** at session start by `/spin-up`, so it never
weighs on the context window no matter how big it grows:

- **Command-Phrases load eagerly, in full.** They are behavioral and won't trigger
  the skill on their own (the bare word "push" won't invoke `glossary`), so they
  must be in context from the start. They're few by design — keep them so.
- **Definitions & Abbreviations load lazily.** At session start only their *term
  list* (the headwords, not the glosses) is loaded, so you know what's defined.
  Read the full line **on demand** — when one of those terms actually comes up, or
  the user asks — by grepping the term in `GLOSSARY.md`. Do NOT pull the whole
  Definitions section into context up front, and do NOT ask the user what a listed
  term means — look it up.
- **Small glossary?** If the whole file is under ~25 entries, `/spin-up` just loads
  it whole — the lazy split only earns its keep once the term sections grow.

**On demand, always.** "What does X mean?", "what does X stand for?", "what's in our
glossary?" → grep/read `GLOSSARY.md` and answer from it. If the term isn't there,
say so — don't guess.

## Command-phrases (behavioral)

When the user uses a phrase defined under **Command-Phrases**, perform the mapped
action — they have already told you what they want, so don't re-ask "do you want
me to push?". But still honor standing safety rules around the action itself:

- Before any push to a **public** repo, run the secrets/PII preflight (scan staged
  files for keys, names, usernames in paths). The command-phrase is permission to
  push, not permission to skip the scan.
- Destructive or irreversible actions (delete, force-push, deploy) still get a
  one-line confirmation, even when aliased.

If a command-phrase is ambiguous in the current context (e.g. "push" but there are
two repos), ask which one — briefly.

## Adding entries

**When explicitly asked** ("add to glossary", "glossary: X means Y", "from now on
X means Y"):

1. **Categorise** the entry — a phrase mapping to an action → Command-Phrase; an
   acronym/short form → Abbreviation; anything else → Definition.
2. **Append silently** under the right section in `GLOSSARY.md`. Don't reorder or
   rewrite existing entries.
3. **Acknowledge in one line** — "Added to the glossary." Don't read it back.

**Proactively** — *offer*, never auto-add, and only when the term clears the
**inclusion bar** below:

- The user defines a term in passing ("by `ret` I mean monthly returns") → offer:
  "Want me to add `ret` to the glossary?"
- You hit an undefined, project-specific abbreviation or variable in their code/data
  → offer to capture it once you know what it means.

Keep offers to one line and don't nag — if declined, drop it.

### What belongs (the inclusion bar)

Add a term only if it is **all four**: *durable* (will still matter next month),
*non-obvious* (not self-explanatory from its name), *recurring* (comes up more than
once), and *project-specific*. Same discipline as the memory system: don't store
what's derivable by reading the code.

- **Belongs:** `ret` (terse, non-obvious), `WellDatabase` (project dataset), "push"
  (a command-phrase), a domain acronym a newcomer wouldn't know.
- **Doesn't:** `monthly_return` (self-documenting name), a one-off abbreviation used
  once, anything already spelled out in `README`/`CLAUDE.md`, general-knowledge
  acronyms (`CSV`, `API`).

When in doubt, leave it out — the glossary earns its always-on cost only by staying
small and high-signal.

### Entry formats

One line per entry: bold headword, em-dash, then a **short** gloss — aim for under
~12 words. If it needs a paragraph, it belongs in `README`/`CLAUDE.md`, not here.
No timestamps. (Command-Phrases sits first because it's the only eagerly-loaded
section — see below.)

```markdown
## Command-Phrases
- **"push"** — commit and push the paper to its GitHub repo

## Definitions
- **ret** — monthly stock return (CRSP, decimal)
- **WellDatabase** — licensed well-level production dataset

## Abbreviations
- **WRDS** — Wharton Research Data Services
```

### Creating GLOSSARY.md

If it doesn't exist, create it at the project root with this structure.
**Command-Phrases comes first** — it's the only section loaded eagerly each session,
so keeping it at the top makes the session-start read cheap:

```markdown
# Glossary

<!-- Project-specific command-phrases, definitions, and abbreviations. -->
<!-- Command-Phrases load eagerly at session start (via /spin-up); Definitions and -->
<!-- Abbreviations load lazily / on demand. Manage with /glossary. -->

## Command-Phrases

## Definitions

## Abbreviations
```

Add a missing section heading if needed; never drop existing entries.

## Showing, editing, removing

- **"Show the glossary" / "what's in our glossary"** — read `GLOSSARY.md` and
  present it by section with a count per section. If empty, say so.
- **"Change X to Y" / "update the definition of X"** — find the entry, edit it in
  place, acknowledge in one line.
- **"Remove X from glossary"** — delete that entry. If it's a command-phrase, note
  the alias is no longer active. Never clear the whole file without explicit
  confirmation.

## Keeping it lean

The glossary is always-on, so it has to stay small and high-signal.

- **Size flags.** `/spin-up` reports the counts and flags for pruning once the
  glossary passes **~50 total entries** or **~15 command-phrases**. Treat those as
  soft ceilings, not targets.
- **Prune on request.** "prune glossary" / "clean up the glossary" → read the file,
  surface likely-dead entries (superseded command-phrases, terms that no longer
  appear in the code/paper, duplicates), and propose removals. Never bulk-delete
  without confirmation.
- **One concept per entry.** If an entry is growing into a paragraph or listing
  several things, it's the wrong tool — move it to `README`/`CLAUDE.md`.

## Relationship to other systems

- **vs `pinboard`** — pinboard holds transient tasks/notes/ideas that get done and
  cleared; the glossary holds stable terms that persist for the project's life.
- **vs memory** (`~/.claude/.../memory/`) — memory stores cross-project facts about
  the user, feedback, and project context; the glossary stores project-specific
  *terms* and *phrases*, and lives inside the project.
- **vs `CLAUDE.md`** — hard project rules belong in `CLAUDE.md`; the glossary is the
  lighter, user-editable list of what tokens mean and what phrases trigger.

## Important rules

- **Read `GLOSSARY.md` before writing it** — append, don't overwrite.
- **Per-project** — always the `GLOSSARY.md` in the current project root, never a
  shared global file. Repeat universal phrases like "push" in each project that
  needs them.
- **Don't editorialize** — it's the user's dictionary; capture their wording, don't
  "improve" definitions.
- **Keep it readable** — a human scans this. Consistent formatting, one entry per
  line, no timestamps (definitions are stable; they don't age like pinboard notes).
