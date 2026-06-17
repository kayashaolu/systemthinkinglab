# SCHEMA — how this wiki works

*This file is the wiki's own rulebook. The mentor reads it at the start of
every session, and it overrides the skill's defaults. When you and the mentor
settle a better convention — a new page type, a lighter ritual, a different
cadence — record it here. The wiki should fit you better every week.*

## Structure

```
scaffold-wiki/
├── SCHEMA.md          # this file
├── index.md           # catalog: every page, one line each — updated on every page add
├── log.md             # append-only timeline: ## [YYYY-MM-DD] type | title
├── codebase/          # LEDGER 1: what the AI knows about THIS repo (stamped ai-ingested)
├── concepts/          # LEDGER 1.5: general engineering concepts encountered here
└── learner/           # LEDGER 2: what YOU have demonstrated — mastery + dated evidence
    └── profile.md     # summary: strengths, gaps, trajectory
```

**The two-ledger rule (never override this one):** `codebase/` + `concepts/`
hold what the AI knows; `learner/` holds only what you have shown in
predictions, challenges, and catches. They are never merged, so "what do I
know?" always gets an honest answer.

## Conventions

- Mastery levels run `learning` → `understanding` → `internalizing`, and
  **levels never move down** — misses set a review flag instead. The rules
  themselves (promotion bars, evidence marks, the review-flag mechanics) live
  in the skill and are deliberately **not restated here** — a summary that
  drifts from the skill silently overrides it. Only local amendments belong
  below.
- Evidence lines are dated, marked, quirk-specific, and tied to a plan or
  commit; the full grammar and scoring tests live in the skill, not here.
- Architecture pages use the seven building blocks vocabulary; the honesty
  clause's full requirements live in the skill, not here.
- Wiki-links between pages use `[[path/page]]` form. Link liberally.

## Local amendments

*(none yet — settled conventions land here)*
