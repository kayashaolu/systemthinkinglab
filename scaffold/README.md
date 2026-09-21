# Scaffold

From [Systems Thinking Lab](https://systemthinkinglab.ai/?ref=scaffold), the workflow [Course 0](https://systemthinkinglab.ai/course-0.html?ref=scaffold) teaches.

**A plan-first developer workflow, run by an AI that works like a great mentor.** Scaffold predicts with you before it builds for you, keeps an honest ledger of what you've demonstrated you know, and turns every commit into a report on your codebase and your growth.

Most AI coding tools optimize one thing: the code. Scaffold optimizes two, at equal weight: the code, and *you*. A junior engineer is doing two jobs at once, shipping and learning, and a tool that does the first while silently skipping you past the second is how skills rot.

> *"What learning protects is your ability to build a mental model of why the
> code works, not the typing. AI only hurts that when it skips you past the
> model-building."*

Scaffold is the runnable version of that idea. It is derived from
[Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f),
a persistent, compounding wiki the AI maintains, pointed at a new target:
**the wiki becomes an external representation of your understanding.**

## The workflow

Four steps, every task:

1. **Plan.** You predict first: what do you think should change, and why.
2. **Diff and spar.** Scaffold answers with its own plan, as a diff against yours, and argues where it genuinely disagrees, before it builds.
3. **Build with the parts you claim.** Anything you said you'd write, you write. Scaffold builds the rest.
4. **Record.** Every commit reports what changed, what the wiki learned, and what you demonstrated. Two ledgers, kept separate (below).

That habit breaks the day you're tired, rushed, or sure you already know the answer. Predicting first makes the disagreement between your plan and the AI's visible instead of invisible. The build waits on your yes, not the agent's. A record after means what you understood is written down, not just what shipped. Skip any of it and you're back to code you cannot defend.

Learn it on real work: [Course 0](https://systemthinkinglab.ai/course-0.html?ref=scaffold) ($99, 8 lessons, 2 labs) teaches it end to end.

## What it does

**Predict, in detail.** The diff Scaffold shows against your plan banks what
you got right as evidence, and holds what it would change to five items,
ordered by stakes, each tagged with the concept behind it. Genuine
disagreement isn't waved through: Scaffold argues it out first, *"if we
shipped your plan as-is, which of my items would bite first?"* An AI that
only agrees teaches nothing.

**Two ledgers, never merged.** The wiki keeps what the *AI* knows about your
codebase (`codebase/`, `concepts/`) strictly separate from what *you've
demonstrated* (`learner/`). Ask "what do I know?" and you get an honest answer
with receipts: dated evidence from real predictions and real commits, not
vibes. Ask "what are my gaps?" and every gap comes with the page to read and a
task that would close it.

**Three mastery levels, mechanically earned, and they never go down.**
*Learning* → *understanding* (2 unaided correct predictions) →
*internalizing* (you applied it somewhere new, or you caught Scaffold's own
miss). A level records the best you've demonstrated, like a belt: knowledge
gets rusty, it doesn't get revoked. Two misses in six weeks flags the concept
for review instead: Scaffold steers tasks at it until two clean reps clear
the flag, always with the exact page to re-read and a task that re-proves it.
Honest, never cruel: warm AND direct, never one without the other.

**Every commit compounds.** After each commit: the most valuable thing the
commit taught about the codebase, what changed, what the wiki learned, and
what *you* learned. Threads that recur across commits get named. Nothing
disappears into chat history.

**Two modes: craft and direction.** By default you're in **craft mode**:
you and your junior engineer (the agent) predicting and diffing together on
every task, exactly as above. **Direction mode** is a different rep: you
write a brief (goal, falsifiable done-criteria, your own bounds on rounds
and time), and a builder-and-breaker pair iterates inside those bounds on
its own, stopping on one of five enumerated conditions. What comes back is a
diff plus findings attached to it, never a verdict, and the go/no-go call
is yours, every time. The brief is the prediction; the go/no-go is what gets
scored. Every direction-mode run also writes one entry to a third artifact,
the **judgment log**: a narrative record of what got pushed back on and
why, separate from the mastery ledger and taking no signed marks of its own.

## Install

Scaffold is a [Claude Code](https://claude.com/claude-code) plugin, distributed
through the Systems Thinking Lab marketplace:

```
/plugin marketplace add kayashaolu/systemthinkinglab
/plugin install scaffold@systemthinkinglab
```

That's it. Updates later are just `/plugin marketplace update systemthinkinglab`.

<details>
<summary>Or install manually as a personal skill</summary>

```bash
git clone https://github.com/kayashaolu/systemthinkinglab.git
ln -s "$(pwd)/systemthinkinglab/scaffold/skills/scaffold" ~/.claude/skills/scaffold
```

</details>

Then in any repo:

```
/scaffold
```

First run offers an optional, read-only exploration of the codebase, yours
(one keystroke to skip), then creates `scaffold-wiki/` (gitignored; your
ledger is yours) and does a light pass over the codebase. From then on it
engages automatically in that repo; you can ask for that same exploration
again at any point in a session, just by saying so.

## The architecture, as a design philosophy

Scaffold describes every codebase using seven building blocks (Service,
Worker, Key-Value Store, File Store, Queue, Relational Database, Vector
Database) and three external entities (User, External Service, Time): a
design philosophy for system structure, usable at any experience level.
Learn the seven free at [systemthinkinglab.ai/learn](https://systemthinkinglab.ai/learn?ref=scaffold).
Scaffold itself, through that lens:

- **User** (you) → **Service** (the mentor session: plans, diffs, answers)
- **Time** (every git commit) → **Worker** (the commit report: integrates what
  happened into the wiki)
- **File Store** (the wiki: plain markdown, the durable compounding artifact)
- **External Service** (git: the record of what actually happened)

No server, no database, no telemetry: the whole product is markdown,
prompts, and conventions, the leverage in the scaffolding, not the machinery.

## FAQ

**Will it slow me down?** A size gate keeps the ritual proportional: typo-level
changes skip it, and the full loop charges one "struggle toll" per task,
capped at minutes. Tell it to just fix something and it pushes back once,
then does it. It never holds work hostage.

**Who can see my ledger?** Nobody. The wiki is plain markdown on your
machine, gitignored by default, sent nowhere. Sharing it with a mentor is
your call, never a default. To share something specific, `/scaffold export`
renders exactly the entries you name, verbatim, into one dated file, instead
of the whole wiki.

**Does it work with other agents?** The skill format is Claude Code's, but
the wiki schema is plain markdown: `scaffold-wiki/SCHEMA.md` reads in any
agent, and porting the loop to an AGENTS.md is straightforward. PRs welcome.

**Is this a course?** No. It's free and works on your real job. If you want
to learn this workflow in full, [Course 0](https://systemthinkinglab.ai/course-0.html?ref=scaffold)
($99, 8 lessons and 2 labs) teaches it on real work; if you want the seven
building blocks behind the concepts it tags in your diffs, applied to real
systems, that's [Courses I-IV](https://systemthinkinglab.ai/courses-i-iv.html?ref=scaffold)
($299, one bundle). Both optional: the blocks themselves are free to read at
[systemthinkinglab.ai/learn](https://systemthinkinglab.ai/learn?ref=scaffold).

## Status

v0.5: an experiment in public. The loop, the mastery rules, and the coaching
voice were calibrated through persona trials and real-junior dogfooding;
direction mode is newer and less battle-tested than craft mode. Expect rough
edges anyway. Issues and field reports very welcome.

Plan approval is a checkpoint, not an assumption (0.3.2). Once the full loop
kicks in, the mentor will not build until you explicitly approve the plan: a
plain yes works. The change closes a defect where a vague "sounds good" could
count as approval.

First run now offers an exploration invitation (0.4.0). Before the wiki is
created, you get offered a few read-only minutes to explore the codebase
yourself: the mentor hands you three generic question shapes (trace a
lifecycle, name an assumption and where it's enforced, what breaks if this
is removed) and you point one at whatever code you choose. One keystroke to
decline, no cost either way.

Exploration is no longer first-run-only (0.5.0). The same read-only look
described above, same question shapes, same no-cost bounds, is now available
on request at any point in a session once `scaffold-wiki/` exists, just by
asking in plain words. Before the wiki exists, first run's own invitation
above is still the entry point. If a task is already open, asking pauses it,
runs the exploration, and picks the task back up exactly where it left off.

Running a 0.2.0-era install? Run `/plugin marketplace update` to pick up
all three changes.

## Who makes this

Kay Ashaolu. Continuing Lecturer at UC Berkeley School of Information, 15+
years as a software engineer and engineering manager (AncestryDNA, Morgan
Stanley). The mission in one line: teaching engineers how to direct AI and
still get stronger doing it.

[systemthinkinglab.ai](https://systemthinkinglab.ai/?ref=scaffold) ·
[Course 0, $99](https://systemthinkinglab.ai/course-0.html?ref=scaffold) ·
[Courses I-IV, $299](https://systemthinkinglab.ai/courses-i-iv.html?ref=scaffold) ·
[The 7 building blocks, free](https://systemthinkinglab.ai/learn?ref=scaffold)
