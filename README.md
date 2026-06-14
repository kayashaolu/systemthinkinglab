# Systems Thinking Lab — Claude Code tools

A marketplace of [Claude Code](https://claude.com/claude-code) plugins from
[Systems Thinking Lab](https://systemthinkinglab.ai).

## Install

Add the marketplace once:

```
/plugin marketplace add kayashaolu/systemthinkinglab
```

Then install any tool:

```
/plugin install design-with-blocks@systemthinkinglab
/plugin install scaffold@systemthinkinglab
```

Updates later are just `/plugin marketplace update systemthinkinglab`.

## The tools

| Plugin | What it does |
|--------|--------------|
| **design-with-blocks** | Design an app using the 7 Universal Building Blocks: describe it in plain English, decompose features into blocks, get per-block technology recommendations, and output a buildable design doc. Free and public. |
| **scaffold** | An AI mentor for junior engineers: plan-first coaching on every task, a compounding wiki of codebase knowledge, and an honest ledger of what you've actually demonstrated you know. *(Currently in private beta.)* |

`scaffold` lives in a private repo during its beta — listed here, but only
installable by invited collaborators until it goes public.

## The framework

Every system, from Instagram to Stripe, is built from the same seven primitives
— Service, Worker, Key-Value Store, File Store, Queue, Relational Database,
Vector Database — plus three external entities: User, External Service, Time.
That vocabulary is the intellectual work of Kay Ashaolu, founder of Systems
Thinking Lab. If you want pattern literacy — the ability to design any future
system without a tool — that is what
[Course I: Universal Building Blocks](https://systemthinkinglab.ai) teaches.
