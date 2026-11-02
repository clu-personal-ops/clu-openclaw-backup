## 7. Source-question registry

This registry conservatively includes every qualifying source comment containing a question mark or indexed as a question/request. Full source bodies are quoted, so rhetorical questions and ambiguous pronouns are not silently reinterpreted. It is a preservation registry, not a list of proven unanswered technical facts. OP+C486 answer the engine name (Ollama) and say the harness is unsettled; many other responses provide suggestions without a verified resolution. No parent IDs are available to prove reply relationships. The index assessment lists remaining gaps.

### C004 — JesusIsMyLord666

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlttl8lxuq/) · [Index assessment](#c004)

> Why not unsloth?

**Remaining questions / verification:** Unsloth Desktop, quants, or another Unsloth component?

### C010 — amadeo681

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwl2pfe3s0y/) · [Index assessment](#c010)

> What are the steps for the jump

**Remaining questions / verification:** No complete migration sequence demonstrated in this exchange.

### C013 — InfiniteBlink

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpu69a5y8y/) · [Index assessment](#c013)

> Is it worth exploring vLLM if I have two 3090s (ones a TI). Lamma.cpp has been pretty good so far with optimizations.

**Remaining questions / verification:** What workload/concurrency or performance gap justifies changing?

### C017 — daft_knight

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnjmf1cd5u/) · [Index assessment](#c017)

> Is there a big benefit in jumping from lmstudio to llama.cpp?

**Remaining questions / verification:** Starting product is obscured; benefit remains unresolved.

### C030 — SDdrums

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwrxs6o7cf7/) · [Index assessment](#c030)

> Newbie here. What is the better option?

**Remaining questions / verification:** Better by accuracy, usability, memory use or speed?

### C039 — Abject-Kitchen3198

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1o132uso0/) · [Index assessment](#c039)

> What's the big difference?

**Remaining questions / verification:** No controlled answer in this comment.

### C043 — NarutoX666X

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlkyh7cae8/) · [Index assessment](#c043)

> What's better ?

**Remaining questions / verification:** Improvement criterion and actual setup unspecified.

### C046 — HolaUsername

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk2ubdhnkx/) · [Index assessment](#c046)

> What quant?
>  What temperature/model parameters are you using?
>  
> What harness?
>  
> What engine and settings?
>  
> There's a lot of information you left out that could contribute as to why it doesn't work. Personally never had any issues with 27b at Q6 other than it contemplating the meaning of life during every task. It's no claude, but it does get the job done.

**Remaining questions / verification:** Exact OP values, engine build and representative failing trace remain missing.

### C047 — superbiche

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlnutsmyzn/) · [Index assessment](#c047)

> This. The fact no quant or sampling is mentioned, or that harness are thrown at the wall to see what sticks, makes me wanna write "skill issue" but I won't write it. 
>  
> Wait.. ..
>  
> NGL I'm just wondering but do you guys use a single box with 3.8 27B at ~128k ctx with multiple people ? 
>  
> Do you know even one single instance of this exact same Qwen would probably be able to tell you "what you're doing is a straight road to failure"?

**Remaining questions / verification:** Concurrency is questioned, not established.

### C060 — Bagelsarenakeddonuts

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwjsxppu0f4/) · [Index assessment](#c060)

> I have used qwen 3.8 27B for many tens of thousands of lines of Rust using a 5090. This code has passed tests and been reviewed by other LLMs (opus, fable) and it seems solid. I use the "swift" version of it to drastically cut down on thinking, with a great deal of success.
>  
> There is no better model in a similar size range. The next up is probably flash next, or GLM 5.3 flash, or mimo flash or deepseek v4.1, all of which are many times larger, but MOE so there is that if you have RAM.
>  
> Sounds like a harness or quant issue?

**Remaining questions / verification:** Exact Swift artifact, test suite, failure/repair rate and runtime not given.

### C061 — InfiniteBlink

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkp1yk23kx/) · [Index assessment](#c061)

> I've got qwen 3.8 27b Q8 running on dual 3090s tensor splitting the model. Im trying to figure out the best way to use it for coding. Im just starting to figure out whether to use codex/Claude to design the app then have Qwen do the grunt work, then review it. 
>  
> Do you have any suggestions on how best to use my local setup and both frontier models? I mainly use my setup with a Hermes agent for controlling home automation stuff, networking, downloading stuff, and other creature comforts. Im barley using its capabilities...

**Remaining questions / verification:** What delegation workflow works and what token/time savings result?

### C063 — InfiniteBlink

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwllh5zhr4z/) · [Index assessment](#c063)

> Interesting. Has it cut down significantly on your token usage?

**Remaining questions / verification:** No numeric before/after accounting.

### C065 — Dubious-Decisions

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2ugj0vlia/) · [Index assessment](#c065)

> Curious how you have copilot configured so it will consistently use the local model as a subagent while using Opis driving the main session. The copilot settings (in the UI) seem to be either a single model or auto and auto never picks the local model.

**Remaining questions / verification:** Configuration answer unavailable in this accessible exchange.

### C067 — hotmerc007

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm337hwdr7/) · [Index assessment](#c067)

> Would you be able to provide a little more info on your specific config for newbies. Seems like you have locked in a solution and I’d love to replicate. Many thanks for any further input you can offer!

**Remaining questions / verification:** Later pointer exists, but exact full recipe remains incomplete.

### C069 — Apprehensive_Stop314

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwjsld6nj50/) · [Index assessment](#c069)

> What model quant exactly, via what engine and with what settings are you using?

**Remaining questions / verification:** OP has not supplied these in the available original post.

### C072 — Abject-Kitchen3198

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1lwdh42hs/) · [Index assessment](#c072)

> Is the effort needed still lower than coding manually? Explaining things in enough details to a junior so he can just translate them to code adhering to our practices, and then checking it and correcting it, is often more work for a senior than doing it himself.

**Remaining questions / verification:** Human time saved versus direct implementation remains unanswered quantitatively.

### C075 — Express_Quail_1493

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwoqd3a6isj/) · [Index assessment](#c075)

> enters repetitive loops is the bigest sign that its might be your config. Most modern qwen27b rarely do this anymore older qwen suffered from this. newer ones thinks for very long yes(without a switft finetune) but newer is often always a coherent chain of thought dispite being long sometimes. maybe chat template issue? or harness not set to the correct token streaming ETC???
>  
> Edit: also if you are just starting out and having issues linking your harness to the infernce then
>  
> LMstudio-Bionic is a good start. a LOTTT better than ollama. they've done the hard work of connection for you. when u get more comfortable u can get the Raw llama.cpp or something else.
>  
> lol good colleagues dont allow another to use ollama. throw it in the bin. 🚮😂
>  even your qwen27b can setup other infrence engines for you once u get Bionic installed. i used my LMstudio+qwen to setup my own llama.cpp and then ditched him afterwards

**Remaining questions / verification:** No trace shows template/streaming error; distinguish long coherent thinking from repetition.

### C082 — colonelx_

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2kurtuk6c/) · [Index assessment](#c082)

> Could you share your hardware specs? Also, which coding agent are you using?

**Remaining questions / verification:** No reply linked by parent metadata in Atom.

### C083 — Pablo_the_brave

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6zhpttmzn/) · [Index assessment](#c083)

> You didn't even post your model parameters (temp, top_p, etc.) or what LLM server you're running. That right there tells me everything about why you guys aren't getting good results. Honestly, I don't even feel like reading the rest of the post without that info. All I'll tell you is: you've got the model, you've got its parameters, and then agent setup is just as critical. There's a ton of useful info right here on this sub—just use the search bar.

**Remaining questions / verification:** Missing values still prevent causal attribution; dismissive tone adds no evidence.

### C090 — former_farmer

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwjvpbzay79/) · [Index assessment](#c090)

> Which quant and thinking mode?
>  
> Thinking mode needs to be xhigh. Quant ideally q6 or higher.

**Remaining questions / verification:** Conflicts with lower-thinking successes; must ablate on task/time budget.

### C092 — LegitimateCopy7

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnvfaelg2p/) · [Index assessment](#c092)

> RTX 3090 24 GB VRAM
>  
> Qwen 3.8 27B (128K context)
>  
>  
> getting a bit greedy here are we? either the model overflowed to system RAM or you're using a heavily lobotomized quantization.
>  
> Don't use Ollama if you're expecting a tool and not a toy. other inference engines may need various levels of tinkering and troubleshooting but they're the better paths to make use of the limited hardware resources you have.

**Remaining questions / verification:** Overflow would primarily affect speed; corruption/quality cause not demonstrated.

### C093 — soulman901

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwo8dn4e6xt/) · [Index assessment](#c093)

> Not sure what’s going on but I’ve been able to get it to complete programming tasks for me. I’m on an M4 Pro 48GB and got it to make me a couple of games, like this Pac-man clone 
>  
>  [https://preview.redd.it/6d4tigsxipyh1.jpeg?width=3024&format=pjpg&auto=webp&s=40e86ed554550c9f6c0d740e6b8401091efc660b] https://preview.redd.it/6d4tigsxipyh1.jpeg?width=3024&format=pjpg&auto=webp&s=40e86ed554550c9f6c0d740e6b8401091efc660b

**Remaining questions / verification:** Screenshot not inspected; tests and exact model settings absent.

### C095 — Number1OchoaHater

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwjoz6t5h2c/) · [Index assessment](#c095)

> lets start with saying that 27b and sonnet are not in the same league, said that, what harness and inference engine are you using?

**Remaining questions / verification:** No actual OP harness or comparative evidence.

### C096 — wegster

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkedh17hr6/) · [Index assessment](#c096)

> What Quant? Get off of ollama. Use Strata, ideally get a bigger card (more VRAM), but look for one of the dynamic/mixed precision Q4 quants. Check thinking and temp settings. QFN beats it but 27B Dense can be pretty competent, close or same as QFN in real-world benchmarks on real repos I'm doing (~100K LOC so reasonable but not enormous), and my QFN generally runs neck to neck with sonnet.
>  
> Try using a simple harness like pi - I've had cline nearly self-destruct in some tests, but pi so far, literally beats them all.

**Remaining questions / verification:** No artifacts or task definitions; repository LOC is not context occupancy.

### C097 — Oli_Luck

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwl16mys6n4/) · [Index assessment](#c097)

> Hello,
>  
> If you want people helps you - help them first with the things that matter:
>  - Quant ?
>  - KV Cache quant
>  - temperature
>  
> these are the most obvious.
>  
> Then : you cant just switch from a frontier model to a local one w/o preparing the terrain.
>  A frontier pone will be able to plan and code "on the fly" - a local one need structure:
>  - planing features to local help files
>  - chunking the job in small logical steps
>  - being reviewed by an "auditor" ( same llm but another role ) 
>  
> Just explains what you tried to do in which context, they you will get reliable answers

**Remaining questions / verification:** Exact inputs/settings and independent evidence still absent.

### C100 — mozillazing

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwqy3w046n6/) · [Index assessment](#c100)

> you've got a 125b model running with 262k context on 12gb vram and 32gb ddr5 system ram? what the hell am i doing wrong lol

**Remaining questions / verification:** What storage/offload architecture and real workload performance make this viable?

### C102 — Smooth-Television-48

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwru2sget2c/) · [Index assessment](#c102)

> Would be heavy disk tax. Hopefully its just reads and they down burn out their ssd

**Remaining questions / verification:** Reads versus writes and actual wear are not established; do not imply reads exhaust write endurance.

### C103 — curiouselectron

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwp94xret9f/) · [Index assessment](#c103)

> What rates do you get for this?

**Remaining questions / verification:** Need prefill, decode and task wall time, not only nominal fit.

### C104 — yourself88xbl

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpv0qg2dut/) · [Index assessment](#c104)

> What are your main use cases. Have you been using it for code gen at all?

**Remaining questions / verification:** Coding applicability remains unclear for the cited configuration.

### C109 — Dracuvlad

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwyor0r0p7m/) · [Index assessment](#c109)

> i am trying to run this on my macbook pro m1 max 64gb 1tb. can you please share with me what is your setup and how is it performing for you right now?

**Remaining questions / verification:** Configuration is partly answered at C110; quantitative speed/success remains missing.

### C114 — caylyn953

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwyteph4omb/) · [Index assessment](#c114)

> OP definitely needs to set their expectations at the right level. Because a single 3090 won't even be able to reach Haiku 5.5 level of quality!
>  
> Maybe by this time next year it will be? Maybe.
>  
> But by that point in time they'll be expecting Sonnet 7.1 or whatever such level of performance. Which won't be happening.

**Remaining questions / verification:** No task-specific measurements; future comparison is speculative.

### C117 — rkcth

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk8m8e88f5/) · [Index assessment](#c117)

> You don’t have enough system RAM to run strata, and you don’t have enough VRAM to run a proper quant of 27b what is the full name of the model you are using? LLMs are best run in systems with lots of RAM, the more, the better. Your system uses DDR4, you can grab 2x32GB kit for $300ish. Do that then install Qwen 3.8 flash next on strata using the 3 bit quant. If you want to go extra smoothly, install 4x32GB sticks.

**Remaining questions / verification:** No measured OP allocation; RAM price/platform capacity and model fit not verified.

### C119 — Longjumping-Road4113

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwojejtbf6p/) · [Index assessment](#c119)

> Have you tried strata ? The Moe option with specifically optimised Qwen coder?

**Remaining questions / verification:** Exact model/artifact and resource requirements unspecified.

### C120 — Emergency-Quiet3210

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxf578ergkj/) · [Index assessment](#c120)

> What harness are you using? I find qwen 27B is mode then enough for most coding tasks. Unless I’m vibe coding and expecting it to one shot a data pipeline I don’t really need frontier models. 
>  
> Try out LM studio + Pi harness or even opencode. I like Pi because it’s lightweight and uses less RAM

**Remaining questions / verification:** No measured prompt overhead or coding suite.

### C123 — skifreek

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk0vrcznol/) · [Index assessment](#c123)

> I am running into exactly this problem. So far I have been tweaking context size settings and thinking level. I set 32KB context window with my 32GB of VRAM (I would expect the model to run slow for you with 128K context as you run out of VRAM). Also I changed the thinking level from extra high to medium to try and avoid these endless thinking loops.
>  
> I haven't found the magic recipe yet and I am pretty frustrated so far. What are you using for inference and coding? I have been trying LM Studio and opencode so far.

**Remaining questions / verification:** No recipe found; actual weight/KV quant, template and failing trace missing.

### C129 — overand

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwln8fnnnol/) · [Index assessment](#c129)

> You should consider using llama.cpp rather than LM Studio, but:
>  
> What quant (and whose quant) are you running?
>  
> I've had really great luck with 27B for coding, on a system with 36 GB of VRAM, so pretty close!

**Remaining questions / verification:** Hardware exceeds OP's and no artifact/test results supplied.

### C132 — Kmic68

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk1ojxlrc0/) · [Index assessment](#c132)

> What quant, do you have a harness (pi, deepseek, etc?), what kv quant, is your temperature and other settings that effect output default?, what reasoning level? 
>  
> These all determine your answer. I have a lot of experience in this and have worked with 27B extensively.

**Remaining questions / verification:** Exact OP values and examples still required.

### C134 — FerretBoom

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkhpnkl4m8/) · [Index assessment](#c134)

> Please post one of your prompts that the Qwen model receives
>  Claude has a caching and ,rag pipeline, all kinds of proxies to route to hot zones, enough compute to retry requests, do internal unit testing. While you are querying against the model directly, which is way different .

**Remaining questions / verification:** Claims about proprietary internal serving are unverified and not used as fact.

### C138 — IsaacLevinsky

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwo1fnlgwps/) · [Index assessment](#c138)

> Please post the quantization and runtime you are using and any other details. The quantization and runtime matter more than people realize it but once you get deep into it they matter more than anything else

**Remaining questions / verification:** No actual settings or task evidence.

### C139 — MLisdabomb

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwplrq6drj6/) · [Index assessment](#c139)

> Came here to post this - OP please share the exact quant and how you are serving it. Your experience with "can't complete basic coding tasks" is so strange compared to my experience with this model that I feel it is likely a configuration issue

**Remaining questions / verification:** No setup or task-matched evidence proving configuration cause.

### C144 — outdoorsgeek

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwtk7aojzj5/) · [Index assessment](#c144)

> Yes, you aren't running this optimally right now and will get better results if you use the right inference engine and harness with good settings.
>  
> With that out of the way, you need to be honest with yourself on whether or not you’re willing to step back roughly a year in model capability from Sonnet 5.5. Remember Sonnet 4.5? A 256k context model that was decent at a single small task if you wrote out very detailed specs or had opus do the planning? That's about the peak of where you will be able to get with lots of work and tuning. It will be nowhere near the fully autonomous loops you are likely running with the current SOTA models.
>  
> I would tell you that your hardware is the problem and you need to be more serious than a 6 year old gaming PC for professional coding work, but the truth of the matter is that you'd have to spend an insane amount of money to get performance that looks like a modestly degraded Sonnet 5.5. Financially it's nowhere near worth it compared to paying the frontier labs. There are, of course, other reasons to run local, but seeing as you're running a business I imagine the ROI matters a lot.

**Remaining questions / verification:** No financial/task dataset; preserve possibility local is worthwhile for non-cost reasons.

### C147 — FudgeEducational2038

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1ck14t5sx/) · [Index assessment](#c147)

> The biggest things are that these models are not sensitive to quantization of the model very much, but they are extremely sensitive to Quant of kv. I am guessing you are running q4 or q6 kv precision?
>  
> What you need to do is go down to Q3_XXS by unsloth and then do fp8 precision if possible. Int8 is... Okay but fp6 is on par with q8/int8
>  
> Fp16/fp16 Fp8/fp8 Q8/q8
>  
> Don't go below that 
>  
> On a side note, you're approaching this wrong. What you should be doing is using strata to run 3.8 flash next GYRO S quant. 
>  
> It's going to give you better performance, while also running 60 or 70 tokens a second. It will run faster and have better performance all at the same time even at full precision.

**Remaining questions / verification:** Format comparisons and 'full precision' language are unsupported; need exact schemes and equal-budget ablation.

### C148 — Sad-Chemist7118

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxfcvlbcfxc/) · [Index assessment](#c148)

> I keep repeating myself in this subred but use Strata with a 272k context if you can. I have a 16 GB GPU (4080) and 64 GB RAM on a PCIE4 SSD and it runs somewhere between 70-80 toks and a very Claude-like ttft, also with a massive first prompt of ~50k tokens. Is it as good as Sonnet 5.5? No. Is it as good as Opus 4.5 from ~1 year ago? Yes.

**Remaining questions / verification:** Model implied from context, not explicit; timings/quality comparison unlogged.

### C160 — RawFreakCalm

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkiry31uap/) · [Index assessment](#c160)

> What’s your harness?
>  
> Mine runs fp8 265 context and has zero problem creating for me. Deepseek v4.1 flash does most of my ai agent work and then 3.8 27b my really long code tasks. I’ll give my small team a project and come back in a day. It’ll always be what I asked.

**Remaining questions / verification:** Hardware, task boundaries and validation missing; 265K may be shorthand/typo.

### C162 — Ell2509

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkofr91sbo/) · [Index assessment](#c162)

> My first question is, what quant are you using? Q4 on complex coding tasks will not be anywhere near as good as q8...

**Remaining questions / verification:** No matched trials; Q4 success reports disagree.

### C163 — GrungeWerX

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkw6gog2w3/) · [Index assessment](#c163)

> Ollama??
>  
> Lol, that’s your first mistake. Has a terrible reputation around these parts.
>  
> Next, would need to know your harness, because you’ll need one with Qwen. 
>  
> I’ll be back later with some suggestions…

**Remaining questions / verification:** A promised future reply is not available evidence.

### C174 — HenkPoley

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm8dsmzxk1/) · [Index assessment](#c174)

> How badly quantized is your KV cache? Keep it at 16 bit, or maybe q8_0.
>  
> Sonnet 5.5 is one of the most high end models. Qwen3.8-27B is near Anthropic/OpenAI lowest end recent models. Think Luna 5.6 / Haiku 5.5.

**Remaining questions / verification:** Exact OP KV unknown; relative ranking not sourced.

### C175 — FizzyDuncDizzel

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmahhpz3qd/) · [Index assessment](#c175)

> What agent are you using? The model has very little direction without an agent guiding it. 
>  
> Also that model really likes to talk to itself. Put thinking to low and have it hard stop somewhere around 20k tokens.

**Remaining questions / verification:** Hard cap may truncate valid reasoning; compare finish reasons and success.

### C194 — Choubix

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwow4bqx19d/) · [Index assessment](#c194)

> Done still need these? I have never used them. Benefit is better tool calling? Tks!

**Remaining questions / verification:** Unanswered in accessible exchange; depends on engine/model/template revision.

### C200 — laxative_surplus

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwrm3bg3btx/) · [Index assessment](#c200)

> when you say with optimizations, do you mean compiler optimizations?

**Remaining questions / verification:** Do the referenced optimizations mean compiler optimizations?

### C204 — MarketingOk3093

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx57enl6gm8/) · [Index assessment](#c204)

> Thats my hardware spec with 64GB DDR4 I was only getting ~20 t/s with Q6. I've since moved to Strata FN 3.8 IQ3 S aat 70 t/s. I would be really interested to see your Q8 27B Llama config...

**Remaining questions / verification:** What is the referenced Q8 27B llama configuration?; What exact GPU, context, offload, and timings produced each speed?

### C205 — hahayeahisit

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxcjtxx3t0l/) · [Index assessment](#c205)

> What should we be using instead ?

**Remaining questions / verification:** What should be used instead?

### C206 — Coach_Unable

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx8whv9khic/) · [Index assessment](#c206)

> Whats the advantage of using llama.cpp over lmstudio? I am using lmstudio as host server (different harnesses) and have specific settings i changed in lmstudio (kv quantization/context size) is llama.cpp worth it for the "low end setup" user (normal pc with single gpu)

**Remaining questions / verification:** What advantages does llama.cpp offer over the server named as ***?; Is changing worthwhile for a single-GPU low-end setup with configurable KV/context?

### C207 — HourLocation2038

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwtqs4gzixs/) · [Index assessment](#c207)

> Came to say this, OP hasn't told us anything about how he is running it.

**Remaining questions / verification:** What exact runtime, model artifact, inference settings, and harness does the OP use?

### C211 — InfiniteBlink

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnoy7kff6s/) · [Index assessment](#c211)

> When you say you split up instances I'm Qwen do you mean spawning sub agents? Does clause decide the sub agents tasks? Sorry I'm starting to dive deeper down the sun agent world.

**Remaining questions / verification:** Does splitting Qwen instances mean spawning subagents?; Does Claude decide the subagents' tasks?

### C213 — InfiniteBlink

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rworfqhmnq8/) · [Index assessment](#c213)

> Interesting, I've never heard of BMAD before. Im currently having Claude and codex review a simple game app. Im curious how do I leverage BMAD, should I include that in my prompt when I'm starting a new project. Apologies for the stupid questions, hopefully your answers help other folks as we go down the rabbit hole 😆

**Remaining questions / verification:** How should BMAD be adopted?; Should it be included in a prompt when starting a project?

### C220 — Blue_Eyed_Behemoth

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxcs1vesplx/) · [Index assessment](#c220)

> Doesn't swift have their own licensing? Just curious if you ran into any issues with that.

**Remaining questions / verification:** Does Swift have its own licensing terms?; Were any licensing issues encountered?

### C223 — Blue_Eyed_Behemoth

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxcmuj0gbkw/) · [Index assessment](#c223)

> Are you using 3.8 flash next coder? Mine still spirals. I'm running a RX9060XT 16GB vRAM w/64gb RAM. I feel like every time the context gets compressed it just removes important information and starts cycling.

**Remaining questions / verification:** Are you using 3.8 Flash Next Coder?; What context/compaction settings, runtime, and quant are involved?; Do compaction traces actually show loss of required information before cycling?

### C230 — Choubix

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwouxcjb6w5/) · [Index assessment](#c230)

> Hi! Did you one shitnthisno4 do you give it a large set of instructions and guardrails? I need to get my kids to start small on AI 😅. Tks!

**Remaining questions / verification:** Was it one-shot, or was a large instruction/guardrail set supplied?

### C239 — kirbyfanner

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwuli2ftlsz/) · [Index assessment](#c239)

> I have some questions about your setup, since I'm new to this.
>  
> Why did you turn vision off? Does that increase VRAM or speed?
>  
> How are you running a 125B model on a 12GB VRAM device, even with 32GB of RAM? My 27B takes up 27GB of VRAM and I imagine a 125B model takes up much more than that.
>  
> What is IQ3_S?
>  
> What are your tokens/second? I get 40t/s on 27B on an R9700.

**Remaining questions / verification:** Why turn vision off: memory savings, speed, or both?; How is the claimed 125B model run with 12GB VRAM and 32GB RAM?; What is IQ3_S?; What tokens/s does that setup achieve?; What quant/context/offload explain the commenter's 27GB 27B footprint?

### C242 — cagriuluc

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx4pkjqtp5v/) · [Index assessment](#c242)

> Have you tried FN as well? I am torn between the two but since FN is much faster on my setup, I use 27b only for vision

**Remaining questions / verification:** Have you tried FN as well?; What setup, quants, context, and coding-quality comparisons support using FN over 27B?

### C249 — flatfalafel

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxjigjd4nts/) · [Index assessment](#c249)

> Are you making that harness available/os? I have some projects I'm working on and can't use my employers developed harness for obvious reasons.

**Remaining questions / verification:** Will that harness be made available/open source?

### C251 — Omegaprime02

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm44e4hgo0/) · [Index assessment](#c251)

> If you're dead set on using LM Studio, try manually setting the KV to run on RAM, You'll see a speed drop, but not nearly that bad. You'll find it under load settings in the advanced options, set Offload KV Cache to GPU Memory to off, that way the weights are in memory at all times.
>  
> Edit: Looking at my files, which quant are you running? With 32GiBof VRAM you absolutely should not be overflowing. Are you running Q8?

**Remaining questions / verification:** Which quant are you running; is it Q8?; At what model, context length, KV precision, and batch/concurrency does 32GiB overflow?; Does CPU KV placement actually retain all weights on GPU and improve measured latency here?

### C252 — a_lost_shadow

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnlv6sn7oi/) · [Index assessment](#c252)

> What card do you have? With an RX6800 I'm getting around 35 tokens/s at 85k context fill. At 6 tokens/s, it sounds like you might already be partially offloading to the CPU.

**Remaining questions / verification:** What card do you have?; What model/quant/runtime and actual offload settings produced each speed?; Does telemetry confirm CPU offload at 6 tokens/s?

### C253 — Catch_022

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx4eejw3i5h/) · [Index assessment](#c253)

> Can I do any relatively simple coding offline with a 10gb 3080 or is that a pipe dream? Trying to do some basic python, kobotoolbox and r

**Remaining questions / verification:** Can a 10GB 3080 do relatively simple offline Python, KoboToolbox, and R coding?; What model, context, and harness fit that workload?

### C258 — Altruistic-Wolf-3938

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm0qnbw5gi/) · [Index assessment](#c258)

> 24+12?

**Remaining questions / verification:** Is the referenced configuration 24+12, and what devices/units do those numbers denote?

### C259 — yourself88xbl

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwq0d1rvxk0/) · [Index assessment](#c259)

> have you rean any sort of head to head comparisons for code generation against the cloud models?

**Remaining questions / verification:** Have any head-to-head comparisons for code generation against cloud models been run?; Were tasks, harnesses, prompts, attempts, tests, and budgets matched?

### C260 — Giuseppe_0112

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx9sc31yxep/) · [Index assessment](#c260)

> Couldn’t you just run codex with llama as the server? (excuse me if this question seems underqualified, I’m not a software engineer myself. Just wondering)

**Remaining questions / verification:** Can Codex run with llama as the server, and through which API/configuration?

### C266 — nfored

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlpft4i3l1/) · [Index assessment](#c266)

> What quant I got well over 128k context on a 32gb vram 100% gpu in Q4

**Remaining questions / verification:** What quant are you using?; Which Q4 model artifact, backend, KV precision, actual context fill, and memory logs support the claimed fit?

### C271 — _RemyLeBeau_

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnk3p91twj/) · [Index assessment](#c271)

> I like this idea, but I would be green I this area. Do you have a prompt I could use and learn from?

**Remaining questions / verification:** Is there a prompt example to use and learn from?

### C272 — FerretBoom

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwo3xy5u3kw/) · [Index assessment](#c272)

> Qwen 27B — General Coding Reasoning Benchmark
>  20 questions | 100 points | Closed-book | No code execution
>  Instructions for the model
>  Answer all 20 questions independently. Do not execute code, browse the web, or use external tools. For tracing questions, give the exact output. For implementation questions, give complete Python 3 code. Explain your reasoning briefly (1–3 sentences) except where code is required. Do not silently guess. Preserve requested time and space complexity. Number your answers Q1–Q20. Do not skip questions.
>  Q1 — Python aliasing
>  What is the exact output?
>  a = [[1], [2]]
>  b = a[:]
>  b[0].append(3)
>  b[1] = [9]
>  print(a)
>  print(b)
>  Q2 — Python closures
>  What is the exact output? How would you change only the lambda expression to capture each iteration’s value?
>  funcs = []
>  for i in range(3):
>  funcs.append(lambda: i)
>  print([f() for f in funcs])
>  Q3 — JavaScript event loop
>  In a standard JavaScript event loop, what is the exact logging order?
>  console.log("A");
>  setTimeout(() => console.log("B"), 0);
>  Promise.resolve().then(() => console.log("C"));
>  queueMicrotask(() => console.log("D"));
>  console.log("E");
>  Q4 — Exception handling
>  What is the exact output, and why?
>  def f():
>  try:
>  return 10
>  finally:
>  return 20
>  
> print(f())
>  Q5 — Complexity analysis
>  Determine the tight asymptotic time complexity and auxiliary space complexity, for n >= 2.
>  for i in range(1, n + 1):
>  j = 1
>  while j <= i:
>  j *= 2
>  Q6 — SQL and NULL
>  A table grades(score) contains four rows: NULL, 40, 50, 70.
>  What are the three returned values, in order?
>  SELECT
>  COUNT(*),
>  COUNT(score),
>  SUM(CASE WHEN score >= 50 THEN 1 ELSE 0 END)
>  FROM grades;
>  Q7 — Python iterators
>  What is the exact output? Modify the function so it returns the positive elements and the complete original sequence, even when xs is an iterator.
>  def inspect(xs):
>  positives = [x for x in xs if x > 0]
>  return positives, list(xs)
>  
> print(inspect(iter([-1, 2, 3])))
>  Q8 — Binary search debugging
>  The function should return the first index where a sorted array has an element >= x, or len(a) if none exists. Explain the bug and provide a corrected implementation.
>  def first_ge(a, x):
>  lo, hi = 0, len(a) - 1
>  while lo < hi:
>  mid = (lo + hi) // 2
>  if a[mid] < x:
>  lo = mid + 1
>  else:
>  hi = mid
>  return lo
>  Required cases:
>  first_ge([1, 3, 3, 5], 3) == 1
>  first_ge([1, 3, 5], 9) == 3
>  first_ge([], 4) == 0
>  Q9 — Mutation during iteration
>  What is the exact output? Then show how to remove every occurrence of 2 while preserving the identity of the original list.
>  a = [1, 2, 2, 3]
>  for x in a:
>  if x == 2:
>  a.remove(x)
>  print(a)
>  Q10 — Merge algorithm defect
>  What does this code output for the given input? Identify the bug and provide a correction with O(len(a) + len(b)) time complexity.
>  def merge_sorted(a, b):
>  i = j = 0
>  out = []
>  while i < len(a) and j < len(b):
>  if a[i] <= b[j]:
>  out.append(a[i])
>  i += 1
>  else:
>  out.append(b[j])
>  j += 1
>  return out
>  
> print(merge_sorted([1, 4], [2, 3, 5]))
>  Q11 — Stack algorithm
>  Implement valid_brackets(s: str) -> bool in Python. Recognize (), [], and {}; ignore non-bracket characters. All brackets must be correctly nested and matched. Use O(n) time.
>  assert valid_brackets("a{b(c)[d]}") is True
>  assert valid_brackets("([)]") is False
>  assert valid_brackets("]") is False
>  assert valid_brackets("") is True
>  Q12 — Interval merging
>  Implement merge_intervals(intervals) in Python. Each interval is a closed integer interval (start, end) with start <= end. Input may be unsorted. Overlapping intervals, including those sharing an endpoint, must merge. Return sorted merged intervals as tuples.
>  Example input:
>  [(5, 7), (1, 3), (3, 4), (8, 8), (7, 9)]
>  Give the result and an O(n log n) implementation. Empty input returns [].
>  Q13 — Directed graph topological sort
>  Implement topo_or_none(n, edges) in Python. Vertices are 0 through n-1. Each edge (u, v) means u must precede v. Return any valid topological ordering if the graph is acyclic. Return None if the graph contains a directed cycle. Include disconnected vertices. Target complexity O(V + E).
>  Q14 — Weighted shortest path
>  Given a directed graph with edges:
>  S -> A (2)
>  S -> B (5)
>  A -> B (1)
>  A -> T (7)
>  B -> T (2)
>  Find the minimum cost and actual path from S to T. Explain whether ordinary unweighted BFS always gives the correct minimum-weight path.
>  Q15 — Dynamic programming
>  Implement min_coins(coins, amount) in Python. coins is a list of positive integer denominations, reusable any number of times. Return the minimum number of coins needed to make amount, or -1 if impossible. amount is nonnegative. Do not use a greedy-only algorithm.
>  assert min_coins([1, 3, 4], 6) == 2
>  assert min_coins([2], 3) == -1
>  assert min_coins([1], 0) == 0
>  Provide time and space complexity.
>  Q16 — Sliding window
>  Implement longest_unique(s: str) -> int: length of the longest substring with no repeated characters. Use O(n) expected time.
>  assert longest_unique("abba") == 2
>  assert longest_unique("pwwkew") == 3
>  assert longest_unique("") == 0
>  Q17 — Prefix sums and hashing
>  Implement count_subarrays(nums, k) in Python. Count every contiguous subarray whose elements sum to exactly k. Input may contain negative integers and zeros. Target O(n) expected time.
>  assert count_subarrays([1, -1, 1], 1) == 3
>  assert count_subarrays([3, -1, 1, 2, -2, 2], 3) == 5
>  Q18 — SQL outer join
>  Tables:
>  users(id PRIMARY KEY)
>  orders(id PRIMARY KEY, user_id, amount)
>  Write SQL returning one row per user with:
>  ● id
>  ● big_orders: number of that user’s orders with amount > 100
>  Include users with zero qualifying orders. Sort by users.id ascending. Explain why filtering o.amount > 100 in a WHERE clause after a LEFT JOIN can give incorrect results.
>  Q19 — Concurrent read/modify/write
>  A shared counter starts at 0. Two threads each execute these abstract operations exactly once:
>  temp = counter
>  temp = temp + 1
>  counter = temp
>  Assume each individual read or write is atomic, operations from different threads may interleave, and execution is sequentially consistent.
>  What final counter values are possible? Give an interleaving demonstrating a lost update. Describe a correct synchronization solution.
>  Q20 — LRU cache design
>  Design an LRU cache supporting:
>  ● get(key) -> value, or -1 if absent
>  ● put(key, value)
>  ● fixed nonnegative capacity, including capacity 0
>  Both operations must take O(1) expected time. Specify:
>  1. Data structures used.
>  2. How get updates recency.
>  3. How put handles a new key.
>  4. How put handles an existing key.
>  5. How eviction works.
>  6. What happens when capacity is zero.
>  No full implementation required.

**Remaining questions / verification:** Q1: What do a and b print after a shallow copy of [[1],[2]], mutation of b[0], and replacement of b[1] with [9]?; Q2: What do loop-created Python lambdas print, and how can only the lambda expression change to capture each iteration value?; Q3: What is the exact JavaScript logging order for synchronous A/E, zero-timeout B, Promise C, and queueMicrotask D?; Q4: What does a function returning 10 in try and 20 in finally print, and why?; Q5: What are tight time and auxiliary-space complexity for the nested i=1..n loop doubling j while j<=i?; Q6: For grades NULL,40,50,70, what do COUNT(*), COUNT(score), and SUM(CASE score>=50 THEN 1 ELSE 0 END) return?; Q7: What does inspect(iter([-1,2,3])) return after consuming positives, and how can it return both positives and the complete original sequence?; Q8: What is wrong with first_ge using hi=len(a)-1, and what corrected lower-bound implementation handles duplicate matches, x beyond the end, and empty input?; Q9: What prints when removing 2s during iteration over [1,2,2,3], and how can all 2s be removed while preserving list identity?; Q10: What does the incomplete merge output for [1,4] and [2,3,5], what is its defect, and how is it corrected in linear total length?; Q11: Implement O(n) valid_brackets for (), [], {}, ignoring other characters and handling mismatches and empty input.; Q12: Give the merged result for [(5,7),(1,3),(3,4),(8,8),(7,9)] and implement O(n log n) merging of closed intervals, including shared endpoints and empty input.; Q13: Implement O(V+E) topo_or_none over vertices 0..n-1, including disconnected vertices and returning None for cycles.; Q14: Find the minimum cost/path from S to T for S-A=2, S-B=5, A-B=1, A-T=7, B-T=2, and explain whether ordinary BFS always handles weighted paths.; Q15: Implement minimum reusable positive-coin count, returning -1 if impossible, without greedy-only logic, including amount zero, and give time/space complexity.; Q16: Implement O(n) expected-time longest_unique substring length, including abba, pwwkew, and empty input.; Q17: Implement O(n) expected-time counting of contiguous subarrays summing to k with negative values/zeros, satisfying the supplied examples.; Q18: Write SQL returning every user and their count of orders above 100, including zero counts and sorting by user id; explain the LEFT JOIN/WHERE filtering trap.; Q19: What final shared-counter values can two sequentially consistent atomic-read/write increments yield, what interleaving loses an update, and what synchronization fixes it?; Q20: Design expected-O(1) LRU get/put, describing structures, recency, insert/update/eviction, and nonnegative capacity including zero.; What are the answer key, grading rubric, model/settings, repeated-run scores, and validated correctness of the benchmark assertions?

### C274 — boosnie

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxaxvib3jxd/) · [Index assessment](#c274)

> Silly assumption. I use Bold and Italic all the time.
>  If the editor supports ways to emphasize and make your message simpler to read and understand why not use it?

**Remaining questions / verification:** What evidence beyond bold/italic supports the assumption being disputed?

### C276 — colonelx_

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2cjsbmnc2/) · [Index assessment](#c276)

> Hey, can you suggest the best coding model for my hardware? I’ve got 10GB Vram and 64GB of RAM. I’ve tried Qwen models with Opencode, but none of them seem to work well. They take forever to think and reason through agentic tasks. I’ve also tried loading the models in LM Studio with different context sizes ranging from 8K to 200K, even with the Qwen 4B and 9B models.
>  Is there any hope for running a decent coding agent on a low end PC? 🥲

**Remaining questions / verification:** What is the best coding model for 10GB VRAM and 64GB RAM?; Is a decent coding agent viable on that PC?; Which versions/quants, actual context fills, hardware, and offload settings explain the latency?

### C278 — colonelx_

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxfsj7j265f/) · [Index assessment](#c278)

> Hey again, Since the Strata Windows app is just for chatting, should I use Strata through the terminal for agentic tasks and connect its API to OpenCode? Which approach would you recommend?

**Remaining questions / verification:** Should Strata be run through the terminal with its API connected to OpenCode for agentic tasks?; Which approach is recommended, and is the Windows app actually limited to chat?

### C281 — roiki11

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6qyzgxsip/) · [Index assessment](#c281)

> Strata needs 12gb of vram though?

**Remaining questions / verification:** Does Strata require 12GB VRAM for the relevant version/model?

### C283 — colonelx_

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxd3mqo0eqo/) · [Index assessment](#c283)

> I have 10gb vram, is it enough?

**Remaining questions / verification:** Is 10GB VRAM enough for the suggested Strata model/version?

### C288 — colonelx_

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3mmrsel5w/) · [Index assessment](#c288)

> Could you share your hardware specs? Also, which coding agent are you using?

**Remaining questions / verification:** What are your hardware specifications?; Which coding agent are you using?

### C293 — Annual_Award1260

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwok76gf7aa/) · [Index assessment](#c293)

> I use qwen 27b for some web browser automation and testing. For coding I’m running glm 5.3 (full) with 1 mil context. Maybe try deekseek flash or glm flash?

**Remaining questions / verification:** What hardware/runtime/context fill and coding outcomes support the GLM setup?; Which Flash variants fit the OP's machine and how do they perform?

### C294 — cmndr_spanky

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwonckfzpgj/) · [Index assessment](#c294)

> What harness have you tried ? Why be vague about it. First, you can’t use Claude code with local models, way too much bloat. Start with open code. Second, qwen can be very sensitive to which inference settings you’re using, third, do you know which quantization of the model you’re using ? Less than q4 is a bad idea. Also, are you absolutely sure you know what its context window is set to and how much it can effectively use?
>  
> Finally, are you just using it in the same code base you were using with Claude and by any chance do you have dozens of Claude.md / agent.md files and 10+ skills ? That will basically instantly wreck what limited context window you have and pretty much guarantee the model will get “lost” trying to do basic tasks

**Remaining questions / verification:** What harnesses have you tried?; Which weight quantization and inference settings are you using?; What context window is set, and how much is effectively usable?; Does the codebase contain dozens of CLAUDE.md/agent.md files and 10+ skills?; How many instruction/skill tokens are actually injected and do controlled removals improve success?

### C299 — Original-Mistake8624

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3fodrkioz/) · [Index assessment](#c299)

> Have you compared the accuracy and task completion rate of this Swift 1.5 IQ3_XXS setup against the original Qwen 27B at Q4 or higher, using the same coding tasks?

**Remaining questions / verification:** Has Swift1.5 IQ3_XXS been compared with original Qwen27B Q4+ on the same coding tasks for accuracy and task completion rate?; Were harness, prompts, context, runtime, attempts, and tests controlled?

### C303 — jellyrole

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwoxu38s7tx/) · [Index assessment](#c303)

> Why only q8 with a pro 6000?

**Remaining questions / verification:** Why choose Q8 rather than a higher-precision format on the RTX 6000 Pro?

### C304 — Humble_Ad_1875

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpzl823tlu/) · [Index assessment](#c304)

> Just got advice from claude: 
>  
> Qwen3-Coder 30B (MoE): only 3.3B of its parameters are active at a time, it’s 19 GB at Q4, and it has a 256K context window. That’s slightly more than your VRAM, but because so few parameters are active, Ollama can put the overflow in system RAM and it still runs at decent speed.
>  
> Rig specs:
>   
> AMD Ryzen 9 9900X3D (4.4GHz) Processor
>  
> 64GB DDR5-6000 RAM
>  
> NVIDIA GeForce RTX 5080 Graphics Card
>   
> Is it going to run?

**Remaining questions / verification:** Will this model and intended context actually fit and run usefully on the listed machine?; Are the quoted footprint, context and offload-speed claims accurate?

### C305 — sudden_aggression

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwqrx7bqmcj/) · [Index assessment](#c305)

> AIs will just give you whatever was in their training data six months ago. qwen3-coder 30B hasn't been a state of the art local model since what, last year?
>  
> with your setup (5080 has 16gb right?) I would advise either a highly quantized qwen 3.8 flash next or a q4 quant of 3.6 35A3B.

**Remaining questions / verification:** Which exact quant, runtime, RAM demand and context make either recommendation viable on that hardware?

### C307 — Bunksha

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwp02lkgvc4/) · [Index assessment](#c307)

> What quant are you using? 24GB VRAM & DDR4 32Gb isnt really that much. Q4 is ~17gb of memory and 128k context is, what, 9gb? That puts you over the 24gb which means its gonna spill over & be slow. I run the same model at Q8 with 256k tokens and its been amazing at coding.

**Remaining questions / verification:** What quant is the OP actually using?; What KV format, hardware, occupied context and allocation behavior support the memory estimates and reported Q8/256k run?

### C308 — FollowKryst

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwp43fr0jok/) · [Index assessment](#c308)

> I’m no expert, but I used this model in Pi harness via llama.cpp… I didnt like the experience in LM Studio and using any model in Hermes vs pi, for me, is noticeable.
>  
> I have a 64gb M1 Max MacBook Pro, and you running that dense model with that context size with less processing than me draws concerns in and of itself.
>  
> You should probably share the harness you’re using, the quant of the model, and what you’re trying to do.. also, I notice running these models in terminal always gives better results.
>  
> I mainly use Q4_K_M Qwen 3.6 35B via llama.cpp in terminal and I get lots of great things done with ease. Even when I did use the Qwen 3.8 27b, I got good results though slow and takes up majority of my ram.
>  
> Idk the comparison of Nvidia vs Apple silicon chips, so you might want to compare you and our systems before you try any I mentioned.

**Remaining questions / verification:** Which harness, quant and concrete tasks does the OP use?; Were LM Studio, Hermes, Pi and terminal comparisons made with identical weights, prompts and sampling?

### C319 — No-Recover109

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwqgpkh5rc3/) · [Index assessment](#c319)

> I used to use qwen3.8 27B FP8 for coding and it did pretty well. I used vllm which actually is too heavy for coding. Now I use Strata and Deepseek v4.1 1017 q3 istalabs version. Seems to be working also. I think you cant run qwen3.8 with that GPU and context amount in any proper quantization? I guess you are running it q4 and that might be too little. Try different engines and make sure you actually set the context same in the inference engine and in the coding agent

**Remaining questions / verification:** What are the OP’s actual quant and server/client context limits?; What does “too heavy” mean for the reported vLLM deployment?

### C325 — ParticularlyStrange

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwr6gc375ib/) · [Index assessment](#c325)

> What quant are you running? Use the EXL3 or NVFP4 quants.

**Remaining questions / verification:** What quant is the OP running?; Are the proposed formats supported efficiently on the OP GPU/runtime, and with what artifact quality?

### C327 — Sea_Advance273

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwrhl8ia200/) · [Index assessment](#c327)

> Have you tried using Qwen in the Claude Code harness? It performs a lot better. Still need to iterate a lot more and be more involved than opus-5.5 of course, but I've been decently impressed with even Q4 running in 24GB VRAM.

**Remaining questions / verification:** Which runtime, cache precision, context and tasks produced the result?

### C330 — Current_Ad5753

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwrt267zvs1/) · [Index assessment](#c330)

> Hey could you please update if you using any harness over your local llm.

**Remaining questions / verification:** Which harness is actually being used for the failing runs?

### C334 — MonadicKierkegaard

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwsavw1x5et/) · [Index assessment](#c334)

> is that setup per dev or for a team?
>  
> you can eke out maybe one coding agent, barely.
>  
> its ok for one shot toy apps/games. but real agentic workflow, 32GB is not enough.
>  
> maybe use cloud providers for generating an extremely detailed spec, with pseudocode. Then instead load an MoE that fits well on a 32GB - this can go as high as 2k tps PP, 70 tps GG. that speed is more than workable at the expense of intelligence (hence you need to guide it)

**Remaining questions / verification:** Is the machine shared by a team or dedicated to one developer?; Which MoE, quant, context and hardware achieve the quoted prompt/generation rates?

### C356 — thilog

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwzkug6ftt0/) · [Index assessment](#c356)

> Which harness do you recommend?

**Remaining questions / verification:** Which harness is recommended, for what workload and deployment?

### C357 — mattjouff

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwy7vusj6ar/) · [Index assessment](#c357)

> This thread is rediscovering the terrible economics of AI from the ground up:
>  
> “We are trying to run the models locally (presumably for cost and privacy) but our 27B open weight model doesn’t perform as well as the 2000B flagship model, what are we missing?”
>  
> By the time you get a model that can actually do the work you’re back to renting GPU by the hour lmao

**Remaining questions / verification:** What ownership, power, engineering-time and hosted/rental costs are being compared?; What evidence supports the claimed flagship parameter count?

### C365 — colonelx_

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2so82h95u/) · [Index assessment](#c365)

> 32core? is that epyc?

**Remaining questions / verification:** Was the CPU 32-core and an EPYC? Answered/corrected within this range by C366: Ryzen 9 5950X, 16 cores/32 threads.

### C372 — VihmaVillu

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1hvljq3dx/) · [Index assessment](#c372)

> In terms of harness you starts from 0 compared to claude code.
>  Also what quantization are you using?
>  PS: I'm having a blast with qwen3.8-flash-next-iq3_s via strata

**Remaining questions / verification:** Which quant is the OP using?; What hardware, tasks, context and validation support the reported Flash Next success?

### C376 — Sea_Shift4327

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1xrpwqt9g/) · [Index assessment](#c376)

> What exact quant are you using, and did you also quant the KV cache?

**Remaining questions / verification:** What exact weight quant is in use?; Was the KV cache quantized, and to what K/V formats?

### C378 — goingsplit

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3guvrvjc1/) · [Index assessment](#c378)

> would you be so kind to include in that project also the prompts used for having QWEN create it?

**Remaining questions / verification:** Can the actual prompts used to create the project be included? C379 supplies an approximate initial prompt and setup advice, not a complete prompt transcript.

### C382 — Tigonimous

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2copl68pv/) · [Index assessment](#c382)

> What harness you use with qwen?

**Remaining questions / verification:** Which harness is being used with Qwen?

### C389 — Original-Mistake8624

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx31xx7eheq/) · [Index assessment](#c389)

> Interesting discussion. I’ve been experimenting with a different approach for a fully local AI assistant.
>  
> Rather than relying on a single powerful machine, I use two dedicated systems:
>  
> System 1 – Orchestration:
>   
> Ryzen 7 8745HS, 32GB DDR5, Radeon 780M
>  
> Handles agent coordination, task planning, persistent SQLite memory, voice interaction and supervision.
>   
> System 2 – AI inference:
>   
> Ryzen 9 3900X, 64GB DDR4
>  
> 2 × RTX 3060 12GB (24GB total across both GPUs)
>  
> Qwen 35B-A3B MoE, Q4_K_M with MTP, running on llama.cpp CUDA
>  
> 34 GPU layers, approximately 37.5 tokens/s in my validated test configuration
>  
> Both GPUs limited to 130W and around 1850MHz, typically running at 50–57°C.
>   
> The two machines communicate through a dedicated 2.5GbE Ethernet connection, with measured throughput of approximately 2.35Gbps in both directions.
>  
> I’ve also experimented with Qwen 27B, but chose the 35B-A3B MoE model as my main configuration based on comparative tests.
>  
> My approach is to separate planning, execution, verification and persistent learning rather than expecting a single LLM to handle everything perfectly.
>  
> I believe many issues with local coding models are related not only to model capabilities, but also to orchestration, context management, tool integration and verification.
>  
> The system is still under development, so I’m not claiming that it already solves every coding reliability issue.
>  
> My goal isn’t to chase the highest tokens/s. What matters most to me is accuracy, reliability and the ability to complete complex tasks correctly, learn from mistakes and improve over time.
>  
> Has anyone experimented with a similar distributed architecture or compared Qwen 27B with the 35B-A3B MoE model for agentic coding?

**Remaining questions / verification:** Has anyone tried a similar distributed architecture or compared 27B with 35B-A3B for agentic coding?; What comparative task results, orchestration overhead and validation support the design?

### C393 — goingsplit

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3bin5g141/) · [Index assessment](#c393)

> what's an ok quant?

**Remaining questions / verification:** Which quant is considered acceptable? C394 names sources/formats but does not provide controlled quality or fit evidence.

### C396 — goingsplit

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3az18w1b5/) · [Index assessment](#c396)

> what would that be

**Remaining questions / verification:** What is the workflow behind the claimed Sonnet-like result? C397 mentions OpenCode/Pi and agents but leaves implementation and validation unspecified.

### C401 — cagriuluc

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx46pway5k1/) · [Index assessment](#c401)

> Are you not sharing the quants and the config because you tried it all, or…?

**Remaining questions / verification:** Actual question: why were quants and configuration not shared; have alternatives actually been tried?

### C402 — T_rex2700

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx47m8c4qe9/) · [Index assessment](#c402)

> lemme guess, ollama on windows? yea forget about performance dude. that thing is good for mini model and chat.
>  
> at minimum you want to use something like lmstudio with llamacpp arg override.
>  and if possible, try on linux.
>  
> and that reasoning loop is well, Qwen being Qwen. I learned to be very specific with Qwen.

**Remaining questions / verification:** Is the poster actually on Windows; which overridden arguments and alternative runtime are intended; what prompts stopped loops?

### C403 — Comprehensive_Rock50

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx49zpk1leo/) · [Index assessment](#c403)

> 128K context is a capacity setting, not a guarantee of comprehension. With a 27B model, even 4-bit weights alone can consume roughly 13.5 GB before quantization overhead, runtime memory, and the KV cache. That leaves limited VRAM for a large context. But we don't know their quantization, actual context usage, or whether layers are offloaded to system RAM. Importantly, insufficient VRAM generally causes memory pressure, offloading, slowdowns, or allocation failures. It doesn't directly reduce the model's inherent reasoning ability. Quantization and truncated context, however, can affect answer quality. model intelligence and agent reliability are separate engineering problems. The Reddit poster hasn't established which one is failing. I also wouldn't conclude that their expectations are unrealistic. Understanding a project, making a small change, running a test, and reporting the result is a reasonable target for evaluating a local coding agent. What I would really want to see is one failed execution trace: the prompt, files actually read, tool calls, context usage, and the point where the agent starts looping. That evidence would tell us considerably more than the model's parameter count. One question remains unanswered in their post: is Qwen actually failing to reason, or is their agent failing to give Qwen a coherent environment in which to reason?

**Remaining questions / verification:** Actual question: is Qwen failing to reason or being given an incoherent agent environment? Missing prompt, files read, tool trace, actual context, quant, offload and loop onset.

### C405 — relmny

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx4ptzd0plv/) · [Index assessment](#c405)

> so you unashamedly say you use ollama, then don't mentuon quant, parameters, hardware, etc and claim is bad?
>  
> First use a proper inference engine, then look at what quant you're using and why and then look at the recommended parameters.

**Remaining questions / verification:** Which engine, quant and recommended parameters are meant, and what is the actual runtime configuration?

### C407 — LocalhostRonin

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx52yc5j99f/) · [Index assessment](#c407)

> Gotta share your full runtime config for better comments (model quant, KV quant, serving stack, vision support, etc)
>  
> How long did you wait before you decided it was a repetitive loop? From my experience, it tends to go in circles for quite a while then decide okay that’s the right way. Qwen tokens per task can be like 5-10x of Opus, so gotta give it time.
>  
> Lastly, Sonnet 5.5 has 1M context window, while Qwen-27B has only 128k. Analogy: Sonnet has a larger chopping board to process a huge pumpkin, while Qwen is expected to process the same pumpkin on a chopping board 88% smaller. The same 30k tokens .md file is a drop in the ocean for sonnet to process, but it’s over 20% of the 27B’s context window.

**Remaining questions / verification:** Actual question: how long was allowed before deciding it was repetitive? Missing runtime settings, actual token use and whether apparent loops eventually complete.

### C411 — Joozio

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx5uc3zz3c1/) · [Index assessment](#c411)

> I did nearly the same swap on my own agent setup, though not for coding, so take this as adjacent. My system is built model-agnostic, so moving it from Claude to a local Qwen 9B served by Ollama was a one-line config change, and then the same agent was running its usual tasks on Qwen.
>  
> What held up: memory recall, anything shaped like "read a file, find the relevant bit, report it", and calling the right tool on straightforward requests. What didn't: analysis or anything needing real synthesis, where the quality gap was obvious. The 4B variant dropped off hard; for my kind of work, 9B was the floor.
>  
> So a local model handled a real subset of what Claude was doing for me, and the pieces that held were the narrow ones. Which part breaks first for you, the planning across files or the individual edits?

**Remaining questions / verification:** Actual question: does planning across files or individual editing fail first? Exact tasks, quant, hardware and measured comparisons are absent.

### C419 — No_Oil_6152

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6bxqz7zj8/) · [Index assessment](#c419)

> You're going to need to tell us what your temperature settings are, what your k/v cache is, what harness you're using with 3.8
>  
> 3.8 can deliver good results - its just VERY SLOW.

**Remaining questions / verification:** What temperature, KV format/size and harness are actually being used; how is slowness measured?

### C422 — immediate-drink-9876

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxbhmc3e00w/) · [Index assessment](#c422)

> Best on your experience, which harness works best?

**Remaining questions / verification:** Actual question: which harness works best in the respondent's experience, and for which model/tasks?

### C431 — sometimes_angery

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx7jq68tdpg/) · [Index assessment](#c431)

> Given the 32gb ram and qwen 27b being 55gb on float 16, I'm guessing you're using a float8 version? Or what quant? We run float16 at work and it does have blind spots but can complete tasks, just not quite perfectly. Flash next was better at an int4 quant than 27b float16 tho.

**Remaining questions / verification:** Actual question: what quant is the poster using? Missing workplace hardware, tasks, context, scores and matched comparison details.

### C433 — Sirlowcruz

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx8hbfnpi1s/) · [Index assessment](#c433)

> it sounds like you still need a harness for the model. something to make it act agentically. maybe hermes.
>  
> also important to know: what quantization and reasoning mode are you running? anything at or under q4 makes this model act weird IMO.

**Remaining questions / verification:** Actual question: what quantization and reasoning mode are being run? What observed failures justify the Q4 cutoff?

### C435 — xapep

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx91i1tw6n6/) · [Index assessment](#c435)

> Before you blame the model, check what the quant and the context length leave you. A 27B at 4-bit is roughly 15-16GB of your 24, and a 128K window needs its KV cache somewhere on top of that. Once it spills into system RAM you're decoding over PCIe at a few tokens a second, and long-context quality falls off a cliff. That looks a lot like a model that lost the plot. 
>  
> Try the same prompt at 16K and watch VRAM and tok/s. If it snaps back to something usable, you were never running the 128K setup you thought you were. 
>  
> The other half is the harness. Sonnet 5.5 in an agent loop reads the file, runs the test, and retries a patch that didn't take. Drop a 27B into the project root with the same md files and none of that happens, so the first wrong step becomes a loop instead of a retry. One file at a time, explicit paths, and let it see the failing test output. 
>  
> I work on the serving side of an inference API, so take the last part with salt. What's your tok/s at 16K versus 128K? That tells you whether this is a hardware ceiling or a setup problem.

**Remaining questions / verification:** Actual question: what are tokens/s at 16K versus 128K? Also missing quant, VRAM/offload measurements, agent loop and retained prompt content.

### C447 — pinkwar

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxax0csoqzl/) · [Index assessment](#c447)

> Crazy how you did it so backwards. First you find a model and setup that suits you (using cloud rented gpus) and then you buy the hardware.
>  
> Who approved buying that without any sort of POC?

**Remaining questions / verification:** Actual question: was there a proof of concept and who approved purchase? More relevant gap: was a representative workload evaluated before selecting hardware?

### C448 — dc740

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxaydwsf3c5/) · [Index assessment](#c448)

> you are using a heavily quantized version of Qwen. that's not the same as running a full version, and the difference can be day and night. as a side note: next time provide details and write the post yourself. nobody cares about typos and writing style. stop asking the AI to think for you. write that in your agents.md

**Remaining questions / verification:** What quant is actually used; is it substantially degraded on matched tasks relative to higher precision?

### C456 — moochine2

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxccjloran7/) · [Index assessment](#c456)

> Which quant? Maybe you are using a 1 or 2 bit quant? Try this for example:  [https://huggingface.co/ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF] https://huggingface.co/ISTA-DASLab/Qwen3.8-27B-GSQ-RCO-GGUF
>  
> Upgrade to 64 RAM as well. It won’t really make things faster, but it will help overall system performance and help you not run out of memory.
>  
> Consider Strata also with the 125b coding version of the model also.

**Remaining questions / verification:** Actual question: which quant is in use? What memory use and task comparisons support the linked quant or 125B option on this hardware?

### C457 — Jazzlike-Plate

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxcl6y6e10l/) · [Index assessment](#c457)

> I had a similar experience with that model. I used ollama. Can someone explain why that was such a huge mistake? I thought the server makes zero difference.

**Remaining questions / verification:** Actual question: why would Ollama make such a difference; what serving-layer behaviors alter outcomes? Missing exact model/settings and matched-runtime trace.

### C464 — BeatDistinct317

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxet1la76hx/) · [Index assessment](#c464)

> Comparing Qwen 27B to Sonnet....does anyone know how many parameters and what quantization does Sonnet use? Ever rumors? 
>  
> If Sonnet is some +300B you probably can't expect Qwen to compete

**Remaining questions / verification:** Actual questions: what parameter count and quantization does Sonnet use; are there rumors? No verified architecture data or matched-task evidence is supplied.

### C474 — flatfalafel

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxjur0zclgh/) · [Index assessment](#c474)

> As someone new to this world myself and learning a lot of the lessons people in here are sharing on my own, do you have resources on llama.cpp for newbies?

**Remaining questions / verification:** Actual question: which llama.cpp resources are appropriate for newcomers?

### C485 — KnavishlyUncommon

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwjv7pf3jxg/) · [Index assessment](#c485)

> what backend are you running it through, that'll make or break the agent behaviour before the model even gets a chance

**Remaining questions / verification:** What backend are you running it through?; No comparative backend evidence supplied.

### C487 — vogelvogelvogelvogel

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk3367s2hw/) · [Index assessment](#c487)

> using ollama as an engine always suggests me someone not relly spent time how to set up an llm
>  
> use i.e. llama.cpp, ask some proper ai to do some test runs with different speculative decoding configs, then go from there
>  
> claude code? rather not uses too much context, try i.e. pi
>  
> also comparing to sonnet 5.5? every half decent benchmark will tell you it settles at best at about two versions earlier
>  
> (also as a software house researching so much only at the surface..? also single 3090..? which means q4..?)

**Remaining questions / verification:** Which speculative-decoding configuration, quant and benchmark support the advice?; Actual single-3090 quant is not established.

### C488 — Ratiofarming

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk51wh0xic/) · [Index assessment](#c488)

> Okay, but which ones are you currently using?

**Remaining questions / verification:** Okay, but which ones are you currently using?; Parent linkage is absent; exact referent unresolved.

### C489 — Potential-Leg-639

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk6fpsmmch/) · [Index assessment](#c489)

> Ollama?
>  You have to dig a bit deeper now. Ollama is a no go. Try with llama.cpp first, but nowadays there are a lot of different inference engines…
>  
> Get another 32GB RAM and run Strata with Qwen3.8-Flash-Next, ot wont get any better. And you will get around 100 tk/s TG and 2000 tk/s PP and a very capable model. But not really optimized for concurrent usage (yet). Therefore vLLm is probably still the best, but another 3090 would be needed for more users anyway minimum..

**Remaining questions / verification:** What exact quant, hardware, context and batch size produce the predicted rates?; How does Strata concurrency compare with vLLM under matched conditions?

### C493 — vimaillig

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk9emyeu91/) · [Index assessment](#c493)

> Which harness are you experimenting with? I’m just starting to setup my environment running it on a 5090, unsloth, and using opencode and/or pi and it’s producing per my expectations…

**Remaining questions / verification:** Which harness are you experimenting with?; Which exact model, quant, context, tasks and Unsloth component are involved?

### C499 — zanar97862

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmsi25di8z/) · [Index assessment](#c499)

> ? Strata is not a dense model engine...

**Remaining questions / verification:** What model architectures and Strata version are supported?

### C504 — Dinth

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx5jezc0syr/) · [Index assessment](#c504)

> Haven’t they went back to mainline llama.cpp in the lastest versions?

**Remaining questions / verification:** Haven’t they gone back to mainline llama.cpp in the latest versions?; Which product, release and backend commit?

### C505 — FMAGF

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpkegv7sf9/) · [Index assessment](#c505)

> Is ollama fine for regular text generation and reasoning?

**Remaining questions / verification:** Is Ollama fine for regular text generation and reasoning?

### C507 — infiniti306

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwztp1spfhc/) · [Index assessment](#c507)

> So I just installed ollama qwen 3 14b two days ago. Should I switch too?

**Remaining questions / verification:** Should I switch too?; What hardware, use case and problems motivate a switch?

### C510 — united_we_ride

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwulk0cza8x/) · [Index assessment](#c510)

> Honestly, for inference engines? Depends entirely on your system.
>  Llama.cpp (Unsloth Studio), or Vllm. 
>  
> For chat interfaces/inference engines:
>  
> Unsloth Desktop/Studio, or Open WebUI.
>  
> I personally recommend Unsloth Studio for the engine and the inference interface. It has great built in tools, can access your terminal if you let it, support for skills, image gen, etc.
>  Its a one stop shop that just works far better than Ollama.

**Remaining questions / verification:** Which backend does each interface actually use in the relevant version?; What comparison supports better behavior?

### C511 — External-Fun-8563

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwurn9zcxb6/) · [Index assessment](#c511)

> Another noob here: I just started playing with LM Studio, is that not a good option? Should I just jump to Unsloth immediately if I want something with a decent UI?

**Remaining questions / verification:** Is LM Studio not a good option?; Should I jump to Unsloth immediately for a decent UI?

### C514 — rororo99

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx5y2sew0x1/) · [Index assessment](#c514)

> What is bad about ollama and what is a better solution?

**Remaining questions / verification:** What is bad about Ollama and what is a better solution?

### C516 — rororo99

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx70cz1u0f6/) · [Index assessment](#c516)

> But why? I have Ollama with Open WebUI and Opencode and works totally fine.

**Remaining questions / verification:** But why?; Which model, hardware, context, tasks and runtime versions work fine?

### C520 — 575_Inverse

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmudwmu84i/) · [Index assessment](#c520)

> so you don't at least tell your model how you want something implemented and why?

**Remaining questions / verification:** Don’t you at least tell your model how you want something implemented and why?

### C530 — _RemyLeBeau_

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmlq4ecja8/) · [Index assessment](#c530)

> Do you have an HF link? I would like to try that model

**Remaining questions / verification:** Do you have an HF link?; Which model does the unstated referent identify?

### C540 — Connect_Ad791

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwu8lsmz89w/) · [Index assessment](#c540)

> ooh, what uncensored model are you using? is it good? I've found a lot of quants to be trash before I found a good one, and I'm afraid to waste time on another lobotomized model.

**Remaining questions / verification:** What uncensored model are you using?; Is it good?; Which quants were poor or good, and by what tests?

### C544 — Badger-Purple

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm5vk1sujp/) · [Index assessment](#c544)

> Why did you only get a 24GB GPU to offload real inference tasks to a model that is natively 27B dense, and therefore occupies at least 27GB without context at half precision? It makes no sense. Sonnet 5.5 is a couple hundred billion parameters, and likely not being served at whatever low quant you are using to get 128k token context on 24GB.

**Remaining questions / verification:** What are the real artifact size, precision, cache allocation and offload?; The stated half-precision size is imprecise: 27B parameters at two bytes is about 54GB before overhead.; Sonnet parameter count and serving precision are not verified here.

### C554 — Canadian_Border_Czar

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwsqf74owip/) · [Index assessment](#c554)

> How long does it take your setup to respond even once? Cramming a Flash Next quant on 12 GB is bonkers, and your context even more. 
>  
> I have way better results by dropping to Qwen3.5-9B. w/ the 7 GB Q5 quant you can still fit the 65k context window and the entire thing runs on GPU VRAM.

**Remaining questions / verification:** How long does your setup take to respond even once?; Which GPU, runtime and KV precision allow the claimed 65k fit?; What tasks were better and against which Flash Next configuration?

### C555 — sudden_aggression

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpe23k5ode/) · [Index assessment](#c555)

> I find that qwen 3.8 27B fills up context rapidly and it's unhappy with less than 200k. It's also harder to configure for good performance than 3.6 27B (I can't seem to crack 50 tps, which was easy on 3.6) That being said, I've gotten it to iterate on coding tasks just fine.
>  
> My setup is
>   
> My setup is Qwen 3.8 27B on R9700 32GB, spent days playing around with settings, ended up with 300k unified cache, 256k per slot (this allows hermes to run cron jobs while the main session codes). I have used 3.8 with session sizes down to 200k with success but 128 is just bad. 
>  
> Q8_0 K cache, Q4_0 V cache. I feel this helps with reasoning strength noticeably. I was running Q4_0 for both previously.
>  
> orchestrated via hermes. basically a vanilla config but I gave it firecrawl, camofox and searxng as well to help it do research
>  
> I gave it a gitea instance to save its work to, gave it a sandbox to run stuff in and it blasts along fine getting shit done. I've been giving my current config real world coding tasks for maybe a month now. Previously I used 3.6 27B with a bunch of different settings. 3.8 seems slower but smarter.
>   
> edit- you're using fucking ollama? get the fuck outta here, switch to llama.cpp
>  
> no seriously, do it now

**Remaining questions / verification:** What weight quant, actual occupied context, runtime build and slot allocation were used?; How were 128k versus 200k and Q4/Q4 versus Q8/Q4 compared?; How do 300k unified and 256k-per-slot settings interact under simultaneous jobs?; What were task success rates and human interventions?

### C563 — kirbyfanner

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwt3enmmfmr/) · [Index assessment](#c563)

> I'm using LM Studio and feel similarly. I have a lot of issues running it.
>  
> For the harness I'm using VS Code GitHub Copilot BYOK. My GPU is the 32gb R9700.
>  
> It's running very fast, the time to first token is near instant, but it seems to fail often and hallucinate/death loop a LOT. It works okay in LM Studio directly, but not great.
>  
> Q6 Quant, 128k context window. K and V cache are Q8.
>  
> Any tips specific to that setup? Thanks y'all.

**Remaining questions / verification:** Any tips specific to that setup?; Which model artifact, LM Studio/backend/Copilot versions and prompts?; Are templates, tool schemas, reasoning parsing and actual context identical between direct and Copilot use?

### C566 — Savantskie1

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwy395eqh0k/) · [Index assessment](#c566)

> 3090 with 120gb of vram? Yeah right. Nice lie lol

**Remaining questions / verification:** Was the stated 120GB system RAM or VRAM?

### C575 — Hunterxmalaa

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx7aazexg9t/) · [Index assessment](#c575)

> I genuinely do not understand people who do this 
>  
> Why do you assume a 27b model is going to outperform or keep up with a frontier model like Claude ? 
>  
> There is a reason these models at hinders of billions to trillions of peramiter 
>  
> Your being extremely unrealistic if your think qwen 3.8 27b is going to outperform proform sonnet 
>  
> Maybe if you ran the model at q8 or bf16 and your tok speeds was still fast maybe but your lowering its quant to get achievable speeds means your father reducing its already limited intelligence just for useage so yes it will forever be dumb

**Remaining questions / verification:** What are verified frontier model sizes and serving precisions?; What matched coding results across quant levels support the claimed degradation?

### C578 — PhilippeEiffel

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx86hp2sk2p/) · [Index assessment](#c578)

> 1) There are missing information in your post: model quant size? KV quant size? which harness?
>  
> 2) Read this:  [https://sleepingrobots.com/dreams/stop-using-ollama/] https://sleepingrobots.com/dreams/stop-using-ollama/
>  
> 3) You want to use model with native size of 54 GB. You need some extra memory to hold the KV cache. You bought a machine without enough RAM to hold this. The model is damaged by the quantization up to the point it is dumb.
>  
> The good way to go: use the model with the native quality (BF16 size for model and KV cache), then reduce the size step by step (this improves the speed and the available context size) while the quality matches your needs.

**Remaining questions / verification:** What are the model quant size, KV quant size and harness?; Is a BF16 reference available, and which tasks/rubric determine acceptable quality?; What actual artifact and KV architecture are used?

### C580 — FiringNerveEndings

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxk5v26p6ea/) · [Index assessment](#c580)

> A quick sanity check. I'm your entire post you haven't mentioned the agentic harness at all... Are you using one? Or are you straight up making calls to the Internet engine. Claude requests go through Claude code that adds system prompt, the LLM knows the cwd, it reads the AGENTS.md file(do you have one?)
>  
> All these can be crucial differences. 
>  
> Disclaimer: I don't run my own local model, I'm currently experimenting on the agent/harness level.

**Remaining questions / verification:** Are you using an agentic harness or making direct engine calls?; Do you have an AGENTS.md file?; Which prompts, file-loading behavior and tools does each side actually receive?

### C581 — majmichu

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxk3btu7f6p/) · [Index assessment](#c581)

> Try another harness, I am building myself a harness exactly for this purpouses its called Local Quench, and I have designed it to help local models finally be able to do something, and also would appreciate someone else's point of view on my project as it is work in progress. Localquench.com
>  
> And setup in my oppinon is very good, try to not go lower than q4km or nvfp4 on this model as he will start more to loose precision and falling in loops. Depending on your engine you can set the quantization of KV cache you can put it at q8_0 no problem (I use myself even q4_0) and it will fit almost twice as much context.
>  
> Qwen 3.8 27b is somewhat a frontier local codign model, I am using its VERY quantised version the bonsai 2 27b, because I have just 8gb of VRAM and yest its sloe for me but it really works, the most matters the harness around so the tools like, opencode, open hands, claude code, codex, this matters more than the benchmark itself. You can have amazing model but if you will give him 30k tokens of instructions of system prompt he looses 1/3 of the context and sooner will drop quality too, and the tools need to be easy for it to understand and work. Try the harnesses designed for smaller models. You can try mine, and I will be very happy tk hear your feedback or other like aider (never liked it too much) but heared a lot of good things about i believe its called tiny swe agent? And open hands, but this one has a big system prompt at the beginning

**Remaining questions / verification:** What exact Bonsai model, quant, backend, CPU offload, context and tasks worked?; How are Q4_0 KV results reconciled with the proposed weight precision floor?; What controlled tests show Local Quench or shorter prompts outperform alternatives?

### C587 — kirbyfanner

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxjjwn4mpia/) · [Index assessment](#c587)

> Oh is it a bad harness? I use it for frontier models a lot and generally like it, but I'm open to change. What do you run?

**Remaining questions / verification:** Is it a bad harness?; What do you run?; Which locally served model behavior differs from frontier use in the same harness?

### C588 — AutomaticDriver5882

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxibdl8061u/) · [Index assessment](#c588)

> I wonder what the TPS is

**Remaining questions / verification:** What is the TPS?; Which model/setup and whether decode, prefill, per-session or aggregate?

### C591 — n4ru

[Direct source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx9hkpmcdr6/) · [Index assessment](#c591)

> why would this matter in this case?

**Remaining questions / verification:** Why would this matter in this case?; Parent linkage is absent; the factor being challenged cannot be identified from this text.

### Peripheral excluded question, preserved explicitly

C019 asks what information LM Studio allegedly sends after C018's unsubstantiated allegation. It is unanswered in the collected evidence, excluded from reliability findings, and not accepted as a privacy finding. [C019 source](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwu947x0lnm/)
