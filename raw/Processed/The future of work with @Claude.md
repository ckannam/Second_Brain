---
title: "The future of work with @Claude"
source: "https://www.youtube.com/watch?v=MhfnicQVkgY"
created: 2026-07-24
tags:
  - "WebClip"
---
![](https://www.youtube.com/watch?v=MhfnicQVkgY)

"In the past, you had to open Claude and ask. With Claude Tag, Claude jumps in." In this conversation, Boris Cherny (Head of Claude Code) and Cat Wu (Head of Product, Claude Code) walk through how they got there: the long-horizon and alignment research that lets Claude stay on track for days at a time, the memory system that finally feels right, and how usage spread inside Anthropic. Today, 65% of the product team's code is created by Claude.  
  
Claude Tag is available now in Slack (beta). Learn more: claude.com/tag

## Transcript

**0:00** · What do you do if there's no Claude in the channel?

**0:01** · I don't know, I can't remember a world without Claude in the channel.

**0:15** · Walk me back.

**0:16** · Three years ago, we were just starting to adopt AI into our day-to-day workflows.

**0:22** · What was it like back then?

**0:24** · And take me all the way to where we are today.

**0:26** · I remember two years ago, I was still using typeahead.

**0:30** · That was what AI could do as an engineer.

**0:34** · And you know, we built Claude Code, we brought agents, and kind of the next generation of ways to do your coding.

**0:42** · And it’s just changed so much since.

**0:44** · With typeahead, I was still deciding, I want to write this line of code, and the agent was helping a little bit.

**0:49** · It was just writing the line.

**0:51** · And then we got to the point where it was writing whole functions, whole files, whole features.

**0:57** · And I feel like now with Tag, it just does the whole thing.

**1:01** · It can write the feature, it can do an entire experiment end-to-end, it does my data analyses.

**1:07** · It's been like two leaps in 2 years.

**1:09** · When I think back to the last couple of years, it's almost like this transition.

**1:13** · We went from a person always in the loop, it's one person sitting there, and they're just typing a line at a time.

**1:20** · We got to one person sitting there with like 10 Claudes, you know, typing a bunch of features at a time.

**1:26** · Now we're at the point where Claude is actually driving a little bit more.

**1:31** · And it's not just one person anymore, it's an entire team that's interacting with it.

**1:37** · So, what is Claude Tag?

**1:38** · In the past, you had to open Claude, and you had to ask it something, and then Claude would do the work.

**1:45** · It'll use your tools, it'll use your computer, and it'll get the task done.

**1:48** · That's the way that it used to be.

**1:50** · With Claude Tag, Claude jumps in, it's proactive, it knows when to jump in.

**1:56** · It'll do the work, even if it takes days or weeks, and it'll follow up.

**2:02** · And I think the coolest thing is, it'll remember what I told it for next time.

**2:07** · Before, I would have to prompt Claude every time, and I would have to say, "Claude, now do this, or now do this."

**2:16** · I would have to remember to do that.

**2:18** · Now we just add Claude to a channel, it will proactively jump in and do the work.

**2:22** · Everyone gets to see it, everyone gets to participate, because it's multi-player, and it'll remember for next time.

**2:28** · Okay, so what on the research side actually enabled this?

**2:32** · How is it that Tag is so good?

**2:34** · For many years, we've been working on making our models more long-running and autonomous.

**2:39** · So if you look at the latest METR evals, our latest models can work for 16 hours at a time, and are now in the zone where we can't even accurately detect how long it's able to work for.

**2:51** · In something like Claude Tag, Claude is able to self-schedule work for itself.

**2:57** · And so you can take this one 16-hour task, and it actually increases over time because Claude can schedule a follow-up after days, or weeks, or months.

**3:08** · I feel like the task that we couldn't trust it to do before, now it can get almost every single time.

**3:14** · I have a bunch of these Claude Tag sessions, personally, that are running for days, weeks.

**3:19** · I think I might have one that's a month.

**3:21** · It's essentially this long-running experiment, and it's just checking in every day, checks the data, once in a while, it sends a bug fix if there's a bug that needs to get fixed.

**3:29** · I just see the pull requests coming in, and I get these data readouts every day.

**3:32** · The other big innovation is just being able to have memory in the model.

**3:37** · The model can not only set reminders for itself, but it can also remember just all the instructions that all the users have given it over time.

**3:46** · Memory took a long time to crack.

**3:48** · I think we tried to get it right for Claude Code for years, and it feels like we finally got it right. It feels really good to use.

**3:56** · If you're working with Claude Tag in a channel, and you tell it, "Hey, I want you to monitor only for this type of issue, but not these other categories," it will do that.

**4:06** · It will remember that for that channel forever after.

**4:09** · And then, if someone else says, "Hey actually, let me expand your scope to this new thing," it will adjust.

**4:15** · Another big thing that people love is Claude's personality and EQ.

**4:19** · Sometimes when I talk with people about adding Claude Tag into a channel, they say, "Oh, how do I know it won't jump in on every thread and be annoying?"

**4:29** · Well, Claude is trained to have a good sense for when it's needed, and it can take the back seat.

**4:36** · If it ever goes too much in the wrong direction, you can just tell it to do something different, to jump in less, or jump in more, and it'll just remember it for the future.

**4:45** · So when you look at the internal usage, and when you talk with our customers who are getting started on Claude Tag, what are the patterns that you see?

**4:53** · The coolest thing to me has been how customers are figuring it out.

**4:58** · It can write your pull requests, it can debug production issues, it can do data analysis.

**5:03** · All you have to do is hook it up to your tools.

**5:05** · I think that's only possible because the memory is just so good.

**5:10** · And I've seen people do this emergent stuff where, you know, for example, this is a channel for Q&amp;A, anytime a question is answered, you must check it off.

**5:17** · You tell Claude Tag this, and it'll just do that.

**5:19** · It'll answer the questions, and it'll react with a check every time, and it'll just do this for you.

**5:24** · We have a channel for data questions, and now Tag just answers all the questions.

**5:28** · Or we have the channel for Claude Code feedback, and Tag just fixes everything now.

**5:32** · The most common way that I ask a data question is, I post in our data channel, but then I tag Claude Tag, and then it takes the first pass, and normally it's pretty good.

**5:41** · I kept doing this in a bunch of channels, and then I just got tired of tagging it, so I just told it, "Please respond every time."

**5:47** · I think it goes to show how powerful the memory is, that you're able to do something like this.

**5:52** · You can just tell it, "Hey, remember to always do this thing," and it just has your back.

**5:55** · It's been a huge shift in how we all do work.

**5:58** · I think this also is a way for more people to understand how to work with AI.

**6:04** · Because Claude Tag is working in public channels, everyone is able to observe how the expert users leverage it.

**6:12** · And then they take those patterns, and they bring it to new projects that they're working in.

**6:17** · And so both internally and in the customers that we've been working with, we've been seeing this diffusion of Claude Tag best practices that is, I think, very novel to AI tools.

**6:28** · It was surprising how fast it took over.

**6:30** · I feel like now I see Tag in every channel that we have; every feedback channel, every data channel.

**6:35** · It started with a few people using it, but I think as other people saw those people using it, they quickly picked it up.

**6:42** · It's been very empowering to be able to have Claude Tag have my back.

**6:46** · So for a lot of our existing tools, like Chat, Cowork, and Claude Code, you typically have to remember to open it.

**6:53** · And so it’s a more reactive experience.

**6:55** · And one thing that's great about Claude Tag is you give it this higher-level objective, like put up PRs for every bug in this channel, and it just has your back and puts up a PR for every single one without you needing to remind it.

**7:10** · The second thing that's really cool is that it's multi-player.

**7:12** · So almost all of the AI tools that people use right now are just you and Claude working together, and then copy and pasting this output to your team.

**7:22** · And I think the big shift that Claude Tag allows is, it brings Claude right into the middle of your work so that multiple people can guide the session to a better output.

**7:33** · There's so many, like, dynamics here.

**7:35** · Like one, we're all learning about how to use Claude Tag better by observing other people.

**7:40** · Claude Tag is learning how to better work with us by hearing the guidance that we're giving it.

**7:46** · At the end of the day, the customer gets a better result, because it's not just my opinion of how we should solve it, it's our whole team is able to jump in to nudge this PR to the best possible state.

**7:57** · I mean, I love this idea.

**7:59** · I keep telling everyone, I want everyone to contribute to the code base, and so many people are afraid because they have to, like, open a terminal, even the desktop app, because you have to deal with a Git and code checkouts and stuff.

**8:10** · And with Tag, they can just do it. It's really cool.

**8:14** · The other thing that I think is really important is making sure that your collaboration platform has public channels.

**8:20** · That way, Claude Tag can monitor different projects that you're tracking.

**8:24** · So as a PM, I'm often working on maybe five to 10 features, and I have Claude Tag look at the status for every single one, and then give me a daily report.

**8:33** · The other big unlock we've been seeing is that, people can now self-serve their questions.

**8:38** · When people onboard to our company, instead of asking Legal about whether they can say this, or instead of asking our HR team what our benefits are, they can just tag Claude Tag.

**8:51** · And because Claude Tag is connected with our source-of-truth files, it can give them a really fast answer, no matter what time they're looking for it.

**8:58** · I think the single biggest thing is just how much more productive it's made everyone.

**9:04** · And, you know, this is driven by our internal version of Claude Tag.

**9:08** · And if you look at just the product org, so, the part of the company that we sit in, the number of PRs that are written by Tag, I think it's like 65% now, and it's just climbing like this.

**9:18** · I thought that Claude Code was the thing that makes engineers go faster.

**9:22** · This is a product that makes engineers go way faster.

**9:25** · I think actually, a lot of the reason is, because the way you're interacting with it, you ask Tag to do something, and it'll respond, and you move on to the next task.

**9:35** · So you actually want to set it up in a way where Tag can do the work, and you don't have to check in all the time.

**9:42** · You have hundreds of these Claude Tags running, but you're still a power user of Claude Code.

**9:47** · How do you decide when to reach for each of them?

**9:50** · Yeah, so I used to use Claude Code for everything, and then I started using Tag for more and more things.

**9:56** · First, it was really simple fixes.

**9:59** · Someone has a bug, the button's off by a few pixels or something.

**10:03** · I'll just ask Claude, "Please fix it."

**10:04** · Or someone has a simple data question, I'll ask them to fix it.

**10:08** · And I think what's been happening more and more over the last few weeks as I've been getting more comfortable with the product, is I've been using Tag for just more and more things.

**10:16** · And even more complicated work, it's actually able to do.

**10:20** · Because it can verify its work, because it's running in the same remote sandbox that we use for mobile and for the desktop app, and it's using the same agent SDK.

**10:30** · So it's just as intelligent.

**10:31** · When you add memory to this, in different channels, I have specific preferences about how I want it to verify.

**10:37** · It might be a little bit different for every channel.

**10:38** · Often what it does is it'll fix some bug, then it'll post back a video in Slack, and I don't even have to leave it.

**10:45** · What's next for Claude Tag?

**10:48** · So we launched Claude Tag in Slack, and we're excited to bring it to more platforms where people collaborate, like Microsoft Teams.

**10:55** · We want to make sure that every knowledge worker is within arm's length of Claude, no matter where they're getting their work done.

**11:02** · And I think one of the coolest parts of Claude Tag is, it's not just changing how individuals work, it's putting Claude in the center of teams and transforming entire orgs.

**11:11** · We've built Claude Tag to be incredibly customizable, just like Claude Code.

**11:16** · And I'm so excited to see how orgs customize Claude Tag and make it their own.

**11:22** · I can't wait.