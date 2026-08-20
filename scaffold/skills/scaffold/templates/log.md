# Log

*Append-only. Entry format:
`## [YYYY-MM-DD] init|plan|commit|query|catchup|brief|run|ruling | mode:
craft|direction|unspecified | short title` — greppable with
`grep "^## \[" log.md | tail -5`.*

*The `mode:` field is **required-on-write, optional-on-read**: every new
entry carries one, but a missing `mode:` on an entry written before this
convention existed reads as `unspecified` and is graded on content — it is
never a miss, and it is never backfilled onto the entry after the fact. See
`SCHEMA.md`'s "Modes" section for why.*

*An entry that cites a claim — a `plan`, `commit`, `brief`, `run`, or
`ruling` entry citing a prediction, a brief's done-criteria, or a diff's
finding — carries a verbatim excerpt of it, captured at the moment the
entry is written, never reconstructed later:*

```
**Excerpt (verbatim, captured at write time):**
> ...
```

*An entry that cites nothing — `init`, `query`, `catchup` — carries no
excerpt. Never manufacture one to fill the field.*
