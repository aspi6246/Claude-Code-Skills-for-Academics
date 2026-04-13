---
name: pinboard
description: >
  Digital pinboard for quick project notes, reminders, and ideas. Use this
  skill when the user wants to jot down a note, reminder, to-do, paper to
  read, idea, or data issue — including phrases like "pin this", "note to
  self", "remind me to", "add to pinboard", "I need to remember to",
  "check out this paper", "look into this later", "jot this down",
  "don't let me forget", or any quick note the user wants saved for later.
  Also use when the user says "show my pinboard", "what's on my pinboard",
  "mark X as done", or "clear my pinboard."
---

# Pinboard: Quick Project Notes

A digital pinboard for capturing notes, reminders, and ideas during a
work session without breaking flow. Notes are saved to `PINBOARD.md` in
the project root.

## Adding a Note

When the user drops a note (e.g., "remind me to call Marco about the
data", "check out Spina et al 2026 on orphan wells"), do the following:

1. **Auto-categorise** the note into one of four categories based on content:
   - **To-Do** — action items, tasks, things to do, people to contact,
     forms to submit, deadlines
   - **Papers** — papers to read, articles to follow up on, citations
     to check, references to find
   - **Ideas** — hypotheses to test, research ideas, alternative
     specifications to try, things to think about
   - **Data Issues** — variables to investigate, data quality concerns,
     sample construction questions, merge problems to check

2. **Add the note silently** to `PINBOARD.md` in the appropriate category
   section. Include a timestamp. Do not ask for confirmation, category,
   or priority — just save it and move on.

3. **Acknowledge briefly** — one short sentence confirming the note was
   pinned. Do not repeat the note back. Do not ask follow-up questions.
   Example: "Pinned." or "Added to your pinboard."

### Format for each note entry

```markdown
- [ ] [YYYY-MM-DD] Note text here
```

### Creating PINBOARD.md

If `PINBOARD.md` does not exist yet, create it with this structure:

```markdown
# Pinboard

## To-Do

## Papers

## Ideas

## Data Issues

---

## Done
```

### Adding to an existing PINBOARD.md

Append the new note under the correct category heading. Do not reorder
or modify existing notes. If the file exists but is missing a category
section, add the section.

## Reading the Pinboard

When the user says "show my pinboard", "what's on my pinboard",
"any notes?", or similar:

1. Read `PINBOARD.md`
2. Present the contents organised by category
3. Note how many items are in each category
4. Flag any items older than 7 days as potentially stale — these may
   have been forgotten or are no longer relevant
5. If the pinboard is empty, say so

### Stale item format

When presenting, add a note next to old items:
```
- [ ] [2026-03-15] Call Marco about the merge issue ⚠️ (3 weeks ago)
```

## Marking Items as Done

When the user says "mark X as done", "done with X", "finished X",
or "completed X":

1. Find the matching item (match on keywords — it doesn't need to be
   an exact quote)
2. Move it from its current category to the **Done** section at the
   bottom of the file
3. Change `- [ ]` to `- [x]` and add the completion date
4. Acknowledge briefly: "Done."

### Format for completed items

```markdown
- [x] [2026-03-15] Call Marco about the merge issue ✓ completed 2026-04-07
```

If multiple items match the user's description, ask which one they mean
before marking done.

## Clearing the Pinboard

When the user says "clear my pinboard", "clean up the pinboard", or
"archive done items":

- **"Clear done items"** — remove everything in the Done section
- **"Clear everything"** — ask for confirmation, then reset the file
  to the empty template
- **"Clear stale items"** — move items older than 14 days to Done

Always ask for confirmation before clearing.

## Important Rules

- Never modify PINBOARD.md without reading it first — append, don't
  overwrite
- Keep the format consistent so the file stays human-readable
- This is the user's scratchpad — don't editorialize, reorganise,
  or "improve" their notes
- If the user's note doesn't clearly fit one category, default to
  **To-Do**
- When in doubt about whether something is a pinboard request, it
  probably is — err on the side of pinning it
