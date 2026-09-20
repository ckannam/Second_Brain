---
title: "Can world models unlock general purpose robotics?"
source: "https://www.bvp.com/atlas/can-world-models-unlock-general-purpose-robotics"
created: 2026-09-20
tags:
  - "WebClip"
---
In 2005, teaching a computer to understand language meant hand-coding grammar rules—thousands of them, painstakingly written by linguists. It was brilliant, careful work. But it did not scale. Then came a different approach: instead of coding the rules, let the machine learn language by reading the internet. By 2023, large language models could write poetry, debug code, and pass the bar exam. The hand-coded rules were obsolete overnight.

**Robotics today looks a lot like NLP in 2005.** We build physics simulations by hand—programming how objects collide, how gravity works, how friction behaves. A robot trained in one of these simulations can pick up a cup in a digital world. Move the cup to a different table in a real kitchen, and the process breaks down. Change the lighting, and the robot fails. Hand it an unfamiliar object, and it freezes. **This is a data problem. And it is a fundamentally harder data problem than LLMs faced.**

LLMs bootstrapped on the internet — billions of pages of text, freely available, already digitized. Robotics has no equivalent corpus. There is no “internet of robot experience.” Teleoperation data requires physical hardware, human operators, and real-world environments. Even the most ambitious collection efforts produce orders of magnitude less data than what language models train on. Teleop will not cut it.

In our [perspective on intelligent robotics](https://www.bvp.com/atlas/intelligent-robotics-the-new-era-of-physical-ai) last year, we identified manipulation and data as the central bottlenecks. The industry is spending accordingly—we estimate aggregate robotic data costs will exceed $3 billion within the next two years, spanning every modality: on-embodiment and off-embodiment, video and teleoperation, tactile, and force. Companies are racing to collect egocentric video, build specialized capture hardware like UMI grippers and force-sensing gloves, and form data partnerships where deployed robots share teleoperation data in exchange for better models.

A rapidly growing class of models—world models—may offer a way through. They learn physics from video rather than relying solely on manually collected robot data. The approach is promising and the early results are striking, but there is a lot still unproven. Here we offer an overview on the state of world models, the set of challenges the industry faces, and new approaches researchers contend with as they advance the field of robotics.

![Available robot data is a billion times smaller ](https://www.bvp.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F2e9xvz8g%2Fproduction%2F1f80bbece60fed6919efd6a087341f58e1160fa5-1156x1019.png%3Fw%3D1600&w=3840&q=75)

Available robot data is a billion times smaller

## What is a World Model?

A world model is a neural network that watches video and learns how the physical world works. Show it millions of hours of footage– people cooking, balls bouncing, water pouring, cars driving – and it builds an internal representation of physics. Not through equations, but through observation. The same way a toddler learns that a ball will roll off a table without solving Newton’s laws.

Two things make world models useful for robotics. First, they develop physical intuition: what happens when you push something, how fabric drapes, how liquid splashes. Second, they can imagine the future. A robot with a world model can mentally simulate “what happens if I grab this mug from the left?” before actually moving – learning from thousands of imagined mistakes without breaking real hardware.

### Are simulators dead?

Traditional robotics simulation only knows what you teach it. Every physics interaction– how a sponge deforms, how a cluttered drawer resists opening, how a wet paper towel tears– must be manually programmed. Much of the real world simply cannot be programmed this way. The permutations are too diverse to model in totality.

**The deeper problem: hand-built simulation scales with the number of engineers you hire, not with compute.** World models flip that– they learn physics from video and improve predictably with more data and more compute. No hand-coding required. Per the bitter lesson: never bet against compute.

Simulators are not dead, but their role is narrowing. For rigid-body locomotion—getting a quadruped to walk across rough terrain—physics engines like MuJoCo and Isaac Sim work well. A foot strikes the ground and lifts off in a rigid, periodic pattern with relatively simple contact forces. Physics engines handle this accurately.

Manipulation is fundamentally different. When a robot hand grips a coffee cup, the contact is soft, distributed across a surface, and sensitive to friction and material properties. Simulating how a sponge compresses or how fabric slides between fingers requires a fidelity that current simulators do not achieve. Simulating contact for manipulation is much harder than contact for locomotion: contact details matter when grasping a coffee cup; not so much when stepping on a floor.

Simulators will remain essential for structured evaluation – testing reach envelopes, validating safety constraints, running reproducible benchmarks. But the future is likely simulators for what we can formalize, and world models for everything else.

## World knowledge vs. action knowledge

A robot needs two kinds of knowledge.

**World knowledge –** how objects behave, how gravity works, how liquids pour and fabrics drape – is universal. It is the same whether you are a human, a robot arm, or a self-driving car. The internet is full of video showing exactly this: cooking tutorials, factory tours, security cameras, sports broadcasts.

**Action knowledge –** how this specific robot’s motors and grippers translate commands into physical outcomes – is embodiment-specific. Torque limits, friction coefficients, gripper geometry. This must be learned from robot-specific data. But you need surprisingly little of it.

The evidence is starting to bear this out.

[Meta’s V-JEPA 2](https://ai.meta.com/research/vjepa/) was pre-trained on over one million hours of internet video. Researchers then added action conditioning from just 62 hours of unlabeled robot video. The result: 80% zero-shot pick-and-place success on real robot arms, across different labs, with no task-specific training.

[DeepMind’s Dreamer 4](https://danijar.com/project/dreamer4/) learned to collect diamonds in Minecraft — a task requiring 20,000+ sequential actions from raw pixels — from purely offline data, with zero environment interaction. If a model can learn world dynamics from video and figure out how to act without ever touching the environment, the same paradigm could apply to warehouse navigation or laundry folding.

At 7-14B parameters, these models are exhibiting emergent physical understanding. OpenAI’s found that the latest Sora models “exhibit emergent capabilities when trained at scale” – 3D consistency, object permanence, realistic physics – properties that are “purely phenomena of scale.” DeepMind’s Genie 2, at 11B parameters, demonstrated emergent object interactions, physics simulation, water and smoke effects. Combine this with reinforcement learning in the world model’s imagination, and you start to see robots that do not just mimic demonstrations but adapt to novel situations.

The internet cannot teach a robot how to move its arm. But it can teach a robot how the world works. That distinction is what makes world models promising — they extract physical intuition from abundant video, dramatically reducing how much expensive robot-specific data is needed.

![the world model landscape ](https://www.bvp.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F2e9xvz8g%2Fproduction%2F104d090886eed140c1a268af47ed7bfca97ad34c-1600x900.png%3Fw%3D1600&w=3840&q=75)

the world model landscape

## Where the world models stand out

### 1\. Scaling is working, and it is expensive.

Models like NVIDIA’s Cosmos (7B/14B parameters), Wayve’s GAIA-2 (8.4B), and DeepMind’s Genie 3 (~11B) represent a rapid increase in scale. (For context, parameters are the learnable weights in a neural network – a rough proxy for model capacity, analogous to how LLM capability scaled with parameter count.) Training runs are starting to rival large LLM runs: Cosmos used 10,000 H100 GPUs over three months. Frontier runs cost tens to hundreds of millions of dollars. The trajectory is consistent across architectures: bigger models, more video, better physics. Open-source releases (e.g. Cosmos, V-JEPA 2, and others) are beginning to democratize access, which matters enormously for the broader ecosystem (more on this below).

![World Model scale over time](https://www.bvp.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F2e9xvz8g%2Fproduction%2F8ac908a66c957244f45da2039aafe47594bf5311-1312x918.png%3Fw%3D1600&w=3840&q=75)

World Model scale over time

### 2\. The architecture debate is unresolved.

Will VLAs win, or something else? Some researchers build on video generation – predicting future frames pixel by pixel. Others, like Meta’s JEPA approach, skip pixels entirely and predict in abstract representation space. Still others use diffusion models for the continuous, fluid movements robots require. No consensus, but the scaling trend holds across all of them. This is reminiscent of the early LLM era when it was unclear whether transformers, RNNs, or some hybrid would dominate – until scale resolved the question.

### 3\. Imitation learning alone may not be enough.

Most robotics companies today use imitation learning– showing a robot how to do a task and having it copy the demonstration. This works in controlled settings but is brittle in the real world. World models enable the robotics equivalent of RL post-training: a robot can explore failure modes and edge cases in imagination, building robustness for sustained autonomous operation. The only demonstrations of robots running 10+ hours without human intervention have used RL-based approaches.

![available robot data is a billion times smaller ](https://www.bvp.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F2e9xvz8g%2Fproduction%2Fa9283a6816ebdce8c459c25d679b3b0c3cc8195a-1600x900.png%3Fw%3D1600&w=3840&q=75)

available robot data is a billion times smaller

## Gaps left to close in world model research

World models are a compelling research direction with genuinely exciting early results. But compelling research directions have a long history of stalling before reaching production. A few areas remain wide open:

**Consistency over time.** Video-centric world models—those that generate pixel-level frames without a persistent scene representation, like those from Genie are impressive in short bursts. Over longer horizons, they suffer from *spatial-temporal inconsistency—* the model's internal representation of the world gradually drifts from coherence. This manifests in several ways: failures of [object permanence](https://arxiv.org/abs/2501.09038) (items disappearing or changing properties mid-scene), spatial drift (a room you walked through thirty seconds ago looks different when you turn around), and violations of basic causal dynamics (objects passing through surfaces, liquids ignoring gravity). [Google's Genie 3,](https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/) arguably the most capable interactive world model today, maintains coherent generation for a few minutes.

The harder question is whether scale fixes this. There is some evidence it helps – OpenAI noted that basic object permanence emerged when scaling Sora's pre-training compute, and specific physics failures (a basketball teleporting to the hoop rather than rebounding off the backboard) were corrected in Sora 2. But various [recent studies show](https://arxiv.org/abs/2411.02385) that scaling alone is insufficient for video generation models to uncover fundamental physical laws because they [learn statistical correlations from pixels](https://arxiv.org/abs/2501.09038), not physical constraints. Promising architectural approaches are emerging – memory mechanisms like [WorldMem](https://arxiv.org/abs/2504.12369) and [WorldPack](https://arxiv.org/abs/2512.02473) that give models explicit ways to store and retrieve past environmental states, extending the coherence window from a handful of frames to hundreds. Whether world models can sustain the long-horizon consistency required for production robotics, or whether they remain better suited to short-horizon planning and policy evals, is one of the most important open questions in the field.

Models with an explicit geometric representation—such as World Labs—are architecturally insulated from many of these failure modes. By grounding generation in a persistent 3D scene scaffold (e.g., a Gaussian splat), they preserve object identity and geometry across time by construction, and the result is dramatically stronger consistency over long horizons: objects stay where you left them, rooms look the same when revisited, and basic physical constraints hold. The tradeoff is that explicit-representation approaches are computationally heavier and, today, more constrained in the richness and variety of environments they can render.

**Tactile sensing and speed.** Video captures how things look, not how they feel. Force, pressure, contact dynamics – critical for dexterous manipulation – cannot be learned from watching. Real robot control operates across multiple frequency layers: a planner at ~1Hz, an action model at ~10Hz, and a low-level control loop at 1,000-10,000Hz. That fastest layer is blind – no vision, just force and proprioception, making thousands of micro-adjustments per second. Tactile sensing unlocks this high-frequency control tier. The hardware for capturing tactile data at scale — sensor gloves, artificial skin — is still maturing. At the planning level, world models remain slow (V-JEPA 2 takes ~16 seconds per action; real-time control needs to be 100x faster), and error accumulation over long horizons is a fundamental problem.

**Cost to train and cost to serve.** World models are expensive to build. They may be even more expensive to run. Cosmos used 10,000 H100 GPUs over three months, and frontier training runs cost tens to hundreds of millions of dollars. But serving costs receive less attention and may prove the harder bottleneck for commercialization.

The core problem is structural. A text model can batch dozens of user requests on a single chip, amortizing cost across concurrent sessions – running a 70-billion-parameter LLM costs a few cents per hour per user. World models cannot do this. They must generate the next state of a simulated environment every few milliseconds and stream it in real-time, which means each user effectively requires a dedicated GPU pipeline. Google's Genie 3 costs roughly $100 per hour to run, according to one industry source we spoke with. Odyssey [requires a full H200 chip per user for its standard model](https://www.google.com/search?q=odyssey+costs+information+world+models&sca_esv=86473391cece26c1&rlz=1C5CHFA_enUS1087US1087&sxsrf=ANbL-n4XbJYB52c16fjzrzwAZ4B9tB-wHg%3A1772835059775&ei=81CrabKGL5if5NoP8u_EsAs&biw=1440&bih=900&ved=0ahUKEwjyy-6fpYyTAxWYD1kFHfI3EbYQ4dUDCBM&uact=5&oq=odyssey+costs+information+world+models&gs_lp=Egxnd3Mtd2l6LXNlcnAiJm9keXNzZXkgY29zdHMgaW5mb3JtYXRpb24gd29ybGQgbW9kZWxzMgoQABiwAxjWBBhHMgoQABiwAxjWBBhHMgoQABiwAxjWBBhHMgoQABiwAxjWBBhHMgoQABiwAxjWBBhHMgoQABiwAxjWBBhHMgoQABiwAxjWBBhHMgoQABiwAxjWBBhHSK0fUMIPWMwQcAJ4AZABAJgBAKABAKoBALgBA8gBAPgBAZgCAqACFpgDAIgGAZAGCJIHATKgBwCyBwC4BwDCBwcwLjEuMC4xyAcQgAgA&sclient=gws-wiz-serp#:~:text=The%20Problem%20With,newsletters%20%E2%80%BA%20ai%2Dagenda), and several H200 chips for its more advanced model – costing several dollars per hour. Even OpenAI has acknowledged that [Sora's economics are "completely unsustainable."](https://x.com/billpeeb/status/1984011952155455596)

![cost to serve wm v llms](https://www.bvp.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F2e9xvz8g%2Fproduction%2F293cfed7634e20e5b6f11cbaaac83600d102217f-958x804.png%3Fw%3D1600&w=3840&q=75)

cost to serve wm v llms

The optimistic case: inference costs for LLMs dropped roughly 1,000x in three years, driven by quantization, distillation, and hardware improvements. World models are earlier on that curve and could follow a similar trajectory. Decart, an Israeli startup, claims to have reduced video generation costs by 400x through a custom inference engine built from scratch in CUDA and C++. But even with aggressive optimization, the architectural constraint remains: real-time, per-user streaming is fundamentally more expensive than batched text generation. How fast serving costs come down – and whether they come down enough to make world-model-powered robots economically viable at scale – will determine how quickly this technology moves from research to deployment.

![the cost curve llms v video generation](https://www.bvp.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F2e9xvz8g%2Fproduction%2Ff4b0d5d7cca37e6ccf8baf42ea3ff7f4fe0b05a8-961x810.png%3Fw%3D1600&w=3840&q=75)

the cost curve llms v video generation

## Building toward the “ChatGPT moment” in robotics

The pattern is familiar. In each major AI wave, the breakthrough came from replacing hand-engineered features with learned representations trained on large-scale data. CNNs replaced hand-designed image filters. Transformers replaced hand-coded grammar rules. World models are attempting the same substitution for physics: replacing hand-built simulators with learned models trained on internet-scale video.

![scaling has driven significant gains in major foundation model categories ](https://www.bvp.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F2e9xvz8g%2Fproduction%2Fffc3b870fe2c1a3af6e27eb3ce2632813815627a-1600x900.png%3Fw%3D1600&w=3840&q=75)

scaling has driven significant gains in major foundation model categories

The early results are directionally clear – zero-shot manipulation from video pre-training, agents trained entirely in imagination, emergent physics at 10B+ parameters. The gaps are equally clear: tactile data, inference speed, the distance between an 80% lab result and 99.9% production reliability.

Whether world models alone achieve general-purpose robotics is an open question. There is a great deal that remains unclear, and we have seen promising research directions in AI stall before reaching production. But the scaling trajectory is consistent, great talent is migrating, and the shift from hand-built to learned simulation follows a pattern we have seen work before. We are going deep with the teams building at this frontier.

***If you’re building world models, foundation models for physical AI, or the infrastructure that enables them – reach out to Talia Goldberg (talia@bvp.com), Grace Ma (gma@bvp.com), or Bhavik Nagda (bnagda@bvp.com).***

## Contributors

![Bhavik Nagda](https://www.bvp.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F2e9xvz8g%2Fproduction%2Feca51474b9c7e2ebd9366b718f1f64ebf1f8af0c-1300x1200.webp%3Frect%3D50%2C0%2C1200%2C1200%26w%3D784%26h%3D784%26fit%3Dcrop&w=828&q=75)

Bhavik Nagda

Bhavik Nagda

Investor

Bhavik is an investor in the New York office, where he focuses on enterprise software and data systems.

Prior to joining Bessemer, Bhavik was an engineer at Cruise Automation and Covariant.ai, building machine learning pipelines and user interfaces for warehouse robotics.

Bhavik earned his B.S. and masters in computer science from the Massachusetts Institute of Technology. He sits on MIT's Computer Science Diversity & Equity Committee and MIT's Center for Entrepreneurship Board. In his spare time, Bhavik enjoys running, hiking, and reconnecting with old friends.

[Read more from Bhavik](https://www.bvp.com/team/bhavik-nagda)

![Grace Ma](https://www.bvp.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F2e9xvz8g%2Fproduction%2F02d5884b210f11585f0a7b0e5fe6f465b8ac1ffb-1300x1200.webp%3Frect%3D50%2C0%2C1200%2C1200%26w%3D784%26h%3D784%26fit%3Dcrop&w=828&q=75)

Grace Ma

Investor

Grace is an investor with Bessemer’s growth investment practice in San Francisco, where she primarily focuses on AI and software investments.

Prior to joining Bessemer, Grace was an Associate at Centana Growth Partners, where she worked on early-stage growth investments in software and fintech. She was also previously at Oliver Wyman as a strategy consultant, advising Fortune 500 companies in M&A, organizational effectiveness, and growth strategy.

Grace earned her B.S. from the University of California, Berkeley, where she majored in Business Administration and minored in Public Policy. Outside of work, Grace enjoys Pilates, traveling, and following the latest in F1.

[Read more from Grace](https://www.bvp.com/team/grace-ma)

![Talia Goldberg](https://www.bvp.com/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F2e9xvz8g%2Fproduction%2F94936b4d3a8115b938c1e4ec6c9116e8c6258085-1300x1200.webp%3Frect%3D50%2C0%2C1200%2C1200%26w%3D784%26h%3D784%26fit%3Dcrop&w=828&q=75)

Talia Goldberg

Talia Goldberg

Partner

Talia Goldberg is a partner in Bessemer’s San Francisco office. She supports teams that leverage AI to create new categories and progress the way we live and work. She looks for founders building radically better products with unique distribution models, or those pushing the frontier.

Talia joined Bessemer in 2013. She is partner to Cognition, Discord, DeepL, fal AI, Fin (fka Intercom), Kindred, Mind Robotics, Papaya Global, Perplexity, Ramp, Recall, ServiceTitan, Shippo, Stubhub, Supermaven (now Cursor / XAI), and Toss, among others. Learn more on [her blog](http://talia.gold/) and hear from many of the entrepreneurs she has backed by listening to [This is Series A](https://www.bvp.com/atlas/this-is-series-a/). She was featured in [Forbes 30 Under 30](https://www.forbes.com/pictures/5a036ab3a7ea436b47b513e9/talia-goldberg-27/) for Venture Capital.

Talia graduated from the University of Pennsylvania. She grew up in Portland, Oregon, which she insists is home to the best ice cream and pizza in America.

[Read more from Talia](https://www.bvp.com/team/talia-goldberg)

Disclaimer: The information presented here is for general informational and educational purposes only and does not constitute investment advice, a recommendation, or an offer or solicitation to buy or sell any securities or investment products. Certain companies discussed may be current or former portfolio companies of Bessemer Venture Partners. Past performance is not indicative of future results. All investments involve risk, including possible loss of principal.