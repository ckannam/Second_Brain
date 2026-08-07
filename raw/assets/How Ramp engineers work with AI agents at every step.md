---
title: "How Ramp engineers work with AI agents at every step"
source: "https://www.youtube.com/watch?v=i4odXOmgMLw"
created: 2026-08-06
tags:
  - "WebClip"
---
![](https://www.youtube.com/watch?v=i4odXOmgMLw)

Ramp runs AI agents across its entire engineering lifecycle: writing code, reviewing it, watching production, and root-causing incidents.  
Boris sat down with Austin Ray and Rahul Sengottuvelu of Ramp to talk about how they got there. Building for the models that are coming rather than the ones that exist, giving every engineer uncapped access to intelligence, and the guardrails that make it work. They compare notes on Claude Code setups, loops versus dynamic workflows, and what Claude Fable 5 unlocked.  
  
Claude Code: anthropic.com/product/claude-code  
Claude Cowork: anthropic.com/product/claude-cowork  
Office Hours LP: claude.com/office-hours  
  
Chapters  
0:00 "Fix all our import cycles"  
0:32 Stress-testing Fable on Ramp's Python modules  
1:33 Fable and dynamic workflows cut CI time 66%  
3:36 Loops vs. dynamic workflows for long-horizon tasks  
5:15 Claude Code setups: vanilla vs. background-heavy  
6:49 AI agents across the engineering lifecycle  
7:23 Building for future models, not today's  
9:11 AI agent guardrails and least privilege  
12:00 Cost controls and AI code review  
13:08 Ramp's culture of experimentation  
13:52 Glass and Inspect: Ramp's AI coworkers  
16:05 On-call assistant: an AI SRE on Claude Code  
17:13 More agent sessions from automations than humans  
18:44 No token budgets for engineers  
20:48 Advice for CTOs adopting AI agents

## Transcript

### Fix all our import cycles

**0:00** · I told Fable to fix all our import cycles.

**0:02** · I also told it to make our app lazy.

**0:04** · So the app boots up, and it’s So the app boots up, and it’s an enormous amount of Python modules and Fable made a lot of progress in both of these.

**0:10** · A lot of this code was merged.

**0:11** · Really understanding what the boundary of where these models break is very important, because those sets of problems are the problems that we would want our people to try when the next Fable comes out or the next release comes out.

### Stress-testing Fable on Ramp's Python modules

**0:32** · One of the first things I tried when I got my hands on Fable was I wanted to find a use case in Ramp that we can empirically verify.

**0:39** · So it must be a large piece of code that I haven't read, that Fable wrote.

**0:44** · It must be in a non-product place.

**0:46** · So something in CI.

**0:47** · So this is for us in our testing suite.

**0:49** · And I wanted to empirically verify it.

**0:52** · To be able to produce a lot of data and check if the code is acting like it should.

**0:56** · It's been working really well.

**0:57** · We're running it for a few weeks in shadow, and it's been consistently faster than what our current implementation is.

**1:03** · But I threw the deep critical problems in our codebase.

**1:07** · So we have this large monolithic Python code base, and I told Fable to fix all our import cycles.

**1:12** · I also told it to make our app lazy.

**1:14** · So the app boots up, and it’s an enormous amount of Python modules and Fable made a lot of progress in both of these.

**1:21** · A lot of this code was merged.

**1:22** · Really understanding what the boundary of where these models break is very important, because those sorts of problems are, the problems that we would want our people to try when the next Fable comes out or the next release comes up.

### Fable and dynamic workflows cut CI time 66

**1:33** · I have these tests that I give every model when they come out, and I just sort of, you know, no model ever just was able to do all of these things.

**1:40** · But this is the first model that just did all the things.

**1:43** · And when Fable struggled, I just used a dynamic workflow, you guys have used it.

**1:48** · This is like where Claude has a bunch of sub agents that it orchestrates.

**1:52** · And using this sort of like algebra in the sandbox.

**1:54** · But essentially it's like a new form of test time compute.

**1:57** · And so you just tell Claude, you know, use a workflow and Fable does it.

**2:00** · Just yesterday, it actually reduced our CI time from, I think, 18 minute P50 to 6 minute P50.

**2:08** · Wow.

**2:08** · And it just like optimization after optimization after optimization.

**2:12** · And they just kept profiling it.

**2:13** · The code landed then it waited a day and used a routine to schedule itself to run a day later to get that real production data.

**2:20** · And then it just like repeated this for days on end until it landed all these wins.

**2:23** · And then it showed me a chart when it was done.

**2:25** · Rahul loves that.

**2:26** · He’s a huge CI time minimization advocate.

**2:31** · It's all I think about.

**2:32** · I just have a follow up question for you.

**2:33** · So when you're doing these, dynamic workflows, I would have to expect that you've already built up the familiarity with Fable as a main agent?

**2:44** · Like a foreground agent, right?

**2:47** · Because there's like a lot of learning from what the 40 or 100 different agents are doing in the background that maybe you're not seeing, but you do have to have comfort by that point because that's a big workload.

**2:59** · Because the agents are, you know, able orchestrate, so the agents might have like work translation they might not, they're executed, you know, in parallel or serial.

**3:08** · You might add more rounds of like adversarial verification or whatever it feels this task needs.

**3:12** · So yeah, I just trust it.

**3:13** · Essentially my mental model for dynamic workflows is the test time compute.

**3:17** · It goes from like low to medium to high to extra high to max.

**3:21** · And essentially the way to think about this is this is the maximum amount of thinking the model can use.

**3:26** · It won't always use a, but it's the maximum.

**3:27** · That's why you have it on the thinking dial at the very end, right?

**3:30** · Exactly.

**3:31** · And for me, dynamic workflows are just like it's a next level.

**3:33** · It's like another form of test time compute.

**3:35** · It's new.

### Loops vs. dynamic workflows for long-horizon tasks

**3:36** · How do you think about loops versus dynamic workflows for achieving some sort of long horizon thing?

**3:43** · So loops are kind of like repetitive work.

**3:45** · And dynamic workflows are like dynamic work.

**3:48** · Like you don't you don't exactly know what the steps are ahead of time.

**3:51** · Like, I use a loop, for example, for babysitting my pull requests, to fix the CI, and rebase them automatically.

**3:57** · But then I use dynamic workflows for things like system optimization, where you don't necessarily know what the next optimization is.

**4:02** · It's a total mental model shift.

**4:04** · It does feel like using Claude Code for the first time, where you have to start relinquishing a lot of the software engineering workflow, including running commands to this agent, right?

**4:16** · I sort of feel like for me loops is, if you have a bunch of engineers doing work, loops are kind of slicing a horizontal off of it.

**4:23** · Like if there's one task every engineer does every day, you can maybe take that and put it in a loop or in a routine.

**4:29** · And this is something like a code review, babysitting a PR, addressing feedback.

**4:35** · You know, like we just have dozens of these.

**4:37** · Like, I have one, for example, for deleting dead code.

**4:39** · This is a routine that runs every day.

**4:41** · And then on the flip side, you can do this vertical slice.

**4:44** · And for us this is like Claude tag.

**4:46** · And you know an example of that is I'll have tag ship and experiment.

**4:50** · It'll make the experiment, it'll land the PR, and then it'll set a reminder for itself, using a routine to monitor and check in the next day, it'll make sure that the exposures are balanced.

**4:59** · It'll crank up the exposure, make sure the experiment’s running, and maybe a couple weeks later, it'll be like, all right, I'm going to ship this variant and it puts up another PR for that.

**5:07** · And I wasn't in the loop at all.

**5:09** · Like at the beginning I asked Claude to do this.

**5:11** · I stamped the pull request, but the rest was just Claude.

**5:14** · Okay, I want to like detour a little bit.

### Claude Code setups: vanilla vs. background-heavy

**5:16** · I want to hear about your coding setups.

**5:17** · So iTerm2, pretty vanilla.

**5:21** · No IDE these days.

**5:24** · And as many pains as my monitors can handle.

**5:29** · Pretty barebones Claude Code set ups.

**5:32** · so not a lot of plug ins or skills or MCPs, pretty simple CLAUDE.MD, inspired by your, you know, your Twitter posts for the vanilla setup.

**5:41** · I think it's the best way to learn the models.

**5:43** · And then good amount of subagent use, adversarial review.

**5:48** · Yeah, mine’s gotten increasingly background heavy, and almost most of my sessions are information gathering.

**5:53** · It's like, why is the memory spiking on the service?

**5:56** · Or how can we get this project done faster?

**5:58** · And it's a great way to like, fan out a lot of sessions and gather a lot of context.

**6:03** · When I do local things local with Claude Code, it's usually maybe more hands on programing where I, it's closer debugging, or I need more services or context on my computer.

**6:14** · Has that changed a lot over time?

**6:15** · Like do you start with a sort of, you know, like an Austin set up of like just terminal, terminal, terminal, terminal.

**6:21** · And then you kind of move to this?

**6:22** · I mean, we have so many services, a lot going on databases and message queues and Reddits and all that.

**6:28** · And so having multiple instances of local dev running can become a constraint very quickly.

**6:33** · Especially with the latest models, I think they require much less hand-holding.

**6:37** · And sometimes you just gotta let them cook, get out of the way.

**6:39** · And so I found myself carrying my laptop with the lid open a little bit too much.

**6:43** · And so then we decided to move.

**6:45** · That’s funny. I know exactly what you mean.

**6:47** · Yeah, make sure Caffeinate is running, right?

### AI agents across the engineering lifecycle

**6:49** · So we've implemented agents at pretty much every part of our business, but especially in the engineering lifecycle.

**6:55** · So if you take the process of building and shipping software, everything from coming up with ideas, figuring out where the bugs are, getting notified when there's problems in our logs and our systems, to writing the code, to reviewing them.

**7:09** · And sometimes when they're after deployed, looking for how they're doing in production and seeing if they're doing the thing you want.

**7:16** · We've tried to build systems along this whole stack.

**7:19** · We've also thought about it from the lens of security, trying to find bugs and other issues.

### Building for future models, not today's

**7:23** · Okay, so now you're at the point where you're using the model kind of everywhere throughout like the whole lifecycle.

**7:29** · How did you get there?

**7:30** · What was like, what was the first place where you started using Claude Code?

**7:34** · And then how did agents kind of expand out of that?

**7:38** · We were seeing and slowly realized, clearly this thing's going to continue to improve and maybe we shouldn’t build for 2.7, maybe we should build for whatever is coming next or the model after that.

**7:49** · And over time as we built these harnesses, we’ve learned to step back and just wait it out because a lot of time we end up removing this scaffolding over and over again because the model is just like outgrown harness.

**8:01** · At any given point, when there's a shortcoming with the harness or the model, we've tried and we're not perfect, we also need to make the product work today because otherwise we won’t have business, but we've tried our best to go the other direction and give the model more tools, more context, more agency with the goal of almost, being able to treat our agents like a coworker.

**8:22** · So, hey, can you go figure this out?

**8:24** · Like there seems to be some sort of exception that's popping up.

**8:27** · Or maybe this customer is complaining of a certain issue.

**8:31** · And we want the models to be able to access the right systems, the right level of access, and produce the right amount of right code.

**8:39** · And so just wanting that simple goal allows us to figure out what we need to do to give the model enough access to do these things.

**8:48** · I think it's a velocity bet in a lot of ways.

**8:51** · Right?

**8:52** · Because you're basically saying, I think the stuff we would put in place to make this work now really well is going to become technical debt really quickly.

**9:01** · And that's going to slow us down.

**9:02** · If we aim a little further in the future or sometimes a lot further in the future, you know, we'll actually make it further with the resources we have.

### AI agent guardrails and least privilege

**9:11** · I have so many questions.

**9:13** · But maybe like one direction we can take is, how do you make sure they have the right guardrails?

**9:18** · Like, you know, like they can access this data, but not this data, or how do you make sure the cost is under control?

**9:24** · How do you make sure the code quality is good?

**9:26** · And how have you guys thought about this, like as you scale up the systems?

**9:29** · Yeah, so we've also, at various levels on the stack, tried to implement safeguards.

**9:33** · We also studied the trace a lot.

**9:35** · One of the things that I think we've tried to focus more on is studying individual traces and less on aggregate level benchmarks.

**9:43** · Benchmarks do give us a lot of information cross model, but a lot of the time there's usually a correct trace.

**9:48** · It's like, what is the command the model should have run in this scenario, and why did it not get there?

**9:52** · Is this a context issue?

**9:54** · Maybe it does not have access to the right tool?

**9:56** · And just following these simple traces for workflows that should work allows us to like get there in the right way.

**10:01** · We've implemented a lot of layers of defense across, I mean we’ll continue to do that.

**10:05** · It's how, how many layers we have also allows us to move faster and give it more agency and more access.

**10:12** · And so again, at every part of the stack, we've done everything we can to give the model what it needs, but nothing more.

**10:18** · So you're essentially like, you go to BigQuery or Data Dog or whatever.

**10:21** · And you give it like a read only service key.

**10:24** · This is essentially how you think about it?

**10:25** · That's right. Yeah, exactly.

**10:27** · So a lot of the time so let's say that, you, I just want to be able to say like, talk to my agent, like I talk to my coworker.

**10:31** · And so we're almost focusing on the default experience, the iPhone experience.

**10:36** · Where you open it up, there's a text box.

**10:38** · You just say what you need to get done, not how to do it.

**10:40** · The prompts must be declarative.

**10:42** · So we're not we don't want people to instruct the agent to do it in a certain way.

**10:46** · We just want people to say, implement this feature, or fix this bug, or help this person out.

**10:53** · And over time, especially when you focus on the correct trace.

**10:57** · So what must the agent do?

**10:59** · It must first query the source and then it must query these other sources and read the code in this in these repos.

**11:04** · Just by focusing on what the correct trace in your head is you can then shape the agent trace purely through prompts and tools and skills to get there.

**11:14** · And thankfully we're also on this exponential increase in model capabilities.

**11:18** · So maybe if it's not working right now, you just got to trust that it will get there.

**11:22** · And just with that belief alone, just ship it and just wait.

**11:25** · And the one thing I'll add is good old fashioned hard controls on top of that, like you said, like principle of least privilege stuff.

**11:32** · The basics of just not even giving it the opportunity to be able to do certain things.

**11:38** · And how do you think about like enforcing it?

**11:40** · Is it like the security team's job to do this or are you like federating out the design of these sort of systems?

**11:46** · How do you think about that?

**11:47** · The really exciting part about this is the infrastructure has been built by the security team, and it's been, the security team is very closely related to this.

**11:54** · So they helped us set up the network access policies.

**11:57** · They helped us get the keys.

**11:58** · And they're also regular users of these agents.

### Cost controls and AI code review

**12:01** · How do you think about cost controls?

**12:02** · How do you think about code quality?

**12:04** · What else do you think about as you scale it?

**12:07** · We're continuing to find and look for cases where, again, we can guarantee we know for sure the worst thing that could happen if, for example, this code has a bug or something like that, the effects are extremely constrained and we do have an upside and we're finding more problems like that.

**12:23** · And we're trying to use this hammer for that.

**12:25** · We're also expecting a massive increase in the amount of productivity, especially with the next few models coming.

**12:30** · And so we're readying our verification loops especially with CI and CD.

**12:34** · I think also changing what our reviewers look out over time because as the models get smarter, they stop making certain classes of mistakes.

**12:41** · And so you, it's not worth spending your reviewer tokens on that anymore, right?

**12:46** · Yeah. I mean, we've invested in our own code review bot as well, which is also built on Inspect or our background agents API.

**12:53** · We pull from some memories of things that we especially want to look for.

**12:57** · We have certain teams that write their own, skill files that look for certain things so that they can codify the knowledge that they have built up over the years into these files that allow people to move a little bit faster.

### Ramp's culture of experimentation

**13:09** · It sounds like it's not like Austin and Rahul that are going in and just like breaking down every bottleneck.

**13:14** · Although I'm sure you're doing a lot of this, like how do you create a culture where engineers feel empowered and have like the visibility and the tools, whatever you need, to find the bottleneck and to break it down?

**13:23** · It's just Ramp, right? Yeah.

**13:25** · I mean, I think a lot of it is the culture that the company has built is a culture of experimentation, a culture of like building something that maybe didn't pan out, and that's okay.

**13:35** · We've tried something. You move quickly.

**13:37** · I think one of the things that has been helpful is, because we've had free access to all the tools, to all our engineers, we don't really like to impose a certain token budget or a tool budget, or tell people that they should use this thing or that thing.

**13:49** · And in general, it becomes a lot easier to speak the same language.

### Glass and Inspect: Ramp's AI coworkers

**13:53** · I mean, it sounds like you guys just built like a huge number of these, like background agents, like various CPIs and systems internally.

**14:00** · So you mentioned Project Glass, you mentioned Inspect, walk me through these. What are these tools?

**14:06** · How do you use them? How are they built?

**14:07** · Yeah.

**14:07** · So Glass is where our, it's the home base for our non-technical folks.

**14:11** · It's where they interact with the coding agent on a daily basis.

**14:15** · And it's been our belief since, since the beginning that everybody should have access to this power.

**14:21** · And this velocity increaser.

**14:23** · But you got to meet people where they are, you know, they don't want to be looking at code.

**14:28** · All the technical detail is not going to help them go faster.

**14:31** · And some things need to be set up ahead of time.

**14:34** · Yeah.

**14:34** · Inspect, at this point, is basically a digital coworker.

**14:38** · We've tried to give Inspect all the tools that a Ramp builder, so product engineer design person, would have.

**14:45** · So this includes access to GitHub, and Linear, and Slack, and Datadog, and Sentry, and various other tools.

**14:52** · And at this point you can ask Inspect to solve a support ticket, or fix a GitHub issue, or look at a Sentry error, or Linear ticket or Zendesk ticket, whatever it may be.

**15:03** · It runs on Modal in the background.

**15:05** · Your access it via web.

**15:07** · Yeah.

**15:07** · And a lot of people kick off stuff from Slack.

**15:09** · So if you're in a conversation with someone about something and you @Inspect, can you go handle this or can you put up a PR to fix this or investigate this?

**15:17** · And that actually ended up being the main way that adoption was spread, because you would hop into someone else's thread and @Inspect.

**15:24** · Can you help them with this?

**15:27** · And they’d see it and go, oh, you can just do that?

**15:28** · Oh. Great.

**15:29** · Yeah.

**15:30** · And every PR now comes with its own VM and it’s like running for a little while so people can take over sessions, collaborate, it's all link based.

**15:38** · It's all multiplayer.

**15:39** · It just works out of the box.

**15:41** · And again we've tried to focus on the correct trace, like, what should this agent have done?

**15:45** · And try to shape it, to that way, so that it can do a lot.

**15:50** · At any given point, sometimes people feel the urge to move back to local dev.

**15:54** · We haven’t fully finished this project, but we've tried to give Inspect that additional tool, that additional repo or dependency that allows people to stay a little bit further in the background.

### On-call assistant: an AI SRE on Claude Code

**16:06** · I also do want to mention on call assistant.

**16:08** · So on call assistant has been running on and always ran on Claude Code.

**16:15** · And that's another instance of just taking what works really well locally, proving it out locally, building up the skills and MCPs and prompts that make, essentially like an AI SRE run really well on incidents to root cause them and put up PRs of fixes and then just packaging that and having it run in a container with safeguards and guardrails.

**16:38** · So on call assistant runs on every instant that gets assigned to our engineers.

**16:43** · So that includes customer tickets, customer support tickets that require an engineer, but also includes system level incidents.

**16:51** · We're working on it. And then comes back in with a really solid root cause analysis in the Slack channel that we have for every incident.

**16:58** · And then the incident responders interact with it.

**17:00** · And we've had that running since late February or March.

**17:06** · The stuff you can build on the primitives on this sort of Unix philosophy, Claude Code executable, it's just wild.

### More agent sessions from automations than humans

**17:14** · Yeah.

**17:14** · We have a bunch of really similar tools internally.

**17:17** · And, now Claude tag, which sounds pretty similar to Inspect.

**17:22** · It sounds like.

**17:23** · In a lot of ways.

**17:23** · Yeah, it's also multiplayer.

**17:25** · It's also kind of proactive.

**17:26** · You know, it's in Slack.

**17:27** · It’s sort of taken over a lot of these special purpose bots.

**17:30** · I wonder if you guys are seeing the same thing?

**17:31** · Yeah, we're seeing something similar.

**17:33** · So more Inspect sessions are coming from automations than humans at this point.

**17:38** · So every time something is, So every time something is, there is some sort of trigger.

**17:40** · Sometimes they're scheduled at a certain time of the day, sometimes they're from other external systems.

**17:45** · Then a session kicks off and sometimes notifies people and channels or by DM.

**17:50** · And I guess for this one also organizationally, culturally, how do you do it?

**17:53** · Is it like each of these automations is built by different teams that's closest to it?

**17:58** · Or do you have like a central dev infra or like AI team that is responsible for all of these?

**18:02** · It’s been very, surprisingly, very decentralized, and we're very happy about that.

**18:06** · I mean, there are teams that maintain certain abstractions, in the Inspect team, as you mentioned, the Inspect abstraction, that is a bedrock for a lot of these automations.

**18:16** · And if you let everybody build what they would like to build we’re okay with that.

**18:20** · And we want that, we want more of it.

**18:22** · All we can do is build a great product, so other teams are incentivized to build on top of us.

**18:26** · It's also a mix of, like, desire paths of people wanting the same, expressing the want for the same sort of thing, or building the same thing separately, and then the sort of platform team going, okay, let's make a solid thing for this.

**18:39** · And vision from the platform team of we're going to need this when the model gets smarter.

### No token budgets for engineers

**18:45** · Yeah. I mean, so taking a step back, one of the things that we've tried to do is not impose limits on how much, how many tokens or dollars each individual spends.

**18:55** · We want them to be able to access any level of intelligence without limits.

**18:59** · So because of that, we've tried to do everything else in our power to make sure that people can step up and get that intelligence where they want.

**19:07** · So that includes things like defaults.

**19:08** · It's using batch and flex APIs.

**19:11** · It's using cheaper models for automations when they're not human controlled.

**19:15** · So we always expect to stay on the latest frontier.

**19:17** · And so we don't want features or people overfit on a certain model's behavior.

**19:21** · And then there's a good amount of just talking to people too.

**19:24** · I think you and I have both done this where we see someone suddenly become a top spender on a certain month, like way above what they normally do.

**19:32** · And we reach out to them and say, hey, what are you working on?

**19:36** · You know, it looks like you're spending a lot.

**19:38** · I'm curious.

**19:39** · And if it's something that you're not planning on platformizing, but is platformizable let’s work together, let's do that, let's expand the impact.

**19:49** · And if it's a mistake then I'll help you with that.

**19:54** · And then we can work on getting the costs down later if it's something you do want a platformize.

**19:59** · So essentially it's like this, this culture of, like, experimentation and innovation.

**20:04** · It's letting you just totally automate, like a big swaths of work that used to be manual before.

**20:09** · So obviously it works.

**20:11** · And so then kind of your job is to support people and optimize the use case after it takes off.

**20:16** · Yeah.

**20:17** · And so the other way to look at it almost is like if you are in the positive ROI section where you know that every dollar you spend on tokens, you're actually making more than $1, you actually don't want to be minimizing costs anymore.

**20:29** · We also expect the level of intelligence that fable has, the cost of that to decrease over time as it has for the last few years.

**20:36** · It's not anything new.

**20:37** · And we rather have, everybody at Ramp be familiar and really good at pushing the frontier and pushing with intelligence, making it sweat on hard problems sooner than later.

### Advice for CTOs adopting AI agents

**20:48** · What is your advice to your peers, to other CTOs that are trying to figure out, what do you do?

**20:53** · How do you adopt agents?

**20:55** · How do you make your way through this thing that's happening in the industry?

**20:59** · We've made a lot of progress in the models today.

**21:01** · We have great tools at our disposal.

**21:04** · But I think the thing that people don't pay as much attention to is also the rate of change and how much things are changing, over the last few years.

**21:13** · And if you pay more attention to that as opposed to the current snapshot, then you begin to see the pattern of like rising intelligence and agency, the ability for models to do more things.

**21:25** · And I think we've tried to build for what comes 3 to 6 months later down the line, because sometimes when you're playing catch up and you’re building for what's available today, it might already be too late by the time you ship.

**21:37** · And so, paying attention to the scaling itself has been very helpful for us.

**21:43** · All right.

**21:43** · So with that, Austin, Rahul, thank you guys so much for taking the time and for hosting us in this beautiful space.

**21:49** · Thank you guys so much.

**21:50** · Thank you.