---
name: spin-up
description: >
  Start-of-session orientation routine that briefs Claude on the current
  state of a project before work begins. Use this skill when the user
  says "spin up", "spin it up", "let's spin up", "spinning up", "spin
  up the project", or any variant signalling they want a session kickoff
  briefing. Performs: git status check (unpushed commits, remote
  divergence), CLAUDE.md and README read, most-recent session log read
  (focusing on "Where we left off"), PINBOARD.md open items, and a
  short synthesis of project state. Ends by asking what to work on today.
---

# Spin-Up: Start-of-Session Orientation

When the user signals the start of a session, perform ALL of the checks
below in order, then present a tight briefing and ask what today's focus
is.

Unlike `wrap-up`, this skill is conversational — the purpose is to
surface information, not to act. Keep the briefing scannable (roughly
one screen), and do NOT start work or propose tasks until the user
replies to the closing question.

---

## Step 1: Read project instructions

Read `CLAUDE.md` at the project root (if it exists). Internalise project
rules, conventions, and any project-specific session-startup instructions.

Also read `README.md` if present, to ground yourself in the directory
structure and project purpose.

If neither file exists, note that in the briefing but continue.

## Step 2: Check git state

If the current working directory is inside a git repository:

1. `git fetch --quiet` to refresh remote refs so divergence is visible.
2. `git log @{u}..HEAD --oneline` to list unpushed commits on the
   current branch. If there is no upstream set, fall back to
   `git log origin/main..HEAD --oneline` (or `origin/master`); if that
   also fails, skip.
3. `git log HEAD..@{u} --oneline` to spot remote commits made elsewhere
   (e.g. GitHub web, another machine) that would require a pull before
   any future push.
4. Note the current branch and whether the working tree is clean.

If the project is not a git repo, skip this step silently.

**Do not push or pull anything** — this step is read-only. Surface
findings; let the user decide.

## Step 3: Read the most recent session log

Look for session logs in the project's log directory. Check these
locations in order:

- The path specified in `CLAUDE.md`, if any.
- `Claude Logs/`
- `Code/_Claude Session Logs/`
- `correspondence/session_logs/` (legacy)

Find the most recently-dated file and read it. Pay particular attention
to:

- **"Where we left off"** — the state work was in at end of last session.
- **"Problems encountered"** — open issues or blockers.
- **"Files created or modified"** — recent file touch points.

If no log exists, note that and continue.

## Step 4: Check the pinboard

Read `PINBOARD.md` at the project root (if it exists). Count open items
by category. Flag anything dated more than two weeks ago or marked
urgent.

If no pinboard exists, skip.

## Step 5: Synthesise the briefing

Present a briefing in approximately this format:

```markdown
## Session briefing — [project name]

**Last session:** YYYY-MM-DD — [one-line summary of last session's work]
**Where we left off:** [short quote or paraphrase]

**Git:**
- Branch: `branch-name` (clean / N unstaged changes)
- Unpushed: N commits [list them, or "none"]
- Remote ahead: N commits [or "in sync"]

**Pinboard:** N open items
- X to-dos (Y older than two weeks)
- Z papers to read
- W data issues

**Project state:** [1–2 sentences synthesising CLAUDE.md + last log]
```

Keep it tight. One scannable screen. Omit sections cleanly if there's
nothing to report ("No pinboard items outstanding.") rather than
leaving empty headings.

## Step 6: Ask the question

End the briefing with exactly:

> **What are we working on today?**

Then wait. Do not start work, propose tasks, or fix things surfaced
above until the user answers.

---

## Important Rules

- **Read-only.** Spin-up never writes files, never pushes, never pulls.
  It surfaces state and waits.
- **Do not create the session log.** That is `wrap-up`'s responsibility
  at end of session. Spin-up only reads prior logs.
- **Do not act on findings.** If there are unpushed commits, a dirty
  working tree, a stale pinboard item, or an unresolved problem from
  last session — list them, but wait for the user to direct action.
- **Briefing is scannable, not exhaustive.** Aim for ~15–25 lines of
  output. If any single step has a lot to say, summarise and offer
  detail on request.
- **Respect `CLAUDE.md`.** If the project's CLAUDE.md specifies a
  different startup ritual or log location, follow it.
