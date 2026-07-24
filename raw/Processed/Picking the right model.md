---
title: "Picking the right model"
source: "https://www.youtube.com/watch?v=P0uMXS6emHA"
created: 2026-07-24
tags:
  - "WebClip"
---
![](https://www.youtube.com/watch?v=P0uMXS6emHA)

Hands-on techniques for testing and comparing models against your use case, so you can make a confident call each time a new release ships.

## Transcript

**0:01** · \[music\] \[music\] \[music\] My name's Lucas. I'm in our applied AI team. And today we're going to be talking about picking the right model.

**0:22** · So, what we're going to talk about today is picking the right model.

**0:28** · And this is something I think conceptually seems very easy, right?

**0:32** · But the more we dig into it, the sort of more difficult the problem tends to be.

**0:38** · And let's consider the following scenario.

**0:41** · And we at Anthropic have just launched a new model.

**0:45** · And as usual, there's a lot of noise.

**0:48** · Alongside the model launch, we will release a model card.

**0:52** · We will give prompting guides. We will give benchmark results.

**0:56** · Um you'll also see a lot of hot takes on X or Twitter from, you know, AGI is here all the way to Anthropic is cooked. And there's, you know, various posts across the internet again giving kind of hot takes on the quality of our on new model.

**1:12** · But the key question often for you guys is, what does that mean for your use case? What does that mean for your business? And should you effectively drop in this new model to your product?

**1:23** · Will it be an uplift?

**1:25** · Or if you're building greenfield, which model should you select to to even start with?

**1:30** · And to address that, what we basically want to build is a repeatable process.

**1:35** · Something you can come back to time and time again that gives you a clear yes, no decision on when to select this new model.

**1:44** · In other words, we want to build an eval.

**1:47** · So, coming back to the original problem, conceptually very simple, right? When you need more intelligence, you reach for Opus. When you need lower latency or lower cost, you reach for Haiku. And when you want some balance of the two, you can use Sonnet.

**2:02** · But what about effort levels? While this introduces a little bit more depth to the problem, should we reach for Sonnet with max thinking? Should we reach for Opus with low thinking? Maybe comparing Haiku versus Sonnet with no thinking.

**2:18** · And this is just Anthropic. A lot of you will be comparing models, not just the Claude models, but across other providers as well.

**2:26** · So, how do we frame this? How do we frame this decision?

**2:30** · And I think there's really three pillars that most folks tend to think through when choosing which model to use.

**2:38** · The first one is the model quality.

**2:40** · Effectively, how well does it actually perform on your task? What is the task completion rate? What is the accuracy of the model? Um and various other metrics you might track.

**2:51** · Number two is latency. Especially for customer-facing use cases, latency becomes very, very important.

**2:58** · And number three is cost, which is obviously a big consideration for a lot of different customers as well.

**3:04** · So, I think through the lens of basically these three pillars of quality, cost, and latency, we can start to build an eval around them to help us make an informed decision on which model we should actually use.

**3:19** · So, the three things we're going to try and take away from today.

**3:22** · Number one is a small, it can be a very small, well-designed eval will be much more important for you guys to assess which model to use than any public benchmark out there.

**3:34** · Number two is the model that's right for your use case is not necessarily the one that's cheapest or fastest per token, but the one that is cheapest per successful outcome. And we'll dive deep dive a little bit more into that later on in the talk.

**3:50** · And number three is we have actually quite a lot of knobs and dials that we can twist and turn to kind of move up and down the cost accuracy frontier with a little bit more fine grain control. Or if you think about that Pareto curve of the performance of the model versus the cost, we can actually shift that curve entirely and there's a number of strategies we have to do that.

**4:16** · But I just want to reflect a little bit on what the public benchmarks at least do and don't tell us.

**4:21** · And I think directionally these benchmarks provide us with some insight as to generally whether a model has improved at coding or various other tasks. So, in our model releases will often include benchmark results on things like SWE bench verified or browse com, which are basically what they what they say on the tin. How good is the model at generally at coding? How good is the model generally at research research type tasks?

**4:48** · However, none of these really tend tend to match your use case. If you think about a coding agent in production, often it will need to go and research and find some niche specific part about an SDK on the web and then go and implement that in code. So, already we're crossing over two benchmarks and your workloads often look much more heterogeneous than that.

**5:10** · And so, you know, you might have a coding task, but your coding task can still look a lot different than SWE bench. Maybe you're using languages that don't even show up in SWE bench.

**5:21** · So, the point being here is these public benchmarks are like somewhat directional and give you a bit of a take on, you know, some of the best models out there. However, for your specific workload, it's incredibly important to build your own evals.

**5:35** · So, how do we do that? I think you will hear us at Anthropic talk a lot about evals and we have some other workshops on this. So, we're going to do a bit of an express tour.

**5:45** · But effectively, what we want to do is build up an eval which is composed of a set of tasks, and we can consider a task to be the kind of atomic unit of our eval.

**5:57** · A task being a kind of test with a set of inputs, some success criteria, and we want to basically build up a data set of these tests.

**6:10** · Now, the kind of heuristic I've been using for evals over the course of the last few months is thinking about them much like a math exam when you're at school.

**6:19** · So, you have your question, you have your answer that you need to get right, but it's also very important to show the working in between. And I think this is, especially for agentic-type tasks, exactly the sort of thing we should think about when evaluating the performance of a model.

**6:35** · So, we will ultimately compose a data set with a set of questions or inputs to our system.

**6:43** · We want to, of course, check that our agent reaches the final outcome correctly, but we also want to make sure it took the right steps to get that.

**6:52** · So, the point being is the kind of working is as important as the outcome.

**6:58** · So, I think it's helpful to kind of consider a real-life example.

**7:02** · If you consider a customer service agent, we might want to build an eval where we use an LLM as a judge to check the final response matches what our expected response should be.

**7:13** · But, we might also want to use some kind of LLM as a judge to make sure the agent queried your database in the right way to find the customer's details.

**7:23** · And I think LLM as a judge can be pretty helpful because, let's say your agent is writing SQL, it can be like syntactically a little bit different, and the LLM as a judge can kind of notice that, and as long as the same data is being pulled, it's kind of robust to to that.

**7:40** · And you can also use deterministic, like code-based evals to make sure, hey, I always want my agent to call this tool to search our internal routines. Or when it's searching the routines, I always want my agent to add an argument to localize the search to whatever country the customer is in.

**7:58** · So effectively, you want to build up this set of graders um per task where you will ultimately will have to do a lot of hard yards of creating these data sets, defining yourself to begin with what is the right solutions and what is the right outcomes and what is the right steps to to get there.

**8:17** · But ultimately, I think it's one of the highest leverage things you will do.

**8:20** · And in a world where we're automating a lot of stuff with AI, taking the time to actually build that eval data set, I think is like one of the best uses of your human time that there is.

**8:33** · So the TLDR here is we want to create this reference set of evals that will effectively form the basis of making a much more data-driven decision on picking the right model.

**8:46** · Now, we within Anthropic have been building evals for quite a bit of time now, and I think it's worth touching on a few kind of common gotchas that we've seen, a few common errors that we've seen or failure modes when when building evals.

**9:01** · So on this slide, there's three main things that I kind of want to call out.

**9:07** · Number one is kind of this process of mistaking noise for signal.

**9:12** · So the simple thing to do here is once you've defined your eval and you're running it, to make sure you run it a number of times on every task and make sure that the result holds. And if you're seeing a lot of variance in the metrics and results that you're getting, it's maybe a signal to you guys that the task is not super well defined or that your evals are kind of not fully aligned.

**9:34** · Number two is infra failures. So, you might see your eval results and see the numbers coming out the other side and something looks a little bit off. Maybe the numbers are really down for Opus.

**9:48** · And when you dig into the actual transcripts, you might notice that there's a lot of API failures or a lot of tool call failures. And I want to be very clear, we should separate those from our actual evaluation of the model itself. These are infra issues and not model issues.

**10:04** · So, I think really like digging into the transcripts and figuring out where a failure happened and figuring out like did something score low on a benchmark because the model actually didn't perform very well itself or was there some kind of infra failure?

**10:20** · And again, this is the kind of work that um is easy to overlook. It's very easy to like run your evals, get a result on the other side, and make a decision based on that. But like actually getting into the transcripts again is like a very good use of your time.

**10:37** · And then number three is this point on silent saturation.

**10:40** · So, I think the most salient point here is having a data set that is actually representative of the data that you'll see in production, actually representative of the types of questions a human might ask your system. And I think generating this feedback loop, especially once you've launched a product, to collect traces, see what people are asking your system, see the failure modes of where your agent or LM use case is failing, and put those back into your eval set.

**11:07** · So, you really get this representative diverse sample of the sorts of inputs that your system needs to take.

**11:16** · And then finally, I think it's worth calling out that every model is a little bit nuanced and has its own kind of quirky behavioral changes. So, we will release a prompting guide when we release any new model. And like we do really put a lot of time into that, and I think it's worth reading through.

**11:33** · Or even just feeding that prompting guide to Claude and asking it to update your prompts accordingly.

**11:39** · So, I'll give you an example. I was working on a tool within Claude AI.

**11:44** · And with Opus 4.5, that tool was like drastically under-triggered. And with Opus 4.6, the tool was drastically over-triggered with the exact same prompt.

**11:55** · And so, the takeaway here is you will also need to do a little bit of like fine-tuning and adjusting your prompts based on the model that you're using.

**12:04** · Claude will ultimately perform a little bit differently between the model variants, and Claude will obviously perform a little bit differently than GPT. So, there's some kind of like hand tweaking to be done there as well.

**12:17** · And the other big thing I really want you to take away from today's session.

**12:21** · I've said it before, and I will say it again. You like really need to read your transcripts of what the agent or model is doing at different points in your system.

**12:30** · So, I would try and make this as stupidly easy as possible.

**12:34** · So, setting up good observability, whether it be LangSmith, BrainTrust, or some of the various other platforms out there, making sure if you're building an agent, everything is traced in there from the system prompts, the tool call that the agent made, the tool result the agent gets back.

**12:50** · Um what you basically want to be able to do is dig in and at any point see exactly what the model saw, and then how it behaved, because that is ultimately your way to debugging any issues that you have.

**13:03** · So, I'll give you an example.

**13:05** · We ran an eval on Claude code, and we saw Claude was performing like very, very well on this coding benchmark.

**13:12** · When we actually dug into the transcripts, what we found was that Claude was going into the get history and seeing what it did in previous trials and extracting the answer from there.

**13:23** · So, if we would have just looked at the headline metrics from the eval, we would have thought like great, we've made a huge improvement, but it's only by digging into the transcripts that you start to see some of the actually underlying patterns that are emerging, some of the real things that need to be fixed and um so the closer you can get to the raw data, very much the better.

**13:44** · So to kind of recap at this point, we've talked a little bit about how building a private eval is extremely important for making a data-informed decision on picking the right model.

**13:57** · We've talked a little bit or done an express loop of actually building an eval and some of the common failure modes in doing so.

**14:04** · Now what I want to talk a little bit more about is what are the tools and dials available to us to kind of move up and down that frontier and trade-off between cost and quality or latency and quality.

**14:19** · And let's start off with a little story.

**14:22** · So we had a code fix pipeline internally and it was a pretty simple task. So the team used Haiku 45 with no thinking to begin with and scored 92% as you can see on the screen there.

**14:36** · Uh the team ultimately wanted to get 100% so they turned thinking on and actually got there. Again, this was actually a pretty simple uh pipeline.

**14:44** · And they actually decided to rerun the eval with Sonnet and Opus as well.

**14:51** · And as you can see on the screen, they actually both scored 100% as well, but counterintuitively took way less time in doing so. We weren't super cost constrained on this task, we just wanted it to run as quickly as possible.

**15:04** · Now this is very interesting, right?

**15:06** · Because on the face of it, you would think that Haiku would be much faster, but actually some of the more intelligent models can be much more efficient from a time perspective because they can do things in fewer turns. They can effectively plan a little bit more strategically. They don't need to spend as much time researching to validate what they're going to do is correct.

**15:28** · And so, what I think we can do is start playing around with these configs, thinking, and effort to really like extract the maximum value for for our specific use case. I think it's worth just touching slightly upon what both of these things are, because we've played around with them quite a lot. There's different types of thinking, different types of effort. So, let's just recap slightly.

**15:50** · Uh from Sonnet 4 6 or our 4 6 class of models onwards, we have adaptive thinking.

**15:56** · So, the model itself will decide how much it needs to think for a given task.

**16:02** · And this is effectively called scratch pad to think before it acts think before it works, in fact. So, this is system two type thinking.

**16:12** · And then we have effort.

**16:14** · And this will tell Claude how much to write across both thinking, tool calls, and responses.

**16:22** · So, you can have low thinking with high effort, for example, or you can have no thinking, but still use effort parameters. Effort is basically telling Claude how much effort or work it should put into this task.

**16:36** · Thinking is giving Claude a scratch pad to think before it acts.

**16:40** · And we can effectively use both of these configs and dials to have quite a lot of fine-grain control of uh where we want to be on the this accuracy cost curve.

**16:52** · So, another example here is uh again another counterintuitive point.

**16:59** · When we released Opus 4 5, what we saw is Opus 4 5 on screen is the orange line there, is that it was again able to complete tasks and have a high high or higher level of accuracy than Sonnet and significantly fewer number of output tokens.

**17:18** · And again, like if you were just going off the vibes of smaller model runs faster, you probably would have chosen Sonnet not knowing that Opus can actually complete things faster and with a lower number of tokens. I think the other thing to call out on this slide is you can see this Opus spread between the different levels of effort.

**17:42** · And what you can see there is you can then make some nice trade-offs between am I optimizing for a lower number of output tokens or am I optimizing for accuracy? And if you want higher accuracy, you can choose higher levels of effort.

**17:56** · Or if you want lower latency, you can probably choose lower lower levels of effort. So you can use this effort parameter to really have like much more control over just selecting a model alone.

**18:11** · The other thing that at least makes me very excited is like actually shifting that frontier entirely. And I think there's a couple of hacks here that we can use in order to not just like move along that curve, but shift the curve entirely.

**18:25** · And the first one is prompt caching.

**18:28** · So with prompt caching, uh we have a bunch of guides online and I would really encourage you to to read into it more.

**18:36** · But effectively, you when you're using prompt caching and you're basically using a prefix of a prompt that's saved, precomputed, and pre-cached, you pay 1/10 the num- the price of the list price of input tokens. So effectively, what this means is you can get Opus quality at Sonnet cost, or you can get Sonnet quality at Haiku cost. This is one of the most effective strategies we use in a lot of our products. Like we use extensively in Claude Code, we use extensively in Cohere.

**19:07** · And to kind of benchmark for yourselves a little bit, uh a lot of the best AI systems and applications we see have prompt cash hit rates of around 80% or 90%. So, that's kind of your goal to aim for.

**19:20** · But, this unlocks whole new use cases, right? If we can use prompt caching effectively, we're paying 1/10 of the list price of input tokens, then suddenly like we couldn't afford Opus and now we can. Or maybe there's whole new use cases and budgets that are opened up because we're able to save so much money.

**19:37** · And the other thing to to call out here is in our APIs and our and our SDKs, we return you the token metrics not only the raw tokens consumed, but the prompt cash uh tokens on the input. So, we make it very very easy for you guys to measure your prompt cash hit rates, as well.

**19:59** · So, I'd really encourage you to effectively measure it, hill climb it, and try and get your prompt cash hit rate as high as possible.

**20:08** · Um the other kind of main thing I would mention when it comes to prompt caching, the simple thing that works, especially if you're building an agent, is use this strategy of append only.

**20:20** · So, if you have a system prompt, don't have too many dynamic variables in that.

**20:25** · The common failure mode I see here is somebody putting a date time variable in that system prompt.

**20:30** · So, with every turn, the time ticks up and you break the cash.

**20:35** · Effectively, I would treat everything in your messages array that you're sending to the API as immutable. Once it's done and you're going and adding only, I would append only to your messages array, and this is like the easiest sure fire way to make sure you don't break the cash.

**20:50** · Tarik from our Claude code team, one of the main engineers on the Claude code team, has written and talked about this extensively. So, I would like go and look at some of the stuff he's written about how he implemented this in Claude code, as well.

**21:03** · And the second thing I want to talk about is context hygiene and context engineering.

**21:09** · Um My kind of hot take here is people spend too much time thinking about these like super complex multi-agent orchestration systems and not enough time doing the simple thing that works, which is just like good context hygiene and good context engineering.

**21:26** · So, effectively, if we can improve the token efficiency of our tool responses, we can save a lot of tokens that we're putting into the model, saving cost and improving latency.

**21:38** · And we also have this kind of secondary effect of because we provided Claude with cleaner, more efficient data, Claude's responses tend to be better and more accurate, as well.

**21:50** · So, if we look at the example of the screen, let's pretend we have a tool which returns sports data, in this case, uh Premier League scores.

**21:59** · And there's a few changes we made to Firstly, we use markdown instead of JSON.

**22:05** · Secondly, instead of these full, inefficient date time stamps, we just put a very simple date time stamp.

**22:13** · And then we also added a day of the week, so Claude much more easily understands, rather than having to think too much about what day of the week every game is happening.

**22:23** · And in just cleaning up this response, we see a 66.4% reduction in tokens from this tool response.

**22:31** · And that compounds every time, right? If you're having an agent that is running multiple turns, your tool response doesn't just show up once, but in every single turn in the conversation.

**22:43** · So, these small hygiene things really make a huge impact, and I can't emphasize this enough.

**22:52** · A couple more examples of this that I've worked on. I was working on a web search use case with a customer, and we effectively deduplicated articles that were returned from the same search or from different searches in fact.

**23:08** · And this one this one trick effectively of multiple searches running, taking the articles and deduplicating them before they're returned to Claude, led to a 77% reduction in the number of input tokens that Claude was receiving. A 65% reduction in cost and Claude's accuracy actually went up 9% because again, it's having to reason over less data.

**23:32** · And these metrics sound kind of like plucked out of thin air, but these are run and we can actually measure them because we built evals to begin with.

**23:40** · And this is like huge amounts, right? If you can save 65% cost just by doing good context engineering, you can think again, this opens up the ability to use a more intelligent model or this opens up the ability to go and run whole new use cases for the given budget that you have.

**24:00** · So again, I would encourage you not to just take an API response and pipe it back through your tool, but to actually have your tool, especially a lot of tools wrap APIs, and be a little bit more thoughtful.

**24:12** · Clean up that JSON response you get back from the API before passing it back to Claude.

**24:17** · Much like a human, make it as simple and easy to read as possible. In doing so, you'll reduce the number of tokens provided to Claude and you'll have this again secondary effect of improving accuracy across a lot of use cases that you have.

**24:34** · So three main things to take away before we get into the workshop. Number one, a small well-designed eval is going to teach you so much more about which model you should use than any public benchmark out there ever could. So spend time investing in building that eval.

**24:52** · Number two, the right model is not the model that is cheapest per token.

**24:58** · The right model is the one that is cheapest per successful outcome.

**25:03** · And once you've built that eval, you can effectively run Claude with multiple different models, multiple different configurations, see that Pareto frontier, and then you have the choice of where you want to select along it.

**25:16** · And then number three, use these different dials that we have, effort, thinking, prompt caching, and context engineering to have much more fine-grained control on where you want to end up on that frontier, or shifting the frontier entirely.

**25:32** · And I think if you can do those three things, you'll end up in a pretty good place when it comes to choosing the right model for your use case, even unlocking new use cases, being able to access higher intelligence at a lower cost.

**25:46** · So now I want to move into a workshop that you can follow along with yourself.

**25:52** · And you can go to this link here. So it's cwc26.short.gy/workshops.

**26:02** · And I'll just give you a minute to get there.

**26:10** · Cool. I think we're slightly strapped for time, but we're going to run 5 minutes over. I think it's all good.

**26:16** · Cool.

**26:17** · Um hopefully you're now all at that link, and we can switch over to the screen.

**26:22** · So effectively, what we're going to do in this workshop, and you can go and do this on your in your own time as well, is we've built a skill that we've provided up there in the top left that you can see, which will audit your existing evals, but can also do a sweep of the eval that you've set up, and basically instrument it so that it runs across multiple models, multiple thinking level like thinking off and on, and multiple effort levels.

**26:53** · It will then take those results, plot them, save them, and format them nicely so you can basically see your eval performance across different models, across different thinking levels, and across different effort levels.

**27:07** · So, in this case, we're doing it with Tao bench, which is basically a benchmark of customer service agent use cases. And in this case, we're focusing on the airline side of Tao bench.

**27:20** · Uh in the read me for the workshop, you will see instructions on firstly, how to download and set up Tao bench yourself.

**27:31** · And again, you can give this prompt here to Claude. Claude will go and set it up for you.

**27:37** · Then the next part, I've already downloaded Tao bench for the sake of time.

**27:41** · The next part is to basically run the skill, instrument the code so that we run the eval across different models, different thinking, and different effort levels.

**27:52** · And then, run the eval itself.

**27:56** · So, let's ask Claude to do this.

**27:59** · Uh Can you see okay, or should I zoom in?

**28:04** · Yeah, we can see okay. Thank you.

**28:08** · Okay, so we can see Claude has successfully loaded the skill.

**28:13** · And in the meantime, I'm going to kind of skip directly to the results in the interest of time. And the Blue Peter, here's one I ran earlier way.

**28:24** · So, this was effectively the results from running this sweep. And you can see uh we've been very easily able to run the benchmark across all three models, Haiku, Opus 4 7, Sonic 4 6, with thinking off and on, and across different effort levels. And the results to me at least were pretty surprising.

**28:46** · So, if we take a look at this first chart, we see the pass rate per task plotted against average output tokens per task.

**28:55** · And what we can see is maybe as we would expect, Opus 4/7 with thinking on with high effort has the highest pass rate.

**29:04** · But it actually is able to do so with a lower number of tokens than Sonnet consumes for the same use case.

**29:15** · If we go to the next chart, it's pretty interesting as well. So, we can see even though Opus was the best performing on high effort, it's also clearly the most expensive.

**29:26** · So, if we're optimizing in this case for just pure pass rate, then we would pick Opus with high thinking, right? Whereas if we have to optimize for cost, well, then it becomes a little bit different because we see that Haiku with thinking on actually was able to perform similarly to Sonnet uh with thinking on and a high level of effort.

**29:50** · And then if we go down to the final uh chart, we will see something uh somewhat similar, but again, very interesting. So, Opus with high effort and thinking on was actually able to perform faster with lower latency than Sonnet was with a similar level of thinking.

**30:11** · But what these charts, I think, more interestingly tell us is it gives us the data to make an informed decision on which model and config to choose.

**30:21** · We can now identify some of these more non-intuitive properties of the models at different thinking levels, and we can make a decision trading off our criteria of what is important, whether that be latency, whether that be cost, or whether that be model quality.

**30:39** · Um so, I think we are definitely over time. So, I'm going to end there for now, but just to leave you again with the core takeaways.

**30:48** · If you want to pick the right model, you really should build an eval for your use case.

**30:54** · For those of you folks who who work with us in Anthropic and the applied AI team, like we're very much here to help you build those.

**31:01** · Number two is really try and optimize for the things you care about in your use case. So, once you've built your eval and you're making these data-driven decisions, you can then pick, am I optimizing for intelligence? Am I optimizing for latency? Am I optimizing for cost?

**31:17** · And then number three is you can shift that curve entirely by actually doing good context engineering, by using these strategies like prompt caching to get more out of the model itself.

**31:29** · Thank you very much.

**31:32** · \[music\]