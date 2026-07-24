---
title: "Set Up Clawdbot on a VPS in Minutes (no mac mini)"
source: "https://www.youtube.com/watch?v=BhjK2Gr0Ryc"
created: 2026-07-24
tags:
  - "WebClip"
---
![](https://www.youtube.com/watch?v=BhjK2Gr0Ryc)

Code NATEHERK for 10% OFF Self-Hosting: https://www.hostg.xyz/SHImM  
Commands to run: https://docs.google.com/document/d/1Ln2RnsUY\_6viCMJQYf08etHVgtLCCqTEL3SXLCOx9n0/edit?usp=sharing  
  
My FREE AI OS Course: https://www.skool.com/ai-automation-society/about?el=set-up-clawdbot-on-a-vps-in-minutes-no-mac-mini&hcategory=youtube-videos&utm\_campaign=free-group  
Full courses + unlimited support: https://www.skool.com/ai-automation-society-plus/about?el=set-up-clawdbot-on-a-vps-in-minutes-no-mac-mini&hcategory=youtube-videos&utm\_campaign=ais-plus  
Apply for my YT podcast: https://podcast.nateherk.com/apply  
Work with me: https://uppitai.com/  
  
My Tools💻  
FREE MONTH voice to text: https://get.glaido.com/nate  
Code NATEHERK for 10% off VPS (annual plan): https://www.hostinger.com/vps/claude-code-hosting  
  
In this video, I walk you through a complete step-by-step setup of Clawdbot on a VPS from scratch. Whether you've never touched a terminal before or just want a clear, no-fluff guide, I'll show you exactly how to get Clawdbot running in minutes—from spinning up your server to creating a dedicated user, installing Clawdbot, and setting it up to run 24/7 automatically.  
  
Sponsorship Inquiries:  
📧 nate@smoothmedia.co  
  
Connect with me:  
https://www.linkedin.com/in/nateherkelman/  
https://x.com/nateherk  
https://www.instagram.com/nateherk/  
  
TIMESTAMPS  
00:00 Why We’re Using a VPS  
01:05 Setup Hostinger VPS  
02:56 Installing Clawdbot  
05:29 Clawdbot Onboarding  
07:34 Starting Gateway and Tunnel  
09:26 Telegram Connection  
10:25 Gateway on VPS  
11:19 Security Talk

## Transcript

### Why We’re Using a VPS

**0:00** · So, Cloudbot has been taking the internet by storm, and you don't have to actually go buy a $600 Mac Mini in order to test it out. So, before I bring you guys any content about how I'm using it in different use cases, I wanted to make sure that you guys could form your own opinions. So, I'm going to be showing you guys step-by-step how you can actually deploy Cloudbot onto a VPS, a virtual private server, and we're going to be doing this with Hostinger. So, the reason why people are buying Mac Minis is because Cloudbot is an open-source project. So, when you deploy it, it basically has access to everything in its environment.

**0:28** · So, you don't want to just push that onto your own main device because then it has access to like everything. And it essentially can do anything that you could do on a computer. So, people are buying Mac Minis and they're putting the Cloudbot just on that little machine, and they know that it lives in there and basically contains it, so it's mitigating the risk a little bit. And we can essentially do that exact same thing with a virtual private server. So, go to Hostinger VPS. You can use the link in the description to get there, and let's go ahead and get set up.

**0:53** · Now, there are some terminal commands that we are going to have to run, unfortunately, but I'm going to give you a document where you can just copy and paste that will also be linked in the description, and you just follow what I'm doing step-by-step, and we should be all set. So, I'm going to go ahead and scroll down. You can see that the options here to set up a virtual private machine. It's going to be a lot cheaper than buying actual hardware. So, for the sake of the video, I'm going to be using KVM 2, which is going to give us two VCPU cores, 8 GB of RAM, 100 GB of disk space, and 8 TB of bandwidth, which is going to be more than enough for us to set up Cloudbot and do tons of testing.

### Setup Hostinger VPS

**1:24** · And if you need to scale up or down, you can. So, I'm going to go ahead and choose plan. Now, when you get in here, it's going to prompt you to choose either 1 month, 12 months, or 24 months. And obviously 24 months is going to be the cheapest, the best deal. But what you can do is if you use an annual plan, so 12 or 24 months, you can use code NateHercus, and that will get you 10% off in addition. So, you can really save a huge chunk of change by using Hostinger VPS. But from there, you're going to want to choose a server location. You're going to choose some sort of operating system. So, in this case, I'm going to use Ubuntu, and I'm going to go ahead and do 24.04 LTS, and go ahead and confirm that.

**1:57** · So, you can obviously choose a different one.

**2:00** · You can choose a different VPS provider, but if you want to just follow what I'm doing step-by-step, then here's what I am running. Now, after you pay, you're going to have to set up a root password.

**2:08** · So, I'm going to go ahead and type this in right here. Now, obviously, you want to remember what this is because you're going to have to use this quite a bit in the setup. You could also add an SSH key right now if you want to. I'm not going to do that right now to keep it simple, but you could always add this later. It allows you to choose some other features like malware scanner or Docker Manager.

**2:23** · And then, it's going to go ahead and actually initialize and set up. So, I'll check in with you guys once this is actually all spun up.

**2:30** · Okay, now that that is all set up, I'm going to go ahead and click on manage VPS and that's just going to take us to our dashboard. I'm going to go ahead and just skip through this questionnaire and this is what it will look like. This is where you'll be able to see information about your VPS and some metrics and things like that. So, now is where we have to actually get into the terminal, unfortunately, but I've got this doc which I will link right down below in the description and it'll have pretty much all the commands that you need in order to follow along with this video and paste them right in. Okay, so depending on your operating system, you're going to have to open up your command prompt, your terminal, your PowerShell, whatever it's called, get in here and then we'll get started.

### Installing Clawdbot

**3:01** · So, the first thing that we have to do is we have our local machine and then we have our VPS. We need to actually get into the VPS so we can install Cloud Bot there, not on our local machine. So, that's kind of called like SSHing into that environment. So, in Hostinger, you can see that there's a root access command right here, which is SSH root at and then this is like our IP address essentially. So, I'm going to click copy. I'm going to go into the terminal and then paste that in there and basically, it says that this isn't established. Are you sure you want to continue?

**3:32** · So, I'm going to say yes and now it asks for the password that we set up earlier when we were kind of configuring this VPS in Hostinger. So, what you're going to do is type in your password, but as you're typing it in, just like actually look at the keyboard because it won't show up as if you're typing.

**3:47** · But, you can see I'm going to go ahead and enter and now I am able to get in there and my password was correct.

**3:52** · Now, if you're typing it in wrong and you keep getting permission denied and you have to reset it, you would basically just come into here and then change your password right there. Okay, so now that we are in that environment, you can see it's no longer the directory of users Nate H. We are now in our server. We're going to do this next command, which is add user Claude. And now that we're adding this user inside of this VPS, we have to give it a password. So, it's going to do the same thing. It's not going to let you see it, so make sure you're looking at your keyboard when you're typing. All right, so I just set up the password. Now, I have to give this user a name, so I'm just going to go with Claude.

**4:22** · I'm not going to give it a room number, work phone, home phone, any of that. And we're going to say that the information is correct. Okay, so the next command we're doing here is basically just giving this user permissions, so the ability to essentially be an admin and install things, stuff like that. And then what we want to do is actually become that user. So, we're going to do su {dash} Claude, which is going to let us in there. And now you can see we have this green Claude, you know, VPS thing, which means that we're now making commands as this user.

**4:48** · And now what I'm going to do is I'm basically going to use the one-line installation from ClaudeBot itself in order to install ClaudeBot and all the dependencies that we need. So, I'm going to go ahead and paste that in there. This is also in the document that I've attached. We're going to go ahead and enter that. And now what it's going to do is it's detecting our operating system. It's going to make sure we have everything we need. So, it looks like right now it's installing node.js. And now it's asking for our password, so I'm going to go ahead and enter that in and then we should be good to go with the installation. So, you'll get to this point where it says that it's installing it.

**5:19** · And this could take, I don't know, anywhere from like 2 to 10 minutes. So, if you're sitting here for a while and you think it's stuck, just be patient. It'll finish up. All right, so now that it has been installed, it goes ahead and puts us into this onboarding flow. So, we can see that there's some security stuff to read. We understand that this is powerful and inherently risky, so we're going to go ahead and continue. We're going to go ahead and do the quick start. And now we're going to choose model provider.

### Clawdbot Onboarding

**5:45** · So, I'm going to go ahead and do Anthropic, and I'm not going to do the actual token because that is actually against their terms of service to be using your plan in here, at least the best of my understanding. So, I'm just going to go ahead and put in my Anthropic API key. Then, it asks you to choose a default model. So, in here, I'm just going to go with Opus 4.5. The next thing is it asks what channel we want to be able to talk to it. So, it could be Telegram, WhatsApp, Discord. There's so many different options. In this case, I'm just going to go ahead and choose Telegram bot API.

**6:12** · So, while this is loading up for us, let me just show you what you actually have to do in Telegram. So, you're going to go to your BotFather, and you're going to do this command, {slash} newbot, and that lets you actually create a bot. So, then I'm going to go ahead and call it YouTube test, and then it asks for a username for the bot, and I went with Nate YouTube test bot, and then this gives you an actual token, and that's what we're going to enter into the terminal. So, you can see I configured Telegram, and now it's asking about skills. So, let's just for now go ahead and click yes so I can show you guys what's in here. We can install the Homebrew, we can choose NPM, and then there's other dependencies that we can install.

**6:43** · So, you have to click space to select and enter to continue. In this case, you can see that we could do, you know, Bird, ClaudeHub. Um so, I'll choose that one. I'll choose GOG, which is for Google stuff. You could choose all of these other ones, Nano Banana, Nano PDF, and you can obviously add these later as well. So, I'm going to go ahead and just enter and choose those two for now. And you can see it actually failed installing GOG, so we can obviously go ahead and fix that later.

**7:06** · For now, we're going to keep going on, so I'm not going to add a Google Places API key for those. And then it asks if I want a Gemini API key for Nano Banana Pro. So, actually, yeah, I am going to go ahead and put that in there. Then, it asks about OpenAI. I'm just going to say no. I'm going to say no. No to 11 Labs, and then for hooks, we're just going to go ahead and choose skip for now. And now, we should be pretty much getting finished up here with the initial onboarding and installation. Okay, so now what it tells us is that we're pretty much set up, and the dashboard is ready for us.

**7:33** · So, we can actually view ClaudeBot in the web on kind of like a web UI and interact with it and see how it works there. We could also add a Brave Search API key if we wanted to enable web search, which we we could add later, of course, as well. But, what happens is it tells us to go to this URL. So, if I basically copy this and I go to my browser and paste that in, it's going to come back and just say, "This site can't be reached." Because it's trying to access a local host that we apparently can't hit. All right, so I'm going to open up a new tab.

### Starting Gateway and Tunnel

**8:02** · We're going to get back into that same kind of like working environment. So, first we have to get into VPS. I'm going to put in my password. And then we need to SU- Claud, and then it will turn green. And then we're going to actually start the gateway. So, I'm going to paste in this next one right here. And now it says that the command Claudbot is not found.

**8:20** · So, first of all, let me make sure that I am Claud. So, I'm going to say, "Who am I?" And it does say Claud, so we're in the right spot. And then I want to make sure we're on the right path. So, I'm going to do this command, which says version. And it looks like we're all set there. So, now we're going to try to go ahead and start the gateway back up. So, there we go. We can see that we have the gateway listening on this port right here. So, now that this is up and running, I'm going to open a new tab.

**8:42** · I'm going to paste in this command to basically create a tunnel for us. And then at the end, instead of doing host, you're going to actually go grab your IP. So, in here, your dashboard for this VPS, you're just going to scroll down and you can choose the IPv4 right there.

**8:57** · Copy that. And then paste that in. And once we shoot that off, got to put in the password for Claud. And this should actually be able to let us go to that URL and it should now work. So, now back in that original tab, if I go ahead and copy this link. There you go. We can now see that we have an actual web app with Claudbot. You can see that the health up here is okay. And if I go ahead and say, "Hello." It should be able to actually talk back to us and we can go ahead and start talking to Claudbot and setting him up.

**9:25** · So, the next step is to actually be able to talk to Claudbot through something like Telegram, which is what we configured earlier. So, I'm going to ask it, "Are you able to chat with me through Telegram?" So, it said, "Yes, I can absolutely connect to you through Telegram. Let me check the setup." So, it read the config, there's all this stuff, and then it says good news it's already set up. What we have to do is just give it some sort of pairing code.

### Telegram Connection

**9:43** · So, if you guys remember in the Bot Father, I called this bot Nate YouTube Test Bot. So, if I search for that, you can see right here, YouTube Test. I'm going to click on that, and I'm going to go ahead and click start. And what it's going to do is give us a pairing code.

**9:54** · And so, this is what we need to give to Claude Bot in order for it to actually work. So, I'm going to go ahead and show Claude Bot, here's the pairing code that I got, and it should be able to make sure that we're actually good to go, and then we'll be able to talk to it through Telegram. Cool. So, it looks like we're all paired up. I'm going to go ahead and open Telegram and just say, "Hey, testing." And hopefully, we should be able to see right up here that Claude Bot is now typing, and it's going to come back right here, and it says, "Hey Nate, I can see you loud and clear in Telegram." And then also shows up right here in Telegram as well.

**10:23** · Now, what's important to think about is the fact that the gateway has to be running on the VPS, so that we can actually access it through Telegram all the time. So, I just went ahead and cleared that out, and now I'm going to put in this command, so that it lets us actually create the file. And so, I'm pasting this in here, and the important things to see are basically that we have the exact start, and we have the always option on.

### Gateway on VPS

**10:44** · So, now I'm going to go ahead and restart it, and I'm going to check on the status. And we can see right here we have active active, and it's been running. And just to show you guys that that works, I actually went ahead and closed out of the terminal, so I shut down the local tunnel. You can see in our web app it says that the health is offline, but we're going to go ahead and check in on Telegram. And you can see I said, "How about now?" and it is still typing, and it is still able to communicate with us, meaning I'm on the go, I'm on vacation, I've got my phone, I've got Telegram, and I can still use Claude Bot.

**11:10** · So, I know it's a little bit intimidating, but I'm going to have the doc down below, which you can go ahead and copy all the commands, follow the video step-by-step, and you should be all set. Now, before we go, I did have to talk about security real quick, and I had to sit down for this. So, back at the beginning when I talked about why people are throwing this on a Mac Mini, it's because of the security aspect.

### Security Talk

**11:29** · Think of this less like an AI agent, but more like a VA that has access to your email and your files and anything else that you give it passwords or access to.

**11:37** · It's autonomous and it's an AI and it's non-deterministic, so you have to be really careful. It can run commands, it can open files, it can browse the web, it can talk to other apps, and if someone else gets control of your Claude bot, they can basically have control of everything that the Claude bot has access to. So, if it's hacked, the attacker could install programs, read files, and mess things up. Your secrets could get leaked because if all of those are in there and someone grabs them or if for some reason Claude bot kind of has all of its data leaked or anything like that, your information's at risk.

**12:05** · You also want to be aware of prompt injections. So, if it's reading emails and stuff, it may confuse if you're giving it commands or if someone random with malicious intent is asking for prompts or asking for, you know, certain access or passwords, things like that.

**12:18** · So, thinking about common beginner mistakes, that's why we wanted to set it up on a VPS. That's why I probably am not going to give this access to my main email or my main calendar and all my, you know, password vaults. I'm going to give it its own email, its own environments, and I'm going to give it a bunch of read-only access permissions.

**12:34** · So, really, there's all this information and you can do more research if you want to, but the moral of the story here is I think right now this tool is a great experiment, it's super cool, and it should be for power users who actually understand the risks of how these AI systems work and security and privacy and things like that. If you're just kind of getting your feet wet and you want to play around with it, go for it, but just be careful what you actually give it access to. And don't forget that I'm doing this on hosting your VPS, which you guys can once again go ahead and use the link in the description and get 10% off when you use code Nater Hrk.

**13:04** · Anyways, that's going to do it for today. Hope you guys enjoyed.

**13:07** · If you learned something new, please give it a like, that would help us out a ton, and I'll see you guys in the next one.