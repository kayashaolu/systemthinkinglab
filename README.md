# Systems Thinking Lab: Free Engineering Tools

Free tools from [Systems Thinking Lab](https://systemthinkinglab.ai), installable as
[Claude Code](https://claude.com/claude-code) plugins or, for other coding agents, as
Agent Skills (see Install below). Scaffold is the workflow; design-with-blocks and
review-with-blocks apply the seven building blocks (see The tools and The framework below).

## Install

Add the marketplace once:

```
/plugin marketplace add kayashaolu/systemthinkinglab
```

Then install any tool:

```
/plugin install design-with-blocks@systemthinkinglab
/plugin install review-with-blocks@systemthinkinglab
/plugin install scaffold@systemthinkinglab
```

Updates later are just `/plugin marketplace update systemthinkinglab`.

For agents other than Claude Code:

```
npx skills add kayashaolu/systemthinkinglab --skill design-with-blocks
npx skills add kayashaolu/systemthinkinglab --skill review-with-blocks
npx skills add kayashaolu/systemthinkinglab --skill scaffold
```

Each skill lands in your project's `.agents/skills/<name>/` as an Agent Skill; they are built and tested in Claude Code.

## The tools

| Plugin | What it does |
|--------|--------------|
| **design-with-blocks** | Design an app using the 7 Universal Building Blocks: describe it in plain English, decompose features into blocks, get per-block technology recommendations, and output a buildable design doc. |
| **review-with-blocks** | Review a finished system design against the 7 building blocks and the non-functional "-ilities": decompose it, flag wrong/missing/over-engineered blocks, rate each load-bearing -ility (holds / at-risk / gap) with its tradeoff, and surface the questions a senior would ask. |
| **scaffold** | A plan-first developer workflow, run by an AI mentor: it predicts before it builds, keeps a compounding wiki of your codebase, and holds an honest ledger of what you've demonstrated you know, in craft or direction mode. |

All three are free, open source (Apache-2.0), and installable by anyone. Together they cover the arc **design → build → review**: design-with-blocks plans the architecture, scaffold runs the plan-first workflow while you build it, and review-with-blocks judges the result. All three use the seven building blocks Courses I-IV teach in full; the path starts with Course 0.

## The framework

Every system, from Instagram to Stripe, is built from the same seven primitives:
Service, Worker, Key-Value Store, File Store, Queue, Relational Database,
Vector Database; plus three external entities: User, External Service, Time.
That vocabulary is the intellectual work of Kay Ashaolu, founder of Systems
Thinking Lab. If you want pattern literacy, the ability to design any future
system without a tool, you can learn the 7 building blocks for free at
[systemthinkinglab.ai/learn](https://systemthinkinglab.ai/learn?ref=marketplace).
