---
title: "Obsidian Vault Deep Dive! Custom Plugins + Agentic Loops | My Full System"
source: "https://www.youtube.com/watch?v=VaGpWWiHXm8"
created: 2026-07-24
tags:
  - "WebClip"
---
![](https://www.youtube.com/watch?v=VaGpWWiHXm8)

🤖 FREE RESOURCES: https://easymachineai.com/links  
📚 Get the Full Setup Here: https://www.skool.com/easymachineai  
📧 Business Inquiries: eric@easymachineai.com  
Hostinger VPS Setup: https://hostinger.com/emaihermes  
Use Code "EMAI" for an additional 10% off your VPS Subscription  
  
I got sick of the friction that comes with standard PKMs and manual data entry, so I built out custom plugins and agentic loops to let AI handle the heavy lifting. In this walkthrough, I break down how I wired up local terminal agents to update my daily notes, set up integrated web viewers, and used Dataview to turn a basic text editor into a fully automated dashboard. I'm using Obsidian a lot differently than the standard note-taking crowd, so if you want to see the actual thought process and execution behind the machine, this is it. Check the links below for the free starter vault, or grab the exact plug-and-play setup inside my Skool community.  
  
TIMESTAMPS  
\[00:00\] Obsidian Vault Deep Dive & PKM System Overview  
\[01:08\] Automating Note-Taking with AI Agents in Obsidian  
\[02:46\] AI Daily Log Template & Time Tracking Workflow  
\[03:33\] Using the Obsidian Web Viewer for Local Development  
\[04:35\] Embedding Web Apps (Slack, Telegram) in Obsidian Sidebar  
\[05:38\] Why Your Second Brain Needs an Optics Layer  
\[06:13\] Building a Productivity Dashboard with Obsidian Canvas  
\[06:49\] Creating Charts with the Obsidian Dataview Plugin  
\[08:01\] Saving Custom Dashboard Layouts with Workspaces  
\[09:09\] Coding a Custom Obsidian Plugin Dashboard with AI  
\[10:52\] Free Obsidian Vault Templates & Plugin Resources  
  
\================================  
Why watch? I run Easy Machine AI, and I built my AI automation business to consistent five figures monthly by learning to build my own tools instead of renting broken ones. This channel is about real developer workflows, live builds, and skipping the hype so you can ship faster. Stop getting held hostage by basic chatbots and build custom AI systems that actually give you real leverage.  
  
🛠️ Tools & Tech Stack Discussed:  
Codex  
Claude Code  
GitHub CLI  
Google Workspace CLI  
Obsidian Skills Repo  
Superpowers  
Browser Harness  
Huashu Design  
FFmpeg  
Supabase  
  
#PiAgent #ClaudeCode #Codex #Obsidian #AIAgents

## Transcript

### Obsidian Vault Deep Dive & PKM System Overview

**0:00** · This is my Obsidian Vault, and this is a bunch of you guys asking me to walk through exactly what's going on. So, today we're going to do that. I guess we'll just start from the top because I don't see a lot of people using Obsidian the same sort of way that I am, and I think I need to explain the thought process and like the trail of breadcrumbs that led me to where I am right now, right? I'm also not going to do an end-to-end tutorial on how to build out this plugin. I'll give you the ideas, but if you've used Cloud Code and built out any of your own tools, you should be able to walk through it once you understand exactly what's going on.

**0:28** · As far as using Obsidian in the manner that it was, you know, advertised for, it is really, really good as a personal knowledge management system, and I like that it lives wherever you tell it to, and you don't have to access the cloud or API tools or anything like that. Your files are just on your computer or on your VPS or whatever, the way that you want them to be, okay? That is awesome.

**0:45** · Where this falls short is the same place that every other note-taking app and PKM falls short in that actually using this thing is sometimes a drag. It's a little bit tough. You actually have to input the information to begin with, and I don't know if you guys are at all like me, but I sometimes don't do that.

**1:01** · Sometimes the reflection at the end of the night slips, or I don't want to go back in and like manually type in all these different fields and properties and stuff. It's kind of a drag, which is where plugins come in really, really handy because we can just input the information to an AI agent through a terminal plugin, and it can route it to the proper places, okay? We don't have to go in and manually select all this stuff. We just tell it what we need, and AI goes and does that. And making note capture really, really easy because you can just, like I said, go in and talk to your AI agent and tell it to update the daily note with whatever it is you need to update with.

### Automating Note-Taking with AI Agents in Obsidian

**1:32** · It's like, "Today went great." Obviously a little bit more in-depth than that. It solves the one problem where all these different note-taking and PKM apps like run into where input sometimes has a bit of friction. This gets rid of that. This is where things start to get really interesting because Obsidian helps the agents work as well because agents don't inherently remember anything. You need to prompt in-depth if you want any sort of consistent response. If you're keeping all your notes inside of Obsidian, it actually really helps your agent with context and understanding the way that you like to work or what you're working on.

**2:03** · They work really well to complement each other. Like, for example, like your AI agent doesn't remember anything, and so you can have all the memory inside of Obsidian. And Obsidian doesn't have any hands, sometimes it's hard to access stuff. No sweat, Claude or Codex can dig into your folder structure and take actions for you. Perfect, right? And that's where a lot of people leave it. They have their folder structure, they use Obsidian as a memory layer, they make sure that Claude is updating their Obsidian memory, and that's okay. That's pretty good. Except it's not good enough.

**2:28** · While I'm pretty good at doing my reflection and planning at the beginning and the end of the day, I didn't really want to like have to go back and reflect on everything and rely on my own like willpower or whatever. I was like, wouldn't it be great if we could keep track of things as we're working? So, that's exactly what I started to do. And I made sure to include that in my daily log template. I started by telling my agents to log activities as I was going on through the day.

### AI Daily Log Template & Time Tracking Workflow

**2:52** · I used Claude hooks and everything with a timestamp, so I could get a really good feeling as to how long things were taking me, where I was spending my time, if there was a block without me doing stuff, I knew I got like, you know, off track a little bit.

**3:05** · Just to keep me accountable, and I could really understand where my time was going. It just gives me a really honest overview of what actually happened over the course of that day instead of me looking back after the fact thinking that, you know, everything went great when in reality I spent like an hour trying to hit a baseball with my hair elastic or something like that.

**3:22** · \[laughter\] So, I mean, that was like step two, I would say, of many, but it was a huge mover because I really, really got to see where my time was going, and it got me infinitely more productive. And I could really zoom in and start to organize my day a lot better. So, at that point we're already working in Obsidian with the terminal plugins. I'm like, all right, what else do you got?

### Using the Obsidian Web Viewer for Local Development

**3:38** · I'm just like looking through to see how I can consolidate my tools into the one spot, okay? And then I noticed it comes with a web viewer out of the box. When you download Obsidian, this comes disabled, which I I is a mistake. So, I enable this, all of a sudden I'm able to work in Obsidian with a web browser.

**3:54** · This is really great to keep me from wandering, but it's also excellent for development in particular because I'll have Codex on the bottom or Pi agent or whatever, and then I've got my local development server on the top, right?

**4:04** · Like so I can have my localhost 3000, for example, and then I can make the edits here, and I've I've got real-time feedback on what's actually happening just like you would if you run it in your browser otherwise, right? So, I mean, this is really starting to come together for me as like not just a memory solution or a note taking app, but like a comprehensive workspace. Now, of course, I'm hooked, and I really, really want to see what else we can do with it. So, then I get to thinking, like what does my browser have that I would miss if I just started using Obsidian all the time like this, right?

**4:32** · And I'm looking at it. I was using Opera at the time, and one of the things I really liked about it, like Opera and Vivaldi in particular, was this sidebar with all the nested apps, right? Like I really liked being able to go to Telegram and like talk to my agent there, and like still be able to be in the same window, or Slack and like not miss notifications because if you use Slack, you know. So, for me, that was the next step. How do I bring that experience inside of Obsidian? And it was actually a lot easier than I'd thought, right?

### Embedding Web Apps (Slack, Telegram) in Obsidian Sidebar

**5:00** · I first played around with how do I build this app inside of Obsidian? And it's way simpler than you think. You click your web viewer, and then you just log in on the web app. Check it out. And then you can just pin that to the side. Boom.

**5:15** · Slack there or Slack over here. And you can do the exact same thing for whatever other apps you want, right? So, like Telegram, WhatsApp, Spotify. I could go down the list of my Opera browser apps and just put them on the sidebar of my Obsidian as well. So, again, another one off the list. It's about this point that I start posting on YouTube about all of my Obsidian fun time adventures, right?

### Why Your Second Brain Needs an Optics Layer

**5:38** · Except we still haven't solved a major problem with every PKM in that like what do you do next? Sure, you've got great note taking and input's easy, and you're taking notes throughout the day and keeping track of your activity, but like then what? You're just collecting a bunch of information. What does this actually get you? And that's kind of the point of the last video I put out on Obsidian right here is that, you know, don't build a second brain to just collect a bunch of notes. You need to start working towards systems. Like we've got all these cool workflows that capture notes and make sure we're taking account of our different metrics and stuff, but like then what? We need to work all this together.

**6:09** · V1 of my Optics layer was actually an Obsidian canvas because I came over from Notion, so this is how we used to do dashboards there as well, right? Just bring in your different charts, have a roll up or whatever. So, if I could figure out a way to do that, then we're laughing, right? And turns out you absolutely can.

### Building a Productivity Dashboard with Obsidian Canvas

**6:24** · Because in canvas, you can go and bring in pictures, you can write in text blocks, right? You can bring in different notes. So, if I want to do just drop this here, you've got your notes like that. You can also bring in web pages. So, I really wanted to make sure that I could see my YouTube comments first thing in the day. And we can just like arrange this however we want. Let's say I've got this note here, right? All sorts of cool stuff like that. For charts, there's actually a really cool solution. There's a community plugin called DataView, and it does pretty much exactly what it says.

### Creating Charts with the Obsidian Dataview Plugin

**6:55** · It helps you visualize data. And I'm like, that is exactly what I want.

**6:58** · However you've been tracking things, whether it's in a property in your daily notes, which is what I do. I make sure that I update YouTube subscribers every day in the property, for example, okay?

**7:07** · You can take that, and since canvas accepts code blocks, you can take DataView notation and punch this in here, and it comes up with charts. So, you can see how this is like starting to come together, right? You can take your properties, use DataView, and then just punch out the code inside here. You can also do line graphs and bar graphs and pie charts and all sorts of stuff like that. What I would recommend is use code X or whatever to go and just like explain exactly what it is you want to do, what you want to track, and then have it punch out the DataView notation. And I mean, that's pretty straightforward. You can do it with natural language.

**7:37** · Just explain what it is you want to do, and then iterate until it gets it right. And then you've got your optics layer on the other side that you can go to every morning or whatever, right? Like if you want to check out your YouTube comments and see what people are talking about. You know what I mean? So, this is like the first iteration, and I'll I'll give you guys a cheat sheet as to how this works exactly. I've got a data view cheat sheet that I can leave as a GitHub gist or something like that in the description. What you do from here, so you don't have to like scroll around all the time, is you make sure that workspace, the core plugin, is enabled.

### Saving Custom Dashboard Layouts with Workspaces

**8:08** · And this will save a layer for you, okay? Whatever it is that's open at that time, it'll save it, and you can just like toggle that on and off. So, check it out. You can go like this, and then just save this as YT.

**8:20** · Boop.

**8:21** · So, now YT's active, and if you want, you can go back to this layer and just like load it up. Now it's gone to this page, refreshed all my terminal stuff, and here we are. That's honestly the easiest way to get there. Just making sure that we capture our notes in the morning and evening.

**8:36** · So, I've got these different workflows to start my day that capture the metrics that I want, and at the end of the day to capture like the reflection sort of metrics. I guess that's where I took this, though. And the only real difference, like the the stuff that feeds this dashboard is exactly the same. All it is is the properties from the daily notes that are triaged by my AI agent, and it's kept in a database.

**8:58** · As I'm filming this video, it's kind of funny because it looks like I'm following the Obsidian home page as like my story arc as to how I built out my vault, right? Cuz it first started out with like the linking and capture, then it was like, "Okay, Canvas is pretty cool for like visualization." I'm like, "And then the next thing I did was build out my own plugin." Which, if you're not aware, it's basically just a an app.

### Coding a Custom Obsidian Plugin Dashboard with AI

**9:18** · It's its own mini app. So, it's a dashboard that I built out with Codex, and I have a plugin view that we're using with Obsidian now, right? So, if I go and click this little house, boop, it goes over to my dashboard.

**9:30** · And I built this out just like you would any other project with your agentic coding assistant, right? Like I it's the same process as I would use if I was building out like a landing page or whatever. Just a little bit more iterative in terms of like getting to this result. But as far as things that are, you know, making this tick and what is fueling this dashboard, it's the daily notes. I'm using Obsidian as a back end for a plugin inside Obsidian.

**9:54** · If we see what's fueling the schedule, it's a note, right? And then that's like populating my calendar. If we want to see what's going on here and how we're populating these metrics, it's the same thing. It's a note just with a database and some tables, right? We want to shuffle around like what shits are in the actual snapshot. I've got a note for that, too. It's the config. We've got our properties all here, all the available properties. And then we've got the different views, right? So, let's move this over here. Let's say I want threads on the inside, right? If I go over here, there go threads.

**10:24** · And then I want it right next to YouTube. Okay?

**10:28** · Boop. There it goes. You know what?

**10:30** · Let's say I want that at the end. You get where I'm going with this. But let's put that here. Now it's down at the end. Same thing with any of these, right? Say I don't want to actually track my sleep score.

**10:42** · If I get rid of that, it won't track it anymore. We just have all our available properties right here. And I can tell it exactly what I want to see by moving those properties in and out of these different headers. And while it was honestly a ton of work for me to get to this point because I'd never built out an Obsidian plugin before and it was like a lot of trial and error. I think now that you see the finished product and how it's being driven, you're a lot better equipped to build out your own custom sort of integrations like this than than I was at the time. All right, so that's the the story arc, I guess, is to like how I got here. But also, I'm not done.

### Free Obsidian Vault Templates & Plugin Resources

**11:11** · I want to see what else I can do with Obsidian and how much more I can get out of this one platform because now I am obsessed. If you want any of the asset resources that I was using in this plugin, you can let me know and I'll I'll point you in the right direction.

**11:22** · This full plugin and my exact setup is part of the paid membership on my school community. If you go to Tools and Agents, I got the whole thing here and a video walk-through of how to use it and configure it for yourself. But if you just want to get started, I won't leave you hanging. I've got free resources you can check out in the description there for free starter vaults, some skills, and a setup for the Pi Harness that I'm currently using in Obsidian to get all this stuff done. Anyway, thanks for hanging out with me. Make sure to like and subscribe for more content just like this cuz this is what I do now, and we'll see you in the next one.