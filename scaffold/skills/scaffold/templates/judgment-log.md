# Judgment log

*Append-only. A **third artifact**, on a different axis from the two
ledgers (`codebase/`+`concepts/` and `learner/`): narrative and
decision-keyed, not mastery-keyed. It records what got pushed back on, what
got ruled, why, and what was learned — from direction-mode runs, and from
any craft-mode moment where a real disagreement got resolved. It takes **no
signed marks**: a narrative commits no single falsifiable claim the way a
prediction or a brief does, so scoring it would blur the mastery model's
semantics for every page that reads a concept's level. This file is evidence
you can point to and quote — it is never itself a scored event, and it never
feeds the review-flag mechanics.*

*If a learner cites a judgment-log entry as a receipt for graded work, pair
it with the `learner/` page evidence line for the same concept — a
judgment-log entry carries no mastery level by design, so it cannot stand
alone wherever a mastery level is what's being asked for; the paired
learner-page line is where that level lives.*

*Entry format, greppable with `grep "^## \[" judgment-log.md | tail -5`:*

```
## [YYYY-MM-DD] mode: craft|direction|unspecified | short title

**What was pushed back on / what was asked:**
...

**What got ruled / what the run did:**
...

**Stop reason:** done-criteria-met | max-rounds | time-box-exceeded |
stuck-detector | student-interrupt | n/a (craft-mode ruling, not a bounded run)

**Excerpt (verbatim, captured at write time):**
> ...

**Why:**
...

**What I learned:**
...
```
