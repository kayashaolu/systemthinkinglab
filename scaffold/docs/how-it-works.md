# How Scaffold works (and why it exists)

## The claim

The standard worry: AI will rot junior engineers' skills — they'll ship code
they don't understand and never build judgement. The standard prescription —
make juniors code by hand like previous generations did — fails on contact:
juniors watching peers ship 5x faster cannot sustain hand-coding by willpower,
and insisting they learn through the previous generation's medium is not
rigor, it is nostalgia.

The actual answer is scaffolding: AI that *protects the model-building* while
doing the typing. What learning protects is your ability to build a mental
model of why the code works — AI only hurts that when it skips you past the
model-building. So don't skip it. Make it the first step of every task.

## The mechanism

Three pieces, each doing one job:

**1. Predict before reveal.** On every non-trivial task, you state what you
think should change and why — *before* the AI shows its hand. This is the
single highest-leverage move in the system: it converts every work task into a
testable prediction, and predictions are how mental models get built and
checked. The AI's plan then arrives as a diff against yours, so the delta —
the thing you didn't see — is explicit, named, and tagged with the concept
behind it.

**2. The two-ledger wiki.** Derived from Karpathy's LLM Wiki pattern: a
persistent markdown wiki the AI maintains, compounding with every task. The
twist is the split. One ledger holds what the *AI* knows (codebase map,
concept pages). The other holds what *you have demonstrated* — every entry a
dated, signed piece of evidence from a real prediction or a real commit. The
wiki becomes an external representation of your understanding, which is what
makes "what do I know?" and "what are my gaps?" honestly answerable.

**3. The adversarial loop, both directions.** When your plan and the AI's
genuinely conflict, the loop stops and makes you argue: *which of its items
would bite first if you shipped your plan?* And the reverse is scored too —
catching the AI's miss is the strongest evidence in the system, the thing
that promotes a concept to *internalizing*. A junior who argues with their AI
daily is doing judgement reps that previous generations had to wait years for
permission to do.

## Why ratings never go down (and why that isn't a participation trophy)

A level records the best you've demonstrated, like a belt — knowledge gets
rusty, it doesn't get revoked. But a ledger that only flatters is worthless,
so the honesty lives elsewhere: every miss is recorded as dated evidence, and
two misses inside six weeks set a **review flag** by mechanical rule. The
flag, not the level, does the work — it steers tasks at the rusty concept
until two clean unaided reps clear it, always with the exact page to re-read
and a task that re-proves it. You never watch a rating drop; you watch a
review queue that tells the truth. An AI that only agrees teaches nothing —
and one that punishes rust teaches you to hide it.

## Two modes: craft and direction

Everything above describes **craft mode** — you and your junior engineer (the
agent) in the loop together, predicting and diffing on every task. It's the
default, and for most work it's the right one.

**Direction mode** is a different kind of rep. You write a brief — a goal,
falsifiable done-criteria, and your own bounds on how long the run gets to
take. A builder-and-breaker pair (the breaker's job is only to find what
the builder missed — Scaffold calls it "the breaker" by default, and you can
rename it in your own wiki) then iterates inside those bounds, on their own,
and stops on one of five enumerated conditions: the criteria were met, the
round cap or time box was hit, it got stuck, or you interrupted it. What
comes back is a diff plus findings attached to it — never a verdict, never a
recommendation to ship. You make the go/no-go call yourself, every time.

The brief is the prediction; the go/no-go is the judgment call being scored.
It's the same mechanism as craft mode's predict-then-diff, aimed at a
different skill: not "did I get the code right," but "did I direct this
right, and did I know when to trust what came back." Every direction-mode run
writes one entry to a third, narrative artifact — the **judgment log** — that
takes no signed marks, because a narrative isn't a falsifiable claim the way
a prediction is. It's the record of what you pushed back on and why, in your
own words, that the mastery ledger can't hold.

## Why every commit reports

The commit is the heartbeat. Each one integrates what happened into the wiki
and surfaces what recurred — the third task that died at the same queue
boundary is a pattern, and patterns walk in before explanations. Nothing
valuable disappears into chat history; good answers get filed back. That is
what "compounding" means operationally: the scaffolding is better on task
fifty than on task five, and so are you.
