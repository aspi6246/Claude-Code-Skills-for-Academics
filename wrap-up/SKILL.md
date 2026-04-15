---
name: wrap-up
description: >
  End-of-session cleanup routine that captures all session work before
  context is lost. Use this skill when the user says "wrap up", "wrap-up",
  "let's wrap it up", "let's wrap up", "wind down", "end session",
  "that's it for today", "save and close", "let's call it", "close out",
  "done for today", or any indication they are finishing a work session
  and want everything documented before starting fresh.
---

# Wrap-Up: End-of-Session Cleanup Protocol

When the user signals the end of a session, perform ALL of the following
steps silently. Do not ask questions, do not explain what you are doing,
do not narrate the process. Just do it.

When all steps are complete, respond with exactly:

**"Wrap-up complete. See you in the next life."**

Nothing else. No summary, no bullet points, no follow-up questions.

---

## Step 1: Session Log

Create or append to a session log file at:
`[project_root]/code/_Claude Logs/session_logs/YYYY-MM-DD.md`

If multiple sessions occur on the same day, append to the existing file
with a horizontal rule separator and a timestamp.

Create the `code/_Claude Logs/` directory if it does not exist.

### Session log format

```markdown
# Session Log — YYYY-MM-DD

**Session time:** [approximate start–end based on conversation context]

## What was done
- [Concrete accomplishments — be specific and verifiable]
- [e.g., "Wrote data cleaning script code/01_clean.R"]
- [e.g., "Ran baseline DiD specification, results in output/tables/"]

## Key decisions made
- [Design choices, methodology decisions, direction changes]
- [e.g., "Decided to cluster SEs at state level rather than firm level"]

## Problems encountered
- [Bugs, data issues, dead ends — anything worth knowing next time]

## Files created or modified
- `path/to/file1.R` — [brief description of change]
- `path/to/file2.tex` — [brief description of change]
- `path/to/new_file.R` — [created: purpose]

## Where we left off
- [Exact state of work — what was mid-progress, what's next]
```

To compile the files list, check the conversation history for any files
that were created, edited, or generated during this session. Include the
path relative to the project root and a brief note about what changed or
why the file was created.

## Step 2: CLAUDE.md Update

Read the current `CLAUDE.md` in the project root. Determine whether
anything learned during this session should be added:

- New project conventions established
- Package or tool preferences clarified
- Data structure or pipeline details discovered
- File paths or naming conventions adopted
- Build/run commands identified
- Variable definitions or data quirks uncovered

If there are meaningful updates, append them to the appropriate section
of `CLAUDE.md`. Do not rewrite existing content — only add genuinely
new information. If nothing new was learned, skip this step silently.

Do NOT add:
- Temporary or session-specific notes
- Task lists or to-do items (those go to the pinboard)
- Information that is already in CLAUDE.md
- Trivial details that would not help a future session

## Step 3: README.md Update

Read the current `README.md` (if it exists). Check whether the project's
folder structure has changed during this session:

- New directories created
- New key files added (scripts, data files, output)
- Significant reorganisation

If the structure has changed, update the folder tree in README.md to
reflect the current state. If README.md has no folder tree section,
add one. If nothing changed, skip this step silently.

## Step 4: Memory Update

Write any new knowledge worth preserving to the auto memory system.
Focus on information that would save time in a future session:

- Data quirks discovered (e.g., "CUSIP has trailing spaces in raw data")
- Gotchas encountered (e.g., "arrow fails on this file, use fread instead")
- Relationships between files or variables uncovered
- Correct commands or procedures figured out through trial and error
- Working solutions to problems that took effort to solve

If nothing novel was learned, skip this step silently.

## Step 5: Pinboard Update

Read the current `PINBOARD.md` (if it exists — create it using the
pinboard skill format if it does not exist and there are items to add).

Review the session for any open tasks, unfinished work, or follow-ups
that were mentioned but not completed:

- Tasks the user said they would do later
- Ideas that came up but were not explored
- Bugs identified but not fixed
- Papers or references mentioned but not looked up
- Questions raised but not answered
- Analysis the user said they wanted to try but did not get to

Add each item to the appropriate category in `PINBOARD.md`:

```markdown
- [ ] [YYYY-MM-DD] Note text here
```

Auto-categorise into To-Do, Papers, Ideas, or Data Issues based on
content. If nothing is outstanding, skip this step silently.

## Step 6: Git Commit

Check the Git status of the project. If there are uncommitted changes
(staged or unstaged):

1. Stage all changes: `git add .`
2. Commit with the message: `wrap-up: end of session YYYY-MM-DD`
3. Do NOT push — just commit locally

If the project is not a Git repository, or if there are no changes to
commit, skip this step silently.

If the commit fails for any reason (merge conflict, hooks, etc.),
note the failure in the session log under "Problems encountered" but
do not ask the user about it — just proceed with the wrap-up.

---

## Important Rules

- **Be silent.** Do not narrate what you are doing. No "I'll now update
  the session log..." — just do it.
- **Be conservative.** Only write information that is genuinely useful.
  An empty update is better than a noisy one.
- **Do not duplicate.** If something is already captured in CLAUDE.md,
  PINBOARD.md, or memory, do not add it again.
- **Do not modify author code or data.** This skill only touches
  documentation and project management files (plus the git commit).
- **Create directories as needed.** If `correspondence/session_logs/`
  does not exist, create it. Do not ask.
- **Respect existing content.** Append to files, do not overwrite them.
  Read before writing.
- **The closing line is sacred.** After all steps are complete, respond
  with exactly: **"Wrap-up complete. See you in the next life."**
  Nothing before it. Nothing after it.
