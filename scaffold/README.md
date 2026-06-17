# Scaffold

**An AI mentor for junior engineers.** It plans with you before it codes for
you, keeps an honest ledger of what you've actually demonstrated you know, and
turns every commit into a report on both your codebase and your growth.

Most AI coding tools optimize one thing: the code. Scaffold optimizes two,
with equal weight: the code, and *you*. Because a junior engineer is doing two
jobs at once — shipping and learning — and a tool that does the first while
silently skipping you past the second is how skills rot.

> *"What learning protects is your ability to build a mental model of why the
> code works, not the typing. AI only hurts that when it skips you past the
> model-building."*

Scaffold is the runnable version of that idea. It is derived from
[Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
— a persistent, compounding wiki the AI maintains — pointed at a new target:
**the wiki becomes an external representation of your understanding.**

## What it does

**Before you code: predict.** Give Scaffold a task and the first thing it asks
is what *you* think should change, and why. Then it shows its own plan as a
diff against yours: what you got right (banked as evidence), what it would
change (max five items, ordered by stakes, each tagged with the concept behind
it). When you genuinely disagree, it won't proceed until you've argued it out —
*"if we shipped your plan as-is, which of my items would bite first?"* The
back-and-forth is where judgement forms. An AI that only agrees teaches
nothing.

**Two ledgers, never merged.** The wiki keeps what the *AI* knows about your
codebase (`codebase/`, `concepts/`) strictly separate from what *you've
demonstrated* (`learner/`). Ask "what do I know?" and you get an honest answer
with receipts — dated evidence from real predictions and real commits, not
vibes. Ask "what are my gaps?" and every gap comes with the page to read and a
task that would close it.

**Three mastery levels, mechanically earned — and they never go down.**
*Learning* → *understanding* (2 unaided correct predictions) →
*internalizing* (you applied it somewhere new, or you caught Scaffold's own
miss). A level records the best you've demonstrated, like a belt — knowledge
gets rusty, it doesn't get revoked. Two misses in six weeks flags the concept
for review instead: Scaffold steers tasks at it until two clean reps clear
the flag, always with the exact page to re-read and a task that re-proves it.
Honest, never cruel: warm AND direct, never one without the other.

**Every commit compounds.** After each commit: the most valuable thing the
commit taught about the codebase, what changed, what the wiki learned, and
what *you* learned. Threads that recur across commits get named. Nothing
disappears into chat history.

## Install

Scaffold is a [Claude Code](https://claude.com/claude-code) plugin, distributed
through the Systems Thinking Lab marketplace. Install it from inside Claude Code:

```
/plugin marketplace add kayashaolu/systemthinkinglab
/plugin install scaffold@systemthinkinglab
```

That's it — updates later are just `/plugin marketplace update systemthinkinglab`.

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

First run creates `scaffold-wiki/` (gitignored — your ledger is yours), does a
light pass over the codebase, and you're working. From then on it engages
automatically in that repo.

## The architecture, in its own vocabulary

Scaffold describes every codebase using seven building blocks (Service,
Worker, Key-Value Store, File Store, Queue, Relational Database, Vector
Database) and three external entities (User, External Service, Time) — a
minimum viable vocabulary for system structure, from
[Systems Thinking Lab](https://systemthinkinglab.ai?ref=scaffold). Scaffold
itself, in that vocabulary:

- **User** (you) → **Service** (the mentor session: plans, diffs, answers)
- **Time** (every git commit) → **Worker** (the commit report: integrates what
  happened into the wiki)
- **File Store** (the wiki — plain markdown, the durable compounding artifact)
- **External Service** (git — the record of what actually happened)

No server, no database, no telemetry. The whole product is markdown, prompts,
and conventions — the leverage is in the scaffolding, not the machinery.

## FAQ

**Will it slow me down?** A size gate keeps the ritual proportional: typo-level
changes skip it entirely, and the full loop charges one "struggle toll" per
task, capped at minutes. If you tell it to just fix something, it pushes back
once — then does it. It never holds work hostage.

**Who can see my ledger?** Nobody. The wiki is plain markdown on your machine,
gitignored by default, sent nowhere. Sharing it with a mentor is your call,
never a default.

**Does it work with other agents?** The skill format is Claude Code's, but the
wiki schema is plain markdown — `scaffold-wiki/SCHEMA.md` is readable by any
agent, and porting the loop to an AGENTS.md is straightforward. PRs welcome.

**Is this a course?** No — it's free and it works on your real job. If the
concepts it keeps tagging in your diffs make you want the deeper treatment,
that's what [the courses](https://systemthinkinglab.ai?ref=scaffold) are for.

## Status

v0.1 — an experiment in public. The loop, the mastery rules, and the coaching
voice were calibrated through persona trials and real-junior dogfooding;
expect rough edges anyway. Issues and field reports very welcome.
