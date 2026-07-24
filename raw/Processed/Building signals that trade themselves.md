---
title: "Building signals that trade themselves"
source: "https://www.youtube.com/watch?v=EOg4gY0Yln0"
created: 2026-07-24
tags:
  - "WebClip"
---
![](https://www.youtube.com/watch?v=EOg4gY0Yln0)

There are trading signals in production at Man Group right now — running real capital — that were researched, backtested, and proposed by AI. Tushara Fernando shares what made that possible inside a regulated investment firm: a governed skills framework and core data layer that taught Claude Code how Man Group's quants have worked for decades, now scaled across ~750 developers and quants and 100+ skills. Walk away with the governance model that lets compliance say yes to AI on your most load-bearing workflows.

## Transcript

**0:18** · I'm Sharan Fernando.

**0:20** · I'm head of data and AI at Man Group.

**0:24** · Man Group are an alternative investment manager.

**0:27** · We manage over 200 billion dollars of assets.

**0:32** · Our clients are pension funds, sovereign wealth funds, and large institutions.

**0:38** · We manage real people's money.

**0:40** · Thousands of people's pensions and investment capital.

**0:45** · So, when we think about AI, the stakes are high for us.

**0:49** · Our clients are real people from the teachers in Canada, the metal workers in Japan.

**0:57** · So, we really need to get AI right.

**0:59** · If we get this wrong, we could lose real money.

**1:04** · One of the really large parts of our business is systematic trading, and that represents a huge opportunity to be aided by AI.

**1:13** · By systematic trading, I mean algorithmic trading capabilities that look across thousands of securities and hundreds of markets to make investment decisions.

**1:29** · So, systematic trading is really about trading signals.

**1:34** · And you can think of a signal like a fantasy football team.

**1:39** · You can think that we want to pick the best players for our squad based on some intuitive strategy.

**1:46** · So, the green bars here would be a starting lineup.

**1:51** · The red bars would be the reserve squad, the people that you don't want in the team.

**1:56** · And the people in the middle, they might come in, you might kind of transfer them in, but they're they're not the star players at the moment.

**2:03** · Maybe your subs bench.

**2:06** · So, a signal is really about thinking about a striker maybe hitting form, but you need to transfer them in before the Friday deadline when the price might go up.

**2:19** · And then you have savvy managers who are really thinking about form, fixtures, and what might happen to get the most points in the season.

**2:29** · And they want to transfer the right players in at the right time and at the right cost.

**2:35** · So, this is quite similar to systematic trading. A trading signal is really just this with stocks. So, the bars here would represent company stocks.

**2:46** · We want to back the ones that would make money, and we want to short the ones that won't.

**2:53** · So, in this example, we've ranked the stocks by the past 3-month returns, and we run that through history to see if it would have made money.

**3:04** · The interesting question is always what is that factor that you want to rank things by? What's the strategy to get the right stocks in your team?

**3:13** · And does it work?

**3:17** · And how do you know whether it works or not?

**3:20** · Well, the truth is you never really know.

**3:23** · I'd love to be able to tell the future, but I can't.

**3:27** · So, the best thing that we can do is look at what happened historically.

**3:34** · We run that strategy, we codify it, and we run it against 15 years of history, or even longer.

**3:42** · And what that does is it runs that strategy through lots of macroeconomic environments, through lots of stresses, and we can see how it performed.

**3:52** · And that backtest produces lots of statistical factors.

**3:55** · Some examples might be how much money did it make? So, what's the annualized return? When it lost money, and they always do at some point, how much did it lose?

**4:06** · And we call that a drawdown. And we look at some even more complex statistical factors. One's called a sharp ratio, which compares the volatility of that strategy versus how much it returned.

**4:20** · And it's this process, this systematic trading workflow, that we think that we can use AI to really enhance, to come up with those ideas, to run the back tests.

**4:33** · And that has been our focus.

**4:38** · So, there are trading signals running right now in production at Man Group, a regulated investment firm, running real capital that were researched, back tested, and proposed by AI.

**4:55** · By that, I mean humans came up with the idea Sorry, AI came up with the idea. AI got the data.

**5:03** · AI ran the back test. AI then wrote up the strategy proposal. And AI productionized the signal.

**5:13** · Humans, of course, reviewed all of the output to make sure that it was sensible.

**5:18** · But AI AI was at the center of that process.

**5:25** · And I'm sure you want to know what was that signal? What was that investment idea?

**5:31** · How much money did it make? How can I use it?

**5:37** · Sorry. I'm not going to tell you that today. That's our IP. What I'm here to tell you about today is our journey.

**5:43** · What was the foundation that allowed us to do that? And how can you apply those learnings in your company?

**5:52** · And it really starts with AI understanding our workflows.

**5:58** · And to do that, we use skills.

**6:01** · Can I have a show of hands in the audience as to who's written a skill?

**6:05** · Okay, that's great. Most of you.

**6:10** · So, coming up with the signal is the quick bit.

**6:14** · The hard part is everything that you need, everything that's underneath it, all of the workflows that make it happen, that allow you to act on it.

**6:25** · Think of it like an iceberg. The signal is the tip.

**6:29** · Underneath it are all of the workflows that make it possible.

**6:33** · How do you clean the data? How do you stitch prices?

**6:37** · How do you detect outliers?

**6:40** · How does it run? What's the infrastructure it runs on?

**6:44** · How do you run those back tests?

**6:47** · And this is where it can quickly go wrong.

**6:50** · If different teams are running different versions of those workflows, you get different answers.

**6:56** · One team's back test looks amazing.

**6:59** · Another team's looks average.

**7:01** · And because they're using different workflows, you don't really know whether it was the idea that was better in one team than the other, or whether they're just measuring things differently.

**7:14** · Shared workflows fix that.

**7:17** · One common foundation means that effort isn't duplicated, and you have consistency. The outputs are comparable. And that's extremely important in systematic trading when we're comparing signals.

**7:35** · Out of the box, Claud is an amazing general-purpose tool.

**7:40** · It does a lot, but it doesn't know us.

**7:43** · It doesn't know our data.

**7:46** · It doesn't know our systems. It doesn't know how we work. And it's the same for everybody in this room.

**7:53** · So, the first thing that we had to do was teach it.

**7:57** · Not by retraining it.

**8:00** · Not by doing fine-tuning.

**8:02** · But by giving it access to our data, our capabilities, and our workflows.

**8:10** · That's our superpower.

**8:12** · We have decades of institutional knowledge and systematic research. And some of the best technical capabilities on the street.

**8:22** · And if we can connect that with AI, then AI can leverage that superpower.

**8:29** · Skills are the connective layer that allow AI to leverage that superpower.

**8:35** · So, getting them right is paramount.

**8:38** · And that was our focus.

**8:43** · But we got it wrong before we got it right. And I want to tell you about our story today.

**8:49** · We really focused on adoption. We went all-in. We were doing skills workshops.

**8:55** · Anthropic helped us with that. We were doing hackathons. We wrote a blog. We were doing show-and-tell sessions.

**9:03** · Everybody was writing skills. The adoption was really out of this world.

**9:09** · But we started to see some cracks in our approach.

**9:12** · It was really the power users that were building the skills.

**9:16** · It wasn't the process owners.

**9:20** · And what that meant is that all of the skills really represented a local optimization for one user. They weren't common organizational solves.

**9:32** · And nothing was really more symptomatic of this than when we ran one of the show and tell sessions one day, and there was a guy who used to travel a lot at my own group, and he had loads of expenses to do. He spent loads of time doing this.

**9:47** · So, he wrote a skill for it. He gave lots of pictures of receipts to Claude, and it would do the expense report for him. And he brought this to the show and tell session, and he even shared it with a few people in his team, and it was working really well.

**10:01** · And then a few days later, the expense approver came to them and was like, "Why is Claude creating so many expense reports for my cost center? People from technology, people from the people team.

**10:12** · Why do I have to approve all of them?

**10:14** · Like, I'm in sales. I I don't want to approve everybody else's expense reports." And we dug into it, and it was just because the the cost center code was hard coded. And it was really just that that was this um this local optimization.

**10:27** · Nobody had reviewed that skill. It worked for him, it worked for his team, so it was going to work for everybody.

**10:33** · But that's not the case.

**10:35** · And he wasn't accountable for that. He kind of thought it was quite funny, and I mean, so did I, to be honest.

**10:42** · Um but it was really symptomatic of a broader problem.

**10:46** · People were just codifying their ways of doing things. They weren't the organizational ways of doing things. And in many cases, they weren't actually the workflow owner.

**10:57** · And this is a huge problem when it comes to things like back testing and systematic trading.

**11:03** · It starts to become a blocker to you scaling to enterprises.

**11:08** · Agents can't leverage those. There's no commonality.

**11:13** · And we saw that something had to change.

**11:16** · Has anyone else faced this problem when they've been writing skills that it was actually the process, it was the people who were the power users of a process, rather than the owners of it, that were writing the skills? Can I have a show of hands for that?

**11:29** · Good.

**11:32** · Yeah, we really saw that across the board.

**11:36** · But we saw that skills governance started to be the secret sauce that unlocked these enterprise use cases.

**11:44** · If you could connect your common workflows to AI, give it access to your data and your capabilities, you could really allow agents to act on those skills.

**11:57** · And if you can do that, you can allow cloud code to do problems as complex as systematic trading.

**12:11** · So our solve this was to have a common marketplace.

**12:14** · Every skill was visible, tagged, and tested with evals.

**12:20** · We wanted to ensure consistency.

**12:24** · Imagine a library.

**12:27** · It captures decades of institutional knowledge.

**12:31** · There are sections for the finance department, the people department, the research department.

**12:39** · We care for every item. We care for every skill in those departments.

**12:45** · The skill is owned by the workflow owner.

**12:49** · They're all tested, usage is tracked, they're all reviewed. They have a life cycle.

**12:56** · And they're all visible to everybody to install.

**12:59** · It's really that care that makes this work.

**13:03** · And it's the foundation that moves skills from individual productivity solves to a foundation that can set you up for the agent to cage.

**13:14** · And it's through that that we were able to apply skills to systematic trading.

**13:20** · So now, I will give you a bit of a flavor for what it's like to build a systematic signal. We've We've a demo and a video on that.

**13:28** · This is Man a knowledge.

**13:30** · It's where you'll find our collection of skills and Man Group's context store. The skill suggestions are tailored to each business unit. They have clear ownership and are organized into managed and community skills. Skills and plugins can easily be installed in Claude. Plugins are useful groups of skills. For example, here we have a data plugin which gives us access to Man Group's data sets.

**13:55** · We can also skills individually. For example, this is the data set skill which allows me to search Man Group's alternative data sets. Now those foundational skills are installed, we can start to get a flavor of what it's like to build a systematic trading signal. We can use the alternative data set skill to search for research such as credit card data.

**14:19** · We ask Claude, what credit card data sets are available and it identifies a data set of US consumer transactions. We can plot Amazon's monthly credit card spend against its stock price returns. These are the results of the credit card data compared to the stock price for the same period. The blue bars are credit card spend and the line is the stock price.

**14:49** · Interestingly, in the graph, you can see spikes for seasonal spend such as Black Friday and Christmas. Next, we run a back test to see if credit card spend is predictive of the stock price by comparing the peaks in credit card spending with the profits and losses of the stock. In the results, the signal shows better performance than a buy and hold strategy.

**15:12** · We can see that investing $1,000 in 2021 using the signal would now be worth around $2,500. This could be a fluke for Amazon, so let's run it on a broader universe of retail companies. As there are multiple companies, we'll run it using our distributed compute infrastructure. Each company is running an individual worker, and then the findings are collected. In this case study, we leveraged four skills to create a systematic trading signal.

**15:44** · In reality, our signal research is much more nuanced, accounting for things like seasonality, inflation, and broader sets of securities. We do this with agents as well as humans exploring these ideas. The key takeaway is that the governance of these skills is key. It ensures that everyone has access to the same data, and everyone uses the same workflows.

**16:10** · Okay, so hopefully what you can see is that if you get that foundation right across the board, if you've got access to all of the data, you can start to leverage more capabilities. Everything from scaling your compute to getting alternative credit card data sets. And these are often owned by different teams. And it's really that that allows you to scale to the Agentech platform.

**16:36** · So, what did we learn along the way?

**16:40** · These are the things that I would tell past me, and that you can take away. Firstly, focus on that organizational context. That is your IP, it's your moat. It's one of the few safe spaces left in AI. The frontier labs are not going to solve context for you. It's not on the internet, they don't know your workflows, and you already have that context. You have decades of it. The work is on exposing it, not reinventing it.

**17:15** · And skills are how that those decades of institutional knowledge become leveraged. Treat those skills like production code because that's what they will become.

**17:27** · Plan your approach before you plan the rollout. Who's going to own the skill?

**17:33** · Who's going to review it?

**17:34** · How does it get retired?

**17:36** · How does it get tested?

**17:38** · Decide this be sure before shipping the first skill, not after the hundredth like us. Adoption is not a licensing problem. It's a people problem. Once you've got that platform in place, you need to encourage people to engage with it. We need to really think about how we capture that organizational context and rethink our workflows rather than just augmenting them.

**18:08** · And that's a training problem. It's an engagement problem. So you really need to outreach to people who are using this platform. And it's through this it's through these ideas that we've been able to scale. Man Group's about 17,800 people 1,700 people something like that. And we now have 750 of them using Claude Code across developers, quants, the people team, the finance team, everybody across all of the departments is using Claude Code.

**18:43** · We're seeing a lot of engagement because they're able to use those capabilities in a simple way. They don't need to know about everything. They have the skills platform that understands our workflows. We now have over 100 governed skills and at least as many community skills that are looked after in a library and they're well governed. And what this has done is it has allowed us to unlock the capability to use AI in systematic trading.

**19:21** · So, skills governance really unlocks AI at that enterprise scale. The thing that I'm most proud of is that I feel that we've got our eyes on the prize. We have a solid bedrock built on decades of institutional knowledge. And in the not-too-distant future, I can see us having swarms of agents leveraging those skills to look for new investment opportunities.

**19:53** · So, what's the takeaway for you?

**19:56** · Really think about how you're going to capture that context.

**20:00** · Which department owns it?

**20:04** · What's the process for governing them?

**20:07** · Where will they live? How will you test them? How will you retire them?

**20:13** · Connect a golden path from your AI platform to your capabilities and your context. Once you have that basis of knowledge, if you care for it and AI can leverage it, that will really set you up for the agent cage. Thank you very much, everyone.