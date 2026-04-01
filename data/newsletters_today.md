# Newsletter Digest



## Email 1

**Source:** TLDR Data <dan@tldrnewsletter.com>

**Date:** Mon, 30 Mar 2026 10:15:28 +0000

**Subject:** SQLMesh Goes Neutral 🤝, Notion’sVector Search Infra ⚡, Speed vs Discipline⚠️


### Content

Fivetran is donating SQLMesh (its SQL-based transformation framework
acquired via Tobiko Data last September) to the Linux
Foundation
DEEP DIVES
HOW NOTION SCALED AI Q&A TO MILLIONS OF WORKSPACES (11 MINUTE READ)
Notion's AI Q&A platform scaled to millions of users by evolving its
vector search architecture through dual ingestion, page state
optimization, a serverless migration, and a switch to turbopuffer.
These engineering decisions resulted in a 600x onboarding increase,
60% lower search costs, and p50 latency improving to 50–70ms, while
Ray and Anyscale led to a 90%+ reduction in embeddings infrastructure
costs. The system is now simpler, significantly more cost-efficient,
and supports real-time, semantically rich document retrieval at
enterprise scale.
ANALYZING ROUND-TRIP QUERY LATENCY (6 MINUTE READ) [5]
Instead of just looking at database execution time, Datadog focused
on round-trip query latency with custom-built observability to break
down this latency into components. This revealed hidden bottlenecks
such as connection pool contention, network latency spikes, and
inefficient result handling.
HOW TO BUILD TRACEABLE AI WORKFLOWS WITH RETRY AND DLQ VISIBILITY (6
MINUTE READ) [6]
Implementing fine-grained, node-based tracing within multi-step
extraction workflows, modeled as an append-only, serializable ledger,
enables deterministic visibility into otherwise opaque LLM-powered
data pipelines. Tracing each decision, retry, and DLQ routing as
distinct nodes not only preserves causal chains and enables efficient,
fine-grained cache invalidation but also transforms debugging and
replayability, allowing teams to precisely audit and re-run extraction
steps without system-wide reprocessing.
THE FOUNDATION — WHAT A/B INFRASTRUCTURE ACTUALLY DOES (9 MINUTE
READ) [7]
EloElo built a high-performance traffic routing engine that assigns
users to experiment variants in real time, ensures consistent
assignment (stickiness) where needed, tracks metrics, and supports
gradual traffic ramp-ups. The architecture evolved from a memory-heavy
V1 (Redis HashMaps) to an efficient V2 using Redis BitFields (3 bits
per user, sharded for scale), and a stateless V3 for non-sticky
experiments.
OPINIONS & ADVICE
AI IS HERE, BUT THE HARD PARTS HAVEN'T CHANGED (8 MINUTE READ) [8]
AI adoption is now nearly universal (99.5% use AI tools, 82% daily or
more), with Claude dominating. However, AI hasn't solved the real hard
part: legacy systems, lack of leadership, poor requirements, and data
modeling and semantic layers. AI speeds up output, but risks creating
more technical debt and "production cesspools" if fundamentals like
context, ownership, and architecture are skipped.
ARCHITECTURAL GOVERNANCE AT AI SPEED (12 MINUTE READ) [9]
GenAI makes code cheap, but architecture alignment is now the
bottleneck. Traditional governance doesn't scale. The solution is
declarative architecture: encode decisions as machine-readable,
enforceable constraints embedded in dev tooling and made available to
agents (think “Architecture.md”). This shifts governance from
human review to automated guardrails, enabling autonomous teams/agents
while preventing drift. Make the correct path the default path, with
bounded, composable “slices” for safe evolution.
LAUNCHES & TOOLS
YOUR PIPELINE WORKS GREAT FOR 3 DATA SOURCES. WILL IT WORK WITH 30?
FIVETRAN DONATES ITS SQLMESH DATA TRANSFORMATION FRAMEWORK TO THE
LINUX FOUNDATION (2 MINUTE READ) [12]
Fivetran is donating SQLMesh (its SQL-based transformation framework
acquired via Tobiko Data last September) to the Linux Foundation to
push vendor-neutral governance of the transformation layer. SQLMesh
brings testing, versioning, and Terraform-like plan/apply workflows to
SQL pipelines. The strategic play: shape the open data infrastructure
standard (alongside dbt) and drive adoption via community ownership.
DATAHIKE (GITHUB REPO) [13]
Datahike is a Datalog-based, immutable, Git-like database: every
write creates a new snapshot you can query, branch, and audit. It
combines time-travel, versioning, and distributed reads (no server
required) with pluggable storage (S3, files, and JDBC).
MONITORING YOUR FEAST FEATURE SERVER WITH PROMETHEUS AND GRAFANA (5
MINUTE READ) [14]
Feast adds built-in monitoring to the feature server using Prometheus
and OpenTelemetry, making it observable like any production API. Teams
can track latency, throughput, feature retrieval, and system health,
enabling proper SLOs and alerting.
MISCELLANEOUS
AI HELPING BUILD BETTER AI: HOW AGENTS ACCELERATE MODEL
EXPERIMENTATION (7 MINUTE READ) [15]
LinkedIn built AI agents to accelerate model experimentation and
infrastructure work, particularly for optimizing LLM post-training and
migrating large TensorFlow models to PyTorch. Its flagship agent,
Autopilot for Torch, generates code/configurations, runs automated
verifiers for correctness (trainability, numerical stability, and
metric parity), and receives structured feedback to improve in loops.
WHY UUID PRIMARY KEYS QUIETLY DESTROY DATABASE PERFORMANCE (5 MINUTE
READ) [16]
Random UUIDv4 primary keys hurt database performance by causing
random inserts, frequent page splits, fragmentation, and poor cache
efficiency in B+ tree storage engines, while time-ordered IDs (like
UUIDv7/ULID) or using a sequential internal key with a UUID secondary
index restore sequential writes and significantly improve efficiency.
QUICK LINKS
MERMAID (TOOL) [17]
Mermaid turns plain text, Markdown-style code, or natural language
into diagrams like flowcharts, ERDs, and timelines in seconds.
BUILDING A PRODUCTION-GRADE MULTI-NODE TRAINING PIPELINE WITH PYTORCH
DDP (8 MINUTE READ) [18]
A modular, production-ready PyTorch DDP pipeline for multi-node,
multi-GPU training.


---

## Email 2

**Source:** TLDR <dan@tldrnewsletter.com>

**Date:** Mon, 30 Mar 2026 10:43:16 +0000

**Subject:** Anthropic model leaks 🤖, OpenAI Anthropic feud 💼, important AI ideas🧠


### Content

A configuration error in Anthropic's content management system exposed
a draft blog post describing a new model called Claude
Mythos
✂️ CUT YOUR QA CYCLES DOWN TO MINUTES WITH AUTOMATED TESTING
BIG TECH & STARTUPS
ANTHROPIC READIES MYTHOS MODEL WITH HIGH CYBERSECURITY RISK (3 MINUTE
READ) [9]
A configuration error in Anthropic's content management system
exposed a draft blog post describing a new model called Claude Mythos.
The model is reportedly larger and more intelligent than the Opus
models. The draft warns that the model poses unprecedented
cybersecurity risks as it is far ahead of any other AI model in cyber
capabilities. Mythos is extremely compute-intensive and expensive to
serve - Anthropic is working on making it much more efficient before
any general release.
THE DECADELONG FEUD SHAPING THE FUTURE OF AI (14 MINUTE READ) [10]
Dario Amodei and Sam Altman clashed for years when Amodei was still
at OpenAI. The final split happened toward the end of 2020, after a
disagreement over whether OpenAI should be a market company or a
public-good company. Dario left with nearly a dozen OpenAI employees.
Within five years, Anthropic would be lining up banks, racing toward
an initial public offering before its founders' former employer.
SCIENCE & FUTURISTIC TECHNOLOGY
I'VE TAKEN AGENCY IN THE TREATMENT OF MY BONE CANCER (WEBSITE) [11]
Sid Sijbrandij ran out of standard care treatments for bone cancer,
so he started creating treatments for himself. This site details his
journey and the results of the treatments so far. Sijbrandij's cancer
is now in remission. He is now working with companies to scale his
approach for others.
“SUPER BIZARRE” – NEUROSCIENTISTS DISCOVER THAT ADULT BRAIN IS
FILLED WITH MILLIONS OF “SILENT SYNAPSES” (5 MINUTE READ) [12]
Scientists have discovered a surprisingly large reserve of silent
synapses in the adult brain. These unused neural connections can be
rapidly activated to store new memories. This system allows the brain
to create new memories without overwriting the important memories
stored in mature synapses. If silent synapses decline with age or
disease, it could help explain why learning new skills or adapting to
change becomes more difficult over time.
PROGRAMMING, DESIGN & DATA SCIENCE
MISCELLANEOUS
THE MOST IMPORTANT IDEAS IN AI RIGHT NOW (11 MINUTE READ) [16]
The most important ideas in AI right now are autonomous component
improvement, the transition to intent-based engineering, the move from
opacity to transparency, the realization that most work is
scaffolding, and the idea that expertise gets diffused into public
knowledge. The speed of improvement in many fields is about to
accelerate beyond anything we've ever seen. The new bottleneck is
being able to say what you actually want. Every organization is going
to converge on the same cycle: define what you're trying to do,
execute with agents, log everything, collect failures, and let the
system improve itself.
BUYING DEEPMIND (14 MINUTE READ) [17]
Google bought DeepMind for $650 million at the end of January 2014.
It poured billions into DeepMind's research, but it took a decade for
the quest for superintelligence to go into overdrive. This article
tells the inside story of how Google ended up purchasing the startup
and the specific terms of the final deal.
QUICK LINKS
MIRRORD — GIVE AI CODING AGENTS REAL-WORLD CONTEXT SO THEY WRITE


---

## Email 3

**Source:** TLDR Fintech <dan@tldrnewsletter.com>

**Date:** Mon, 30 Mar 2026 13:15:57 +0000

**Subject:** NYSE-parent invests in Polymarket 💸,Revolut profit soars 🚀, Visa subscription management 🗞️


### Content

Intercontinental Exchange invested an additional $600M into
Polymarket, completing a $2B commitment and signaling growing
institutional
interest
NEWS & TRENDS
NYSE-PARENT COMPLETES $2B INVESTMENT IN POLYMARKET AS PREDICTION
MARKETS GO MAINSTREAM (3 MINUTE READ) [5]
NYSE-parent Intercontinental Exchange (ICE) invested an additional
$600M into Polymarket, completing a $2B commitment and signaling
growing institutional interest in prediction markets as a data and
trading layer. ICE plans to leverage Polymarket's real-time sentiment
data to inform investment decisions, while the broader industry sees
rising valuations and adoption despite regulatory scrutiny. Prediction
markets are moving from fringe products toward integration with
traditional financial infrastructure and analytics.
REVOLUT PROFIT SOARS TO RECORD $2.3 BILLION IN 2025, PLANS UK LENDING
(3 MINUTE READ) [6]
Revolut reported a record $2.3 billion in profit for 2025, fueled by
strong fee-based revenue across its growing global user base. The
company is now doubling down on becoming a primary banking provider,
rolling out credit cards, personal loans, and overdrafts in the UK
while expanding its lending portfolio. As it pushes deeper into
traditional banking territory and eyes global expansion, its long-term
bet is clear: convert millions of secondary users into full-service
banking customers.
MASTERCARD BIDS TO OFFLOAD NETS PAYMENTS UNIT BOUGHT FOR $3.2BN (2
MINUTE READ) [7]
Mastercard is trying to find a buyer for the real-time payments
business it acquired for $3.2 billion from Danish outfit Nets in 2019.
DEEP DIVES & REPORTS
AGENTIC PAYMENTS COULD UNLOCK NEW MONETIZATION FOR CONTENT PLATFORMS
(4 MINUTE READ) [8]
Agentic payment infrastructure enables new business models beyond
subscriptions, including pay-per-article, pay-to-preview for AI
crawlers, paid comments, and tipping, allowing creators to monetize
without sacrificing reach. The core shift is from fixed monetization
models to configurable, multi-layered revenue streams aligned with
both human and AI consumption. Payments embedded at the protocol level
could rebalance incentives, reduce spam, and expand total revenue
across the content ecosystem.
AMERICA'S CFOS SAY AI IS COMING FOR ADMIN JOBS (2 MINUTE READ) [9]
A survey of ~750 CFOs shows AI is expected to modestly reduce overall
headcount, about 0.4%, but disproportionately impact clerical and
administrative roles while benefiting higher-skilled workers. The
shift reflects classic skill-biased technological change, with AI
augmenting technical roles rather than replacing them. The key
implication is a gradual workforce reallocation, not mass layoffs,
with entry-level pathways at the greatest risk.
WALLET WARS PT 4: THE PERSONAL FINANCE AGENT (15 MINUTE READ) [10]
The next wave of consumer fintech isn't an app. It's a personal
agent. Nobody's built the product yet. In the guardian agent war,
there isn't a winner yet. Maybe it's a partnership, an acquisition, or
a company we haven't seen yet. One that starts with the agent-first
assumption and builds backward into financial infrastructure. The way
Stripe started with developers and built backward into the financial
system.
THE CLARITY ACT BANNED STABLECOIN YIELD TO PROTECT BANKS (6 MINUTE
READ) [11]
A proposed US crypto bill is reshaping the stablecoin landscape by
restricting interest earned simply from holding these assets,
triggering sharp market reactions. The change undercuts the
revenue-sharing model behind USDC, wiping billions in value from
related companies while leaving competitors like Tether unaffected and
potentially advantaged. As policymakers leave decentralized finance
largely undefined, capital may increasingly flow toward DeFi platforms
where yield remains available, creating an unintended shift in where
value accrues.
US LAWMAKERS PUSH FOR TOKENIZED SECURITIES: WHAT IT MEANS FOR CRYPTO
MARKETS (5 MINUTE READ) [12]
US policymakers are accelerating efforts to bring blockchain-based
versions of traditional financial assets under clearer regulatory
frameworks, signaling a shift toward integrating digital
infrastructure into mainstream markets. Recent guidance from
regulators and growing bipartisan support suggest tokenized stocks and
bonds will be treated like their traditional counterparts, unlocking
institutional participation while maintaining strict compliance
standards. This momentum points to a future where crypto and
traditional finance converge, potentially improving market efficiency
but also reshaping how liquidity, oversight, and risk are managed.
LAUNCHES & PRODUCTS
BRIDGE ADDS GBP RAILS TO EXPAND STABLECOIN FIAT CONNECTIVITY (1
MINUTE READ) [13]
Bridge is expanding its fiat-to-stablecoin infrastructure with GBP
on- and offramps, enabling global businesses to move funds between
pounds and stablecoins via virtual accounts. The launch supports use
cases like payroll, payouts, remittances, and treasury, and builds
toward a multi-currency stack alongside USD, EUR, MXN, and BRL. The
broader trend is stablecoins evolving into a global financial backend
with localized fiat entry points.
VISA ROLLS OUT SUBSCRIPTION MANAGEMENT SERVICE (2 MINUTE READ) [14]
Visa has launched a service that helps issuers make it easy for their
customers to manage their subscriptions in-app. As the number of
subscriptions worldwide is projected to reach 12 billion by 2030,
consumers are seeking simple, transparent ways to track and manage
recurring charges.
STARLING ROLLS OUT AGENTIC AI MONEY MANAGER (2 MINUTE READ) [15]
Starling Bank has introduced a new AI-powered assistant that can
actively help users manage their finances through voice and natural
language interactions. The tool can execute banking tasks, track
spending, suggest budgets, and guide users toward savings goals, all
within a single interface built on Google Gemini.
MISCELLANEOUS
KLARNA STRUGGLES WITH LOAN LOSS ACCOUNTING (3 MINUTE READ) [16]
Klarna's push into longer-term consumer lending is driving strong
growth but also increasing upfront loss provisions, which has
pressured its stock despite underlying profitability. The accounting
dynamic, where losses are recognized immediately while revenue is
spread over time, is creating near-term earnings volatility and
investor concern. The key tension is whether Klarna can balance rapid
lending expansion with disciplined credit risk and clearer financial
execution.
GOLDMAN'S NEW ADVISER RISHI SUNAK URGES SMALL FIRMS TO ADOPT AI (2
MINUTE READ) [17]
Rishi Sunak, now a Goldman Sachs adviser, is urging small businesses
to rapidly adopt AI, warning that failure to do so increases the risk
of being outcompeted by larger firms. At Goldman's UK small business
summit, adoption is already widespread, with 98% of surveyed firms
using AI in some capacity. The broader signal is that AI is becoming
table stakes for competitiveness, even among traditional and highly
regulated small businesses.
UBS RECEIVES FULL APPROVAL FOR US NATIONAL BANK CHARTER (1 MINUTE
READ) [18]
UBS has secured full approval for a US national bank charter, marking
a key step in expanding its domestic banking footprint. The approval
allows UBS Bank USA to broaden its product offerings and compete more
directly in everyday banking while deepening relationships with
clients and financial advisors. It also signals a longer-term push to
consolidate assets and accelerate growth in the US following its
integration of Credit Suisse clients.
QUICK LINKS
PLAID ACQUIRES THIS WEEK IN FINTECH TO EXPAND MEDIA AND COMMUNITY
STRATEGY (1 MINUTE READ) [19]
Plaid is acquiring This Week in Fintech, signaling a move to build a
media and community layer alongside its core infrastructure business.
FROM AUTOMATION TO AUTONOMY: INDIA'S NEXT BIG LEAP IN PAYMENTS (8
MINUTE READ) [20]
India's digital payments journey is already a global success.


---

## Email 4

**Source:** TLDR AI <dan@tldrnewsletter.com>

**Date:** Mon, 30 Mar 2026 13:44:30 +0000

**Subject:** Claude Mythos leaks 🤖, last xAI cofounder exits 👋, lessons from OpenAI💡


### Content

'Mythos' is the name for a new tier of Anthropic models that are
larger and more intelligent than Opus. The models get dramatically
higher
scores
BLACK DUCK SIGNAL: AGENTIC APPSEC BUILT FOR AI-NATIVE DEVELOPMENT
HEADLINES & LAUNCHES
CLAUDE MYTHOS (3 MINUTE READ) [5]
'Mythos' is the name for a new tier of Anthropic models that are
larger and more intelligent than Opus. The models get dramatically
higher scores on tests of software coding, academic reasoning, and
cybersecurity compared to Claude Opus 4.6. Mythos is a large,
compute-intensive model that is very expensive to use and serve.
Anthropic is working on making the model much more efficient before
any general release.
META TESTS AVOCADO 9B, AVOCADO MANGO AGENT, AND MORE (2 MINUTE READ)
Meta's Avocado model has been pushed back to at least May as it still
falls short of leading systems from competitors. The company appears
to be running parallel experiments with multiple Avocado variants. The
model appears to be able to solve complex math problems that earlier
Llama models could not, but these problems have already been solved by
other labs months earlier. Meta's AI leadership has reportedly
discussed temporarily licensing Google's Gemini technology. Some
requests within Meta AI are already being routed through Gemini
models.
ANTHROPIC'S CLAUDE POPULARITY WITH PAYING CONSUMERS IS SKYROCKETING
(4 MINUTE READ) [7]
Anthropic is more popular with customers than ever. Claude is gaining
paid subscribers in record numbers. Paid subscriptions have more than
doubled this year. The majority of new subscribers were in the lowest
tier. OpenAI is still gaining new paid subscribers at a rapid rate and
remains the biggest consumer AI platform.
DEEP DIVES & ANALYSIS
FUNCTION CALLING HARNESS: FROM 6.75% TO 100% (32 MINUTE READ) [8]
AutoBe is an open-source AI agent that takes a single natural
language conversation and generates a complete backend.
qwen3-coder-next has a 6.75% function calling success rate when asked
to generate API data types for a shopping mall backend. AutoBe boosts
that success rate up to over 99.8%. It uses a harness where type
schemas constrain outputs, compilers verify results, and structure
feedback pinpoints compactly where and why something went wrong so the
agent can correct itself. This post dissects the engineering behind
AutoBe.
AI'S CAPABILITY IMPROVEMENTS HAVEN'T COME FROM IT GETTING LESS
AFFORDABLE (12 MINUTE READ) [9]
AI's capability improvements at the frontier have not led to
increased inference costs relative to human labor. Despite rising
per-task inference costs, current models achieve tasks at roughly 3%
of human costs without any upward trend in median cost ratios. Models
can continue advancing even under strict cost constraints, enabling
profitable automation with AI cost ratios remaining well below human
levels.
THE CAPABILITY OVERHANG IN AI (4 MINUTE READ) [10]
Coding agents outperform other domains because codebases provide a
self-contained environment of critical context, unlike fragmented
knowledge work spread across video calls and legacy systems.
Enterprise adoption remains stalled by the three hard problems of
context fragmentation, complex access control, and a rapidly shifting
architecture landscape.
ENGINEERING & RESEARCH
SCHEDULE TASKS ON THE WEB (5 MINUTE READ) [11]
Claude Code on the web users can now schedule tasks. The tasks will
run on Anthropic-managed infrastructure, so they will keep working
even if users turn off their devices. Scheduled tasks are available to
all Claude Code on the web users. Example tasks include reviewing open
pull requests each morning, analyzing CI failures overnight and
surfacing summaries, syncing documentation after PRs merge, and
running dependency audits every week.
LAT.MD (GITHUB REPO) [12]
lat.md is a spec that agents keep in sync with the code base that
helps them understand big ideas and key business logic. It ensures
that corner cases have proper high-level tests that matter and can
speed up coding by saving agents from endless grepping. The spec uses
plain Markdown, with Wiki links connecting concepts into a navigable
graph.
WHAT PRETEXT REINFORCED ABOUT AI LOOPS (5 MINUTE READ) [13]
Pretext is a fast, accurate, comprehensive text measurement algorithm
that can lay out web pages without leaning on DOM measurement and
reflow. It was created using AI agent workflows. The particular loop
that was used in developing the tool (constrain -> measure -> isolate
-> classify -> test -> reject -> keep only what survives broad
pressure) made the engineering rigorous. This article analyzes the
loop to see what makes it so successful.
MISCELLANEOUS
XAI'S LAST COFOUNDER LEAVES (3 MINUTE READ) [14]
All remaining co-founders of xAI reportedly departed, marking the
complete exit of the original founding team.
THINGS I LEARNED AT OPENAI (7 MINUTE READ) [15]
OpenAI alumni emphasize the significance of creating effective
evaluations and benchmarks, noting that the best benchmarks drive
collective optimization efforts. Post-training data design and model
alignment are critical for unlocking new AI capabilities, particularly
in subjective attributes like empathy or creativity. Fast iteration,
choosing the right problems, and leveraging internal tooling are key
competitive advantages in AI research.
QUICK LINKS
THREE WEEKS AGO THERE WERE RUMORS THAT ONE OF THE LABS HAD COMPLETED
ITS LARGEST EVER SUCCESSFUL TRAINING RUN (2 MINUTE READ) [17]
That lab was likely Anthropic, which trained Mythos.
LIVE TRANSLATE COMES TO HEADPHONES ON IOS (4 MINUTE READ) [18]
Google rolled out real-time translation through headphones on iOS,
expanding support to more countries and 70+ languages while preserving
speaker tone and cadence.
WHY AI IS NOT KILLING THE CYBERSECURITY INDUSTRY, BUT EXPANDING IT
EXPONENTIALLY - THOUGHTS FROM RSA (10 MINUTE READ) [19]
AI-powered exploitation can attack systems at a scale never possible
before.


---

## Email 5

**Source:** TLDR <dan@tldrnewsletter.com>

**Date:** Tue, 31 Mar 2026 10:41:10 +0000

**Subject:** Apple's AI strategy 🤖, Codex for Claude Code 🤖, Inside Sora's fall🎥


### Content

Apple is recommitting to its core business model of selling hardware
and services. It knows its homegrown AI technology lags behind
competitors
BIG TECH & STARTUPS
THE SUDDEN FALL OF OPENAI'S MOST HYPED PRODUCT SINCE CHATGPT (14
MINUTE READ) [5]
Sora was hyped as AI's next consumer-friendly frontier, and even
Disney signed onto the vision. OpenAI then suddenly killed the
project, with many Disney executives learning about the decision less
than an hour before it was announced. OpenAI needed to free up more
computing resources, and Sora was using far too much. The product
wasn't profitable, and every user drew down a finite resource. CEO Sam
Altman says the move was a difficult but necessary sacrifice toward
the company's larger goals.
APPLE PIVOTS ITS AI STRATEGY TO APP STORE, SEARCH-LIKE PLATFORM
APPROACH (13 MINUTE READ) [6]
Apple is recommitting to its core business model of selling hardware
and services. It knows its homegrown AI technology lags behind
competitors, so it is focusing on its core strengths. Historically,
Apple's software has been about driving product sales rather than
generating revenue in their own right. It plans to embed just enough
AI in its OSes to keep users from defecting, while opening Siri and
Apple Intelligence to third-party services. This approach leverages
its hardware, makes its products more customizable, and keeps the
company in control of its ecosystem.
SCIENCE & FUTURISTIC TECHNOLOGY
INSIDE THE STEALTHY STARTUP THAT PITCHED BRAINLESS HUMAN CLONES (29
MINUTE READ) [7]
A Californian startup called R3 has raised funds to create
non-sentient monkey 'organ sacks' as an alternative to animal testing.
The startup's founder reportedly secretly pitched a vision where the
startup creates 'brainless clones' to serve as backups for human
bodies. This could be in the form of a baby version of a person with
enough brain structure to be alive in case they ever need a new kidney
or liver, or it may even be possible to one day transplant a brain
into a younger clone to gain a second lifespan. The company has denied
that it ever made the pitch, saying that any allegations of intent or
conspiracy to create human clones or humans with brain damage are
categorically false.
VULNERABILITY RESEARCH IS COOKED (16 MINUTE READ) [8]
Coding agents will soon drastically alter both the practice and the
economics of exploit development. A substantial amount of the
high-impact vulnerability research will just be pointing an agent at a
source three and telling it to find zero days. This will profoundly
alter information security and the Internet itself.
PROGRAMMING, DESIGN & DATA SCIENCE
MISCELLANEOUS
TO LURE TOP AI TALENT, STARTUPS ARE TURNING TO COLD HARD CASH (6
MINUTE READ) [13]
High-growth AI startups are flush with venture capital. Combined with
a wildly competitive talent market, this has caused increasingly
creative incentive structures and more cash-heavy offers. Startups are
focusing on hiring the best as they need to stay lean and small. This
is creating a split economy in the tech industry where the top 5% to
10% of candidates are getting all of the offers and the rest are
struggling.
SEEING LIKE A SPREADSHEET (28 MINUTE READ) [14]
AI will see much further than the spreadsheet ever could. It will
allow businesses to accomplish incredible things, and make possible
coordinations of labor and capital more ambitious than anything we can
imagine today. However, as corporations become dominated by AI
systems, the most human elements of organizations may be devalued or
discarded entirely. Great organizations are great because of something
irreducible about the collection and organization of particular people
toward particular ends.
QUICK LINKS
🎁 GET 1 FREE MONTH OF GRANOLA - THE AI NOTEPAD YOU KEEP HEARING
META TESTING PAID INSTAGRAM SERVICE THAT LETS USERS SECRETLY VIEW
STORIES (1 MINUTE READ) [18]
Instagram Plus is being tested in select markets, including the
Philippines, Japan, and Mexico, with the plans costing the equivalent
of $2 USD per month.
COST TO IMPLEMENT VS COST TO VERIFY (11 MINUTE READ) [19]
The cost to implement is the time and expertise needed to produce
code, and the cost to verify is the time and expertise needed to
confirm the code is correct.
MAKE SMARTER APPLICATION DECISIONS WITH AZURE COPILOT MIGRATION AGENT


---

## Email 6

**Source:** TLDR AI <dan@tldrnewsletter.com>

**Date:** Tue, 31 Mar 2026 13:35:28 +0000

**Subject:** Codex Plugin for Claude Code 💻,Qwen3.5-Omni 🤖, workload harness fit🧑‍💻


### Content

The Codex plugin for Claude Code gives users a simple way to pull
Codex into their Claude Code workflow. It is useful for normal Codex
reviews
HOW TO SCALE CODE REVIEW WHEN AI WRITES CODE FASTER THAN YOU CAN
HEADLINES & LAUNCHES
INTRODUCING CODEX PLUGIN FOR CLAUDE CODE (3 MINUTE READ) [5]
The Codex plugin for Claude Code gives users a simple way to pull
Codex into their Claude Code workflow. It is useful for normal Codex
reviews, a more adversarial review, and handing work off to Codex when
a second pass from a different agent is required. The plugin delegates
through the local Codex CLI and Codex app server, so it uses the
system's existing local auth, configuration, environment, and MCP
setup.
QWEN3.5-OMNI: SCALING UP, TOWARD NATIVE OMNI-MODAL AGI (94 MINUTE
READ) [6]
Qwen3.5-Omni is a full omnimodal large language model that
understands text, images, audio, and audio-visual content. It can
process more than 10 hours of audio input and over 400 seconds of 720P
audio-visual input at 1 FPS. The model is trained on a massive amount
of text and visual data, and more than 100 million hours of
audio-visual data. It supports speech recognition in 113 languages and
dialects and speech generation in 36 languages and dialects.
MICROSOFT 365 COPILOT GETS CRITIQUE AND COUNCIL MODES (2 MINUTE READ)
Microsoft 365 Copilot has introduced Critique and Council modes to
enhance research capabilities. Critique uses a dual-model system to
generate and refine research drafts, outperforming single-model
solutions by 13.88% on the DRACO benchmark. Council allows parallel
report generation using Anthropic and OpenAI models for impactful
comparison and insight aggregation.
DEEP DIVES & ANALYSIS
A MIRROR TEST FOR LLMS (16 MINUTE READ) [8]
The proposed "Mirror Test" assesses LLM self-awareness by challenging
models to identify their own outputs without explicit cues. Testing
reveals that Anthropic's Opus 4.6 model shows notable self-recognition
capabilities due to its distinct token outputs, outperforming OpenAI's
GPT models, which fail to recognize self-generated tokens. Despite
indications of attempted self-marking, no LLM demonstrated consistent
self-awareness, as none effectively communicated using message
passing.
AI INFRASTRUCTURE ROADMAP: FIVE FRONTIERS FOR 2026 (17 MINUTE READ)
The first generation of AI was a world where progress meant bigger
weights, more data, and stellar benchmarks. The landscape has now
changed. Big labs are now designing AI that interfaces with the real
world. Infrastructure optimized for scale and efficiency won't get us
to the next phase. What's needed now is infrastructure for grounding
AI in operational contexts, real-world experiences, and continuous
learning.
AI APPLICATIONS AND VERTICAL INTEGRATION (6 MINUTE READ) [10]
AI application companies are increasingly becoming "full-stack" by
vertically integrating either downward into the model layer or upward
into the service layer. Companies like Cursor and Intercom achieve
differentiation and cost efficiency by developing proprietary models,
while others, such as Crosby AI and WithCoverage, focus on delivering
end-to-end services. As AI capabilities evolve, these strategies allow
companies to enhance performance, reduce costs, and offer
comprehensive solutions.
ENGINEERING & RESEARCH
MISCELLANEOUS
PLENTIFUL, HIGH-PAYING JOBS IN THE AGE OF AI (23 MINUTE READ) [15]
AI might not eliminate high-paying human jobs due to potential
constraints like limited computing power and energy usage. These
constraints could lead to the principle of comparative advantage,
where humans remain employed in roles despite AI's superior
capabilities, because the opportunity cost of allocating AI to all
tasks would be too high. As AI advances, human roles could change, but
new tasks and increased wealth might sustain or even increase
compensation for human jobs.
AUDIT CLAUDE PLATFORM ACTIVITY WITH THE COMPLIANCE API (2 MINUTE
READ) [16]
The Compliance API on the Claude Platform enables admins to audit
logs, monitor user activities, and integrate data into existing
compliance systems. It tracks admin and system activities, as well as
resource activities like file creation or deletion. To access it,
organizations should contact their account team and create an admin
API key.
QUICK LINKS


---
