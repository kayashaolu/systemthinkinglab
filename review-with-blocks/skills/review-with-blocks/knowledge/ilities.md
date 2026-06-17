# The "-ilities" — the non-functional review rubric

The structural pass (blocks + forces) says *what the system is*. The -ilities say *whether it survives contact with reality* — the difference between "it works on my laptop" and "it holds up at 3am."

**Do not run all of these on every review.** Select the ones the system's **forces and stakes** make load-bearing, and say which you are setting aside and why. A draft-only app may not need durability; a payments app lives or dies on it. Naming which -ilities matter *here* is the senior move.

For each load-bearing -ility, rate it **`holds` / `at-risk` / `gap`**, tie it to the block(s) that should carry it, and name the **tradeoff** (every -ility you buy costs another).

## The 7 core -ilities

| -ility | The question it asks | Block(s) that add it | Common failure it catches | What it costs (tradeoff) |
|--------|----------------------|----------------------|---------------------------|--------------------------|
| **Latency / Performance** | What is the user-perceived time, and what is on the critical path? | **KV cache**, precompute **Worker** (fan-out on write), **File Store + CDN**, **Vector DB** for similarity | Expensive work on the read path that should be precomputed | Caching costs **consistency** (stale reads); precompute costs **write complexity** |
| **Scalability** | What breaks first at 10x / 100x — read path or write path? | stateless **Service**, **Queue + Worker** (absorb spikes), **KV cache**, **RDB read replicas** | Fan-out on read instead of write; an unindexed hot query | Statelessness pushes state into KV/RDB; queues add **latency** |
| **Reliability** | Does the work complete correctly even when a dependency fails mid-way? | **Queue** (durably hold the work) + **Worker** (retry, idempotency, dead-letter) | Fire-and-forget work with no retry / dead-letter | Async reliability costs **immediacy** (no synchronous result) |
| **Availability** | What is the blast radius when one component is down? | **Queue** (decouple so failure does not cascade), redundant **Services**, **KV** (serve last-known-good) | One slow External Service takes the whole request down | Often trades against **consistency** (serve stale to stay up — CAP) |
| **Durability** | Can data be lost? Where? | **File Store**, **Relational DB** (committed rows), **persistent Queue** | Acknowledging a write before it is persisted | Sync persistence + replication cost **latency** and **money** |
| **Consistency** | Is stale or conflicting data possible, and is that acceptable here? | **Relational DB** (ACID), disciplined **KV cache invalidation**, clear **state ownership** | A cache serving a value whose owner already changed | Strong consistency costs **availability + latency** (coordination) |
| **Security** | Who can reach what; where does untrusted input enter; who owns the data? | **Service** as the auth/validation boundary, **data ownership**, **External Service** trust boundary | Trusting an External Service's response without validation | Adds **latency/friction** and **complexity** |

## How the 3 forces drive the -ilities (outside-in)

- **User** → latency, availability, scalability (the read/write paths the user touches).
- **External Service** → reliability, fault-tolerance, security (the dependency you do not control).
- **Time** → consistency, durability, recoverability (scheduled work, TTLs, replays).

## Observability — the cross-cutting thread (not a block you add)

Observability does not fit "add a block to get it." You do not add a block — you **instrument the seams *between* blocks** (logs, metrics, traces at every handoff). The blocks are where work happens; the handoffs are where bugs hide and where you watch. When reviewing, ask: *when this breaks at 3am, can they tell which handoff failed?* Flag designs where a Service returns success before downstream work finished with no trace across the boundary.

## The folded-in mechanisms (judge inside Reliability / Availability)

- **Fault-tolerance / Resilience** — timeouts, circuit breakers, back-pressure (Worker + Queue). Judge under Reliability/Availability.
- **Recoverability** — replay, idempotency, backups (Queue replay + idempotent Worker). Judge under Reliability/Durability.

## On the bench (raise only if the design makes them load-bearing)

- **Cost-efficiency** — right block for the access pattern (don't run a Vector DB for a KV-shaped lookup).
- **Maintainability / Modularity** — correct block boundaries = the seams; one block doing three jobs is the smell.
- **Testability** — can each block be exercised in isolation (stateless Services, pure Workers).

## The judgment that makes a review a review

Name which -ilities this system needs, which it can sacrifice, and what each choice costs. "Make it all scalable, consistent, durable, and available" is impossible (CAP and friends) and is a wish list, not a review. The senior output is an **-ility budget**: these two or three matter here, this one we sacrifice, and here are the blocks and the tradeoffs.
