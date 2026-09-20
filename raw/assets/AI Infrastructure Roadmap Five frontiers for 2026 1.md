---
title: "AI Infrastructure Roadmap: Five frontiers for 2026"
source: "https://www.bvp.com/atlas/ai-infrastructure-roadmap-five-frontiers-for-2026"
created: 2026-09-20
tags:
  - "WebClip"
---
The first generation of AI was built for a world where the model was the product, and progress meant bigger weights, more data, and stellar benchmarks. AI infrastructure mirrored this reality, fueling the rise of giants in foundation models, compute capacity, training techniques, and data ops. This was the focus of our [2024 AI Infrastructure Roadmap](https://www.bvp.com/atlas/roadmap-ai-infrastructure), which drove our investments in companies such as [Anthropic](https://anthropic.com/), [Fal AI](https://fal.ai/), [Supermaven](https://supermaven.com/) (acquired by [Cursor](https://cursor.com/)), and [VAPI](https://vapi.ai/) as the AI infrastructure revolution unfolded.

But the landscape has changed. Big labs are moving beyond chasing benchmark gains to designing AI that interfaces with the real world, and enterprises are graduating from POCs to production. The infrastructure that got us here — which was optimized for scale and efficiency — won’t get us to the next phase. What’s needed now is infrastructure for grounding AI in operational contexts, real-world experience, and continuous learning.

The stage is being set for a new wave of AI infrastructure tools to enable AI to operate in the real world. We’ve identified five frontiers that will define this next wave, each addressing a structural limitation that needs to be solved beyond model scaling.

## Five cutting-edge frontiers for next gen AI infrastructure

![](https://www.bvp.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F2e9xvz8g%2Fproduction%2Ff8cbe199e8306dcee468eefa0775f9c33518ba0b-1600x900.png%3Fw%3D1600&w=3840&q=75)

The first generation of AI was built for a world where the model was the product, and progress meant bigger weights, more data, and stellar benchmarks. AI infrastructure mirrored this reality, fueling the rise of giants in foundation models, compute capacity, training techniques, and data ops. This was the focus of our 2024 AI Infrastructure Roadmap, which drove our investments in companies such as Anthropic, Fal AI Supermaven (acquired by Cursor ), and VAPI as the AI infrastructure revolution unfolded.

### 1\. “Harness” infrastructure

As AI deployments shift from single models to compound systems, infrastructure designed to "harness" models — unlocking their full potential — becomes more important than ever.

Take memory and context management. Most enterprise AI systems suffer from organizational amnesia. While basic Retrieval-Augmented Generation (RAG) solved the connection problem between models and data sources, compound AI systems now require more sophisticated memory infrastructure. Enterprises hold vast amounts of historical data and organizational knowledge — from proprietary documents to CRM records — that AI systems must access to avoid hallucinations and stay grounded in company-specific reality.

Reliable AI deployment depends not just on raw model horsepower, but on orchestrating components like knowledge retrieval, cross-session context management, and planning. As models become commoditized, differentiation shifts to the memory and context layer. What developers once built from scratch — custom vector databases and retrieval systems — is now emerging as its own infrastructure category. Startups and [Big Tech alike](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/) now offer plug-and-play semantic layers that maintain conversation context, user preferences, and long-term memory across sessions.

Novel evaluation and observability present another critical infrastructure challenge — one that didn’t exist in prior software development paradigms. Consider teams shipping conversational AI agents to production. Traditional monitoring tracks completion rates, latency, error codes, and thumbs up/down feedback. But conversational AI fails differently. When a chatbot gives a confident wrong answer, gradually drifts from the user's actual question, or misunderstands the request while producing something plausible, users often don’t react. No complaint, no thumbs down, no error signal. The conversation looks fine in dashboards, and AI just quietly failed.

An estimated [**78% of AI failures are invisible**](https://arxiv.org/abs/2603.15423) — AI gets something wrong, but no one catches it. Not the user, not traditional monitoring, not even a sentiment analysis. These failures cluster into recurring patterns:

- **The confidence trap** — AI is confidently wrong, and the user accepts it
- **The drift** — AI gradually answers a different question than what was asked
- **The silent mismatch** — AI misunderstands but produces something plausible enough that the user doesn't push back

These patterns persist across 93% of cases even with more powerful models, because they stem from interaction dynamics — how models present outputs and how users communicate intent — not capability gaps.

New infrastructure is emerging to address this. Platforms like [Bigspin.ai](http://bigspin.ai/) provide not just pre-deployment testing but real-time production monitoring of model outputs against golden datasets and user feedback. We’re also moving beyond traditional analytics toward semantic metrics, with new platforms such as [Braintrust](https://www.braintrust.dev/) and [Judgment Labs](https://judgmentlabs.ai/), as well as techniques such as LLM-as-a-judge, that are emerging for high-quality evals and metrics definition.

**These examples illustrate evolving needs for AI harness infrastructure. For more on environments, runtime, orchestration, protocols, and frameworks, see our [Software 3.0 roadmap](https://www.bvp.com/atlas/roadmap-developer-tooling-for-software-3-0).**

### 2\. Continual learning systems

Today’s AI models face a fundamental constraint: frozen weights prevent true learning after deployment. While context management strategies like compaction are powerful, and we see many big labs use them for long-running agents, in-context learning enables only surface-level adaptation through rote memorization, not the acquisition of new skills. It also becomes prohibitively expensive as contexts grow, since the KV cache scales linearly with added context. From both technical and economic perspectives, it’s infeasible to build AI systems that remember everything and continuously improve over years of use.

This is where continual learning offers a solution. It enables AI to accumulate knowledge and skills across tasks over time, maintaining earlier capabilities while acquiring new ones. Unlike traditional models trained once and deployed statically, continual learning systems evolve in production — getting smarter with each interaction while avoiding catastrophic forgetting. Researchers and practitioners are pursuing this through innovations at both pre-training and post-training stages.

Architectural approaches fundamentally rethink how models learn:

- [Learning Machine](https://learning-machine.ai/) is building models that continuously learn during inference, as humans do. Through a new architecture and training paradigm, models will master the meta skill of "how to learn", enabling adaptation to individual users and enterprises post-deployment
- Core Automation is fundamentally rethinking transformer architecture to build systems where memory emerges naturally from novel attention mechanisms
- [Stanford and Nvidia’s TTT-E2E](https://arxiv.org/pdf/2512.23675) uses a sliding-window Transformer that continues learning at test time through next-token prediction on its context – compressing that context into its weights. During training, the model learns how to better update its own weights at inference, making the approach end-to-end

Near-term, production-ready solutions are also emerging:

- [“Cartridges” methodology](https://scalingintelligence.stanford.edu/pubs/cartridges/) stores long contexts in small KV caches trained offline once, then reused across different user requests during inference
- Sublinear Systems and foundation model labs are racing to address context limitations through novel techniques

**The spectrum of approaches we’ve seen for continual learning ranges from high-risk architectural moonshots that could redefine the field entirely to production-ready techniques that incrementally improve existing transformers. We’re eager to meet founders across this spectrum.**

Production deployment of continual learning requires new governance primitives that don’t yet exist in standard ML workflows. Rollback mechanisms enable reversion to stable checkpoints when updates introduce regressions, requiring full lineage tracking of weights, data, and hyperparameters. Isolation techniques allow safe experimentation without affecting core capabilities. Creating benchmarks, beyond needle-in-the-haystack tests, to gauge the performance of continual learning systems versus in-context learning will also be critical.

### 3\. Reinforcement learning platforms

With data quality fundamentally determining AI capabilities, the old machine learning axiom of “garbage in, garbage out” has never been more relevant. Data platforms such as [Mercor](https://www.mercor.com/), [Turing](https://www.turing.com/), and [micro1](https://www.micro1.ai/) have been instrumental in the AI revolution’s first wave by mobilizing human expertise to create high-quality datasets. But we believe that as AI systems evolve from pattern recognition to autonomous decision-making, a critical limitation has emerged: human-generated labeled data is no longer enough to enable production-grade AI. It cannot teach AI systems how to navigate complex, multi-step tasks with delayed consequences and compounding decisions.

This is where reinforcement learning (RL) becomes essential, as AI must learn through interaction rather than static datasets to ground the AI in “experience.” Leveraging an RL stack is now a cornerstone of AI infra tooling to teach agents complex behaviors without the cost and risk of real-world trial and error. Platforms in this emerging stack include:

Environment building and experience curation [Bespoke Labs](https://www.bespokelabs.ai/), [Deeptune](https://deeptune.com/), [Fleet](http://fleet.so/), [Habitat](https://www.habitat.inc/), [Matrices](https://matrices.ai/), [Mechanize,](https://www.mechanize.work/) [OpenReward](https://openreward.ai/), [Phinity](https://www.phinity.ai/), [Preference Model](https://www.preferencemodel.com/), [Proximal,](https://proximal.ai/) [SepalAI](https://www.sepalai.com/), [Steadyworks,](https://steadyworks.ai/) [Veris](https://veris.ai/), [VMax](https://vmax.ai/) RL-as-a-service [Applied Compute](https://appliedcompute.com/), [cgft](https://cgft.io/), [Metis](https://www.withmetis.ai/), [osmosis,](https://osmosis.ai/) [Trajectory](https://trajectory.ai/) Platform infrastructure [AgileRL](https://www.agilerl.com/), [Hud](https://www.hud.ai/), [Isidor](https://www.isidor.ai/), [OpenPipe](https://openpipe.ai/blog/announcing-6-7m-seed-raise), [Prime Intellect](https://www.primeintellect.ai/), [Tinker](https://thinkingmachines.ai/tinker/)

### 4\. Inference inflection point

Model deployment and inference optimization emerged as a critical infrastructure layer in our 2024 roadmap, when vendors like [Fal](https://fal.ai/), [Together](https://www.together.ai/), [Baseten](https://www.baseten.co/), and [Fireworks](https://fireworks.ai/) pioneered efficient serving solutions. At that time, capital-intensive model training consumed the majority of compute resources across the AI stack. Today, we’re witnessing a fundamental shift in the compute center of gravity. As AI agents and applications transition from prototype to production at scale, inference workloads now rival — and in many cases exceed — training in both compute demand and economic importance. As NVIDIA’s [Jensen Huang stated in his GTC 2026 keynote](https://www.youtube.com/watch?v=jw_o0xr8MWU), “Finally, AI is able to do productive work, and therefore the inflection point of inference has arrived.”

**This inflection point reflects a maturing market where the cost and performance of running AI systems continuously matter just as much as the initial investment in building them.**

A new generation of infrastructure startups is addressing this production imperative through specialized optimization across the inference stack. Companies like [TensorMesh](https://www.tensormesh.ai/) are leveraging [LMCache](https://lmcache.ai/) to eliminate redundant re-computation, [RadixArk](https://www.radixark.ai/) is advancing SGLang-based routing and scheduling for multi-turn conversations, [Inferact](https://inferact.ai/) is pushing vLLM performance boundaries for high-throughput serving, and [Sail Research](https://www.sailresearch.com/) is purpose-built for background agentic workloads—optimizing open-source model serving for async, high-volume tasks like deep research and overnight coding runs. [Gimlet Labs](https://gimletlabs.ai/) and even hyperscalers like [NVIDIA](https://developer.nvidia.com/blog/inside-nvidia-groq-3-lpx-the-low-latency-inference-accelerator-for-the-nvidia-vera-rubin-platform/) are working on heterogeneous inference innovations purpose-built for complex agentic systems. These innovations translate cutting-edge systems research into measurable production gains: faster response times and lower costs.

We’re also seeing innovations in inference for novel deployments, with edge and on-device as one prime example. As AI proliferates all sectors of the economy, from robotics to consumer, AI deployments need to meet users where they are, which isn’t always cloud-based. We’re seeing companies such as [WebAI](https://www.webai.com/), [FemtoAI](https://femto.ai/), [PolarGrid](https://www.polargrid.ai/), [Aizip Mirai](https://aizip.ai/), and [OpenInfer](https://openinfer.io/) build at the very “edge” of what’s possible for on-device AI deployments in consumer devices. On-device innovations from model vendors such as [Perceptron](https://www.perceptron.inc/) are also important for physical AI, and we expect more in the space as we outlined in [our thinking on intelligent robotics](https://www.bvp.com/atlas/intelligent-robotics-the-new-era-of-physical-ai).

[Edge AI is also critical for industries such as defense](https://www.bvp.com/atlas/defense-tech-roadmap-five-frontiers-for-2026), where comms are jammed or denied; companies such as [TurbineOne](https://www.turbineone.com/), [Dominion Dynamics](https://www.bvp.com/news/dominion-dynamics-forging-the-future-of-interoperable-attritable-systems-for-arctic-and-allied-defense), [Picogrid](https://picogrid.com/), and [Breaker](https://breakerindustries.com/) are leading the charge on providing the infrastructure tooling for warfighters to harness the power of AI even in the most austere environments.

### 5\. World models

[The model layer is one of the most dynamic and hotly contested layers within the AI infrastructure stack](https://www.bvp.com/atlas/roadmap-ai-infrastructure#1-Innovations-in-scaling-novel-model-architectures-and-specialized-purpose-foundation-models). While LLMs have taken over language intelligence, a new class of models — world models — has emerged to deliver intelligence for the physical world.

As AI moves from our screens to our physical realities, new challenges arise: how does an AI "brain" develop intuition for physics and the world if it has no "body"? World models offer a solution. At the core, these are AI systems trained on real-world data — video, sensors, GPS, and more — that learn to predict how the world evolves given a current situation and action. Rather than describing reality, they simulate it.

Out of this newer research, three broad architectural paradigms have emerged. In practice, companies are also beginning to explore hybrids that combine elements of each:

- **Video-based world models** from companies such as [Reka](https://reka.ai/) and [Decart](https://decart.ai/) frame the problem as one of video generation, predicting future frames directly in pixel space. Because they generate outputs step-by-step, they can operate in real time and respond dynamically to new inputs, making them well-suited for interactive environments. Though they still struggle with maintaining physical consistency over longer horizons, they produce visually compelling outputs
- **Explicit 3D representation models** from companies such as [World Labs](https://www.worldlabs.ai/) take a different path, constructing persistent 3D scene representations that deliver strong spatial coherence at a lower inference cost. For now, these environments are pre-generated and static, but World Labs has signaled that real-time interactivity is on its roadmap
- **Latent predictive models**, based on Joint Embedding Predictive Architectures (JEPA) pioneered by [AMI Labs](https://amilabs.xyz/), avoid pixel generation altogether by forecasting future states in a compressed latent space. This approach is significantly more compute-efficient and sidesteps many visual failure modes, but comes with reduced interpretability. While each paradigm has seen meaningful progress, important gaps remain — how these are resolved will shape the path to the broader commercialization of world models

This commercial opportunity for world models is expansive. We recently shared our view of [world models in robotics](https://www.bvp.com/atlas/can-world-models-unlock-general-purpose-robotics), as this sector has been among the most visible early applications. By generating unlimited synthetic training environments, world models solve the data scarcity problem that has bottlenecked physical AI for decades. Autonomous driving is proving this as Waymo and Wayve use world models to simulate rare edge cases that no real-world test program could economically replicate. The same core capability unlocks even more, such as high-stakes simulation in defense, healthcare, industrial operations, and enterprise planning.

World models are not a vertical-specific kind of tool — they’re a new substrate for machine intelligence, analogous to what LLMs did for text-based reasoning. The industries that build on top of them early will have a significant head start on deploying agents that work in the real world. We’re excited about companies building the architectures and simulators that make world models possible across industries.

## Building infrastructure for AI to experience and enter the real world

While the first generation of AI infrastructure companies built the engines of intelligence — the models, compute clusters, and training pipelines that proved AI’s capability — the next generation must build the nervous system and harnesses that allow AI to sense, remember, adapt, and operate continuously in the real world. These frontiers represent more than incremental improvements to existing infrastructure. The companies building in these spaces aren’t just optimizing latency or reducing costs; they’re solving the fundamental challenges that separate impressive demos from reliable systems that create enduring value.

We believe 2026 will be the year when AI infrastructure’s center of gravity definitively shifts, reimagining what AI-native operations look like for this year and beyond. **We’re particularly excited to work with founders who are pursuing these endeavors. To get in touch with us, please contact aiinfra@bvp.com.**

**Disclaimer**: The information presented here is for general informational and educational purposes only and does not constitute investment advice, a recommendation, or an offer or solicitation to buy or sell any securities or investment products. The information presented is also not intended as advertising material under the Investment Advisers Act. Certain companies discussed may be current or former portfolio companies. BVP may still have a financial interest in these companies. Any discussion of specific companies, securities, or investment strategies should not be considered a recommendation to take any particular action. Past performance is not indicative of future results. All investments involve risk, including possible loss of principal. Market conditions and investment returns can fluctuate significantly. Please visit https://www.bvp.com/legal for more information.

## Contributors

![Janelle Teng Wade](https://www.bvp.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F2e9xvz8g%2Fproduction%2F0c7d1f5eea7177f808aa06c0bde30cf789dc23b3-1300x1200.webp%3Frect%3D50%2C0%2C1200%2C1200%26w%3D784%26h%3D784%26fit%3Dcrop&w=828&q=75)

Janelle Teng Wade

Janelle Teng Wade

Partner

Janelle Teng Wade is a partner at Bessemer where she leads the firm’s early-stage investment roadmaps in AI/ML, data infrastructure, developer platforms, and defense tech. She is passionate about supporting highly technical teams and founders from research backgrounds pushing on the technological frontier.

Before joining Bessemer, Janelle was a product manager at SalesforceIQ (formerly RelateIQ) where she led mobile development for Salesforce Inbox and was one of the inventors of Einstein Email Insights. She began her career as a business analyst at McKinsey and Company.

A science enthusiast at heart, Janelle studied biology and economics at Stanford University, where she graduated with academic distinction and departmental honors. She also earned an MBA at Harvard Business School. Outside of work, you can find Janelle skiing, hiking, or writing her [Substack](https://nextbigteng.substack.com/).

[Read more from Janelle](https://www.bvp.com/team/janelle-teng-wade)

![Lance Co Ting Keh](https://www.bvp.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F2e9xvz8g%2Fproduction%2F8e9856989f36ce940cac9aff54245078a2210721-1300x1200.webp%3Frect%3D50%2C0%2C1200%2C1200%26w%3D784%26h%3D784%26fit%3Dcrop&w=828&q=75)

Lance Co Ting Keh

Lance Co Ting Keh

Venture Partner

Lance Co Ting Keh founded OpenPay, an AI subscription company acquired by Airwallex in 2025, and today is the co-founder, CEO of t0.ai and a GM at Airwallex. He is a builder at heart: he co-founded Vega Health, a Duke spinout in health AI, and earlier bootstrapped SharedRoof Investments, a real estate company that valued homes off predicted prices, and co-founded a sports analytics shop.

Based in our Silicon Valley office, Lance focuses on early-stage applied AI, leading technical diligence and incubating new companies. He serves on the boards of Vega Health and ChipAgents, which builds AI for chip design.

Lance led engineering for two teams at Google X working on AI drug discovery and computer vision, was the second engineer at Cresta building language models for contact centers, and helped start the machine learning team at Box, well before the current surge in deep learning.

He earned bachelor's and master's degrees in electrical engineering and computer science from Duke University, where he was an A.B. Duke Scholar. He lives in Portola Valley with his wife and two children, and maintains that his best athletic days are ahead of him, a position he has held for almost a decade.

[Read more from Lance](https://www.bvp.com/team/lance-co-ting-keh)

![Talia Goldberg](https://www.bvp.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F2e9xvz8g%2Fproduction%2F94936b4d3a8115b938c1e4ec6c9116e8c6258085-1300x1200.webp%3Frect%3D50%2C0%2C1200%2C1200%26w%3D784%26h%3D784%26fit%3Dcrop&w=828&q=75)

Talia Goldberg

Talia Goldberg

Partner

Talia Goldberg is a partner in Bessemer’s San Francisco office. She supports teams that leverage AI to create new categories and progress the way we live and work. She looks for founders building radically better products with unique distribution models, or those pushing the frontier.

Talia joined Bessemer in 2013. She is partner to Cognition, Discord, DeepL, fal AI, Fin (fka Intercom), Kindred, Mind Robotics, Papaya Global, Perplexity, Ramp, Recall, ServiceTitan, Shippo, Stubhub, Supermaven (now Cursor / XAI), and Toss, among others. Learn more on [her blog](http://talia.gold/) and hear from many of the entrepreneurs she has backed by listening to [This is Series A](https://www.bvp.com/atlas/this-is-series-a/). She was featured in [Forbes 30 Under 30](https://www.forbes.com/pictures/5a036ab3a7ea436b47b513e9/talia-goldberg-27/) for Venture Capital.

Talia graduated from the University of Pennsylvania. She grew up in Portland, Oregon, which she insists is home to the best ice cream and pizza in America.

[Read more from Talia](https://www.bvp.com/team/talia-goldberg)

![David Cowan](https://www.bvp.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F2e9xvz8g%2Fproduction%2F270de2655b4eb350059c20a85dddf295b6b97fa7-1300x1200.webp%3Frect%3D138%2C75%2C1125%2C1125%26w%3D784%26h%3D784%26fit%3Dcrop&w=828&q=75)

David Cowan

David Cowan

Partner

David Cowan is one of the world’s leading investors, having funded Seed, Series A, and

Series B

rounds that led to over 30 IPOs. David was ranked sixth on the Midas List and tied for fourth in the Midas List of Hall of Fame.

Based in our Silicon Valley office, David launched Bessemer's practices in cloud, cybersecurity, consumer internet, gaming, space, and quantum computing. Known for taking chances on the unorthodox, David’s early stage bets include Twitch (acquired by Amazon), Rocket Lab (NASDAQ: RKLB), and Skybox Imaging (acquired by Google).

David has co-founded three cybersecurity companies incubated within Bessemer’s offices: VeriSign (NASDAQ: VRSN), serving as initial Chairman and CFO; Good Technology (fka Visto, acquired by Blackberry) serving as CEO; and Defense.net (acquired by F5).

He earned an AB in computer science / mathematics and an MBA, both from Harvard University. Today he serves on several non-profit boards including the Center for Inquiry and the Smithsonian Center for Astrophysics. He is the co-writer of the Silicon Valley mockumentary series “ [Bubbleproof](https://bubbleproof.tv/bubbleproof-series),” and Emmy-nominated producer of the award-winning MTV Documentary film “Afghan Dreamers.”

[Read more from David](https://www.bvp.com/team/david-cowan)

![Grace Ma](https://www.bvp.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F2e9xvz8g%2Fproduction%2F02d5884b210f11585f0a7b0e5fe6f465b8ac1ffb-1300x1200.webp%3Frect%3D50%2C0%2C1200%2C1200%26w%3D784%26h%3D784%26fit%3Dcrop&w=828&q=75)

Grace Ma

Investor

Grace is an investor with Bessemer’s growth investment practice in San Francisco, where she primarily focuses on AI and software investments.

Prior to joining Bessemer, Grace was an Associate at Centana Growth Partners, where she worked on early-stage growth investments in software and fintech. She was also previously at Oliver Wyman as a strategy consultant, advising Fortune 500 companies in M&A, organizational effectiveness, and growth strategy.

Grace earned her B.S. from the University of California, Berkeley, where she majored in Business Administration and minored in Public Policy. Outside of work, Grace enjoys Pilates, traveling, and following the latest in F1.

[Read more from Grace](https://www.bvp.com/team/grace-ma)

![Bhavik Nagda](https://www.bvp.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F2e9xvz8g%2Fproduction%2Feca51474b9c7e2ebd9366b718f1f64ebf1f8af0c-1300x1200.webp%3Frect%3D50%2C0%2C1200%2C1200%26w%3D784%26h%3D784%26fit%3Dcrop&w=828&q=75)

Bhavik Nagda

Bhavik Nagda

Investor

Bhavik is an investor in the New York office, where he focuses on enterprise software and data systems.

Prior to joining Bessemer, Bhavik was an engineer at Cruise Automation and Covariant.ai, building machine learning pipelines and user interfaces for warehouse robotics.

Bhavik earned his B.S. and masters in computer science from the Massachusetts Institute of Technology. He sits on MIT's Computer Science Diversity & Equity Committee and MIT's Center for Entrepreneurship Board. In his spare time, Bhavik enjoys running, hiking, and reconnecting with old friends.

[Read more from Bhavik](https://www.bvp.com/team/bhavik-nagda)

![Brandon Nydick](https://www.bvp.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F2e9xvz8g%2Fproduction%2Fd4d781f7aa13d9f87b4d759e074118093d21b519-1300x1200.jpg%3Frect%3D50%2C0%2C1200%2C1200%26w%3D784%26h%3D784%26fit%3Dcrop&w=828&q=75)

Brandon Nydick

Brandon Nydick

Investor

Brandon is an investor at Bessemer Venture Partners based out of the New York City office.

He graduated Phi Beta Kappa from Stanford and earned the J.E. Wallace Sterling Award for Scholastic Achievement, which recognizes the top 25 graduating seniors by GPA in Stanford’s School of Humanities and Sciences. He was a Summer Analyst at Bessemer, Draper Associates, and Corvex Management as well as a Venture Fellow at NFX.

Brandon helps lead Icons, a community of 1,500 Stanford students and alumni, where he organizes dinners with iconic founders and investors.

He is a National Master of chess and was ranked in the top ten in the USA for his age from 2009-2020. Brandon is the founder and president of Kids For Chess – a non-profit that provides scholarships for America’s best youth chess players to attend the World Youth Chess Championships.

In his free time, he enjoys surfing, skiing, tennis, and spending time with friends.

![Bar Weiner](https://www.bvp.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F2e9xvz8g%2Fproduction%2Fb935aabbc39ba5d36c1a7060fcccec1c6f717877-1300x1200.png%3Frect%3D50%2C0%2C1200%2C1200%26w%3D784%26h%3D784%26fit%3Dcrop&w=828&q=75)

Bar Weiner

Bar Weiner

Investor

Bar Weiner is an investor in Bessemer’s New York City office, where he focuses on artificial intelligence, enterprise software applications, infrastructure and security.

Before joining Bessemer, Bar worked as an AI researcher and software engineer at Houzz and InfluxData, and later founded a generative AI procurement and RFP automation startup. He also held venture investing roles at Battery Ventures, the SoftBank Vision Fund and S32, and has been an active angel investor.

Bar graduated from Stanford University with both a bachelor’s and master’s degree in computer science, specializing in artificial intelligence. At Stanford, he led Cardinal Ventures, the university’s largest startup accelerator, and served as a teaching assistant for several courses at the Graduate School of Business and the School of Engineering.

Outside work, he enjoys hiking, snowboarding, surfing, spending time with his dog and trying new restaurants.

[Read more from Bar](https://www.bvp.com/team/bar-weiner)

Disclaimer: The information presented here is for general informational and educational purposes only and does not constitute investment advice, a recommendation, or an offer or solicitation to buy or sell any securities or investment products. Certain companies discussed may be current or former portfolio companies of Bessemer Venture Partners. Past performance is not indicative of future results. All investments involve risk, including possible loss of principal.