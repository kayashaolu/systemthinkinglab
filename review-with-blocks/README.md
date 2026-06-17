# Review with Blocks

A free skill for Claude Code that reviews a system **design** the way a senior engineer would — through the 7 universal building blocks and the non-functional "-ilities."

Paste a design doc, describe your architecture, or share a diagram. The skill decomposes it into blocks and forces, flags the wrong and missing ones, rates the load-bearing "-ilities" (does it actually scale / stay up / stay correct?), names the tradeoffs, and hands you the questions a senior would ask in the review meeting.

It is the **review** end of the arc: **design → build → review**. (Pairs with [design-with-blocks](https://github.com/kayashaolu/systemthinkinglab), which is the *design* end.)

**Scope: design review only.** It judges the architecture, not the code. It does not write code, run anything, or read your repository — point it at the design.

## What it checks

**1. Structure** — decompose into the 7 blocks + 3 external forces, then catch:
- the wrong block for the job (an image in a relational database, a sync call that should be a queue),
- a missing block (a force with nothing answering it),
- over-engineering (a block for a force you cannot see yet).

**2. The "-ilities"** — only the ones your forces make load-bearing, each rated `holds` / `at-risk` / `gap`, tied to the blocks that carry it and the tradeoff it costs:
Latency, Scalability, Reliability, Availability, Durability, Consistency, Security — plus Observability as the thread through all of them.

**3. The senior questions** — the 3–5 pointed questions that expose whether the design understood its forces.

## The output

A prioritized review: the architecture as designed, a verdict, findings tagged `[BLOCKER]` / `[RISK]` / `[POLISH]`, a table of the -ilities that matter here with ratings and tradeoffs, and the senior questions.

## Install

```
/plugin marketplace add kayashaolu/systemthinkinglab
/plugin install review-with-blocks@systemthinkinglab
```

Then run `/review-with-blocks` and give it your design.

## Why building blocks

Every system, from Instagram to Stripe, is composed of the same seven primitives (Service, Worker, Key-Value Store, File Store, Queue, Relational Database, Vector Database) plus three external entities (User, External Service, Time). Reviewing through that lens judges the *architecture* — which AI cannot do for you — instead of nitpicking syntax. Learn the framework free at [systemthinkinglab.ai](https://systemthinkinglab.ai).

## License

Apache-2.0.
