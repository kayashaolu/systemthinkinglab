# The 7 Building Blocks + 3 External Forces (quick reference for decomposition)

Every system is composed of seven primitives plus three external entities. To review a design, first decompose it into these, then check that each block is the right one for its job and that every force is answered by a block.

## The 7 blocks

**Task primitives (blue)**
- **Service** — synchronous; the caller waits for the answer. (request/response, an API endpoint, the thing a user waits on)
- **Worker** — asynchronous; runs after the caller has moved on. (background jobs, retries, fan-out, scheduled processing)

**Storage primitives (pink)**
- **Key-Value Store** — O(1) lookup by a single key. (caching, sessions, counters, hot config) — *the latency block.*
- **File Store** — blobs. (images, video, documents, uploads/downloads, CDN-fronted assets)
- **Queue** — durable, decoupled hand-off between producer and consumer. (buffering, smoothing spikes, absorbing failure) — *the reliability block.*
- **Relational Database** — structured data with relationships and transactions. (the source of truth; ACID)
- **Vector Database** — similarity search over embeddings. ("find things like this," RAG, recommendations)

## The 3 external forces (the "why" that drives block selection)

- **User** — a human is waiting → drives Service, latency, availability.
- **External Service** — a third party you do not control (an API, an LLM, a payment processor) → drives reliability, fault-tolerance, security; usually wants a Worker buffer with retries.
- **Time** — scheduled or time-driven work, TTLs, deadlines → drives Worker + Time, consistency windows, durability.

## The decomposition move

For each feature in the design, ask **"what force is acting, and which block answers it?"**
- A user is waiting → a **Service**.
- Work that can happen after the user is gone → a **Worker** (usually fed by a **Queue**).
- Data with relationships → a **Relational Database**; single-key hot reads → a **Key-Value Store**; blobs → a **File Store**; "find similar" → a **Vector Database**.
- A flaky/slow External Service → a **Worker** with retries + a **Queue** to absorb it.

Review checks that fall out of the decomposition:
- **Wrong block for the job** — the block present does not match the access pattern or the force (image in the RDB; sync call that should be async).
- **Missing block** — a force with no block answering it.
- **Over-engineering** — a block answering a force that is not actually present yet (restraint).
