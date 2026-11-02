## OP — Major-Creative
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/

Hey everyone!
 
We're a small software house, and we recently bought a machine specifically to experiment with running local LLMs for software development.
 
Our hardware:
  
CPU: Ryzen 5 5500
 
RAM: 32 GB DDR4
 
GPU: RTX 3090 24 GB VRAM
  
We're currently running Qwen 3.8 27B (128K context) locally.
 
Until now, our main AI coding assistant has been Claude Sonnet 5.5 with Medium effort. Since we wanted to reduce our reliance on cloud-based AI services, we decided to experiment with a local alternative.
 
However, our experience has been surprisingly bad, and I don't mean that it's simply less capable than Claude.
 
The main problem is that the local model seems practically incapable of completing even basic coding tasks on its own.
 
It struggles to understand straightforward instructions, gets lost in its own reasoning, enters repetitive loops, and frequently fails to provide a single correct answer.
 
What's particularly confusing is that we're using exactly the same project structure and documentation we use with Claude.
 
We open the local model in the same project root directory, with access to all the .md files containing our development guidelines, project context, instructions, and documentation. These are the same files Claude uses successfully.
 
Yet, while Claude can understand the project, navigate the codebase, follow our instructions, and independently complete tasks, the local model seems completely lost.
 
Even relatively easy tasks that Claude handles without much trouble become a frustrating experience with Qwen. It often fails to understand what needs to be done in the first place, let alone implement the solution.
 
At this point, the difference isn't that Claude performs better. It's that Claude actually works as a coding agent, while our local setup feels like it barely works at all.
 
This makes us wonder whether we're doing something fundamentally wrong.
 
A few questions for people experienced with local LLMs:
  
Is Qwen 3.8 27B simply not suitable for autonomous coding agents, or could this be a configuration issue?
 
Could our hardware be limiting the model's reasoning capabilities? We're particularly wondering about the 24 GB VRAM limitation when using a 128K context window.
 
Are there specific inference engines, quantization levels, or context settings that make a significant difference?
 
Are there better local models in a similar size range that can reliably understand a codebase and execute multi-step coding tasks?
 
For those actually using local models with tools like Claude Code, Cline, Roo Code, or similar agents, what has your experience been like?
  
We're not expecting a 27B local model to magically outperform Claude Sonnet. We understand that we're comparing very different models and infrastructure.
 
However, we expected it to at least understand instructions, navigate a project, and complete relatively simple tasks reliably.
 
Are our expectations unrealistic, or is there something seriously wrong with our local setup?
 
I'd really appreciate feedback from people who have actually deployed local models for day-to-day software development, especially in legacy codebases.
 
Edit: We're currently using Ollama as the inference engine. As for the harness, we're still experimenting and haven't settled yet
    submitted by    [https://www.reddit.com/user/Major-Creative]  /u/Major-Creative  
  [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/] [link]    [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/] [comments]

## C001 — Repulsive_Initial308
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwjzs2rk8f7/

I can already tell you're running ollama.

## C002 — InfiniteBlink
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkrclmvfkw/

Haha we all start somewhere. But yea, it's great to get into local LLMs but the eventual llama.cpp jump is the next obvious step.

## C003 — nfored
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlg9bq4i3n/

I waited so long to switch and I kick myself once a day for waiting for so long; so I remember don't be lazy in the future

## C004 — JesusIsMyLord666
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlttl8lxuq/

Why not unsloth?

## C005 — 575_Inverse
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmm82ykdd0/

I'm using unsloth-desktop and indeed it's working really well. The backend is llama.cpp by the way.

## C006 — Yok82
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx7e28ki17m/

llama.cpp is the next Debian 😂

## C007 — xsilas43
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwu8e8yrsf8/

unsloth desktop is so good, their custom llama.cpp builds run faster for me on amd as well.

## C008 — DystopianRealist
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpk3zg23kz/

Unsloth is a llama.cpp fork.

## C009 — Damn-Sky
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx62cgn0a75/

unsloth is unreal. I switched from ollama to unsloth and difference is night and day.
 it is so freaking convenient

## C010 — amadeo681
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwl2pfe3s0y/

What are the steps for the jump

## C011 — Spearush
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlhysunuzl/

Anythingllm, then ollama, lm studio, zed, cursor, then llama.cpp.
 
Source: personal experience

## C012 — DeedleDumbDee
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm5it4gfj5/

Then vLLM (;
 
(You’ve just spent several thousand dollars to run multiple concurrency AI server for yourself)

## C013 — InfiniteBlink
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpu69a5y8y/

Is it worth exploring vLLM if I have two 3090s (ones a TI). Lamma.cpp has been pretty good so far with optimizations.

## C014 — pArbo
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwq8d620crn/

if you're running all on the single discrete gpu, then you have capacity for a second, or several other models. you don't really require it unless you're trying to cluster gpus and spread inference of a larger model across both. llama.cpp can also do this, but people don't refer to it as *the* solution for distributed inference, probably for good reasons that my tired monkey brain can't communicate right now.

## C015 — [unavailable]
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmd5oyp2g1/

[deleted]

## C016 — _RemyLeBeau_
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmgtq2hh2d/

They do, but running llama.cpp yourself, you get to control what settings matter for agentic needs. There are a lot of combinations and finding the sweet spot, you need to be able to control these settings.

## C017 — daft_knight
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnjmf1cd5u/

Is there a big benefit in jumping from lmstudio to llama.cpp?

## C018 — _RemyLeBeau_
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnmx602h0g/

The reason I skipped LMStudio is because they send your information to their data lake. To answer your question: I wouldn't know because I tried it very early on, then moved away.

## C019 — l1o2l
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwu947x0lnm/

What information do they send?

## C020 — InfiniteBlink
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlj7a9tdi9/

The easy way is to use codex or Claude and give it your specs for your GPU, find the best performative model that fits, so the quantization is a big factor if you have less than 24gb VRAM. If you want to use openwebui have it wire it up. It's crazy how easy it is to do. If you have a lot of RAM maybe look into strata and the Qwen next models. I run dual 3090s tensor splitting qwen. 3.8 27b Q8 and it's been amazing. Did some optimization and I get 75tk/s. I still use codex and Claude but to help me optimize my setup so I can ween myself off the cloud models. Good luck. You're fucked lol 😆

## C021 — BonnieReborn
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmm0ac80wx/

Yeah he’s cooked. One doesn’t simply take coding away from frontier models and move to local. Not professionally at least. It’s fun for hobbyists not serious work with that set up

## C022 — Callum_S_AUS
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwny0hqyb37/

Short of GLM/DeepSeek level, I agree, now. The difference is now too large.

## C023 — sonicnerd14
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwtgaa4ex0i/

Been optimizing my local stack for about a year or so through frontier agents. It was VScode with cline, cursor, then antigravity, warp, and eventually Claude code and Codex
 
Now, I mix in codex and Claude code to only work on the hardest stuff, but I used them to get all my local engines, model parameters, and local agents setup. A0 and Hermes agent across multiple devices. Only reason I still use Codex or Claude Code is because Codex has the most SOTA voice agent systen available to use out of the box, which speeds up building projects even more than just typing everything, and Claude Code is simply because you get access to the best models right there out of the box. Most likely Qwen 4 or 5 will make it so that if you have a halfway decent setup we might only need frontier anything for only less than 5 percent of tasks, and these would be the hardest tasks.

## C024 — [unavailable]
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmeed7tl0g/

[deleted]

## C025 — woeful_cabbage
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpsezohy1v/

Ollama used to, but not anymore

## C026 — 6ft1in
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwtj65uw9lu/

😲

## C027 — jandersson82
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx9ybugq9i8/

Start OpenCode, select model Big Pickle and ask it to setup the llama.cpp (or whatever you want to run as local LLM engine) for you. Ask it to optimize the settings for your hardware.

## C028 — OnyxProyectoUno
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk2xgkvzqb/

He confirmed it in a comment

## C029 — Repulsive_Initial308
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwklrc2eg0z/

lol, I didn't see that comment but it was just obvious.

## C030 — SDdrums
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwrxs6o7cf7/

Newbie here. What is the better option?

## C031 — bytejuggler
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx08pdl03hd/

Strata running Qwen 3.8 FlashNext running the ISTA DASLab IQ3_S or IQ3_XXS GCO-RCQ quant, Hands down.

## C032 — Arkasha74
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx8zmwgepwg/

No, not strata. Use llama.cpp until you get a handle on things and understand what's what. That will give you a baseline, then move on to more esoteric options.
 
If you start with strata you'll end up getting caught out by the buggy releases and wondering why nothing works that was working five minutes ago

## C033 — bytejuggler
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxaf2n4uyld/

FWIW, I think this overstates bugs & the likelihood of issues. I am quite actively following this project and even have my own fork and by and large if you're not using some very edge case setup or insist on deviating from recommended defaults for your hardware (like some people insist on doing) you'll be most likely be fine.
 
But I don't disagree with also exploring alternatives and vanilla llama.cpp (which Strata is based on) too. 👍

## C034 — Arcane_Satyr
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwud4j0u6xu/

llama.cpp or koboldcpp

## C035 — ColaEuphoria
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm0qskfhk5/

If ollama were a video game it would be like defaulting to 360p with no option to change resolution.

## C036 — cellcore667
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnaxg2l7ds/

Yes, Ollama $in Baden.
 
Edit: Lost in translation.

## C037 — rinmperdinck
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwsq3yrdnds/

OP using Ollama was the first tower, then making this post on Reddit was the second tower
 
The comments section is the Pentagon

## C038 — Apprehensive_Stop314
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxd867ose5g/

Obama without Biden Almost read as

## C039 — Abject-Kitchen3198
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1o132uso0/

What's the big difference?

## C040 — vogelvogelvogelvogel
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwki9a643vo/

if they didn't already have added it i would immediately have known by the level of effort they put in for the rest (about zero research)

## C041 — Obvious_Equivalent_1
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwzg623ly1s/

Honestly, Claude is a pretty excellent tool to fix a multitude of software challenges. That being said out-of-the-box setting up a real performant local model setup ain’t one of them.
 
I can’t shake the feeling that both their Opus and Fable models hold a terrible grudge against LocalLLM setting it up in any performant way without the user steering.
 
You will and without doubt end up with a Qwen 3.8 27B Q2-4 on Ollama, even if your machine runs with 32-48Gb VRAM. With the models training being so recent I can’t believe during training it didn’t read any of the multitude of Reddit posts, GitHub issues.
 
About a proper LocalLLM, even for machines uniform as Apple Silicon it still frequently gaslights me into setting me back to a smaller quant, even when you run a heavy Mac Studio. When asked through ”for memory conderns”, or “for concerns about the system performance“ (no jokes Sherlock, of course 100% GPU and the accompanying CPU cycles will strain my system that’s the whole goal)

## C042 — Creative_Diver3492
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwketw3ojab/

Haha 🤣🤣

## C043 — NarutoX666X
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlkyh7cae8/

What's better ?

## C044 — TrustworthiestFart
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlptn50bdx/

Llama.cpp

## C045 — sonicnerd14
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwt027yv5b8/

Ditched that trash a year ago once I recognize the power of llama cpp. Although, don't get me wrong it's good for beginners to understand how to get local stuff started. Then again LMStudio and the newer unsloth studio are probably even better options for that.

## C046 — HolaUsername
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk2ubdhnkx/

What quant?
 What temperature/model parameters are you using?
 
What harness?
 
What engine and settings?
 
There's a lot of information you left out that could contribute as to why it doesn't work. Personally never had any issues with 27b at Q6 other than it contemplating the meaning of life during every task. It's no claude, but it does get the job done.

## C047 — superbiche
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlnutsmyzn/

This. The fact no quant or sampling is mentioned, or that harness are thrown at the wall to see what sticks, makes me wanna write "skill issue" but I won't write it. 
 
Wait.. ..
 
NGL I'm just wondering but do you guys use a single box with 3.8 27B at ~128k ctx with multiple people ? 
 
Do you know even one single instance of this exact same Qwen would probably be able to tell you "what you're doing is a straight road to failure"?

## C048 — lumpyspacebreh
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwksv5pa9b4/

Same, built my own harness, get my desired output after 2-3 turns.
 
I think the issue may be people slap 27b in some web chat ui and then ask it to spit out code or something, but it’s hard to say with no context from op.
 
The harness, toolset, prompting, and settings matter almost as much as the model itself I would argue.

## C049 — Ratiofarming
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk9gmpqtuo/

I suspect he doesn't know half of those things are even a thing, which is the reason their LLM performs so poorly. Because it's basically not set up for the task at all.

## C050 — pheoxs
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwssg1jub34/

Okay but Q1 is smaller and saves bandwidth so obviously it’s better. Why doesn’t it do anything right I don’t get it this sucks. Open models sucks, Claude is better. /s

## C051 — Turbulent_Office1340
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwy9v1p3o9s/

Q1 is unusable.. i begin to see the trolls her..

## C052 — StillOnTheInterweb
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwklsw5ddi8/

Well thankfully they get very detailed and helpful advise from reddit subs on local LLMs!

## C053 — superbiche
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlz940zixx/

If only they had a LLM to read from this sub and even the weights and...
 
Wait...

## C054 — MarcusAurelius68
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkk3kgv1r4/

It is wordy, that’s for sure. I prefer QFN over 27B.

## C055 — Minute-Plantain
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlbg4sbkwy/

The "meaning of life" stuff is why I stopped using Qwen. Its very capable but awful at staying on task.

## C056 — FastHotEmu
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk0fdkpqjl/

No, that's not normal for 3.8 27B. Even at Q4 it works really well.
 
You are running the wrong model, the wrong engine, or have a configuration problem.

## C057 — 575_Inverse
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkfosnyfmp/

I say all three combined

## C058 — FastHotEmu
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkw9v3yx0l/

lol. It's funny because you really have to go out of your way to get it wrong. If you just download llama.cpp and an unsloth 27B quant, you'll get it running - even if slowly. I wonder what OP did.

## C059 — Erik-Zandros
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwr6l585sbn/

Non-coder who’s experimented a lot with local and cloud based AI here. I think your issue may be trying to use qwen as a drop in replacement for Claude sonnet. Your existing skills and background documents are probably taking too much context window which limits its ability to think. And with just 24GB vram you’re likely running a 4 bit quant which further reduces accuracy over full precision qwen.
 
That being said I don’t think even running full qwen will get you to Sonnet level coding ability. I run qwen 3.8 27b at 8 bit quant (near lossless) on a dual RTX 3090 rig and it still doesn’t answer questions as well as Chatgpt medium thinking. And I’ve even run a heavily quantized version of Qwen 3.8 flash next (a significantly more powerful model) and it couldn’t compete. I’m not talking benchmark scores I’m talking real world research and reasoning tasks.
 
If you’re serious about replacing sonnet for your business workflows with a fully local AI model your best bet right now is to invest 30K in a dual RTX6000 server to run something like DeepSeek 4.1 flash or GLM 5.3 or an equivalent model. Before doing that though you can rent an AI server on someplace like vast.ai to see what class of model you actually need.

## C060 — Bagelsarenakeddonuts
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwjsxppu0f4/

I have used qwen 3.8 27B for many tens of thousands of lines of Rust using a 5090. This code has passed tests and been reviewed by other LLMs (opus, fable) and it seems solid. I use the "swift" version of it to drastically cut down on thinking, with a great deal of success.
 
There is no better model in a similar size range. The next up is probably flash next, or GLM 5.3 flash, or mimo flash or deepseek v4.1, all of which are many times larger, but MOE so there is that if you have RAM.
 
Sounds like a harness or quant issue?

## C061 — InfiniteBlink
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkp1yk23kx/

I've got qwen 3.8 27b Q8 running on dual 3090s tensor splitting the model. Im trying to figure out the best way to use it for coding. Im just starting to figure out whether to use codex/Claude to design the app then have Qwen do the grunt work, then review it. 
 
Do you have any suggestions on how best to use my local setup and both frontier models? I mainly use my setup with a Hermes agent for controlling home automation stuff, networking, downloading stuff, and other creature comforts. Im barley using its capabilities...

## C062 — Biotot
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwljwqub34x/

I've got the same setup, I just have opus directly run Qwen as a sub agent for me. It keeps it on task and kills it when it starts looping
 
I'm using vs code copilot (shoot me. I know, but it works)

## C063 — InfiniteBlink
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwllh5zhr4z/

Interesting. Has it cut down significantly on your token usage?

## C064 — Biotot
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm7jsn5dia/

Massively. 
 
I also have codex to do large planning steps and docs, but then use opus+Qwen for execution. 
 
Codex doesn't work well with byok sub agents (in vs code) but copilot works perfectly

## C065 — Dubious-Decisions
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2ugj0vlia/

Curious how you have copilot configured so it will consistently use the local model as a subagent while using Opis driving the main session. The copilot settings (in the UI) seem to be either a single model or auto and auto never picks the local model.

## C066 — Bagelsarenakeddonuts
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnexazbhyb/

Ive been using BMAD method with bmad-loop. I do a very detailed design and breakdown with opus, and then pretty much hands-off build the whole thing with qwen locally. Its not perfect, and Im still working on a better system than bmad-loop, but it does work. I use claude as an orchestrator to answer questions from the qwen subagents running stories, and fix any hiccups and make sure nothing gets stuck. 
 
I run a precheck so that one instance of qwen reviews the scope of the story and sends back any issues to claude before wasting hours. Once its good, then a new instance of qwen builds out the code. As part of the prompt I have a series of code quality rules that needs to be followed specific to the language being used to prevent it taking lazy shorcuts. (IE, per instance justification of "unsafe" in rust) that a second instance of qwen needs to validate or else it gets sent back to fix. These extra checks take about twice as long, but shortcutting the debugging and troubleshooting and hung effort makes it almost a wash in the long run, but much cleaner.
 
I run 3 instances on ninfer on a 5090 with context caching. I do shared prefix with eg, the story context, files, code standards etc, since all agents use the same ones, that massively speeds things up.
 
Ive tried a few things, and its critical that the spec be immaculate. Qwen 3.8 27B can write really good code, but it can't do that AND design and troubleshoot and keep the overall vision simultaneously very well. Not enough context.

## C067 — hotmerc007
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm337hwdr7/

Would you be able to provide a little more info on your specific config for newbies. Seems like you have locked in a solution and I’d love to replicate. Many thanks for any further input you can offer!

## C068 — Bagelsarenakeddonuts
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnkpj4us9t/

I replied to InfiniteBlink below

## C069 — Apprehensive_Stop314
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwjsld6nj50/

What model quant exactly, via what engine and with what settings are you using?

## C070 — dreamyrhodes
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx01c8e0bz7/

Your expectations are unrealistic. You need to handle small models differently. While a huge model like Claude with its enormous context and knowledge you can throw something at like "build me destop app with these features..." small models you need to talk to like a junior. Go step by step. Add feature by feature. Ask it to summarize every step and document what it has been doing.
 
You totally can code with a 27B model, even a smaller model or a MoE model. You just need to work with it differently. It requires more effort in planning and prompting from your side.

## C071 — ConsiderationFair657
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxex4gs9k83/

Absolutely. It is unrealistic to hand a small model a prompt like "Build me a 747" and expect it to fly. Small models work great if you break down tasks into manageable steps. I perceive there are many who just want to write a single prompt and have the model do all the magic without understanding the process involved.

## C072 — Abject-Kitchen3198
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1lwdh42hs/

Is the effort needed still lower than coding manually? Explaining things in enough details to a junior so he can just translate them to code adhering to our practices, and then checking it and correcting it, is often more work for a senior than doing it himself.

## C073 — dreamyrhodes
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2upo78vxe/

Of course it is. The point is breaking it down into smaller tasks, not doing half the coding yourself. I mean you don't even have to know the language you code in at all.
 
A small model like Qwen3.8 27b does small coding tasks relatively well. A small model on a small machine (even with 24gb VRAM) can only keep a relatively small context and at the same time also fully understand it.
 
So my approach is switching between ask and code. The work is much more interactive. Prompt the feature you want. Have it lay down the design without actually doing any code. Correct if it understood your feature wrong. Then tell it to implement it. Have it write a test and analyze the output. Move to the next feature and so on.
 
Of course the effort is much greater than telling Claude "write a photoshop clone for me" or something like that. But it is possible - and it won't refuse to work because of copyright, safety or some bs like that.

## C074 — jefoce
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwjvtwq3v6r/

I’ve been using Qwen 27B in both versions 3.6 and 3.8. They were both superior for their size. I’ve been upgrading my own prompts for agents to achieve good communication between agents and subagents in OpenCode throughout this year.
 
It became more and more capable when you slice into subagents with small responsibilities for a single direction, e.g., coding, code review, read-only postgres, and any other direction you need (the best practice overall). For most daily tasks, I can simply use it without worrying. But for big tasks, with Opus 5.5 as planner, it became a monster.
 
I also found that XML tags combined with CAPS for sections work much more strictly and effectively as agent prompts than regular markdown, resulting in higher success rates over long distances (even 200k+) to follow instructions.
 
You can just ask any Cloud AI to research topic how to build better with XML and CAPS for topics inside the sections to build agents, and you will get great results.
 
Just don’t expect the same behaviour as cloud models like Claude, since their models are already specified with good harness and learned how to work via their tool layer (which is also have its advantages), while large models simply have significantly more “thinking” space thanks to their knowledges across many fields, and that’s why local models can sometimes perform even better e.g. when searching for bugs, since Qwen 27B primarily focused on code and hit it more accurately.
 
For the context, I use: Unsloth Q8_L + F16 KV in llama.cpp with my own patches for the specific setup 5080 + 5090 + 32GB RAM. But I started from Q4 and it was good enough as well (just a bit more errors for the tools and earlier context drift).

## C075 — Express_Quail_1493
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwoqd3a6isj/

enters repetitive loops is the bigest sign that its might be your config. Most modern qwen27b rarely do this anymore older qwen suffered from this. newer ones thinks for very long yes(without a switft finetune) but newer is often always a coherent chain of thought dispite being long sometimes. maybe chat template issue? or harness not set to the correct token streaming ETC???
 
Edit: also if you are just starting out and having issues linking your harness to the infernce then
 
LMstudio-Bionic is a good start. a LOTTT better than ollama. they've done the hard work of connection for you. when u get more comfortable u can get the Raw llama.cpp or something else.
 
lol good colleagues dont allow another to use ollama. throw it in the bin. 🚮😂
 even your qwen27b can setup other infrence engines for you once u get Bionic installed. i used my LMstudio+qwen to setup my own llama.cpp and then ditched him afterwards

## C076 — Lopsided-Comedian-32
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwsy2p3j5pe/

This guy gets it. Ollama out of the box makes an assumption on context for Qwen 27b and undercuts it massively. Got to make a config file/model file with context like 128k for example or it will be a horrible experience. Plus the Swift 27b fixed the overthinking so it’s like twice as fast now.

## C077 — tinny66666
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwrouvqe5r6/

Also the default/wrong template can cause some pretty weird looping effects and errors.

## C078 — Smooth-Television-48
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rws5h4gfrtx/

It sure does this if the kv is quantised hard

## C079 — an0maly33
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwy776p4ski/

Qwen 3.8 27b starts out great but once it gets some context loaded up, it inevitably spirals into a thought hole. I've endlessly fiddled with settings and reasoning levels. It will always get stuck in a thought loop at some point. Someone suggested using pi. That was my main driver. It still did it.
 
I'm now on qwen next flash through strata and while I haven't done any deep coding with it yet, it's overall thinking is FAR more reasonable and concise.
 
"Check this code and see what this error is about."
 
27b: "user wants me to check the code. Reading. Ah, I see the problem. I'll prep the edit. Wait, the user said there is an error here. Maybe there isn't actually an error. No, I'll make the edit. Wait, the user is human and humans are known to do drugs from time to time. Hm, I think this edit should work. Editing. Wait, if the user loves him some drugs, he could be tripling balls right now. Editing. Wait...(loop endlessly.)"
 
QNF: "user mentioned an error. Reading. I see the error. Editing. Done."

## C080 — Extreme-Childhood251
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx5lbdb6zz7/

This ^
 
It'll be still worse and much slower than claude, but in my experience WAY better than qwen 27b. Also qwen4 is supposed to launch next week, so don't waste your time by a lot

## C081 — pioo84
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx0v6grhztx/

Qwen 3.8 27b created nice android apps for me. It plans, designs and codes it. With proper tools and pipelines of course.
 I have moved to Flash Next already, but yes, 27b is capable to do so.

## C082 — colonelx_
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2kurtuk6c/

Could you share your hardware specs? Also, which coding agent are you using?

## C083 — Pablo_the_brave
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6zhpttmzn/

You didn't even post your model parameters (temp, top_p, etc.) or what LLM server you're running. That right there tells me everything about why you guys aren't getting good results. Honestly, I don't even feel like reading the rest of the post without that info. All I'll tell you is: you've got the model, you've got its parameters, and then agent setup is just as critical. There's a ton of useful info right here on this sub—just use the search bar.

## C084 — InsurmountableMind
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx81rvuajdu/

I had much the same feeling. The agent setup and the orchestration is crucial to control the flow of data. Happy hunting to OP!

## C085 — Mysterious_Prune415
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwqh6f98t5u/

Just get opus to pull benchmarks and figure it out.
 
Maybe look into alternative harnesses like Pi.
 128k context isnt that great. And if you plug it into a bloated harness like claude code you will hit roadblocks

## C086 — yellowsockss
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm4oapltpg/

this whole thread is a huge red flag. nobody in here really knows whats they are talking about

## C087 — notMyPenis
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnp9fq8zaa/

That's the thing tho. I don't think anyone knows wtf is going on.

## C088 — Connect_Ad791
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwolc5xy084/

Easiest way to spot a bullshitter at the very least. The space changes so fast, you’re knowledge is outdated if you’ve been lucky enough to get an hours sleep.

## C089 — yellowsockss
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm9d04q3z8/

qwen 27B is nowhere near sonnet level. the closest to sonnet has been near 400B - 500B range. you’re basically using haiku for coding

## C090 — former_farmer
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwjvpbzay79/

Which quant and thinking mode?
 
Thinking mode needs to be xhigh. Quant ideally q6 or higher.

## C091 — 575_Inverse
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkal81uc9s/

with 24GB I seriously doubt they can go past Q4 and 128k context at Q8, the fact they omitted mentioning the harness, backend and inference settings tells me their setup is most likely faulty in multiple ways.

## C092 — LegitimateCopy7
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnvfaelg2p/

RTX 3090 24 GB VRAM
 
Qwen 3.8 27B (128K context)
 
 
getting a bit greedy here are we? either the model overflowed to system RAM or you're using a heavily lobotomized quantization.
 
Don't use Ollama if you're expecting a tool and not a toy. other inference engines may need various levels of tinkering and troubleshooting but they're the better paths to make use of the limited hardware resources you have.

## C093 — soulman901
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwo8dn4e6xt/

Not sure what’s going on but I’ve been able to get it to complete programming tasks for me. I’m on an M4 Pro 48GB and got it to make me a couple of games, like this Pac-man clone 
 
 [https://preview.redd.it/6d4tigsxipyh1.jpeg?width=3024&format=pjpg&auto=webp&s=40e86ed554550c9f6c0d740e6b8401091efc660b] https://preview.redd.it/6d4tigsxipyh1.jpeg?width=3024&format=pjpg&auto=webp&s=40e86ed554550c9f6c0d740e6b8401091efc660b

## C094 — Creative_Bookkeeper9
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwwr9gmhxnl/

Ive got a 5090 woth 32 GB RAM and a 3090 with 120 GB RAM. I hate how slow it is on my 3090, however you're biggest problems are likely quant like others have said, as well as the client you use and your documentation itself.
 
I use PI to code with, as well as some custom prompts running on xhigh thinking for everything. It is not worth reducing thinking on this model. For you, you're going to want to run ninfer for 3090, ninfer is very fast and will maximize what you can do. I would say you really want to have 200k+ context, I run at 200k-220k on my 5090. Bare minimum would be 150k. 
 
You also need to make sure you've got some good extensions and skills made. Sonnet has a huge context allowance, you do not. So you need to compensate by letting things work in a more round about way, such as only showing a list of utilities then it looks specifically at one to reduce the context usage. But now it takes 2 calls.

## C095 — Number1OchoaHater
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwjoz6t5h2c/

lets start with saying that 27b and sonnet are not in the same league, said that, what harness and inference engine are you using?

## C096 — wegster
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkedh17hr6/

What Quant? Get off of ollama. Use Strata, ideally get a bigger card (more VRAM), but look for one of the dynamic/mixed precision Q4 quants. Check thinking and temp settings. QFN beats it but 27B Dense can be pretty competent, close or same as QFN in real-world benchmarks on real repos I'm doing (~100K LOC so reasonable but not enormous), and my QFN generally runs neck to neck with sonnet.
 
Try using a simple harness like pi - I've had cline nearly self-destruct in some tests, but pi so far, literally beats them all.

## C097 — Oli_Luck
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwl16mys6n4/

Hello,
 
If you want people helps you - help them first with the things that matter:
 - Quant ?
 - KV Cache quant
 - temperature
 
these are the most obvious.
 
Then : you cant just switch from a frontier model to a local one w/o preparing the terrain.
 A frontier pone will be able to plan and code "on the fly" - a local one need structure:
 - planing features to local help files
 - chunking the job in small logical steps
 - being reviewed by an "auditor" ( same llm but another role ) 
 
Just explains what you tried to do in which context, they you will get reliable answers

## C098 — michinya
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwtki99rjxh/

I run inference for an engineering team working on complex codebases. The minimum model size we have been successful with is glm 5.3 nvfp4 or equivalent. It costs good money to rent the hardware. 
 
It's complex right now to not just set up but maintain an inference stack. What most teams miss when you move local is you also need to engineer your gateway even if you have the model optimized. The serverless inference providers do a ton behind the scenes to make these models work for teams. 
 
As others mentioned, it also requires the engineers to have tuned harness and change their approach. Prompt, context, and harness engineering all matter. I only use 27b models for well defined workflows with custom harness.
 
In the end, a bigger model compensates for a good chunk of laziness and skill issue. Local is the way,but it means learning how to do it

## C099 — stianhoiland
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwp0tk50k2t/

You likely have a config problem and a sizable knowledge gap. It takes a couple of days of focused research and learning to start putting the pieces together.
 
Your hardware is great for local. The jury is still out on whether your expectations are actually right-sized, though. You'll find out in time.
 
My setup and config, which is slow but usable and rock solid, impressive output (for local):
 
- 4070 SUPER 12GB (610.88)
 - 32GB DDR5 5600
 - Qwen3.8-Flash-Next (125B A6B model with 51B N-grams)
 - IQ3_S (125B means Q4 doesn't have to be baseline)
 - Strata 0.2.6 (build 0.1.51), CUDA 13
 - Config with almost nothing touched (i.e. many more things that could be tweaked):
 ```
 --model IQ3_S \
 --model-path "$MODELS/Strata/models" \
 --parallel 1 \
 --port 8080 \
 --access local \
 --vision off \
 --context 262144 \
 --mtp off \
 --kv k8v4 \
 --set kv-resident=20480 \
 --tune skip
 ```

## C100 — mozillazing
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwqy3w046n6/

you've got a 125b model running with 262k context on 12gb vram and 32gb ddr5 system ram? what the hell am i doing wrong lol

## C101 — Pixelplanet5
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx84ajmde3p/

you are not going anything wrong, this guy is just offloading most of the memory to the SSD which makes it super slow.
 
And despite how his comment makes it seem he didnt do much research or anything for it, he simply used Strata.

## C102 — Smooth-Television-48
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwru2sget2c/

Would be heavy disk tax. Hopefully its just reads and they down burn out their ssd

## C103 — curiouselectron
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwp94xret9f/

What rates do you get for this?

## C104 — yourself88xbl
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpv0qg2dut/

What are your main use cases. Have you been using it for code gen at all?

## C105 — Comfortable-Crew-919
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwss0z7myed/

I ran this same setup for a while with slow, but good results. Upgraded to 128GB of ddr5-5600 (lucky local FB marketplace find) and it transformed this machine into a workhorse. iq3_s avgs 75-85 tk/s at 128k context. Unsloth q4_k_xl is ~55 tk/s. I’m adding a second 4070 Super to see if I can open up 1-2 streams for sub-agents.

## C106 — FragmentedHeap
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwr2xodjqn8/

Or you can just ask claude to setup llama swap and vllm for you for qwen 3.8 27b with the best model for the current hardware and properly configured and use hugging face cli to get the model, and claude will set it up for you and you can tell claude to run benchmarks on it and find the optimum accuracy and speed for however many users you want and it'll shake it out.
 
I setup my whole home lab like this and I'm getting 90 tokens/sec with 3k prompt prefills on qwen 3.8 flash next at iq4 quant on one r9700 using the strata engine and it's purring like a kitten.

## C107 — aithosrds
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwuriw2j0dg/

Your quant is probably low, q4 is a minimum IMO. In addition qwen3.8 is notoriously bad with reasoning, so a better fine tune along with low or even disabled reasoning will likely yield better results.
 
However, with that being said: a 27b model is fundamentally stupid compared to a flagship model and you can’t expect them to function using the same harness and project structure/context when they are literally worlds apart.
 
You’re asking a high school boys soccer team to play a Champions Cup mens team and wondering why they are getting smoked. Qwen3.6-27b and Qwen3.8-27b are in my opinion far and away the best two coding models in that parameter range.
 
Settings do also matter, and keep in mind that beyond about 50% context a model gets awfully loopy. So on 128k context you really want to keep most of your tasks in the 0-64k range and that means using sub-agents more often to manage context.

## C108 — Patient_Tea_401
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwx9oodgo10/

Q4 is the minimum, but Qwen3.8 27b is not bad with reasoning. It is very good at it, if you have the right inference engine with full context lenght and unquantized kv cache. This will take around 64 GB of VRAM minimum. 
 
I have run it 24/7 on agentic tasks with oMLX Qwen3.8 27b-oQ4-FP16-MTP with full context. It has very long reasoning spurs with multiple turns. It has always eventually come out with a reasonable solution that far outruns 3.6. But it’s very important to have inference that doesn’t compromise quality for speed, by for example compressing the kv cache.

## C109 — Dracuvlad
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwyor0r0p7m/

i am trying to run this on my macbook pro m1 max 64gb 1tb. can you please share with me what is your setup and how is it performing for you right now?

## C110 — Patient_Tea_401
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1egufux7p/

oMLX running on Studio M1M 64 GB, Qwen3.8 27b-oQ4-FP16-MTP
 self quantised, but you can download also from Jundot hugginface. Standard recommended setting, MTP on.
 
Claude code in a different machine set up to use the Studio inference with anthropic style API.
 
It’s amazing. It does thorough code analysis, plans, executes and tests until a solution is found. Most of the time the solution is selected. It takes time, usually while I sleep though so I don’t have FOMO of the tok/s numbers.
 
Chase quality over speed. The greatest part of 3.8 27b is the persistency to follow the prompt (which also should be clear with its goals) through long reasoning and multiple turns. The harness plays a big role in this too, so the relevant context survives the compactions. Full context length is needed. 
 
If you want speed without quality compromises, most of the time it means hardware upgrades. The 2xtok/s “optimisations” in configuration almost always are a quality compromises. Not all, but most of them.

## C111 — Creative_Bookkeeper9
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwwfwq3dvab/

Dont suggest no reasoning, it's so unbelievably bad compared to even low reasoning.

## C112 — Patient_Tea_401
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwzqa7lprxf/

Reasoning is the absolutely necessary, if you are running tasks that require it like agentic coding or reverse engineering

## C113 — opravdin
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx04jlyo2w2/

no reasoning is a good option to run fast lookup i.e. for reading a bunch of code for heavier agent and pointing him at the exact location of some function

## C114 — caylyn953
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwyteph4omb/

OP definitely needs to set their expectations at the right level. Because a single 3090 won't even be able to reach Haiku 5.5 level of quality!
 
Maybe by this time next year it will be? Maybe.
 
But by that point in time they'll be expecting Sonnet 7.1 or whatever such level of performance. Which won't be happening.

## C115 — dsdt
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwjqzdeiqw3/

Bro local qwen 3.8 27b fixes bugs that claude left in my repos.

## C116 — 575_Inverse
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkbl90vdlw/

same here. it's damn thorough when it comes to revising and testing code.

## C117 — rkcth
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk8m8e88f5/

You don’t have enough system RAM to run strata, and you don’t have enough VRAM to run a proper quant of 27b what is the full name of the model you are using? LLMs are best run in systems with lots of RAM, the more, the better. Your system uses DDR4, you can grab 2x32GB kit for $300ish. Do that then install Qwen 3.8 flash next on strata using the 3 bit quant. If you want to go extra smoothly, install 4x32GB sticks.

## C118 — DickVonShit
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkwhr0xfvk/

Check your reasoning first. Unfortunately qwen models are notorious for overthinking which makes running it feel like a slog, especially locally. Qwen 3.8 being smart and doing well on benchmarks is on the max reasoning. I'd recommend giving swift 1.5 a try, it's essentially qwen 3.8 with a lot of the unnecessary thinking loops turned down while keeping about the same performance. If you've been on medium it's a significant bump. With swift you'll be able to get the performance of qwen 3.8 on max reasoning without waiting forever. However, you're also not alone in this, i've had a similar issue where i feel like I need to be unreasonably specific at times with qwen that i haven't had to do with frontier models in a while. 
 
This sort of thing also heavily depends on what it's doing. You'll see plenty of people posting benchmark numbers or proclaiming that it works well for them, and while I don't think anyone is lying, there is a pretty massive difference between what you can run locally vs the smarter models from claude or openai. 
 
The model is the model, the limitations of 24gb vram or 32gb ram don't make it smarter or dumber, it just affects the size of a model you can fit on your graphics card, how much context you can hold, and how fast you can actually run the model. 
 
Different harnesses can actually improve performance from what i've heard though, i'm using llama and opencode and it's solid.

## C119 — Longjumping-Road4113
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwojejtbf6p/

Have you tried strata ? The Moe option with specifically optimised Qwen coder?

## C120 — Emergency-Quiet3210
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxf578ergkj/

What harness are you using? I find qwen 27B is mode then enough for most coding tasks. Unless I’m vibe coding and expecting it to one shot a data pipeline I don’t really need frontier models. 
 
Try out LM studio + Pi harness or even opencode. I like Pi because it’s lightweight and uses less RAM

## C121 — flarpflarpflarpflarp
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwjpskbwx41/

Look at Strata

## C122 — rkcth
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk0xdldfvk/

32GB RAM though. They are going to have a rough time doing anything without bumping the RAM. 64GB they can run a decent quant of QFN on strata and likely he surprised by how good it is.

## C123 — skifreek
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk0vrcznol/

I am running into exactly this problem. So far I have been tweaking context size settings and thinking level. I set 32KB context window with my 32GB of VRAM (I would expect the model to run slow for you with 128K context as you run out of VRAM). Also I changed the thinking level from extra high to medium to try and avoid these endless thinking loops.
 
I haven't found the magic recipe yet and I am pretty frustrated so far. What are you using for inference and coding? I have been trying LM Studio and opencode so far.

## C124 — Perfect-Campaign9551
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk9qbqb350/

33k context is simply not enough to do any programming tasks

## C125 — skifreek
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlb07ndaqs/

This is what I am wondering. However spilling out of VRAM took me from about 6 tokens/s to about 1 token/s

## C126 — Badger-Purple
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmbd3lpy8y/

You don’t have the hardware period. It’s a dense model, and dense models will need GPU (not system ram) to be usable. At least as many GB of VRAM as billions of parameters, and we are not talking about Intel GPUs…

## C127 — DystopianRealist
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpgqk9qs9s/

32k context.... For perspective, Claude Code is 27k of system prompt reading before it even says "Hello."

## C128 — pjkm123987
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxhmxq0kzvn/

and 20k of them are guard rails

## C129 — overand
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwln8fnnnol/

You should consider using llama.cpp rather than LM Studio, but:
 
What quant (and whose quant) are you running?
 
I've had really great luck with 27B for coding, on a system with 36 GB of VRAM, so pretty close!

## C130 — PuzzleheadedArm3732
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx76s9v3q90/

Your expectations are probably a bit too high compared with Claude Sonnet, but Qwen3.8-27B should still perform much better than this. I’d suspect a tool/harness issue first.
 Try three things:
 Ollama now explicitly supports launching Qwen3.8 into Claude Code and OpenCode:
 ollama launch claude --model qwen3.8
 and
 ollama launch opencode --model qwen3.8
 
That gives you a much fairer comparison with the same tool loop, file access, shell, context management, etc.
 
Then also try the official Qwen Code harness, which is built specifically around Qwen and local backends.

## C131 — Fractoos
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmhdq9gk2p/

Look at strata. You can run 150B Qwen

## C132 — Kmic68
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk1ojxlrc0/

What quant, do you have a harness (pi, deepseek, etc?), what kv quant, is your temperature and other settings that effect output default?, what reasoning level? 
 
These all determine your answer. I have a lot of experience in this and have worked with 27B extensively.

## C133 — Naiw80
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk4mvv91gk/

I have not been using 27b since strata came out, simply because qwen 3.8 flash next is multiple times faster and maybe slightly stronger. 
 
I used my own harness with 27b (and still do with FN) the problem with small models such as the 27b is they simply don't know that much reliably, but if you give it tools so it can research and/or inject the necessary information in it's context it's a very intelligent model capable of solving most tasks I threw at it. 
 
For FN this is not as critical as it's simply a much larger model with a lot more knowledge, neither model will one shot most tasks reliably which is why you need a validation gate for good results.

## C134 — FerretBoom
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkhpnkl4m8/

Please post one of your prompts that the Qwen model receives
 Claude has a caching and ,rag pipeline, all kinds of proxies to route to hot zones, enough compute to retry requests, do internal unit testing. While you are querying against the model directly, which is way different .

## C135 — FerretBoom
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkkxe7yqp1/

Make sonnet create a 30 question coding reasoning test for qwen and see how it does, context shouldn't matter so is hardware, model is a model wether it's on a gpu or cpu

## C136 — Immediate_Compote743
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlodpor15t/

Installing HyperQwen will give you a much better experience

## C137 — Sexyvette07
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnwtcn33c1/

Sonnet 5.5 medium scores about 50% higher than Qwen 3.8 27b on Xhigh. The two models are not at all in the same league. The only open weights model that can get anywhere close to Sonnet 5.5 are models like Deepseek v4.1 and GLM 5.3, which technically could run on that hardware, but the speed would probably make it unusable. Even then, Sonnet 5.5 is usually better. You'll have to sink a LOT more money than that to do better locally. 
 
Try Flash Next Coder on Strata or Basalt and see if that serves your needs. Qwen 4.0 is also being released sometime next week last I saw, so theres a chance that Qwen 4.0 27b gets much closer to fitting your needs. Your system is severely limited by only having 32gb of RAM and theres also a question of what quantization you are using, what settings (this alone can destroy the quality of work and make it put out nonsense). If you arent paying the $20 for a basic subscription, IMO do it at least for one month so you can access Claude Code to have it set everything up perfectly. Or if you have the model hooked into an agent harness (or the Claude code interface workaround with a local model), you can see if it can successfully optimize its own settings. 
 
FWIW you can get a lot done with a $20-$30 cloud subscription. You can also use a hybrid approach and have Claude direct your local model also to reduce your usage and get better results than just Qwen running everything.

## C138 — IsaacLevinsky
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwo1fnlgwps/

Please post the quantization and runtime you are using and any other details. The quantization and runtime matter more than people realize it but once you get deep into it they matter more than anything else

## C139 — MLisdabomb
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwplrq6drj6/

Came here to post this - OP please share the exact quant and how you are serving it. Your experience with "can't complete basic coding tasks" is so strange compared to my experience with this model that I feel it is likely a configuration issue

## C140 — SeaRefractor
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwo2cy7hvvl/

If you can run it with Strata, I really recommend looking into Qwen3.8 Flash Next with at least IQ3_S or higher.
 
The reasoning capabilities are much stronger than 27B.

## C141 — Smooth-Television-48
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwrls0m4of5/

This is a fair amount of effort for a friday shitpost

## C142 — theamazingo
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rws4uecoyw4/

Effort for the AI that wrote it, maybe. No real human bolds that freaking much crap.

## C143 — 905cougarhunter
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwsuhnxcsyq/

ffs. Ollama is ass.
 
HyperQwen on github. Single mode. huge context (262k tokens) 
 
Fuckin balls out hard.

## C144 — outdoorsgeek
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwtk7aojzj5/

Yes, you aren't running this optimally right now and will get better results if you use the right inference engine and harness with good settings.
 
With that out of the way, you need to be honest with yourself on whether or not you’re willing to step back roughly a year in model capability from Sonnet 5.5. Remember Sonnet 4.5? A 256k context model that was decent at a single small task if you wrote out very detailed specs or had opus do the planning? That's about the peak of where you will be able to get with lots of work and tuning. It will be nowhere near the fully autonomous loops you are likely running with the current SOTA models.
 
I would tell you that your hardware is the problem and you need to be more serious than a 6 year old gaming PC for professional coding work, but the truth of the matter is that you'd have to spend an insane amount of money to get performance that looks like a modestly degraded Sonnet 5.5. Financially it's nowhere near worth it compared to paying the frontier labs. There are, of course, other reasons to run local, but seeing as you're running a business I imagine the ROI matters a lot.

## C145 — Civil_Fee_7862
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwtkiytz5b8/

24 GB VRAM is not enough for 27b because it will run it heavily quantizied.
 
The sweet spot seems to be 48GB for full context.
 
4-bit weights, 8-bit activations, 8-bit kvcache
 
Use a good coding harness like opencode

## C146 — No_Audience2449
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwvfrh6cqeb/

I tested Qwen 3.8 27B with Drupal11 coding task, only 20% right. It's unusable, because they train model with internet garbage drupal7, drupal8, drupal10. I read that if I want to make it pass 100% Drupal11 coding task, I need to train it for LoRa( rsLora-pro) with train data Drupal11.

## C147 — FudgeEducational2038
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1ck14t5sx/

The biggest things are that these models are not sensitive to quantization of the model very much, but they are extremely sensitive to Quant of kv. I am guessing you are running q4 or q6 kv precision?
 
What you need to do is go down to Q3_XXS by unsloth and then do fp8 precision if possible. Int8 is... Okay but fp6 is on par with q8/int8
 
Fp16/fp16 Fp8/fp8 Q8/q8
 
Don't go below that 
 
On a side note, you're approaching this wrong. What you should be doing is using strata to run 3.8 flash next GYRO S quant. 
 
It's going to give you better performance, while also running 60 or 70 tokens a second. It will run faster and have better performance all at the same time even at full precision.

## C148 — Sad-Chemist7118
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxfcvlbcfxc/

I keep repeating myself in this subred but use Strata with a 272k context if you can. I have a 16 GB GPU (4080) and 64 GB RAM on a PCIE4 SSD and it runs somewhere between 70-80 toks and a very Claude-like ttft, also with a massive first prompt of ~50k tokens. Is it as good as Sonnet 5.5? No. Is it as good as Opus 4.5 from ~1 year ago? Yes.

## C149 — dzedaj
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxfk36mppd0/

Use Strata with Qwen 3.8 Flash Next running the ISTA DASLab IQ3_S or IQ3_XXS GCO-RCQ quant and ut will be both: faster and better than 27b on your hardware.

## C150 — DisastrousProfit5204
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxfo3zrswip/

yes, switch to qwen flash next or qwen next coder. Strata handles it great and it's way better than qwen 27b

## C151 — Ejo2001
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxih2eqix7l/

I have been running qwen3.8:27b at NVFP4 (equivalent to roughly a q8 quant) and I have used it for agentic work, and it has been doing quite well for me. It isn't nearly as capable as Sonnet of course, but I have used it to build applications and worked on my own projects. It sounds like a configuration issue, but also maybe an issue of expectations.
 
I actually started with local first, and then moved to claude (Though I will go back to local soon, just needed Claude for a particular project). My experience so far is that Claude is waaaay faster, much better, and gets things done much faster. It might take 5-10 prompts on qwen3.8:27b to get it to do something that would take Claude 1 prompt. The reason is psrtially context window (128k won't beat 1M), but also that the model will struggle with big instructions, it is simply better when using it to implement small changes one at a time.
 
The harness I've used has been Roo Code and Pi Agent, and I suspect a better harness that is more optimized for smaller models would render better results. I am actually building a custom harness using claude code currently to try that theory (which is reason I switched for now).
 
But if I were you, I would either try to get another 3090, or upgrade to 64gb ram and attempt strata, it might perform slightly better, at much faster speeds. Also, try strata, vllm and llama.cpp, it gives you much better control over what models you load compared to Ollama.
 
Good luck!

## C152 — skipITjob
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxit3lz36hw/

Get Claude to help with the setup. 
 
I had issues with Ryzen RX 9060 xt 16GB and Claude found the issue, and a temporary fix while AMD released a better windows driver. 
 
It even built a tool to rephrase Claude generated text to make it less likely to be detected as Claude generated...

## C153 — vtkayaker
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnmysfxy91/

Qwen3.8 27B is kind of bad at complex software architecture, and needs a lot of tokens to accomplish tasks.
 
But within those limits, it does work. You should expect it to be able write simple scripts and useful command line tools.
 
I would aim for full 256k context, with a minimum of 128k. I found that 3.5 was somewhat forgiving of 4 bit quants, but I strongly prefer 6 bit quants for 3.8. Yes, this is a lot of VRAM: Anywhere from 32GB to 48GB.

## C154 — Many_Discussion_1696
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwt70jws9ep/

You have Claude, so you need to put Claude in Fable Mid or Opus 5.5 High. You're going to ask Claude to help you decide how to use and delegate work to your local LLMs, and you want to configure your local models for the best performance possible in your system.
 
Claude will verify your system, check what models can run in it, and then download and test them one by one. I did the same with my system. I know I can't run a lot of reasoning in my local system, but I leave Claude, ChatGPT, or Gemini to run the reasoning and do the planning. It then delegates to local models.
 
Local models takes longer building and coding and fails a few times but it works. Cloud-based agents have to verify the work after the local models are done, but the work they do is not billable, or you don't have to pay for it. It takes a lot longer do.
 
Please reach out if you need any help, and I hope this helps.

## C155 — OldEffective9726
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwv48gfxorm/

The Qwen3.8 27B dense version is bad. It cant do math and you would need a 5090 to get a high token rate. I much prefer the Qwen3.6-Claude-Opus-4.6-Heretic-Obliterated 36B-40B Q4 MOE version. M [https://huggingface.co/mradermacher] radermacher and Jackrong make the best remixes.  [https://huggingface.co/Jackrong] https://huggingface.co/Jackrong

## C156 — Perfect-Campaign9551
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk5bp3fwro/

You have enough specs except for RAM to run Strata with Qwen 3.8 flash next IQ3_XXS. It kicks ass and you should try that model instead
 
Try to update to 64gig RAM. Then use 3.8 flash next

## C157 — feverdoingwork
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk5t2kilr6/

configuration issue
 
nope, 24gb can get shit done, even smaller cards can.
 
q4 or better is smart enough. Make sure to use qwen's recommended sampling settings like temp 1(check the official qwen model card)
 
qwen flash is about as good, it reasons less(so it is less annoying to read it's thought traces) but i find it's not as great on difficult tasks that takes lots of persistence. I do think setting it up is less beginner friendly.
 
Just use pi agent with a basic  [http://agents.md] agents.md

## C158 — More_Personality_126
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkgol52wma/

128K context on one 3090 is your problem... the KV cache eats the VRAM before the weights even load )

## C159 — IllustratorInner4904
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkh1ido334/

Seconding the comment about qwen 3.8:27b fixing mistakes by claude.
 
Use the model in pi. Q4 from unsloth. Llama cpp backend, and one bash guard extension to block destructive / fork bombs / dangerous commands. 
 
It rips!

## C160 — RawFreakCalm
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkiry31uap/

What’s your harness?
 
Mine runs fp8 265 context and has zero problem creating for me. Deepseek v4.1 flash does most of my ai agent work and then 3.8 27b my really long code tasks. I’ll give my small team a project and come back in a day. It’ll always be what I asked.

## C161 — starkruzr
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkn806tp5t/

it sounds like you didn't do a drop of research before you set whatever this is up.

## C162 — Ell2509
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkofr91sbo/

My first question is, what quant are you using? Q4 on complex coding tasks will not be anywhere near as good as q8...

## C163 — GrungeWerX
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkw6gog2w3/

Ollama??
 
Lol, that’s your first mistake. Has a terrible reputation around these parts.
 
Next, would need to know your harness, because you’ll need one with Qwen. 
 
I’ll be back later with some suggestions…

## C164 — ThaSipah
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwl0i75so83/

It codes well for me, but it gets bogged down in the weeds too often on highest reasoning. Always hitting context limits on 128k.

## C165 — Aubrey_D_Graham
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwl3dus3wdf/

No Qwen3.6/3.8 27B are probably one of the most capable open weight models today. They are Opus4.5 level, 6-10 months behind. They are capable but need help. 
  
You need to implement the Anthropic advisor paradigm.

 
If your problem is a long multistep task, break the problem into subproblems.

## C166 — BarracudaDefiant4702
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwl942mc0bn/

You need a decent card (or more) that you can allow at least 250k token context. I have enough trouble getting it to work well in 48gb GPU with a Q4, I hate to think trying to run it in 24gb.

## C167 — Frail_Waif
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwl9h4s7zc1/

I've noticed a few things with a vaguely similar setup (2x MI-50 32GB with 32GB RAM, 2x Intel Xeon Silver Lake 4214R).
  
Qwen 3.8 27B (Q8_0 from  [https://huggingface.co/unsloth/Qwen3.8-27B-GGUF] Unsloth for me, using a fork of llama.cpp for  [https://github.com/mxxm-t/mx-llama.cpp] gfx906 cards) is really stupid if not given appropriate tools and information; in Hermes when my container was broken, it made shit up all over the place; in Pi with access to lots of tools, it was decent at solving problems but did make mistakes
 
Qwen 3.8 27B from ISTA-DASLab is tiny and even worse
 
Qwen 3.8 Flash Next (IQ3_S from  [https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF] ISTA-Das Lab) is much better and fits about as well on my hardware; I would try this next if I were you
  
I think the lesson here is that it's really hard to put a lot of world knowledge in 27 billion parameters, especially compressed. Small models can do good things with tools and lots of information, but you need to actively ensure they're using those resources. That comes down to harness, prompts, and skills/AGENTS.md. The biggest upgrade you could make, I think, would be more RAM and larger MoE models, if you can fit it. There's a tradeoff between model size and speed and it seems like you should be willing to sacrifice some speed to run larger, smarter models.

## C168 — mdwsr06
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlo8ql14m9/

I notice this happens a lot sooner on the old Qwen 3.5 9B models. It’s like once it gets to a certain point in its context length it just loses its mind. Likely the same issue in 27B since it’s the same architecture but more parameters. Probably just takes longer to wig out than the smaller models. Then again Sonnet 5.5 is highly capable.

## C169 — overand
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlwm184dr5/

I've had tons of great success with Qwen3.8-27B, and I imagine you will too, when you're set up correctly.
  
Install llama.cpp with CUDA (or the "llama" app)  
Don't be stubborn about this; ollama leaves a lot of performance on the table, and has mediocre defaults set up.
 
 
Change port as needed
 
Run the following:
  
llama-server -hf unsloth/Qwen3.8-27B-GGUF:UD-Q4_K_M --host 0.0.0.0 --port 12345 --no-mmproj-offload -c 98304
 
This is assuming you're running this on a headless machine, or with the 3090 not running a GUI in Windows or Linux. If you're running your desktop environment on a monitor plugged into the 3090, you're giving up VRAM.
 
The above config uses about 6GB of VRAM for your 96k of KV Cache / context, and ~16.5 GB for the model itself. That leaves some breathing room.
 
With the 96k context, you'll probably have better luck with pi than with OpenCode.
 
Things to consider:
  
Using a "model config file" with multiple configurations, as you're testing. (Not great when you have multiple users, though.)
 
Using a slightly smaller quant, like:  
-hf ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF:IQ3_S (12.1 GB, room for ~180k)
 
-hf unsloth/Qwen3.8-27B-GGUF:UD-IQ4_XS (14.3 GB, room for ~145k)
 
 
Looking into 'quantized kv cache' if you need more context. (You'll lose quality doing this, but it may be a worthwhile tradeoff)
 
Adding another card to get you enough VRAM to get more context.

## C170 — Hungry-Rip-2384
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlygpn1nz6/

to me sounds like a context problem. that'll be the biggest difference between Claude and Qwen3.8 local. you have over filled your context with project files... it will struggle ro do even the most basic thing in that state.

## C171 — BrodyFriend
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm1bxxhbqd/

Holy shit there are so many replies. Looping is directly related to temperature and repeat penalty. I didn't read all the replies, so I hope someone else explained it. Coding is something im inexperienced with. No think temp .3 sounds about right

## C172 — WishfulAgenda
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm2oi265cw/

Buy another card, tensor split, run it on highest reasoning, 160k plus context an q8. Maybe try vllm on Linux.

## C173 — ZallenDuZari
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm5muv15sz/

I've gotten ok results from Qwen 27b locally. I did it with a strix halo box tho so I had enough memory for context . I later switched to Qwen 3.8 flash next and I've straight up been able to vibe code with it.

## C174 — HenkPoley
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm8dsmzxk1/

How badly quantized is your KV cache? Keep it at 16 bit, or maybe q8_0.
 
Sonnet 5.5 is one of the most high end models. Qwen3.8-27B is near Anthropic/OpenAI lowest end recent models. Think Luna 5.6 / Haiku 5.5.

## C175 — FizzyDuncDizzel
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmahhpz3qd/

What agent are you using? The model has very little direction without an agent guiding it. 
 
Also that model really likes to talk to itself. Put thinking to low and have it hard stop somewhere around 20k tokens.

## C176 — _RemyLeBeau_
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmcwyp7ycl/

Don't use Ollama, switch to llama.cpp or vLLM. Also there's no way you're getting a 128k context on Ollama.
 
After you've switched inference providers, try the endpoint with a stock harness. You'll need to be diligent about the variables you introduce along the way.
 
Moving away from Ollama allowed me to control a lot of variables that matter for agentic workflows.

## C177 — Spirited_Eggplant_98
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmeeigcx40/

I’ve gotten decent results (by decent I mean it can write thousands of lines of code that compile and pass a decent number of automated tests) with qwen 3.8 27b awq5 on oMLX on an m4 Mac Studio. It needs about 64 gb of vram and 128k context seems to be the sweet spot. Basic plain pi as the harness with a couple of our custom mcp tools. Tried with oh mi pi and got way worse results. 128k context isn’t much these days hence why simple pi harness seems to work better. IMO many q4 quants are bare minimum for useful quality, q6 for most is the sweet spot. The awq5 is the best speed / quality we’ve found so far. It takes the Mac about 4 hours to do what sonnet can do in ~20 min so… yeah there’s that (but prefill is known to be horrendous on the m4)

## C178 — ISJA809
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmmp8qgbz6/

Same with 98003xd 32 gb of ram 5070 (12 gb) useless for coding

## C179 — a_lost_shadow
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmn96j9x28/

For reference, I'm having decent success with Qwen3.8 27B IQ3_XSS with 155k context window & K/V also Q4. Q3 is needed to fit on my local RX6800 (16GB). I'm running with llama.cpp and OpenCode as the harness.
 
A few things that really help with Qwen:
 - Drop the reasoning effort down to medium. It defaults to extra high and supports [off, low, medium, extra high]
 - Be very specific in what you ask it to do. The more it needs to assume, the more likely it will end up in a reasoning loop. After I started having Qwen grill me on the specs before starting, I've seen far fewer reasoning loops. For reference, I've been using Matt Pocock's grill-me skill. But there are others that will achieve the same
 - Limit how much you ask Qwen to do at once. I've noticed it likes to read in everything needed and plan everything before it gets started. This will sometimes put it into a loop where it reads everything, plans 90%, runs out of context and restarts. Interrupting it and telling it to focus on specific areas can kick it out of the these loops.
 - Be careful with your skills/tooling/AGEND.md load. Qwen likes to think a lot. Tasks that I've done with claude code in 20-50k tokens often take 100k tokens on Qwen. So you can really limit yourself if you have too many skills/tools, or your  [http://AGENTS.md] AGENTS.md is too verbose.
 - Consider using older versions of libraries that it knows well. It looks like it's only trained on libraries up to around 2024. If you have it use newer libraries, it's going to spend a decent number of tokens decompiling the library to see what's the new interface is. It may actually go to the web first, but I run my LLMs in a locked down environment with no net access.

## C180 — Bounce_back1225
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmnemgk7fo/

Pretty sure 32gb is like the bare minimum required RAM for LLM’s… if you are using it for legitimate business purposes I’d imagine you want AT LEAST 256gb RAM. I just want a unit for personal use and have a hard time imagining even 96gb will be enough…

## C181 — Popular-Direction984
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwn4hzlsrdu/

I think the only thing that’s getting in the way in your case is the context size; the model supports 256k - and that should already be enough to solve a clearly stated task

## C182 — ferargie
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwn4xvab6ao/

Dude I use 27b in my 5060 ti 16gb and it performs good with unsloth Q3_S quant!
 I have worked so many proyects with this. U have to use llama.cpp as the engine. CUDA version, last build, no reasoning effort, mtp enable, q8 i guess. Dont remember now. I use 80k context and i got 43tps.
 Coding with opencode every time.

## C183 — Drewskie92
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnbvvkpcbo/

Far out. I have a i9-11900k, 32gb of ram, and a 3090. I left the qwen 3.8 27b 4km alone for 7 hours today. Come back and it worked for 4 hours on over 40 pages of research documents for me. I use Bionic from LM Studio. I've also enabled their experimental unified memory option, and q4 for the k and m in model settings. I've also in the system prompt told it to make a progress.md and decisions.md to keep contextual awareness across sessions.

## C184 — cjadwick
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwngpos3ogz/

I use qwen 3.8-27b NVFP4 with a good multi-agent system and it outputs code on par with clause sonnet 5. The problem maybe you are using too low of a quantization level to get the quality you need. The other part of this is if you don't have a good harness even higher quality models aren't going to give you really good outputs.

## C185 — asankhs
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwniv627wkg/

You can try with a different mlx based inference or a coding agent meant for local models like optiq code

## C186 — moonlitpawprints
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnkx49i3dv/

Definitely sounds like a config issue.

 

Somewhat preference, but I would recommend reducing thinking to medium or low...the default xhigh is insane with limited context. Also aggressive work tracking to deal with resuming after compaction.

 

Yes. Most are pretty well optimized for Nvidia gpus, but it's worth considering some other details. For example, vllm seems better optimized for parallel agents while llama.cpp can be a little lighter for handling single requests because of how they each handle memory caching (both can generally work well, that's just my experience).

 

IMHO, not currently, but I'm sure there are people with more experience and other opinions.

 

I've been running with OpenCode. Adding instructions about tracking work, breaking up tasks, etc. went miles for being able to run locally. It's not perfect but is definitely capable of complex projects if they're broken into well scoped tasks. Don't count on its knowledge of current packages, provide references and a general outline. Also using type and unit testing can help it to fix a lot on its own.

  
For reference, I'm running a 4bpw exl3 version with fp8 kv cache, 232k context on 32GB VRAM.
 
Edit: using vllm, with MTP (2 spec tokens) and mmproj.

## C187 — skinnyzaz
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnnqkrs3aa/

I wouldn’t use anything lower than Q8 for coding, that being said I use qwen 3.8 27B Q8 for lots of coding of small web apps and website updates and so far it’s been great but I find anything under Q8 started to make mistakes.

## C188 — Maximum-Security5699
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnqp18zq1v/

Unless you’re using NVFP4, any quant below Q8 is going to be super lossy. Most people can get away with Q6, maybe Q5. Despite being popular, Q4 just isn’t capable of holding enough data to really work well with these newer models. They work fine for low context tasks, but as soon as you got past ~40k tokens they just fall apart.

## C189 — Old-Discipline233
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnr8688hi9/

If you had more ram I’d suggest going for the 3.8 flash next. I switched from 27b to flash next and got much more speed and intelligence. Im getting ~120t/s decode and ~4000t/s prefill with a 5080 and 128gb ddr5.

## C190 — joshhope87
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnwivj5y1w/

I'm a noob to local LLMs, but the GPU RAM is too low if this model isn't heavily quantized, especially considering it sounds like multiple people are using it at the same time. It's essentially designed to fail. On the other hand, if it's heavily quantized, it's not going to be as intelligent, which seems pretty important for what you're doing. So, the hardware is a problem either way for what you're trying to do. I have 64 GB of unified RAM and it seems to run fine for me on my personal computer, based on my limited experience with it.

## C191 — junhua119
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwo912em5cy/

I have an M1 pro 32gb running swift1.5-qwen3.8-27b q4_k_m on medium thinking effort using splash-m1 inference with max context 98k. My actual context is 66k with avg 19t/s on pi agent. Qwen3.8 27b base model thinks too much. Abit slow I am able to build a full stack web app and other personal projects with no problems. It's actually quite good and finding the errors on its own.

## C192 — talaman4eg
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwoa2189ndv/

My 27b to go is unsloth q6 xl, but I tried q3 xl and it worked just fine with opencode on its own. It needs sandbox to test code and fix mistakes, other than that it is able to deliver working product (python, bash, simple frontend), analyze logs and make fixes, implement features and so on. Backend is unsloth studio or llama.cpp, lm studio also works. Try out unsloth xl quants, they are really good.

## C193 — soloyeets
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwoamj90n8i/

use froggeric chat completion template for Qwen, bridges the gap your seeing.
  [https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates] https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates
 
edit: theres some community that likely has better templates, but this will at least get you off the tarmac

## C194 — Choubix
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwow4bqx19d/

Done still need these? I have never used them. Benefit is better tool calling? Tks!

## C195 — InspiredUserNamez
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwob1o1ve75/

The answer to your problem is in your post. It's the last line of your p.s. edit answer: you were using Claude in a really good harness. Now you're seeing the reason why Claude subscription is so expensive. It's not just the model nor the legions of GPUs but that harness in Claude Code is f***ing magic. That's the secret sauce. I've been working for months on getting Qwen-3-Coder-30B-A3B to produce fully functioning code let alone produce it reliably. My first step was to get reliable instrumentation and probes. You see, to begin, it's fine that the coder not finish the code successfully as long as it can honestly park jobs it can't finish. Then you dial in the success rate - after you can properly identify ALL failures. I'm up to like 40% success rate, 60% honestly parked, zero false positives (aka lying to me that it produced working code).

## C196 — NickReese
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwobdnfu3z4/

Colocation of complexity for small models. Without it you’re dead in the water.

## C197 — problem_def
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwohzmjc78i/

not quite same boat here but using ninfer-4090 with qwen cli basically replaced most of cloud for me. There is a popular ninfer 3090 stable git build with good updates but i don't have the link atm

## C198 — FuShiLu
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwoi2suowwy/

Works great here. Different hardware and of course tuned for the hardware. We use the Qwen3.8 6bit version on the Mac Mini M4 Pro 64 GB. Quite fast and seriously improved accuracy.

## C199 — Smooth-Television-48
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwrvtv340it/

Yeah its very much easy mode

## C200 — laxative_surplus
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwrm3bg3btx/

when you say with optimizations, do you mean compiler optimizations?

## C201 — salynch
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwv6v8f8o0w/

Or SGLang or NVIDIA NIM/Dynamo!

## C202 — solaris_var
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwwhwtj4rdu/

Not ollama. Afaik they used an early fork of llama.cpp, and tried implementing subsequent feature updates that mimics llama.cpp's, but just worse.
 
It might've changed since I last used it tho.

## C203 — Turbulent_Office1340
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwxxmynd21s/

Qwen 3.8 is not out from years.. lol

## C204 — MarketingOk3093
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx57enl6gm8/

Thats my hardware spec with 64GB DDR4 I was only getting ~20 t/s with Q6. I've since moved to Strata FN 3.8 IQ3 S aat 70 t/s. I would be really interested to see your Q8 27B Llama config...

## C205 — hahayeahisit
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxcjtxx3t0l/

What should we be using instead ?

## C206 — Coach_Unable
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx8whv9khic/

Whats the advantage of using llama.cpp over lmstudio? I am using lmstudio as host server (different harnesses) and have specific settings i changed in lmstudio (kv quantization/context size) is llama.cpp worth it for the "low end setup" user (normal pc with single gpu)

## C207 — HourLocation2038
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwtqs4gzixs/

Came to say this, OP hasn't told us anything about how he is running it.

## C208 — Otherwise-Mail-4654
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwzcqw0cp7n/

Yeah I was thinking the same thing. I assume OP was using the q4 just by the post

## C209 — MrRoyce
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxaoj0g9pr4/

I’m not OP, but the first time I tried running AI locally, I just got Ollama and downloaded some version if Qwen 27B and it was straight up useless, it would stop working on its own all the time, it couldn’t do a single task for me… so I get it that they’re lost and confused.
 
This time I’m using Strata and QFN and it’s actually insane what it can do, I finally get the hype for local models. 70-100t/s and it produced a code that Sol 6.1 said is better than it’s own wtf

## C210 — InfiniteBlink
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmfd6nvbfl/

Thanks man, appreciate the tips

## C211 — InfiniteBlink
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnoy7kff6s/

When you say you split up instances I'm Qwen do you mean spawning sub agents? Does clause decide the sub agents tasks? Sorry I'm starting to dive deeper down the sun agent world.

## C212 — Bagelsarenakeddonuts
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwojim7m6qq/

So BMAD is key to all this. it breaks down the project to epics and stories. So each story becomes a discrete chunk of code, with specific tests and requirements. It is packaged and ready for a smaller agent to work on. Once its at that stage, claude isn't necessary. 
 
So then bmad loop launches a subagent that does pre-flight checks, then it launches one that writes the code, then it launches one that reviews teh code, then the code is pushed to the repo mirror. Rinse and repeat for each chunk of code. If a preflight fails it goes to claude to adjust scope or context, if a check fails it goes back to the code agent to fix, and there are time limits and thresholds and time limits and such so that if it fails or takes too long it goes back.
 
I used claude to help work this, it took a while, but now it runs pretty well.

## C213 — InfiniteBlink
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rworfqhmnq8/

Interesting, I've never heard of BMAD before. Im currently having Claude and codex review a simple game app. Im curious how do I leverage BMAD, should I include that in my prompt when I'm starting a new project. Apologies for the stupid questions, hopefully your answers help other folks as we go down the rabbit hole 😆

## C214 — Bagelsarenakeddonuts
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwoypqops4i/

BMAD is a set of skills for your agents that you download to your project folder. It basically forces you/your LLM to build out a proper spec and plan before starting. It uses many more tokens, since every plan change needs to be reconciled to everything it touches, but that's the cost of going large. You can look it up, its very well documented and there are a bunch of videos and tutorials on it.
 
It also forces the agent to reconcile changes against the entire project instead of "oh I'll just change this one thing", since that causes ripple effects that aren't managed otherwise, which is the main source of project code drift from intent.
 
I use it for anything that would require more than about 5 regular sessions to complete. I don't use it for small projects, its too much overhead. But if the project is going to have a codebase larger than say 20k lines, its a much better structure for things. Its something you decide going into a project ideally, rather than half-ass add later.
 
There are other alternatives to it that have slightly different philosophies, that may be better for smaller codebases or projects.

## C215 — InfiniteBlink
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwp5utr93ts/

Thank you, it's another avenue to explore when I get further along.

## C216 — sirphoenix3000
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx07r63b8gx/

[https://github.com/noonghunna/club-3090/blob/master/models/qwen3.8-27b/vllm/compose/dual/fp8/mtp.yml] https://github.com/noonghunna/club-3090/blob/master/models/qwen3.8-27b/vllm/compose/dual/fp8/mtp.yml
 
Running this on dual RTX 3090 with the Pi agent has been a game changer for me. Club-3090 repo has many good recipies to try out if you got the hardware for it.

## C217 — New_Egg_1024
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxc62fnpxuo/

There is this recursive loop like process you can do with small model to start with Massive Vague goal, and via few iterations bring it down to phases with 100s of tasks, which are very well executable by even smaller models. 
 
Just like you would have to do with teams of hoomans.
 
It will -exactly like claude or any other llm- just guess-probability lock- things you do not specify. So requirement to go deep and validate and understand is exactly the same, so do not fire your engineers just yet, or ever. Rather work on their education plan, so you the knowledge capital in your company increases.

## C218 — dreamyrhodes
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxf5svaco11/

Correct. Just tell it from the beginning not to start any coding yet. Nail the features down into small parts and then do the implementation step by step.

## C219 — SpiritRealistic8174
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1i17d9r51/

This is the way. 
 
I've also used 3.6 and 3.8. I found 3.6 to be suitable for most tasks. 3.8 was a real step up. 
 
The biggest problem is the RAM and context window. It's difficult to get good results with a local model with insufficient resources. 
 
I've also been using Opus 5.5 as a deep planning and agent to put together specs and even sample code together for qwen 3.8 as well as testing best practices. 
 
I was getting good results before doing this, but after, even better. Qwen delivers great code according to my specs, but i'm not running the agent on long-form autonomous tasks across may files across the codebase. Any agent will do much better with a limited scope and task list. 
 
I've also been using 3.8 in a sandboxed Hermes instance. I've been very impressed with its planning and implementation abilities, when given an easily searchable persistant memory, plus explcit workflow patterns to improve content quality and accuracy. 
 
I think people running local models can benefit from studying what different RAM and setup configurations can do for model quality and ensuring that they are taking model performance into account in the context of system resources. Another benefit is understanding agent harnesses and workflow patterns to optimize what they're getting from them. 
 
Frontier models can be more forgiving (although they're not perfect) and this knowledge can help get more out of them, at lower cost, as well.

## C220 — Blue_Eyed_Behemoth
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxcs1vesplx/

Doesn't swift have their own licensing? Just curious if you ran into any issues with that.

## C221 — Damn-Sky
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx655rgilr9/

I always try to keep my sessions short.. make it update  [http://CLAUDE.md] CLAUDE.md and just resume in another session. (I am pretty noob to LLM though, not sure if it is a good practice)

## C222 — Twistpunch
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxb84gj6mjn/

That’s exactly my problem with QFN. I MENTIONED an error, nobody asked you to fix it.

## C223 — Blue_Eyed_Behemoth
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxcmuj0gbkw/

Are you using 3.8 flash next coder? Mine still spirals. I'm running a RX9060XT 16GB vRAM w/64gb RAM. I feel like every time the context gets compressed it just removes important information and starts cycling.

## C224 — MiaIsOut
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxiaoegv3c3/

the funniest part about 3.8 27b is that it will spiral for ages and then randomly remember what it's supposed to be doing, lock in, and nail the task perfectly

## C225 — pioo84
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxhz7425uas/

I belong to the dual 3090 gang, plus 128GB RAM. Using HyperQwen (vLLM) for 27b and Strata for Flash Next. With HyperQwen I have 3x250k context. With Strata I don't know how to calculate, Strata is very... exotic.
 
I plan with Hermes and code with OpenCode. I don't interact with OpenCode at all.

## C226 — stupidio_the_return
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx8czh9ohb5/

proper tools and pipelines, amen brother

## C227 — pioo84
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxhod7fzq91/

We are all plumbers.

## C228 — former_farmer
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpa07vvv6r/

The truth is qwen 27B needs 32-36gb of vram or unified to run at a decent quant and context size.

## C229 — Snoo_81913
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpljsnzkpt/

Nah I run Q4 XL Huihui with 164k context in hipfire on a 7900 xtx with 24GB VRAM and it's fine. Runs at 1500 t/s prefill and 95 t/s mean over 100k with no problems. You have to Quant your own so I keep a base copy and run it with the new ROCm as a backup. I give the finished product to opus to review and it's not perfect mostly just a few fixes here and there occasionally a one shot. Even Claude has said it's good for a local model. I use Pi as a harness. I ran Flash Next at Q3 and xxs and it's pretty decent runs about 65 t/s but prefill is slow (I've got a bottleneck I've got to fix) but the output is erratic. Likely I'm not using it right lol. But 128k on 24GB is fine at Q8 KV and you could push it bigger easily. I run mmproj and 164k context and it's 23.6GB on the card

## C230 — Choubix
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwouxcjb6w5/

Hi! Did you one shitnthisno4 do you give it a large set of instructions and guardrails? I need to get my kids to start small on AI 😅. Tks!

## C231 — soulman901
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpbey5nc82/

I’d have to look at the prompt what I gave it but it was a small paragraph telling it a few parameters such asking for a pac man like game with a cat for pac man and mice for the ghosts. When the cat eats a power pellet the mice turn blue for a period of time at which the cat can eat them. Make sure the pellets are in the corners of the map. At random periods a treat will appear that the cat can eat for different points. Make 4 levels that the cat will progress through. It delivered a mostly working game but I did have to tweak a couple of things and have it fix a couple of items but it runs pretty decent now

## C232 — SenorPeterz
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3u9tve36o/

This made me laugh out loud

## C233 — jtgyk
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxhe86invs3/

I got it to make a 3D Pac-Man game for me, and it took hours but it got it done in one shot and it works (mostly)!
 
Aaaand, this was on a Q2 quant of 3.8 27B, with KV cache compressed to 4_0, using Unsloth Desktop.
 
What's weird is when I try the Q4 quants, they seem not as smart and I have to do a lot more hand-holding. I wonder if anyone else is seeing this.

## C234 — reliablemomentum
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwzlkj80nfo/

check your sampler settings too, temp 0.7 with min_p 0.05 stops it looping on long context for me

## C235 — pragmojo
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6yektujdw/

I use the recommended parameters and it works great

## C236 — mtbMo
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2rxxlpajl/

Yes same here, running on a xeonV3 10c 128GB RAM and dual Mi50 16GB
 Runs Qwen-Flash-next about 600pps/40tps on strata engine.

## C237 — sadomazoku
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxgolwt1kf4/

for real ! When I come here, looks like everybody is runing qwen flash next on a very frugace vram setup.

## C238 — Kalahdin
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwu6vug4ucg/

.....

## C239 — kirbyfanner
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwuli2ftlsz/

I have some questions about your setup, since I'm new to this.
 
Why did you turn vision off? Does that increase VRAM or speed?
 
How are you running a 125B model on a 12GB VRAM device, even with 32GB of RAM? My 27B takes up 27GB of VRAM and I imagine a 125B model takes up much more than that.
 
What is IQ3_S?
 
What are your tokens/second? I get 40t/s on 27B on an R9700.

## C240 — caylyn953
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwyy1kyogbo/

Turning vision off means that part of the model doesn't get activated and can be ditched, saving space.

## C241 — Zestyclose_Yak_3174
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx9zhrqdmsg/

Interesting. I've been using the Dstar DS4 fork for M1 Max. There are many options out there and they all seem to have pros and cons.

## C242 — cagriuluc
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx4pkjqtp5v/

Have you tried FN as well? I am torn between the two but since FN is much faster on my setup, I use 27b only for vision

## C243 — Patient_Tea_401
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx5pfx4k49u/

I have run FN GSQ-RCO-GGUF:IQ3_XXS through splash engine (M1 fork, --bf16 kv cache). It's better for science and overall knowledge in my subjective experience. But at least the IQ3 is not enough to keep long agentic coding sessions on target. It drifts away and does not have the persistency of the 27b Q4 at these low quantisations. Can be also that splash engine is the cause of some of the drifts. Be aware of engines that do not publish divergence data! It should be the first metric on the repo.

## C244 — Chips_fr_
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2p1o3j3c1/

"Your quant is probably low, q4 is a minimum IMO. In addition qwen3.8 is notoriously bad with reasoning, so a better fine tune along with low or even disabled reasoning will likely yield better results."
 
wow, exactly the opposite: qwen is less sensible to low quant than others models and is excellent at reasoning. Thoses items are what it make interesting (but slow).

## C245 — FudgeEducational2038
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2y4lslkf9/

This exactly, the model itself can be quantized a lot without much problem. The KV is linear attention and sparse so the problem is that you must run your attention KV Cache at full precision or at least q8 q8

## C246 — Spiritual_Scheme8158
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxdplee86u9/

Fable 5.5 = Real Madrid, Barca, PSG, Bayern Munich, Man City...
 Opus 5.5 = Liverpool, Arsenal, Athletico Madrid, Inter, Napoli...
 Sonnet 5.5 = Borussia Dortmund, Tottenham, Aston Villa, Manchester United, Juventus...
 .
 .
 .
 .
 
27b model = Shanghai Port, Shandong Taishan

## C247 — feudalle
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxghtieoyhu/

That was my issue starting out i was using a q3 for 27b. It was horrible. Im using q8 now and its respectable for a junior dev. Break down tasks into bit sized peices then walk away.

## C248 — dsdt
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkdxkdqi04/

it reads all of it line by line for real which i really like, if you have time and like to debug your own code it is the best tool we have ever had.

## C249 — flatfalafel
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxjigjd4nts/

Are you making that harness available/os? I have some projects I'm working on and can't use my employers developed harness for obvious reasons.

## C250 — BonnieReborn
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmilqmb1k2/

This guy gets it!

## C251 — Omegaprime02
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm44e4hgo0/

If you're dead set on using LM Studio, try manually setting the KV to run on RAM, You'll see a speed drop, but not nearly that bad. You'll find it under load settings in the advanced options, set Offload KV Cache to GPU Memory to off, that way the weights are in memory at all times.
 
Edit: Looking at my files, which quant are you running? With 32GiBof VRAM you absolutely should not be overflowing. Are you running Q8?

## C252 — a_lost_shadow
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnlv6sn7oi/

What card do you have? With an RX6800 I'm getting around 35 tokens/s at 85k context fill. At 6 tokens/s, it sounds like you might already be partially offloading to the CPU.

## C253 — Catch_022
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx4eejw3i5h/

Can I do any relatively simple coding offline with a 10gb 3080 or is that a pipe dream? Trying to do some basic python, kobotoolbox and r

## C254 — Stats_monkey
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxaj5xcbtlv/

Single file scripts with little to no context maybe (think early chat gpt). Anything agentic that requires reading around a project is probably a pipe dream

## C255 — J35ter-
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxgnrw5gz35/

Yes you can. You just need to find an appropriate harness. I use Deepseek Harness and Codex. Each has it's own merits. Also, watch the context and compaction sizes. 27b is good, but if you have 62gb RAM and 16gb+ VRAM, you can already use Atrata with qwen 3.8 Flash, which is a completely different league (forget coder)

## C256 — Borkato
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxhh4sjkrdu/

Try pi with Qwen 9B or 12B

## C257 — Throtex
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxiisbyeqat/

Not to mention, hobbling the context is killing the entire point of that Qwen model. It “thinks” loudly and refines its output that way. Running at its full context window uses 40GB including the model itself, on my A6000.

## C258 — Altruistic-Wolf-3938
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm0qnbw5gi/

24+12?

## C259 — yourself88xbl
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwq0d1rvxk0/

have you rean any sort of head to head comparisons for code generation against the cloud models?

## C260 — Giuseppe_0112
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx9sc31yxep/

Couldn’t you just run codex with llama as the server? (excuse me if this question seems underqualified, I’m not a software engineer myself. Just wondering)

## C261 — Stats_monkey
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxagmywxjtt/

That's essentially what the ollama launch command is doing under the hood

## C262 — Business_Opening6629
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnama3fg69/

I tried strata didn’t really get great performance it worked but I was getting better performance from llama cpp

## C263 — Miserable-Answer-416
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx9xaydpr51/

This will wear out you’re SSD pretty fast

## C264 — oktollername
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxconq31nz4/

this, I‘ve been running qwen3.8 next with strata on 24GB VRAM and the speed and capability are pretty good, definitely usable. Been porting some of my automations to it, it‘s also had no problems doing dev tasks that involved calling powershell from bash, which then ssh exec‘d into a server to then exec into a docker container to diagnose stuff there. a year ago most models struggled to simply write powershell lol.

## C265 — vogelvogelvogelvogel
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkkiu70l9e/

128k (or as someone mentioned 80k at least) for agentic coding. try pi

## C266 — nfored
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlpft4i3l1/

What quant I got well over 128k context on a 32gb vram 100% gpu in Q4

## C267 — PigSlam
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwo8kn0wk9u/

32k context window is too small. You should be able to run 192k+ with 32GB vram. I can in my R9700.

## C268 — dreamyrhodes
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx0akx2nwkg/

If you do not have the context to work with, limit thinking and introduce an extra step of summarizing previous work. Have it document everything in an md file. Then work with it step by step. If it fails to get a feature down, divide it into smaller steps and let it recapitulate after every step what it has been doing.
 
I am running Qwen3.6 35B A3B with 132k context on 16GB VRAM and 48GB SysRAM. It works but you need to approach everything slower. It only can do relatively small code tasks so divide your project down to small code tasks.

## C269 — FudgeEducational2038
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1akis7esj/

Use q3_xxs by unsloth. 
 
These models are quantize aware training so they can be quantized but, the KV is extremely compressed already and sparse so it should be at fp16 if possible 
 
Fp8 is the next best then int8. 
 
Don't go below Q8 for kv cache. 
 
Trust me.

## C270 — Miserable-Answer-416
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx9tikfsuxu/

Try using Bionic from LMstudio with qwen3.8 (the harness is everything)

## C271 — _RemyLeBeau_
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnk3p91twj/

I like this idea, but I would be green I this area. Do you have a prompt I could use and learn from?

## C272 — FerretBoom
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwo3xy5u3kw/

Qwen 27B — General Coding Reasoning Benchmark
 20 questions | 100 points | Closed-book | No code execution
 Instructions for the model
 Answer all 20 questions independently. Do not execute code, browse the web, or use external tools. For tracing questions, give the exact output. For implementation questions, give complete Python 3 code. Explain your reasoning briefly (1–3 sentences) except where code is required. Do not silently guess. Preserve requested time and space complexity. Number your answers Q1–Q20. Do not skip questions.
 Q1 — Python aliasing
 What is the exact output?
 a = [[1], [2]]
 b = a[:]
 b[0].append(3)
 b[1] = [9]
 print(a)
 print(b)
 Q2 — Python closures
 What is the exact output? How would you change only the lambda expression to capture each iteration’s value?
 funcs = []
 for i in range(3):
 funcs.append(lambda: i)
 print([f() for f in funcs])
 Q3 — JavaScript event loop
 In a standard JavaScript event loop, what is the exact logging order?
 console.log("A");
 setTimeout(() => console.log("B"), 0);
 Promise.resolve().then(() => console.log("C"));
 queueMicrotask(() => console.log("D"));
 console.log("E");
 Q4 — Exception handling
 What is the exact output, and why?
 def f():
 try:
 return 10
 finally:
 return 20
 
print(f())
 Q5 — Complexity analysis
 Determine the tight asymptotic time complexity and auxiliary space complexity, for n >= 2.
 for i in range(1, n + 1):
 j = 1
 while j <= i:
 j *= 2
 Q6 — SQL and NULL
 A table grades(score) contains four rows: NULL, 40, 50, 70.
 What are the three returned values, in order?
 SELECT
 COUNT(*),
 COUNT(score),
 SUM(CASE WHEN score >= 50 THEN 1 ELSE 0 END)
 FROM grades;
 Q7 — Python iterators
 What is the exact output? Modify the function so it returns the positive elements and the complete original sequence, even when xs is an iterator.
 def inspect(xs):
 positives = [x for x in xs if x > 0]
 return positives, list(xs)
 
print(inspect(iter([-1, 2, 3])))
 Q8 — Binary search debugging
 The function should return the first index where a sorted array has an element >= x, or len(a) if none exists. Explain the bug and provide a corrected implementation.
 def first_ge(a, x):
 lo, hi = 0, len(a) - 1
 while lo < hi:
 mid = (lo + hi) // 2
 if a[mid] < x:
 lo = mid + 1
 else:
 hi = mid
 return lo
 Required cases:
 first_ge([1, 3, 3, 5], 3) == 1
 first_ge([1, 3, 5], 9) == 3
 first_ge([], 4) == 0
 Q9 — Mutation during iteration
 What is the exact output? Then show how to remove every occurrence of 2 while preserving the identity of the original list.
 a = [1, 2, 2, 3]
 for x in a:
 if x == 2:
 a.remove(x)
 print(a)
 Q10 — Merge algorithm defect
 What does this code output for the given input? Identify the bug and provide a correction with O(len(a) + len(b)) time complexity.
 def merge_sorted(a, b):
 i = j = 0
 out = []
 while i < len(a) and j < len(b):
 if a[i] <= b[j]:
 out.append(a[i])
 i += 1
 else:
 out.append(b[j])
 j += 1
 return out
 
print(merge_sorted([1, 4], [2, 3, 5]))
 Q11 — Stack algorithm
 Implement valid_brackets(s: str) -> bool in Python. Recognize (), [], and {}; ignore non-bracket characters. All brackets must be correctly nested and matched. Use O(n) time.
 assert valid_brackets("a{b(c)[d]}") is True
 assert valid_brackets("([)]") is False
 assert valid_brackets("]") is False
 assert valid_brackets("") is True
 Q12 — Interval merging
 Implement merge_intervals(intervals) in Python. Each interval is a closed integer interval (start, end) with start <= end. Input may be unsorted. Overlapping intervals, including those sharing an endpoint, must merge. Return sorted merged intervals as tuples.
 Example input:
 [(5, 7), (1, 3), (3, 4), (8, 8), (7, 9)]
 Give the result and an O(n log n) implementation. Empty input returns [].
 Q13 — Directed graph topological sort
 Implement topo_or_none(n, edges) in Python. Vertices are 0 through n-1. Each edge (u, v) means u must precede v. Return any valid topological ordering if the graph is acyclic. Return None if the graph contains a directed cycle. Include disconnected vertices. Target complexity O(V + E).
 Q14 — Weighted shortest path
 Given a directed graph with edges:
 S -> A (2)
 S -> B (5)
 A -> B (1)
 A -> T (7)
 B -> T (2)
 Find the minimum cost and actual path from S to T. Explain whether ordinary unweighted BFS always gives the correct minimum-weight path.
 Q15 — Dynamic programming
 Implement min_coins(coins, amount) in Python. coins is a list of positive integer denominations, reusable any number of times. Return the minimum number of coins needed to make amount, or -1 if impossible. amount is nonnegative. Do not use a greedy-only algorithm.
 assert min_coins([1, 3, 4], 6) == 2
 assert min_coins([2], 3) == -1
 assert min_coins([1], 0) == 0
 Provide time and space complexity.
 Q16 — Sliding window
 Implement longest_unique(s: str) -> int: length of the longest substring with no repeated characters. Use O(n) expected time.
 assert longest_unique("abba") == 2
 assert longest_unique("pwwkew") == 3
 assert longest_unique("") == 0
 Q17 — Prefix sums and hashing
 Implement count_subarrays(nums, k) in Python. Count every contiguous subarray whose elements sum to exactly k. Input may contain negative integers and zeros. Target O(n) expected time.
 assert count_subarrays([1, -1, 1], 1) == 3
 assert count_subarrays([3, -1, 1, 2, -2, 2], 3) == 5
 Q18 — SQL outer join
 Tables:
 users(id PRIMARY KEY)
 orders(id PRIMARY KEY, user_id, amount)
 Write SQL returning one row per user with:
 ● id
 ● big_orders: number of that user’s orders with amount > 100
 Include users with zero qualifying orders. Sort by users.id ascending. Explain why filtering o.amount > 100 in a WHERE clause after a LEFT JOIN can give incorrect results.
 Q19 — Concurrent read/modify/write
 A shared counter starts at 0. Two threads each execute these abstract operations exactly once:
 temp = counter
 temp = temp + 1
 counter = temp
 Assume each individual read or write is atomic, operations from different threads may interleave, and execution is sequentially consistent.
 What final counter values are possible? Give an interleaving demonstrating a lost update. Describe a correct synchronization solution.
 Q20 — LRU cache design
 Design an LRU cache supporting:
 ● get(key) -> value, or -1 if absent
 ● put(key, value)
 ● fixed nonnegative capacity, including capacity 0
 Both operations must take O(1) expected time. Specify:
 1. Data structures used.
 2. How get updates recency.
 3. How put handles a new key.
 4. How put handles an existing key.
 5. How eviction works.
 6. What happens when capacity is zero.
 No full implementation required.

## C273 — TheRealCranedisk
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwx0n0cscki/

I mean I do sometimes to emphasize something to drill something into someone's head

## C274 — boosnie
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxaxvib3jxd/

Silly assumption. I use Bold and Italic all the time.
 If the editor supports ways to emphasize and make your message simpler to read and understand why not use it?

## C275 — jtgyk
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxhsfome2le/

Qwen 4 will be out soon. I imagine it has more recent training data, not sure about Drupal 11 obviously, but you might want to give it a shot when it's out.

## C276 — colonelx_
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2cjsbmnc2/

Hey, can you suggest the best coding model for my hardware? I’ve got 10GB Vram and 64GB of RAM. I’ve tried Qwen models with Opencode, but none of them seem to work well. They take forever to think and reason through agentic tasks. I’ve also tried loading the models in LM Studio with different context sizes ranging from 8K to 200K, even with the Qwen 4B and 9B models.
 Is there any hope for running a decent coding agent on a low end PC? 🥲

## C277 — FudgeEducational2038
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2p5whu2sg/

Actually you can run flash next with strata 
 
3.8 flash next is really good, all of the 3.5 models are really old and I wouldn't bother with them. They aren't very good. 
 
3.8 flash next can run at around 40 or 50 tokens a second on a 10 GB card and 64 GB of vram, especially on Windows it's basically just a GUI interface click next next setup and then automatically tune and off you are!

## C278 — colonelx_
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxfsj7j265f/

Hey again, Since the Strata Windows app is just for chatting, should I use Strata through the terminal for agentic tasks and connect its API to OpenCode? Which approach would you recommend?

## C279 — FudgeEducational2038
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2rvr6n1r6/

[https://github.com/Niko1221/Strata/releases/tag/v0.2.8] https://github.com/Niko1221/Strata/releases/tag/v0.2.8
 
The funny thing is, you can download the windows version of this and it will automatically download configure the model get everything working for you and you'll have a full-blown 180 billion parameter model running at 40 tokens a second at 262k context ;) yes even on your hardware, forget the 4 billion and 9 billion parameter, the 180 billion is what you want. But you need SSD for sure.

## C280 — colonelx_
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3lk939up1/

OMG!! After reading all your comments, I feel like trying it out right now! That’s some solid info. Thanks so much! 🙌 and yes I have a decent ssd.

## C281 — roiki11
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6qyzgxsip/

Strata needs 12gb of vram though?

## C282 — FudgeEducational2038
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxafc9w9in5/

Exactly

## C283 — colonelx_
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxd3mqo0eqo/

I have 10gb vram, is it enough?

## C284 — roiki11
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxhh6qkhaci/

I don't know, docs say 12 minimum.

## C285 — FudgeEducational2038
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2tv4x6js0/

If you need something even smaller, strata actually has a couple models to choose from, I recommend the GYRO S model even if it probably suggests the medium or large. 
 
But if that's too heavy for you and you need something a little lighter weight that's a little bit faster, the drop-down also has an option for the ISTA coder model which is basically just flash next with half of its brain removed, the half that is the least used during coding tasks.

## C286 — matrixino
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx34ejp7kwy/

no, forget it. you need money if you want to go local. save a budget of 4-6k€ for a decent box.

## C287 — Material-Database-24
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2udz5d1nm/

27B will code fine with q4 kv. I used it quite a lot with zero problems.

## C288 — colonelx_
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3mmrsel5w/

Could you share your hardware specs? Also, which coding agent are you using?

## C289 — Material-Database-24
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx4buwqgf4y/

StrixHalo and llama.cpp, both Vulkan and ROCm.
 
I mainly run vscode and its builtin agent, which frankly has gotten really good as long as you do not want to use a swarm.
 
I used q4 first with Q4_K_XL as it was just recommended by some and I had 0 issues with that and medium thinking. I now run MXFP4 quant with f16 as I get more speed with llama.cpp+ROCm and its even higher in quality. Takes about 10gb more memory, but it's not an issue with StrixHalo.

## C290 — DisastrousProfit5204
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxfot7lnelf/

and increase the context for comples projects, like 256/512k it handles it.

## C291 — nfored
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlls45pxgl/

I got it to work at 200k context in q4 with a R9700

## C292 — Hofi2010
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnge4v0bs4/

27B on Q8 is pretty good and with a good context size you need about 48GB max. If you want to run it on floating point then you need a lot more of course. But it completes easy to medium complex tasks ok. Of course no comparison against a sonnet 5.5 which is much superior but also a lot more expensive

## C293 — Annual_Award1260
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwok76gf7aa/

I use qwen 27b for some web browser automation and testing. For coding I’m running glm 5.3 (full) with 1 mil context. Maybe try deekseek flash or glm flash?

## C294 — cmndr_spanky
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwonckfzpgj/

What harness have you tried ? Why be vague about it. First, you can’t use Claude code with local models, way too much bloat. Start with open code. Second, qwen can be very sensitive to which inference settings you’re using, third, do you know which quantization of the model you’re using ? Less than q4 is a bad idea. Also, are you absolutely sure you know what its context window is set to and how much it can effectively use?
 
Finally, are you just using it in the same code base you were using with Claude and by any chance do you have dozens of Claude.md / agent.md files and 10+ skills ? That will basically instantly wreck what limited context window you have and pretty much guarantee the model will get “lost” trying to do basic tasks

## C295 — Iamisseibelial
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwondcvu36q/

Use the local model in Claude code and see how the results are. That's been my experience that and Hermes work really well at specific tasks.

## C296 — CordusPorf
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwonfy5aly8/

4060ti 16gb ram, 128gb sys ram, it does well for me as a worker/subagent if my orchestrator makes sure to properly scope it's tasks.

## C297 — Happy_Brilliant7827
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwonj3vf6p0/

Look up Atlas and other coding platforms on github.

## C298 — ismaelgokufox
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwooah6maw4/

I use this on a similar machine (not the GPU though) and I have a good experience with this on Qwen3.8 27B creating things for myself/family and diagnosing issues. Just today did a Stream Deck custom plugin for OpenDeck to see the PP and TG progress of llama-swap proxied llama-server processes. Note this runs on Fedora 44:
  
5600X
 
RX 6800 16G
 
32GB DDR4
  
350PP/32TG
 
Edit: Using these releases of llama.cpp  [https://github.com/unslothai/llama.cpp/releases] https://github.com/unslothai/llama.cpp/releases
 
yaml Qwen3.8-27B: sendLoadingState: true filters: stripParams: "temperature, top_p, top_k, min_p, presence_penalty, repetition_penalty, reasoning_effort" cmd: | ${llama-cpp-rocm} -m /fast/ai/huggingface/hub/models--ukisai--Swift-1.5-Qwen3.8-27B-GSQ-RCO-GGUF/snapshots/d74895bbe5db4bec1e0024e7cc87d59c02d7631a/Swift-1.5-Qwen3.8-27B-GSQ-RCO-IQ3_XXS-mtp.gguf --mmproj /fast/ai/huggingface/hub/models--ISTA-DASLab--Qwen3.8-27B-GSQ-RCO-GGUF/snapshots/d562806dbafae37109975e970aae91b43e73b440/mmproj-Qwen3.8-27B-BF16.gguf --no-mmproj-offload --flash-attn on --no-context-shift -fitc 64000 -ctk q8_0 -ctv q8_0 -ngl -1 --fit on --reasoning on --reasoning-preserve --reasoning-effort medium --load-mode none --spec-type draft-mtp --temperature 1.0 --top-p 0.95 --top-k 20 --min-p 0.0 --presence-penalty 0 --repeat-penalty 1.0 -fitt 2048

## C299 — Original-Mistake8624
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3fodrkioz/

Have you compared the accuracy and task completion rate of this Swift 1.5 IQ3_XXS setup against the original Qwen 27B at Q4 or higher, using the same coding tasks?

## C300 — WCWRingMatSound
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwoqlig3vl1/

I’m feeling the same pressure. I have a 64GB MBP M5 Pro. I know it isn’t the best for local AI, but sheeesh it took Qwen 51 minutes to do a git add, git commit, and git push to origin. That’s it.

## C301 — BarWhole6344
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwoqxv4a5k5/

ur not gonna get a great coding experience with qwen 27b. go buy some tokens on openrouter. if you want extremely fast intelligence, go buy tokens on or baseten / modal / fireworks / together ai.
 
DS V4.1 Flash 1017 Fast on baseten cooks around 1-2k tok/s. Once you try it you can’t go back.

## C302 — Schudz
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwot2r7ie1t/

i use unsloth, ive used the base qwen 3.8 27b for months, and now im using a spin off uncensored and distilled from fable, with is like 5% better, but even the base nodel is good enough. i tried qwen flash next, which is close to older versions of deepseek, but came back to the 3.8 27b, its just always reliable, even if not that fast. i run it on a rtx 6000 pro, q8 with kv q8. i get around 120t/s with 131k context (my custom harnes handles compaction pretty well so that context works fine for me)
 
i also tryed running it on my dev machine, a 32gb RAM with 9070xt, i can run a q3 with 70k context at around 45 t/s, with kv at q4. with pretty good results altough i need models to run at least at 100t/s on my current workflow.
 
i also use opencode go basically for deepseek 4.1 flash when i need to do work on multiple project at the same time, and i have access to claude and opus 5.5 which i use for very complex things, like bootstraping complex solutions like my custom harnes, but then qwen assume the project and work on new features perfectly fine.
 
i just love qwen and i think the qwen 4 27b might be close to an endgame model when it releases this monday.

## C303 — jellyrole
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwoxu38s7tx/

Why only q8 with a pro 6000?

## C304 — Humble_Ad_1875
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpzl823tlu/

Just got advice from claude: 
 
Qwen3-Coder 30B (MoE): only 3.3B of its parameters are active at a time, it’s 19 GB at Q4, and it has a 256K context window. That’s slightly more than your VRAM, but because so few parameters are active, Ollama can put the overflow in system RAM and it still runs at decent speed.
 
Rig specs:
  
AMD Ryzen 9 9900X3D (4.4GHz) Processor
 
64GB DDR5-6000 RAM
 
NVIDIA GeForce RTX 5080 Graphics Card
  
Is it going to run?

## C305 — sudden_aggression
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwqrx7bqmcj/

AIs will just give you whatever was in their training data six months ago. qwen3-coder 30B hasn't been a state of the art local model since what, last year?
 
with your setup (5080 has 16gb right?) I would advise either a highly quantized qwen 3.8 flash next or a q4 quant of 3.6 35A3B.

## C306 — alexander123454
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwozdfus9t1/

You have to use a harness and preferably a metaharness (i still use a lot of GSD)
 
Im about to ship some metaharness capabilities for my open source harness if you wanna try it out 0.26.0. I could use the user feedback on different tasks.
 
 [https://github.com/ahwurm/localharness] https://github.com/ahwurm/localharness

## C307 — Bunksha
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwp02lkgvc4/

What quant are you using? 24GB VRAM & DDR4 32Gb isnt really that much. Q4 is ~17gb of memory and 128k context is, what, 9gb? That puts you over the 24gb which means its gonna spill over & be slow. I run the same model at Q8 with 256k tokens and its been amazing at coding.

## C308 — FollowKryst
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwp43fr0jok/

I’m no expert, but I used this model in Pi harness via llama.cpp… I didnt like the experience in LM Studio and using any model in Hermes vs pi, for me, is noticeable.
 
I have a 64gb M1 Max MacBook Pro, and you running that dense model with that context size with less processing than me draws concerns in and of itself.
 
You should probably share the harness you’re using, the quant of the model, and what you’re trying to do.. also, I notice running these models in terminal always gives better results.
 
I mainly use Q4_K_M Qwen 3.6 35B via llama.cpp in terminal and I get lots of great things done with ease. Even when I did use the Qwen 3.8 27b, I got good results though slow and takes up majority of my ram.
 
Idk the comparison of Nvidia vs Apple silicon chips, so you might want to compare you and our systems before you try any I mentioned.

## C309 — 808phone
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwp6banwgir/

Try open code or pi. You didn’t tell us what kind of code base you have. The model does work and can produce pretty decent code which will be spot checked at the end by a better model. But it does follow instructions and write code surprisingly well. I use LM studio and Pi or Open Code and even Kilo Code.

## C310 — Captain--Cornflake
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwp9jbm3zxh/

Any ambiguity in prompts that moe llms usually infer correct meaning tends to trigger more thinking and looping. To keep it from overthinking loops have the agent look at the main thinking words such as , hmmm, but, etc. etc. if they are repeated more than say 3 times , let it use its original code, which tends to be correct most of the time anyway. Write your own harnes / agent, claude can help if you cant do it, its lite and can work a lot better if you dont have tons of tools., the public agents you can use bring tons of bloat .

## C311 — altdotboy
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpcnjaef8k/

My 2 cents. I run the 3.8 27B model and 3.8 Flash next. I’m using 128GB M5. I run the 27B at bf16 and FN at Q4. 
 
The 27B, I did a lot of testing with this model vs a lot of others running locally. Deepseek v4, GLM 5.3, Nemotron and QFN. Qwen 3.8 27B in bf16 is the king of local. I ran tests at Q4 and Q8, these would not pass my demanding reasoning tests, so I dropped them. Also going to Q8 resulted in much longer thinking. 50% more than at bf16.
 I see a lot of people on Reddit complain that the model overthinks. I believe this is a result of quantization. I don’t see this at bf16. 
 
If you have the ability to get another system that fits the full model, try that. I know it’s not cheap.
 If you want to do simple tasks or creative writing use a quant. If you need the output to be impeccable and precise get the full model. 
 
One other thought is to run the model through qwen code. Ask codex or Claude to set that up. 
 
Just my thoughts, hope it helps.

## C312 — lazyfai
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpe6psnesg/

I and my team use it daily. 2 Machines, one for coding and one for chat / others.
 
vLLM (Qwen 3.8 27B FP8) on dual L20, Strata (for swift 1.5) on single 5090D
 Coding agent used / tested and good: Pi, Prime agent, OpenCode Codex (quick and actually worked)
 Not so suitable: Deepseek Harness, Claude Code (they both suffer from over thinking sometimes)
 
PS. Harness is IMPORTANT, I think in most case the problem is around the harness not the model itself.

## C313 — No-Consideration5347
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpoo6es49v/

Try Strata; it's the easiest to set up. llama.cpp is more stable, but slower than Strata.
 
Use a reasonably good quantized model (IQ3_S/XS for Qwen Next with Strata, and Q4 for Qwen 3.8 with llama.cpp). Keep in mind that higher quantization levels generally require more resources and can result in slower inference.

## C314 — Snoo_81913
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpwjyh950h/

It's probably config reasoning seems touchy with this model it can easily loop unless you have it set right. Best thing to do is start giving it test prompts and adjust the config until you get the right results. I just have a series of tests prompts and have Claude run it with polling and test one config flag at a time save the data pick the best then start on combinations. Different cards are give different results so it's good to test everything. You should have plenty of resources on Reddit though that's a popular card for inference and Qwen3.8 27b is one of the most popular models.

## C315 — word_executable
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpx40tn2qq/

I mean sonnet 5.5 is leaps ahead of qwen 27B. Local ai and open source is great but is overhyped how good it is

## C316 — ContraryConman
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwqbh2xzkbo/

Anything in the Claude 5.5 model family will be better than a Qwen3.8 27B quant. They are all distills from an internal teacher model that is like 2 generations ahead of Qwen3.8's teacher model

## C317 — Vassallo97
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwq5cxsn25e/

I find that Qwen performs pretty good inside the deepseek harness, I also made my own coding assistant built for Qwen, designed it around the way Qwen models call tools and I find that works well for shorter coding tasks but deepseek harness is still my go to harness for qwen3.8

## C318 — MoneroApe
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwq7j32s5ut/

Looking at your config, you May succeed using strata coder or hyperqwen repo (fines tuned for 3090) you Will get much better experience. You are using lousy quants and bad caché. Just download hyperqwen repo, run it on Linux. 
 
Then try strata coder (only coding).

## C319 — No-Recover109
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwqgpkh5rc3/

I used to use qwen3.8 27B FP8 for coding and it did pretty well. I used vllm which actually is too heavy for coding. Now I use Strata and Deepseek v4.1 1017 q3 istalabs version. Seems to be working also. I think you cant run qwen3.8 with that GPU and context amount in any proper quantization? I guess you are running it q4 and that might be too little. Try different engines and make sure you actually set the context same in the inference engine and in the coding agent

## C320 — Key_River_9288
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwqoyl897l0/

More ram, use strata 3.8 flash next at quant 5 is the beez neeZ

## C321 — Tight_Ad_5220
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwqrwpbpyn8/

The problem is your prefill is too large. In Claude do /context and see how big is ur pre fill. Take everything out and watch how well it works.

## C322 — nincius
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwqtkorfvz9/

Try get some tuning tips from  [https://github.com/noonghunna/club-3090] https://github.com/noonghunna/club-3090 
 
I have same specs as you and got better results after turn reasoning off completely.

## C323 — Dediadeis
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwqvy3np5ep/

I use both 27b and QFN in what might be considered a legacy codebase and the important thing is to configure the model for smarts first, then speed second. You really wont squeeze much out of the hardware you have and a dense 27b model can feel sluggish. With that said, the hardware is tight, and you are using Ollama so it would be my guess some of your or some automatic right-sizing was done for you that has made the model retarded.
  
Config issue, many people have used it for coding

 
Yes and no, depends on expectations. A preferable amount of VRAM/RAM though will be 64/64, you can get away with less but this is where the tradeoffs can be made wrong

 
Model Q8, KV no lower than 8 but preferably FP, 262k context.

 
Get more system RAM and try QFN, for this Q4, KV8_4

 
I use Cline inside sandboxed code-server container. Experience is great when you dont cut too many corners. What I would actually suggest, as you seem reasonably familiar enough with harnesses and agentic coding is to put one of your cloud models on the case and see if it can setup and bench and tune. Also things get much better with tooling and properly configured environment but perfectly capable in a practical blank slate so these are certainly capable of complex several hour tasks when configured and given the right setup

## C324 — isademigod
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwr4si9r06c/

I use it for simple scripts all the time. I am not a software developer, just a datahoarder and sysadmin. It's perfectly cromulent for regex and powershell scripts. The context window is awfully small to make a whole program

## C325 — ParticularlyStrange
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwr6gc375ib/

What quant are you running? Use the EXL3 or NVFP4 quants.

## C326 — exzw
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwr94ofgnmt/

You bought wrong hardware simply. Got a PC with at least 128GB ram DDR5 + at least 1x R9700 or RTX pro 4500. Then you try either 27B Q6 at least or Strata QFN Q4 at least. You will feel the difference. Sometimes I feel QFN even out perform opus 5. I use QFN as coder and Opus as Auditor.

## C327 — Sea_Advance273
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwrhl8ia200/

Have you tried using Qwen in the Claude Code harness? It performs a lot better. Still need to iterate a lot more and be more involved than opus-5.5 of course, but I've been decently impressed with even Q4 running in 24GB VRAM.

## C328 — Promotional_Pickle
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwri0l42dut/

I get excellent results with that model running locally. Pay special attention to your infrastructure. Harness, notes, etc. Those separate a fun toy from a useful tool.

## C329 — dahc_
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwrljnbmkyr/

I have almost the same setup (5600x + rtX 3090) Tried that same model setup on pi, Claude and Hermes but didn't get good results either. Then I tested Qwen 3.6 35B A3B in IQ4-XS + OpenCode and it's a complete different story: it refactors files very well, fixes bugs, implements new features and so on like a proper coding agent. Right now I'm still getting the setup ready (better context window and memory system) but I'm very happy with the results.

## C330 — Current_Ad5753
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwrt267zvs1/

Hey could you please update if you using any harness over your local llm.

## C331 — endockhq
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rws0t23mqhx/

Use vLLM
 
Use Qwen3.8-Flash-Next-FP8, the 27b model is mega slow.
 
You bought into the hype, if you are a "Software House", you need a better model for proper software.
 
You need to use "claude code" with your local inference. Just make sure the engine supports "Anthropic Messages API".

## C332 — Remote-Pineapple-541
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rws2z26hg9v/

You say you’re a software development house, but can’t follow online development documentation and do basic troubleshooting? That’s troubling.

## C333 — ContraryConman
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwsal0il483/

I use the Pi agent for programming tasks. A goal mode plugin is the only way I can actually get Qwen 27B (128K context window) to actually stay on task, because the harness itself will keep track of the current goal even after its filled the context window with its own thinking and its forced to compact. And even then, it's not like using Claude or whatever. You can't really "vibe code" with it because it's too slow, and you can't really do multi agent parallel whatevers because it will melt your card. 
 
It's more like, if there is a tedious programming task that I don't want to do myself, I can give it to my assistant and come back later in the day or tomorrow morning and have it completed. And then I can use that time to write other code or do something else. 
 
Sonnet 5.5 on medium in Claude Code is absolutely the wrong comparison here. Such a task I've used my local Qwen for was to set up a complicated CMake project in the background while I did other research for the same project in parallel. I get like 25 tps on my setup and took over an hour in goal mode with some need to keep it away from dead end ideas. At work Claude would have this done in 2 minutes, 5 minutes tops with higher thinking

## C334 — MonadicKierkegaard
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwsavw1x5et/

is that setup per dev or for a team?
 
you can eke out maybe one coding agent, barely.
 
its ok for one shot toy apps/games. but real agentic workflow, 32GB is not enough.
 
maybe use cloud providers for generating an extremely detailed spec, with pseudocode. Then instead load an MoE that fits well on a 32GB - this can go as high as 2k tps PP, 70 tps GG. that speed is more than workable at the expense of intelligence (hence you need to guide it)

## C335 — Osi32
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwsbtb19qci/

Any skills you’re using are essentially a pre-prompt. They will go to the model before you say anything. If you’re using a 128k context window, you’ll be unlikely to have much left for the actual task at hand.
 While having a 3090 is good for a single dev with a small set of tasks, not much good for multi-user and not for long chain of thought tasks.
 
The people in the thread running qwen3.8-flash-next are likely using strata to offload big parts of the model to main memory and disk. You really can’t do that with a dense model like qwen 27B.
 
My advice is really simple- use Qwen3.6-35B-A3B. It is fast, it’s a coding model. Use 27B for planning work.

## C336 — 247nuts
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwsyut1nan9/

Qwen 27b for instruction and qwen coder for coding

## C337 — jikilan_
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwu5nheaxlw/

OP better get at least 2 3090s , best is 4 for 27B with vllm before landed with that conclusion. It is not a replacement for cloud but a junior entry developer with 20 years working experience. 😎

## C338 — Demonicated
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwu99aiudnp/

First of all, for qwen 27B you have to have to have to use at least q8 and really you gotta use bf16. Using 4bit quant and saying its not good enough is like...... well duh.
 
Also Qwen 27B isnt a white glove model. You have to know what you want and tell it exactly what to do, and it will do it pretty well.
 
Always use a planning phase for all work. Tell it to create implementation documents that will be given to a junior developer to complete. Then hand it back that document. Qwens an overthinker, it will take a while, but it will get the job done.

## C339 — xsilas43
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwub6ix1291/

Give qwen agentworld a shot, i found it produced much simple more effective code in 1 shot much faster than 3.8 27b did. although 3.8's was nicer visually and it did eventually get there.
 
I'd also give unsloth desktop a shot over Ollama, its much more customizable, and a better harness to begin with, a good harness alone will solve a lot of issues. Nice part about it is you can always keep the optimizations and run it headless with another harness as well.
 
I would also recommend using the sharp chat templates for either.

## C340 — ImpossibleNumber7345
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwudho2cyar/

Get Swift. Its a model that is that same Qwen but fine tuned by punishing it for over thinking. Its amazing and just as smart and gets work done

## C341 — c4chokes
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwuf5yhvsf7/

Use the sonnet to debug your setup 🤷‍♂️

## C342 — thebemusedmuse
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwuvcygqftv/

Really hard to know what you’re doing wrong. Qwen is my primary coding agent. I’m doing 6m output tokens a day on it.
 
It’s not flawless and my harness has checks and balances to fix the bugs it introduces.
 
If you give it too much work it may not do it all. So you have to right size the work you send it.

## C343 — TheRiddler79
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwvcvxsdbc4/

Have Claude give it instructions, turn on thinking, have Claude check the output.

## C344 — dethstrobe
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwvd6k4tspt/

[https://www.reddit.com/r/LocalLLM/comments/1xaxd6j/running_local_models_for_agents_a_mac_mini_vs_a/] My also have had similar results.

## C345 — jabies
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwvw3d0t09t/

no mention of chat vs completions API, prompt template, quantization, temperature, or sampler settings. Start by figuring those out.

## C346 — mrepop
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwvyierx50g/

It’s a config issue, that version of qwen isn’t intended to be run with thinking on xhigh, try changing it to low, or turning it off altogether, it’ll be night and day.
 
There’s additional changes you can make to penalize token reuse which will cut down on the repetition, but not completely eliminate it if you absolutely need to run in xhigh for some reason.
 
 [https://huggingface.co/Qwen/Qwen3.8-27B/discussions/178] https://huggingface.co/Qwen/Qwen3.8-27B/discussions/178
 
 [https://www.reddit.com/r/LocalLLaMA/comments/1vtq8hc/qwen_38_27b_medium_is_insane_120th_the_thinking/] https://www.reddit.com/r/LocalLLaMA/comments/1vtq8hc/qwen_38_27b_medium_is_insane_120th_the_thinking/
 
I’m using qwen 3.8 27b in a number of places on various hardware platforms and everyone runs into this issue. Its not just you and your expectations aren’t unrealistic at all.
 
I will say your hardware is honestly at the bare minimum for getting a useful instance running. You’ll be able to load the model, but with larger contexts it won’t have much room at all. You might consider the flash variant so you can offload if you’re stuck with that hardware.

## C347 — Past_Ad6251
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rww5ghf7usi/

As a so called software house but using ollama, I have to say your team has room to step up. I'm OPC with 24G VRAM and 64GB RAM, Qwen3.8-27B+llama.cpp, 200k ctx with mm support, actually can complete +85% of my tasks including medium complexity coding tasks. I only use paid tokens for complex tasks or time consuming ones. Regarding harness, I'm using DeepSeek Harness and Hermes Agents.

## C348 — fobsthedev
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rww81p6k3vm/

Use swift 1.5 and avoid any quant lower than 8

## C349 — lordpuddingcup
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwwrva3bhyd/

Context window 256k is minimum
 to be useful for coding and that’s pushing it honestly
 
Also quants matter and reasoning matter to really get decent anything you need max reasoning on local models which ways context too

## C350 — Sad_Olive3034
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwwslb38bdv/

Its a total pita. I have an intel arc pro b60 for my coding AI. I am SLOOOOOOWLY getting him to work. But im using Claude and GPT to work together to help him out. the new AIs are great at basic. but you need to literally treat and train them like a child/teen/adult.

## C351 — MatthewBochsler
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwx3bzdmnqb/

yeah i havent had too much luck with qwen models either. So far the only thing im testing before i try something else is a heavily controlled harness with them, and all the other specifics you need to know from the github community on using them. query github for qwen harness and control tips.

## C352 — ulysses_size
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwxcykx6aaq/

I was in your shoes 3 years ago. Don't fret just yet. PM me.

## C353 — Turbulent_Office1340
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwxrl8rguqq/

The rest of the comment are just people who have no idea..

## C354 — bazuchan
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwxslkgb7hh/

Most of things already suggested, but still: 1. Agent - use claude code or pi. 2. Instructions - give model something task can be tested on. 3. There is Swift version of 27b, try it, it should reason less. But still for dense model you need to run it Q8 (Q6 might work too, but difference is visible). Same for KV keys, Q8 at least. This will lead to getting second 3090.

## C355 — 0xnobot
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwy3v1toq01/

Usa llama.cpp y la configuración del perfil del LLM, y un buen harness

## C356 — thilog
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwzkug6ftt0/

Which harness do you recommend?

## C357 — mattjouff
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwy7vusj6ar/

This thread is rediscovering the terrible economics of AI from the ground up:
 
“We are trying to run the models locally (presumably for cost and privacy) but our 27B open weight model doesn’t perform as well as the 2000B flagship model, what are we missing?”
 
By the time you get a model that can actually do the work you’re back to renting GPU by the hour lmao

## C358 — Frosty-Bid-8735
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwyd8p5tuw1/

I would not use Qwen 3.8 for coding. Use it for classification, summarizing text, a rag with limited context window.

## C359 — maxido
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwymu7uybvn/

We deploy qwen3.8 27b for the company and it works pretty well. Sounds like a configuration issue

## C360 — Sufficient-Rock-8482
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwz4wyafl41/

You may run the unsloth's q4 km using vllm.cpp (it is llama, vllm hybrid). Configured properly, it can scale well for agentic use. Also, better to use a small plan like opencode go with this. Make deepseek 4.1 the orchestrator and let qwen implement.

## C361 — bytejuggler
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx02kua8asl/

27B has all these issues. Try running the (larger!) Qwen Flash Next 3.8 125/180B class parameter model using Strata and you'll have something that actually works, doesn't get stuck in loops, prefills 3x-4x faster and processes significantly faster too.

## C362 — Mission-Shopping-615
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx0c5ucv0yt/

You can ask Claude to optimize your set up and ask if the hardware is capable enough

## C363 — dfgxxx
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx0chzybnoh/

Try changing the harness, Claude code is really bad for local llms because it is token inefficient (it's system prompts are huge), try something like deepseek harness

## C364 — dlbogdan
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx0lmssnvdw/

I’ve been using q3.8fn for a while now on a similar hw: 3090 128gb ram 16c/32t cpu
 Never had any looping issues and it works for every coding task I throw at it. Fast too.

## C365 — colonelx_
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2so82h95u/

32core? is that epyc?

## C366 — dlbogdan
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx33ezihz8l/

Sorry. Corrected it. It’s a ryzen 9 5950x 16c/32t

## C367 — ifeelprettyosopretty
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx0nlqelz1f/

Good local ai for even better results on tasks at usable speed is expensive. I run a 20,000 dollar system and im getting about 77toks but im running a qwen flash next 177b (55gb of that is look up) I run the 8 bit model and it's very good at complex tasks. 27b is just too quantized to do much of the long multi turn work without many small errors. Its still a great model just not a solo artist with complex tasks. I use it occasionally but I back it up with codex or claude task refinement.

## C368 — aCuria
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx0uvafuqw1/

Although it’s called local I don’t think you want to run it on your dev machine, run it on a separate machine so you can do stuff in parallel on the dev machine
 
Context window feels small on rtx5090, it’s possible dual 3090 would be better
 
You need an agentic framework to go around it, and accept that the intelligence is only around haiku 5.5 low effort 
 
You really should be using opus 5.5 not Sonett, these models cost the same but opus is smarter

## C369 — Hrmerder
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx0vc95128w/

Could be the way you are hosting it.. I had been using QWEN 3.6 35B A3B for a while using LM-Studio, but coding was absolute garbage. I set it up today in Strata and HOLY HELL It's better.. I can actually vibe code stuff and it not just argue with me about crap I already corrected it on...

## C370 — SeveralCamera292
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx0w4bvfz50/

For work 3090 is not enough for Qwen 27b. You need at least 32GB VRam. You also need to experiment with different model builds most are just broken. Don’t go straight for uncensored straight away. Spend the time to configure your harness. But this is after you add another 3090 in the box. I will also suggest separate inference machine that is dedicated for that. And this is the start you will spen 3-4 weeks at minimum of tuning. What comes out of the box from Anthropic and OpenAI is very well tuned package out of the box (agents, harness, instructions). If you want to go on the dark path you need to spend your time and dedication on it.

## C371 — ifeelprettyosopretty
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx0xelhqjl0/

.... the other issue is using highly detailed claude models work structure for a smaller model to pick up on. My campaign tools for instance for my DnD DM that were created and used by codex required many revisions to work well with my 177b model...

## C372 — VihmaVillu
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1hvljq3dx/

In terms of harness you starts from 0 compared to claude code.
 Also what quantization are you using?
 PS: I'm having a blast with qwen3.8-flash-next-iq3_s via strata

## C373 — sod0
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1n8ypr9no/

You need more context! Try to optimize the runtime for more context. My 3090 csn serve 245k context with no issues. Or 200k in "batch" mode when optimized for concurrency. Look into HyperQwen.
 The model is replacing my personal Claude with no issues. Just remember it NEEDs a plan and research phase and a qa-phase after the job. One-Shooting like Claude will give you bad results.

## C374 — never_supernova
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1ojyyyuua/

As many folks will say, use the frontier models such as Claude to do the high-level architecture design, then get it to break implementation down into phases. Then get it to break down each phase into smaller implementation steps that Qwen can handle. Then get the frontier model to review Qwen's code. Most of the time, it works great for me. Just don't expect frontier level speed: Qwen might take 30 mins to do what Claude does in 5. Use ADR and implementation planning docs in combination with AGENTS.md to maintain context and direction. Good luck.

## C375 — sub-dy
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1olncrhr9/

You are doing it wrong. You expect a model that's 40 times smaller to have the same smarts as a huge commercial model with 10 times the context size.
 
A 27B model, even at Q3 quantization, is absolutely capable of writing code. But you have to be realistic about how much it can do.
 
If your model is only capable of small coding tasks, you only give it small coding tasks. Simple as. So instead of treating it like a master developer AND software-architect at the same time, use it as a coding assistant that needs guidance. You define the architecture, define the interfaces and break the work down into small clearly defined tasks.
 
Have it implement one thing at a time. Test the result, review the changes, document the outcome only then move on to the next step.
 
One thing is that you should never let mistakes pile up. If something goes wrong, address it immediately. Trying to debug an entire application with 10thousands of lines of accumulated code is a completely different challenge than fixing a mistake in a small, isolated component.
 
The same applies to context. Don't dump the entire project on the model and expect it to figure everything out. Give it the relevant files and enough context to understand the task at hand.
 
tldr: While you save on expenses paying a Claude subscriptions, you need to do more of the thinking and planning yourself.

## C376 — Sea_Shift4327
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1xrpwqt9g/

What exact quant are you using, and did you also quant the KV cache?

## C377 — MediumAd4983
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx21synp679/

It's totally capable. Yes, it's not so smart as Claude or ChatGPT (obviously, it's literally 100x smaller). But it definitely can code, fix it's own bugs and use your instructions.
 
 [https://github.com/morgan55555/EasyMoney] https://github.com/morgan55555/EasyMoney
 
This entire project is a test of that exact model with that exact context size. Even without enabled vision capability, so it can't see, only text, only hardcore. Llama.cpp + OpenCode as harness + surf.cli to control the browser.
 
I mean, it made ENTIRELY by this model, for real. It was a torture test for Qwen, and it's definitely passed. I'm amazed, it was just an experiment, I didn't expect that quality for this model size.
 
Downsides - mostly in a very low development speed. While Claude can make app like this by 2-3 hours, local setup with Qwen will take 2-3 days. It heavy relying on "reasoning effort", which take much time to "thinking", and with speed ~50-60 tok/s it can take time. Also it will take another bunch of time on a hard tasks with cycles "make-test-fix-repeat".
 
Also it will make code, design and any other things with medium quality at the best. It will not overcome Claude. But it's small and it's free.
 
So, use it or not - your choice.

## C378 — goingsplit
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3guvrvjc1/

would you be so kind to include in that project also the prompts used for having QWEN create it?

## C379 — MediumAd4983
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3zwssmahx/

Probably, it will be better to upload the entire Qwen setup as a separate project, because it's mainly not about the prompt.
 
Like, first prompt was something like "Make a PLAN.md and AGENTS.md in a current project directory.", and then just a list of requirements, which programming language should be used, which frameworks, and what this project should do, so it's not something magic, it's the same requirements that can be used in Claude or other LLM.
 
Most important thing is context management, you should use as minimum context for your tool as possible, because of the 128K context window. So, throw away Claude Code, get OpenCode (and OpenChamber, if you prefer GUI, it's basically just a better UI for the same OpenCode), disable integrated browser (skill-based Surf-cli is much better), set up automatic compaction settings, use files for a long or difficult tasks. Use every token wisely, it's not a 1M window like in more powerful LLMs.

## C380 — goingsplit
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx44wgu73c4/

thanks for the directons. also please ping if you create that other project, i suppose it would be useful for some (me:)

## C381 — Muted_Anteater1170
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx26ez7i7q8/

i’m betting u something rn, it is model prompting, agents and harness issues. i had the same issue agents fixed most of it for me. my 27b model is out of this world even tho i use flash next more bc i can

## C382 — Tigonimous
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2copl68pv/

What harness you use with qwen?

## C383 — Iajah
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2cyunu010/

You need to run Q8 and 256K context on llama.cpp and I'm pretty sure your hardware can't do that at reasonable speeds. You might be able to run one such agent with 48GB VRAM and 64GB RAM but I would recommend 96GB VRAM and 128GB RAM to run three agents. As for the endless loops problem it is a harness issue. The newly introduced Copilot harness is known to do that with Qwen, use the VS Code Local harness instead.

## C384 — Comfortable-Cry-3261
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2fsxapm77/

A lot of answers, so I will be quick. 
 
Works for me on 3090: - headless Linux - ninfer (200k context, KV q8, +image, mtp3) - claude (but use ninfer endpoint, disable subagents etc.)
 
70-110 t/s response, 1.2-1.7 prefill
 
Perfectly usable as a claude replacement, but 5-10 times slower. Still solves the same tasks. More time for Reddit at work :)

## C385 — Effective-Giraffe655
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2ouo70q03/

Check  [https://www.reddit.com/r/LocalLLM/comments/1xjr28d/qwen_38_27b_really_bad_for_newcomers/] https://www.reddit.com/r/LocalLLM/comments/1xjr28d/qwen_38_27b_really_bad_for_newcomers/ - basically the same question, with some good comments.
 
The problem is with how you approach the model - prompts, domain knowledge, etc. 27b model is small, it doesn't know a lot of stuff, and you need to provide that.
 
See  [https://rakshazi.me/blog/you-dont-need-frontier-llm/#a-smaller-model-is-dumb-and-doesnt-understand-what-i-want] https://rakshazi.me/blog/you-dont-need-frontier-llm/#a-smaller-model-is-dumb-and-doesnt-understand-what-i-want - there is an example of the "spec" skill used to help with explaining what you want to a model. (There are other posts in this blog that mention similar-sized models).
 
27b model is pretty capable, it just knows way less than bigger models. For example, I'm working on red-teaming skill, and the model does a decent job finding most of the security issues (27 of 38, across 4 tiers), and building PoC exploits to prove the findings. Without skill - ~10 of 38, missing harder tiers entirely. So with a proper action framework and supplied domain knowledge as part of the skill, the model works pretty great.

## C386 — humanbutnothuman
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2pvy47zc5/

If you need Claude like working, try using Agentic AI tools such as Bionic or Hermes. They’ll work better for your use case

## C387 — Hot_Half_5263
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2v1w5m2ea/

I switched to 1.5 swift qwen 3.8 27B nfvp4 from qwen 3.8 27B nfvp4 and it started worked 100x better, clear response, reasonable reasoning time

## C388 — AdOrnery5134
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2wn9cww4j/

Try strata with 3.8 flash next. Very good in thinking.

## C389 — Original-Mistake8624
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx31xx7eheq/

Interesting discussion. I’ve been experimenting with a different approach for a fully local AI assistant.
 
Rather than relying on a single powerful machine, I use two dedicated systems:
 
System 1 – Orchestration:
  
Ryzen 7 8745HS, 32GB DDR5, Radeon 780M
 
Handles agent coordination, task planning, persistent SQLite memory, voice interaction and supervision.
  
System 2 – AI inference:
  
Ryzen 9 3900X, 64GB DDR4
 
2 × RTX 3060 12GB (24GB total across both GPUs)
 
Qwen 35B-A3B MoE, Q4_K_M with MTP, running on llama.cpp CUDA
 
34 GPU layers, approximately 37.5 tokens/s in my validated test configuration
 
Both GPUs limited to 130W and around 1850MHz, typically running at 50–57°C.
  
The two machines communicate through a dedicated 2.5GbE Ethernet connection, with measured throughput of approximately 2.35Gbps in both directions.
 
I’ve also experimented with Qwen 27B, but chose the 35B-A3B MoE model as my main configuration based on comparative tests.
 
My approach is to separate planning, execution, verification and persistent learning rather than expecting a single LLM to handle everything perfectly.
 
I believe many issues with local coding models are related not only to model capabilities, but also to orchestration, context management, tool integration and verification.
 
The system is still under development, so I’m not claiming that it already solves every coding reliability issue.
 
My goal isn’t to chase the highest tokens/s. What matters most to me is accuracy, reliability and the ability to complete complex tasks correctly, learn from mistakes and improve over time.
 
Has anyone experimented with a similar distributed architecture or compared Qwen 27B with the 35B-A3B MoE model for agentic coding?

## C390 — xoxoxosevenhorserace
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx36pg8w23o/

Youre just using a badly quantised version of 27B. I found its night and day been who and how the models was quantised

## C391 — xoxoxosevenhorserace
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx398invhr5/

A badly quantised model is particularly perceptible to repetitive thinking loops IME

## C392 — xoxoxosevenhorserace
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3bzk5fu02/

I had a similar experience with ollama, but for mlx. Id be using vllm and a good unsloth quant from hugging face if i was you

## C393 — goingsplit
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3bin5g141/

what's an ok quant?

## C394 — xoxoxosevenhorserace
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3rq8jxbc2/

One of the Unsloth ones on hugging face for gguf or an mlx version from mlx-community or lmstudio-community is what i run on my mac  [https://huggingface.co/lmstudio-community/Qwen3.8-27B-MLX-4bit] https://huggingface.co/lmstudio-community/Qwen3.8-27B-MLX-4bit

## C395 — Unhappy_Relief_9158
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx370lcu2zo/

with right workflow is like sonet 5

## C396 — goingsplit
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3az18w1b5/

what would that be

## C397 — Unhappy_Relief_9158
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3s6mh715x/

You can use opencode, or pi code and add agents and subagents and build workflow agents i can teaching you

## C398 — Upper_Ad_8397
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3iiohdb50/

llama.cpp is the way to go here

## C399 — Embarrassed_Ad3189
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3md16enxf/

I have pretty much same setup, but I use llama.cpp + CUDA 13 drivers; Unsloth Q4_K_M quantization (there might be already some better ones out there)
 
here's my command line (currently on build cuda13-b11146):
 
```
 set MTP=--spec-type draft-mtp --spec-draft-n-max 2 --draft-p-min 0.80
 
set CACHE=--cache-type-k q4_0 --cache-type-v q4_0 --ctx-checkpoints 16
 
set BUILD=cuda13-b11146
 
set MMPROJ=--mmproj models\mmproj-F16-Qwen3.8.gguf --image-min-tokens 1024
 
builds\%BUILD%\llama-server.exe ^
 
--model models\Qwen3.8-27B-Q4_K_M.gguf %MMPROJ% -ngl all --threads 16 -lv 4 -np 1 --top-p 0.95 --min-p 0.00 %MTP% %CACHE% --reasoning-budget 131072 --reasoning-preserve --log-colors off --log-timestamps 2>&1
 
```
 
for me, it's the first open weight model I could fit on my machine that is actually good enough to produce working applications, process data, etc.
 
using Pi coding agent (mostly Pendant in VS Code)
 
just don't compare it to Claude, it's a completely different category and you need to understand it's limitations. start with smaller, contained tasks and you'll eventually see where the boundaries are.
 
I have mostly stopped using Claude for pet projects, Qwen is good enough. But if it's some niche area, like, running DNA tests, etc, I still use Claude; also where speed is important - Qwen can easily take up to 20-30 minutes on some complex tasks, So, I am mostly talking to Qwen on telegram in "fire-and-forget" mode, like, in the gym or something 🙂 getting around 35-45 token/s, if anyone is curious.
 
fortunately Pi is very proactive and persistent, does not give up that easy, auto-compacts etc.. and it can also run tools, for example it can run Firefox in marionette mode, take screenshots, etc.
 
PS: forgot to mention: 3.8 really needs thinking mode; 3.6 was a bit better without it, see for example  [https://blog.jetbrains.com/junie/2026/08/qwen-for-junie/] https://blog.jetbrains.com/junie/2026/08/qwen-for-junie/

## C400 — brianlmerritt
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx4307dcasl/

Qwen 3.8 flash next on one RTX 3090 and 128 gb ddr4 ram and strata provided a base system, but until I added autocode (or use pi) it was no good for projects.
 
I did some test projects involving data analysis and they did work but looked pretty crap. Speed was good, context 128k.
 
I would say it's good enough for backend development, especially if you get claude opus or gpt astra to set it up for you and oversee the project.

## C401 — cagriuluc
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx46pway5k1/

Are you not sharing the quants and the config because you tried it all, or…?

## C402 — T_rex2700
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx47m8c4qe9/

lemme guess, ollama on windows? yea forget about performance dude. that thing is good for mini model and chat.
 
at minimum you want to use something like lmstudio with llamacpp arg override.
 and if possible, try on linux.
 
and that reasoning loop is well, Qwen being Qwen. I learned to be very specific with Qwen.

## C403 — Comprehensive_Rock50
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx49zpk1leo/

128K context is a capacity setting, not a guarantee of comprehension. With a 27B model, even 4-bit weights alone can consume roughly 13.5 GB before quantization overhead, runtime memory, and the KV cache. That leaves limited VRAM for a large context. But we don't know their quantization, actual context usage, or whether layers are offloaded to system RAM. Importantly, insufficient VRAM generally causes memory pressure, offloading, slowdowns, or allocation failures. It doesn't directly reduce the model's inherent reasoning ability. Quantization and truncated context, however, can affect answer quality. model intelligence and agent reliability are separate engineering problems. The Reddit poster hasn't established which one is failing. I also wouldn't conclude that their expectations are unrealistic. Understanding a project, making a small change, running a test, and reporting the result is a reasonable target for evaluating a local coding agent. What I would really want to see is one failed execution trace: the prompt, files actually read, tool calls, context usage, and the point where the agent starts looping. That evidence would tell us considerably more than the model's parameter count. One question remains unanswered in their post: is Qwen actually failing to reason, or is their agent failing to give Qwen a coherent environment in which to reason?

## C404 — xb1n0ry
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx4pqkg0l2c/

The harness is the most important topic here, especially with smaller models which might need correct guidance. Use qwen 27 with pi on medium or low thinking. At least Q6. high or xhigh will make the model get lost in overthinking and mess up the very basics.
 Better: Qwen flash next with strata (might need additional RAM).
 But first of all, get rid of that stupid engine first and get proper llama or vllm.
 But if you really want to stay on 27B, then look for finetuned models with better coding and reasoning capabilities for example this one  [https://huggingface.co/blog/bytkim/qwen38-27b-pi] https://huggingface.co/blog/bytkim/qwen38-27b-pi

## C405 — relmny
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx4ptzd0plv/

so you unashamedly say you use ollama, then don't mentuon quant, parameters, hardware, etc and claim is bad?
 
First use a proper inference engine, then look at what quant you're using and why and then look at the recommended parameters.

## C406 — ddensa
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx52aqitl7n/

For me it works well, I'm using unsloth desktop for the inference engine, Qwen desktop for the harness and a q4 model (unsloth version). 
 
That being said, I also ask codex to do a first pass on all tickets that Qwen3.8:27b will work on, codex does the planning and I explicitly ask it to drop a coding guidance so Qwen gets a good direction. Also ask codex to perform the work review and drop change requests until the work is good.

## C407 — LocalhostRonin
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx52yc5j99f/

Gotta share your full runtime config for better comments (model quant, KV quant, serving stack, vision support, etc)
 
How long did you wait before you decided it was a repetitive loop? From my experience, it tends to go in circles for quite a while then decide okay that’s the right way. Qwen tokens per task can be like 5-10x of Opus, so gotta give it time.
 
Lastly, Sonnet 5.5 has 1M context window, while Qwen-27B has only 128k. Analogy: Sonnet has a larger chopping board to process a huge pumpkin, while Qwen is expected to process the same pumpkin on a chopping board 88% smaller. The same 30k tokens .md file is a drop in the ocean for sonnet to process, but it’s over 20% of the 27B’s context window.

## C408 — loudguitar42
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx53z9l8sdd/

You are holding it wrong.
 
And I mean it.
 
I sue Qwen3.8-27b as my primary workhorse and is doing wonderfully.
 
Get a decent harness, like Hermes, make sure you have the system trained properly. And be happy.
 
I can guarantee you that is my main coding agent since May.
 
On a RTX3090 with llama

## C409 — _BookBurner_
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx58zrllqjp/

I had to do multi-level orchestration to make Qwen3.8 27b usable. Planner agent splits work into bite sized tasks, these are then fed to the main orchestration agent through a tool of your choice, If the tool manages it in separate sessions, that is even better.
 
Orchestrator and his context are responsible for planning only and for pushing the task forward, invoked subagents search for context, do analysis and perform code work.
 
a) single parallel process, that way, even if the agent decides to think a lot (which happens often with Qwen3.8 27b) it does not run out, if the agent spawns multiple subagents they are handled in a merry go round style.
 b) dcp compress and configure it to clear when above 60%, that way, the orchestrator clears tool calls and steps that are no longer relevant.
 c) task manager which prompts the orchestrator with next tasks when it is idle and ideally starts new sessions for them.
 d) a test agent which then checks that the results compiles, contains what was decided at the beginning of the task etc. I myself task the orchestration agent to create criteria file with original requirements and spawn a "tester" subagent as the last step to check the changes made (by git diffs) fulfill the criteria.
 
That way, you can do quite extensive work with limited context size. Tbh it took me a while to wrap my head around this and set something like this up :D but it works. But it is slower as there are tokens consumed on the orchestration and the "talking" between the agent and subagents obviously.
 
PS: but from my observation, if you can get qwen3.8-flash-next-gsq-rco-coder from ISTA-DASLab to run, it achieves better results than 27b even if partially offloaded. And it does not suffer from the insane 10k+ reasoning, meaning, even when it outputs tokens at some 60% of the speed, it will still finish the tasks faster. (16 + 16 GB RX 9060 XT + 64 GB RAM)

## C410 — jsbot-02
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx5f9r3nezk/

I did the pelican riding a bike test. Qwen 27B, apart from being a bit slow, actually did a pretty good job — the visuals and logic are quite normal. The only issue is that the physical relationship between the pelican's legs and the bike pedals wasn't handled well; other than that, there are no major problems. 9800X3D 9070XT 16G 64G DDR5 Qwen3.8-27B-GSQ-RCO-GGUF q3 Speed is around 30-40 tokens.

## C411 — Joozio
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx5uc3zz3c1/

I did nearly the same swap on my own agent setup, though not for coding, so take this as adjacent. My system is built model-agnostic, so moving it from Claude to a local Qwen 9B served by Ollama was a one-line config change, and then the same agent was running its usual tasks on Qwen.
 
What held up: memory recall, anything shaped like "read a file, find the relevant bit, report it", and calling the right tool on straightforward requests. What didn't: analysis or anything needing real synthesis, where the quality gap was obvious. The 4B variant dropped off hard; for my kind of work, 9B was the floor.
 
So a local model handled a real subset of what Claude was doing for me, and the pieces that held were the narrow ones. Which part breaks first for you, the planning across files or the individual edits?

## C412 — Damn-Sky
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx5vscyrixw/

I am using switft 1.5 iq3_xxs on 16gb vram with 132k context and it works wonderfully well.
 
Sure it is much slower (46 token/s) than claude but for home use, it's great. Sure, there are some errors from time to time but it's perfectly fine most of the time.
 
edit: I use it mostly with deepseek harness and I am still amazed how well it works. DSH is fcking great btw.

## C413 — vintagevibes_
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx69edwx4tg/

As others have said before ollama is likely the culprit. I haben’t got it to work for agentic tasks.
 
Try lm studio + claude code cli, claude will help you set it up. On a 3090 with 24GB ram I suggest to use the quantization Q4_K_M. I tested it yesterday on a 4090 and it was a blast, averaging 60-70 t/s on agentic tasks and it did a good job on all of them.
 
Also don’t use smaller quants than Q4 in my experience they don’t work well, just get stuck in loops on tool calls.
 
Just one caveat I noticed: It is more bullish than Claude would be, i.e. it will install stuff without asking just to solve the task and not fact check as much. I assume this can be solved via promoting and system set-up.
 
Have fun and I am excited to hear back how it goes for you!

## C414 — fififijamie
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx69im9z63p/

Been working well for me (mostly small personal projects though). Running 24B oQ4e-mtp on oMLX. 64GB unified memory, 262k context. Most of the time I just turn thinking off.

## C415 — sarp3d0n
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6amdc1zmo/

Try PolyStrata. I moved from Ollama, to llama.cpp and since few days Polystrata. There are some models quite impressive. I only have a Rtx 5060 8gb vram with 32gb ram and my speed is now X3. So I now use Tiel Coder 35B a3b. But you could use Swift 1.5 with your hardware.

## C416 — BlAcKdN
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6b8egtc4h/

I do use Qwen 27B a lot on some light work and it performs quite good for me I use it mainly through opencode howere I don't think the harness is the problem in your case. I've done a lot of testing with claude on different configurations to find the best quality/speed. I'd recommend swapping from Ollama to llama.cpp and find out the best configuration for your case. I did encounter (rarely) some looping on High thinking other than that it works perfectly for me. If you'd like me to share more how I configured it and how exactly I use it you can DM me, happy to share.

## C417 — bobish01
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6baubhrxf/

Use qwen strata flash 125B instead, its way better when it comes to coding larger projects and following instructions. For me ChatGpt act as the architect and planmaker, qwen 3.8 flash the coder, and then GPT again as the final "bug fixer".

## C418 — sumane12
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6bh1aoh45/

Llama.cpp with deepseek harness at q4 quant.
 
Have claude opus 5.5 set it objectives and instructions.
 
Thank me later.

## C419 — No_Oil_6152
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6bxqz7zj8/

You're going to need to tell us what your temperature settings are, what your k/v cache is, what harness you're using with 3.8
 
3.8 can deliver good results - its just VERY SLOW.

## C420 — webAd-8847
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6etug50o4/

Had similar issues.
 I switched to LM Studio and had more control. It all was about the perfect settings / context size etc.
 In my case VSCode + Chat + LM Studio (Custom Endpoint).
 It took hours to find the right model and settings for me.

## C421 — nomorespamplz
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6ftbfzag1/

llama.cpp and a good harness with a good custom prompt and even a smaller model will outperform what you’re seeing now.

## C422 — immediate-drink-9876
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxbhmc3e00w/

Best on your experience, which harness works best?

## C423 — Ancient-Camel1636
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6isohm9i9/

Qwen 3.8 27B is not as good as the frontier models, but its quite cabable, so if its not working at all for you you must be doing something wrong. Hard to say what is wrong while knowing nothing about your setup but perhaps concider:
  
Context window. A context window under 128k is useless. Around 200k is fine. Use compaction and/or handoff when needed.
 
Harness. Local models run best on harnesses with low overhead like PI.
 
Thinking budget. If it overthinks, set a thinking budget.
 
Skills. It need skills to work well, but keep skills and MCP's to a minimum, don't overload the context window.
 
Use it for 90% of the work, not 100%. Plan with a frontier (or top tier open source) model, execute with Qwen 3.8 27B. Use a a frontier (or top tier open source) model as Advsor that Qwen can call when unsure, confused or needing help. Also do the final review with a frontier (or top tier open source) model.
  
A well organised and well documented codebase (code-wiki give you automatically generated, up-to-date documentation for your code) also makes a great difference. Using tools for indexing/mapping and retrieving the codebase may also help it understand and navigate it better (consider lean-ctx and serena for this).

## C424 — floriv1999
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6iu372279/

Depending on the harness and inference engine, deactivate rolling context and set the context size in the harness. Otherwise your prompt etc might leave the context window.

## C425 — Pretend_Engineer5951
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6kqwguvfn/

Swift 3.8-27b at 8bit and xhigh reasoning is an excellent coding solution.
 
Just buy 2nd 3090 and run at least fp8 quant with vllm and tensor parallelism. Look at club-3090 on Github for performance tweaks.
 
As for harness try  [http://omp.sh] omp.sh . Many people run  [http://pi.dev] pi.dev but I compared both spending reasonable time and pi easily overbloats llm requests with unnecessary tooling instructions. For example you add 3-5 extensions which you need for certain functionality and they bring 30 tools. From that 30 tools you need only 10-15 so they bloat and pollute context. Yes, you can exclude or include manully each tool but it's not easy. 
 
On the other hand, omp has anything I need out of the box and optional tools can be safely disabled from TUI. When I compared pi vs omp I had on "hi" prompt 26k tokens vs 12k.

## C426 — Thutex
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6yiaketuo/

qwen is absolutely capable, so it's likely a config issue + for a dedicated llm setup, your machine is quite average (as in: more of a mid-tier gaming machine than an actual high-tier ai machine)
 
i would suggest:
 
1) using llama.cpp to load up the model (so install llama.cpp and configure the model in the config file)
 
2) run it using hermes (i.e. connect it to llama)
 
3) and add mcpproxy to add some mcp stuff as well as set up the md config in hermes
 
i run this same model on my laptop with a 5090 24gb, and it performs ok, especially with hermes.
 
with "ok" i mean that it does its tasks really well, but not as fast as claude or any cloud would (just a laptop, afterall),
 
and even though hermes is pretty good ad compressing context, when you hit the context size a few times and compress too much, quality does degrade. (only 24gb vram, afterall)
 
if you've got the budget, and can extend the machine, i'd try to add atleast 1 or 2 tesla v100 cards (if you get the 32gb model twice, you'd end up with a total of 88gb vram and that's going to make a huge difference)

## C427 — lacrem
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6yt3qubab/

I run qwen 3.8 27b in a MacStudio m2 max with 64gb using LM Studio, gets around 20t/s. Flint runs faster and same reasoning level.
 
You have to split up prompts in smaller chunks, don't expect a 27b model behave like DeepSeek 1.7T

## C428 — ChemicalRoom2878
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx7dp1mb2cj/

I hope you’re running Linux, have unlocked the full TFLOPS potential of your GPU, and consider switching from Ollama to Unsloth. You might get a very different experience!

## C429 — rusl1
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx7ebxcbna9/

AI slop, I can smell it from kilometers away

## C430 — Crazyfucker73
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx7iz80r6oz/

If you're not using the 8bit quant this is why and also you only have 24 gig of VRAM which is very limiting...
 
You need to read this because if you don't, then you're just gonna keep getting shit results.
 
You must have an 8bit quant for this model to be useful
 You must be using a decent harness. I use Hermes agent.
 24gb of VRAM is NOT ENOUGH
 You must leave reasoning on up to Max. This model does not work if you cannot let it think

## C431 — sometimes_angery
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx7jq68tdpg/

Given the 32gb ram and qwen 27b being 55gb on float 16, I'm guessing you're using a float8 version? Or what quant? We run float16 at work and it does have blind spots but can complete tasks, just not quite perfectly. Flash next was better at an int4 quant than 27b float16 tho.

## C432 — AnxietyCorrect106
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx7laxa9mzn/

Me when I use 1 bit quant and wonder why my model is retarded

## C433 — Sirlowcruz
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx8hbfnpi1s/

it sounds like you still need a harness for the model. something to make it act agentically. maybe hermes.
 
also important to know: what quantization and reasoning mode are you running? anything at or under q4 makes this model act weird IMO.

## C434 — megadonkeyx
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx8i49l0mg4/

I've found strata and Qwen next to be very good. My harness has months of work around loop detection and intervention to manage thinking issues. I run strata under Linux headless so that machine is dedicated.

## C435 — xapep
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx91i1tw6n6/

Before you blame the model, check what the quant and the context length leave you. A 27B at 4-bit is roughly 15-16GB of your 24, and a 128K window needs its KV cache somewhere on top of that. Once it spills into system RAM you're decoding over PCIe at a few tokens a second, and long-context quality falls off a cliff. That looks a lot like a model that lost the plot. 
 
Try the same prompt at 16K and watch VRAM and tok/s. If it snaps back to something usable, you were never running the 128K setup you thought you were. 
 
The other half is the harness. Sonnet 5.5 in an agent loop reads the file, runs the test, and retries a patch that didn't take. Drop a 27B into the project root with the same md files and none of that happens, so the first wrong step becomes a loop instead of a retry. One file at a time, explicit paths, and let it see the failing test output. 
 
I work on the serving side of an inference API, so take the last part with salt. What's your tok/s at 16K versus 128K? That tells you whether this is a hardware ceiling or a setup problem.

## C436 — Slow-Secretary4262
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx91rw0hvoh/

You have a big margin to make it work way better by using a different inference engine and tweaking it for days, but do not expect it to be even close to sonnet or deepseek or glm, we are not there yet, i think most of us enjoy the process of learning/endless optimizazion rather than actually doing real work with it in terms of autonomous coding, at least the one of us who don't have a 5000€ setup

## C437 — flapjack
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx9hq1a1wv9/

128k context window is absolutely tiny compared to Claude. You need to do a lot of work to effectively use that window. You can compensate by spreading the task out over a long time. What you could do with sonnet in 20 minutes will probably take 3-6 hours with your setup.

## C438 — Future_Deer_7518
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx9ox1prq90/

As an owner of basic Ryzen 8700g with igpu (no dedicated GPU) and only 32gb of ram I prefer Qwen3 Coder Instruct 30B with MoE architecture and A3B active parameters per token. I run UD-Q3_K_XL version from unsloth under llama.cpp and opencode agent, Q4 does not fit into my ram. I do not use this setup as vibe agent but as helper tool - I often offload small tasks like "scratch me a unit test", "implement pooling for this data set" or whatever for 30-90 lines of code. With short and stupid prompt it's doing a mess in 3-5 minutes with speed 11-19 tokens per second (still faster than my wpm), with refined prompt I usually satisfied after 1st iteration and then only cleanup this stuff a bit. Step by step I have control over architecture, spot errors early and have a good knowledge what is going on in my application. May be dense 27B model will be better but I have found it too slow, I need short feed back loop. Regarding your pc I do not know how much you paid but I am looking for an upgrade to ryzen ai 395 with 128gb of ram. This should fit 30B model in highest possible quality or bigger 80B model like Coder-Next. I am not willing to pay 4000 at the moment so I am waiting for a pop of this bubble :-)

## C439 — Minimum_Site_1915
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx9per340ip/

I don’t know exactly what you are making, but if you are working on something like Roblox, local models are horrible at it. Luau is just too much of a niche language for them to have any real knowledge of it.

## C440 — Top_Ingenuity_1830
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx9pq9r96zn/

Try using with pi.dev. I feel like other tools load too much system context or whatever the fuck. Also have Claude tune it for your system. It's slowish but it works.

## C441 — ThrowawayALAT
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx9rf3d8yoz/

It’s not you - it’s that industrial models are getting stronger, better, and more updated daily/weekly, and the general population mostly doesn’t have access to them for a reason. You wouldn’t want average Joes meddling with a quick-to-fire shotgun in public, just as some of breakthroughs were right under our noses for centuries before we were able to connect the dots like discovering another research drug and publishing 10 papers prior to FDA approval with an ethics board involved, or so we’ve been told.

## C442 — Ok-Concentrate-5228
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx9u164tuap/

For real work and LLM inference, I would use real GPU. Like get a VM on the cloud. If you are a software house, I can assume you consume a lot of $-tokens. Run a 120B model at least at BF16.
 
But also this requires time.
 
Local LLMs don’t work out of the box. And a lot of things matter like VLLM tags, coding IDE (ZooCode, Codex). Etc.
 
Also for coding your claude model can plan and Qwen 3.8 can code. Make sure you force 3.8 to test in a loop and not produce you code that isn’t tested. This is different from Claude or OpenAI frontier models, the loop is innate. Based on my experience Qwen Models requires you forcing it through prompting and skill
 Happy yo provide guidance.

## C443 — Head_Evening_5697
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxa4hfzg4o0/

try out Gemma 4 27B A4B with 1 mil context size and report back - just a suggestion.

## C444 — boosnie
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxa6mpbmz6s/

Hi  [/u/Major-Creative] u/Major-Creative
 
Here's my local config. I run pi coding agent at 160K ctx that I use for code analisys, coding etc in a professionasl environment, mostly for privacy reasons. with a fresh ctx this will give you ~110tps generation and ~1250 prefill.
 I have only minor issues with this config (this is llama.cpp in router-mode. if you use a simple server rewrite the config accordingly).
 
The only HW spec that matters is your total VRAM. I have 24GB on an single rtx3090.
 
 [https://huggingface.co/ajgazin/Swift-Qwen3.8-27B-Uncensored-Dynamic-MTP-GGUF] https://huggingface.co/ajgazin/Swift-Qwen3.8-27B-Uncensored-Dynamic-MTP-GGUF
 
[*] n-gpu-layers = 99 flash-attn = on parallel = 1 metrics = true [swift-qwen3.8_Vision_Uncensored] # vision, single slot model = ~/llama.cpp/models/Swift-Qwen3.8-27B-Uncensored-Dynamic-MTP-UD-Q4_K_XL.gguf mmproj = ~/llama.cpp/models/mmproj-Swift-Qwen3.8-27B-F16.gguf spec-type = draft-mtp spec-draft-n-max = 3 ctx-size = 160000 batch-size = 1024 ubatch-size = 512 cache-type-k = q8_0 cache-type-v = q4_0 jinja = true temp = 1.0 top-p = 0.95 top-k = 20 min-p = 0 presence-penalty = 0 repeat-penalty = 1.0

## C445 — Ok_Parfait_5373
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxadhu7zfz6/

J’utilise ce modele tous les jours sur la même carte j’ai aucun problèmes j’ai 150tok/s, il raisonne bien (et je suis dev). Avec le 27b c connu qu’il travaille mieux en thinking medium pour les taches de tous les jours. Ou sinon prend un modele swift ça peut aussi améliorer ça. Mais a mon avis ton problème c que tu met trop de skill en contexte . Utilise pi-agent deja c moins glouton et met uniquement le nécessaire a ce niveau

## C446 — Rogglando
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxafychgqea/

Heey OP!
 
Your harware setup is fine. Your inference engine is a good place to start as it's easy when you are jumping into local AI.
 
But with your setup, you should look into an engine called Strata. When setting up Strata you can follow the recomended settings, but if you are able to increase you context to 200k I highly recomend doing so.
 
With strata you can utalize your system ram for your setup aswell as you 24gb vram card. I would recomend also switching to a Linux distro to free up more of your system for inference. I also recomend useing this pc for only for running your llm and set it to have 3 slots, minimum 2.
 
Now, to explane why. 27b is a dence model, meaning you have to send every token request through the whole model. With strata you can run Qwen3.8 Flash Next Coding. This is an MoE model of 125b with 6B active (A6B). So you can load this model on your GPU, System RAM and some on your SSD. Thats the magic trick. 27b you have to keep only in your GPU.
 
Also set it to serve localy so you guy can use your regualr PCs for codeing and connect OpenCode, Pi or some other harness you want on your normal machines.
 
That way you can have all the power of that PC to run the model while you can code and do your work on your own laptops or hardware.
 
Also, do the 2h tuning. Dont use the App, use the CLI version.

## C447 — pinkwar
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxax0csoqzl/

Crazy how you did it so backwards. First you find a model and setup that suits you (using cloud rented gpus) and then you buy the hardware.
 
Who approved buying that without any sort of POC?

## C448 — dc740
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxaydwsf3c5/

you are using a heavily quantized version of Qwen. that's not the same as running a full version, and the difference can be day and night. as a side note: next time provide details and write the post yourself. nobody cares about typos and writing style. stop asking the AI to think for you. write that in your agents.md

## C449 — Sensitive_Mountain97
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxb0crmh95v/

Claude is superior for coding tasks. I'm using Ternary Bonsai 2 which is a compressed version of Qwen 27b. Qwen is super dumb for coding tasks. It can't even compete with sonnet 3.5

## C450 — KEIY75
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxb37ix3s85/

Actually it has to be config issue and yeah use llama it’s better because even my heretic qwen created an entire call center with asterisk without any problems. It surprised me

## C451 — AnticRaven
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxbdrs0egf9/

I tried this, it’s overthinking. Qwen 3.8 Flash Next. Is the best. Good luck

## C452 — tuborgwarrior
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxbfat1dgo5/

Test if it chokes on context. If it's always auto compacting early it's sometimes much better to have a stupider model that gets to see the full picture of the task.

## C453 — TomFlatterhand
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxbhzgm6isi/

Also ja, die Hardware kann ein Problem sein. Ich setze Qwen 3.8 27b 8Q bei vollen 262144 Tokens ein. Das macht einen Unterschied zu einer kleineren Grafikarte. Dann könnte es sein das die Art von Denken von Claude auch zu einer bestimmten Art des Aufbaus von Projekten und Dokumenten führt, bei denen andere LLMs Probleme haben sich zu orientieren. Qwen kann programmieren. Ich habe aber häufig Probleme mit Hermes, welches sich als Agent immer wieder einmal verheddert. Ich baue jetzt an einem eigenen Agenten. Und natürlich ist es nur eine kleines lokales Model! Versuchen Sie sich eine größere Hardware anzuschaffen, vielleicht mehrere RTX 6000 Pro und dann ein größeres LLM betreiben.

## C454 — Virtual_Rice7837
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxbzmcnchia/

I went through a similar experience. After figuring out that a 4090 wasn't going to comfortably handle things, I stumbled across ninfer and landed there. Was able to get a decent context and over 50 tok/s. For some very general things, the answers were ok. I had been following all the hype how the 27b model scored this and that. Unfortunately, it's the real coding tests that show how capable it is (or isn't). I've been writing apps to consume AI for about 3y and using code agents for a little over a year, swapping back and forth with the big boys on their various models. My hope had been to utilize something local for both .net and java coding.
 
While Qwen did ultimately produce results, the quality was almost always unacceptable. Large tasks (go build a poc Blazor app or write a small java app) were a waste of typing. Narrowing down to targeted changes within apps that Claude/ChatGPT had spit out, would give me something, although reviewing what it did more times than not just couldn't be used without either me pointing out to it all the issues or passing it back to a big boy model to review and correct. It wasted more of my time trying to utilize it for anything meaningful.
 
I went through several front ends (don't care for CLI, given its limitations, personally). Ended up on LibreChat, which was the best of the bunch for my needs. I'm fairly skilled in writing decent instructions and optimizing for the given model. No matter how strict, light, heavy or focused I attempted them, the overall quality of 27b is not for the level of work I'd expect to use. Standards can vary I suppose lol.
 
-max-context -"131072" -kv-capacity -"131072" -max-concurrency -"1" -max-pending-requests -"16" -pending-timeout-ms -"600000" -prefill-chunk -"1024" -kv-dtype -int8 -spec -mtp -draft-tokens -"3" -default-max-tokens -"32768" -lm-head-draft -prefix-checkpoint-policy -rolling-tool -continuation-cache -l1-l2-l3 -continuation-cache-dir -/var/cache/ninfer -continuation-cache-namespace -orcarouter-qwen38-314e2812-int8-131072 -continuation-cache-l1-mib -"768" -continuation-cache-l2-mib -"16384" -continuation-cache-l3-mib -"49152" -continuation-cache-filesystem-reserve-mib -"8192" -preserve-thinking -vision

## C455 — anaNimrod
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxc2yjfgrkz/

If you're using an autonomous agent as an agent, you're doing crap. Connect a cloud agent and use the local model as a SUB-agent. You'll be surprised. For start is enough opencode's free tier deepseek v4.1 flash.

## C456 — moochine2
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxccjloran7/

Which quant? Maybe you are using a 1 or 2 bit quant? Try this for example:  [https://huggingface.co/ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF] https://huggingface.co/ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF
 
Upgrade to 64 RAM as well. It won’t really make things faster, but it will help overall system performance and help you not run out of memory.
 
Consider Strata also with the 125b coding version of the model also.

## C457 — Jazzlike-Plate
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxcl6y6e10l/

I had a similar experience with that model. I used ollama. Can someone explain why that was such a huge mistake? I thought the server makes zero difference.

## C458 — icecraft1337
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxdaud9kskg/

Ich glaube es ist ein Harness Problem. Ich nutze einen eigenen Harness und da funktioniert es super mit 128k Kontext. Aber auch Pi Agent sollte gut funktionieren und ist leichtgewichtig. Ich habe Swift 1.5 Qwen 3.8 27b in IQ4_XS quantisierung und kv Cache auf Q4 laufen. Backend ist llamacpp.

## C459 — Great_Airport_4495
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxdf7t7fg6c/

The local models are not in the same category as Sonnet 5.5. You can compare high quants of Qwen 3.8 27b or especially Qwen 3.8 Flash Next (much larger MoE) to ~Opus 4.5 / 4.6 reasonably favorably but Claude 5.5 family models are MUCH more capable especially fully autonomous.
 
And you are not running a "high quant" on a 24gb GPU so that doesn't help either. At most Q4. Qwen 3.8 27b at Q4 is a good local model but yes, it's not anywhere close to the frontier and you will have to babysit it closely.
 
Also note your kv cache should be at least 8 bit, otherwise you will find much bigger context coherence problems.

## C460 — Wolkenflitzer
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxdjdz0fpgj/

Use qwen flash next with strata. It handled everything I threw it at.

## C461 — No_Ad_5933
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxdn96ygbz9/

try strata ->  [https://github.com/Niko1221/Strata] https://github.com/Niko1221/Strata
 I tried this with rt 2080 super 8GB gpu with 32GB RAM, qwen-3.8-flash-next-coder 27B can explain me about repositories and can create single file scripts without issues, I tried with  [http://pi.dev] pi.dev harness and used this tool to index the codebase  [https://github.com/Graphify-Labs/graphify] https://github.com/Graphify-Labs/graphify  [/u/Major-Creative] u/Major-Creative

## C462 — PressTilde
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxedo6taaw3/

I’m coming at this late, but, I can tell you I spent a boatload of time fixing this on bantamfactory:  [https://github.com/BANTAM-ADMIN/bantam-factory] https://github.com/BANTAM-ADMIN/bantam-factory
 
I fixed it by constraining output on the 27b and putting it in more of a factory workflow. I’m using a 4 bit k_s or iq4 and it’s amazing, faster and more accurate, able to finish.

## C463 — ruineka
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxeg4kkg6ua/

I absolutely adore qwen 3.8 27b. It single handedly made me want to upgrade my workstation by adding another dual Intel arc b60 48GB into my system. I'm sooo glad I took the chance on intel when the cards were cheap because the payoff has been incredible. Use the deepseek harness with Qwen 3.8 27b and the potential is outstanding.

## C464 — BeatDistinct317
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxet1la76hx/

Comparing Qwen 27B to Sonnet....does anyone know how many parameters and what quantization does Sonnet use? Ever rumors? 
 
If Sonnet is some +300B you probably can't expect Qwen to compete

## C465 — FRackgfxhjxgfhj
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxeumcvmmjo/

You need a lot of setting up, rag, memories, tuning, and not comparing to Claude. Ollama+OpenWebUI is very powerful.

## C466 — robertotomas
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxez5v5cs69/

There are two things that stand out as first to check: model quantization and kv cache bit depth (if it is 4, maybe that’s the problem).
 
Also if you were using sumthin like mtp or the like for speed, incorrectly implemented or using the wrong predictive model, and if you are using nvfp4 quantization or similar, not providing the scaling factors, etc.
 
After that it is maybe an issue in using the model incorrectly, like not using a current OpenAI protocol with a runtime that serves it that way, etc

## C467 — mechitworks
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxf7fsfmmjn/

The biggest problem with ollama as inference is that it truncates as your context gets larger than it can handle. Tools like claude code will use a lot of context very quickly.
 
I run on a specific nvfp4 3.8 27b on a rtx 5090 with 180k context with vllm and setup with Pi harness that also automatically compacts the context as it goes.

## C468 — nosimsol
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxftgg4o3ab/

I roll 3.8 27b fp8 on vllm and it’s spot on most of the time. Comparable to Luna 5.6

## C469 — thisisme_whoareyou
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxg24x4njj9/

I just started testing it myself for complex logic not even coding yet and it doesn't pass.

## C470 — Sizzin
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxg4cwwccki/

You'll have problems if you want to serve more than one person with that hardware. Also, I don't really think Q4 is good enough for serious stuff, but if you do it in small steps, it can probably do it. 
 
Anything Claude aimed that I've seen is extremely bloated, content-wise. Not worth using on local models. 
 
I use FP8 with pi and it blows my mind at how capable it is. It's smart enough that I'm confident about leaving it working autonomously overnight or when I'm off at work.
 
Qwen 27b is really smart, but it was trained on the most common dev usage. If your work is too niche, you should probably try Qwen flash next, that has a wider knowledge base. Though, with your hardware, the quant you'll be able to run is not very trustworthy for unsandboxed stuff.
 
And be mindful of the quant you use. In my tests, nothing beats stock Qwen fp8. But I haven't done any real benchmark, just my usual usage, so take it with a grain of salt.

## C471 — sadomazoku
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxgf6pnx3fl/

100% configuration issue. I use the same model (q4_K_M) for coding task and never had any issue. I don't even use frontier models for coding anymore. I have a 24gb gpu as well and qwen fits inside with no ram offload. Get rid of ollama. If you're a team, you'll need to lean toward vllm. But start with llama.cpp on a single computer

## C472 — bigb159
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxhdetmdiua/

My experience - nothing lower than q6 was reliable with code and tool calls. Also, it's hard to work concurrently on so little vram - painfully slow. You'll have to either allocate team usage, or get another GPU to increase concurrency headroom

## C473 — w1ldr3dx
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxhin83o6n9/

Hmmm, such a long post and you didn't even mention what you exactly are trying to build or how it exactly failed.
 
I used Qwen 3.8 27b Swift 1.5 Q5_K_M (xhigh reasoning, with llama cpp server and pi agent) on my 5090 to extend the Steam Frame VR gamescope compositor, KDE Kwin compositor, linux wacom tablet drivers, wlserver, Xwayland to make my wacom tablet incl. pen works decently on the Steam Frame VR with drawing apps. This was a higher level of "new" coding task and it did this so well, it's all working perfectly now.

## C474 — flatfalafel
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxjur0zclgh/

As someone new to this world myself and learning a lot of the lessons people in here are sharing on my own, do you have resources on llama.cpp for newbies?

## C475 — International_Emu772
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxhishpppk0/

Try GLM 4.7 Flash the best coder LLM for 24 GB cards

## C476 — Sufficient_Phone_242
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxhmhs5es2s/

Had 3.7b 2x rtx 3090 you need like 200k context and even there it’s not worth it , it will create more errors than paying 200$ a month … or be slower

## C477 — Certain_Series6810
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxiw8fahxnm/

Quant matters a lot. Harness also matters. And your inference engine also matters. 
 
If I have to break it down 
 
Inference engine - llama CPP or vllm Harness - pi agent or something that is not bloated Quant - should be 4 or higher

## C478 — hopsec_
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxj12w7xk0y/

It’s the context size. That’s the main issue in my experience. None of the mainstream harnesses work great with really limited context, and a few have no compaction mechanism even built in, expecting it to occur on the inference provider’s side.
 
I built a harness shaped around Qwen 27B and limited context (I call it Sidecar cause it pairs with my AI named Skootr - though you can use it with any inference local or not), but I haven’t publicly distributed it yet. If anyone wants to be part of the beta, drop me a message.

## C479 — humanpersonlol
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxj137mpuw5/

sonnet 5.5 is probably ~700b
 
ofc a 27b benchmaxxed model will suck

## C480 — fathergoat_adventure
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxj6ktus1wg/

I've had good results coding with 3.8 27b on my 4090 using ninfer. I believe there is a ninfer implementation for the 3090 as well. With the same 24GB you've got, I can consistently get about ~250k context.
 
I was having a tough time before ninfer as I could never get a truly usable context length so I was constantly starting new sessions or the context was constantly compacting and degrading. Now, with ninfer, I just let 'er rip!
 
Ask professor Google about "ninfer 3090" and enjoy!

## C481 — mamjazzo
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxj83ew5ggz/

Gpt oss 20b has been doing pretty good for me on 16GB VRAM

## C482 — darksteelsteed
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxjhyyyc49w/

If you at still using the Claude harness it will break your local model as it just includes way too much junk in its context. 
 
I would suggest Pi.dev OMP Opencode
 
Also make sure you use the right template for qwen3.8. That was the main reason I failed when starting out.

## C483 — filliravaz
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxjldv1zzc0/

I use a different version of 3.8 27B, specifically designed for security work.
 
It is great and also quite efficient. Not at frontier level, but it gets most of the way there. 
 
The harness does a lot (I use OpenCode), and I believe that queen 3.8 needs a specific Jinja chat template. If you don't use it, output quality drops significantly. Correct temperatures and penalties also affect output greatly.

## C484 — starwaver
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxjnuucjcmb/

That has been my experience with Qwen as well

## C485 — KnavishlyUncommon
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwjv7pf3jxg/

what backend are you running it through, that'll make or break the agent behaviour before the model even gets a chance

## C486 — Major-Creative
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwjy0nkveeb/

We're currently using Ollama as the inference engine. As for the harness, we're still experimenting and haven't settled yet

## C487 — vogelvogelvogelvogel
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk3367s2hw/

using ollama as an engine always suggests me someone not relly spent time how to set up an llm
 
use i.e. llama.cpp, ask some proper ai to do some test runs with different speculative decoding configs, then go from there
 
claude code? rather not uses too much context, try i.e. pi
 
also comparing to sonnet 5.5? every half decent benchmark will tell you it settles at best at about two versions earlier
 
(also as a software house researching so much only at the surface..? also single 3090..? which means q4..?)

## C488 — Ratiofarming
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk51wh0xic/

Okay, but which ones are you currently using?

## C489 — Potential-Leg-639
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk6fpsmmch/

Ollama?
 You have to dig a bit deeper now. Ollama is a no go. Try with llama.cpp first, but nowadays there are a lot of different inference engines…
 
Get another 32GB RAM and run Strata with Qwen3.8-Flash-Next, ot wont get any better. And you will get around 100 tk/s TG and 2000 tk/s PP and a very capable model. But not really optimized for concurrent usage (yet). Therefore vLLm is probably still the best, but another 3090 would be needed for more users anyway minimum..

## C490 — Perfect-Campaign9551
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk6tmw9bj4/

Ollama is trash. Look into llamacpp. Or strata

## C491 — UraidDiag
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk7g768nfm/

Dude, it probably just doesn’t fit into your vram. I run the same exactly LLM in my MacBook Pro M5pro 48GB. And some times it struggles with memory pressure, but never has any of the issues you report. I’ve built an entire app on pretty well. It can be a little slow at times, but it does work. You might just need a smaller model.

## C492 — overand
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlob09glnk/

A Q4_K_M quant would fit just fine on their GPU.

## C493 — vimaillig
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk9emyeu91/

Which harness are you experimenting with? I’m just starting to setup my environment running it on a 5090, unsloth, and using opencode and/or pi and it’s producing per my expectations…

## C494 — Hood-Boy
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkb8b3b7oj/

[https://sleepingrobots.com/dreams/stop-using-ollama/] https://sleepingrobots.com/dreams/stop-using-ollama/

## C495 — Prudent-Ad4509
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkwdf70hb5/

This marks your position as very, very early expertiments. First, 24Gb gpu and models that you can run on it are more of a second opinion/search the problem/throw-promts-at-the-wall-and-see-what-sticks kind of tool. You need at least two if you want it to actually write useful code. Second, ollama is basically not an option, except for early experiments. Third, you have already seen several comments about the harness, I won't go into that. I'm using opencode, others use Pi, everyone have their preferences.
 
I have experimented today with 27B on 8x3090. It is not easy to set up, but it is about enough to run with 4 agents without dropping native model precision. Acceptable drop of precision with just 1-2 agent moves you into 2x3090 territory. With just one 3090 you can use it for wild goose chases when you need fresh ideas about a source of a particular bug, without risking blowing up your token limits. It is actually very useful for that.
 
But, and this is a very big but. If your goal is to save money on tokens, you are better off getting opencode go or glm or kimi or deepseek subscription. I would not even suggest getting a second 3090 if your goal is to save. For wild goose chases one is enough.

## C496 — Frail_Waif
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmk8ynn2ch/

I don't understand why people are down voting you for answering the question. It's very helpful for where to go next.

## C497 — Un4giv3n-madmonk
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkd63t65k3/

I notice barely any difference for straight coding tasks between opus 5.5 and sonnet and 27b

## C498 — OrangeManSad
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkqm34f8v9/

Lol yeah qwen3.8 27b is miles above sonnet, you are right

## C499 — zanar97862
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmsi25di8z/

? Strata is not a dense model engine...

## C500 — PituSmart
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwuut4ni0m9/

No, Strata is for MoE inference.

## C501 — zanar97862
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwwbpudoiw0/

Yep, though it would be cool to see some dense optimisations

## C502 — ieatdownvotes4food
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwppzgl36w4/

then vllm, then sglang, then nintendo64s

## C503 — _RemyLeBeau_
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwytdbkepwk/

Check their docs. I said I don't use their product.

## C504 — Dinth
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx5jezc0syr/

Haven’t they went back to mainline llama.cpp in the lastest versions?

## C505 — FMAGF
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpkegv7sf9/

Is ollama fine for regular text generation and reasoning?

## C506 — Smooth-Television-48
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwry23bgfqc/

Yeah its fine, just can be slower.
 
Honestly unsloth is pretty great as a click to run style do everything

## C507 — infiniti306
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwztp1spfhc/

So I just installed ollama qwen 3 14b two days ago. Should I switch too?

## C508 — sebt3
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx0famuazz9/

Depending on your hardware, if you have enough RAM strata. Else llama.cpp with a more modern model. Qwen3 is last year tech and pretty much worthless by today standard

## C509 — username8914
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwo4qvtzqn5/

That's not quite true, it is beginner mode for local ai though. Very few people will magically jump into custom tunes from zero. Ollama also backend exposes all the same llama.cpp and vllm stuff, you can tweak it just the same. It won't run Strata for them though.

## C510 — united_we_ride
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwulk0cza8x/

Honestly, for inference engines? Depends entirely on your system.
 Llama.cpp (Unsloth Studio), or Vllm. 
 
For chat interfaces/inference engines:
 
Unsloth Desktop/Studio, or Open WebUI.
 
I personally recommend Unsloth Studio for the engine and the inference interface. It has great built in tools, can access your terminal if you let it, support for skills, image gen, etc.
 Its a one stop shop that just works far better than Ollama.

## C511 — External-Fun-8563
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwurn9zcxb6/

Another noob here: I just started playing with LM Studio, is that not a good option? Should I just jump to Unsloth immediately if I want something with a decent UI?

## C512 — CLG-Rampage
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwv4uwdud2b/

LM Studio is okay but it's generally behind on features and the latest llama.cpp versions compared to Unsloth.

## C513 — united_we_ride
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwv8cg3van7/

LM studio was where I started, moved to open webui, and now moved to unsloth.
 
LM studio is basically the same thing, unsloth offers more to do inside the suite.
 
So, my recommendation would absolutely be to swap to unsloth, if you like it self contained like lm studio you can run unsloth desktop, which I just studio in a GUI app, or you can run unsloth studio which is in a webui.
 
Go unsloth desktop if you're familiar with LM Studio, you'll find you can do a little more in it. Even image gen

## C514 — rororo99
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx5y2sew0x1/

What is bad about ollama and what is a better solution?

## C515 — Repulsive_Initial308
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx62innfxk5/

Most people try lm studio after ollama.

## C516 — rororo99
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx70cz1u0f6/

But why? I have Ollama with Open WebUI and Opencode and works totally fine.

## C517 — USArmy68Whiskey
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk00ddx8kh/

It's a mix of both. You're spoiled from using a better model so weaker models seem way worse, and also yes the weaker models are still really weak. Unfortunately local AI (that you can actually run without a mini datacenter) still doesn't really compare to even frontier's lower end models. It's getting better still though, over time. I've been using qwen 3.8 flash and I have been honestly pretty disappointed, even comparing it to something like gpt luna.

## C518 — 575_Inverse
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkf2lzf7hg/

the 3.8-27b is not weak at all. The only issue is you're expected to know what you're doing

## C519 — USArmy68Whiskey
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkxs8hejdu/

I mean yeah if you know what you are doing and are willing to sit there and hold it's hand every step of the way then it's great, but better models you don't have to do that nearly as much.

## C520 — 575_Inverse
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmudwmu84i/

so you don't at least tell your model how you want something implemented and why?

## C521 — KinkyMonitorLizard
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkaiqo84v9/

Medium on this model is known to cause problems and has poor results. Either none, low or xhigh.

## C522 — SkiBikeDad
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwl0q0ncqzo/

This was early speculation but I think plenty of benchmarks since have demonstrated medium to be a fine middle ground between low and xhigh for most work.

## C523 — skifreek
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlb9wu6aw4/

I will try this, thanks!

## C524 — sudden_aggression
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpfw0i75pc/

medium is fine, I found there are a bunch of levers that affect reasoning strength (quantizing cache too much hurts it).

## C525 — PatienceSweaty33
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2jgoow8f6/

the "v" from "kv" doesn't mind lower than q8/int8. Just make sure your "k" is set to as high as your card can handle.

## C526 — ptear
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmptuvelcy/

That's your solution for everything.

## C527 — superbiche
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmw9zw73qa/

That's the solution for everything of this kind that's already explained in hundreds of threads here yes. This is like going to your car dealer to ask for something that's in the manual or smth that can be freaking Googled.

## C528 — Ratiofarming
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx66wcn6c9s/

That's indeed a perfectly valid solution for searching a large amount of information for a very specific answer quickly. Setting up LLMs with the help of Claude or ChatGPT is almost trivial. People not using those tools are just making their life difficult for no reason.

## C529 — superbiche
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm9b6w4kv9/

Yeah QFN is amazing to run locally. But 27B is not that bad. 
 
Tbh using Sonnet and being surprised a single 24Gb VRAM GPU is not better for one person is... Interesting. I'd give away a kidney to know how many people are trying to get something out of this poor rig - with 120k ctx. The poor Qwen

## C530 — _RemyLeBeau_
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmlq4ecja8/

Do you have an HF link? I would like to try that model

## C531 — MarcusAurelius68
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwrubhbxy8z/

Look up Radiance - that’s what I use with 2 x R9700. Or Strata.

## C532 — _RemyLeBeau_
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwzbb89p7dw/

Strata isn't a model, but an inference provider. If you're comparing QFN to 27B, you must be referencing a model.

## C533 — sinan_online
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmz7d2r8o2/

Harness is probably the most important question. Consider looking into dev.pi, I haven’t tried to myself, but I heard many good things about it.

## C534 — Plastic-Stress-6468
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkglagel5x/

On 24gb with 128 context and 27b, you are using what is commonly known as "a lobotomized setup."
 
Don't quant kv, and use Q8 for model weights at minimum. Aim for 96GB vram across total pool so you get some concurrency in there too.

## C535 — MainWrangler988
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkteq5edut/

It’s better than a 5 year old llm. But no local model would be worth its time

## C536 — BawbbySmith
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm1yocgo80/

You fell for the hype, that’s the main issue

## C537 — FragmentedHeap
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwr4wm38ote/

If the answer isn't "use claude to do this" it's wrong, because using claude to do this is the only way you can do live research fast enough to keep up...

## C538 — Connect_Ad791
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwrfqkc3ezl/

yeah but, the local models don't refuse my nefarious code requests.

## C539 — FragmentedHeap
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwruisar4ps/

Claude happily built my entire uncensored Qwen 3.8 Flash Next stack, no refusals, and now I have an AI that will do anything I ask it too.
 
Claude will also happily work on engines for reverse engineering things, even if it won't "itself" reverse engineer a thing.
 
It will say "I can't do this, but I can help you on this RE engine because it's your software and you'll be the one using it."
 
And then I can put qwen 3.8 flash next inside of it, and RE anything.

## C540 — Connect_Ad791
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwu8lsmz89w/

ooh, what uncensored model are you using? is it good? I've found a lot of quants to be trash before I found a good one, and I'm afraid to waste time on another lobotomized model.

## C541 — FragmentedHeap
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwuy5osbr8g/

I run this one, on an AMD r9700 32GB gpu with 128gb of ram and 2tb nvme on a 7950x cpu using the Strata Engine
 
 [https://huggingface.co/orcarouter/Qwen3.8-Flash-Next-Uncensored] https://huggingface.co/orcarouter/Qwen3.8-Flash-Next-Uncensored
 
Strata ->  [https://github.com/niko1221/strata] https://github.com/niko1221/strata
 
I get about 70 token/second with concurrency with near 3k token/sec prompt prefill.
 
Yeah, it's pretty good. It thinks a lot, but it gets the job done.
 
I use an iq4s quant of it, it's not bad for what it is, it will get work done, it just thinks for so long. It passed by "make me a tetris game" benchmark, it just took it 2-3 hours where claude opus 5.5 did it in 20 minutes.
 
If you have two r9700 32gb gpus you can get it to run 4-8 concurrent at 65 token/sec each on output decode (where it thinks). But it will use a LOT OF RAM, I will be reorganizing my ram for it soon and it'll have 192 gb DDR5 and I'll put the 128 in my main desktop instead.
 
CPU is very important, because when it cache misses it has to do those calculations on the CPU, so 3d vcache and AVX 512 is very necessary. Also ram speed is important, you want your RAM to be as fast as possible. I overclock the shit of my ram, max stable configuration. Ideally you want to run 2x64gb ddr sticks at like 6300 mhz and have a gen 5 nvme, but you're really just chasing 5%.
 
It runs really good at 128 on 4x32 gb sticks and a gen 4 nvme.
 
The CPU and the GPU is the primary thing, you need a fast CPU and a 32gb GPU and the faster the memory bandwidth is on the GPU the better.
 
r9700 > intel b70 32. But a 5090 is the GOAT at this but they're $7500, r9700 is $1800, b70 32 is $1300.
 
2 x 4090s is also faster, but they're $2500 each. 2 3090 ti's isn't worth it, r9700 is better than 2 3090s.
 
Also you can use 16gb gpus, so two 5080's will smoke an r9700 because 5080s are fast.
 
5070 ti super also good, but you need 2, but not that much better than an r9700
 
And 2 r9700's opens up a lot of options because then you have 64gb vram for parallization.
 
Buying the gpu with the most vram is really the best move.

## C542 — OneInspection927
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwuhs9l4hi8/

Ha, I just did the same thing

## C543 — Zenoran
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwq5tgvy7qa/

Shhhh let them live in their fantasy.

## C544 — Badger-Purple
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm5vk1sujp/

Why did you only get a 24GB GPU to offload real inference tasks to a model that is natively 27B dense, and therefore occupies at least 27GB without context at half precision? It makes no sense. Sonnet 5.5 is a couple hundred billion parameters, and likely not being served at whatever low quant you are using to get 128k token context on 24GB.

## C545 — JMowery
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwn2cj1wgww/

You're doing it wrong. I've had it reverse engineering complex things and coding without issue. Doesn't always get it right the first time, but it gets it done.

## C546 — sQeeeter
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rws6rvxr7ad/

What’s a dick tax?

## C547 — UnrealizedLosses
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwsd80nb63p/

Ask your mother

## C548 — Appropriate-Fun-3313
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwvt19fx86d/

Not a chance he’s running that model on those specs.

## C549 — Hypnonotic
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwwct3qz89x/

Look up Strata, it loads more into RAM than VRAM.

## C550 — Appropriate-Fun-3313
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwwl7a4j1k0/

If he’s able to load it up, it’s moving slower than molasses. I’ve got better specs on my hardware and running a 70b model is a joke.

## C551 — Hypnonotic
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwx6nm5b82p/

Strata loads the experts into vram and the rest of the model in ram, so the heavily utilized parameters are the ones on the GPU. You need 64gb of RAM and 16gb of VRAM to run it effectively. but 32 and 12 is the minimum. It's pretty slick, try it out.

## C552 — Appropriate-Fun-3313
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx28ebnulcy/

I’ll definitely spin it up. I don’t mean to sound overly skeptical, but that kind of performance hasn’t been my experience thus far. Happy to be proven wrong.

## C553 — Ramona00
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx7gyphvdes/

I was skeptical too. But man. Strata is pwoerfull, fast, and sooo good on gaming hardware that I've never experienced before.

## C554 — Canadian_Border_Czar
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwsqf74owip/

How long does it take your setup to respond even once? Cramming a Flash Next quant on 12 GB is bonkers, and your context even more. 
 
I have way better results by dropping to Qwen3.5-9B. w/ the 7 GB Q5 quant you can still fit the 65k context window and the entire thing runs on GPU VRAM.

## C555 — sudden_aggression
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpe23k5ode/

I find that qwen 3.8 27B fills up context rapidly and it's unhappy with less than 200k. It's also harder to configure for good performance than 3.6 27B (I can't seem to crack 50 tps, which was easy on 3.6) That being said, I've gotten it to iterate on coding tasks just fine.
 
My setup is
  
My setup is Qwen 3.8 27B on R9700 32GB, spent days playing around with settings, ended up with 300k unified cache, 256k per slot (this allows hermes to run cron jobs while the main session codes). I have used 3.8 with session sizes down to 200k with success but 128 is just bad. 
 
Q8_0 K cache, Q4_0 V cache. I feel this helps with reasoning strength noticeably. I was running Q4_0 for both previously.
 
orchestrated via hermes. basically a vanilla config but I gave it firecrawl, camofox and searxng as well to help it do research
 
I gave it a gitea instance to save its work to, gave it a sandbox to run stuff in and it blasts along fine getting shit done. I've been giving my current config real world coding tasks for maybe a month now. Previously I used 3.6 27B with a bunch of different settings. 3.8 seems slower but smarter.
  
edit- you're using fucking ollama? get the fuck outta here, switch to llama.cpp
 
no seriously, do it now

## C556 — Own-Buy8294
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpl70k6vtu/

We could sit here and give you advice on how to make it run better or you can just pay eight dollars get the lowest subscription of Grok Bot for a month and tell it you want your model to improve its coding ability and it will go through all your settings and set everything up for you. You’re welcome.

## C557 — RemainAbove
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpsu3jn2ch/

This is the real answer. Even the 20 dollar claude code for one month would be more than worth it to get a running worth anything. Im about to do it move from ollama

## C558 — FragmentedHeap
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwqwb07bcf6/

You built the wrong thing.
 
You want Dual (2) amd R9700's, and you want to run Strata with Qwen 3.8 Flash Next, and you want 192 gb DDR5 (4 * 48 gb), not 32gb.
 
Qwen 3.8 27b is a Dense model and it does not fit on a 24gb gpu without being heavily quantized, which costs extreme amounts of precision, it's crap when it's quantized.
 
Qwen 3.8 Flash Next is an MOE model and Strata can hot load experts on the 2 r9700 gpus and handle 2-8 concurrent sesisons at 60+ token/sec on each session, but needs a lot of RAM because the rest of the model stays hot in ram, and you need cache ram for the extra concurrency.
 
That CPU is also garbage, you need a FAST cpu with 3d vcache and avx 512, like a 9950X3D.
 
Do not waste your time with 24gb vram for LLM's, get serious, get an r9700 or a b70 32 (amd has better support with rocm). And 2 is better than 1.
 
Ideally you want 4 * r9700's and you run them in a thread ripper with 256gb of ddr5 rdimm with 4 x 8x 5.0 pcie slots... But rdimm is crazy expensive, and it will cost you $40k to build.
 
Also, you should be using AI to help you set this up, you will never catch up or stay caught up without using AI to help you, this whole setup will be wrong in two weeks, space changes fast af. Qwen 4 is dropping soon.

## C559 — Iajah
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx36rin46u8/

Qwen 27b will get pretty much any job done, given enough time, albeit with more hand holding than Sonnet. Though OP hardware can't run it properly I reckon. Single RTX6K is still needed.

## C560 — NonAwesomeDude
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwrrwy12tgg/

Its definitely your setup. Tbh I trust Qwen 27b more than any claude model.

## C561 — OkMaintenance9799
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rws8qx4b2qt/

Try  [https://github.com/Niko1221/Strata] https://github.com/Niko1221/Strata with qwen 3.8 flash next

## C562 — Qorsair
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwt1tj77rmt/

The hard truth that most people here aren't going to admit is commercial models absolutely crush local setups for actual coding agents.
 
I have priced this out thoroughly and frequently. I currently spend about $45/mo total on API access, using models like Gemini for orchestration and Claude for planning and Muse for adversarial review, and I never hit a cap. When you calculate the upfront cost of the multi-GPU system required to run a local model with comparable speed and reasoning, the breakeven is maybe five years if you don't include the cost of power. And by then, the hardware is beyond obsolete.
 
In your case, with a single 3090, you're forced to choose between castrating the model's reasoning with quant or restricting it to a tiny context window. Local models are fun for tinkering and learning, but if your goal is productive and efficient software development, there's no world that cloud inference doesn't pay for itself. If you're concerned about privacy, use a good cheap ZDR platform like Deepinfra or Openrouter.

## C563 — kirbyfanner
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwt3enmmfmr/

I'm using LM Studio and feel similarly. I have a lot of issues running it.
 
For the harness I'm using VS Code GitHub Copilot BYOK. My GPU is the 32gb R9700.
 
It's running very fast, the time to first token is near instant, but it seems to fail often and hallucinate/death loop a LOT. It works okay in LM Studio directly, but not great.
 
Q6 Quant, 128k context window. K and V cache are Q8.
 
Any tips specific to that setup? Thanks y'all.

## C564 — SSarrrrrrrrrr
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwvywa8v82r/

Using copilot what do u expect 😂

## C565 — FudgeEducational2038
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1flzonauc/

The funny thing is it's actually the other way, the quantization of these models are actually not a problem, they are quantized aware trained. You can compress them all the way down to q3_xxs with less degradation then you would ever think. 
 
The problem is that these models are sparse attention and linear attention and extremely extremely incredibly sensitive to KV noise especially when the model itself is compressed. 
 
I run q3_xxs but fp8 precision (which is way better than q8/int8)

## C566 — Savantskie1
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwy395eqh0k/

3090 with 120gb of vram? Yeah right. Nice lie lol

## C567 — Creative_Bookkeeper9
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwy4q7jl7z8/

Read that again... I said RAM, not VRAM...

## C568 — Educational-Row-6782
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwwudvnhllw/

Those cloud models run on like 100k of hardware, is impossible to get the same results with a 3090.

## C569 — Turbulent_Office1340
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwxqjg0a5k3/

Use unsloth studio..and keep it up to date.. set this parameter.. Temperature: 0.6 Top P: 0.95 Top K: 20 Min P: 0.0 Presence penalty: 0.0 Repetition penalty: 1.0 Context: fino a 256K (se la RAM regge) Quant consigliata: UD-Q4_K_XL
 
Modello: unsloth/Qwen3.8-27B-GGUF. 
 
If you whant a better model use use : DavidAU/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF

## C570 — jjcsea
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwys2zg7t0h/

sorry but a 3090 and 32GB of memory just aren't a valid setup for running local LLMs. try a 5090 and 64GB ram. or even an architecture with more shared memory.

## C571 — alonsojr1980-retry
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx0pm7jjtes/

The main problem of the smaller models is the inability to create comprehensive plans. Use the more capable models for that. Use the less capable models for the execution and tool calling.

## C572 — sod0
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1p246wy3o/

Qwen 27B creates great plans. Not using them is a bad idea.
 Sure Opus is better but I think it reaches Sonnet-level.

## C573 — sultan_papagani
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx29mvkwgbn/

who could have guessed a 27b local model is shit compared to sonnet 5.5 🤷‍♂️

## C574 — Gullible-Monitor-997
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3e9bvj1r4/

Il tuo problema non sembra hw ma solo un problema harness o comportamento agentico da rivedere ti consiglio di vedere little-coder sicuramente migliora dal comportamento standard

## C575 — Hunterxmalaa
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx7aazexg9t/

I genuinely do not understand people who do this 
 
Why do you assume a 27b model is going to outperform or keep up with a frontier model like Claude ? 
 
There is a reason these models at hinders of billions to trillions of peramiter 
 
Your being extremely unrealistic if your think qwen 3.8 27b is going to outperform proform sonnet 
 
Maybe if you ran the model at q8 or bf16 and your tok speeds was still fast maybe but your lowering its quant to get achievable speeds means your father reducing its already limited intelligence just for useage so yes it will forever be dumb

## C576 — ldn-ldn
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx81ggfil5x/

Qwen is useless for serious coding. People who praise it are slop generating kids.

## C577 — Pixelplanet5
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx81o9s2v8i/

yea thats normal, the "tests" of people you see where it works great are done on high end hardware or simply only do a thing or two before stopping.
 
Thats the big problem with local LLMs, no matter how good and compact your model is, if you dont have a TON of ultra fast memory for the context window it doesnt matter what the model is capable of.
 
thats why even all these 128GB unified memory AI dev boxes are kinda meh in the real world, sure they can load a model but then theres barely anything left for the context and on top of that they are slow.
 
the first usable thing will probably be the Ryzen AI 495+ with 196GB of unified memory.

## C578 — PhilippeEiffel
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx86hp2sk2p/

1) There are missing information in your post: model quant size? KV quant size? which harness?
 
2) Read this:  [https://sleepingrobots.com/dreams/stop-using-ollama/] https://sleepingrobots.com/dreams/stop-using-ollama/
 
3) You want to use model with native size of 54 GB. You need some extra memory to hold the KV cache. You bought a machine without enough RAM to hold this. The model is damaged by the quantization up to the point it is dumb.
 
The good way to go: use the model with the native quality (BF16 size for model and KV cache), then reduce the size step by step (this improves the speed and the available context size) while the quality matches your needs.

## C579 — Affectionate_Ripper
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx8qv9gb3j8/

I would recommend that you use models from this guy  [https://huggingface.co/bartowski] https://huggingface.co/bartowski

## C580 — FiringNerveEndings
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxk5v26p6ea/

A quick sanity check. I'm your entire post you haven't mentioned the agentic harness at all... Are you using one? Or are you straight up making calls to the Internet engine. Claude requests go through Claude code that adds system prompt, the LLM knows the cwd, it reads the AGENTS.md file(do you have one?)
 
All these can be crucial differences. 
 
Disclaimer: I don't run my own local model, I'm currently experimenting on the agent/harness level.

## C581 — majmichu
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxk3btu7f6p/

Try another harness, I am building myself a harness exactly for this purpouses its called Local Quench, and I have designed it to help local models finally be able to do something, and also would appreciate someone else's point of view on my project as it is work in progress. Localquench.com
 
And setup in my oppinon is very good, try to not go lower than q4km or nvfp4 on this model as he will start more to loose precision and falling in loops. Depending on your engine you can set the quantization of KV cache you can put it at q8_0 no problem (I use myself even q4_0) and it will fit almost twice as much context.
 
Qwen 3.8 27b is somewhat a frontier local codign model, I am using its VERY quantised version the bonsai 2 27b, because I have just 8gb of VRAM and yest its sloe for me but it really works, the most matters the harness around so the tools like, opencode, open hands, claude code, codex, this matters more than the benchmark itself. You can have amazing model but if you will give him 30k tokens of instructions of system prompt he looses 1/3 of the context and sooner will drop quality too, and the tools need to be easy for it to understand and work. Try the harnesses designed for smaller models. You can try mine, and I will be very happy tk hear your feedback or other like aider (never liked it too much) but heared a lot of good things about i believe its called tiny swe agent? And open hands, but this one has a big system prompt at the beginning

## C582 — airdumb
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxk0ojenfz7/

that’s weird , i’m building full web apps and managing infra with a single RTX 5060ti 16gb vram + Qwen 26b 3bitd EXL3 server

## C583 — AutomaticDriver5882
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxi6tzreoiq/

Not enough gpu buddy. You are trying shove a square peg into a round hole. It was until I stitch together 6 GPUs together until I got something on par with opus 4.6. I know it doesn’t help you but just my personal experience I run qwen flash next at 8 bit

## C584 — B1g_BuddhAH
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxadg5p70de/

who said i'm using it for coding? take your pride and swallow it.

## C585 — alonsojr1980-retry
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxihf4owrdt/

Do this very easy test:
  
Ask Qwen 27b to create a plan for developing a given app.
 
Use the exactly same prompt on Sonnet 5.5.
 
Get both results and ask Opus 5.5 to analyze both and score them against each other.
 
Come here and apologize.
  
The only way they can match is if your initial prompt is too shallow and the app's requirements are too little.

## C586 — alonsojr1980-retry
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxicbp5399f/

It doesn't come near, dude. But suit yourself.

## C587 — kirbyfanner
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxjjwn4mpia/

Oh is it a bad harness? I use it for frontier models a lot and generally like it, but I'm open to change. What do you run?

## C588 — AutomaticDriver5882
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxibdl8061u/

I wonder what the TPS is

## C589 — Smooth-Television-48
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxewcjcvvs5/

Something you dont have to worry about.

## C590 — MarcusAurelius68
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxcdq4fa8x0/

Both Strata and Radiance are ways of serving up Qwen 3.8 Flash Next. In the case of Radiance, which I use, it packages up everything including the quant.

## C591 — n4ru
https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx9hkpmcdr6/

why would this matter in this case?