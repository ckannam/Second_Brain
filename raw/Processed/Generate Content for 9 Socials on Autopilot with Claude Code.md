---
title: "Generate Content for 9 Socials on Autopilot with Claude Code"
source: "https://www.youtube.com/watch?v=4Zaoo0YbYaw"
created: 2026-07-24
tags:
  - "WebClip"
---
![](https://www.youtube.com/watch?v=4Zaoo0YbYaw)

Get 30% off Blotato for 6 months: https://blotato.com/?ref=nate  
My FREE AI OS Course: https://www.skool.com/ai-automation-society/about?el=generate-content-for-9-socials-on-autopilot-with&hcategory=youtube-videos&utm\_campaign=free-group  
Full courses + unlimited support: https://www.skool.com/ai-automation-society-plus/about?el=generate-content-for-9-socials-on-autopilot-with&hcategory=youtube-videos&utm\_campaign=ais-plus  
Apply for my YT podcast: https://podcast.nateherk.com/apply  
Work with me: https://uppitai.com/  
  
My Tools💻  
FREE MONTH voice to text: https://get.glaido.com/nate  
Code NATEHERK for 10% off VPS (annual plan): https://www.hostinger.com/vps/claude-code-hosting  
  
In this video, you'll learn how to combine Claude Code and Blotato to automatically repurpose a single YouTube video into finished LinkedIn, Instagram, and X posts with custom visuals, all in a matter of minutes.  
  
Starting from a brand new setup, the full walkthrough covers installing Claude Code in VS Code, connecting to Blotato, and building a reusable skill that handles transcript extraction, platform-specific copy, and graphic creation. Every time you run it and give it feedback, it gets better, making this one of the highest-leverage content systems you can build right now.  
  
Sponsorship Inquiries:  
📧 nate@smoothmedia.co  
  
Connect with me:  
https://www.linkedin.com/in/nateherkelman/  
https://x.com/nateherk  
https://www.instagram.com/nateherk/  
  
Timestamps  
0:00 - Introduction & Demo Overview  
1:28 - Setting Up Claude Code & Blotato  
4:34 - Building the Repurpose Skill (Clarifying Questions)  
7:48 - Test Run & Fixing Visual Issues  
12:29 - Reviewing Final Outputs & Posting to X  
15:06 - Project Structure & Wrapping Up

## Transcript

### Introduction & Demo Overview

**0:00** · You can see right here, all I said was hey Claude, I want you to take this YouTube video and repurpose it into a LinkedIn X and Instagram post. Then I dropped in the link to the YouTube video and shot it off. Not only did it create all of these assets, but it also found bugs in its own code and fixed those.

**0:13** · And then we have this folder over here called drafts, and if I open it up, you can see that we have building beautiful websites with Claude Code, which is the video I gave it. And then in here we have Instagram with our actual post text and five visuals. We've got LinkedIn with our post text and a visual, and then same exact thing for X. So that exact workflow right there took me from having one long-form YouTube video to having a finished LinkedIn post, a finished Instagram post, and a finished X post.

**0:37** · And if I wanted to ask it to generate posts for six other social platforms, it could because it can use all of them and understands how they all work. So today I'm going to be showing you guys how you can basically nine X your content game using a combination of Claude Code and Botato. So right now when you're creating content, you know it takes a lot of time. And when you put all that time into creating, let's just say a YouTube video, it'd be really nice to be able to repurpose that content into different platforms as well. So what Botato can help you do is it can create the source, so it can look through transcripts, websites, PDFs. It can find inspiration.

**1:07** · It can then create visuals for you, so infographics, carousels, or videos. And then it can actually go ahead and schedule that stuff. So it can post it to nine platforms, it can create the stories, it can create the, you know, content calendar, and we can do all of that using Botato and automate it with Claude Code. So you guys saw a demo earlier, but I'm literally going to set up a brand new account today. I'm going to walk you through the exact steps that you need to do. And basically all we have to do is get our API key, add our MCP config for Botato, and then just connect our accounts and we're already ready to start creating content in less than 5 minutes.

### Setting Up Claude Code & Blotato

**1:38** · All right, so the way that I like to use Claude Code is within an IDE called Visual Studio Code. Now you could use this in Anti-Gravity, you could use it in the terminal, you could use it in Cursor, but I like to use Visual Studio Code. So if you don't have this, then just go to your browser, type in Visual Studio Code. You can download this for both Windows or Mac or whatever operating system that you're on. Now once you're in here, this is what it should look like and I'm going to walk you through everything you need to click on and everywhere you need to type, so don't get overwhelmed. If you'd rather watch like kind of an intro video and then come back, then I'll tag this one right up here and then hop on back over here.

**2:09** · And by the way, if you've been watching my channel for a while, then you've known about Bloatato. I showed it in N8N in this video and also in all of my kind of like faceless shorts videos, we use Bloatato to do the auto posting and scheduling. But now I'm just showing you how it's actually a lot easier to use with Claude code. So, that's exactly why once we're in here, we're going to go over to this left-hand side and click on the extensions button and all you have to do is type in Claude code. It'll be this one right here that's verified from Anthropic and then you just go ahead and install this. When you install it, it will prompt you to sign in with your paid Claude subscription.

**2:38** · Now, this does have to be the pro or max plan because if you're on just the free, you don't have access to Claude code. Now, once you've installed this, what it will do is give you this little orange button in the top right which lets you open up Claude code. And this is kind of like your typical Claude or ChatGPT interface where you get to talk to an agent right here. And now what we need to do is open up a project or a folder.

**2:59** · So, I'm going to go over to this top left button that says explore and it will say you have not yet opened a folder, go ahead and open one up and that's where we'll be working inside for this specific, you know, AI social media poster project.

**3:13** · So, I just went ahead and I created a brand new one. I just called it Bloatato. There's absolutely nothing in here and this is what your screen should look like. And now what we want to do is just basically close out of the welcome thing. We can go ahead and double click and then hit the Claude code button and now we just have our files which will be on the left. We don't have any yet. And then we have our Claude code agent right here that we are going to be able to talk to. So, what I'm going to do in the chat is paste in this prompt that says create me a new skill called repurpose YouTube video. It's going to create an AI social media manager that makes social media posts for LinkedIn, Instagram, and X.

**3:42** · The user will input a YouTube video URL and wants it, I misspelled this here, to be turned into a LinkedIn post, Instagram post, X post and each one should have a visual that's optimized for that platform. So PluralSight is basically going to take this video and do everything for us. I end this prompt by saying ask me clarifying questions one at a time until you are 95% confident that you can complete the task successfully and I kind of use this templated prompt from Sabrina. So shout out Sabrina. You guys can all copy and paste this exact prompt from my free school community or you can just copy it by looking at it right here.

**4:13** · So now that this is running, it's going to start going through that process. The first thing that it's doing is it's researching about PluralSight to figure out actually able to do. It's basically going to help us build out this flow where we drop in a video, PluralSight extracts the transcript, adapts the content for these different media platforms, and then it creates everything.

**4:30** · And then we're able to review it and then just basically approve it manually.

### Building the Repurpose Skill (Clarifying Questions)

**4:34** · Now before I start going through this flow of answering questions, I wanted to explain what is a skill because you'll notice I asked it to create a new skill.

**4:41** · Just think of a skill like a recipe.

**4:43** · If you tell your agent to write a LinkedIn post, it would look at the LinkedIn post skill and that would have the name of the dish, the ingredients, the steps, and then the finished output.

**4:53** · That way the agent could read the recipe and make sure that every single time you ask it to make that dish, it comes out perfect. So because we're turning this process into a skill, every single time we use it, it's only going to get better and more consistent. But anyways, now we're going to come back into Cloud Code and answer the clarifying questions. So it's asking me what program language to build this in. I don't really know what I want to do here and you may not either. So what I'm just going to say is whatever you think is best. It decides to go with Python because it's the cleanest for this kind of API driven tool. So then it asks, should the tool auto publish or do preview and approval?

**5:26** · I want you to always make sure I review it before you ever publish anything on my social media accounts. If you guys are curious about how I'm talking and words are appearing, then check out the description for the tool. Anyways, for the AI generated post copy, do you want to use Claude to write the tailored posts or should the tool just reformat the extracted YouTube content without an LLM? I definitely want to use Claude to rewrite the text content for the different platforms. Cool. So, we'll eventually have to give it an Anthropic API key as well as the Bot API key. Now, it asks about the tone of voice that we want.

**5:56** · So, in this case, if you had like a custom GPT or Claude project already that helps you write LinkedIn posts or Instagram posts, you can just go ahead and grab the instructions from that and put that here. But, for now, I'm just going to keep this really simple for the sake of the demo and just say platform adapted, professional on LinkedIn, um and on X you can be casual and maybe even a little bit humorous.

**6:16** · Now, it's asking for Instagram what type of post should it create? I would like you to create a educational carousel that looks like I am writing tweets.

**6:25** · And now, it's asking about the visuals for LinkedIn and X. For LinkedIn, let's do a key takeaway graphic. It should be clean and it should have some text that explains the value in the video. And for X, yeah, let's just do something eye-catching, maybe a cool quote.

**6:40** · Next question is, how do you want to review the stuff? Let's just go ahead and save everything to the drafts folder so I can take a look at it myself. When publishing, should you be able to selectively approve which platforms to post to? Yeah, I will tell you one by one which ones have been approved. I think I nearly have everything. One last question, should the tool that you edit the draft text files before publishing and have the publish command pick up your changes? Absolutely.

**7:06** · Okay. So, it looks like we're done with the question stage now. Now, you might notice that there's still some stuff that we might want to give to this platform like maybe some more information about our business. It doesn't really know anything about what we do and maybe things like the colors we like to use or our logo or something like that so that it can be on the visuals. So, now what it's going to do is it's going to build up those different tools. As you can see, it makes it to-do list and it's going to go through one by one and finish all that.

**7:30** · And also, what you're going to notice is on the left-hand side, we're going to start to get files and folders in our project setup. And that's really important because if your Claude code workspace isn't organized and it doesn't understand where files are. And if you don't understand where files are, then it's just going to get messy and it might be hard to manage the context.

### Test Run & Fixing Visual Issues

**7:48** · Okay, so that has finished up. You can see that we have a new project structure. So over here we have a PyCash, we've got .cloud with our commands. So this is essentially the exact same thing as skills. So this is the repurpose YouTube video skill that it created. You can see that it created some actual Python scripts to draft, to post, to publish. And so maybe we would want to clean this up and put this in a different folder called scripts or something like that. But the action item on us now is to actually set up our API keys.

**8:14** · So if I go into the .env, you can see that we have a Botato API key and an Anthropic API key that we need to set up. So the first step would be to use the link in the description and go to Botato and that will help you get 30% off for 6 months. Now once you get that set up, all you'll have to do is go over to the bottom left and go to your settings and then click on right here API. And this is where it will ask you to just basically make sure that this is a paid feature. So if you enable it, you will be on a paid plan.

**8:41** · And then you'll go ahead and copy this API key right there. And then in the .env, you'll paste this in and then you will save it. And then it's also asking for an Anthropic API key. I'm actually going to go ahead and use OpenRouter instead cuz you can access all the models there. So I went to OpenRouter, I created a new key and I'm going to copy this and paste it into Visual Studio Code and I'm just going to tell Cloud Code that I am using OpenRouter with Cloud models instead of Anthropic, but you can use whatever you want here.

**9:08** · So I just cleared the context and we're about to do a test run, but before that, I just wanted to show you guys something that we can do that's pretty cool real quick. So I'm going to go over here and I'm going to drop in a new folder and I'm going to call this brand underscore assets. Now what I'm going to do is drag in a profile picture of myself in the brand assets. It's this profile picture right here because I want it to be able to use this in the tweet style infographics or carousels that we told it we want to make. So what I can do now is go to YouTube. I've got this video I made a a days ago about building websites in Cloud Code.

**9:35** · Copy the link, come back into Visual Studio Code and say, "Hey Claude, I want you to take this YouTube video and repurpose it into a LinkedIn, X, and Instagram post. I've given you in the brand assets folder a profile picture of myself to use in these, you know, different visual posts.

**9:52** · Let me know when you've got some stuff ready to review and make sure you're updating your skill document with your findings from this first test run." So now it's going to read through the skill, it's going to execute these different Python scripts right here, and if it runs into any issues or any things that we told it like using our profile picture, it will update that skill document with. And here's an example of it already needing to make an adjustment is because it said, "YouTube is blocked by the web fetch tool. Let me try alternative approaches." So that just finished up. You can see that it started off by reading the skill. It goes through and it tries different things.

**10:23** · It made a to-do list, and it was able to create the actual text-based posts, but what happened was it actually failed on the visuals. So what it did is it added a known issues and findings section to the actual skill itself, but we're going to go ahead and try it again and we're going to see if it can fix it. So I just said, "Try to create the visuals again.

**10:41** · Make sure they are images, not videos, and we aren't worried about posting it.

**10:45** · We just want you to create the assets."

**10:47** · So it's once again going to dive in everything. It is going to investigate the templates, and then it's going to come back hopefully with something that we can review.

**10:54** · So visuals have been created this time, and apparently they're looking great.

**10:58** · And you can see once again it's updating the skill document so that that never happens again. Okay, so these have been created successfully. We've got our LinkedIn with a whiteboard infographic.

**11:06** · Let me go ahead and open that up real quick. It's putting all of this stuff in the drafts folder, and you can see we've got Instagram, LinkedIn, and X, and this is all for the YouTube video, which is called building beautiful websites. So it's keeping our stuff organized. So for LinkedIn, here's our visual. We've got a whiteboard that says building beautiful websites with Claude code, three key steps. We've got claude.md, front-end design skill, and then adding your brand assets to a folder. And you can see the bottom it also says full walk-through on YouTube at natehurk. And then we also have the actual post right here, which is the text-based copy of the LinkedIn post. So, let's say we like that one.

**11:39** · Let's go ahead and look at Instagram.

**11:41** · We've got the same thing. We've got the post right here with the different, you know, slides. And then we have the actual visuals. So, here's number one.

**11:47** · Your Claude dot MD file is everything.

**11:49** · It is a system prompt that runs before every session. We've got the next one, which is the front-end design skill. And then pretty much all of these I'm assuming are the same. We've got brand assets. We've got you don't need to be a developer. And we've got the difference between Vibe Coded and Professional. So, the one thing I will say about these are that I think this would look a lot better if we had our profile picture as well as like a blue check mark verified badge. So, that's something that we'll probably want to change. And then real quick just to look at the X post, we've got the actual text itself, which is um very casual and it's kind of more like a meme. And then for the visual, we just have a very simple quote.

**12:20** · But as you guys know, I want to make those carousels have the profile picture in there. So, I just asked Claude Code to put our profile picture in the carousel slides as well as adding a blue check mark. So, we'll see if we can get the job done. All right. So, look how cool this is. It fixed that workflow, so it now should have new carousel slides for us. But what it did is it actually had to resize our image because it realized that the Potato API wouldn't take it if it was too big. So, this was the original and then it resized it to make it smaller, but it still obviously looks the same.

### Reviewing Final Outputs & Posting to X

**12:51** · And now every single time that we run this for Instagram carousels, it should be able to make it the way we want it. So, let's take a look. All right. Here is the new Instagram carousel. We've got our name. We've got the verified badge as well as our profile picture. And so now it would just be a matter of optimizing the actual content that's put in here if we don't think that this was prompted well enough. And maybe adding one more at the end, which would be a CTA that says like follow for more or something like that.

**13:14** · But keep in mind, all I said was take this YouTube video and repurpose it. We didn't give it any context about our business, about previous Instagram or LinkedIn posts. We didn't give it anything, but literally just said make us content. And the only reason I'm telling you this is because think about how much better this will be as you start to add more business context, add more brand guidelines, and then iterate and refine. We've ran this workflow twice, I think, at this point, and it's gotten better each time. What would happen if we ran this 10 times?

**13:39** · And every time we gave it more feedback and more feedback, so that by the time we're ready to host it, so that if we wanted to run automatically every time I post a new YouTube video, it automatically gives us this stuff, by the time we do that automatically, it's already like a really rock-solid or battle- tested skill. And by the way, in Blo Potato, if you go to my videos, you can see all of the ones that you've generated, and you can also go to the API dashboard to see all of the requests that you had been making to Blo Potato. But at this point, the only thing left to do is schedule these out or just instantly post them now that we've reviewed them.

**14:08** · So, what you do is you go to your settings, and you have to log in with your different accounts. And it's literally like, let's say we wanted to log in with Instagram, we'd click on this, and it would just bring us to a sign-in page in Instagram, and it would connect everything very easy for us. And then after we've done that, you can see here I've only connected to my X account, it lets you copy your account ID. So, basically, it associates an account ID in here with Blo Potato to actually post on your behalf. But Claude code, using the right API endpoints, should be able to grab all those IDs for us, so there's really nothing manual here.

**14:37** · So, just as an example, let's make sure that it can actually post to X for us. Cool, that output looks great. Can you go ahead and post our content on X for us? All right, so that post is live. If I open this up, we should see on X that I did just make this tweet, which I'm going to delete right now. But just wanted to prove to you guys that that endpoint does, in fact, work.

**14:59** · So, at this point, now that we know this works, we could just build different skills within this kind of Blo Potato environment. So, we could build one for getting inspiration, we could build one for creating, you know, TikTok videos, whatever we want to do. But before you start scaling this up, it's really important to have some structure to this project, because we've got, you know, our Claude with our skills, we've got our brand assets, we've got our drafts, but we also have some scripts right here that are just kind of in the middle of nowhere. And we also don't have a claw.md file yet.

### Project Structure & Wrapping Up

**15:23** · So, I'm just going to go ahead and do {slash} init, which basically just reads through the current project structure and creates a claw.md file around what we have right here. And I assume at this point everyone's aware of what the claw.md file is, but if you're not, it's basically the overall system prompts for this specific project, meaning every time before you shoot off a message to Cloud Code or before Cloud Code reads it, it's going to read the claw.md file first to understand the direction, what tools it has at its disposal, what rules it needs to follow, things like that.

**15:52** · Which means you don't want to keep your claw.md file very long. I think best practice is to keep it under 150 lines. Otherwise, you're just going to fill up your context much quicker. So, now you can see that we have a claw.md file that goes over the overview, the commands, environment variables, architecture, patterns, things like that. Which now, as you can see, gives our project a little bit more structure right here.

**16:14** · But, I'm still not satisfied. What I want to say now is we have four Python scripts that don't have a home. Could you throw those into a folder, maybe call it scripts or something like that, and make sure that our other skills and claw.md files are aware of this and can reference it in the future. And that's just the way that I decided to set it up, but you could also say, "Hey, you know, we've got a ton of files here. Can you help me figure out a strategy to clean this up so we can continue to scale this project."

**16:37** · So, you can see that it made a new folder, it threw all of the Python scripts in there, and now it's updating other files in here to make sure that the whole project understands where everything is. So, that is going to do it for today. I think that you guys should be in a really good spot now, set up with Cloud Code, set up with Potato, to really improve your content game.

**16:54** · Just a reminder that you can access the resources you saw in today's video, as well as every other resource I've given out on YouTube for free by joining my free school community. The link for that is down in the description. And if you want to go deeper with this kind of stuff, then I definitely recommend checking out my paid community, AI Automation Society Plus. The link for that is also down in the description.

**17:11** · We've got over 3,000 members who are building businesses with AI every single day. So, I'd love to see you guys in this community. But, like I said, that is the end of today's video. So, if you learned something new or you enjoyed, then please give it a like. It definitely helps me out a ton. And as always, I appreciate you guys making it to the end of the video. I'll see you on the next one.

**17:27** · Thanks, everyone.