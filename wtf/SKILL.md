---
name: wtf
description: >
  Re-explain the previous response in plain language when the user did not
  follow it. Use this skill when the user types "wtf", "wtf?", "huh?", "in
  English?", "say that simpler", "I don't follow", "you lost me", "explain
  that again but simpler", "eli5 that", or any short reaction signalling the
  last answer was too long, too dense, or too jargon-heavy. Rephrases what was
  already said in ASD-STE100 Simplified Technical English — it does not answer
  a new question or redo the work.
---

# wtf: Say That Again, Simply

The user just read something and did not follow it. Take the **previous
assistant message** and say the same thing again, in plain language.

Do not apologise. Do not say "let me simplify that". Do not restate the
question. Give the simpler version and nothing else.

## Step 1: Check that it is a rephrase request

A bare "wtf" — or "huh?", "in English?", "you lost me" — is a rephrase
request. Use this skill.

"wtf" attached to a specific object is a **question**, not a rephrase request:

- "wtf" → rephrase the last message.
- "wtf is a control function?" → answer the question. It is a new question,
  so answer it plainly, but do not treat it as a rephrase.
- "wtf, the regression dropped 400 observations" → investigate. Something is
  wrong. This skill does not apply.

If the user points at one part — "wtf does the second paragraph mean" —
rephrase only that part.

If there is no previous assistant message, say so in one line and stop.

## Step 2: Rewrite in Simplified Technical English

Write the reply in ASD-STE100 Simplified Technical English:

- One idea per sentence. Keep sentences to about 20 words or fewer.
- Active voice. Name who does what: "The regression drops those firms", not
  "those firms are dropped".
- Present tense where it works.
- One word, one meaning. Do not use the same word for two different things.
  Do not switch words for the same thing halfway through.
- Plain connectives: "so", "because", "but", "then".
- No nominalisations. "We estimate" beats "estimation is performed".

## Step 3: Keep the technical names

ASD-STE100 permits **Technical Names** — domain nouns with no plainer
equivalent. Academic finance and econometrics terms qualify. Keep them when
they carry the meaning:

> regression, fixed effects, standard errors, clustering, instrument, first
> stage, panel, event study, difference-in-differences, SDF, factor loading,
> spread, duration, leverage

Keep the term. Simplify the sentence around it. "Fixed effects" stays; what
gets simpler is the explanation of what they do.

Cut the jargon that is **not** doing work:

- Academic hedging — "it is worth noting", "one might argue", "broadly
  speaking".
- Abstraction with no referent — "leverage the framework", "orthogonal to".
- Latinate verbs where a short one exists — "utilise" → "use", "facilitate"
  → "help", "sufficient" → "enough".

If a term is both necessary and genuinely obscure, keep it and gloss it in
one short sentence straight after.

## Step 4: Keep the facts exact

Never change: file paths, commands, code, variable names, function names,
numbers, coefficients, sample sizes, dates, citations.

Copy them character for character. Only the prose around them gets simpler.
A simplification that changes a number is a mistake, not a simplification.

## Step 5: Cut the structure

The original was probably too long. The rephrase should be shorter — aim for
half the length or less.

- Drop headers unless the original genuinely covered separate topics.
- Flatten nested bullets into sentences.
- Turn a table into prose if it has three rows or fewer.
- Cut the preamble and the closing summary. Keep the middle.

## Escalating

If the user types "wtf" a second time on an already-simplified answer, go
further. Do not simply reword it again. Add something concrete:

- The smallest numerical example that makes the point. Round numbers, worked
  through so the user can check it by hand.
- Or a one-sentence analogy — then say explicitly what maps to what.

## Important Rules

- **Rephrase only.** Do not answer new questions, add new information, run
  tools, or redo the analysis. Say what was already said, differently.
- **Do not change the claim.** If the original said "probably", the rephrase
  says "probably". Simpler language must not become more confident language.
- **No files, no side effects.** This skill is conversational. It writes
  nothing.
- **Do not announce the simplification.** No "in other words", no "think of
  it like this", no closing "does that help?". Lead with the answer.
- **Output styles do not override this.** If a custom output style is active,
  the ASD-STE100 register still applies to this one response.
- **If the original was wrong, say so.** Rephrasing is a second look at it.
  If the simple version exposes an error, flag the error rather than
  restating it clearly.
