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
├── log.md             # append-only timeline: ## [YYYY-MM-DD] type | mode: ... | title
├── judgment-log.md    # THIRD ARTIFACT: narrative judgment trail (created on first use)
├── codebase/          # LEDGER 1: what the AI knows about THIS repo (stamped ai-ingested)
├── concepts/          # LEDGER 1.5: general engineering concepts encountered here
├── learner/           # LEDGER 2: what YOU have demonstrated — mastery + dated evidence
│   └── profile.md     # summary: strengths, gaps, trajectory
├── briefs/            # direction-mode: one file per brief (created on first use)
└── artifacts/         # selective exports from `/scaffold export` (created on first use)
```

`judgment-log.md`, `briefs/`, and `artifacts/` don't exist until direction
mode or `/scaffold export` is used for the first time — same lazy-creation
pattern as a learner page. A craft-mode-only wiki never grows them, and
that's fine.

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

## Modes

- Every task runs in **craft mode** (the loop, unchanged) or **direction
  mode** (a bounded builder+breaker pair, scoped by a brief you write). The
  mode is chosen once per task and announced in one line. The full rules for
  both live in the skill, not here — this file states only the fields.
- `mode: craft | direction | unspecified` is a field on every `log.md` entry,
  `judgment-log.md` entry, and learner-page evidence line. It is
  **required-on-write, optional-on-read**: a missing `mode:` reads as
  `unspecified` and is graded on content, never treated as a miss.
  **This field is never backfilled onto an existing entry.** Retro-stamping
  provenance onto an entry that never had it destroys the exact property the
  field exists to provide — an entry written before this convention existed
  simply predates it, permanently, and that's the honest record.
- Every `log.md` entry and every `judgment-log.md` entry that cites a claim
  captures a **verbatim excerpt of it, at the moment it's written** — never
  reconstructed after the fact. An entry that cites nothing carries no
  excerpt.
- The `mode:` token sits in a different place on each of the three
  artifacts it appears on: a `| mode: craft|direction|unspecified |`
  segment inside the `##` header line on both `log.md` and
  `judgment-log.md` entries, and a trailing `[mode: craft|direction]` tag
  on a learner-page evidence line.

## Local configuration

- `catcher_name:` *(unset)* — the display name for the adversarial reviewer
  role, in both craft-mode diffs and direction-mode findings. Default when
  unset: **"the breaker"** (a second junior engineer whose only job is to
  break the first one's work). Set a value here to change it everywhere at
  once, instead of it drifting across sessions.
- `direction_mode_ceiling:` *(unset — PROVISIONAL default: 10 rounds / 60
  minutes)* — a hard backstop on any direction-mode brief's own bounds,
  regardless of what the brief requests. This default is an arbitrary
  engineering safety cap, not a pedagogical number — a real published value
  (if one exists for your course or team) belongs here instead. A brief's
  own bounds should usually be tighter than this ceiling, not looser.

## Local amendments

*(none yet — settled conventions land here)*
