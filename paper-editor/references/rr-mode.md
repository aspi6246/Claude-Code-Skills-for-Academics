# R&R Mode: Revision Audit Protocol

When the author is responding to referee reports, The Editor operates in
R&R Mode. This is a different workflow from the standard seven-audit
protocol.

## Inputs Required

1. Original referee reports in `correspondence/referee_reports/`
   - `R1_report.pdf` (or `.txt`, `.md`)
   - `R2_report.pdf`
   - `editor_letter.pdf`
2. Author's response letter in `correspondence/response_letters/`
3. Revised manuscript

## R&R Audit Protocol

### Step 1: Extract all referee concerns

Create a numbered list of every distinct concern raised by each referee
and the editor. Number them as R1.1, R1.2, ..., R2.1, R2.2, ..., E.1,
E.2, etc.

### Step 2: Map claims to evidence

For each concern, identify:
- What the author claims to have done in the response letter
- Where in the revised manuscript this change appears
- Whether the change actually addresses the concern

### Step 3: Verify completeness

Check that every concern is addressed (even if to disagree with the
referee). Flag any concerns that are simply ignored.

### Step 4: Assess response quality

For each response, evaluate:
- Does the revision match the claim in the response letter?
- Is the referee's concern actually resolved?
- Is the response tone appropriate (responsive without being defensive)?

### Step 5: Check for introduced problems

Revisions to address one concern sometimes create new problems elsewhere.
Check for internal inconsistencies, new logical gaps, or contradictions
with other parts of the paper.

## R&R Report Format

File the report at:
`[project_root]/correspondence/the_editor/YYYY-MM-DD_rr_round[N]_report.md`

```
=================================================================
                    R&R AUDIT REPORT
              [Paper Title] — Revision Round [N]
              Date: YYYY-MM-DD
=================================================================

## Referee Concerns Mapping

### Referee 1

| # | Concern | Response Letter Claim | Manuscript Location | Verified? | Assessment |
|---|---------|----------------------|--------------------|-----------| -----------|
| R1.1 | [Concern] | [Claim] | §X, ¶Y | Yes/No | [Quality] |
| ... | ... | ... | ... | ... | ... |

### Referee 2

| # | Concern | Response Letter Claim | Manuscript Location | Verified? | Assessment |
|---|---------|----------------------|--------------------|-----------| -----------|
| R2.1 | [Concern] | [Claim] | §X, ¶Y | Yes/No | [Quality] |
| ... | ... | ... | ... | ... | ... |

### Editor

| # | Concern | Response Letter Claim | Manuscript Location | Verified? | Assessment |
|---|---------|----------------------|--------------------|-----------| -----------|
| E.1 | [Concern] | [Claim] | §X, ¶Y | Yes/No | [Quality] |
| ... | ... | ... | ... | ... | ... |

---

## Unaddressed Concerns

[List any concerns not addressed at all]

---

## Inadequately Addressed Concerns

[List concerns where the response is insufficient, with explanation]

---

## Response Letter Issues

[Problems with the response letter itself: tone, clarity, completeness]

---

## New Problems Introduced

[Issues created by the revisions]

---

## Recommendation

[ ] Ready to resubmit
[ ] Needs additional revisions
[ ] Response letter needs rewriting

=================================================================
```
