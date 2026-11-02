# Local Qwen 27B coding reliability: exhaustive review of the accessible Reddit corpus

**Thread:** [Local Qwen 27B is practically unusable for coding tasks. Are we doing something wrong?](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/)  
**OP:** u/Major-Creative · post timestamp2026-10-30T23:54:00Z · community r/LocalLLM  
**Research date:**2026-10-31 (America/New_York). Last successful source listing13:40:43UTC /09:40:43EDT.  
**Scope:** read-only research. No configuration changes, implementation, model loads, fresh inference benchmarks, purchases, public posts or external messages. Executive summary is deliberately **last**, after the individual index, taxonomy, roadmap and unresolved questions.

## 0. Retrieval, coverage and reading conventions

### 0.1 What was and was not recovered

| Coverage item | Verified result |
| --- | --- |
| Unique post/comment records |1 post +591 distinct comment IDs |
| Readable comment bodies reviewed |589; every collected readable comment received an individual disposition |
| Qualifying individual index entries |534, including substantive questions, weak claims, negative experiences and dissent |
| Exclusions |57 =55 readable nonqualifying comments +2 deleted placeholders; all individually recorded below |
| Deleted placeholders |2: C015,C024; author/body unavailable |
| Removed placeholders |0 observed; total removed comments **unknown**, not zero |
| Public displayed comment counter |599 in saved `embed-response`; earlier adjacent search snippet displayed597 |
| Counter discrepancy |599−591=8. **Not eight proven removed comments**: omissions, hidden items and snapshot drift cannot be separated |
| Reddit `more`/continuation nodes |Not exposed by Atom;0 explicit markers observed, actual number of unresolved `more` gaps **unknown** |
| Tree/depth/score metadata |Absent for all591 comments; raw ID, author when present, body, timestamp and source permalink retained |
| Low-score coverage |Old/new/top/controversial/confidence views were cross-checked, but low-score completeness cannot be certified without scores/tree |
| Completeness claim |**Exhaustive review of the collected accessible corpus; not certified retrieval of the entire Reddit comment tree** |
| Duplicate body versions |0 differing bodies found across successful feed snapshots |

The share URL resolved to the canonical thread above. Normal HTML returned a challenge shell; browser displayed **“Prove your humanity”** with reCAPTCHA, and that route was not advanced. Public JSON/API requests returned403; old Reddit redirected to login. The ordinary public Atom endpoint succeeded. Rate-limited429 attempts were not treated as content; later retries followed the stated reset. No challenge/login/security control was bypassed and no cookies were imported. Five comment sort orders, plus different feed limits, were collected and unioned by exact Reddit comment ID. Last three ranking views added no IDs beyond591. This improves recall but does not reveal invisible IDs or reconstruct `morechildren`.

**Honest limitation:** the requested complete tree, exact removed count and exact continuation-gap count are not verifiable from the accessible interfaces. No content, deleted author, score, parent, or gap count has been invented to close that difference. Feeds flatten comments: apparent exchanges are discussed cautiously, not reconstructed as a proven tree. Source permalinks are those supplied by Reddit's feed; every permalink was not separately browser-opened through the challenge.

### 0.2 Successful source inventory

| Saved source | Entries including post | Comment IDs | New IDs added to union |
| --- | ---: | ---: | ---: |
| [rss-response](rss-response) |199|198|198|
| [rss-limit500.xml](rss-limit500.xml) |485|484|286|
| [rss-limit1000.xml](rss-limit1000.xml) |484|483|0|
| [rss-old.xml](rss-old.xml) |488|487|95|
| [rss-new.xml](rss-new.xml) |486|485|12|
| [rss-controversial.xml](rss-controversial.xml) |486|485|0|
| [rss-top.xml](rss-top.xml) |485|484|0|
| [rss-confidence.xml](rss-confidence.xml) |485|484|0|

Raw XML, failed-attempt logs, initial HTML, embed HTML, normalized JSON/Markdown corpus, index JSON and coverage JSON are retained alongside this report. `artifact-manifest.json` provides sizes and SHA256 hashes. Stable refs C001–C591 were assigned on first encounter and never renumbered: they do **not** encode time, depth, popularity or relevance. OP is separate from C486, the OP's collected clarification comment.

### 0.3 OP disclosures, not assumed diagnoses

The original post states Ryzen5 5500,32GBDDR4,RTX3090 24GB; Qwen3.8-27B with a claimed128K context; comparison with Claude Sonnet5.5 Medium; instruction difficulty, repetitive reasoning/loops and inability to finish allegedly simple coding tasks in the same project/docs. The edit and C486 identify **Ollama** and an unsettled harness. Exact weight/KV quant, effective sampler/thinking, runtime build, applied template, actual occupied context, concurrency and a failed task trace are not supplied. No other user's guesses fill these gaps.

OP's five questions are preserved: capability/configuration;24GB/128K hardware limits; inference/quant/context choices; similar-size local alternatives; actual experiences with coding-agent harnesses. The post also asks whether expectations or setup are wrong and requests legacy-codebase experience. Full original text is the OP record in [comment-corpus.md](comment-corpus.md).

### 0.4 Index/evidence rules

“Contribution” is a faithful summary of the commenter, not this report asserting the claim is true. “Relevance,” “open questions” and “transferability” are analysis and explicitly distinct. E0 = question, proposal or unsupported assertion; E1 = vague firsthand report; E2 = setup/task-specific firsthand account or concrete recipe **without independent verification**. E3 would require controlled/reproduced evidence and is not attained here. Counts are dispositions, not votes or independent experiments. Several comments by one author are correlated; a recommendation repeated by many authors is still not a causal test.

Exclusions cover empty reactions, jokes, insults, redundant bare crossreferences, privacy tangent and unreadable deleted records. Borderline methodological dissent/questions were retained conservatively, even when low relevance. All534 qualifying entries come next, **before synthesis**.

## 1. Individual qualifying-comment index


<a id="c001"></a>

### C001 — u/Repulsive_Initial308

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwjzs2rk8f7/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwjzs2rk8f7/)

- **Faithful contribution:** Guesses OP is using Ollama; the post edit does confirm that runtime.
- **Type:** diagnostic suspicion
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** No demonstrated causal link from Ollama to OP's failure.
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate.
- **Themes:** runtime

<a id="c002"></a>

### C002 — u/InfiniteBlink

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkrclmvfkw/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkrclmvfkw/)

- **Faithful contribution:** Calls moving from Ollama to llama.cpp the next obvious step.
- **Type:** recommendation
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Which effective setting or behavior changes?
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate.
- **Themes:** runtime

<a id="c003"></a>

### C003 — u/nfored

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlg9bq4i3n/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlg9bq4i3n/)

- **Faithful contribution:** Regrets delaying a switch; no measurable outcome or configuration supplied.
- **Type:** personal endorsement
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures.
- **Evidence quality:** E1 — first-person report without reproducible configuration/outcome data.
- **Open questions / verification gaps:** What changed besides the server?
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate.
- **Themes:** runtime

<a id="c004"></a>

### C004 — u/JesusIsMyLord666

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlttl8lxuq/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlttl8lxuq/)

- **Faithful contribution:** Asks why not use Unsloth.
- **Type:** question
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures. Provides an alternative-model/runtime lead, not a demonstrated fix for unchanged target model.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Unsloth Desktop, quants, or another Unsloth component?
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate. Changing model changes the hypothesis; establish a working baseline and fit before considering this lead.
- **Themes:** runtime, alternatives

<a id="c005"></a>

### C005 — u/575_Inverse

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmm82ykdd0/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmm82ykdd0/)

- **Faithful contribution:** Reports Unsloth Desktop works well and says its backend is llama.cpp.
- **Type:** experience
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures.
- **Evidence quality:** E1 — first-person report without reproducible configuration/outcome data.
- **Open questions / verification gaps:** No model, harness, settings, or outcome supplied.
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate.
- **Themes:** runtime

<a id="c007"></a>

### C007 — u/xsilas43

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwu8e8yrsf8/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwu8e8yrsf8/)

- **Faithful contribution:** Reports Unsloth Desktop custom llama.cpp builds are faster on AMD.
- **Type:** experience
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures. Tests fit, residency/offload, shared memory and concurrency, not hardware-as-intelligence.
- **Evidence quality:** E1 — first-person report without reproducible configuration/outcome data.
- **Open questions / verification gaps:** Which build and comparable workload? AMD speed does not establish NVIDIA accuracy.
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate. OP uses a discrete3090; user has a different Apple unified-memory/MLX path. Do not copy memory/tok/s estimates.
- **Themes:** runtime, hardware

<a id="c008"></a>

### C008 — u/DystopianRealist

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpk3zg23kz/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpk3zg23kz/)

- **Faithful contribution:** Describes Unsloth as a llama.cpp fork.
- **Type:** architecture clarification
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Which Unsloth product/build is meant? Not independent performance evidence.
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate.
- **Themes:** runtime

<a id="c009"></a>

### C009 — u/Damn-Sky

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx62cgn0a75/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx62cgn0a75/)

- **Faithful contribution:** Describes an Ollama-to-Unsloth switch as night-and-day and more convenient.
- **Type:** experience
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures.
- **Evidence quality:** E1 — first-person report without reproducible configuration/outcome data.
- **Open questions / verification gaps:** No controlled quality or settings comparison.
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate.
- **Themes:** runtime

<a id="c010"></a>

### C010 — u/amadeo681

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwl2pfe3s0y/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwl2pfe3s0y/)

- **Faithful contribution:** Asks for the steps to move to llama.cpp.
- **Type:** question
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** No complete migration sequence demonstrated in this exchange.
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate.
- **Themes:** runtime

<a id="c011"></a>

### C011 — u/Spearush

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlhysunuzl/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlhysunuzl/)

- **Faithful contribution:** Lists personal progression through AnythingLLM, Ollama, LM Studio, Zed, Cursor and llama.cpp.
- **Type:** experience
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures. Tests usable tool access, orchestration, protocol and prompt overhead.
- **Evidence quality:** E1 — first-person report without reproducible configuration/outcome data.
- **Open questions / verification gaps:** These mix harnesses and inference servers; which actual combination helped?
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate. A suggested harness may change several variables; validate access, protocol and prompt budget separately.
- **Themes:** runtime, harness

<a id="c012"></a>

### C012 — u/DeedleDumbDee

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm5it4gfj5/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm5it4gfj5/)

- **Faithful contribution:** Suggests vLLM, while joking about buying hardware for concurrent serving.
- **Type:** recommendation/cost aside
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures. Evaluates elapsed time, senior attention, maintenance and accepted-work cost.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Does OP need concurrency, and would it fit?
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate. Preference and task dependent; quoted throughput, prices and savings are not cost-effectiveness proof.
- **Themes:** runtime, economics

<a id="c013"></a>

### C013 — u/InfiniteBlink

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpu69a5y8y/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpu69a5y8y/)

- **Faithful contribution:** Asks whether vLLM is worth exploring on two 3090-class cards when optimized llama.cpp works.
- **Type:** question
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures. Tests fit, residency/offload, shared memory and concurrency, not hardware-as-intelligence.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** What workload/concurrency or performance gap justifies changing?
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate. OP uses a discrete3090; user has a different Apple unified-memory/MLX path. Do not copy memory/tok/s estimates.
- **Themes:** runtime, hardware

<a id="c014"></a>

### C014 — u/pArbo

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwq8d620crn/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwq8d620crn/)

- **Faithful contribution:** Discusses distributing inference across GPUs, says llama.cpp can do it, and suggests vLLM matters more for clustering.
- **Type:** technical opinion
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures. Tests fit, residency/offload, shared memory and concurrency, not hardware-as-intelligence.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** No measured comparison or concrete distributed-serving explanation supplied.
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate. OP uses a discrete3090; user has a different Apple unified-memory/MLX path. Do not copy memory/tok/s estimates.
- **Themes:** runtime, hardware

<a id="c016"></a>

### C016 — u/_RemyLeBeau_

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmgtq2hh2d/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmgtq2hh2d/)

- **Faithful contribution:** Says direct llama.cpp exposes settings important for agents and allows finding a useful combination.
- **Type:** configuration argument
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures. Improves causal identification, failure visibility and comparison validity.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Which settings differ from the current effective values?
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate. Transfer measurement discipline, not the commenters root-cause certainty.
- **Themes:** runtime, methodology

<a id="c017"></a>

### C017 — u/daft_knight

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnjmf1cd5u/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnjmf1cd5u/)

- **Faithful contribution:** Asks whether switching from a redacted/unspecified product to llama.cpp provides a big benefit.
- **Type:** question
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Starting product is obscured; benefit remains unresolved.
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate.
- **Themes:** runtime

<a id="c020"></a>

### C020 — u/InfiniteBlink

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlj7a9tdi9/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlj7a9tdi9/)

- **Faithful contribution:** Reports dual-3090 Qwen3.8-27B Q8 tensor split at 75 tok/s and suggests using a cloud agent to select/optimize a fitting local setup.
- **Type:** experience/recommendation
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures. Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** No benchmark logs or exact settings; dual cards exceed OP's resources.
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate. Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence.
- **Themes:** runtime, weights, hardware, economics

<a id="c021"></a>

### C021 — u/BonnieReborn

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmm0ac80wx/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmm0ac80wx/)

- **Faithful contribution:** Argues OP's setup is for hobby use, not a professional frontier replacement.
- **Type:** capability dissent
- **Why relevant (assessment):** Evaluates elapsed time, senior attention, maintenance and accepted-work cost. Tests scope, planning, verification and supervision as determinants of accepted work.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** No task-specific evidence; do scoped tasks still have positive ROI?
- **Transferability (inference):** Preference and task dependent; quoted throughput, prices and savings are not cost-effectiveness proof. Applies as an evaluation/workflow pattern; autonomy and net benefit must be measured.
- **Themes:** economics, workflow

<a id="c022"></a>

### C022 — u/Callum_S_AUS

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwny0hqyb37/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwny0hqyb37/)

- **Faithful contribution:** Agrees the gap is too large short of GLM/DeepSeek-scale models.
- **Type:** capability dissent
- **Why relevant (assessment):** Provides an alternative-model/runtime lead, not a demonstrated fix for unchanged target model. Evaluates elapsed time, senior attention, maintenance and accepted-work cost.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Which task and threshold? No measured comparison.
- **Transferability (inference):** Changing model changes the hypothesis; establish a working baseline and fit before considering this lead. Preference and task dependent; quoted throughput, prices and savings are not cost-effectiveness proof.
- **Themes:** alternatives, economics

<a id="c023"></a>

### C023 — u/sonicnerd14

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwtgaa4ex0i/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwtgaa4ex0i/)

- **Faithful contribution:** Reports using cloud agents to configure a local multi-device A0/Hermes stack and retaining cloud for difficult tasks; predicts future local improvement.
- **Type:** experience/prediction
- **Why relevant (assessment):** Tests scope, planning, verification and supervision as determinants of accepted work. Provides an alternative-model/runtime lead, not a demonstrated fix for unchanged target model.
- **Evidence quality:** E1 — first-person report without reproducible configuration/outcome data.
- **Open questions / verification gaps:** No current controlled success rate; future-version prediction is not present evidence.
- **Transferability (inference):** Applies as an evaluation/workflow pattern; autonomy and net benefit must be measured. Changing model changes the hypothesis; establish a working baseline and fit before considering this lead.
- **Themes:** workflow, alternatives

<a id="c025"></a>

### C025 — u/woeful_cabbage

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpsezohy1v/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpsezohy1v/)

- **Faithful contribution:** Says Ollama used to do an unspecified preceding behavior but no longer does.
- **Type:** factual dispute
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Missing parent prevents identifying exactly what claim is disputed.
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate.
- **Themes:** runtime

<a id="c027"></a>

### C027 — u/jandersson82

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx9ybugq9i8/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx9ybugq9i8/)

- **Faithful contribution:** Suggests OpenCode's Big Pickle configure and optimize llama.cpp for the user's hardware.
- **Type:** setup suggestion
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures. Improves causal identification, failure visibility and comparison validity.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** No tested recipe; generated settings require independent checks.
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate. Transfer measurement discipline, not the commenters root-cause certainty.
- **Themes:** runtime, methodology

<a id="c028"></a>

### C028 — u/OnyxProyectoUno

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk2xgkvzqb/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk2xgkvzqb/)

- **Faithful contribution:** Says OP confirmed Ollama in a comment.
- **Type:** OP-context clarification
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** The post edit independently supplies Ollama; referenced reply not identified.
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate.
- **Themes:** runtime

<a id="c030"></a>

### C030 — u/SDdrums

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwrxs6o7cf7/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwrxs6o7cf7/)

- **Faithful contribution:** Asks a better option than the criticized setup.
- **Type:** question
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures. Provides an alternative-model/runtime lead, not a demonstrated fix for unchanged target model.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Better by accuracy, usability, memory use or speed?
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate. Changing model changes the hypothesis; establish a working baseline and fit before considering this lead.
- **Themes:** runtime, alternatives

<a id="c031"></a>

### C031 — u/bytejuggler

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx08pdl03hd/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx08pdl03hd/)

- **Faithful contribution:** Recommends Strata and Qwen3.8 FlashNext with ISTA-DASLab IQ3_S or IQ3_XXS GCO-RCQ.
- **Type:** recommendation
- **Why relevant (assessment):** Provides an alternative-model/runtime lead, not a demonstrated fix for unchanged target model. Tests whether effective serving defaults/behavior, rather than model name, explain failures.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Exact artifact identifier and OP's 32GB fit not established.
- **Transferability (inference):** Changing model changes the hypothesis; establish a working baseline and fit before considering this lead. Transfer the controlled comparison method; not an automatic requirement to migrate.
- **Themes:** alternatives, runtime, weights

<a id="c032"></a>

### C032 — u/Arkasha74

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx8zmwgepwg/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx8zmwgepwg/)

- **Faithful contribution:** Recommends vanilla llama.cpp first for a baseline, warning Strata's buggy releases may confound beginners.
- **Type:** caution/disagreement
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures. Improves causal identification, failure visibility and comparison validity.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Which bugs/builds and recommended hardware are affected?
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate. Transfer measurement discipline, not the commenters root-cause certainty.
- **Themes:** runtime, methodology

<a id="c033"></a>

### C033 — u/bytejuggler

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxaf2n4uyld/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxaf2n4uyld/)

- **Faithful contribution:** Follows/forks Strata and says bugs are overstated for recommended defaults; also supports baseline alternatives.
- **Type:** experience/disagreement
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures. Improves causal identification, failure visibility and comparison validity.
- **Evidence quality:** E1 — first-person report without reproducible configuration/outcome data.
- **Open questions / verification gaps:** Project familiarity is not a controlled reliability comparison.
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate. Transfer measurement discipline, not the commenters root-cause certainty.
- **Themes:** runtime, methodology

<a id="c034"></a>

### C034 — u/Arcane_Satyr

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwud4j0u6xu/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwud4j0u6xu/)

- **Faithful contribution:** Suggests llama.cpp or koboldcpp.
- **Type:** recommendation
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** No supporting configuration or comparison.
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate.
- **Themes:** runtime

<a id="c039"></a>

### C039 — u/Abject-Kitchen3198

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1o132uso0/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1o132uso0/)

- **Faithful contribution:** Asks what the big difference between runtimes is.
- **Type:** question
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** No controlled answer in this comment.
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate.
- **Themes:** runtime

<a id="c041"></a>

### C041 — u/Obvious_Equivalent_1

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwzg623ly1s/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwzg623ly1s/)

- **Faithful contribution:** Claims Claude repeatedly recommends overly small local quants even on large-memory hardware; interprets this as bias.
- **Type:** experience/caution
- **Why relevant (assessment):** Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal. Improves causal identification, failure visibility and comparison validity.
- **Evidence quality:** E1 — first-person report without reproducible configuration/outcome data.
- **Open questions / verification gaps:** No prompts/logs; motive speculation unsupported. Verify agent-generated capacity estimates.
- **Transferability (inference):** Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence. Transfer measurement discipline, not the commenters root-cause certainty.
- **Themes:** weights, methodology

<a id="c043"></a>

### C043 — u/NarutoX666X

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlkyh7cae8/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlkyh7cae8/)

- **Faithful contribution:** Asks what is better.
- **Type:** question
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Improvement criterion and actual setup unspecified.
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate.
- **Themes:** runtime

<a id="c044"></a>

### C044 — u/TrustworthiestFart

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlptn50bdx/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlptn50bdx/)

- **Faithful contribution:** Answers llama.cpp.
- **Type:** recommendation
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** No causal mechanism or test supplied.
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate.
- **Themes:** runtime

<a id="c045"></a>

### C045 — u/sonicnerd14

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwt027yv5b8/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwt027yv5b8/)

- **Faithful contribution:** Reports preferring llama.cpp and suggests LM Studio/Unsloth Studio as beginner alternatives.
- **Type:** experience/recommendation
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures.
- **Evidence quality:** E1 — first-person report without reproducible configuration/outcome data.
- **Open questions / verification gaps:** No matched task or settings comparison.
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate.
- **Themes:** runtime

<a id="c046"></a>

### C046 — u/HolaUsername

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk2ubdhnkx/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk2ubdhnkx/)

- **Faithful contribution:** Asks quant, sampling, harness, engine/settings; reports Q6 27B works but overthinks.
- **Type:** diagnostic questions/experience
- **Why relevant (assessment):** Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal. Tests generation controls as a cause of unstable or looping output.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** Exact OP values, engine build and representative failing trace remain missing.
- **Transferability (inference):** Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence. Use exact model/mode-recommended settings as a measured baseline, not a universal numeric recipe.
- **Themes:** weights, sampling, harness, runtime, reasoning

<a id="c047"></a>

### C047 — u/superbiche

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlnutsmyzn/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlnutsmyzn/)

- **Faithful contribution:** Highlights missing quant/sampling and asks whether multiple people share the single 128K model server.
- **Type:** diagnostic question
- **Why relevant (assessment):** Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal. Tests generation controls as a cause of unstable or looping output.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Concurrency is questioned, not established.
- **Transferability (inference):** Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence. Use exact model/mode-recommended settings as a measured baseline, not a universal numeric recipe.
- **Themes:** weights, sampling, hardware, harness

<a id="c048"></a>

### C048 — u/lumpyspacebreh

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwksv5pa9b4/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwksv5pa9b4/)

- **Faithful contribution:** Reports desired output in two or three turns with own harness and says toolset, prompting and settings matter greatly.
- **Type:** experience/hypothesis
- **Why relevant (assessment):** Tests usable tool access, orchestration, protocol and prompt overhead. Tests scope, planning, verification and supervision as determinants of accepted work.
- **Evidence quality:** E1 — first-person report without reproducible configuration/outcome data.
- **Open questions / verification gaps:** What harness/tools and objective task outcome?
- **Transferability (inference):** A suggested harness may change several variables; validate access, protocol and prompt budget separately. Applies as an evaluation/workflow pattern; autonomy and net benefit must be measured.
- **Themes:** harness, workflow

<a id="c051"></a>

### C051 — u/Turbulent_Office1340

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwy9v1p3o9s/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwy9v1p3o9s/)

- **Faithful contribution:** Calls Q1 unusable while accusing trolls.
- **Type:** quantization opinion
- **Why relevant (assessment):** Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Which artifact/task? Universal threshold is unsupported.
- **Transferability (inference):** Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence.
- **Themes:** weights

<a id="c054"></a>

### C054 — u/MarcusAurelius68

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkk3kgv1r4/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkk3kgv1r4/)

- **Faithful contribution:** Calls 27B wordy and prefers QFN.
- **Type:** experience
- **Why relevant (assessment):** Separates useful long reasoning, pathological loops and output/time budgets. Provides an alternative-model/runtime lead, not a demonstrated fix for unchanged target model.
- **Evidence quality:** E1 — first-person report without reproducible configuration/outcome data.
- **Open questions / verification gaps:** No matched accuracy/speed results.
- **Transferability (inference):** Task-specific tradeoff; a finetune and a base-model thinking toggle are not the same intervention. Changing model changes the hypothesis; establish a working baseline and fit before considering this lead.
- **Themes:** reasoning, alternatives

<a id="c055"></a>

### C055 — u/Minute-Plantain

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlbg4sbkwy/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlbg4sbkwy/)

- **Faithful contribution:** Stopped using Qwen because it was capable but poor at staying on task.
- **Type:** negative experience
- **Why relevant (assessment):** Separates useful long reasoning, pathological loops and output/time budgets.
- **Evidence quality:** E1 — first-person report without reproducible configuration/outcome data.
- **Open questions / verification gaps:** Unknown model version, quant and context occupancy.
- **Transferability (inference):** Task-specific tradeoff; a finetune and a base-model thinking toggle are not the same intervention.
- **Themes:** reasoning

<a id="c056"></a>

### C056 — u/FastHotEmu

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk0fdkpqjl/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk0fdkpqjl/)

- **Faithful contribution:** Says 3.8 27B works well even Q4 and suspects wrong model, engine or configuration.
- **Type:** counterexperience/hypothesis
- **Why relevant (assessment):** Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal. Tests whether effective serving defaults/behavior, rather than model name, explain failures.
- **Evidence quality:** E1 — first-person report without reproducible configuration/outcome data.
- **Open questions / verification gaps:** Working elsewhere does not establish OP's cause.
- **Transferability (inference):** Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence. Transfer the controlled comparison method; not an automatic requirement to migrate.
- **Themes:** weights, runtime, methodology

<a id="c057"></a>

### C057 — u/575_Inverse

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkfosnyfmp/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkfosnyfmp/)

- **Faithful contribution:** Suggests all three possibilities in C056 apply.
- **Type:** hypothesis
- **Why relevant (assessment):** Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal. Tests whether effective serving defaults/behavior, rather than model name, explain failures.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** No new supporting evidence.
- **Transferability (inference):** Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence. Transfer the controlled comparison method; not an automatic requirement to migrate.
- **Themes:** weights, runtime, methodology

<a id="c058"></a>

### C058 — u/FastHotEmu

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkw9v3yx0l/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkw9v3yx0l/)

- **Faithful contribution:** Claims vanilla llama.cpp plus an Unsloth 27B quant should run even if slowly.
- **Type:** setup opinion
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures. Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** No known-good command, versions or reproduction here.
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate. Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence.
- **Themes:** runtime, weights

<a id="c059"></a>

### C059 — u/Erik-Zandros

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwr6l585sbn/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwr6l585sbn/)

- **Faithful contribution:** Suspects oversized Claude documents and Q4 on 24GB; reports dual-3090 Q8 still below ChatGPT for research/reasoning, and suggests renting a larger model before expensive hardware.
- **Type:** experience/hypothesis/cost suggestion
- **Why relevant (assessment):** Separates configured context, occupied context, working headroom and compaction. Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** OP's quant and prompt occupancy unknown; research results do not establish coding accuracy; $30K recommendation unvalidated.
- **Transferability (inference):** Task/harness dependent; no universal minimum or fraction follows from this report. Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence.
- **Themes:** context, weights, workflow, economics, alternatives

<a id="c060"></a>

### C060 — u/Bagelsarenakeddonuts

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwjsxppu0f4/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwjsxppu0f4/)

- **Faithful contribution:** Reports tens of thousands of Rust lines using 5090 and a Swift 27B variant, passing tests and cloud-LLM review; suspects harness/quant.
- **Type:** coding experience
- **Why relevant (assessment):** Separates useful long reasoning, pathological loops and output/time budgets. Tests usable tool access, orchestration, protocol and prompt overhead.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** Exact Swift artifact, test suite, failure/repair rate and runtime not given.
- **Transferability (inference):** Task-specific tradeoff; a finetune and a base-model thinking toggle are not the same intervention. A suggested harness may change several variables; validate access, protocol and prompt budget separately.
- **Themes:** reasoning, harness, alternatives, workflow

<a id="c061"></a>

### C061 — u/InfiniteBlink

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkp1yk23kx/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkp1yk23kx/)

- **Faithful contribution:** Dual-3090 Q8 user asks how to combine cloud design/review with local coding; currently uses Hermes for household tasks.
- **Type:** question
- **Why relevant (assessment):** Tests scope, planning, verification and supervision as determinants of accepted work. Tests fit, residency/offload, shared memory and concurrency, not hardware-as-intelligence.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** What delegation workflow works and what token/time savings result?
- **Transferability (inference):** Applies as an evaluation/workflow pattern; autonomy and net benefit must be measured. OP uses a discrete3090; user has a different Apple unified-memory/MLX path. Do not copy memory/tok/s estimates.
- **Themes:** workflow, hardware

<a id="c062"></a>

### C062 — u/Biotot

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwljwqub34x/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwljwqub34x/)

- **Faithful contribution:** Reports Opus driving Qwen as a VS Code Copilot subagent, keeping it on task and terminating loops.
- **Type:** experience
- **Why relevant (assessment):** Tests scope, planning, verification and supervision as determinants of accepted work. Separates useful long reasoning, pathological loops and output/time budgets.
- **Evidence quality:** E1 — first-person report without reproducible configuration/outcome data.
- **Open questions / verification gaps:** How is local subagent routing configured and what success rate?
- **Transferability (inference):** Applies as an evaluation/workflow pattern; autonomy and net benefit must be measured. Task-specific tradeoff; a finetune and a base-model thinking toggle are not the same intervention.
- **Themes:** workflow, reasoning

<a id="c063"></a>

### C063 — u/InfiniteBlink

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwllh5zhr4z/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwllh5zhr4z/)

- **Faithful contribution:** Asks whether this hybrid approach substantially cuts cloud token usage.
- **Type:** question
- **Why relevant (assessment):** Evaluates elapsed time, senior attention, maintenance and accepted-work cost. Tests scope, planning, verification and supervision as determinants of accepted work.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** No numeric before/after accounting.
- **Transferability (inference):** Preference and task dependent; quoted throughput, prices and savings are not cost-effectiveness proof. Applies as an evaluation/workflow pattern; autonomy and net benefit must be measured.
- **Themes:** economics, workflow

<a id="c064"></a>

### C064 — u/Biotot

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm7jsn5dia/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm7jsn5dia/)

- **Faithful contribution:** Answers token savings are massive; uses Codex planning and Opus+Qwen execution, saying Copilot BYOK subagents work better than Codex in VS Code.
- **Type:** experience
- **Why relevant (assessment):** Evaluates elapsed time, senior attention, maintenance and accepted-work cost. Tests scope, planning, verification and supervision as determinants of accepted work.
- **Evidence quality:** E1 — first-person report without reproducible configuration/outcome data.
- **Open questions / verification gaps:** No measurements; product/version-specific integration claim.
- **Transferability (inference):** Preference and task dependent; quoted throughput, prices and savings are not cost-effectiveness proof. Applies as an evaluation/workflow pattern; autonomy and net benefit must be measured.
- **Themes:** economics, workflow, harness

<a id="c065"></a>

### C065 — u/Dubious-Decisions

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2ugj0vlia/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2ugj0vlia/)

- **Faithful contribution:** Asks how Copilot reliably selects a local subagent when UI only offers one model or automatic routing.
- **Type:** question
- **Why relevant (assessment):** Tests usable tool access, orchestration, protocol and prompt overhead. Tests scope, planning, verification and supervision as determinants of accepted work.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Configuration answer unavailable in this accessible exchange.
- **Transferability (inference):** A suggested harness may change several variables; validate access, protocol and prompt budget separately. Applies as an evaluation/workflow pattern; autonomy and net benefit must be measured.
- **Themes:** harness, workflow

<a id="c066"></a>

### C066 — u/Bagelsarenakeddonuts

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnexazbhyb/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnexazbhyb/)

- **Faithful contribution:** Uses BMAD/bmad-loop, immaculate Opus specs, Claude orchestration, Qwen scope precheck then fresh coder then independent quality check; reports three ninfer instances and shared-prefix caching on 5090.
- **Type:** detailed workflow experience
- **Why relevant (assessment):** Tests scope, planning, verification and supervision as determinants of accepted work. Tests usable tool access, orchestration, protocol and prompt overhead.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** Exact config/code and throughput per concurrency absent; independent same-model review may share blind spots.
- **Transferability (inference):** Applies as an evaluation/workflow pattern; autonomy and net benefit must be measured. A suggested harness may change several variables; validate access, protocol and prompt budget separately.
- **Themes:** workflow, harness, context, methodology

<a id="c067"></a>

### C067 — u/hotmerc007

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm337hwdr7/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm337hwdr7/)

- **Faithful contribution:** Asks C060's author for a reproducible beginner configuration.
- **Type:** question
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures. Tests scope, planning, verification and supervision as determinants of accepted work.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Later pointer exists, but exact full recipe remains incomplete.
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate. Applies as an evaluation/workflow pattern; autonomy and net benefit must be measured.
- **Themes:** runtime, workflow

<a id="c069"></a>

### C069 — u/Apprehensive_Stop314

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwjsld6nj50/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwjsld6nj50/)

- **Faithful contribution:** Asks exact quant, engine and settings.
- **Type:** diagnostic questions
- **Why relevant (assessment):** Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal. Tests whether effective serving defaults/behavior, rather than model name, explain failures.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** OP has not supplied these in the available original post.
- **Transferability (inference):** Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence. Transfer the controlled comparison method; not an automatic requirement to migrate.
- **Themes:** weights, runtime, sampling

<a id="c070"></a>

### C070 — u/dreamyrhodes

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx01c8e0bz7/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx01c8e0bz7/)

- **Faithful contribution:** Says 27B requires junior-style incremental tasks, explicit steps and summaries rather than a frontier drop-in.
- **Type:** workflow recommendation
- **Why relevant (assessment):** Tests scope, planning, verification and supervision as determinants of accepted work. Separates configured context, occupied context, working headroom and compaction.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Task-specific net time benefit needs measurement.
- **Transferability (inference):** Applies as an evaluation/workflow pattern; autonomy and net benefit must be measured. Task/harness dependent; no universal minimum or fraction follows from this report.
- **Themes:** workflow, context

<a id="c071"></a>

### C071 — u/ConsiderationFair657

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxex4gs9k83/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxex4gs9k83/)

- **Faithful contribution:** Advocates manageable steps and rejects one-prompt magic for small models.
- **Type:** workflow opinion
- **Why relevant (assessment):** Tests scope, planning, verification and supervision as determinants of accepted work.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** What task size is effective and how much supervision is needed?
- **Transferability (inference):** Applies as an evaluation/workflow pattern; autonomy and net benefit must be measured.
- **Themes:** workflow

<a id="c072"></a>

### C072 — u/Abject-Kitchen3198

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1lwdh42hs/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1lwdh42hs/)

- **Faithful contribution:** Asks if detailed briefing/review of a junior-like model takes more senior time than coding manually.
- **Type:** economic counterquestion
- **Why relevant (assessment):** Tests scope, planning, verification and supervision as determinants of accepted work. Evaluates elapsed time, senior attention, maintenance and accepted-work cost.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Human time saved versus direct implementation remains unanswered quantitatively.
- **Transferability (inference):** Applies as an evaluation/workflow pattern; autonomy and net benefit must be measured. Preference and task dependent; quoted throughput, prices and savings are not cost-effectiveness proof.
- **Themes:** workflow, economics

<a id="c073"></a>

### C073 — u/dreamyrhodes

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2upo78vxe/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2upo78vxe/)

- **Faithful contribution:** Uses interactive ask/design/correct/implement/test cycles and says decomposition is still less work than manual coding.
- **Type:** workflow experience
- **Why relevant (assessment):** Tests scope, planning, verification and supervision as determinants of accepted work. Separates configured context, occupied context, working headroom and compaction.
- **Evidence quality:** E1 — first-person report without reproducible configuration/outcome data.
- **Open questions / verification gaps:** No measured time comparison or representative task set.
- **Transferability (inference):** Applies as an evaluation/workflow pattern; autonomy and net benefit must be measured. Task/harness dependent; no universal minimum or fraction follows from this report.
- **Themes:** workflow, context

<a id="c074"></a>

### C074 — u/jefoce

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwjvtwq3v6r/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwjvtwq3v6r/)

- **Faithful contribution:** Reports focused OpenCode subagents, Opus planning, XML+CAPS prompts, patched llama.cpp, Q8_L/F16 KV on 5080+5090; Q4 initially worked with more tool errors and earlier drift.
- **Type:** detailed coding experience
- **Why relevant (assessment):** Tests scope, planning, verification and supervision as determinants of accepted work. Tests usable tool access, orchestration, protocol and prompt overhead.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** XML/CAPS advantage unablated; patches, tasks and matched traces absent; hardware is much larger than OP's.
- **Transferability (inference):** Applies as an evaluation/workflow pattern; autonomy and net benefit must be measured. A suggested harness may change several variables; validate access, protocol and prompt budget separately.
- **Themes:** workflow, harness, weights, kv, context

<a id="c075"></a>

### C075 — u/Express_Quail_1493

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwoqd3a6isj/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwoqd3a6isj/)

- **Faithful contribution:** Suggests looping reflects template or token-streaming mismatch and recommends LM Studio+Bionic before raw llama.cpp.
- **Type:** hypotheses/recommendation
- **Why relevant (assessment):** Tests prompt rendering and tool-call serialization/stop-token compatibility. Tests usable tool access, orchestration, protocol and prompt overhead.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** No trace shows template/streaming error; distinguish long coherent thinking from repetition.
- **Transferability (inference):** Inspect the applied template and wire trace before replacing templates. A suggested harness may change several variables; validate access, protocol and prompt budget separately.
- **Themes:** template, harness, reasoning, runtime

<a id="c076"></a>

### C076 — u/Lopsided-Comedian-32

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwsy2p3j5pe/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwsy2p3j5pe/)

- **Faithful contribution:** Claims Ollama defaults can undercut context and recommends an explicit context setting; says Swift reduces overthinking roughly twofold.
- **Type:** configuration claim/variant recommendation
- **Why relevant (assessment):** Separates configured context, occupied context, working headroom and compaction. Separates useful long reasoning, pathological loops and output/time budgets.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Effective OP context and output caps unknown; speed claim lacks matched logs.
- **Transferability (inference):** Task/harness dependent; no universal minimum or fraction follows from this report. Task-specific tradeoff; a finetune and a base-model thinking toggle are not the same intervention.
- **Themes:** context, reasoning, runtime

<a id="c077"></a>

### C077 — u/tinny66666

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwrouvqe5r6/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwrouvqe5r6/)

- **Faithful contribution:** Says a wrong/default template can cause looping and errors.
- **Type:** technical hypothesis
- **Why relevant (assessment):** Tests prompt rendering and tool-call serialization/stop-token compatibility. Separates useful long reasoning, pathological loops and output/time budgets.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Need rendered prompt and actual applied template to test.
- **Transferability (inference):** Inspect the applied template and wire trace before replacing templates. Task-specific tradeoff; a finetune and a base-model thinking toggle are not the same intervention.
- **Themes:** template, reasoning

<a id="c078"></a>

### C078 — u/Smooth-Television-48

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rws5h4gfrtx/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rws5h4gfrtx/)

- **Faithful contribution:** Says aggressive KV quantization can cause the same behavior.
- **Type:** technical hypothesis
- **Why relevant (assessment):** Tests cache precision versus available context and fidelity. Separates useful long reasoning, pathological loops and output/time budgets.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Exact cache precision and controlled comparison absent.
- **Transferability (inference):** Compare matched tasks with explicit cache scheme; different architectures/caches may respond differently. Task-specific tradeoff; a finetune and a base-model thinking toggle are not the same intervention.
- **Themes:** kv, reasoning

<a id="c079"></a>

### C079 — u/an0maly33

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwy776p4ski/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwy776p4ski/)

- **Faithful contribution:** Reports 27B spiraling after context grows despite settings changes and Pi; says FlashNext via Strata is more concise but not deeply coding-tested.
- **Type:** negative experience/counterexample
- **Why relevant (assessment):** Separates configured context, occupied context, working headroom and compaction. Separates useful long reasoning, pathological loops and output/time budgets.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** Unknown weights/KV and traces; a Pi recommendation alone does not rule out loops.
- **Transferability (inference):** Task/harness dependent; no universal minimum or fraction follows from this report. Task-specific tradeoff; a finetune and a base-model thinking toggle are not the same intervention.
- **Themes:** context, reasoning, harness, alternatives

<a id="c080"></a>

### C080 — u/Extreme-Childhood251

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx5lbdb6zz7/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx5lbdb6zz7/)

- **Faithful contribution:** Reports an alternative much better than 27B but still worse/slower than Claude; mentions an expected upcoming Qwen release.
- **Type:** experience/prediction
- **Why relevant (assessment):** Provides an alternative-model/runtime lead, not a demonstrated fix for unchanged target model. Evaluates elapsed time, senior attention, maintenance and accepted-work cost.
- **Evidence quality:** E1 — first-person report without reproducible configuration/outcome data.
- **Open questions / verification gaps:** Alternative inferred from surrounding text, not proven parent; future release not verified.
- **Transferability (inference):** Changing model changes the hypothesis; establish a working baseline and fit before considering this lead. Preference and task dependent; quoted throughput, prices and savings are not cost-effectiveness proof.
- **Themes:** alternatives, economics

<a id="c081"></a>

### C081 — u/pioo84

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx0v6grhztx/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx0v6grhztx/)

- **Faithful contribution:** Reports 27B planned/designed/coded Android apps with appropriate tools and pipelines, before moving to FlashNext.
- **Type:** experience
- **Why relevant (assessment):** Tests scope, planning, verification and supervision as determinants of accepted work. Tests usable tool access, orchestration, protocol and prompt overhead.
- **Evidence quality:** E1 — first-person report without reproducible configuration/outcome data.
- **Open questions / verification gaps:** Specific harness, hardware and validation unknown.
- **Transferability (inference):** Applies as an evaluation/workflow pattern; autonomy and net benefit must be measured. A suggested harness may change several variables; validate access, protocol and prompt budget separately.
- **Themes:** workflow, harness, alternatives

<a id="c082"></a>

### C082 — u/colonelx_

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2kurtuk6c/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2kurtuk6c/)

- **Faithful contribution:** Asks for hardware specifications and coding agent.
- **Type:** question
- **Why relevant (assessment):** Tests usable tool access, orchestration, protocol and prompt overhead. Tests fit, residency/offload, shared memory and concurrency, not hardware-as-intelligence.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** No reply linked by parent metadata in Atom.
- **Transferability (inference):** A suggested harness may change several variables; validate access, protocol and prompt budget separately. OP uses a discrete3090; user has a different Apple unified-memory/MLX path. Do not copy memory/tok/s estimates.
- **Themes:** harness, hardware

<a id="c083"></a>

### C083 — u/Pablo_the_brave

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6zhpttmzn/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6zhpttmzn/)

- **Faithful contribution:** Requests temperature/top_p and server, emphasizing agent setup.
- **Type:** diagnostic questions
- **Why relevant (assessment):** Tests generation controls as a cause of unstable or looping output. Tests whether effective serving defaults/behavior, rather than model name, explain failures.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Missing values still prevent causal attribution; dismissive tone adds no evidence.
- **Transferability (inference):** Use exact model/mode-recommended settings as a measured baseline, not a universal numeric recipe. Transfer the controlled comparison method; not an automatic requirement to migrate.
- **Themes:** sampling, runtime, harness

<a id="c084"></a>

### C084 — u/InsurmountableMind

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx81rvuajdu/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx81rvuajdu/)

- **Faithful contribution:** Emphasizes orchestration controlling data flow.
- **Type:** technical opinion
- **Why relevant (assessment):** Tests usable tool access, orchestration, protocol and prompt overhead. Tests scope, planning, verification and supervision as determinants of accepted work.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** No concrete implementation or measurement.
- **Transferability (inference):** A suggested harness may change several variables; validate access, protocol and prompt budget separately. Applies as an evaluation/workflow pattern; autonomy and net benefit must be measured.
- **Themes:** harness, workflow

<a id="c085"></a>

### C085 — u/Mysterious_Prune415

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwqh6f98t5u/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwqh6f98t5u/)

- **Faithful contribution:** Suggests Pi and warns a bloated Claude Code harness can consume a 128K budget.
- **Type:** recommendation
- **Why relevant (assessment):** Tests usable tool access, orchestration, protocol and prompt overhead. Separates configured context, occupied context, working headroom and compaction.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Actual harness prompt overhead not measured here.
- **Transferability (inference):** A suggested harness may change several variables; validate access, protocol and prompt budget separately. Task/harness dependent; no universal minimum or fraction follows from this report.
- **Themes:** harness, context

<a id="c089"></a>

### C089 — u/yellowsockss

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm9d04q3z8/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm9d04q3z8/)

- **Faithful contribution:** Places Qwen 27B far below Sonnet and claims 400–500B is the closest scale.
- **Type:** capability opinion
- **Why relevant (assessment):** Provides an alternative-model/runtime lead, not a demonstrated fix for unchanged target model. Evaluates elapsed time, senior attention, maintenance and accepted-work cost.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** No task-matched benchmark; size alone cannot rank deployment utility.
- **Transferability (inference):** Changing model changes the hypothesis; establish a working baseline and fit before considering this lead. Preference and task dependent; quoted throughput, prices and savings are not cost-effectiveness proof.
- **Themes:** alternatives, economics

<a id="c090"></a>

### C090 — u/former_farmer

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwjvpbzay79/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwjvpbzay79/)

- **Faithful contribution:** Asks quant/thinking and prescribes xhigh with ideally Q6+.
- **Type:** diagnostic question/prescription
- **Why relevant (assessment):** Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal. Separates useful long reasoning, pathological loops and output/time budgets.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Conflicts with lower-thinking successes; must ablate on task/time budget.
- **Transferability (inference):** Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence. Task-specific tradeoff; a finetune and a base-model thinking toggle are not the same intervention.
- **Themes:** weights, reasoning

<a id="c091"></a>

### C091 — u/575_Inverse

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkal81uc9s/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkal81uc9s/)

- **Faithful contribution:** Doubts 24GB can exceed Q4 weights and 128K Q8 KV; suspects multiple setup faults.
- **Type:** capacity hypothesis
- **Why relevant (assessment):** Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal. Tests cache precision versus available context and fidelity.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Actual weight/cache bytes, reservations and offload not known.
- **Transferability (inference):** Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence. Compare matched tasks with explicit cache scheme; different architectures/caches may respond differently.
- **Themes:** weights, kv, hardware, context

<a id="c092"></a>

### C092 — u/LegitimateCopy7

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnvfaelg2p/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnvfaelg2p/)

- **Faithful contribution:** Suspects RAM overflow or a poor quant when fitting 27B+128K in 24GB.
- **Type:** capacity hypothesis/runtime criticism
- **Why relevant (assessment):** Tests fit, residency/offload, shared memory and concurrency, not hardware-as-intelligence. Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Overflow would primarily affect speed; corruption/quality cause not demonstrated.
- **Transferability (inference):** OP uses a discrete3090; user has a different Apple unified-memory/MLX path. Do not copy memory/tok/s estimates. Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence.
- **Themes:** hardware, weights, context, runtime

<a id="c093"></a>

### C093 — u/soulman901

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwo8dn4e6xt/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwo8dn4e6xt/)

- **Faithful contribution:** Reports games including a Pac-Man clone on M4 Pro 48GB and links a screenshot.
- **Type:** experience
- **Why relevant (assessment):** Tests fit, residency/offload, shared memory and concurrency, not hardware-as-intelligence. Tests scope, planning, verification and supervision as determinants of accepted work.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** Screenshot not inspected; tests and exact model settings absent.
- **Transferability (inference):** OP uses a discrete3090; user has a different Apple unified-memory/MLX path. Do not copy memory/tok/s estimates. Applies as an evaluation/workflow pattern; autonomy and net benefit must be measured.
- **Themes:** hardware, workflow

<a id="c094"></a>

### C094 — u/Creative_Bookkeeper9

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwwr9gmhxnl/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwwr9gmhxnl/)

- **Faithful contribution:** Uses Pi/custom prompts with xhigh and 200–220K on a 5090; recommends ninfer on 3090 and lazy discovery of tools to save context.
- **Type:** experience/recommendation
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures. Separates useful long reasoning, pathological loops and output/time budgets.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** 150K minimum and no-reduced-thinking prescriptions are personal judgments, not universal requirements.
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate. Task-specific tradeoff; a finetune and a base-model thinking toggle are not the same intervention.
- **Themes:** runtime, reasoning, context, harness

<a id="c095"></a>

### C095 — u/Number1OchoaHater

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwjoz6t5h2c/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwjoz6t5h2c/)

- **Faithful contribution:** Says Sonnet and 27B differ greatly and asks engine/harness.
- **Type:** diagnostic question/capability caution
- **Why relevant (assessment):** Tests usable tool access, orchestration, protocol and prompt overhead. Tests whether effective serving defaults/behavior, rather than model name, explain failures.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** No actual OP harness or comparative evidence.
- **Transferability (inference):** A suggested harness may change several variables; validate access, protocol and prompt budget separately. Transfer the controlled comparison method; not an automatic requirement to migrate.
- **Themes:** harness, runtime, economics

<a id="c096"></a>

### C096 — u/wegster

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkedh17hr6/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkedh17hr6/)

- **Faithful contribution:** Recommends dynamic/mixed Q4 and Pi; reports real-repo 27B/QFN tests and Cline failures, QFN near Sonnet in own ~100K LOC repos.
- **Type:** experience/recommendation
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures. Tests usable tool access, orchestration, protocol and prompt overhead.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** No artifacts or task definitions; repository LOC is not context occupancy.
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate. A suggested harness may change several variables; validate access, protocol and prompt budget separately.
- **Themes:** runtime, harness, weights, alternatives

<a id="c097"></a>

### C097 — u/Oli_Luck

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwl16mys6n4/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwl16mys6n4/)

- **Faithful contribution:** Requests weight/KV quant and temperature, plus a concrete task; recommends planned local files, small steps and an auditor role.
- **Type:** diagnostic questions/workflow
- **Why relevant (assessment):** Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal. Tests cache precision versus available context and fidelity.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Exact inputs/settings and independent evidence still absent.
- **Transferability (inference):** Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence. Compare matched tasks with explicit cache scheme; different architectures/caches may respond differently.
- **Themes:** weights, kv, sampling, workflow

<a id="c098"></a>

### C098 — u/michinya

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwtki99rjxh/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwtki99rjxh/)

- **Faithful contribution:** Engineering-team operator says GLM5.3 NVFP4 is their minimum for complex codebases; 27B only for defined custom workflows; stresses gateway and maintenance work.
- **Type:** team experience
- **Why relevant (assessment):** Tests usable tool access, orchestration, protocol and prompt overhead. Tests scope, planning, verification and supervision as determinants of accepted work.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** Their workloads/resource budget may differ; gateway details and measured success rates not supplied.
- **Transferability (inference):** A suggested harness may change several variables; validate access, protocol and prompt budget separately. Applies as an evaluation/workflow pattern; autonomy and net benefit must be measured.
- **Themes:** harness, workflow, economics, alternatives

<a id="c099"></a>

### C099 — u/stianhoiland

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwp0tk50k2t/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwp0tk50k2t/)

- **Faithful contribution:** Reports slow but solid FlashNext IQ3_S on Strata with 4070 Super 12GB/32GB RAM and 262144 context; provides configuration with k8v4 and 20480 resident KV.
- **Type:** detailed alternative configuration
- **Why relevant (assessment):** Provides an alternative-model/runtime lead, not a demonstrated fix for unchanged target model. Tests whether effective serving defaults/behavior, rather than model name, explain failures.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** No code benchmark; large configured context is not fully resident/effectively used context; compare disk/offload costs.
- **Transferability (inference):** Changing model changes the hypothesis; establish a working baseline and fit before considering this lead. Transfer the controlled comparison method; not an automatic requirement to migrate.
- **Themes:** alternatives, runtime, hardware, kv, context

<a id="c100"></a>

### C100 — u/mozillazing

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwqy3w046n6/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwqy3w046n6/)

- **Faithful contribution:** Asks how a 125B/262K setup fits 12GB VRAM and 32GB RAM.
- **Type:** capacity question
- **Why relevant (assessment):** Tests fit, residency/offload, shared memory and concurrency, not hardware-as-intelligence. Separates configured context, occupied context, working headroom and compaction.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** What storage/offload architecture and real workload performance make this viable?
- **Transferability (inference):** OP uses a discrete3090; user has a different Apple unified-memory/MLX path. Do not copy memory/tok/s estimates. Task/harness dependent; no universal minimum or fraction follows from this report.
- **Themes:** hardware, context, alternatives

<a id="c101"></a>

### C101 — u/Pixelplanet5

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx84ajmde3p/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx84ajmde3p/)

- **Faithful contribution:** Attributes C099-style fitting to SSD offload and warns it will be slow.
- **Type:** capacity explanation
- **Why relevant (assessment):** Tests fit, residency/offload, shared memory and concurrency, not hardware-as-intelligence. Provides an alternative-model/runtime lead, not a demonstrated fix for unchanged target model.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** No measured I/O or speed in this comment; implementation details not verified.
- **Transferability (inference):** OP uses a discrete3090; user has a different Apple unified-memory/MLX path. Do not copy memory/tok/s estimates. Changing model changes the hypothesis; establish a working baseline and fit before considering this lead.
- **Themes:** hardware, alternatives

<a id="c102"></a>

### C102 — u/Smooth-Television-48

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwru2sget2c/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwru2sget2c/)

- **Faithful contribution:** Raises disk load and SSD-wear concerns about offloading.
- **Type:** risk question
- **Why relevant (assessment):** Tests fit, residency/offload, shared memory and concurrency, not hardware-as-intelligence. Evaluates elapsed time, senior attention, maintenance and accepted-work cost.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Reads versus writes and actual wear are not established; do not imply reads exhaust write endurance.
- **Transferability (inference):** OP uses a discrete3090; user has a different Apple unified-memory/MLX path. Do not copy memory/tok/s estimates. Preference and task dependent; quoted throughput, prices and savings are not cost-effectiveness proof.
- **Themes:** hardware, economics

<a id="c103"></a>

### C103 — u/curiouselectron

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwp94xret9f/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwp94xret9f/)

- **Faithful contribution:** Asks the alternative setup's actual token rates.
- **Type:** question
- **Why relevant (assessment):** Tests fit, residency/offload, shared memory and concurrency, not hardware-as-intelligence. Evaluates elapsed time, senior attention, maintenance and accepted-work cost.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Need prefill, decode and task wall time, not only nominal fit.
- **Transferability (inference):** OP uses a discrete3090; user has a different Apple unified-memory/MLX path. Do not copy memory/tok/s estimates. Preference and task dependent; quoted throughput, prices and savings are not cost-effectiveness proof.
- **Themes:** hardware, economics

<a id="c104"></a>

### C104 — u/yourself88xbl

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpv0qg2dut/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpv0qg2dut/)

- **Faithful contribution:** Asks use cases and whether the alternative has been tested for code generation.
- **Type:** question
- **Why relevant (assessment):** Tests scope, planning, verification and supervision as determinants of accepted work. Provides an alternative-model/runtime lead, not a demonstrated fix for unchanged target model.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Coding applicability remains unclear for the cited configuration.
- **Transferability (inference):** Applies as an evaluation/workflow pattern; autonomy and net benefit must be measured. Changing model changes the hypothesis; establish a working baseline and fit before considering this lead.
- **Themes:** workflow, alternatives

<a id="c105"></a>

### C105 — u/Comfortable-Crew-919

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwss0z7myed/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwss0z7myed/)

- **Faithful contribution:** Reports similar slow setup improved after 128GB DDR5 upgrade, claiming 75–85 tok/s IQ3_S and ~55 tok/s Unsloth Q4_K_XL at 128K; plans second 4070.
- **Type:** experience
- **Why relevant (assessment):** Tests fit, residency/offload, shared memory and concurrency, not hardware-as-intelligence. Provides an alternative-model/runtime lead, not a demonstrated fix for unchanged target model.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** Exact workload/config not provided; a planned upgrade is not an observed result.
- **Transferability (inference):** OP uses a discrete3090; user has a different Apple unified-memory/MLX path. Do not copy memory/tok/s estimates. Changing model changes the hypothesis; establish a working baseline and fit before considering this lead.
- **Themes:** hardware, alternatives, economics

<a id="c106"></a>

### C106 — u/FragmentedHeap

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwr2xodjqn8/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwr2xodjqn8/)

- **Faithful contribution:** Suggests agent-assisted llama-swap/vLLM setup and benchmarking; separately reports FlashNext IQ4 via Strata on R9700 at 90 tok/s and ~3K prefill.
- **Type:** experience/recommendation
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures. Provides an alternative-model/runtime lead, not a demonstrated fix for unchanged target model.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** Multiple products/hardware make transfer indirect; no matched quality test.
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate. Changing model changes the hypothesis; establish a working baseline and fit before considering this lead.
- **Themes:** runtime, alternatives, methodology

<a id="c107"></a>

### C107 — u/aithosrds

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwuriw2j0dg/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwuriw2j0dg/)

- **Faithful contribution:** Recommends at least Q4, a fine-tune with low/off thinking, and keeping a 128K session roughly below 64K with subagents.
- **Type:** reasoning/workflow opinion
- **Why relevant (assessment):** Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal. Separates useful long reasoning, pathological loops and output/time budgets.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** 50% threshold and reasoning prescription unvalidated and directly disputed below.
- **Transferability (inference):** Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence. Task-specific tradeoff; a finetune and a base-model thinking toggle are not the same intervention.
- **Themes:** weights, reasoning, context, workflow

<a id="c108"></a>

### C108 — u/Patient_Tea_401

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwx9oodgo10/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwx9oodgo10/)

- **Faithful contribution:** Reports 24/7 oMLX oQ4-FP16-MTP full-context agents eventually solving tasks after long reasoning; argues unquantized KV and ~64GB are needed.
- **Type:** counterexperience
- **Why relevant (assessment):** Separates useful long reasoning, pathological loops and output/time budgets. Tests cache precision versus available context and fidelity.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** No logs or ablations; 64GB minimum is not general, and successful completion cost is unquantified.
- **Transferability (inference):** Task-specific tradeoff; a finetune and a base-model thinking toggle are not the same intervention. Compare matched tasks with explicit cache scheme; different architectures/caches may respond differently.
- **Themes:** reasoning, kv, context, hardware

<a id="c109"></a>

### C109 — u/Dracuvlad

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwyor0r0p7m/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwyor0r0p7m/)

- **Faithful contribution:** M1 Max 64GB user asks for full setup and current performance.
- **Type:** question
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures. Tests fit, residency/offload, shared memory and concurrency, not hardware-as-intelligence.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Configuration is partly answered at C110; quantitative speed/success remains missing.
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate. OP uses a discrete3090; user has a different Apple unified-memory/MLX path. Do not copy memory/tok/s estimates.
- **Themes:** runtime, hardware

<a id="c110"></a>

### C110 — u/Patient_Tea_401

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1egufux7p/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1egufux7p/)

- **Faithful contribution:** Describes M1 Max Studio 64GB, oMLX self-quant/Jundot oQ4-FP16-MTP, standard settings and remote Claude Code Anthropic API; values overnight thoroughness and retained context.
- **Type:** detailed experience
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures. Tests usable tool access, orchestration, protocol and prompt overhead.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** Exact revision, prompts, compaction behavior and task metrics absent; preference for quality over speed is not a controlled conclusion.
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate. A suggested harness may change several variables; validate access, protocol and prompt budget separately.
- **Themes:** runtime, harness, reasoning, context, kv

<a id="c111"></a>

### C111 — u/Creative_Bookkeeper9

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwwfwq3dvab/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwwfwq3dvab/)

- **Faithful contribution:** Argues no-thinking is far worse than even low thinking.
- **Type:** reasoning disagreement
- **Why relevant (assessment):** Separates useful long reasoning, pathological loops and output/time budgets.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Which tasks, model variant and measured error rates?
- **Transferability (inference):** Task-specific tradeoff; a finetune and a base-model thinking toggle are not the same intervention.
- **Themes:** reasoning

<a id="c112"></a>

### C112 — u/Patient_Tea_401

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwzqa7lprxf/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwzqa7lprxf/)

- **Faithful contribution:** Says reasoning is necessary for agentic coding/reverse engineering.
- **Type:** reasoning disagreement
- **Why relevant (assessment):** Separates useful long reasoning, pathological loops and output/time budgets. Tests scope, planning, verification and supervision as determinants of accepted work.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Does this refer to any thinking versus highest effort? No controlled evidence.
- **Transferability (inference):** Task-specific tradeoff; a finetune and a base-model thinking toggle are not the same intervention. Applies as an evaluation/workflow pattern; autonomy and net benefit must be measured.
- **Themes:** reasoning, workflow

<a id="c113"></a>

### C113 — u/opravdin

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx04jlyo2w2/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx04jlyo2w2/)

- **Faithful contribution:** Suggests no-thinking for fast code lookup on behalf of a stronger agent.
- **Type:** task-routing suggestion
- **Why relevant (assessment):** Separates useful long reasoning, pathological loops and output/time budgets. Tests scope, planning, verification and supervision as determinants of accepted work.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Lookup correctness and actual token/time savings need validation.
- **Transferability (inference):** Task-specific tradeoff; a finetune and a base-model thinking toggle are not the same intervention. Applies as an evaluation/workflow pattern; autonomy and net benefit must be measured.
- **Themes:** reasoning, workflow

<a id="c114"></a>

### C114 — u/caylyn953

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwyteph4omb/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwyteph4omb/)

- **Faithful contribution:** Says single 3090 cannot reach Haiku5.5 and frontier expectations keep moving.
- **Type:** capability opinion/prediction
- **Why relevant (assessment):** Tests fit, residency/offload, shared memory and concurrency, not hardware-as-intelligence. Evaluates elapsed time, senior attention, maintenance and accepted-work cost.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** No task-specific measurements; future comparison is speculative.
- **Transferability (inference):** OP uses a discrete3090; user has a different Apple unified-memory/MLX path. Do not copy memory/tok/s estimates. Preference and task dependent; quoted throughput, prices and savings are not cost-effectiveness proof.
- **Themes:** hardware, economics

<a id="c115"></a>

### C115 — u/dsdt

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwjqzdeiqw3/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwjqzdeiqw3/)

- **Faithful contribution:** Says local Qwen3.8-27B fixes bugs Claude left.
- **Type:** experience/counterexample
- **Why relevant (assessment):** Tests scope, planning, verification and supervision as determinants of accepted work. Improves causal identification, failure visibility and comparison validity.
- **Evidence quality:** E1 — first-person report without reproducible configuration/outcome data.
- **Open questions / verification gaps:** No bug/reproduction/test evidence; fixing different bugs does not establish overall parity.
- **Transferability (inference):** Applies as an evaluation/workflow pattern; autonomy and net benefit must be measured. Transfer measurement discipline, not the commenters root-cause certainty.
- **Themes:** workflow, methodology

<a id="c116"></a>

### C116 — u/575_Inverse

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkbl90vdlw/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkbl90vdlw/)

- **Faithful contribution:** Agrees Qwen is thorough at code revision/testing.
- **Type:** experience
- **Why relevant (assessment):** Tests scope, planning, verification and supervision as determinants of accepted work. Improves causal identification, failure visibility and comparison validity.
- **Evidence quality:** E1 — first-person report without reproducible configuration/outcome data.
- **Open questions / verification gaps:** No settings or concrete tests.
- **Transferability (inference):** Applies as an evaluation/workflow pattern; autonomy and net benefit must be measured. Transfer measurement discipline, not the commenters root-cause certainty.
- **Themes:** workflow, methodology

<a id="c117"></a>

### C117 — u/rkcth

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk8m8e88f5/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk8m8e88f5/)

- **Faithful contribution:** Asks full model name, doubts RAM/VRAM capacity and recommends 64–128GB then FlashNext 3-bit via Strata.
- **Type:** capacity question/upgrade recommendation
- **Why relevant (assessment):** Tests fit, residency/offload, shared memory and concurrency, not hardware-as-intelligence. Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** No measured OP allocation; RAM price/platform capacity and model fit not verified.
- **Transferability (inference):** OP uses a discrete3090; user has a different Apple unified-memory/MLX path. Do not copy memory/tok/s estimates. Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence.
- **Themes:** hardware, weights, alternatives, economics

<a id="c118"></a>

### C118 — u/DickVonShit

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkwhr0xfvk/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkwhr0xfvk/)

- **Faithful contribution:** Recommends Swift1.5 to shorten high-effort thinking; reports needing extra specificity and solid llama.cpp+OpenCode use; distinguishes hardware capacity/speed from model intelligence.
- **Type:** experience/reasoning recommendation
- **Why relevant (assessment):** Separates useful long reasoning, pathological loops and output/time budgets. Tests usable tool access, orchestration, protocol and prompt overhead.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** Swift equivalence and performance need matched tests; reasoning level OP uses is unknown.
- **Transferability (inference):** Task-specific tradeoff; a finetune and a base-model thinking toggle are not the same intervention. A suggested harness may change several variables; validate access, protocol and prompt budget separately.
- **Themes:** reasoning, harness, hardware, workflow

<a id="c119"></a>

### C119 — u/Longjumping-Road4113

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwojejtbf6p/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwojejtbf6p/)

- **Faithful contribution:** Asks whether OP tried Strata with an optimized Qwen MoE coder.
- **Type:** alternative question
- **Why relevant (assessment):** Provides an alternative-model/runtime lead, not a demonstrated fix for unchanged target model. Tests whether effective serving defaults/behavior, rather than model name, explain failures.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Exact model/artifact and resource requirements unspecified.
- **Transferability (inference):** Changing model changes the hypothesis; establish a working baseline and fit before considering this lead. Transfer the controlled comparison method; not an automatic requirement to migrate.
- **Themes:** alternatives, runtime

<a id="c120"></a>

### C120 — u/Emergency-Quiet3210

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxf578ergkj/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxf578ergkj/)

- **Faithful contribution:** Asks harness; says 27B suffices outside one-shot pipeline demands and recommends LM Studio+Pi or OpenCode, favoring Pi's light footprint.
- **Type:** experience/recommendation/question
- **Why relevant (assessment):** Tests usable tool access, orchestration, protocol and prompt overhead. Tests scope, planning, verification and supervision as determinants of accepted work.
- **Evidence quality:** E1 — first-person report without reproducible configuration/outcome data.
- **Open questions / verification gaps:** No measured prompt overhead or coding suite.
- **Transferability (inference):** A suggested harness may change several variables; validate access, protocol and prompt budget separately. Applies as an evaluation/workflow pattern; autonomy and net benefit must be measured.
- **Themes:** harness, workflow

<a id="c121"></a>

### C121 — u/flarpflarpflarpflarp

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwjpskbwx41/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwjpskbwx41/)

- **Faithful contribution:** Suggests Strata.
- **Type:** recommendation
- **Why relevant (assessment):** Provides an alternative-model/runtime lead, not a demonstrated fix for unchanged target model. Tests whether effective serving defaults/behavior, rather than model name, explain failures.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** No model, configuration or supporting outcome.
- **Transferability (inference):** Changing model changes the hypothesis; establish a working baseline and fit before considering this lead. Transfer the controlled comparison method; not an automatic requirement to migrate.
- **Themes:** alternatives, runtime

<a id="c122"></a>

### C122 — u/rkcth

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk0xdldfvk/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk0xdldfvk/)

- **Faithful contribution:** Warns 32GB RAM is tight and proposes 64GB for FlashNext via Strata.
- **Type:** capacity opinion
- **Why relevant (assessment):** Tests fit, residency/offload, shared memory and concurrency, not hardware-as-intelligence. Provides an alternative-model/runtime lead, not a demonstrated fix for unchanged target model.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Actual fit/latency and exact quant are not demonstrated.
- **Transferability (inference):** OP uses a discrete3090; user has a different Apple unified-memory/MLX path. Do not copy memory/tok/s estimates. Changing model changes the hypothesis; establish a working baseline and fit before considering this lead.
- **Themes:** hardware, alternatives

<a id="c123"></a>

### C123 — u/skifreek

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk0vrcznol/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk0vrcznol/)

- **Faithful contribution:** 32GB-VRAM user reports loops on LM Studio+OpenCode after trying 32K context and lowering xhigh to medium; asks OP's inference/coding stack.
- **Type:** negative experience/questions
- **Why relevant (assessment):** Separates configured context, occupied context, working headroom and compaction. Separates useful long reasoning, pathological loops and output/time budgets.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** No recipe found; actual weight/KV quant, template and failing trace missing.
- **Transferability (inference):** Task/harness dependent; no universal minimum or fraction follows from this report. Task-specific tradeoff; a finetune and a base-model thinking toggle are not the same intervention.
- **Themes:** context, reasoning, runtime, harness, hardware

<a id="c124"></a>

### C124 — u/Perfect-Campaign9551

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk9qbqb350/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk9qbqb350/)

- **Faithful contribution:** Claims 33K is insufficient for any programming task.
- **Type:** context opinion
- **Why relevant (assessment):** Separates configured context, occupied context, working headroom and compaction. Tests scope, planning, verification and supervision as determinants of accepted work.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Overbroad; small-task counterexamples and actual harness overhead must be tested.
- **Transferability (inference):** Task/harness dependent; no universal minimum or fraction follows from this report. Applies as an evaluation/workflow pattern; autonomy and net benefit must be measured.
- **Themes:** context, workflow

<a id="c125"></a>

### C125 — u/skifreek

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlb07ndaqs/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlb07ndaqs/)

- **Faithful contribution:** Reports VRAM spill reduced speed from ~6 to ~1 tok/s.
- **Type:** speed experience
- **Why relevant (assessment):** Tests fit, residency/offload, shared memory and concurrency, not hardware-as-intelligence. Separates configured context, occupied context, working headroom and compaction.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** No allocation/prefill trace; identifies latency, not proven intrinsic reasoning degradation.
- **Transferability (inference):** OP uses a discrete3090; user has a different Apple unified-memory/MLX path. Do not copy memory/tok/s estimates. Task/harness dependent; no universal minimum or fraction follows from this report.
- **Themes:** hardware, context, economics

<a id="c126"></a>

### C126 — u/Badger-Purple

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmbd3lpy8y/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmbd3lpy8y/)

- **Faithful contribution:** Claims dense models need GPU VRAM roughly equal to parameter billions and dismisses system RAM/Intel GPUs.
- **Type:** hardware prescription
- **Why relevant (assessment):** Tests fit, residency/offload, shared memory and concurrency, not hardware-as-intelligence. Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Unsupported universal rule; quantized working counterexamples exist in thread.
- **Transferability (inference):** OP uses a discrete3090; user has a different Apple unified-memory/MLX path. Do not copy memory/tok/s estimates. Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence.
- **Themes:** hardware, weights

<a id="c127"></a>

### C127 — u/DystopianRealist

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpgqk9qs9s/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpgqk9qs9s/)

- **Faithful contribution:** Claims Claude Code consumes 27K system-prompt tokens before greeting.
- **Type:** prompt-overhead claim
- **Why relevant (assessment):** Separates configured context, occupied context, working headroom and compaction. Tests usable tool access, orchestration, protocol and prompt overhead.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Version/workspace dependent and not measured here; inspect actual prompt tokens.
- **Transferability (inference):** Task/harness dependent; no universal minimum or fraction follows from this report. A suggested harness may change several variables; validate access, protocol and prompt budget separately.
- **Themes:** context, harness

<a id="c128"></a>

### C128 — u/pjkm123987

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxhmxq0kzvn/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxhmxq0kzvn/)

- **Faithful contribution:** Claims 20K of the preceding overhead are guardrails.
- **Type:** prompt-overhead claim
- **Why relevant (assessment):** Separates configured context, occupied context, working headroom and compaction. Tests usable tool access, orchestration, protocol and prompt overhead.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** No source or token trace; do not use as a verified token budget.
- **Transferability (inference):** Task/harness dependent; no universal minimum or fraction follows from this report. A suggested harness may change several variables; validate access, protocol and prompt budget separately.
- **Themes:** context, harness

<a id="c129"></a>

### C129 — u/overand

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwln8fnnnol/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwln8fnnnol/)

- **Faithful contribution:** Reports strong 27B coding on 36GB VRAM and asks exact quant/publisher, while preferring llama.cpp.
- **Type:** experience/question
- **Why relevant (assessment):** Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal. Tests whether effective serving defaults/behavior, rather than model name, explain failures.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** Hardware exceeds OP's and no artifact/test results supplied.
- **Transferability (inference):** Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence. Transfer the controlled comparison method; not an automatic requirement to migrate.
- **Themes:** weights, runtime, hardware

<a id="c130"></a>

### C130 — u/PuzzleheadedArm3732

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx76s9v3q90/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx76s9v3q90/)

- **Faithful contribution:** Claims Ollama supports Qwen3.8 launch into Claude Code/OpenCode and suggests official Qwen Code; offers same-tool-loop comparison.
- **Type:** counterrecommendation
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures. Tests usable tool access, orchestration, protocol and prompt overhead.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Support/commands not executed or externally verified; directly counters categorical anti-Ollama claims.
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate. A suggested harness may change several variables; validate access, protocol and prompt budget separately.
- **Themes:** runtime, harness, methodology

<a id="c131"></a>

### C131 — u/Fractoos

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmhdq9gk2p/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmhdq9gk2p/)

- **Faithful contribution:** Suggests Strata and a claimed 150B Qwen model.
- **Type:** recommendation
- **Why relevant (assessment):** Provides an alternative-model/runtime lead, not a demonstrated fix for unchanged target model. Tests whether effective serving defaults/behavior, rather than model name, explain failures.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Exact model identity/parameter accounting and memory fit unresolved.
- **Transferability (inference):** Changing model changes the hypothesis; establish a working baseline and fit before considering this lead. Transfer the controlled comparison method; not an automatic requirement to migrate.
- **Themes:** alternatives, runtime

<a id="c132"></a>

### C132 — u/Kmic68

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk1ojxlrc0/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk1ojxlrc0/)

- **Faithful contribution:** Requests quant, KV precision, default output settings, harness and reasoning level; claims extensive 27B experience.
- **Type:** diagnostic questions
- **Why relevant (assessment):** Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal. Tests cache precision versus available context and fidelity.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Exact OP values and examples still required.
- **Transferability (inference):** Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence. Compare matched tasks with explicit cache scheme; different architectures/caches may respond differently.
- **Themes:** weights, kv, sampling, reasoning, harness

<a id="c133"></a>

### C133 — u/Naiw80

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk4mvv91gk/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk4mvv91gk/)

- **Faithful contribution:** Reports own harness with 27B then faster/stronger FlashNext; says research tools/context compensate for limited reliable knowledge, and neither reliably one-shots without validation.
- **Type:** experience/mechanism hypothesis
- **Why relevant (assessment):** Tests missing/current domain knowledge separately from reasoning capability. Tests usable tool access, orchestration, protocol and prompt overhead.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** No comparative logs; reasoning capability versus memorized knowledge remains a hypothesis.
- **Transferability (inference):** Current references/tools are lower-cost hypotheses to test before retraining. A suggested harness may change several variables; validate access, protocol and prompt budget separately.
- **Themes:** knowledge, harness, workflow, alternatives

<a id="c134"></a>

### C134 — u/FerretBoom

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkhpnkl4m8/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkhpnkl4m8/)

- **Faithful contribution:** Asks for an actual received prompt; speculates about Claude's caching, RAG, routing, retry and internal testing infrastructure.
- **Type:** diagnostic question/speculation
- **Why relevant (assessment):** Tests usable tool access, orchestration, protocol and prompt overhead. Separates configured context, occupied context, working headroom and compaction.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Claims about proprietary internal serving are unverified and not used as fact.
- **Transferability (inference):** A suggested harness may change several variables; validate access, protocol and prompt budget separately. Task/harness dependent; no universal minimum or fraction follows from this report.
- **Themes:** harness, context, methodology

<a id="c135"></a>

### C135 — u/FerretBoom

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkkxe7yqp1/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkkxe7yqp1/)

- **Faithful contribution:** Suggests a 30-question cloud-generated coding/reasoning test and says hardware/context should not affect the same model's identity.
- **Type:** test proposal
- **Why relevant (assessment):** Improves causal identification, failure visibility and comparison validity. Tests fit, residency/offload, shared memory and concurrency, not hardware-as-intelligence.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Generated tests may be biased or miss agent loops; control prompt and runtime representation.
- **Transferability (inference):** Transfer measurement discipline, not the commenters root-cause certainty. OP uses a discrete3090; user has a different Apple unified-memory/MLX path. Do not copy memory/tok/s estimates.
- **Themes:** methodology, hardware

<a id="c136"></a>

### C136 — u/Immediate_Compote743

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlodpor15t/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlodpor15t/)

- **Faithful contribution:** Suggests HyperQwen.
- **Type:** recommendation
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures. Provides an alternative-model/runtime lead, not a demonstrated fix for unchanged target model.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** No source link, exact version or evidence supplied.
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate. Changing model changes the hypothesis; establish a working baseline and fit before considering this lead.
- **Themes:** runtime, alternatives

<a id="c137"></a>

### C137 — u/Sexyvette07

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnwtcn33c1/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnwtcn33c1/)

- **Faithful contribution:** Claims Sonnet medium scores ~50% higher than 27B xhigh, suggests FlashNext/Strata/Basalt, hybrid use and possible upcoming Qwen release.
- **Type:** benchmark claim/cost suggestion
- **Why relevant (assessment):** Provides an alternative-model/runtime lead, not a demonstrated fix for unchanged target model. Evaluates elapsed time, senior attention, maintenance and accepted-work cost.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Benchmark/source and release prediction unverified; paid subscription/hardware suggestions not required to diagnose.
- **Transferability (inference):** Changing model changes the hypothesis; establish a working baseline and fit before considering this lead. Preference and task dependent; quoted throughput, prices and savings are not cost-effectiveness proof.
- **Themes:** alternatives, economics, weights, sampling, workflow

<a id="c138"></a>

### C138 — u/IsaacLevinsky

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwo1fnlgwps/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwo1fnlgwps/)

- **Faithful contribution:** Requests quant/runtime details, arguing their importance is underappreciated.
- **Type:** diagnostic request
- **Why relevant (assessment):** Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal. Tests whether effective serving defaults/behavior, rather than model name, explain failures.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** No actual settings or task evidence.
- **Transferability (inference):** Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence. Transfer the controlled comparison method; not an automatic requirement to migrate.
- **Themes:** weights, runtime

<a id="c139"></a>

### C139 — u/MLisdabomb

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwplrq6drj6/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwplrq6drj6/)

- **Faithful contribution:** Reports OP's failure differs sharply from own experience and asks exact quant/serving details.
- **Type:** counterexperience/request
- **Why relevant (assessment):** Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal. Tests whether effective serving defaults/behavior, rather than model name, explain failures.
- **Evidence quality:** E1 — first-person report without reproducible configuration/outcome data.
- **Open questions / verification gaps:** No setup or task-matched evidence proving configuration cause.
- **Transferability (inference):** Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence. Transfer the controlled comparison method; not an automatic requirement to migrate.
- **Themes:** weights, runtime, methodology

<a id="c140"></a>

### C140 — u/SeaRefractor

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwo2cy7hvvl/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwo2cy7hvvl/)

- **Faithful contribution:** Recommends FlashNext via Strata at IQ3_S or higher, claiming stronger reasoning.
- **Type:** recommendation
- **Why relevant (assessment):** Provides an alternative-model/runtime lead, not a demonstrated fix for unchanged target model. Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Need exact artifact, memory fit and matched coding trials.
- **Transferability (inference):** Changing model changes the hypothesis; establish a working baseline and fit before considering this lead. Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence.
- **Themes:** alternatives, weights

<a id="c143"></a>

### C143 — u/905cougarhunter

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwsuhnxcsyq/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwsuhnxcsyq/)

- **Faithful contribution:** Recommends HyperQwen single mode with ~262K context while insulting Ollama.
- **Type:** recommendation
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures. Separates configured context, occupied context, working headroom and compaction.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** No memory/quality evidence; configured maximum is not effective utilization.
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate. Task/harness dependent; no universal minimum or fraction follows from this report.
- **Themes:** runtime, context

<a id="c144"></a>

### C144 — u/outdoorsgeek

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwtk7aojzj5/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwtk7aojzj5/)

- **Faithful contribution:** Expects tuning improvements but roughly older-frontier small-task ability; says professional parity would cost too much relative to cloud.
- **Type:** capability/ROI opinion
- **Why relevant (assessment):** Evaluates elapsed time, senior attention, maintenance and accepted-work cost. Tests fit, residency/offload, shared memory and concurrency, not hardware-as-intelligence.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** No financial/task dataset; preserve possibility local is worthwhile for non-cost reasons.
- **Transferability (inference):** Preference and task dependent; quoted throughput, prices and savings are not cost-effectiveness proof. OP uses a discrete3090; user has a different Apple unified-memory/MLX path. Do not copy memory/tok/s estimates.
- **Themes:** economics, hardware, workflow

<a id="c145"></a>

### C145 — u/Civil_Fee_7862

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwtkiytz5b8/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwtkiytz5b8/)

- **Faithful contribution:** Suggests 48GB full-context target with 4-bit weights, 8-bit activations/KV and OpenCode.
- **Type:** capacity recommendation
- **Why relevant (assessment):** Tests fit, residency/offload, shared memory and concurrency, not hardware-as-intelligence. Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Quant schemes not specified; no evidence 24GB categorically cannot work.
- **Transferability (inference):** OP uses a discrete3090; user has a different Apple unified-memory/MLX path. Do not copy memory/tok/s estimates. Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence.
- **Themes:** hardware, weights, kv, harness

<a id="c146"></a>

### C146 — u/No_Audience2449

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwvfrh6cqeb/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwvfrh6cqeb/)

- **Faithful contribution:** Reports ~20% correct on Drupal11 tasks and attributes errors to older Drupal training; says LoRA may be needed for 100%.
- **Type:** domain-specific failure/learning proposal
- **Why relevant (assessment):** Tests missing/current domain knowledge separately from reasoning capability. Tests scope, planning, verification and supervision as determinants of accepted work.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** No test set or training evidence; documentation retrieval should precede costly fine-tuning and 100% is not guaranteed.
- **Transferability (inference):** Current references/tools are lower-cost hypotheses to test before retraining. Applies as an evaluation/workflow pattern; autonomy and net benefit must be measured.
- **Themes:** knowledge, workflow, alternatives

<a id="c147"></a>

### C147 — u/FudgeEducational2038

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1ck14t5sx/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1ck14t5sx/)

- **Faithful contribution:** Argues KV precision matters more than weights, suggesting smaller weight quant with FP8/Q8 or higher KV; recommends Strata FlashNext and claims speed/quality benefits.
- **Type:** quantization hypothesis/recommendation
- **Why relevant (assessment):** Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal. Tests cache precision versus available context and fidelity.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Format comparisons and 'full precision' language are unsupported; need exact schemes and equal-budget ablation.
- **Transferability (inference):** Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence. Compare matched tasks with explicit cache scheme; different architectures/caches may respond differently.
- **Themes:** weights, kv, alternatives

<a id="c148"></a>

### C148 — u/Sad-Chemist7118

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxfcvlbcfxc/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxfcvlbcfxc/)

- **Faithful contribution:** Reports Strata at claimed 272K, 4080 16GB/64GB RAM/PCIe4 SSD, 70–80 tok/s and fast ~50K prefill; ranks it below Sonnet5.5 but near older Opus.
- **Type:** alternative experience
- **Why relevant (assessment):** Provides an alternative-model/runtime lead, not a demonstrated fix for unchanged target model. Tests fit, residency/offload, shared memory and concurrency, not hardware-as-intelligence.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** Model implied from context, not explicit; timings/quality comparison unlogged.
- **Transferability (inference):** Changing model changes the hypothesis; establish a working baseline and fit before considering this lead. OP uses a discrete3090; user has a different Apple unified-memory/MLX path. Do not copy memory/tok/s estimates.
- **Themes:** alternatives, hardware, context, economics

<a id="c149"></a>

### C149 — u/dzedaj

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxfk36mppd0/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxfk36mppd0/)

- **Faithful contribution:** Recommends FlashNext ISTA-DASLab IQ3_S/IQ3_XXS GCO-RCQ on Strata, claiming faster/better on OP's hardware.
- **Type:** recommendation
- **Why relevant (assessment):** Provides an alternative-model/runtime lead, not a demonstrated fix for unchanged target model. Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** No 32GB-RAM proof; exact naming differs elsewhere.
- **Transferability (inference):** Changing model changes the hypothesis; establish a working baseline and fit before considering this lead. Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence.
- **Themes:** alternatives, weights, runtime

<a id="c150"></a>

### C150 — u/DisastrousProfit5204

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxfo3zrswip/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxfo3zrswip/)

- **Faithful contribution:** Recommends FlashNext/Next Coder via Strata as better than 27B.
- **Type:** recommendation
- **Why relevant (assessment):** Provides an alternative-model/runtime lead, not a demonstrated fix for unchanged target model. Tests whether effective serving defaults/behavior, rather than model name, explain failures.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Exact version and controlled outcomes absent.
- **Transferability (inference):** Changing model changes the hypothesis; establish a working baseline and fit before considering this lead. Transfer the controlled comparison method; not an automatic requirement to migrate.
- **Themes:** alternatives, runtime

<a id="c151"></a>

### C151 — u/Ejo2001

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxih2eqix7l/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxih2eqix7l/)

- **Faithful contribution:** Reports NVFP4 27B with Roo/Pi works but needs 5–10 prompts versus Claude's one; proposes finer steps, possibly custom harness, second GPU or RAM/Strata.
- **Type:** experience/capability comparison
- **Why relevant (assessment):** Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal. Tests usable tool access, orchestration, protocol and prompt overhead.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** NVFP4≈Q8 is the author's unverified equivalence, not a general format fact; no same-task logs.
- **Transferability (inference):** Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence. A suggested harness may change several variables; validate access, protocol and prompt budget separately.
- **Themes:** weights, harness, workflow, alternatives, economics

<a id="c152"></a>

### C152 — u/skipITjob

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxit3lz36hw/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxit3lz36hw/)

- **Faithful contribution:** Reports cloud-agent help identifying an AMD Windows-driver problem and temporary fix.
- **Type:** setup experience
- **Why relevant (assessment):** Tests fit, residency/offload, shared memory and concurrency, not hardware-as-intelligence. Tests whether effective serving defaults/behavior, rather than model name, explain failures.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** Different GPU/driver; relevant as a diagnostic category, not OP's proven issue.
- **Transferability (inference):** OP uses a discrete3090; user has a different Apple unified-memory/MLX path. Do not copy memory/tok/s estimates. Transfer the controlled comparison method; not an automatic requirement to migrate.
- **Themes:** hardware, runtime, methodology

<a id="c153"></a>

### C153 — u/vtkayaker

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnmysfxy91/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnmysfxy91/)

- **Faithful contribution:** Says 27B handles scripts/CLI but struggles with architecture; prefers Q6 for 3.8 and 128–256K requiring 32–48GB.
- **Type:** experience/recommendation
- **Why relevant (assessment):** Tests scope, planning, verification and supervision as determinants of accepted work. Separates configured context, occupied context, working headroom and compaction.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** No universal minimum established; task size and KV scheme unknown.
- **Transferability (inference):** Applies as an evaluation/workflow pattern; autonomy and net benefit must be measured. Task/harness dependent; no universal minimum or fraction follows from this report.
- **Themes:** workflow, context, weights, hardware

<a id="c154"></a>

### C154 — u/Many_Discussion_1696

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwt70jws9ep/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwt70jws9ep/)

- **Faithful contribution:** Reports cloud planning/setup/testing, local execution with retries, and cloud verification; says local takes longer but reduces billable work.
- **Type:** hybrid experience/recommendation
- **Why relevant (assessment):** Tests scope, planning, verification and supervision as determinants of accepted work. Evaluates elapsed time, senior attention, maintenance and accepted-work cost.
- **Evidence quality:** E1 — first-person report without reproducible configuration/outcome data.
- **Open questions / verification gaps:** No accounting of review/setup costs or measured failure rate.
- **Transferability (inference):** Applies as an evaluation/workflow pattern; autonomy and net benefit must be measured. Preference and task dependent; quoted throughput, prices and savings are not cost-effectiveness proof.
- **Themes:** workflow, economics, methodology

<a id="c155"></a>

### C155 — u/OldEffective9726

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwv48gfxorm/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwv48gfxorm/)

- **Faithful contribution:** Calls dense 3.8 bad at math and favors a Qwen3.6-Claude-remix MoE Q4, linking remix publishers.
- **Type:** alternative preference
- **Why relevant (assessment):** Provides an alternative-model/runtime lead, not a demonstrated fix for unchanged target model. Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal.
- **Evidence quality:** E1 — first-person report without reproducible configuration/outcome data.
- **Open questions / verification gaps:** Different model/alignment; exact artifact, provenance and coding evidence absent.
- **Transferability (inference):** Changing model changes the hypothesis; establish a working baseline and fit before considering this lead. Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence.
- **Themes:** alternatives, weights, reasoning

<a id="c156"></a>

### C156 — u/Perfect-Campaign9551

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk5bp3fwro/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk5bp3fwro/)

- **Faithful contribution:** Suggests 64GB RAM and FlashNext IQ3_XXS via Strata.
- **Type:** upgrade recommendation
- **Why relevant (assessment):** Tests fit, residency/offload, shared memory and concurrency, not hardware-as-intelligence. Provides an alternative-model/runtime lead, not a demonstrated fix for unchanged target model.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** No tested OP-equivalent fit or task gain.
- **Transferability (inference):** OP uses a discrete3090; user has a different Apple unified-memory/MLX path. Do not copy memory/tok/s estimates. Changing model changes the hypothesis; establish a working baseline and fit before considering this lead.
- **Themes:** hardware, alternatives

<a id="c157"></a>

### C157 — u/feverdoingwork

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk5t2kilr6/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk5t2kilr6/)

- **Faithful contribution:** Says Q4+ can work on 24GB or less, recommends model-card sampling (mentions temp1), Pi/basic AGENTS.md, and says Flash is less persistent on difficult tasks.
- **Type:** experience/recommendation
- **Why relevant (assessment):** Tests generation controls as a cause of unstable or looping output. Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal.
- **Evidence quality:** E1 — first-person report without reproducible configuration/outcome data.
- **Open questions / verification gaps:** Model-card values not verified; temperature must match actual variant/mode and task.
- **Transferability (inference):** Use exact model/mode-recommended settings as a measured baseline, not a universal numeric recipe. Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence.
- **Themes:** sampling, weights, harness, alternatives, reasoning

<a id="c158"></a>

### C158 — u/More_Personality_126

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkgol52wma/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkgol52wma/)

- **Faithful contribution:** Blames 128K context on one 3090, claiming KV exhausts VRAM before weights load.
- **Type:** capacity hypothesis
- **Why relevant (assessment):** Tests fit, residency/offload, shared memory and concurrency, not hardware-as-intelligence. Separates configured context, occupied context, working headroom and compaction.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** No allocation measurements; weight/cache initialization order and exact cache format unknown.
- **Transferability (inference):** OP uses a discrete3090; user has a different Apple unified-memory/MLX path. Do not copy memory/tok/s estimates. Task/harness dependent; no universal minimum or fraction follows from this report.
- **Themes:** hardware, context, kv

<a id="c159"></a>

### C159 — u/IllustratorInner4904

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkh1ido334/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkh1ido334/)

- **Faithful contribution:** Reports Unsloth Q4 + llama.cpp + Pi with bash guard extension fixes mistakes left by Claude.
- **Type:** specific experience
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures. Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** No case/test artifacts; useful combination to evaluate, not proven universally best.
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate. Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence.
- **Themes:** runtime, weights, harness, methodology

<a id="c160"></a>

### C160 — u/RawFreakCalm

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkiry31uap/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkiry31uap/)

- **Faithful contribution:** Asks harness; reports FP8 ~265K 27B long-code projects alongside DeepSeek agents, returning after a day to requested work.
- **Type:** experience/question
- **Why relevant (assessment):** Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal. Separates configured context, occupied context, working headroom and compaction.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** Hardware, task boundaries and validation missing; 265K may be shorthand/typo.
- **Transferability (inference):** Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence. Task/harness dependent; no universal minimum or fraction follows from this report.
- **Themes:** weights, context, harness, workflow

<a id="c162"></a>

### C162 — u/Ell2509

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkofr91sbo/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkofr91sbo/)

- **Faithful contribution:** Asks quant and says Q4 is much worse than Q8 for complex coding.
- **Type:** diagnostic question/opinion
- **Why relevant (assessment):** Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** No matched trials; Q4 success reports disagree.
- **Transferability (inference):** Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence.
- **Themes:** weights

<a id="c163"></a>

### C163 — u/GrungeWerX

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkw6gog2w3/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkw6gog2w3/)

- **Faithful contribution:** Criticizes Ollama and asks harness, promising suggestions later.
- **Type:** runtime criticism/question
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures. Tests usable tool access, orchestration, protocol and prompt overhead.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** A promised future reply is not available evidence.
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate. A suggested harness may change several variables; validate access, protocol and prompt budget separately.
- **Themes:** runtime, harness

<a id="c164"></a>

### C164 — u/ThaSipah

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwl0i75so83/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwl0i75so83/)

- **Faithful contribution:** Says 27B codes well but highest reasoning gets lost and repeatedly exhausts 128K.
- **Type:** negative experience
- **Why relevant (assessment):** Separates useful long reasoning, pathological loops and output/time budgets. Separates configured context, occupied context, working headroom and compaction.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** Unknown quant/template/harness; test medium versus xhigh on same task.
- **Transferability (inference):** Task-specific tradeoff; a finetune and a base-model thinking toggle are not the same intervention. Task/harness dependent; no universal minimum or fraction follows from this report.
- **Themes:** reasoning, context

<a id="c165"></a>

### C165 — u/Aubrey_D_Graham

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwl3dus3wdf/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwl3dus3wdf/)

- **Faithful contribution:** Calls 27B capable with help and recommends an advisor paradigm and decomposed subproblems.
- **Type:** workflow/capability opinion
- **Why relevant (assessment):** Tests scope, planning, verification and supervision as determinants of accepted work. Provides an alternative-model/runtime lead, not a demonstrated fix for unchanged target model.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Relative Opus-era ranking and advisor effectiveness unverified.
- **Transferability (inference):** Applies as an evaluation/workflow pattern; autonomy and net benefit must be measured. Changing model changes the hypothesis; establish a working baseline and fit before considering this lead.
- **Themes:** workflow, alternatives

<a id="c166"></a>

### C166 — u/BarracudaDefiant4702

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwl942mc0bn/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwl942mc0bn/)

- **Faithful contribution:** Reports difficulty with Q4 even on 48GB and recommends at least ~250K context.
- **Type:** negative experience/capacity advice
- **Why relevant (assessment):** Separates configured context, occupied context, working headroom and compaction. Tests fit, residency/offload, shared memory and concurrency, not hardware-as-intelligence.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** Task and cache precision unknown; personal requirement is not a universal threshold.
- **Transferability (inference):** Task/harness dependent; no universal minimum or fraction follows from this report. OP uses a discrete3090; user has a different Apple unified-memory/MLX path. Do not copy memory/tok/s estimates.
- **Themes:** context, hardware, weights

<a id="c167"></a>

### C167 — u/Frail_Waif

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwl9h4s7zc1/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwl9h4s7zc1/)

- **Faithful contribution:** On dual MI50 32GB cards, reports Unsloth Q8 27B hallucinated with broken Hermes container but did better with tools in Pi; ISTA 27B worse and FlashNext IQ3_S better.
- **Type:** detailed experience
- **Why relevant (assessment):** Tests missing/current domain knowledge separately from reasoning capability. Tests usable tool access, orchestration, protocol and prompt overhead.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** Broken container and quant/runtime changes confounded; useful functional-tool check, not clean model comparison.
- **Transferability (inference):** Current references/tools are lower-cost hypotheses to test before retraining. A suggested harness may change several variables; validate access, protocol and prompt budget separately.
- **Themes:** knowledge, harness, weights, runtime, alternatives, hardware

<a id="c168"></a>

### C168 — u/mdwsr06

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlo8ql14m9/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlo8ql14m9/)

- **Faithful contribution:** Observes older Qwen3.5-9B losing coherence as context grows and suspects similar behavior in 27B.
- **Type:** analogy/hypothesis
- **Why relevant (assessment):** Separates configured context, occupied context, working headroom and compaction. Separates useful long reasoning, pathological loops and output/time budgets.
- **Evidence quality:** E1 — first-person report without reproducible configuration/outcome data.
- **Open questions / verification gaps:** Different model/scale; architecture similarity does not establish mechanism.
- **Transferability (inference):** Task/harness dependent; no universal minimum or fraction follows from this report. Task-specific tradeoff; a finetune and a base-model thinking toggle are not the same intervention.
- **Themes:** context, reasoning

<a id="c169"></a>

### C169 — u/overand

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlwm184dr5/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlwm184dr5/)

- **Faithful contribution:** Supplies llama-server Unsloth UD-Q4_K_M at 98304 context, estimating 16.5GB weights+6GB KV on headless 3090; suggests smaller weights, Pi, optional cache quant or second card.
- **Type:** concrete configuration proposal
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures. Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** Command not executed; estimates build/format dependent. It binds 0.0.0.0 and must not be copied without considering network exposure. No such change made.
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate. Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence.
- **Themes:** runtime, weights, kv, context, hardware, harness

<a id="c170"></a>

### C170 — u/Hungry-Rip-2384

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlygpn1nz6/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlygpn1nz6/)

- **Faithful contribution:** Suspects project files overfill Qwen's useful context compared with Claude.
- **Type:** context hypothesis
- **Why relevant (assessment):** Separates configured context, occupied context, working headroom and compaction. Tests usable tool access, orchestration, protocol and prompt overhead.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Need actual rendered prompt and session token distribution.
- **Transferability (inference):** Task/harness dependent; no universal minimum or fraction follows from this report. A suggested harness may change several variables; validate access, protocol and prompt budget separately.
- **Themes:** context, harness

<a id="c171"></a>

### C171 — u/BrodyFriend

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm1bxxhbqd/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm1bxxhbqd/)

- **Faithful contribution:** Attributes looping directly to temperature/repetition penalty and speculates no-think temp0.3, while admitting coding inexperience.
- **Type:** sampling advice
- **Why relevant (assessment):** Tests generation controls as a cause of unstable or looping output. Separates useful long reasoning, pathological loops and output/time budgets.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** No evidence for exclusive causal claim; compare official variant-specific settings first.
- **Transferability (inference):** Use exact model/mode-recommended settings as a measured baseline, not a universal numeric recipe. Task-specific tradeoff; a finetune and a base-model thinking toggle are not the same intervention.
- **Themes:** sampling, reasoning

<a id="c172"></a>

### C172 — u/WishfulAgenda

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm2oi265cw/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm2oi265cw/)

- **Faithful contribution:** Suggests another GPU, tensor split, Q8, highest effort, >160K and maybe Linux vLLM.
- **Type:** upgrade/configuration recommendation
- **Why relevant (assessment):** Tests fit, residency/offload, shared memory and concurrency, not hardware-as-intelligence. Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Costly multi-variable change; no evidence each component needed.
- **Transferability (inference):** OP uses a discrete3090; user has a different Apple unified-memory/MLX path. Do not copy memory/tok/s estimates. Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence.
- **Themes:** hardware, weights, reasoning, context, runtime

<a id="c173"></a>

### C173 — u/ZallenDuZari

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm5muv15sz/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm5muv15sz/)

- **Faithful contribution:** Reports okay 27B on memory-rich Strix Halo then successful vibe coding on FlashNext.
- **Type:** experience
- **Why relevant (assessment):** Tests fit, residency/offload, shared memory and concurrency, not hardware-as-intelligence. Provides an alternative-model/runtime lead, not a demonstrated fix for unchanged target model.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** No matched tasks or time/quality measures; hardware differs.
- **Transferability (inference):** OP uses a discrete3090; user has a different Apple unified-memory/MLX path. Do not copy memory/tok/s estimates. Changing model changes the hypothesis; establish a working baseline and fit before considering this lead.
- **Themes:** hardware, alternatives, workflow

<a id="c174"></a>

### C174 — u/HenkPoley

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm8dsmzxk1/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm8dsmzxk1/)

- **Faithful contribution:** Asks cache quant and recommends F16 or Q8, while placing 27B near smaller frontier offerings.
- **Type:** diagnostic question/capability caution
- **Why relevant (assessment):** Tests cache precision versus available context and fidelity. Provides an alternative-model/runtime lead, not a demonstrated fix for unchanged target model.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Exact OP KV unknown; relative ranking not sourced.
- **Transferability (inference):** Compare matched tasks with explicit cache scheme; different architectures/caches may respond differently. Changing model changes the hypothesis; establish a working baseline and fit before considering this lead.
- **Themes:** kv, alternatives

<a id="c175"></a>

### C175 — u/FizzyDuncDizzel

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmahhpz3qd/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmahhpz3qd/)

- **Faithful contribution:** Asks agent/harness and recommends low thinking with an approximately 20K hard stop.
- **Type:** diagnostic question/recommendation
- **Why relevant (assessment):** Tests usable tool access, orchestration, protocol and prompt overhead. Separates useful long reasoning, pathological loops and output/time budgets.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Hard cap may truncate valid reasoning; compare finish reasons and success.
- **Transferability (inference):** A suggested harness may change several variables; validate access, protocol and prompt budget separately. Task-specific tradeoff; a finetune and a base-model thinking toggle are not the same intervention.
- **Themes:** harness, reasoning, context

<a id="c176"></a>

### C176 — u/_RemyLeBeau_

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmcwyp7ycl/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmcwyp7ycl/)

- **Faithful contribution:** Recommends llama.cpp/vLLM, a stock harness and careful control of introduced variables; says direct control improved own agents.
- **Type:** experience/methodology
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures. Separates configured context, occupied context, working headroom and compaction.
- **Evidence quality:** E1 — first-person report without reproducible configuration/outcome data.
- **Open questions / verification gaps:** Categorical claim Ollama cannot provide128K is unverified and conflicts with C076/C130.
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate. Task/harness dependent; no universal minimum or fraction follows from this report.
- **Themes:** runtime, context, methodology

<a id="c177"></a>

### C177 — u/Spirited_Eggplant_98

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmeeigcx40/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmeeigcx40/)

- **Faithful contribution:** Reports 27B AWQ5 oMLX M4 Studio+plain Pi/custom MCP compiles and passes tests, unlike worse oh-mi-pi; 128K sweet spot, ~4h versus Sonnet20min.
- **Type:** detailed comparison experience
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures. Tests usable tool access, orchestration, protocol and prompt overhead.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** No shared tests/traces; AWQ naming/model build need verification; relative time is workload-specific.
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate. A suggested harness may change several variables; validate access, protocol and prompt budget separately.
- **Themes:** runtime, harness, weights, context, economics

<a id="c178"></a>

### C178 — u/ISJA809

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmmp8qgbz6/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmmp8qgbz6/)

- **Faithful contribution:** Reports coding useless on 5070 12GB/32GB system RAM.
- **Type:** negative experience
- **Why relevant (assessment):** Tests fit, residency/offload, shared memory and concurrency, not hardware-as-intelligence. Tests scope, planning, verification and supervision as determinants of accepted work.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** Exact model, quant, settings and task unknown.
- **Transferability (inference):** OP uses a discrete3090; user has a different Apple unified-memory/MLX path. Do not copy memory/tok/s estimates. Applies as an evaluation/workflow pattern; autonomy and net benefit must be measured.
- **Themes:** hardware, workflow

<a id="c179"></a>

### C179 — u/a_lost_shadow

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmn96j9x28/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmn96j9x28/)

- **Faithful contribution:** Reports IQ3_XSS 27B, Q4 KV,155K on RX6800 16GB via llama.cpp/OpenCode works; medium thinking, grill-me clarification, narrow scope, lean skills and library familiarity help.
- **Type:** detailed constrained-hardware counterexample
- **Why relevant (assessment):** Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal. Tests cache precision versus available context and fidelity.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** Directly disputes universal Q4-KV/high-quant/full-context rules; no controlled logs and training-cutoff speculation unverified.
- **Transferability (inference):** Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence. Compare matched tasks with explicit cache scheme; different architectures/caches may respond differently.
- **Themes:** weights, kv, context, reasoning, harness, knowledge, workflow

<a id="c180"></a>

### C180 — u/Bounce_back1225

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmnemgk7fo/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmnemgk7fo/)

- **Faithful contribution:** Speculates32GB is minimum and business use needs≥256GB RAM.
- **Type:** hardware opinion
- **Why relevant (assessment):** Tests fit, residency/offload, shared memory and concurrency, not hardware-as-intelligence. Evaluates elapsed time, senior attention, maintenance and accepted-work cost.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Unsupported size requirement; no workload or model accounting.
- **Transferability (inference):** OP uses a discrete3090; user has a different Apple unified-memory/MLX path. Do not copy memory/tok/s estimates. Preference and task dependent; quoted throughput, prices and savings are not cost-effectiveness proof.
- **Themes:** hardware, economics

<a id="c181"></a>

### C181 — u/Popular-Direction984

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwn4hzlsrdu/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwn4hzlsrdu/)

- **Faithful contribution:** Claims increasing from128K to supported256K is the only necessary fix.
- **Type:** context hypothesis
- **Why relevant (assessment):** Separates configured context, occupied context, working headroom and compaction.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** No evidence excludes other causes; configuration maximum is not useful context.
- **Transferability (inference):** Task/harness dependent; no universal minimum or fraction follows from this report.
- **Themes:** context

<a id="c182"></a>

### C182 — u/ferargie

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwn4xvab6ao/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwn4xvab6ao/)

- **Faithful contribution:** Reports5060Ti16GB, UnslothQ3_S, llama.cpp CUDA, OpenCode,80K and43tok/s, little/no thinking; cache recollection uncertain.
- **Type:** constrained-hardware experience
- **Why relevant (assessment):** Tests fit, residency/offload, shared memory and concurrency, not hardware-as-intelligence. Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** Author says settings are not fully remembered; still counters categorical24GB impossibility.
- **Transferability (inference):** OP uses a discrete3090; user has a different Apple unified-memory/MLX path. Do not copy memory/tok/s estimates. Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence.
- **Themes:** hardware, weights, kv, reasoning, harness, runtime

<a id="c183"></a>

### C183 — u/Drewskie92

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnbvvkpcbo/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnbvvkpcbo/)

- **Faithful contribution:** Reports3090/32GB system, Qwen3.8-27B4KM, LMStudioBionic/unified memory/Q4 settings worked hours on40+ research pages using progress/decisions files.
- **Type:** near-hardware experience
- **Why relevant (assessment):** Tests fit, residency/offload, shared memory and concurrency, not hardware-as-intelligence. Tests whether effective serving defaults/behavior, rather than model name, explain failures.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** Research rather than coding, elapsed time includes idle; exact K/V nomenclature unclear.
- **Transferability (inference):** OP uses a discrete3090; user has a different Apple unified-memory/MLX path. Do not copy memory/tok/s estimates. Transfer the controlled comparison method; not an automatic requirement to migrate.
- **Themes:** hardware, runtime, kv, context, workflow

<a id="c184"></a>

### C184 — u/cjadwick

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwngpos3ogz/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwngpos3ogz/)

- **Faithful contribution:** Reports NVFP4 27B with a multiagent system producing Sonnet5-like code; suspects low quant or harness.
- **Type:** experience/quality claim
- **Why relevant (assessment):** Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal. Tests usable tool access, orchestration, protocol and prompt overhead.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** No tests or matched comparison; FP4-format equivalence must not be assumed.
- **Transferability (inference):** Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence. A suggested harness may change several variables; validate access, protocol and prompt budget separately.
- **Themes:** weights, harness, workflow

<a id="c185"></a>

### C185 — u/asankhs

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwniv627wkg/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwniv627wkg/)

- **Faithful contribution:** Suggests MLX inference or a local-oriented agent such as Optiq Code.
- **Type:** recommendation
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures. Tests usable tool access, orchestration, protocol and prompt overhead.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** MLX not a direct3090 option; hardware route differs.
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate. A suggested harness may change several variables; validate access, protocol and prompt budget separately.
- **Themes:** runtime, harness, alternatives

<a id="c186"></a>

### C186 — u/moonlitpawprints

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnkx49i3dv/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnkx49i3dv/)

- **Faithful contribution:** ReportsOpenCode,4bpw exl3,FP8KV,232K on32GBVRAM via vLLM+MTP; recommends low/medium reasoning, work tracking, narrow tasks, references and tests.
- **Type:** detailed experience/recommendation
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures. Tests usable tool access, orchestration, protocol and prompt overhead.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** exl3/vLLM artifact/backend compatibility and exact build unverified; personal runtime-memory comparison not universal.
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate. A suggested harness may change several variables; validate access, protocol and prompt budget separately.
- **Themes:** runtime, harness, weights, kv, context, reasoning, knowledge, workflow

<a id="c187"></a>

### C187 — u/skinnyzaz

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnnqkrs3aa/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnnqkrs3aa/)

- **Faithful contribution:** Reports good Q8 for small web apps and more mistakes belowQ8; would not use lower.
- **Type:** experience/weight prescription
- **Why relevant (assessment):** Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal. Tests scope, planning, verification and supervision as determinants of accepted work.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** No matched trials; differs from Q3/Q4 success reports.
- **Transferability (inference):** Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence. Applies as an evaluation/workflow pattern; autonomy and net benefit must be measured.
- **Themes:** weights, workflow

<a id="c188"></a>

### C188 — u/Maximum-Security5699

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnqp18zq1v/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnqp18zq1v/)

- **Faithful contribution:** Claims subQ8 exceptNVFP4 is very lossy and Q4 fails past~40K.
- **Type:** weight-quality claim
- **Why relevant (assessment):** Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal. Separates configured context, occupied context, working headroom and compaction.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** No dataset; universal threshold and NVFP4 exception unsupported.
- **Transferability (inference):** Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence. Task/harness dependent; no universal minimum or fraction follows from this report.
- **Themes:** weights, context

<a id="c189"></a>

### C189 — u/Old-Discipline233

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnr8688hi9/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnr8688hi9/)

- **Faithful contribution:** ReportsFlashNext on5080+128GBDDR5 at~120tok/s and~4000tok/s prefill, stronger/faster than27B.
- **Type:** alternative experience
- **Why relevant (assessment):** Tests fit, residency/offload, shared memory and concurrency, not hardware-as-intelligence. Provides an alternative-model/runtime lead, not a demonstrated fix for unchanged target model.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** Prompt lengths/config and quality measures absent; different memory budget.
- **Transferability (inference):** OP uses a discrete3090; user has a different Apple unified-memory/MLX path. Do not copy memory/tok/s estimates. Changing model changes the hypothesis; establish a working baseline and fit before considering this lead.
- **Themes:** hardware, alternatives, economics

<a id="c190"></a>

### C190 — u/joshhope87

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnwivj5y1w/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnwivj5y1w/)

- **Faithful contribution:** Novice suspects low VRAM plus possible multiuser use; reports fine on64GB unified memory.
- **Type:** capacity hypothesis/experience
- **Why relevant (assessment):** Tests fit, residency/offload, shared memory and concurrency, not hardware-as-intelligence. Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** OP concurrency is speculation and 'heavily quantized' not an established cause.
- **Transferability (inference):** OP uses a discrete3090; user has a different Apple unified-memory/MLX path. Do not copy memory/tok/s estimates. Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence.
- **Themes:** hardware, weights, context

<a id="c191"></a>

### C191 — u/junhua119

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwo912em5cy/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwo912em5cy/)

- **Faithful contribution:** ReportsM1Pro32GB,Swift1.5-Qwen3.8-27B Q4_K_M,medium,splash-m1,98K max/66Kactual,~19tok/s withPi builds full-stack personal projects.
- **Type:** detailed constrained-memory experience
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures. Tests usable tool access, orchestration, protocol and prompt overhead.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** No code/tests or controlled base-versusSwift comparison; Apple throughput does not transfer to3090.
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate. A suggested harness may change several variables; validate access, protocol and prompt budget separately.
- **Themes:** runtime, harness, weights, reasoning, context

<a id="c192"></a>

### C192 — u/talaman4eg

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwoa2189ndv/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwoa2189ndv/)

- **Faithful contribution:** PrefersUnslothQ6XL but reportsQ3XL works inOpenCode with sandbox/test feedback forPython/bash/frontend; llama.cpp,UnslothStudio orLMStudio.
- **Type:** experience
- **Why relevant (assessment):** Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal. Tests whether effective serving defaults/behavior, rather than model name, explain failures.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** No logs; supports testing/repair loop rather than a universalquant minimum.
- **Transferability (inference):** Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence. Transfer the controlled comparison method; not an automatic requirement to migrate.
- **Themes:** weights, runtime, harness, workflow

<a id="c193"></a>

### C193 — u/soloyeets

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwoamj90n8i/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwoamj90n8i/)

- **Faithful contribution:** Links froggeric/Qwen-Fixed-Chat-Templates, claiming it bridges the gap and noting other community templates.
- **Type:** template recommendation
- **Why relevant (assessment):** Tests prompt rendering and tool-call serialization/stop-token compatibility. Tests usable tool access, orchestration, protocol and prompt overhead.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** No applied-template diff, compatibility check or before/after tests.
- **Transferability (inference):** Inspect the applied template and wire trace before replacing templates. A suggested harness may change several variables; validate access, protocol and prompt budget separately.
- **Themes:** template, harness

<a id="c194"></a>

### C194 — u/Choubix

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwow4bqx19d/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwow4bqx19d/)

- **Faithful contribution:** Asks whether fixed templates are still needed and whether the benefit is better tool calling.
- **Type:** question
- **Why relevant (assessment):** Tests prompt rendering and tool-call serialization/stop-token compatibility. Tests usable tool access, orchestration, protocol and prompt overhead.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Unanswered in accessible exchange; depends on engine/model/template revision.
- **Transferability (inference):** Inspect the applied template and wire trace before replacing templates. A suggested harness may change several variables; validate access, protocol and prompt budget separately.
- **Themes:** template, harness

<a id="c195"></a>

### C195 — u/InspiredUserNamez

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwob1o1ve75/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwob1o1ve75/)

- **Faithful contribution:** On different Qwen3-Coder30B-A3B, reports40%success/60%honestlyparked/zerofalsepositives after instrumentation; prioritizes detecting everyfailure before optimizing success.
- **Type:** instrumentation experience
- **Why relevant (assessment):** Improves causal identification, failure visibility and comparison validity. Tests usable tool access, orchestration, protocol and prompt overhead.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** Self-report, no logs/denominator; model not OP's. Valuable principle: honest parking over false completion.
- **Transferability (inference):** Transfer measurement discipline, not the commenters root-cause certainty. A suggested harness may change several variables; validate access, protocol and prompt budget separately.
- **Themes:** methodology, harness, workflow, economics

<a id="c196"></a>

### C196 — u/NickReese

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwobdnfu3z4/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwobdnfu3z4/)

- **Faithful contribution:** Advocates colocating complexity for small models.
- **Type:** design principle
- **Why relevant (assessment):** Tests scope, planning, verification and supervision as determinants of accepted work. Separates configured context, occupied context, working headroom and compaction.
- **Evidence quality:** E0 — question, hypothesis or unsupported claim; not independently validated.
- **Open questions / verification gaps:** Phrase not explained; what concrete code/task organization is meant?
- **Transferability (inference):** Applies as an evaluation/workflow pattern; autonomy and net benefit must be measured. Task/harness dependent; no universal minimum or fraction follows from this report.
- **Themes:** workflow, context

<a id="c197"></a>

### C197 — u/problem_def

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwohzmjc78i/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwohzmjc78i/)

- **Faithful contribution:** Reportsninfer-4090+QwenCLI largely replaced cloud, mentions3090stable build but lackslink.
- **Type:** experience
- **Why relevant (assessment):** Tests whether effective serving defaults/behavior, rather than model name, explain failures. Tests usable tool access, orchestration, protocol and prompt overhead.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** No artifact/build/settings or task metrics; do not present unavailablebuild as verified.
- **Transferability (inference):** Transfer the controlled comparison method; not an automatic requirement to migrate. A suggested harness may change several variables; validate access, protocol and prompt budget separately.
- **Themes:** runtime, harness, hardware

<a id="c198"></a>

### C198 — u/FuShiLu

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwoi2suowwy/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwoi2suowwy/)

- **Faithful contribution:** Reports6bitQwen3.8 onMacMiniM4Pro64GB is fast and moreaccurate.
- **Type:** experience
- **Why relevant (assessment):** Tests fit, residency/offload, shared memory and concurrency, not hardware-as-intelligence. Tests exact conversion/quantizer/precision rather than assuming all same-bit artifacts equal.
- **Evidence quality:** E2 — setup/task-specific first-person report or concrete recipe; logs/results not independently validated.
- **Open questions / verification gaps:** Compared to what quant/config and on whichtasks? Hardware differsfromOP.
- **Transferability (inference):** OP uses a discrete3090; user has a different Apple unified-memory/MLX path. Do not copy memory/tok/s estimates. Need exact artifact/revision and equal-task tests; nominal bits do not establish equivalence.
- **Themes:** hardware, weights, workflow

<a id="c200"></a>

### C200 — u/laxative_surplus

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwrm3bg3btx/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwrm3bg3btx/)

- **Faithful contribution:** Asks whether the referenced optimizations mean compiler optimizations.
- **Type:** clarification question
- **Why relevant (assessment):** Clarifies an otherwise ambiguous performance claim; no result supplied.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Do the referenced optimizations mean compiler optimizations?
- **Transferability (inference):** Cannot attribute earlier performance to compiler changes from this question alone.
- **Themes:** runtime, methodology

<a id="c201"></a>

### C201 — u/salynch

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwv6v8f8o0w/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwv6v8f8o0w/)

- **Faithful contribution:** Suggests SGLang or NVIDIA NIM/Dynamo as additional inference options.
- **Type:** runtime recommendation
- **Why relevant (assessment):** Relevant alternatives to the discussed inference stack, without measurements.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which suggested stack supports the target model, quantization, and single-3090 configuration effectively?
- **Transferability (inference):** Candidate runtimes only; suitability and gains on the target setup are unverified.
- **Themes:** runtime, alternatives

<a id="c202"></a>

### C202 — u/solaris_var

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwwhwtj4rdu/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwwhwtj4rdu/)

- **Faithful contribution:** Criticizes Ollama as allegedly using an early llama.cpp fork with worse later feature implementations, while admitting this may have changed since their last use.
- **Type:** runtime criticism
- **Why relevant (assessment):** Substantive but explicitly potentially stale criticism of the runtime.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** Which Ollama and llama.cpp versions were compared?; Does the architectural/feature criticism still apply?
- **Transferability (inference):** Version-sensitive recollection is not evidence that current Ollama causes the reported failure.
- **Themes:** runtime, methodology

<a id="c203"></a>

### C203 — u/Turbulent_Office1340

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwxxmynd21s/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwxxmynd21s/)

- **Faithful contribution:** Disputes an apparent years-long Qwen 3.8 usage implication, saying the release has not existed for years.
- **Type:** chronology correction
- **Why relevant (assessment):** Potential source-credibility/model-version clarification, not a performance measurement.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which prior statement and model/version timeline is being corrected?
- **Transferability (inference):** Useful reminder to distinguish version histories; no release date is independently checked here.
- **Themes:** methodology

<a id="c204"></a>

### C204 — u/MarketingOk3093

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx57enl6gm8/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx57enl6gm8/)

- **Faithful contribution:** Reports roughly 20 tokens/s with Q6 on hardware described as matching another setup but with 64GB DDR4, then roughly 70 tokens/s after switching to Strata FN 3.8 IQ3_S; requests a Q8 27B llama configuration.
- **Type:** performance report and configuration request
- **Why relevant (assessment):** Relevant setup/quant/runtime trade-off, but model and quant changed together.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What is the referenced Q8 27B llama configuration?; What exact GPU, context, offload, and timings produced each speed?
- **Transferability (inference):** The reported speedup cannot isolate runtime quality or imply equal output quality across Q6 27B and FN IQ3_S.
- **Themes:** hardware, weights, runtime, alternatives, methodology

<a id="c205"></a>

### C205 — u/hahayeahisit

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxcjtxx3t0l/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxcjtxx3t0l/)

- **Faithful contribution:** Asks what should be used instead of the criticized option.
- **Type:** alternative request
- **Why relevant (assessment):** Substantive request for an actionable runtime/model replacement; referent is not explicit in this comment.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** What should be used instead?
- **Transferability (inference):** No comparative evidence or target configuration is supplied.
- **Themes:** alternatives, runtime

<a id="c206"></a>

### C206 — u/Coach_Unable

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx8whv9khic/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx8whv9khic/)

- **Faithful contribution:** Asks what llama.cpp offers over a host server rendered as ***, noting they already adjust KV quantization and context and use different harnesses on a normal single-GPU PC.
- **Type:** runtime comparison question
- **Why relevant (assessment):** Directly relevant to whether changing the backend helps a modest local setup.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** What advantages does llama.cpp offer over the server named as ***?; Is changing worthwhile for a single-GPU low-end setup with configurable KV/context?
- **Transferability (inference):** Cannot identify the obscured backend or infer that changing it improves quality.
- **Themes:** runtime, kv, context, hardware, harness

<a id="c207"></a>

### C207 — u/HourLocation2038

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwtqs4gzixs/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwtqs4gzixs/)

- **Faithful contribution:** Points out that the OP has not described how the model is run.
- **Type:** diagnostic information request
- **Why relevant (assessment):** Highlights missing configuration needed to attribute poor behavior.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** What exact runtime, model artifact, inference settings, and harness does the OP use?
- **Transferability (inference):** A request for reproducibility, not proof of a configuration fault.
- **Themes:** methodology, runtime, harness

<a id="c208"></a>

### C208 — u/Otherwise-Mail-4654

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwzcqw0cp7n/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwzcqw0cp7n/)

- **Faithful contribution:** Assumes from the post that the OP was using Q4.
- **Type:** quantization speculation
- **Why relevant (assessment):** Raises a relevant missing quant detail but supplies no confirmation.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Was the OP actually using Q4, and which quant artifact?
- **Transferability (inference):** Do not treat the guessed quant as established configuration.
- **Themes:** weights, methodology

<a id="c209"></a>

### C209 — u/MrRoyce

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxaoj0g9pr4/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxaoj0g9pr4/)

- **Faithful contribution:** Recalls an unspecified Qwen 27B under Ollama failing to complete tasks or stopping, then reports much better coding with Strata and QFN at 70–100 tokens/s; says Sol 6.1 praised its code over its own.
- **Type:** comparative anecdote
- **Why relevant (assessment):** Relevant contrasting experience, with many uncontrolled changes and no hardware disclosed.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** Which models/quants, hardware, context, and harness were used in each attempt?; Were identical tasks used, and was code independently tested?
- **Transferability (inference):** Backend/model changes and a model judging another output do not establish causal improvement or superiority.
- **Themes:** runtime, alternatives, workflow, methodology

<a id="c211"></a>

### C211 — u/InfiniteBlink

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnoy7kff6s/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnoy7kff6s/)

- **Faithful contribution:** Asks whether splitting Qwen instances means spawning subagents and whether Claude decides their tasks.
- **Type:** orchestration question
- **Why relevant (assessment):** Clarifies the local-worker/cloud-orchestrator workflow.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Does splitting Qwen instances mean spawning subagents?; Does Claude decide the subagents' tasks?
- **Transferability (inference):** Question only; no evidence that any specific orchestration is working.
- **Themes:** workflow, harness

<a id="c212"></a>

### C212 — u/Bagelsarenakeddonuts

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwojim7m6qq/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwojim7m6qq/)

- **Faithful contribution:** Describes using BMAD to turn epics into testable stories, followed by preflight, coding, and reviewing subagents and pushing to a repo mirror; failures/time thresholds route back to coding or Claude for scope/context repair. Says Claude helped build this workflow and it now runs fairly well.
- **Type:** first-person orchestration workflow
- **Why relevant (assessment):** Concrete alternative to broad autonomous local coding; success is not quantified.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What model/runtime and exact harness implement each stage?; What are the failure thresholds, tests, completion rates, and cloud-token costs?
- **Transferability (inference):** Task packaging and escalation are plausible practices, but this does not show Qwen alone handles broad projects.
- **Themes:** workflow, harness, context, methodology, economics

<a id="c213"></a>

### C213 — u/InfiniteBlink

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rworfqhmnq8/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rworfqhmnq8/)

- **Faithful contribution:** Asks how to adopt BMAD, including whether to name it in the prompt at the start of a project; mentions currently using Claude and Codex to review a simple game app.
- **Type:** workflow adoption question
- **Why relevant (assessment):** Substantive follow-up about installing or invoking planning structure.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** How should BMAD be adopted?; Should it be included in a prompt when starting a project?
- **Transferability (inference):** No BMAD efficacy or local-model outcome is demonstrated.
- **Themes:** workflow, harness

<a id="c214"></a>

### C214 — u/Bagelsarenakeddonuts

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwoypqops4i/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwoypqops4i/)

- **Faithful contribution:** Describes BMAD as project-installed agent skills enforcing specifications, planning, and reconciliation of changes; says it costs more tokens, is too much overhead for small projects, and personally uses it for work exceeding about five sessions or codebases around 20k+ lines, preferably adopted at project start. Mentions alternative philosophies.
- **Type:** workflow explanation and personal heuristic
- **Why relevant (assessment):** Adds implementation/overhead nuance to structured decomposition.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What version/configuration of BMAD and which alternatives fit smaller projects?; Do the personal session/line-count thresholds generalize, and what measurable overhead or drift reduction occurs?
- **Transferability (inference):** The thresholds and claims about preventing drift are personal heuristics, not universal requirements.
- **Themes:** workflow, harness, economics, methodology

<a id="c216"></a>

### C216 — u/sirphoenix3000

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx07r63b8gx/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx07r63b8gx/)

- **Faithful contribution:** Reports a game-changing experience using a linked club-3090 dual-GPU Qwen3.8-27B vLLM FP8/MTP recipe with the Pi agent on two RTX 3090s; recommends other recipes in that repository.
- **Type:** setup-specific recommendation
- **Why relevant (assessment):** Specific reproducible starting artifact, but different hardware from one 3090 and no quantified quality result.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Does the linked recipe work unchanged, and what context, speed, and task success does it achieve?; Is there an equivalent viable single-3090 configuration?
- **Transferability (inference):** Dual 3090 capacity and FP8/MTP behavior cannot be assumed on the target single card; link was not opened.
- **Themes:** runtime, hardware, harness, weights, alternatives

<a id="c217"></a>

### C217 — u/New_Egg_1024

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxc62fnpxuo/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxc62fnpxuo/)

- **Faithful contribution:** Recommends iteratively decomposing a vague goal into phases and hundreds of explicit tasks for smaller models, validating unspecified requirements, and retaining/educating engineers rather than replacing them.
- **Type:** task-decomposition advice
- **Why relevant (assessment):** Relevant proposed remedy for weak autonomous planning; no concrete run supplied.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** What decomposition/validation loop and acceptance checks make this reliable in practice?
- **Transferability (inference):** Organizational analogy is not proof that arbitrary tasks become executable by a small model.
- **Themes:** workflow, reasoning, methodology

<a id="c218"></a>

### C218 — u/dreamyrhodes

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxf5svaco11/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxf5svaco11/)

- **Faithful contribution:** Advises explicitly prohibiting coding initially, defining small feature parts first, then implementing step by step.
- **Type:** workflow recommendation
- **Why relevant (assessment):** Concrete prompt-level scoping suggestion without outcomes.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Does this staged approach improve completion on the OP's tasks?
- **Transferability (inference):** Low-cost experiment; not evidence that planning instructions solve runtime or capability limits.
- **Themes:** workflow, reasoning

<a id="c219"></a>

### C219 — u/SpiritRealistic8174

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1i17d9r51/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1i17d9r51/)

- **Faithful contribution:** Reports 3.6 usable for most tasks and 3.8 a step up; says Opus 5.5 planning/specs/sample code further improved scoped Qwen work, not long autonomous cross-file tasks. Also reports promising 3.8 planning/implementation in sandboxed Hermes with searchable persistent memory and explicit workflows, and argues RAM/context/resources and harness knowledge matter.
- **Type:** workflow and capability experience
- **Why relevant (assessment):** Important qualified success: scoped tasks plus cloud planning/memory, without hardware or controlled comparison.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Which model artifacts, hardware, context limits, Hermes settings, and tasks were used?; What changed in success rate and cloud cost after adding Opus planning?
- **Transferability (inference):** Task scope and scaffolding may help, but claims tying resources directly to quality require separating precision, truncation, offload, and runtime effects.
- **Themes:** workflow, harness, context, hardware, reasoning, economics, methodology

<a id="c220"></a>

### C220 — u/Blue_Eyed_Behemoth

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxcs1vesplx/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxcs1vesplx/)

- **Faithful contribution:** Asks whether Swift has its own licensing and whether the user encountered any licensing issues.
- **Type:** licensing question
- **Why relevant (assessment):** Substantive model-artifact deployment question; peripheral to coding quality.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Does Swift have its own licensing terms?; Were any licensing issues encountered?
- **Transferability (inference):** No license terms were inspected; model-name identity and deployment obligations remain unresolved.
- **Themes:** weights, alternatives, methodology

<a id="c221"></a>

### C221 — u/Damn-Sky

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx655rgilr9/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx655rgilr9/)

- **Faithful contribution:** Says they keep sessions short, have the model update CLAUDE.md, and resume in a new session, while explicitly being unsure this is good practice.
- **Type:** session-management anecdote
- **Why relevant (assessment):** Relevant mitigation for context accumulation, cautiously stated.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** Does updating CLAUDE.md preserve the information needed across resets?; Is this a good practice for the relevant harness/model?
- **Transferability (inference):** User-declared novice practice is a hypothesis to check, not an established context strategy.
- **Themes:** workflow, context

<a id="c222"></a>

### C222 — u/Twistpunch

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxb84gj6mjn/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxb84gj6mjn/)

- **Faithful contribution:** Reports QFN responding to a mentioned error by trying to fix it despite not being asked.
- **Type:** instruction-following complaint
- **Why relevant (assessment):** Retains substantive dissent about unwanted agent initiative.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** What prompt/harness and task boundaries produced the unsolicited fix?
- **Transferability (inference):** No transcript/configuration separates model behavior from harness instructions.
- **Themes:** workflow, harness, reasoning

<a id="c223"></a>

### C223 — u/Blue_Eyed_Behemoth

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxcmuj0gbkw/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxcmuj0gbkw/)

- **Faithful contribution:** Asks whether the model is 3.8 Flash Next Coder; reports spiraling on an RX9060XT 16GB with 64GB RAM and suspects context compaction removes important information and triggers cycles.
- **Type:** setup-specific failure report and question
- **Why relevant (assessment):** Counterexample to positive FN anecdotes; identifies a suspected compaction failure.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Are you using 3.8 Flash Next Coder?; What context/compaction settings, runtime, and quant are involved?; Do compaction traces actually show loss of required information before cycling?
- **Transferability (inference):** Hardware-specific first-person failure is meaningful, but compaction causality is suspected rather than demonstrated.
- **Themes:** context, harness, reasoning, hardware, alternatives, methodology

<a id="c224"></a>

### C224 — u/MiaIsOut

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxiaoegv3c3/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxiaoegv3c3/)

- **Faithful contribution:** Observes 3.8 27B sometimes spiraling for a long time before returning to the task and completing it well.
- **Type:** behavioral anecdote
- **Why relevant (assessment):** Substantive characterization of intermittent reasoning/task recovery, despite humorous wording.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** Under what runtime, context, sampler, and task conditions does this occur?; How often does recovery happen versus unrecoverable looping?
- **Transferability (inference):** No frequency or reproducible trace supports predicting eventual recovery.
- **Themes:** reasoning, workflow, methodology

<a id="c225"></a>

### C225 — u/pioo84

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxhz7425uas/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxhz7425uas/)

- **Faithful contribution:** Reports dual 3090s and 128GB RAM, HyperQwen/vLLM for 27B with a claimed 3×250k context, and Strata for Flash Next; plans in Hermes and codes in OpenCode without directly interacting with OpenCode. Says Strata context accounting is unclear to them.
- **Type:** setup and orchestration report
- **Why relevant (assessment):** Specific large-resource workflow; claimed context allocation needs interpretation.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Does 3×250k mean concurrent slots, effective filled context, or another allocation?; What quantization, memory use, and task-completion metrics apply?; How is context capacity calculated in Strata?
- **Transferability (inference):** Dual-GPU/128GB experience does not transfer directly to 24GB VRAM/32GB RAM; allocated windows are not validated usable context.
- **Themes:** hardware, runtime, context, harness, workflow, alternatives

<a id="c228"></a>

### C228 — u/former_farmer

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpa07vvv6r/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpa07vvv6r/)

- **Faithful contribution:** Asserts Qwen 27B needs 32–36GB of VRAM or unified memory for decent quantization and context.
- **Type:** hardware requirement assertion
- **Why relevant (assessment):** Direct capacity claim disputed elsewhere in the assigned comments.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which quantization, KV precision, context length, runtime, and meaning of decent support this threshold?
- **Transferability (inference):** Unspecified threshold is not a universal minimum; lower-memory counterreports must be compared under matching conditions.
- **Themes:** hardware, weights, kv, context

<a id="c229"></a>

### C229 — u/Snoo_81913

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpljsnzkpt/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpljsnzkpt/)

- **Faithful contribution:** Disputes the 32–36GB requirement, reporting Q4 XL Huihui in hipfire on a 24GB 7900 XTX at 164k context/Q8 KV, about 1500 tokens/s prefill and 95 tokens/s mean over 100k, with mmproj and 23.6GB used. Uses Pi, self-quantization and a ROCm backup; says Opus reviews find mostly a few fixes. Separately reports Flash Next Q3/XXS around 65 tokens/s with slow prefill and erratic output.
- **Type:** detailed setup-specific counterexample
- **Why relevant (assessment):** Strong local detail for a 24GB counterclaim, not independent validation; model variant and runtime differ.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Can the exact artifact, self-quant procedure, hipfire version, flags, and full memory/timing logs be shared?; Does mean over 100k describe decode speed at a filled context or an aggregate workload?; How does this variant compare on identical tested tasks with original 27B?
- **Transferability (inference):** AMD/hipfire/Huihui performance cannot establish a single-3090 baseline; model-judge praise is not independent correctness, and claimed spare context is untested.
- **Themes:** hardware, runtime, weights, kv, context, harness, alternatives, methodology

<a id="c230"></a>

### C230 — u/Choubix

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwouxcjb6w5/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwouxcjb6w5/)

- **Faithful contribution:** Asks whether the game result was one-shot or required a large set of instructions and guardrails, seeking a small starting point for children.
- **Type:** prompting/workflow question
- **Why relevant (assessment):** Tests how much intervention underlies an apparent game-building success.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Was it one-shot, or was a large instruction/guardrail set supplied?
- **Transferability (inference):** No outcome or setup in this comment; question usefully exposes hidden prompting effort.
- **Themes:** workflow, methodology

<a id="c231"></a>

### C231 — u/soulman901

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpbey5nc82/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpbey5nc82/)

- **Faithful contribution:** Recalls a short paragraph specifying a cat-and-mice Pac-Man-like game, blue mice after power pellets, corner pellets, random treats, and four levels; says the game mostly worked but needed a few tweaks and model-assisted fixes.
- **Type:** task-specific first-person outcome
- **Why relevant (assessment):** Clarifies that a small-game result was not entirely hands-off or perfect.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What was the exact original prompt, model/quant/runtime, and the failing items?; What testing supports mostly working?
- **Transferability (inference):** A bounded toy-game anecdote is not evidence for autonomous legacy-repository work; iterations were necessary.
- **Themes:** workflow, methodology

<a id="c233"></a>

### C233 — u/jtgyk

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxhe86invs3/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxhe86invs3/)

- **Faithful contribution:** Reports a mostly working 3D Pac-Man game produced in one shot after hours on Qwen3.8 27B Q2 with q4_0 KV in Unsloth Desktop; says Q4 versions seem less smart and need more hand-holding, asking whether others see this.
- **Type:** task/setup-specific outcome and quantization dissent
- **Why relevant (assessment):** Unusual low-precision success and a reversed quant-quality impression; not a controlled benchmark.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Has anyone else found Q4 less capable than Q2 here?; Were prompts, tasks, samplers, templates, model variants, and runtime versions identical?; What failures remain in the mostly working game?
- **Transferability (inference):** One small-game run does not show Q2 or q4_0 KV is generally better or safe for long agentic sessions.
- **Themes:** weights, kv, runtime, workflow, methodology

<a id="c234"></a>

### C234 — u/reliablemomentum

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwzlkj80nfo/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwzlkj80nfo/)

- **Faithful contribution:** Reports temperature 0.7 and min_p 0.05 stopping long-context looping for them and recommends checking samplers.
- **Type:** sampler recommendation with anecdotal outcome
- **Why relevant (assessment):** Direct tunable hypothesis for looping, without model artifact or controlled comparison.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Which runtime/model/quant/context and other sampler values were used?; Does changing these two values alone remove loops on matched tasks?
- **Transferability (inference):** Treat as a setup-dependent experiment, not a universal recommended sampler.
- **Themes:** sampling, context, reasoning, methodology

<a id="c235"></a>

### C235 — u/pragmojo

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6yektujdw/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6yektujdw/)

- **Faithful contribution:** Says using the recommended parameters works great.
- **Type:** parameter-success anecdote
- **Why relevant (assessment):** Positive but too unspecified to reproduce or identify the relevant recommendation.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** Which recommended parameters, source/version, model, and tasks?
- **Transferability (inference):** No concrete settings or outcome measures transfer.
- **Themes:** sampling, methodology

<a id="c236"></a>

### C236 — u/mtbMo

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2rxxlpajl/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2rxxlpajl/)

- **Faithful contribution:** Reports Qwen-Flash-next on Strata at about 600 prompt-processing tokens/s and 40 generation tokens/s using a 10-core Xeon v3, 128GB RAM, and two 16GB Mi50s.
- **Type:** hardware-specific throughput report
- **Why relevant (assessment):** Concrete alternative-model/runtime throughput with substantially different resources.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Which quant, context fill, Strata version, and measurement method produced 600pps/40tps?; What coding quality accompanies this speed?
- **Transferability (inference):** Dual accelerator and 128GB system-memory results do not imply target-machine throughput or task success.
- **Themes:** hardware, runtime, alternatives, methodology

<a id="c237"></a>

### C237 — u/sadomazoku

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxgolwt1kf4/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxgolwt1kf4/)

- **Faithful contribution:** Expresses skepticism at the apparent prevalence of Flash Next reports on very limited VRAM setups.
- **Type:** hardware plausibility concern
- **Why relevant (assessment):** Substantive caution about interpreting low-VRAM anecdotes, despite no configuration or explicit test.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** What offload, system RAM, storage, quantization, and effective context underlie the low-VRAM reports?
- **Transferability (inference):** Skepticism alone establishes neither feasibility nor infeasibility.
- **Themes:** hardware, alternatives, methodology

<a id="c239"></a>

### C239 — u/kirbyfanner

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwuli2ftlsz/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwuli2ftlsz/)

- **Faithful contribution:** Asks why vision was disabled, whether that affects VRAM or speed, how a 125B model fits 12GB VRAM plus 32GB RAM, what IQ3_S means, and what speed is achieved. Reports their own 27B uses 27GB VRAM and gets 40 tokens/s on an R9700.
- **Type:** hardware/quantization questions with baseline
- **Why relevant (assessment):** Preserves multiple practical questions and a hardware-specific comparison baseline.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Why turn vision off: memory savings, speed, or both?; How is the claimed 125B model run with 12GB VRAM and 32GB RAM?; What is IQ3_S?; What tokens/s does that setup achieve?; What quant/context/offload explain the commenter's 27GB 27B footprint?
- **Transferability (inference):** Model size alone does not determine resident footprint; comparisons require precision, offload, architecture, and context details.
- **Themes:** hardware, weights, context, runtime, alternatives, methodology

<a id="c240"></a>

### C240 — u/caylyn953

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwyy1kyogbo/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwyy1kyogbo/)

- **Faithful contribution:** Claims disabling vision allows that part of the model not to activate and to be discarded, saving space.
- **Type:** memory explanation
- **Why relevant (assessment):** Proposed partial answer to a vision/VRAM question; no model/runtime specifics.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Does the relevant runtime actually avoid loading or offload the vision component, and how much memory does it save?; Is there a speed effect?
- **Transferability (inference):** Savings depend on component loading/placement; disabling usage is not established to remove resident weights in every runtime.
- **Themes:** hardware, weights, runtime

<a id="c241"></a>

### C241 — u/Zestyclose_Yak_3174

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx9zhrqdmsg/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx9zhrqdmsg/)

- **Faithful contribution:** Reports using the Dstar DS4 fork for M1 Max and notes available options have pros and cons.
- **Type:** alternative-runtime anecdote
- **Why relevant (assessment):** Identifies an Apple-specific alternative, with no comparison data.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** Which fork version, model, configuration, and concrete trade-offs were observed?
- **Transferability (inference):** M1 Max experience does not directly apply to a discrete NVIDIA GPU.
- **Themes:** runtime, hardware, alternatives

<a id="c242"></a>

### C242 — u/cagriuluc

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx4pkjqtp5v/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx4pkjqtp5v/)

- **Faithful contribution:** Asks whether Flash Next has been tried; says it is much faster on their setup, so they use 27B only for vision.
- **Type:** alternative-model comparison and question
- **Why relevant (assessment):** Useful differing model-role allocation; setup and quality unspecified.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** Have you tried FN as well?; What setup, quants, context, and coding-quality comparisons support using FN over 27B?
- **Transferability (inference):** Speed preference is not a matched coding-reliability comparison.
- **Themes:** alternatives, workflow, hardware

<a id="c243"></a>

### C243 — u/Patient_Tea_401

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx5pfx4k49u/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx5pfx4k49u/)

- **Faithful contribution:** Reports FN GSQ-RCO-GGUF IQ3_XXS through the splash M1 fork with bf16 KV; subjectively prefers its science/general knowledge but finds long coding sessions drift more than 27B Q4. Allows that splash may cause drift and calls for published engine divergence metrics.
- **Type:** setup-specific model/runtime comparison
- **Why relevant (assessment):** Important counterpoint to FN enthusiasm; explicitly separates subjective knowledge impressions from uncertain drift cause.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Were FN and 27B evaluated with the same harness, tasks, context, and settings?; How much of the drift comes from quantization versus engine behavior?; What divergence data do these engines publish and against which reference?
- **Transferability (inference):** Different model sizes/quants and runtime uncertainty prevent assigning causality; divergence measurement is a useful proposal, not supplied evidence.
- **Themes:** alternatives, weights, kv, runtime, knowledge, reasoning, context, methodology

<a id="c244"></a>

### C244 — u/Chips_fr_

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2p1o3j3c1/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2p1o3j3c1/)

- **Faithful contribution:** Disputes quoted advice that Q4 is a minimum and Qwen3.8 is bad at reasoning; instead asserts Qwen tolerates low quants better than other models and reasons excellently, albeit slowly.
- **Type:** substantive dissent
- **Why relevant (assessment):** Directly preserves conflicting quantization and reasoning assessments.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which controlled quantization/reasoning comparisons support either side?; Does disabling reasoning help or hurt matched coding tasks?
- **Transferability (inference):** Neither side's universal capability claim is established by this reply.
- **Themes:** weights, reasoning, methodology

<a id="c245"></a>

### C245 — u/FudgeEducational2038

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2y4lslkf9/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2y4lslkf9/)

- **Faithful contribution:** Claims model weights tolerate substantial quantization, but because the attention/KV is linear and sparse, attention KV must remain full precision or at least q8/q8.
- **Type:** KV-precision recommendation
- **Why relevant (assessment):** Central asserted distinction between weight and KV quantization, disputed by q4 KV anecdotes.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which exact cache tensors and architecture does the claim describe?; What controlled task/divergence results establish a full-precision or Q8 minimum?
- **Transferability (inference):** Architecture explanation and mandatory threshold are unverified and should not be generalized across runtimes or cache components.
- **Themes:** weights, kv, runtime, methodology

<a id="c246"></a>

### C246 — u/Spiritual_Scheme8158

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxdplee86u9/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxdplee86u9/)

- **Faithful contribution:** Uses football-club tiers to portray Fable 5.5, Opus 5.5, and Sonnet 5.5 as much stronger than a 27B model, placing the latter in a much lower tier.
- **Type:** capability analogy/dissent
- **Why relevant (assessment):** Retained for its substantive small-local-versus-frontier capability ranking; contains no technical evidence.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** What shared tasks, budgets, and measured outcomes support the proposed ranking?
- **Transferability (inference):** An analogy cannot quantify the gap or establish whether the target setup is broken.
- **Themes:** alternatives, reasoning, methodology

<a id="c247"></a>

### C247 — u/feudalle

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxghtieoyhu/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxghtieoyhu/)

- **Faithful contribution:** Reports a 27B Q3 initially performing horribly, Q8 now being respectable as a junior developer, and recommends bite-sized tasks before leaving it to work.
- **Type:** quantization/workflow anecdote
- **Why relevant (assessment):** Counterpoint to low-quant tolerance claims, but runtime/hardware and matched tasks are absent.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Which 27B artifact, hardware, runtime, and context were used?; Were Q3 and Q8 tested with identical tasks and samplers?; How reliable are the unattended small tasks?
- **Transferability (inference):** Quant change is associated with a subjective improvement, not isolated causality or a guaranteed Q8 requirement.
- **Themes:** weights, workflow, methodology

<a id="c248"></a>

### C248 — u/dsdt

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkdxkdqi04/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkdxkdqi04/)

- **Faithful contribution:** Praises the model/tool for reading code line by line and being useful when the user has time and is willing to debug their own code.
- **Type:** qualified usefulness assessment
- **Why relevant (assessment):** Adds a human-debugging/time qualification to positive local coding claims.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which model/harness behavior demonstrates line-by-line reading, and what time/debugging effort is required?
- **Transferability (inference):** Not evidence of autonomous correctness; the claimed value explicitly depends on user time and debugging.
- **Themes:** workflow, methodology, economics

<a id="c249"></a>

### C249 — u/flatfalafel

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxjigjd4nts/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxjigjd4nts/)

- **Faithful contribution:** Asks whether the referenced harness will be made available or open source, noting they cannot use their employer's harness for their own projects.
- **Type:** harness availability question
- **Why relevant (assessment):** Substantive access/reproducibility question about a proposed working setup.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** Will that harness be made available/open source?
- **Transferability (inference):** No harness artifact or local-model result is supplied in this comment.
- **Themes:** harness, workflow, methodology

<a id="c251"></a>

### C251 — u/Omegaprime02

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm44e4hgo0/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm44e4hgo0/)

- **Faithful contribution:** Recommends disabling LM Studio load setting Offload KV Cache to GPU Memory so KV runs in system RAM, expecting a smaller speed penalty than the one discussed and persistent weight residency. Asks which quant is being used, whether Q8, and argues 32GiB VRAM should not overflow.
- **Type:** memory-placement advice and diagnostic question
- **Why relevant (assessment):** Actionable proposed workaround, but memory/speed assertions lack full configuration.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which quant are you running; is it Q8?; At what model, context length, KV precision, and batch/concurrency does 32GiB overflow?; Does CPU KV placement actually retain all weights on GPU and improve measured latency here?
- **Transferability (inference):** Placement can trade memory for throughput, but speed penalty and fit depend on backend/model/context; no guarantee from 32GiB alone.
- **Themes:** runtime, kv, hardware, context, weights, methodology

<a id="c252"></a>

### C252 — u/a_lost_shadow

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnlv6sn7oi/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnlv6sn7oi/)

- **Faithful contribution:** Asks what GPU is used, reports about 35 tokens/s at 85k filled context on an RX6800, and suspects a referenced 6 tokens/s means partial CPU offload.
- **Type:** setup-specific performance and diagnosis
- **Why relevant (assessment):** Useful filled-context throughput detail; offload explanation is explicitly a suspicion.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What card do you have?; What model/quant/runtime and actual offload settings produced each speed?; Does telemetry confirm CPU offload at 6 tokens/s?
- **Transferability (inference):** Different models, cards, or precision can explain speed differences; 6 tokens/s does not alone establish offload.
- **Themes:** hardware, context, runtime, methodology

<a id="c253"></a>

### C253 — u/Catch_022

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx4eejw3i5h/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx4eejw3i5h/)

- **Faithful contribution:** Asks whether relatively simple offline Python, KoboToolbox, and R coding is feasible with a 10GB RTX 3080.
- **Type:** hardware feasibility question
- **Why relevant (assessment):** Concrete low-VRAM use case, distinct from large autonomous repository work.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Can a 10GB 3080 do relatively simple offline Python, KoboToolbox, and R coding?; What model, context, and harness fit that workload?
- **Transferability (inference):** No result supplied; feasibility needs task granularity and full system-memory details.
- **Themes:** hardware, workflow, alternatives

<a id="c254"></a>

### C254 — u/Stats_monkey

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxaj5xcbtlv/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxaj5xcbtlv/)

- **Faithful contribution:** Suggests a 10GB setup may support single-file scripts with little context but not agentic project navigation.
- **Type:** pessimistic feasibility assessment
- **Why relevant (assessment):** Substantive dissent against low-resource agentic optimism.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which model/harness and project sizes support or contradict this limitation?
- **Transferability (inference):** Unmeasured blanket restriction is not a universal hardware boundary.
- **Themes:** hardware, context, workflow, alternatives

<a id="c255"></a>

### C255 — u/J35ter-

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxgnrw5gz35/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxgnrw5gz35/)

- **Faithful contribution:** Answers that coding is possible with an appropriate harness; reports using Deepseek Harness and Codex, recommends watching context/compaction, and claims a setup with 62GB RAM and 16GB+ VRAM can use Atrata with Qwen3.8 Flash in a different league from 27B.
- **Type:** harness advice and alternative-model claim
- **Why relevant (assessment):** Optimistic reply mixes a low-resource question with a substantially larger-memory suggested setup.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** Which model/setup does the initial yes refer to for a 10GB card?; What context/compaction settings and tests support the comparison?; What is meant by Atrata, as spelled in the comment?
- **Transferability (inference):** The 16GB+/62GB suggestion does not directly establish feasibility on 10GB; keep the source's backend spelling rather than assuming identity.
- **Themes:** harness, context, hardware, alternatives, workflow

<a id="c256"></a>

### C256 — u/Borkato

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxhh4sjkrdu/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxhh4sjkrdu/)

- **Faithful contribution:** Recommends Pi with Qwen 9B or 12B.
- **Type:** small-model/harness recommendation
- **Why relevant (assessment):** Concrete candidate direction for the 10GB/offline question, with no measured outcome.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which Qwen versions/quants and context fit, and how well do they perform on the requested tasks?
- **Transferability (inference):** Candidate configurations need testing; not proof of reliable agentic work.
- **Themes:** harness, alternatives, hardware

<a id="c257"></a>

### C257 — u/Throtex

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxiisbyeqat/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxiisbyeqat/)

- **Faithful contribution:** Argues restricting context defeats the model's verbose reasoning/refinement behavior; reports full-window use taking 40GB including weights on an A6000.
- **Type:** context argument with hardware footprint
- **Why relevant (assessment):** Specific memory anecdote supporting a larger window, but full-window length and precision are missing.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What is the full context length, weight quant, KV precision, and filled-versus-allocated memory accounting?; Does reducing the window measurably reduce task success with equal prompts?
- **Transferability (inference):** A 40GB A6000 configuration is not a universal memory requirement, and allocation does not prove beneficial use of every token.
- **Themes:** context, reasoning, hardware, weights, kv, methodology

<a id="c258"></a>

### C258 — u/Altruistic-Wolf-3938

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm0qnbw5gi/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm0qnbw5gi/)

- **Faithful contribution:** Asks whether a referenced memory/GPU configuration is 24+12.
- **Type:** hardware clarification question
- **Why relevant (assessment):** Minimal but substantive attempt to clarify a mixed-capacity setup; units and referent are absent.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Is the referenced configuration 24+12, and what devices/units do those numbers denote?
- **Transferability (inference):** Do not assume a specific two-GPU arrangement or usable combined capacity from this fragment.
- **Themes:** hardware, methodology

<a id="c259"></a>

### C259 — u/yourself88xbl

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwq0d1rvxk0/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwq0d1rvxk0/)

- **Faithful contribution:** Asks whether any head-to-head code-generation comparisons with cloud models have been run.
- **Type:** evaluation question
- **Why relevant (assessment):** Direct demand for comparative evidence rather than anecdotes.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Have any head-to-head comparisons for code generation against cloud models been run?; Were tasks, harnesses, prompts, attempts, tests, and budgets matched?
- **Transferability (inference):** No comparative result is provided here.
- **Themes:** methodology, alternatives

<a id="c260"></a>

### C260 — u/Giuseppe_0112

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx9sc31yxep/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx9sc31yxep/)

- **Faithful contribution:** Asks whether Codex can run with llama as its server.
- **Type:** harness/backend compatibility question
- **Why relevant (assessment):** Relevant potential route for using a local model in an existing coding harness.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Can Codex run with llama as the server, and through which API/configuration?
- **Transferability (inference):** Compatibility and tool/schema/template behavior require verification; llama could denote a backend rather than a specific model.
- **Themes:** harness, runtime

<a id="c261"></a>

### C261 — u/Stats_monkey

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxagmywxjtt/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxagmywxjtt/)

- **Faithful contribution:** Says that is essentially what the ollama launch command does under the hood.
- **Type:** integration explanation
- **Why relevant (assessment):** Proposed answer to the Codex/local-server integration question; no tested configuration.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which Ollama/Codex versions and generated configuration demonstrate the equivalence?
- **Transferability (inference):** Do not infer complete feature or template compatibility from the word essentially.
- **Themes:** harness, runtime, methodology

<a id="c262"></a>

### C262 — u/Business_Opening6629

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnama3fg69/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnama3fg69/)

- **Faithful contribution:** Reports trying Strata successfully but getting better performance from llama.cpp.
- **Type:** runtime comparative anecdote
- **Why relevant (assessment):** Retains dissent against general Strata performance superiority.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** Which model/quant, hardware, context, Strata/llama.cpp versions, and performance metric were compared?
- **Transferability (inference):** Uncontrolled performance recollection does not establish which backend is faster for the target setup.
- **Themes:** runtime, alternatives, methodology

<a id="c263"></a>

### C263 — u/Miserable-Answer-416

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx9xaydpr51/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx9xaydpr51/)

- **Faithful contribution:** Warns the referenced workflow will wear out an SSD quickly.
- **Type:** storage-longevity assertion
- **Why relevant (assessment):** Substantive potential operating-cost concern, with the mechanism unspecified in this comment.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** What read/write pattern, measured write volume, drive endurance, and timescale support rapid wear?
- **Transferability (inference):** Do not equate model offloading or SSD reads with proven write-wear; no endurance evidence is supplied.
- **Themes:** hardware, economics, methodology

<a id="c264"></a>

### C264 — u/oktollername

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxconq31nz4/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxconq31nz4/)

- **Faithful contribution:** Reports Qwen3.8 Next with Strata on 24GB VRAM having usable speed/capability while porting automations, including a task chaining PowerShell from Bash through SSH and Docker to diagnose a server.
- **Type:** setup/task-specific success report
- **Why relevant (assessment):** Relevant nontrivial tool-use example on 24GB, but a different model and missing system RAM/quant.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What system RAM/storage, quant, context, harness, and exact task transcript were used?; Were diagnostic actions/results independently checked?
- **Transferability (inference):** Concrete tool-chain success does not show original 27B coding reliability or fit on the OP's full configuration.
- **Themes:** hardware, runtime, alternatives, workflow, harness, methodology

<a id="c265"></a>

### C265 — u/vogelvogelvogelvogel

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkkiu70l9e/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkkiu70l9e/)

- **Faithful contribution:** Recommends 128k context, or at least the 80k suggested elsewhere, for agentic coding and suggests Pi.
- **Type:** context/harness recommendation
- **Why relevant (assessment):** Actionable but unsupported window target.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** What task-size evidence supports 80k/128k as a minimum, and with which memory/quant settings?
- **Transferability (inference):** Not a universal context requirement; fitting and effective utilization need separate validation.
- **Themes:** context, harness, hardware

<a id="c266"></a>

### C266 — u/nfored

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlpft4i3l1/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlpft4i3l1/)

- **Faithful contribution:** Asks which quant is used and reports well over 128k context at Q4 fully on GPU with 32GB VRAM.
- **Type:** context-fit counterexample and question
- **Why relevant (assessment):** Specific rebuttal to constrained-context/capacity claims, though model/runtime are unstated.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What quant are you using?; Which Q4 model artifact, backend, KV precision, actual context fill, and memory logs support the claimed fit?
- **Transferability (inference):** A Q4 allocation on 32GB does not establish fit at other precisions or long-context correctness.
- **Themes:** weights, hardware, context, kv, methodology

<a id="c267"></a>

### C267 — u/PigSlam

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwo8kn0wk9u/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwo8kn0wk9u/)

- **Faithful contribution:** Argues 32k context is too small and that 32GB VRAM should allow 192k+; reports doing so on an R9700.
- **Type:** context-capacity report and recommendation
- **Why relevant (assessment):** Specific capacity counterexample plus an unvalidated adequacy threshold.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Which model/quant, KV precision, runtime, and actual filled length support 192k+ on that R9700?; Which tasks show 32k to be insufficient?
- **Transferability (inference):** Hardware-specific window fit does not establish universal fit or useful long-context reasoning.
- **Themes:** context, hardware, weights, kv, methodology

<a id="c268"></a>

### C268 — u/dreamyrhodes

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx0akx2nwkg/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx0akx2nwkg/)

- **Faithful contribution:** Recommends limiting thinking when context is scarce, summarizing prior work in Markdown, recapitulating each step, and dividing failed features further. Reports Qwen3.6 35B A3B at 132k on 16GB VRAM plus 48GB system RAM works slowly for relatively small coding tasks.
- **Type:** setup-specific constrained-context workflow
- **Why relevant (assessment):** Concrete coping strategy and different-model example, explicitly limited in scope/speed.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Which runtime/quant/KV settings and offload produce this configuration?; Do summaries preserve necessary constraints, and how is success checked?
- **Transferability (inference):** Different architecture, version, and 48GB RAM preclude direct performance/quality transfer to 27B on the OP's machine.
- **Themes:** context, reasoning, workflow, hardware, alternatives

<a id="c269"></a>

### C269 — u/FudgeEducational2038

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1akis7esj/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1akis7esj/)

- **Faithful contribution:** Recommends Unsloth q3_xxs weights while asserting quantization-aware training permits weight compression but already-compressed sparse KV should remain fp16 if possible, then fp8/int8, and never below Q8.
- **Type:** weight/KV quantization prescription
- **Why relevant (assessment):** Explicit strong precision rule, without evidence, conflicting with q4 KV success reports.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which exact model artifact/training process supports the quantization-aware-training assertion?; Which cache/state tensors and runtimes accept these formats?; What controlled accuracy results justify a never-below-Q8 rule?
- **Transferability (inference):** Do not treat trust me or asserted architecture/training details as validated universal requirements.
- **Themes:** weights, kv, runtime, methodology

<a id="c270"></a>

### C270 — u/Miserable-Answer-416

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx9tikfsuxu/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx9tikfsuxu/)

- **Faithful contribution:** Recommends Bionic from LM Studio with Qwen3.8 and asserts the harness is everything.
- **Type:** harness recommendation
- **Why relevant (assessment):** Names an alternative agent path, but provides no setup or results.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which Bionic version/configuration and tasks were evaluated?; How much improvement remains when model/runtime/settings are held constant?
- **Transferability (inference):** The absolute harness claim is unsupported; use as a candidate comparison only.
- **Themes:** harness, workflow, alternatives

<a id="c271"></a>

### C271 — u/_RemyLeBeau_

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnk3p91twj/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnk3p91twj/)

- **Faithful contribution:** Asks for an example prompt to learn the referenced approach.
- **Type:** prompt example request
- **Why relevant (assessment):** Substantive practical follow-up, with no self-contained description of the approach.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Is there a prompt example to use and learn from?
- **Transferability (inference):** Referent is unresolved in this isolated comment; do not invent the prompt or workflow.
- **Themes:** workflow, methodology

<a id="c272"></a>

### C272 — u/FerretBoom

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwo3xy5u3kw/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwo3xy5u3kw/)

- **Faithful contribution:** Posts a proposed closed-book, no-tools/no-code-execution 20-question, 100-point general coding-reasoning benchmark for Qwen 27B, covering language tracing, debugging, algorithms, SQL, concurrency, and LRU design. Requests exact outputs, complete Python where appropriate, brief reasoning, and stated complexity; supplies no model responses, scores, or answer key.
- **Type:** evaluation artifact/proposed benchmark
- **Why relevant (assessment):** Concrete reusable question set, not an observed capability result and not an agentic repository benchmark.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Q1: What do a and b print after a shallow copy of [[1],[2]], mutation of b[0], and replacement of b[1] with [9]?; Q2: What do loop-created Python lambdas print, and how can only the lambda expression change to capture each iteration value?; Q3: What is the exact JavaScript logging order for synchronous A/E, zero-timeout B, Promise C, and queueMicrotask D?; Q4: What does a function returning 10 in try and 20 in finally print, and why?; Q5: What are tight time and auxiliary-space complexity for the nested i=1..n loop doubling j while j<=i?; Q6: For grades NULL,40,50,70, what do COUNT(*), COUNT(score), and SUM(CASE score>=50 THEN 1 ELSE 0 END) return?; Q7: What does inspect(iter([-1,2,3])) return after consuming positives, and how can it return both positives and the complete original sequence?; Q8: What is wrong with first_ge using hi=len(a)-1, and what corrected lower-bound implementation handles duplicate matches, x beyond the end, and empty input?; Q9: What prints when removing 2s during iteration over [1,2,2,3], and how can all 2s be removed while preserving list identity?; Q10: What does the incomplete merge output for [1,4] and [2,3,5], what is its defect, and how is it corrected in linear total length?; Q11: Implement O(n) valid_brackets for (), [], {}, ignoring other characters and handling mismatches and empty input.; Q12: Give the merged result for [(5,7),(1,3),(3,4),(8,8),(7,9)] and implement O(n log n) merging of closed intervals, including shared endpoints and empty input.; Q13: Implement O(V+E) topo_or_none over vertices 0..n-1, including disconnected vertices and returning None for cycles.; Q14: Find the minimum cost/path from S to T for S-A=2, S-B=5, A-B=1, A-T=7, B-T=2, and explain whether ordinary BFS always handles weighted paths.; Q15: Implement minimum reusable positive-coin count, returning -1 if impossible, without greedy-only logic, including amount zero, and give time/space complexity.; Q16: Implement O(n) expected-time longest_unique substring length, including abba, pwwkew, and empty input.; Q17: Implement O(n) expected-time counting of contiguous subarrays summing to k with negative values/zeros, satisfying the supplied examples.; Q18: Write SQL returning every user and their count of orders above 100, including zero counts and sorting by user id; explain the LEFT JOIN/WHERE filtering trap.; Q19: What final shared-counter values can two sequentially consistent atomic-read/write increments yield, what interleaving loses an update, and what synchronization fixes it?; Q20: Design expected-O(1) LRU get/put, describing structures, recency, insert/update/eviction, and nonnegative capacity including zero.; What are the answer key, grading rubric, model/settings, repeated-run scores, and validated correctness of the benchmark assertions?
- **Transferability (inference):** Useful bounded knowledge/reasoning probe, but closed-book answers do not establish repository navigation, tool reliability, or autonomous coding; no execution/score occurred in this indexing task.
- **Themes:** methodology, knowledge, reasoning

<a id="c273"></a>

### C273 — u/TheRealCranedisk

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwx0n0cscki/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwx0n0cscki/)

- **Faithful contribution:** Says they sometimes use emphasis to reinforce a point to another person.
- **Type:** emphasis/formatting dissent
- **Why relevant (assessment):** Very low technical relevance; retained as a substantive defense of intentional emphasis, not a pure reaction. The disputed assumption is not stated in this comment.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** What specific assumption about emphasis is being disputed?
- **Transferability (inference):** Personal use of emphasis is not evidence about model quality; the broader disputed assumption is unresolved here.
- **Themes:** methodology

<a id="c274"></a>

### C274 — u/boosnie

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxaxvib3jxd/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxaxvib3jxd/)

- **Faithful contribution:** Rejects a formatting-based assumption, saying they use bold and italic to make messages easier to read.
- **Type:** emphasis/formatting dissent
- **Why relevant (assessment):** Very low technical relevance; substantive explanation of deliberate formatting rather than a pure reaction. The disputed assumption is not stated here.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** What evidence beyond bold/italic supports the assumption being disputed?
- **Transferability (inference):** A preference for bold/italic does not establish model capability or the truth of the unspecified disputed assumption.
- **Themes:** methodology

<a id="c275"></a>

### C275 — u/jtgyk

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxhsfome2le/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxhsfome2le/)

- **Faithful contribution:** Predicts Qwen 4 will arrive soon with more recent training data and suggests trying it then, explicitly unsure about Drupal 11 knowledge.
- **Type:** future-model/knowledge suggestion
- **Why relevant (assessment):** Addresses possible knowledge freshness but supplies neither availability nor task evidence.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** When will Qwen 4 be available?; Will its training actually cover Drupal 11 sufficiently for the target tasks?
- **Transferability (inference):** Time-sensitive speculation is not a currently tested remedy; no release or training claim was externally checked.
- **Themes:** knowledge, alternatives, methodology

<a id="c276"></a>

### C276 — u/colonelx_

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2cjsbmnc2/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2cjsbmnc2/)

- **Faithful contribution:** Asks for a coding-model recommendation for 10GB VRAM and 64GB RAM; reports Qwen models in OpenCode taking very long to reason through agent tasks, including 4B/9B experiments in LM Studio with 8k–200k context.
- **Type:** setup-specific failure report and recommendation question
- **Why relevant (assessment):** Concrete low-end agentic complaint and broad configuration experiments, without timing/precision detail.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What is the best coding model for 10GB VRAM and 64GB RAM?; Is a decent coding agent viable on that PC?; Which versions/quants, actual context fills, hardware, and offload settings explain the latency?
- **Transferability (inference):** Large allocated windows and slow reasoning do not identify a single root cause; low model parameter count alone does not guarantee responsiveness.
- **Themes:** hardware, context, reasoning, runtime, harness, alternatives, methodology

<a id="c277"></a>

### C277 — u/FudgeEducational2038

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2p5whu2sg/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2p5whu2sg/)

- **Faithful contribution:** Recommends Strata with 3.8 Flash Next, dismisses older 3.5 models, and claims 40–50 tokens/s on a 10GB card and 64GB of vram, with easy Windows GUI autotuning. The source says vram for the 64GB figure despite the preceding system-RAM question.
- **Type:** alternative/runtime performance assertion
- **Why relevant (assessment):** Direct optimistic answer to low-resource feasibility, but no first-person run and internally ambiguous memory wording.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Is the 64GB figure system RAM rather than VRAM?; What exact model/quant, storage, context, and benchmark support 40–50 tokens/s on 10GB?; Does the GUI support agentic tool use, and what minimum does this version require?
- **Transferability (inference):** Do not silently correct the source or treat throughput/feasibility as measured; the 10GB claim conflicts with the later reported 12GB minimum.
- **Themes:** runtime, alternatives, hardware, methodology

<a id="c278"></a>

### C278 — u/colonelx_

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxfsj7j265f/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxfsj7j265f/)

- **Faithful contribution:** Asks whether agentic use should run Strata in a terminal and connect its API to OpenCode, given an understanding that the Windows app is chat-only.
- **Type:** runtime/harness integration question
- **Why relevant (assessment):** Separates chat convenience from actual agent integration.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Should Strata be run through the terminal with its API connected to OpenCode for agentic tasks?; Which approach is recommended, and is the Windows app actually limited to chat?
- **Transferability (inference):** Application mode/API compatibility and tool support need confirmation; no successful connection is reported.
- **Themes:** runtime, harness, workflow

<a id="c279"></a>

### C279 — u/FudgeEducational2038

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2rvr6n1r6/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2rvr6n1r6/)

- **Faithful contribution:** Links Strata v0.2.8 and claims the Windows version automatically downloads/configures a 180B model that runs at 40 tokens/s and 262k context even on the referenced hardware, provided an SSD is available; recommends this over 4B/9B models.
- **Type:** version-linked feasibility/performance claim
- **Why relevant (assessment):** Specific version and ambitious low-resource claim, without run evidence.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Does v0.2.8 support the commenter's 10GB GPU/64GB RAM and which exact model/quant?; Are 40 tokens/s and 262k measured at filled context, with what prefill/latency/storage behavior?; How does this reconcile with the reported 12GB documented minimum?
- **Transferability (inference):** The link was not opened; advertised setup automation, large parameter count, and context size do not establish coding reliability or target-hardware fit.
- **Themes:** runtime, alternatives, hardware, context, weights, methodology

<a id="c280"></a>

### C280 — u/colonelx_

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3lk939up1/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3lk939up1/)

- **Faithful contribution:** Expresses intent to try the suggested setup and confirms having an SSD they consider decent.
- **Type:** hardware disclosure/intention
- **Why relevant (assessment):** Retained only because SSD availability adds a hardware prerequisite detail; not a success report.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** What SSD capacity/interface and endurance are available?; Does the suggested setup actually run on this hardware?
- **Transferability (inference):** Intent and a vague SSD description do not validate the preceding performance claims.
- **Themes:** hardware, methodology

<a id="c281"></a>

### C281 — u/roiki11

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6qyzgxsip/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6qyzgxsip/)

- **Faithful contribution:** Questions whether Strata requires 12GB VRAM.
- **Type:** minimum-hardware challenge
- **Why relevant (assessment):** Direct challenge to the 10GB feasibility recommendation.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Does Strata require 12GB VRAM for the relevant version/model?
- **Transferability (inference):** An unresolved question, not a verified minimum.
- **Themes:** hardware, runtime, methodology

<a id="c283"></a>

### C283 — u/colonelx_

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxd3mqo0eqo/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxd3mqo0eqo/)

- **Faithful contribution:** States having 10GB VRAM and asks whether it is enough.
- **Type:** hardware feasibility question
- **Why relevant (assessment):** Restates the target constraint explicitly amid conflicting requirements.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** Is 10GB VRAM enough for the suggested Strata model/version?
- **Transferability (inference):** No successful load or task outcome is reported.
- **Themes:** hardware, runtime, alternatives

<a id="c284"></a>

### C284 — u/roiki11

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxhh6qkhaci/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxhh6qkhaci/)

- **Faithful contribution:** Says they do not know whether 10GB works and that documentation says 12GB minimum.
- **Type:** reported documentation constraint
- **Why relevant (assessment):** Important caveat to low-VRAM recommendations, but the document is not quoted or linked here.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which documentation/version/model specifies the 12GB minimum?; Are there supported smaller-model exceptions or overrides for 10GB?
- **Transferability (inference):** Treat as an unverified report of documentation, not an independently confirmed hard floor.
- **Themes:** hardware, runtime, methodology

<a id="c285"></a>

### C285 — u/FudgeEducational2038

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2tv4x6js0/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2tv4x6js0/)

- **Faithful contribution:** Recommends choosing Strata's GYRO S option rather than suggested medium/large variants, or ISTA coder as a lighter/faster fallback, describing it as Flash Next with the less coding-used half removed.
- **Type:** smaller-variant recommendation
- **Why relevant (assessment):** Possible answer to memory limits, but architecture, sizes, quality, and fit are unverified.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** What are the actual parameter/quant sizes, VRAM/RAM/storage requirements, and coding scores for GYRO S and ISTA coder?; Do these options work with 10GB VRAM in the cited release?; What precisely is removed and what capabilities are lost?
- **Transferability (inference):** The half-brain description is an analogy/assertion, not a verified technical account or quality guarantee.
- **Themes:** alternatives, weights, hardware, runtime, knowledge, methodology

<a id="c286"></a>

### C286 — u/matrixino

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx34ejp7kwy/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx34ejp7kwy/)

- **Faithful contribution:** Dismisses low-end local feasibility and advises a €4k–€6k budget for a decent machine.
- **Type:** economic/hardware dissent
- **Why relevant (assessment):** Strongly pessimistic cost assertion contradicting small-setup suggestions, with no bill of materials or workload.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** What hardware, region/prices, task standard, and throughput target justify €4k–€6k?
- **Transferability (inference):** An unspecified definition of decent cannot establish a universal spending floor.
- **Themes:** economics, hardware, alternatives

<a id="c287"></a>

### C287 — u/Material-Database-24

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2udz5d1nm/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2udz5d1nm/)

- **Faithful contribution:** Reports using 27B with q4 KV extensively for coding without problems.
- **Type:** KV-precision counterexample
- **Why relevant (assessment):** Direct dissent from never-below-Q8 KV prescriptions; details appear separately in C289.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Which model/runtime/hardware, tasks, context fills, and tests support zero problems?; How does q4 KV compare to higher precision under matched conditions?
- **Transferability (inference):** A first-person counterreport challenges a universal prohibition but does not prove q4 safe for every task/cache/backend.
- **Themes:** kv, workflow, methodology

<a id="c288"></a>

### C288 — u/colonelx_

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3mmrsel5w/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3mmrsel5w/)

- **Faithful contribution:** Asks for hardware specifications and the coding agent used.
- **Type:** reproducibility question
- **Why relevant (assessment):** Critical missing context for interpreting the q4 KV success report.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** What are your hardware specifications?; Which coding agent are you using?
- **Transferability (inference):** Question only; no configuration supplied by this commenter.
- **Themes:** hardware, harness, methodology

<a id="c289"></a>

### C289 — u/Material-Database-24

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx4buwqgf4y/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx4buwqgf4y/)

- **Faithful contribution:** Reports StrixHalo with llama.cpp Vulkan/ROCm and mainly VS Code's built-in agent; says Q4_K_XL weights with q4 KV and medium thinking had no issues, while current MXFP4 weights plus f16 gives higher speed and perceived quality with llama.cpp/ROCm at about 10GB extra memory. Qualifies the VS Code praise for non-swarm use.
- **Type:** detailed KV/weight/runtime experience
- **Why relevant (assessment):** Important context for C287 and direct tension with strict KV rules; several configuration dimensions changed.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What exact StrixHalo memory size, model artifact, versions, context lengths, and tests apply?; How much improvement is attributable separately to MXFP4, f16 KV, ROCm, or other changes?; What does medium thinking map to in the harness/runtime?
- **Transferability (inference):** Unified-memory StrixHalo and extra 10GB headroom differ from a single 24GB discrete GPU; subjective quality is not an isolated precision benchmark.
- **Themes:** hardware, runtime, weights, kv, harness, reasoning, methodology

<a id="c290"></a>

### C290 — u/DisastrousProfit5204

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxfot7lnelf/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxfot7lnelf/)

- **Faithful contribution:** Advises increasing context to 256k/512k for complex projects, claiming the model handles it.
- **Type:** long-context recommendation
- **Why relevant (assessment):** Substantive capability claim but lacks setup, task, or fill details.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which model/configuration fits 256k/512k and demonstrably retains task accuracy?; What actual context fills and memory costs were measured?
- **Transferability (inference):** Large configured windows are not proof of effective retrieval, reasoning, or agent completion.
- **Themes:** context, hardware, methodology

<a id="c291"></a>

### C291 — u/nfored

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlls45pxgl/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlls45pxgl/)

- **Faithful contribution:** Reports getting 200k context working at Q4 on an R9700.
- **Type:** hardware-specific context-fit anecdote
- **Why relevant (assessment):** Additional large-window counterreport without quality or KV details.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Which artifact/backend, KV precision, and filled-context memory/latency measurements support this?
- **Transferability (inference):** Working allocation/load does not establish long-context coding quality or fit on a 3090.
- **Themes:** hardware, weights, kv, context, methodology

<a id="c292"></a>

### C292 — u/Hofi2010

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnge4v0bs4/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnge4v0bs4/)

- **Faithful contribution:** Assesses 27B Q8 as good for easy-to-medium tasks with a good context window and roughly 48GB maximum memory, says floating point needs more, and calls Sonnet 5.5 much better but more expensive.
- **Type:** capability/memory/cost assessment
- **Why relevant (assessment):** Moderate local capability view with explicit frontier gap and cost trade-off; no first-person setup.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** What context/KV/runtime and memory accounting support about 48GB max?; What tasks, success rates, and usage/hardware costs support the quality/cost comparison?
- **Transferability (inference):** The memory number and task labels are not universal bounds; no measured total-cost comparison is provided.
- **Themes:** weights, context, hardware, alternatives, economics, methodology

<a id="c293"></a>

### C293 — u/Annual_Award1260

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwok76gf7aa/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwok76gf7aa/)

- **Faithful contribution:** Reports using Qwen 27B for browser automation/testing and full GLM5.3 with a claimed one-million-token context for coding; suggests Deepseek Flash or GLM Flash.
- **Type:** model-role anecdote and alternatives
- **Why relevant (assessment):** Differentiates Qwen's chosen role from coding, but full-model hardware and outcomes are absent.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What hardware/runtime/context fill and coding outcomes support the GLM setup?; Which Flash variants fit the OP's machine and how do they perform?
- **Transferability (inference):** Using another much larger-context model does not establish a local alternative within 24GB VRAM/32GB RAM.
- **Themes:** alternatives, workflow, context, hardware

<a id="c294"></a>

### C294 — u/cmndr_spanky

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwonckfzpgj/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwonckfzpgj/)

- **Faithful contribution:** Requests exact harness, quant, inference settings, and usable context; recommends OpenCode over allegedly bloated Claude Code, warns against below-Q4 weights, and argues many CLAUDE.md/agent.md files and 10+ skills can exhaust a limited context and cause confusion.
- **Type:** diagnostic questions and harness/context prescription
- **Why relevant (assessment):** Actionable missing-information checklist mixed with absolute/unvalidated rules disputed by other comments.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** What harnesses have you tried?; Which weight quantization and inference settings are you using?; What context window is set, and how much is effectively usable?; Does the codebase contain dozens of CLAUDE.md/agent.md files and 10+ skills?; How many instruction/skill tokens are actually injected and do controlled removals improve success?
- **Transferability (inference):** Context overhead is measurable, but blanket Claude Code incompatibility, Q4 minimum, and guaranteed failure from file counts are not established.
- **Themes:** harness, weights, sampling, context, workflow, methodology

<a id="c295"></a>

### C295 — u/Iamisseibelial

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwondcvu36q/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwondcvu36q/)

- **Faithful contribution:** Recommends trying the local model in Claude Code and reports that Claude Code and Hermes work well for specific tasks in their experience.
- **Type:** harness-success anecdote
- **Why relevant (assessment):** Direct dissent from C294's categorical Claude Code warning, explicitly task-scoped.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** Which local model, adapter/API, runtime settings, and specific tasks worked in Claude Code or Hermes?
- **Transferability (inference):** Vague scoped success rebuts neither all overhead concerns nor proves general compatibility/reliability.
- **Themes:** harness, workflow, alternatives, methodology

<a id="c296"></a>

### C296 — u/CordusPorf

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwonfy5aly8/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwonfy5aly8/)

- **Faithful contribution:** Reports a 4060 Ti with 16GB stated as ram and 128GB system RAM working well as a local worker/subagent when an orchestrator scopes tasks appropriately.
- **Type:** hardware/scoped-worker anecdote
- **Why relevant (assessment):** Relevant success on a smaller GPU but much more system RAM; model/artifact unspecified in this comment.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Which model/quant/runtime, context and actual offload are used?; Does 16GB ram refer to GPU VRAM?; What task acceptance tests and orchestrator effort underlie does well?
- **Transferability (inference):** A 128GB-RAM scoped-worker setup does not establish autonomous performance or target-machine feasibility.
- **Themes:** hardware, workflow, harness, context, methodology

<a id="c297"></a>

### C297 — u/Happy_Brilliant7827

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwonj3vf6p0/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwonj3vf6p0/)

- **Faithful contribution:** Suggests looking for Atlas and other coding platforms on GitHub.
- **Type:** platform recommendation
- **Why relevant (assessment):** Potential harness alternative, too underspecified to identify a unique project.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which Atlas repository/version is intended and what local-model integration/results does it provide?
- **Transferability (inference):** No project was searched or verified; name alone does not establish suitability.
- **Themes:** harness, alternatives

<a id="c298"></a>

### C298 — u/ismaelgokufox

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwooah6maw4/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwooah6maw4/)

- **Faithful contribution:** Reports positive Qwen3.8 27B personal/family development and diagnosis on Fedora44, Ryzen5600X, RX6800 16GB, and 32GB DDR4 at about 350 prompt-processing/32 generation tokens/s; cites an OpenDeck/Stream Deck monitoring-plugin task. Supplies an Unsloth llama.cpp release link and llama-swap command for Swift1.5 Qwen3.8-27B GSQ-RCO IQ3_XXS MTP with vision mmproj not GPU-offloaded, flash attention, no context shift, 64k fit-context target, q8_0 K/V, all GPU layers/auto-fit, draft-MTP speculation, medium preserved reasoning, temp1.0/top_p0.95/top_k20/min_p0/presence0/repeat1.0, and stripping client sampler/effort parameters.
- **Type:** detailed reproducible configuration and outcome
- **Why relevant (assessment):** Most detailed assigned single-GPU low-quant success recipe, but fine-tuned variant/AMD stack differs from original Qwen on 3090.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What exact llama.cpp release, actual fitted context, memory/offload breakdown, and task tests produced the result?; How do these settings perform against original Qwen27B Q4+ on identical tasks?; How much improvement comes from the variant, MTP, enforced settings, template, or harness?
- **Transferability (inference):** Useful candidate recipe, not proof IQ3_XXS generally matches Q4+; command uses a specific derivative and AMD/Fedora environment. Link was not opened and recipe was not run.
- **Themes:** hardware, runtime, weights, kv, context, sampling, reasoning, harness, workflow, methodology

<a id="c299"></a>

### C299 — u/Original-Mistake8624

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3fodrkioz/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3fodrkioz/)

- **Faithful contribution:** Asks whether Swift1.5 IQ3_XXS has been compared with original Qwen27B at Q4 or higher on identical coding tasks for accuracy and completion rate.
- **Type:** controlled-comparison question
- **Why relevant (assessment):** Directly identifies the key verification gap in the detailed low-quant recipe.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Has Swift1.5 IQ3_XXS been compared with original Qwen27B Q4+ on the same coding tasks for accuracy and task completion rate?; Were harness, prompts, context, runtime, attempts, and tests controlled?
- **Transferability (inference):** No head-to-head results appear in this comment; derivative-model anecdotes cannot settle original-model precision trade-offs.
- **Themes:** methodology, weights, alternatives

<a id="c300"></a>

### C300 — u/WCWRingMatSound

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwoqlig3vl1/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwoqlig3vl1/)

- **Faithful contribution:** Reports Qwen taking 51 minutes just to git add, commit, and push on a 64GB MacBook Pro M5 Pro; expresses similar frustration with local AI.
- **Type:** hardware/task-specific failure report
- **Why relevant (assessment):** Strong negative latency anecdote, but model size/version, harness, and cause are missing.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Which Qwen model/quant/runtime/harness, context, and tool traces account for the 51 minutes?; Was delay reasoning, tool waiting/retries, repository hooks, network, or a different bottleneck?
- **Transferability (inference):** Different Apple hardware and an uninstrumented elapsed time do not establish intrinsic model speed or a 3090 failure cause.
- **Themes:** hardware, runtime, harness, reasoning, workflow, methodology

<a id="c301"></a>

### C301 — u/BarWhole6344

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwoqxv4a5k5/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwoqxv4a5k5/)

- **Faithful contribution:** Recommends buying hosted tokens rather than expecting a great Qwen 27B coding experience; claims DS V4.1 Flash 1017 Fast on Baseten reaches about 1–2k tokens/s and is hard to leave once tried.
- **Type:** hosted-alternative recommendation
- **Why relevant (assessment):** Relevant dissent on local practicality and latency, not a diagnosis of the reported failure.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** Which task, serving conditions, cost and measurement support the 1–2k tokens/s claim?
- **Transferability (inference):** Hosted model and infrastructure differ from local 27B; speed and preference do not establish comparative coding correctness.
- **Themes:** alternatives, economics, hardware

<a id="c302"></a>

### C302 — u/Schudz

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwot2r7ie1t/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwot2r7ie1t/)

- **Faithful contribution:** Reports reliable Qwen 3.8 27B coding with Unsloth: RTX 6000 Pro, Q8 weights/KV, about 120 tokens/s and 131k context with custom compaction. Also reports Q3/KV Q4 on a 9070 XT with 32GB RAM at about 45 tokens/s and 70k context. Uses Claude/Opus for complex bootstrapping and DeepSeek for parallel projects; describes a Fable-derived variant as roughly 5% better and speculates about an upcoming Qwen release.
- **Type:** multi-setup experience
- **Why relevant (assessment):** Detailed positive counterexample that also documents hybrid delegation and a workflow requiring at least 100 tokens/s.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What runtime build, tasks, benchmark method and context occupancy underlie the rates and 5% estimate?; What specifically does the custom harness do to compact context?
- **Transferability (inference):** Neither the larger GPU nor the AMD low-quant setup reproduces the OP machine. Positive low-quant experience challenges universal Q8 minimums; the release forecast is unverified speculation.
- **Themes:** runtime, weights, kv, context, hardware, harness, workflow, alternatives, methodology

<a id="c303"></a>

### C303 — u/jellyrole

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwoxu38s7tx/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwoxu38s7tx/)

- **Faithful contribution:** Asks why the preceding RTX 6000 Pro setup uses only Q8.
- **Type:** configuration question
- **Why relevant (assessment):** Preserves an unanswered question about precision choice on larger hardware.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Why choose Q8 rather than a higher-precision format on the RTX 6000 Pro?
- **Transferability (inference):** A question, not evidence that higher precision would improve the reported workload.
- **Themes:** weights, hardware

<a id="c304"></a>

### C304 — u/Humble_Ad_1875

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpzl823tlu/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpzl823tlu/)

- **Faithful contribution:** Relays Claude advice that Qwen3-Coder 30B MoE has 3.3B active parameters, a roughly 19GB Q4 footprint and 256K context, and would tolerate RAM overflow. Asks whether it will run on a Ryzen 9 9900X3D, 64GB DDR5-6000 and RTX 5080.
- **Type:** secondhand advice and feasibility question
- **Why relevant (assessment):** Specific hardware question; the relayed AI answer is not a measured deployment report.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Will this model and intended context actually fit and run usefully on the listed machine?; Are the quoted footprint, context and offload-speed claims accurate?
- **Transferability (inference):** Active-parameter count alone does not validate total-memory fit or acceptable offload latency. C305 supplies alternatives, not a measured answer.
- **Themes:** alternatives, hardware, weights, context, runtime, methodology

<a id="c305"></a>

### C305 — u/sudden_aggression

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwqrx7bqmcj/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwqrx7bqmcj/)

- **Faithful contribution:** Warns that AI advice may be stale, calls Qwen3-Coder 30B no longer state of the art, and recommends a heavily quantized Qwen 3.8 Flash Next or Q4 Qwen 3.6 35A3B for the presumed 16GB RTX 5080.
- **Type:** alternative recommendation and source criticism
- **Why relevant (assessment):** Relevant to C304 model selection, but unsupported performance and freshness judgments.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which exact quant, runtime, RAM demand and context make either recommendation viable on that hardware?
- **Transferability (inference):** Treat the training-data timing and model ranking as commenter assertions; no comparative test is supplied.
- **Themes:** alternatives, weights, hardware, methodology

<a id="c306"></a>

### C306 — u/alexander123454

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwozdfus9t1/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwozdfus9t1/)

- **Faithful contribution:** Says a harness, preferably a metaharness, is necessary; reports using GSD and advertises forthcoming metaharness features in the commenter’s open-source localharness 0.26.0, requesting task feedback.
- **Type:** harness recommendation and self-promotion
- **Why relevant (assessment):** Substantive orchestration suggestion, with an explicit author interest and no effectiveness results.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** What are the proposed metaharness features and which failures do they prevent?; Does localharness improve outcomes on this model and hardware?
- **Transferability (inference):** A project recommendation is not evidence that a metaharness is required; repository was not accessed.
- **Themes:** harness, workflow

<a id="c307"></a>

### C307 — u/Bunksha

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwp02lkgvc4/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwp02lkgvc4/)

- **Faithful contribution:** Asks the OP’s quant; estimates Q4 weights at about 17GB plus about 9GB for 128k context, predicting VRAM overflow and slowness on 24GB. Reports excellent coding with the same model at Q8 and 256k context.
- **Type:** memory hypothesis and setup report
- **Why relevant (assessment):** Useful distinction between memory pressure and a positive higher-precision experience, but memory numbers are estimates.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What quant is the OP actually using?; What KV format, hardware, occupied context and allocation behavior support the memory estimates and reported Q8/256k run?
- **Transferability (inference):** Overflow can motivate a latency hypothesis but does not itself establish reduced reasoning quality; the positive setup lacks hardware details.
- **Themes:** weights, kv, context, hardware, runtime

<a id="c308"></a>

### C308 — u/FollowKryst

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwp43fr0jok/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwp43fr0jok/)

- **Faithful contribution:** Reports using Qwen 27B with Pi/llama.cpp on a 64GB M1 Max, finding it good but slow and memory-heavy; currently prefers Q4_K_M Qwen 3.6 35B in terminal. Describes noticeable harness/runtime differences and asks for the OP harness, quant and tasks, while explicitly cautioning about Apple/Nvidia comparisons.
- **Type:** cross-platform experience and diagnostic request
- **Why relevant (assessment):** Detailed positive experience with appropriate uncertainty about hardware transfer.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Which harness, quant and concrete tasks does the OP use?; Were LM Studio, Hermes, Pi and terminal comparisons made with identical weights, prompts and sampling?
- **Transferability (inference):** Apple unified memory and a different primary model are not a 3090 reproduction; terminal use alone is not demonstrated causal.
- **Themes:** runtime, harness, weights, hardware, alternatives, methodology

<a id="c309"></a>

### C309 — u/808phone

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwp6banwgir/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwp6banwgir/)

- **Faithful contribution:** Recommends OpenCode or Pi and asks about the codebase. Reports using LM Studio with Pi, OpenCode or Kilo Code and says the model follows instructions and writes decent code, with a stronger model spot-checking results.
- **Type:** harness experience and hybrid review
- **Why relevant (assessment):** Relevant positive report whose stated success includes external review.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What kind of codebase and tasks are involved?; What quant, hardware and corrections by the stronger model are required?
- **Transferability (inference):** Cannot attribute reviewed outcomes solely to Qwen, or assume the same harness works equally on an unspecified legacy codebase.
- **Themes:** harness, runtime, workflow, methodology

<a id="c310"></a>

### C310 — u/Captain--Cornflake

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwp9jbm3zxh/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwp9jbm3zxh/)

- **Faithful contribution:** Attributes thinking loops to prompt ambiguity and proposes a custom lightweight harness that detects repeated reasoning words such as “hmmm” or “but” and falls back to the original code after about three repetitions; claims public agents have excessive tool bloat.
- **Type:** loop-control heuristic
- **Why relevant (assessment):** Directly addresses looping, but provides no validated detector or correctness evidence.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** How reliably does word repetition distinguish a harmful loop from useful reasoning?; How is original code recovered and checked before use?
- **Transferability (inference):** An untested early-stop heuristic could discard valid reasoning or preserve an incorrect first attempt; no universal threshold is established.
- **Themes:** reasoning, harness, workflow, context

<a id="c311"></a>

### C311 — u/altdotboy

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpcnjaef8k/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpcnjaef8k/)

- **Faithful contribution:** Reports tests on a 128GB M5 comparing Qwen 27B BF16, Q8 and Q4; says quantized versions failed demanding reasoning tests and Q8 used about 50% more thinking than BF16, while BF16 did not overthink. Calls BF16 the best local model among several tried and recommends full precision for precise work and Qwen Code as a harness.
- **Type:** precision comparison and recommendation
- **Why relevant (assessment):** Strongly relevant precision/loop hypothesis, with a claimed within-model comparison but no shared tests.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What prompts, sample counts, seeds, runtime and identical sampling were used?; Do results generalize beyond the commenter’s demanding tests?
- **Transferability (inference):** A single unreplicated Apple setup does not establish that all quantization causes looping or that quantized models cannot do precise coding.
- **Themes:** weights, reasoning, hardware, harness, alternatives, methodology

<a id="c312"></a>

### C312 — u/lazyfai

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpe6psnesg/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpe6psnesg/)

- **Faithful contribution:** Reports daily team use across two machines: vLLM Qwen 3.8 27B FP8 on dual L20, and Strata for Swift 1.5 on a single 5090D. Finds Pi, Prime agent and OpenCode Codex useful, while DeepSeek Harness and Claude Code sometimes overthink; suspects harnesses more than the model.
- **Type:** team deployment and harness comparison
- **Why relevant (assessment):** Specific positive deployment with clear contrary harness preferences.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Which tasks and controlled settings distinguish the harness results?; Which model/runtime combination produced each reported outcome?
- **Transferability (inference):** Different accelerators and mixed model variants limit transfer; a harness explanation is the commenter’s inference, not isolated causality.
- **Themes:** runtime, harness, hardware, weights, reasoning, alternatives, methodology

<a id="c313"></a>

### C313 — u/No-Consideration5347

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpoo6es49v/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpoo6es49v/)

- **Faithful contribution:** Recommends Strata for ease of setup and describes llama.cpp as more stable but slower; suggests IQ3_S/XS Qwen Next with Strata or Q4 Qwen 3.8 with llama.cpp and warns that higher-precision quant formats demand more resources.
- **Type:** runtime and quant recommendation
- **Why relevant (assessment):** Relevant practical alternative to high-precision-only advice, without first-person measurements.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which hardware, workload, versions and context substantiate the speed/stability comparison?
- **Transferability (inference):** Recommended formats are candidate experiments, not demonstrated fixes for the OP’s loops or hardware.
- **Themes:** runtime, weights, alternatives, hardware

<a id="c314"></a>

### C314 — u/Snoo_81913

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpwjyh950h/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpwjyh950h/)

- **Faithful contribution:** Says reasoning is configuration-sensitive and may loop; describes maintaining test prompts and having Claude poll runs, vary one flag at a time, save results, then test combinations. Claims different cards can give different outcomes.
- **Type:** configuration-testing workflow
- **Why relevant (assessment):** Concrete evaluation procedure, though no flags or results are disclosed.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** Which flags, prompts, success criteria and saved results identify a working configuration?; Are apparent card differences confounded by runtime or numerical settings?
- **Transferability (inference):** The one-variable-at-a-time procedure is transferable; the asserted hardware dependency needs verification and held-out prompts.
- **Themes:** methodology, reasoning, runtime, sampling, hardware, workflow

<a id="c315"></a>

### C315 — u/word_executable

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpx40tn2qq/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpx40tn2qq/)

- **Faithful contribution:** Argues Sonnet 5.5 is far ahead of Qwen 27B and local/open-source AI capability is overhyped.
- **Type:** capability dissent
- **Why relevant (assessment):** Retained substantive negative judgment about expectations despite no supporting setup.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which tasks and configurations substantiate the claimed gap?
- **Transferability (inference):** Does not distinguish an intrinsic model limit from this deployment’s configuration problems.
- **Themes:** alternatives, methodology

<a id="c316"></a>

### C316 — u/ContraryConman

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwqbh2xzkbo/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwqbh2xzkbo/)

- **Faithful contribution:** Claims every Claude 5.5 family model will outperform a quantized Qwen 3.8 27B because Claude models are distills from an internal teacher allegedly two generations ahead.
- **Type:** capability and provenance assertion
- **Why relevant (assessment):** Relevant dissent, but both model ranking and private teacher provenance are unsupported.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** What public evidence supports the alleged teacher lineage or two-generation gap?; Which coding tests support the universal comparison?
- **Transferability (inference):** Do not treat speculative internal training details or all-task superiority as established facts.
- **Themes:** alternatives, weights, knowledge, methodology

<a id="c317"></a>

### C317 — u/Vassallo97

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwq5cxsn25e/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwq5cxsn25e/)

- **Faithful contribution:** Reports good Qwen performance in DeepSeek Harness and a self-built coding assistant tailored to Qwen tool calls; says the custom assistant works for short tasks but DeepSeek remains the preferred harness.
- **Type:** harness experience
- **Why relevant (assessment):** Relevant counterexample to C312’s negative DeepSeek Harness experience.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What tool-call adaptations, model settings and tasks explain the benefit?
- **Transferability (inference):** Supports testing tool compatibility but not a universally best harness; runtime and hardware are unspecified.
- **Themes:** harness, workflow, methodology

<a id="c318"></a>

### C318 — u/MoneroApe

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwq7j32s5ut/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwq7j32s5ut/)

- **Faithful contribution:** Attributes the OP’s problems to poor quants/cache and recommends Linux HyperQwen, described as 3090-tuned, followed by Strata Coder for coding.
- **Type:** runtime and cache recommendation
- **Why relevant (assessment):** Directly actionable candidate paths, but diagnoses and performance improvement are asserted without measurements.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** What exact weight and cache formats are considered poor in the OP setup?; Which HyperQwen/Strata versions and memory requirements apply?
- **Transferability (inference):** Repository suitability and improvement were not verified; specificity of a GPU target is not evidence of correctness.
- **Themes:** runtime, weights, kv, hardware, alternatives

<a id="c319"></a>

### C319 — u/No-Recover109

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwqgpkh5rc3/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwqgpkh5rc3/)

- **Faithful contribution:** Reports Qwen 27B FP8 coding well under vLLM, which felt too heavy, then switching successfully to Strata with a Q3 Istalabs DeepSeek V4.1 1017. Questions whether the OP can fit Qwen/context at adequate precision and recommends matching context settings between inference engine and agent.
- **Type:** runtime/model experience and diagnostic advice
- **Why relevant (assessment):** Useful context-alignment check plus a positive FP8 report; the suggested precision failure is conjectural.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What are the OP’s actual quant and server/client context limits?; What does “too heavy” mean for the reported vLLM deployment?
- **Transferability (inference):** Changing model and runtime together cannot isolate a runtime effect; context agreement is a check, not proof of model quality.
- **Themes:** runtime, weights, context, harness, alternatives, hardware

<a id="c320"></a>

### C320 — u/Key_River_9288

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwqoyl897l0/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwqoyl897l0/)

- **Faithful contribution:** Recommends adding RAM and using Strata with Qwen 3.8 Flash Next at quant 5.
- **Type:** alternative and hardware recommendation
- **Why relevant (assessment):** Substantive but minimal recommendation without a demonstrated setup.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** How much RAM and what exact Q5 artifact/context are needed?
- **Transferability (inference):** A different MoE model may suit offloading, but no measured fit or coding reliability is given.
- **Themes:** alternatives, runtime, weights, hardware

<a id="c321"></a>

### C321 — u/Tight_Ad_5220

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwqrwpbpyn8/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwqrwpbpyn8/)

- **Faithful contribution:** Diagnoses excessive prefill and recommends inspecting Claude’s /context output, removing existing material and comparing results.
- **Type:** context-reduction experiment
- **Why relevant (assessment):** Relevant hypothesis about inherited instructions and prompt load; causality is unproven.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** How large is the actual initial prompt and which content is necessary?; Does a reduced-context run improve correctness under unchanged settings?
- **Transferability (inference):** A minimal-context baseline can test this claim; it does not establish that all project documentation should be discarded.
- **Themes:** context, harness, methodology

<a id="c322"></a>

### C322 — u/nincius

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwqtkorfvz9/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwqtkorfvz9/)

- **Faithful contribution:** Links club-3090 tuning guidance and reports better results on the same stated hardware after disabling reasoning entirely.
- **Type:** hardware-matched reasoning experience
- **Why relevant (assessment):** Potentially close hardware counterexample to recommendations that thinking is essential.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Which quant, runtime, tasks and before/after measurements were used?; Did disabling reasoning preserve correctness on harder tasks?
- **Transferability (inference):** Hardware match is promising but insufficient without configuration parity; linked guidance was not read.
- **Themes:** reasoning, hardware, runtime, methodology

<a id="c323"></a>

### C323 — u/Dediadeis

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwqvy3np5ep/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwqvy3np5ep/)

- **Faithful contribution:** Reports using 27B and Qwen Flash Next in a legacy-like codebase with Cline in a sandboxed code-server container. Recommends prioritizing quality over speed, approximately 64GB VRAM/64GB RAM, Q8 weights, KV at least Q8 preferably full precision, and 262k context; suggests QFN Q4/KV8_4 and cloud-assisted tuning. Says well-configured models can handle multi-hour tasks.
- **Type:** legacy-code deployment and configuration recommendation
- **Why relevant (assessment):** Directly relevant positive legacy-work report, alongside unvalidated precision/capacity prescriptions.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What exact model/runtime/KV8_4 format, tasks and completion criteria support the multi-hour claim?; Which recommendations are measured requirements versus personal preferences?
- **Transferability (inference):** Much larger recommended memory differs from the OP; the minimum-precision and context prescriptions conflict with successful lower-resource reports.
- **Themes:** weights, kv, context, hardware, harness, workflow, alternatives, methodology

<a id="c324"></a>

### C324 — u/isademigod

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwr4si9r06c/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwr4si9r06c/)

- **Faithful contribution:** Reports frequent use for regex and PowerShell scripts as a sysadmin/datahoarder rather than developer; judges it adequate for those tasks but the context window too small for an entire program.
- **Type:** bounded-task experience
- **Why relevant (assessment):** Useful narrow success case that does not claim autonomous repository development.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** What model settings, script complexity and validation procedures are used?
- **Transferability (inference):** Simple-script success does not settle large-codebase capability; a program’s context needs depend on selective retrieval and workflow.
- **Themes:** workflow, context, methodology

<a id="c325"></a>

### C325 — u/ParticularlyStrange

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwr6gc375ib/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwr6gc375ib/)

- **Faithful contribution:** Asks which quant the OP uses and recommends EXL3 or NVFP4 formats.
- **Type:** quantization question and recommendation
- **Why relevant (assessment):** Relevant missing diagnostic detail; format preference has no supporting comparison.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** What quant is the OP running?; Are the proposed formats supported efficiently on the OP GPU/runtime, and with what artifact quality?
- **Transferability (inference):** Format names alone do not guarantee fit, backend compatibility or a coding-quality improvement.
- **Themes:** weights, runtime, hardware

<a id="c326"></a>

### C326 — u/exzw

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwr94ofgnmt/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwr94ofgnmt/)

- **Faithful contribution:** Says the hardware purchase was inadequate and recommends at least 128GB DDR5 plus an R9700 or RTX Pro 4500, then 27B at Q6 or higher or Strata/QFN Q4. Reports using QFN as coder with Opus as auditor and sometimes feeling QFN outperforms Opus 5.
- **Type:** hardware prescription and hybrid experience
- **Why relevant (assessment):** Relevant hardware/alternative dissent, but the claimed requirements and superiority lack a reproduced test.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** What exact hardware, quant, tasks and audit corrections support the comparison?; Are the proposed purchases necessary for the OP’s bounded tasks?
- **Transferability (inference):** A subjective QFN comparison under Opus review does not establish standalone superiority or universal hardware minimums.
- **Themes:** hardware, weights, alternatives, workflow, methodology

<a id="c327"></a>

### C327 — u/Sea_Advance273

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwrhl8ia200/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwrhl8ia200/)

- **Faithful contribution:** Reports being impressed by Qwen Q4 in 24GB VRAM using Claude Code, while needing more iteration and involvement than Opus 5.5.
- **Type:** hardware/quant/harness experience
- **Why relevant (assessment):** Directly challenges claims that Q4/24GB or Claude Code cannot be useful.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Which runtime, cache precision, context and tasks produced the result?
- **Transferability (inference):** Useful close-capacity anecdote, but more human iteration and unspecified workload limit comparison with autonomous cloud coding.
- **Themes:** weights, hardware, harness, workflow, alternatives

<a id="c328"></a>

### C328 — u/Promotional_Pickle

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwri0l42dut/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwri0l42dut/)

- **Faithful contribution:** Reports excellent local results and emphasizes harnesses, notes and infrastructure as the distinction between a toy and a useful tool.
- **Type:** infrastructure experience
- **Why relevant (assessment):** Relevant positive experience but too vague to reproduce.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** Which infrastructure, model settings, tasks and outcome checks were used?
- **Transferability (inference):** Supports an infrastructure hypothesis, not evidence that the OP’s model is otherwise capable on every task.
- **Themes:** harness, workflow, methodology

<a id="c329"></a>

### C329 — u/dahc_

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwrljnbmkyr/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwrljnbmkyr/)

- **Faithful contribution:** Reports poor results with the same model setup across Pi, Claude and Hermes on a Ryzen 5600X/RTX 3090. Says Qwen 3.6 35B A3B IQ4-XS with OpenCode instead refactors, fixes bugs and adds features effectively, while context/memory setup is still being improved.
- **Type:** near-hardware negative experience and alternative
- **Why relevant (assessment):** Important counterexample to blanket configuration optimism and a specific alternative on similar hardware.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What exact failed 27B quant, context and runtime were shared across the harnesses?; How were alternative outcomes verified and did other settings change?
- **Transferability (inference):** Close GPU match increases relevance, but changing model and harness together prevents assigning cause; setup is not finalized.
- **Themes:** hardware, weights, harness, alternatives, context, methodology

<a id="c330"></a>

### C330 — u/Current_Ad5753

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwrt267zvs1/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwrt267zvs1/)

- **Faithful contribution:** Asks the OP to identify any harness used over the local LLM.
- **Type:** diagnostic question
- **Why relevant (assessment):** Preserves a material missing deployment detail.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which harness is actually being used for the failing runs?
- **Transferability (inference):** A necessary contextual question, not evidence that a harness change fixes the failure.
- **Themes:** harness, methodology

<a id="c331"></a>

### C331 — u/endockhq

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rws0t23mqhx/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rws0t23mqhx/)

- **Faithful contribution:** Recommends vLLM, Qwen3.8-Flash-Next-FP8 and Claude Code with an Anthropic Messages API-compatible inference engine; calls 27B too slow and inadequate for proper software-house work.
- **Type:** runtime/model/harness recommendation
- **Why relevant (assessment):** Contains actionable integration advice despite dismissive language and unsupported quality judgments.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Will Flash Next FP8 and vLLM fit the OP hardware/RAM?; Which server actually supports the required API and tool semantics?
- **Transferability (inference):** Different model memory demands and API compatibility need checking; the recommendation is not a measured 3090 solution.
- **Themes:** runtime, alternatives, weights, harness, hardware

<a id="c333"></a>

### C333 — u/ContraryConman

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwsal0il483/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwsal0il483/)

- **Faithful contribution:** Reports Pi with a goal-mode plugin as necessary in the commenter’s workflow to keep 27B/128K on task through thinking-heavy compaction. Describes about 25 tokens/s and over an hour, with steering away from dead ends, for a complex CMake setup that the commenter estimates Claude would finish in 2–5 minutes; uses it for unattended tedious work, not interactive or parallel agents.
- **Type:** task-specific workflow experience
- **Why relevant (assessment):** Rich bounded success with explicit intervention, latency and comparison limits.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What hardware, quant and task transcript establish completion and intervention frequency?; Is the estimated Claude timing measured on the same task?
- **Transferability (inference):** A completed background task is not equivalent to fast autonomous cloud work; goal persistence may transfer as a workflow idea, not a universal requirement.
- **Themes:** harness, context, reasoning, workflow, hardware, alternatives, methodology

<a id="c334"></a>

### C334 — u/MonadicKierkegaard

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwsavw1x5et/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwsavw1x5et/)

- **Faithful contribution:** Asks whether the machine is per-developer or team-wide; says 32GB barely supports one agent and proposes cloud-generated detailed pseudocode/specifications followed by a fitting MoE, claiming up to 2k tokens/s prompt processing and 70 tokens/s generation at reduced intelligence.
- **Type:** capacity question and hybrid recommendation
- **Why relevant (assessment):** Relevant concurrency and team-capacity concern with unsupported performance ceilings.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Is the machine shared by a team or dedicated to one developer?; Which MoE, quant, context and hardware achieve the quoted prompt/generation rates?
- **Transferability (inference):** Concurrency capacity depends on memory and serving details; proposed numbers and intelligence tradeoff are not established for this system.
- **Themes:** hardware, context, workflow, alternatives, economics

<a id="c335"></a>

### C335 — u/Osi32

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwsbtb19qci/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwsbtb19qci/)

- **Faithful contribution:** Warns that preloaded skills consume context, considers a 3090 suitable only for limited single-developer tasks, and attributes Flash Next use to Strata offloading to RAM/disk. Recommends Qwen3.6-35B-A3B for coding and 27B for planning.
- **Type:** context/hardware analysis and model split
- **Why relevant (assessment):** Relevant prompt-budget and role-allocation hypotheses, but categorical memory/offload claims lack measurements.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** How much context do actual loaded skills consume?; What model/cache allocation and offload policy apply on the OP runtime?
- **Transferability (inference):** Skill size is not inherently close to 128K, and dense-model offloading feasibility is a matter to measure rather than an absolute prohibition.
- **Themes:** context, hardware, runtime, alternatives, workflow

<a id="c336"></a>

### C336 — u/247nuts

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwsyut1nan9/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwsyut1nan9/)

- **Faithful contribution:** Recommends Qwen 27B for instructions and a Qwen Coder model for coding.
- **Type:** model-role recommendation
- **Why relevant (assessment):** Substantive role split, but unspecified coder version and no evidence.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which coder model and configuration are intended, and how do they compare on the same tasks?
- **Transferability (inference):** Model-role labeling alone does not establish superior coding performance or feasible memory use.
- **Themes:** alternatives, workflow

<a id="c337"></a>

### C337 — u/jikilan_

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwu5nheaxlw/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwu5nheaxlw/)

- **Faithful contribution:** Recommends at least two, preferably four, 3090s with vLLM before judging 27B, while saying the model is not a cloud replacement and likening it to a junior developer.
- **Type:** hardware prescription and expectation-setting
- **Why relevant (assessment):** Retained technical prescription despite a joking metaphor; no supporting measurement.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which quant, context, batch size or concurrency requires two to four cards?
- **Transferability (inference):** The GPU count is a commenter preference, not a demonstrated minimum for useful single-agent coding.
- **Themes:** hardware, runtime, workflow, alternatives

<a id="c338"></a>

### C338 — u/Demonicated

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwu99aiudnp/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwu99aiudnp/)

- **Faithful contribution:** Insists on at least Q8, ideally BF16, and argues Q4 criticism is unsurprising. Recommends precise instructions, a planning phase, implementation documents aimed at a junior developer, then executing that plan despite slow reasoning.
- **Type:** precision prescription and planning workflow
- **Why relevant (assessment):** Relevant workflow proposal coupled to a universal quantization claim contradicted by other reports.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** What comparison establishes the claimed Q8 minimum?; How should planning quality, implementation correctness and reasoning time be measured?
- **Transferability (inference):** Planning and explicit scope are testable workflow changes; neither their success nor a precision floor is established universally.
- **Themes:** weights, reasoning, workflow, methodology

<a id="c339"></a>

### C339 — u/xsilas43

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwub6ix1291/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwub6ix1291/)

- **Faithful contribution:** Reports Qwen AgentWorld producing simpler effective code faster in one shot than 3.8 27B, though the latter eventually gave better visuals. Recommends Unsloth Desktop over Ollama for customization and headless reuse, plus sharp chat templates.
- **Type:** alternative comparison and template recommendation
- **Why relevant (assessment):** One of the range’s explicit template suggestions and a task-level comparative anecdote.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Which AgentWorld artifact, sharp template, runtime settings and task were compared?; Did visual quality and functional correctness receive separate checks?
- **Transferability (inference):** Changing model, runtime and template can confound attribution; no template was inspected or validated.
- **Themes:** alternatives, runtime, template, harness, methodology

<a id="c340"></a>

### C340 — u/ImpossibleNumber7345

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwudho2cyar/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwudho2cyar/)

- **Faithful contribution:** Recommends Swift, described as Qwen fine-tuned by penalizing excessive thinking, and claims it keeps the same intelligence while completing work.
- **Type:** reasoning-tuned alternative recommendation
- **Why relevant (assessment):** Directly addresses looping/latency, but training description and equal-intelligence claim are unsupported.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which Swift version, quant and evaluation support preserved capability with shorter reasoning?
- **Transferability (inference):** A fine-tune is a different artifact; reduced thinking may change task success as well as speed.
- **Themes:** alternatives, reasoning, weights, methodology

<a id="c341"></a>

### C341 — u/c4chokes

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwuf5yhvsf7/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwuf5yhvsf7/)

- **Faithful contribution:** Suggests using Sonnet to debug the local setup.
- **Type:** cloud-assisted troubleshooting suggestion
- **Why relevant (assessment):** Minimal but substantive diagnostic workflow proposal.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** What configuration/logs should Sonnet inspect, and how will suggested changes be validated?
- **Transferability (inference):** Cloud assistance can structure diagnosis but does not independently verify the resulting advice.
- **Themes:** workflow, methodology, alternatives

<a id="c342"></a>

### C342 — u/thebemusedmuse

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwuvcygqftv/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwuvcygqftv/)

- **Faithful contribution:** Reports Qwen as the primary coding agent generating about six million output tokens daily, with harness checks and balances to repair introduced bugs; warns that overly large assignments may be incomplete and must be right-sized.
- **Type:** high-volume workflow experience
- **Why relevant (assessment):** Relevant success claim that explicitly includes repair mechanisms and bounded task sizing.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** What model, hardware, runtime and token-accounting method support the volume?; What fraction of tasks succeed, and which checks/human interventions repair bugs?
- **Transferability (inference):** Output volume is not task correctness or productivity; the unspecified harness is central to the claimed outcome.
- **Themes:** harness, workflow, methodology

<a id="c343"></a>

### C343 — u/TheRiddler79

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwvcvxsdbc4/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwvcvxsdbc4/)

- **Faithful contribution:** Proposes having Claude write Qwen’s instructions, enabling thinking, and having Claude check the output.
- **Type:** hybrid orchestration recommendation
- **Why relevant (assessment):** Relevant division of labor and reasoning preference, without first-person results.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** How much of the final result and cost depends on Claude’s instructions and corrections?
- **Transferability (inference):** A cloud-supervised workflow is not evidence of autonomous local capability; thinking preference conflicts with disabling advice elsewhere.
- **Themes:** workflow, reasoning, alternatives, economics

<a id="c345"></a>

### C345 — u/jabies

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwvw3d0t09t/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwvw3d0t09t/)

- **Faithful contribution:** Notes missing chat-versus-completions API, prompt template, quantization, temperature and sampler details and recommends identifying them first.
- **Type:** diagnostic checklist
- **Why relevant (assessment):** Important missing-variable inventory for reproducing a failure.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which API mode, prompt template, weight quant, temperature and sampler settings were used?
- **Transferability (inference):** These are reproducibility requirements and possible failure sources, not evidence any single one is currently wrong.
- **Themes:** runtime, template, weights, sampling, methodology

<a id="c346"></a>

### C346 — u/mrepop

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwvyierx50g/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwvyierx50g/)

- **Faithful contribution:** Attributes failures to xhigh thinking, recommends low or disabled thinking and token-reuse penalties, and links supporting discussions. Reports using 27B across multiple hardware platforms and says looping is common; calls the OP hardware barely adequate for larger contexts and suggests Flash for offloading.
- **Type:** reasoning-configuration advice and broad experience
- **Why relevant (assessment):** Directly relevant loop hypothesis, with multiple suggested interventions but no exact settings or results.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** Does the OP actually use xhigh and does the backend implement that control?; Which penalty values and controlled comparisons reduce loops without harming coding accuracy?
- **Transferability (inference):** Widespread-use and universal-issue claims are not measured prevalence; linked material was not accessed and named reasoning levels may be harness-specific.
- **Themes:** reasoning, sampling, hardware, context, alternatives, runtime, methodology

<a id="c347"></a>

### C347 — u/Past_Ad6251

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rww5ghf7usi/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rww5ghf7usi/)

- **Faithful contribution:** Reports Qwen3.8-27B with llama.cpp on 24GB VRAM/64GB RAM at 200k context with multimodal support completing over 85% of personal tasks, including medium-complexity coding. Uses DeepSeek Harness and Hermes, reserving paid tokens for complex or time-consuming tasks.
- **Type:** capacity-matched deployment experience
- **Why relevant (assessment):** Specific positive counterexample retained despite an opening personal jab; task success percentage is self-reported.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Which quant/cache settings fit 200k context, and how much is offloaded?; What denominator, task selection and validation define over 85% success?
- **Transferability (inference):** More RAM than the OP and unspecified success accounting limit transfer; selected paid fallback is part of the workflow.
- **Themes:** runtime, hardware, context, harness, workflow, alternatives, methodology

<a id="c348"></a>

### C348 — u/fobsthedev

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rww81p6k3vm/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rww81p6k3vm/)

- **Faithful contribution:** Recommends Swift 1.5 and avoiding any quant below 8 bits.
- **Type:** alternative and precision recommendation
- **Why relevant (assessment):** Relevant but unsupported variant/quant prescription.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which artifact, hardware and tasks establish the proposed 8-bit floor?
- **Transferability (inference):** Conflicts with positive Q4/NVFP4 anecdotes; no universal precision requirement follows.
- **Themes:** alternatives, weights

<a id="c349"></a>

### C349 — u/lordpuddingcup

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwwrva3bhyd/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwwrva3bhyd/)

- **Faithful contribution:** Claims coding requires at least 256k context, higher-quality quants and maximum reasoning, which also consumes context.
- **Type:** context and reasoning prescription
- **Why relevant (assessment):** Substantive strong dissent from context-minimization and low/no-thinking advice.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** What tasks demonstrate that 128k or lower reasoning cannot be useful?; Does maximum reasoning increase correctness enough to offset loops and latency?
- **Transferability (inference):** A universal 256k minimum or maximum-effort requirement is unvalidated and contradicted by bounded-task reports.
- **Themes:** context, reasoning, weights, methodology

<a id="c350"></a>

### C350 — u/Sad_Olive3034

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwwslb38bdv/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwwslb38bdv/)

- **Faithful contribution:** Reports slowly trying to make a coding AI work on an Intel Arc Pro B60 with Claude and GPT helping, and argues these models need staged guidance and training-like treatment.
- **Type:** hardware-specific struggle and hybrid workflow
- **Why relevant (assessment):** Relevant negative experience, though the exact local model and concrete failures are absent.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Which local model, runtime and tasks are failing or improving?; Does “training” mean prompting, memory, fine-tuning or manual iteration?
- **Transferability (inference):** Different Intel hardware and unspecified model are not direct evidence about Qwen 27B on a 3090; the developmental metaphor is not a technical method.
- **Themes:** hardware, workflow, alternatives, methodology

<a id="c351"></a>

### C351 — u/MatthewBochsler

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwx3bzdmnqb/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwx3bzdmnqb/)

- **Faithful contribution:** Reports little success with Qwen models and says a heavily controlled harness plus community-specific configuration guidance is the remaining approach being tested before switching. Recommends searching GitHub for control tips.
- **Type:** negative experience and ongoing test
- **Why relevant (assessment):** Retained substantive unsuccessful experience; proposed mitigation has not yet succeeded.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** Which Qwen models, tasks and settings failed?; Does the controlled harness improve outcomes, and by what measure?
- **Transferability (inference):** An unfinished test is not evidence that harness control resolves the problem or that every Qwen variant fails.
- **Themes:** harness, workflow, methodology

<a id="c354"></a>

### C354 — u/bazuchan

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwxslkgb7hh/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwxslkgb7hh/)

- **Faithful contribution:** Recommends Claude Code or Pi, testable task instructions, and a Swift 27B variant for less reasoning; asserts dense weights should be Q8 (Q6 might work) and KV keys at least Q8, implying another 3090 is needed.
- **Type:** harness/precision/testing recommendation
- **Why relevant (assessment):** Useful testability advice mixed with unsupported hardware and precision minimums.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** What controlled tasks show the stated Q6/Q8 differences and KV minimum?; Is a second GPU required after measuring the actual context/KV allocation?
- **Transferability (inference):** Testable acceptance criteria can transfer; particular precision and hardware requirements must be validated against the desired workload.
- **Themes:** harness, workflow, methodology, weights, kv, hardware, alternatives, reasoning

<a id="c355"></a>

### C355 — u/0xnobot

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwy3v1toq01/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwy3v1toq01/)

- **Faithful contribution:** In Spanish, recommends llama.cpp, the LLM profile configuration, and a good harness.
- **Type:** runtime/configuration recommendation
- **Why relevant (assessment):** Minimal substantive configuration advice; no actual profile values or outcomes.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which LLM profile settings and harness are intended?
- **Transferability (inference):** Insufficient detail to reproduce or infer benefit on the OP setup.
- **Themes:** runtime, harness, methodology

<a id="c356"></a>

### C356 — u/thilog

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwzkug6ftt0/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwzkug6ftt0/)

- **Faithful contribution:** Asks which harness is recommended.
- **Type:** harness question
- **Why relevant (assessment):** Retains an explicit practical question not resolved by a specific reply in this assigned range.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which harness is recommended, for what workload and deployment?
- **Transferability (inference):** Other comments list conflicting preferences; the question itself supplies no effectiveness evidence.
- **Themes:** harness

<a id="c357"></a>

### C357 — u/mattjouff

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwy7vusj6ar/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwy7vusj6ar/)

- **Faithful contribution:** Argues local AI economics become unattractive when a 27B model is compared with an allegedly 2000B flagship, claiming adequate capability ultimately leads back to hourly GPU rental.
- **Type:** economic dissent
- **Why relevant (assessment):** Relevant cost/practicality critique despite sarcasm; commercial parameter count and inevitability are unsupported.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** What ownership, power, engineering-time and hosted/rental costs are being compared?; What evidence supports the claimed flagship parameter count?
- **Transferability (inference):** An unpriced economic assertion cannot establish that renting always wins or that local bounded tasks are uneconomic.
- **Themes:** economics, alternatives, hardware, methodology

<a id="c358"></a>

### C358 — u/Frosty-Bid-8735

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwyd8p5tuw1/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwyd8p5tuw1/)

- **Faithful contribution:** Recommends against Qwen 3.8 for coding and instead proposes classification, summarization and limited-context RAG.
- **Type:** capability dissent and task-role recommendation
- **Why relevant (assessment):** Substantive negative recommendation with no setup or examples.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which Qwen variant, coding tasks and configurations support the coding limitation?
- **Transferability (inference):** Does not negate concrete positive coding anecdotes, nor demonstrate that the proposed noncoding roles are validated.
- **Themes:** workflow, alternatives, context, methodology

<a id="c359"></a>

### C359 — u/maxido

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwymu7uybvn/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwymu7uybvn/)

- **Faithful contribution:** Reports deploying Qwen3.8 27B for a company with good results and suspects a configuration issue in the OP case.
- **Type:** organizational deployment experience
- **Why relevant (assessment):** Positive company-use claim, but no deployment details or failure analysis.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** What hardware, runtime, quant, harness and work types are deployed?; What specifically indicates misconfiguration in the OP run?
- **Transferability (inference):** Organizational use is not a reproducible comparison; configuration diagnosis remains an inference.
- **Themes:** workflow, runtime, methodology

<a id="c360"></a>

### C360 — u/Sufficient-Rock-8482

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwz4wyafl41/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwz4wyafl41/)

- **Faithful contribution:** Recommends Unsloth Q4_K_M under “vllm.cpp,” described as a llama/vLLM hybrid, plus a small OpenCode Go plan with DeepSeek 4.1 orchestrating and Qwen implementing. Claims proper configuration can scale for agents.
- **Type:** runtime recommendation and hybrid orchestration
- **Why relevant (assessment):** Relevant lower-precision proposal, but runtime identity and scaling claims require verification.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** What exact project/build is meant by vllm.cpp, and does it support this model/format?; How are orchestration, implementation and validation divided and priced?
- **Transferability (inference):** Do not silently reinterpret the named runtime; this is an unverified multi-model recommendation, not standalone local success.
- **Themes:** runtime, weights, workflow, alternatives, economics, methodology

<a id="c361"></a>

### C361 — u/bytejuggler

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx02kua8asl/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx02kua8asl/)

- **Faithful contribution:** Attributes the reported issues to 27B itself and recommends the larger Qwen Flash Next 3.8 125/180B-class model under Strata, claiming no loops, 3–4 times faster prefill and substantially faster processing.
- **Type:** alternative and performance assertion
- **Why relevant (assessment):** Relevant counterproposal against harness-only explanations; quantitative speed comparison is unsupported.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** What exact Flash Next artifact, quant, hardware and baseline produce the claimed speedup?; Does it fit the OP’s 32GB RAM and chosen context?
- **Transferability (inference):** A larger sparse model under another runtime is not a controlled 27B comparison; no-loop guarantees are unvalidated.
- **Themes:** alternatives, runtime, hardware, reasoning, methodology

<a id="c362"></a>

### C362 — u/Mission-Shopping-615

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx0c5ucv0yt/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx0c5ucv0yt/)

- **Faithful contribution:** Suggests asking Claude to optimize the setup and assess hardware adequacy.
- **Type:** cloud-assisted troubleshooting suggestion
- **Why relevant (assessment):** Substantive but minimal diagnostic workflow recommendation.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which measurements will be supplied and how will advice be validated?
- **Transferability (inference):** A model-generated hardware assessment is not independent verification of fit or reliability.
- **Themes:** workflow, hardware, alternatives, methodology

<a id="c363"></a>

### C363 — u/dfgxxx

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx0chzybnoh/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx0chzybnoh/)

- **Faithful contribution:** Calls Claude Code token-inefficient because of large system prompts and recommends a different harness such as DeepSeek Harness for local models.
- **Type:** harness/context recommendation
- **Why relevant (assessment):** Relevant explanation for prompt overhead, conflicting with positive Claude Code reports.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** How large is the actual system prompt and does it differ under the compared harnesses?; Do identical model/settings runs show better task outcomes with DeepSeek Harness?
- **Transferability (inference):** Prompt overhead may matter without proving Claude Code is generally bad; no controlled comparison is provided.
- **Themes:** harness, context, methodology

<a id="c364"></a>

### C364 — u/dlbogdan

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx0lmssnvdw/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx0lmssnvdw/)

- **Faithful contribution:** Reports Qwen 3.8 Flash Next working quickly for every attempted coding task without loops on an RTX 3090, 128GB RAM and a 16-core/32-thread CPU.
- **Type:** alternative-model hardware experience
- **Why relevant (assessment):** Specific positive offload-capable setup with four times the OP RAM.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What Strata/runtime, quant, context, speeds and task set were used?; What tests confirm each coding task’s correctness?
- **Transferability (inference):** Uses Flash Next rather than dense 27B and substantially more RAM; “every task” is limited to the commenter’s selection. CPU identity is corrected in C366.
- **Themes:** alternatives, hardware, runtime, reasoning, methodology

<a id="c365"></a>

### C365 — u/colonelx_

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2so82h95u/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2so82h95u/)

- **Faithful contribution:** Asks whether the preceding apparently 32-core CPU is an EPYC.
- **Type:** hardware clarification question
- **Why relevant (assessment):** Preserves the actual hardware-identification question and distinguishes cores from threads.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Was the CPU 32-core and an EPYC? Answered/corrected within this range by C366: Ryzen 9 5950X, 16 cores/32 threads.
- **Transferability (inference):** The question is not a separate performance result; use the corrected configuration rather than infer EPYC hardware.
- **Themes:** hardware, methodology

<a id="c366"></a>

### C366 — u/dlbogdan

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx33ezihz8l/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx33ezihz8l/)

- **Faithful contribution:** Corrects the earlier CPU description to Ryzen 9 5950X with 16 cores and 32 threads.
- **Type:** hardware correction
- **Why relevant (assessment):** Necessary substantive correction to the C364 deployment context.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** The core/thread question in C365 is answered; runtime/quant and task-validation details remain absent from the performance report.
- **Transferability (inference):** Configuration clarification only; it adds no independent model-quality measurement.
- **Themes:** hardware, methodology

<a id="c367"></a>

### C367 — u/ifeelprettyosopretty

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx0nlqelz1f/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx0nlqelz1f/)

- **Faithful contribution:** Reports a roughly $20,000 system running Qwen Flash Next 177B at 8 bits, with 55GB described as lookup, at about 77 tokens/s and good complex-task results. Argues heavily quantized 27B accumulates errors over long multi-turn work and says occasional 27B use is backed by Codex/Claude task refinement.
- **Type:** expensive deployment and quantization critique
- **Why relevant (assessment):** Specific cost/variant/rate anecdote showing claimed quality with substantial hardware and cloud assistance.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What hardware, runtime, context and benchmark yield 77 tokens/s?; What does the 55GB lookup figure mean and what matched tests isolate 27B quantization effects?
- **Transferability (inference):** A costly different model does not establish the minimum useful 27B setup; general long-turn precision conclusions exceed the provided evidence.
- **Themes:** hardware, economics, weights, alternatives, workflow, context, methodology

<a id="c368"></a>

### C368 — u/aCuria

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx0uvafuqw1/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx0uvafuqw1/)

- **Faithful contribution:** Recommends a dedicated inference machine so development can proceed in parallel; says context feels small on a 5090, speculates dual 3090s may be better, places model intelligence near Haiku 5.5 low effort, and recommends Opus over Sonnet while claiming equal cost.
- **Type:** deployment advice and capability/pricing comparison
- **Why relevant (assessment):** Relevant separation/concurrency idea, but model ranking, dual-GPU benefit and pricing are unverified.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** Which model/quant/context makes the 5090 feel limited?; What evidence supports equal pricing and the Haiku capability comparison?
- **Transferability (inference):** Capacity, interconnect and serving configuration determine dual-GPU benefit; price and capability assertions should not be treated as facts.
- **Themes:** hardware, context, workflow, alternatives, economics

<a id="c369"></a>

### C369 — u/Hrmerder

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx0vc95128w/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx0vc95128w/)

- **Faithful contribution:** Reports Qwen 3.6 35B A3B coding poorly in LM Studio but becoming useful for vibe coding after moving to Strata, with less argument over corrections.
- **Type:** runtime-change experience on another model
- **Why relevant (assessment):** Relevant runtime hypothesis, but not a Qwen 27B test and no controlled settings are given.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Did quant, template, sampling, harness or prompt history change alongside the runtime?
- **Transferability (inference):** A before/after impression on another MoE model cannot establish a backend-only fix for dense 27B.
- **Themes:** runtime, alternatives, methodology

<a id="c370"></a>

### C370 — u/SeveralCamera292

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx0w4bvfz50/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx0w4bvfz50/)

- **Faithful contribution:** Claims a 3090 is insufficient for work with 27B and at least 32GB VRAM, another 3090, a dedicated inference machine, different model builds and at least 3–4 weeks of tuning are needed. Advises avoiding an immediate uncensored build and contrasts local effort with tuned cloud products.
- **Type:** hardware/tuning prescription
- **Why relevant (assessment):** Substantive deployment-effort dissent; universal minimums and broken-build prevalence are unsupported.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which tasks, quant and context establish the claimed memory and tuning-time minimums?; Which builds are broken, by what reproducible failure?
- **Transferability (inference):** Useful reminder to compare full stacks, but no basis to prescribe purchases or weeks of tuning to every workload.
- **Themes:** hardware, weights, runtime, harness, workflow, economics, methodology

<a id="c371"></a>

### C371 — u/ifeelprettyosopretty

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx0xelhqjl0/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx0xelhqjl0/)

- **Faithful contribution:** Reports that Codex-created DnD campaign tools needed many revisions to work well with the commenter’s 177B model, arguing that detailed workflows created for stronger models may not transfer directly.
- **Type:** artifact/workflow portability experience
- **Why relevant (assessment):** Concrete domain example challenging reuse of cloud-oriented instructions, though it concerns a larger local model.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What revisions, tools and failure modes were required?; Was the issue tool format, missing knowledge, context load or model capability?
- **Transferability (inference):** Another model and DnD workflow do not isolate 27B limitations; instruction/tool portability is a testable hypothesis.
- **Themes:** workflow, harness, knowledge, context, alternatives, methodology

<a id="c372"></a>

### C372 — u/VihmaVillu

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1hvljq3dx/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1hvljq3dx/)

- **Faithful contribution:** Asks the quant, argues local harness work starts behind Claude Code, and reports enjoying Qwen3.8-Flash-Next-IQ3_S with Strata.
- **Type:** configuration question and alternative experience
- **Why relevant (assessment):** Specific low-bit alternative anecdote, without task metrics or hardware.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Which quant is the OP using?; What hardware, tasks, context and validation support the reported Flash Next success?
- **Transferability (inference):** Different model/runtime and missing memory details limit transfer to 27B or the OP hardware.
- **Themes:** harness, weights, alternatives, runtime, methodology

<a id="c373"></a>

### C373 — u/sod0

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1n8ypr9no/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1n8ypr9no/)

- **Faithful contribution:** Reports serving 245k context on a 3090, or 200k optimized for concurrent batch mode, and recommends HyperQwen. Says the model replaces personal Claude use when given planning, research and post-task QA phases, while one-shot attempts perform badly.
- **Type:** hardware/context workflow experience
- **Why relevant (assessment):** Close-GPU positive report that contradicts fixed larger-VRAM prescriptions, with substantial workflow qualification.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Which weights, KV precision, runtime build, RAM and concurrency enable the quoted context?; What tasks and QA interventions establish replacement quality?
- **Transferability (inference):** Context capacity is not occupied-context performance or proof that more context improves accuracy; the phased workflow is inseparable from this reported success.
- **Themes:** hardware, context, runtime, weights, kv, workflow, methodology

<a id="c374"></a>

### C374 — u/never_supernova

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1ojyyyuua/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1ojyyyuua/)

- **Faithful contribution:** Reports good results when frontier models design architecture, break work into phases and small steps, and review Qwen code. Recommends ADRs, implementation plans and AGENTS.md for continuity, and gives an approximate 30-minute Qwen versus 5-minute Claude timing example.
- **Type:** hybrid workflow experience
- **Why relevant (assessment):** Relevant effective-use account with explicit cloud dependence and latency tradeoff.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** Which tasks, settings and review corrections support the timing and success claims?
- **Transferability (inference):** The workflow may transfer, but final quality cannot be assigned solely to Qwen and the timing is an unverified approximation.
- **Themes:** workflow, context, alternatives, economics, methodology

<a id="c375"></a>

### C375 — u/sub-dy

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1olncrhr9/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1olncrhr9/)

- **Faithful contribution:** Argues even Q3 27B can code if given small, clearly defined components rather than architecture and whole-project autonomy. Recommends human-defined interfaces, relevant files, immediate tests/reviews and fixing errors before they accumulate; frames subscription savings as more human planning. Also alleges large size/context ratios versus commercial models.
- **Type:** bounded-task workflow and capability argument
- **Why relevant (assessment):** Substantive counterpoint to high-precision minimums and large-context prescriptions, with no first-person benchmark.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** What task complexity and intervention load make Q3 coding successful?; What evidence supports the claimed commercial/local parameter and context ratios?
- **Transferability (inference):** Task decomposition and immediate verification are general workflow proposals, not proof of Q3 sufficiency for every task or of the asserted commercial model sizes.
- **Themes:** workflow, weights, context, economics, methodology, alternatives

<a id="c376"></a>

### C376 — u/Sea_Shift4327

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1xrpwqt9g/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1xrpwqt9g/)

- **Faithful contribution:** Asks for the exact weight quant and whether the KV cache was also quantized.
- **Type:** weight/cache diagnostic question
- **Why relevant (assessment):** Explicitly separates two often-conflated precision variables.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** What exact weight quant is in use?; Was the KV cache quantized, and to what K/V formats?
- **Transferability (inference):** These missing variables enable reproduction but do not themselves establish quantization as the failure cause.
- **Themes:** weights, kv, methodology

<a id="c377"></a>

### C377 — u/MediumAd4983

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx21synp679/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx21synp679/)

- **Faithful contribution:** Claims the exact 27B/128K model made an entire linked project using llama.cpp, OpenCode and surf.cli without vision. Reports roughly 50–60 tokens/s and estimates 2–3 days rather than Claude’s 2–3 hours, with extensive thinking and make-test-fix cycles; judges quality medium at best, not Claude-level.
- **Type:** project-level experience with limitations
- **Why relevant (assessment):** Detailed positive end-to-end claim that acknowledges speed, iteration and quality ceilings.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What prompts, intervention history, quant, hardware and acceptance tests support the entire-project attribution?; Are the Claude timing estimates measured?
- **Transferability (inference):** The linked project was not inspected, so authorship and correctness are unverified; eventual completion with repeated repair is not equivalent to frontier speed or quality.
- **Themes:** runtime, harness, workflow, reasoning, context, alternatives, methodology

<a id="c378"></a>

### C378 — u/goingsplit

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3guvrvjc1/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3guvrvjc1/)

- **Faithful contribution:** Requests that the preceding project include the prompts used to generate it with Qwen.
- **Type:** reproducibility request
- **Why relevant (assessment):** Important request for evidence behind C377’s project-level claim.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Can the actual prompts used to create the project be included? C379 supplies an approximate initial prompt and setup advice, not a complete prompt transcript.
- **Transferability (inference):** A request is not validation; exact prompts, history and interventions remain needed to reproduce the project.
- **Themes:** methodology, workflow

<a id="c379"></a>

### C379 — u/MediumAd4983

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3zwssmahx/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3zwssmahx/)

- **Faithful contribution:** Replies that a full setup release would be more useful than prompts and describes starting with PLAN.md/AGENTS.md plus requirements. Recommends minimal tool context, OpenCode (optionally OpenChamber), surf.cli rather than an integrated browser, automatic compaction and files for long tasks, contrasting 128K with larger-model context.
- **Type:** project follow-up and context-management recipe
- **Why relevant (assessment):** Substantive partial answer to C378 with concrete workflow details but no full released setup.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Will the complete setup, actual prompt history and compaction settings be published?; What exact context savings and task outcomes follow from the tool/harness changes?
- **Transferability (inference):** This is a context-efficient workflow preference, not a controlled demonstration that Claude Code or integrated browsers are universally unsuitable.
- **Themes:** context, harness, workflow, methodology

<a id="c381"></a>

### C381 — u/Muted_Anteater1170

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx26ez7i7q8/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx26ez7i7q8/)

- **Faithful contribution:** Suspects prompting, agents and harness issues and reports agents fixed most of a similar problem; says 27B now works extremely well, though Flash Next is used more often.
- **Type:** vague before/after experience
- **Why relevant (assessment):** Relevant claimed improvement, but missing all reproduction details.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** Which agents, prompts, model settings and tasks changed?; What problems remain after “most” were fixed?
- **Transferability (inference):** Does not isolate agents as the cause, establish a universal fix, or quantify comparative performance.
- **Themes:** harness, workflow, alternatives, methodology

<a id="c382"></a>

### C382 — u/Tigonimous

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2copl68pv/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2copl68pv/)

- **Faithful contribution:** Asks which harness is used with Qwen.
- **Type:** harness question
- **Why relevant (assessment):** Preserves an explicit missing-workflow question.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which harness is being used with Qwen?
- **Transferability (inference):** No effectiveness evidence follows from the question alone; no direct answer is identified within the assigned range.
- **Themes:** harness, methodology

<a id="c383"></a>

### C383 — u/Iajah

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2cyunu010/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2cyunu010/)

- **Faithful contribution:** Prescribes Q8/256K with llama.cpp, suggests 48GB VRAM/64GB RAM for one agent or 96GB/128GB for three, and attributes loops to a newly introduced Copilot harness, recommending the VS Code Local harness instead.
- **Type:** hardware sizing and harness diagnosis
- **Why relevant (assessment):** Specific concurrency guidance and loop hypothesis, but no first-person test or measured capacity.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** What model/cache allocation, occupied context and throughput support those memory sizes?; Which Copilot/Local harness versions reproduce and eliminate loops?
- **Transferability (inference):** The asserted precision/context minimum and harness causality are not validated; contrary Q4/24GB successes require task-matched comparison.
- **Themes:** weights, context, runtime, hardware, harness, reasoning, methodology

<a id="c384"></a>

### C384 — u/Comfortable-Cry-3261

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2fsxapm77/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2fsxapm77/)

- **Faithful contribution:** Reports usable Claude replacement on a 3090 with headless Linux and ninfer: 200k context, Q8 KV, image support and mtp3; uses the ninfer endpoint with subagents disabled. Claims 70–110 tokens/s response and “1.2–1.7 prefill,” while completing the same tasks 5–10 times slower.
- **Type:** hardware-matched runtime configuration report
- **Why relevant (assessment):** Detailed near-target configuration, but weight quant and prefill units are missing.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Which weights, RAM, runtime build and sampling are used?; What are the units and measurement conditions for “1.2–1.7 prefill,” and is the 5–10x comparison measured?
- **Transferability (inference):** Promising candidate replication, not a verified replacement claim; do not silently convert ambiguous prefill units or assume capacity equals full-context speed.
- **Themes:** runtime, hardware, weights, kv, context, harness, workflow, methodology

<a id="c385"></a>

### C385 — u/Effective-Giraffe655

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2ouo70q03/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2ouo70q03/)

- **Faithful contribution:** Argues 27B lacks knowledge rather than basic capability and recommends supplying domain-specific specs/skills. Reports a red-team skill finding 27 of 38 security issues across four tiers with proof-of-concept exploits, compared with about 10 of 38 without it and failure on harder tiers. Links related discussion/blog examples.
- **Type:** domain-knowledge intervention experience
- **Why relevant (assessment):** Specific within-workflow numeric comparison supporting knowledge scaffolding as a hypothesis.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What tasks, tier definitions, model/settings, repetitions and false-positive checks underpin 27/38 versus about 10/38?; Were the tests held out from skill construction and what human corrections were involved?
- **Transferability (inference):** The claimed finding counts are not independent security validation or general coding reliability; linked materials were not accessed.
- **Themes:** knowledge, harness, workflow, methodology

<a id="c386"></a>

### C386 — u/humanbutnothuman

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2pvy47zc5/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2pvy47zc5/)

- **Faithful contribution:** Recommends agentic tools such as Bionic or Hermes for a more Claude-like workflow.
- **Type:** agent-tool recommendation
- **Why relevant (assessment):** Substantive alternative-harness suggestion without a reported comparison.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which specific tools, configurations and tasks demonstrate the claimed improvement?
- **Transferability (inference):** Tool choice alone does not establish Claude-like capability, and Hermes preferences elsewhere in this range conflict.
- **Themes:** harness, alternatives, workflow

<a id="c387"></a>

### C387 — u/Hot_Half_5263

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2v1w5m2ea/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2v1w5m2ea/)

- **Faithful contribution:** Reports switching from Qwen 3.8 27B “nfvp4” to Swift 1.5 Qwen 3.8 27B “nfvp4,” describing clearer output and more reasonable thinking time as “100x better.”
- **Type:** same-format variant-change experience
- **Why relevant (assessment):** Useful model-variant anecdote at low precision; the magnitude is rhetorical, not a measured score.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Which exact artifact/format is meant by “nfvp4,” and what hardware/runtime was used?; How do correctness and reasoning lengths compare on identical tasks?
- **Transferability (inference):** Do not silently normalize the source’s format spelling or treat “100x” as quantitative; a fine-tune may trade capability for shorter reasoning.
- **Themes:** alternatives, weights, reasoning, methodology

<a id="c388"></a>

### C388 — u/AdOrnery5134

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2wn9cww4j/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2wn9cww4j/)

- **Faithful contribution:** Recommends Strata with Qwen 3.8 Flash Next and calls its thinking very good.
- **Type:** runtime/alternative recommendation
- **Why relevant (assessment):** Minimal substantive alternative recommendation with no deployment evidence.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which quant, hardware, context and tasks support the assessment?
- **Transferability (inference):** Different model/runtime and unspecified memory requirements preclude assuming a solution on the OP machine.
- **Themes:** alternatives, runtime, reasoning

<a id="c389"></a>

### C389 — u/Original-Mistake8624

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx31xx7eheq/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx31xx7eheq/)

- **Faithful contribution:** Describes a two-machine local assistant under development: Ryzen 7 8745HS/32GB DDR5 orchestration with SQLite memory, and Ryzen 9 3900X/64GB DDR4 plus dual 12GB RTX 3060 inference using Qwen35B-A3B Q4_K_M, MTP and llama.cpp CUDA. Reports 34 GPU layers, about 37.5 tokens/s, 130W GPU limits, 50–57°C and about 2.35Gbps over dedicated 2.5GbE. Prefers the MoE after comparison with 27B and separates planning/execution/verification; explicitly does not claim solved reliability.
- **Type:** distributed-architecture setup and research question
- **Why relevant (assessment):** Highly specific architecture report, but no comparative coding results or complete reliability evidence.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Has anyone tried a similar distributed architecture or compared 27B with 35B-A3B for agentic coding?; What comparative task results, orchestration overhead and validation support the design?
- **Transferability (inference):** Different GPUs/model and a work-in-progress agent stack limit transfer; tokens/s, thermals and network speed do not establish task correctness.
- **Themes:** hardware, runtime, weights, harness, workflow, alternatives, methodology

<a id="c390"></a>

### C390 — u/xoxoxosevenhorserace

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx36pg8w23o/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx36pg8w23o/)

- **Faithful contribution:** Attributes the issue to a badly quantized 27B artifact and reports large differences depending on who produced the quant and how.
- **Type:** quant-provenance experience
- **Why relevant (assessment):** Relevant artifact-quality hypothesis but no named comparison or measurements.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** Which exact artifacts, provenance, quant methods and matched tasks show the difference?
- **Transferability (inference):** Same nominal bit width may hide differing artifacts/settings, but the OP’s quant is not demonstrated defective.
- **Themes:** weights, methodology

<a id="c391"></a>

### C391 — u/xoxoxosevenhorserace

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx398invhr5/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx398invhr5/)

- **Faithful contribution:** Adds that, in the commenter’s experience, badly quantized models are especially prone to repetitive thinking loops.
- **Type:** quantization/loop experience
- **Why relevant (assessment):** Adds a specific proposed failure mode beyond C390; retained rather than treated as duplicate.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** Which artifacts and loop measurements establish this association under identical runtime/sampling?
- **Transferability (inference):** Association is a hypothesis, not proof that quant quality causes every loop or that higher bit width always fixes it.
- **Themes:** weights, reasoning, methodology

<a id="c392"></a>

### C392 — u/xoxoxosevenhorserace

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3bzk5fu02/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3bzk5fu02/)

- **Faithful contribution:** Reports a similar experience involving Ollama and MLX and recommends vLLM plus a good Unsloth quant from Hugging Face.
- **Type:** runtime/artifact experience and recommendation
- **Why relevant (assessment):** Relevant broad runtime/artifact hypothesis, but the reported Ollama/MLX relationship is unclear.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** What precisely was compared between Ollama and MLX?; Which Unsloth format is compatible with the recommended vLLM deployment?
- **Transferability (inference):** Do not infer a controlled backend comparison or assume any named quant loads in any engine; the intended runtime path needs clarification.
- **Themes:** runtime, weights, methodology

<a id="c393"></a>

### C393 — u/goingsplit

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3bin5g141/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3bin5g141/)

- **Faithful contribution:** Asks which quant is acceptable.
- **Type:** quant-selection question
- **Why relevant (assessment):** Preserves a concrete request for artifact guidance.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which quant is considered acceptable? C394 names sources/formats but does not provide controlled quality or fit evidence.
- **Transferability (inference):** Naming a source is only a candidate selection step, not validation of quality on this workload.
- **Themes:** weights, methodology

<a id="c394"></a>

### C394 — u/xoxoxosevenhorserace

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3rq8jxbc2/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3rq8jxbc2/)

- **Faithful contribution:** Recommends Unsloth GGUFs or MLX-community/community MLX artifacts and says a linked Qwen3.8-27B-MLX-4bit variant is what the commenter runs on a Mac.
- **Type:** artifact recommendation and platform experience
- **Why relevant (assessment):** Specific low-bit Mac artifact use, with partly obscured source identity in the corpus.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Which exact community/artifact is intended where the source link contains asterisks?; What Mac memory, context, task results and comparisons justify calling the artifact good?
- **Transferability (inference):** MLX-on-Mac use is not a 3090 replication; provenance recommendations and merely running a 4-bit model do not establish coding correctness.
- **Themes:** weights, runtime, hardware, methodology

<a id="c395"></a>

### C395 — u/Unhappy_Relief_9158

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx370lcu2zo/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx370lcu2zo/)

- **Faithful contribution:** Claims the model is like Sonnet 5 when used with the right workflow.
- **Type:** workflow-dependent capability assertion
- **Why relevant (assessment):** Retained substantive but unsupported parity claim.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** What workflow and task-matched tests support Sonnet-like performance? C396 requests details; C397 gives only a broad agent suggestion.
- **Transferability (inference):** No model, quant, hardware, outcome metric or intervention accounting supports treating the parity claim as fact.
- **Themes:** workflow, alternatives, methodology

<a id="c396"></a>

### C396 — u/goingsplit

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3az18w1b5/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3az18w1b5/)

- **Faithful contribution:** Asks what the purported right workflow would be.
- **Type:** workflow clarification question
- **Why relevant (assessment):** Direct request to make C395’s capability assertion concrete.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** What is the workflow behind the claimed Sonnet-like result? C397 mentions OpenCode/Pi and agents but leaves implementation and validation unspecified.
- **Transferability (inference):** The question highlights missing reproducibility; it is not an endorsement of the parity claim.
- **Themes:** workflow, harness, methodology

<a id="c397"></a>

### C397 — u/Unhappy_Relief_9158

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3s6mh715x/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3s6mh715x/)

- **Faithful contribution:** Suggests OpenCode or Pi Code with agents, subagents and workflow agents, and offers to teach the approach.
- **Type:** workflow clarification and offer
- **Why relevant (assessment):** Substantive partial answer to C396 but not a complete, tested procedure.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** How are agents configured, scheduled and constrained on the OP hardware?; What checks and measured results support the preceding Sonnet comparison?
- **Transferability (inference):** Multi-agent orchestration may add memory/context/latency pressure; naming agents does not validate capability parity.
- **Themes:** harness, workflow, hardware, methodology

<a id="c398"></a>

### C398 — u/Upper_Ad_8397

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3iiohdb50/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3iiohdb50/)

- **Faithful contribution:** Recommends llama.cpp as the appropriate path.
- **Type:** runtime recommendation
- **Why relevant (assessment):** Minimal substantive runtime preference retained under the inclusion rule.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which build, weights, template, cache and sampling settings are required?
- **Transferability (inference):** A runtime name without a configuration or outcome cannot establish a fix.
- **Themes:** runtime

<a id="c399"></a>

### C399 — u/Embarrassed_Ad3189

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3md16enxf/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3md16enxf/)

- **Faithful contribution:** Reports a similar machine using llama.cpp CUDA 13 build b11146, Unsloth Q4_K_M, Pi/Pendant, Q4_0 K/V cache and draft-MTP up to two tokens at minimum probability 0.80. Provides a Windows server command with all GPU layers, 16 threads, one parallel slot, top-p 0.95, min-p 0, F16 multimodal projection and reasoning budget 131072/preserve. Reports 35–45 tokens/s and useful applications/data work, often asynchronously for 20–30 minutes; retains Claude for niche/time-critical tasks and says 3.8 needs thinking.
- **Type:** detailed reproducible configuration and bounded success
- **Why relevant (assessment):** Most concrete low-weight/low-KV-precision counterexample in the range; command is source evidence, not executed or independently validated.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What exact CPU/RAM, actual context setting/occupancy and task acceptance tests were used?; What offload/memory behavior occurs, and how much intervention or Claude fallback is required?
- **Transferability (inference):** Close-hardware recipe merits controlled replication but cannot establish universals. Reasoning budget is not itself a configured context length; success contradicts Q8-only claims without proving Q4 equivalent to BF16.
- **Themes:** runtime, weights, kv, hardware, sampling, reasoning, context, harness, workflow, methodology

<a id="c400"></a>

### C400 — u/brianlmerritt

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx4307dcasl/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx4307dcasl/)

- **Faithful contribution:** Reports Flash Next on one 3090 with 128GB DDR4 and Strata was insufficient for projects until adding autocode (or Pi). Says data-analysis test projects worked but looked poor, with good speed and 128k context; considers it suitable for backend work with Claude Opus/GPT Astra setup and supervision.
- **Type:** hardware/runtime/harness experience with caveats
- **Why relevant (assessment):** Specific before/after orchestration anecdote that acknowledges presentation quality and cloud oversight.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What quant, task tests and exact changes accompanied adding autocode/Pi?; How much setup, correction and review are supplied by cloud models?
- **Transferability (inference):** Uses a different MoE and four times the OP RAM; backend suitability is the commenter’s inference from limited test projects, not validated standalone autonomy.
- **Themes:** hardware, runtime, harness, context, workflow, alternatives, methodology

<a id="c401"></a>

### C401 — u/cagriuluc

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx46pway5k1/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx46pway5k1/)

- **Faithful contribution:** Asks whether the missing quantization and runtime configuration were omitted because the poster already tried everything.
- **Type:** diagnostic question
- **Why relevant (assessment):** Directly identifies missing reproducibility details.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Actual question: why were quants and configuration not shared; have alternatives actually been tried?
- **Transferability (inference):** Requesting configuration is transferable; it does not establish that configuration is the cause.
- **Themes:** weights, runtime, methodology

<a id="c402"></a>

### C402 — u/T_rex2700

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx47m8c4qe9/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx47m8c4qe9/)

- **Faithful contribution:** Guesses the setup is Ollama on Windows, dismisses its performance for this use, suggests a runtime with llama.cpp argument overrides and Linux, and says personal experience taught them to be very specific with Qwen because of reasoning loops.
- **Type:** runtime recommendation and anecdote
- **Why relevant (assessment):** Addresses runtime and prompting, but the platform diagnosis is a guess and the named alternative is obscured in the source.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** Is the poster actually on Windows; which overridden arguments and alternative runtime are intended; what prompts stopped loops?
- **Transferability (inference):** Do not infer that Windows or Ollama universally prevents agentic coding; no controlled comparison or exact configuration is supplied.
- **Themes:** runtime, hardware, workflow, reasoning

<a id="c403"></a>

### C403 — u/Comprehensive_Rock50

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx49zpk1leo/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx49zpk1leo/)

- **Faithful contribution:** Distinguishes advertised 128K capacity from comprehension, estimates 4-bit weights at about 13.5GB before overhead/cache, and argues VRAM shortages usually cause offload, slowness or allocation failure rather than directly reducing inherent reasoning. Says quantization/truncation can affect quality and requests a failed execution trace to separate model failure from agent-environment failure. Also argues that understanding a project, making a small change, running a test and reporting it is a reasonable local-agent evaluation target rather than an inherently unrealistic expectation.
- **Type:** diagnostic analysis
- **Why relevant (assessment):** Strong diagnostic framing, but its memory estimate and causal assertions are explanatory claims, not measurements from this setup.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Actual question: is Qwen failing to reason or being given an incoherent agent environment? Missing prompt, files read, tool trace, actual context, quant, offload and loop onset.
- **Transferability (inference):** The proposed trace-based diagnosis is broadly useful; the rough memory estimate is not a measured fit guarantee and capability remains untested.
- **Themes:** runtime, weights, kv, context, harness, reasoning, methodology

<a id="c404"></a>

### C404 — u/xb1n0ry

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx4pqkg0l2c/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx4pqkg0l2c/)

- **Faithful contribution:** Calls harness choice central; recommends Pi with medium/low thinking and at least Q6, claiming high/xhigh causes overthinking. Suggests llama.cpp/vLLM, Flash Next with Strata and possibly more RAM, or a linked coding/reasoning fine-tune for remaining on 27B.
- **Type:** configuration and alternative recommendations
- **Why relevant (assessment):** Contains concrete knobs and alternatives but no described test or hardware fit evidence.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** What exact Pi settings and fine-tune tests support Q6 and the thinking ceiling; can the proposed alternatives fit the available memory?
- **Transferability (inference):** The Q6 minimum and high-thinking failure claim are unvalidated universals and conflict with successful Q4/xhigh reports in this slice.
- **Themes:** harness, reasoning, weights, runtime, alternatives, hardware

<a id="c405"></a>

### C405 — u/relmny

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx4ptzd0plv/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx4ptzd0plv/)

- **Faithful contribution:** Criticizes declaring the model bad without reporting quantization/parameters and recommends changing inference engine, understanding the quant and applying recommended parameters.
- **Type:** diagnostic recommendation
- **Why relevant (assessment):** Retains the substantive reproducibility request despite accusatory phrasing; the claim that hardware was not supplied should not be adopted as fact.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which engine, quant and recommended parameters are meant, and what is the actual runtime configuration?
- **Transferability (inference):** Configuration disclosure and parameter checking generalize; replacing Ollama is a hypothesis, not an established remedy.
- **Themes:** runtime, weights, sampling, methodology

<a id="c406"></a>

### C406 — u/ddensa

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx52aqitl7n/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx52aqitl7n/)

- **Faithful contribution:** Reports good results with Unsloth Desktop serving an Unsloth Q4 model through Qwen Desktop, while Codex plans every ticket, writes coding guidance, reviews the result and issues change requests until satisfactory.
- **Type:** hybrid workflow report
- **Why relevant (assessment):** A concrete positive Q4 example, but cloud planning and repeated review are integral to the claimed success.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Hardware, task sizes, exact quant/settings, success rate and number/cost of Codex review cycles are missing.
- **Transferability (inference):** Supports testing assisted local execution rather than proving independent local-agent parity; Q4 success may depend on task decomposition and cloud supervision.
- **Themes:** runtime, weights, harness, workflow, alternatives

<a id="c407"></a>

### C407 — u/LocalhostRonin

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx52yc5j99f/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx52yc5j99f/)

- **Faithful contribution:** Requests full runtime/quant/KV/vision details and asks how long the poster waited before calling behavior a loop. Says Qwen may circle before resolving and use 5–10 times Opus's tokens per task; contrasts a claimed 128K Qwen window with Sonnet's claimed 1M, noting 30K documentation consumes a larger share of Qwen's budget.
- **Type:** diagnostic questions and anecdotal comparison
- **Why relevant (assessment):** Raises patience and context overhead as competing explanations, without measured traces or verified cross-model capacities.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** Actual question: how long was allowed before deciding it was repetitive? Missing runtime settings, actual token use and whether apparent loops eventually complete.
- **Transferability (inference):** Measure tokens-to-completion and effective context rather than transferring the 5–10x ratio or treating advertised capacities as equal-quality usable windows.
- **Themes:** runtime, weights, kv, context, reasoning, methodology

<a id="c408"></a>

### C408 — u/loudguitar42

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx53z9l8sdd/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx53z9l8sdd/)

- **Faithful contribution:** Says Qwen3.8-27B has been their main coding agent since May and works wonderfully on an RTX3090 with llama; recommends a harness such as Hermes and a properly prepared system setup.
- **Type:** positive setup report
- **Why relevant (assessment):** Direct same-GPU counterexample to unusability, but successful tasks and configuration are unspecified.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What does 'system trained properly' mean; what quant, context, prompts, test results and harness settings were used?
- **Transferability (inference):** Same GPU improves relevance but does not isolate the harness or demonstrate reliability on the poster's codebase.
- **Themes:** hardware, runtime, harness, workflow

<a id="c409"></a>

### C409 — u/_BookBurner_

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx58zrllqjp/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx58zrllqjp/)

- **Faithful contribution:** Reports making Qwen27B usable with a planner, a planning-only orchestrator, separate worker sessions, serial/round-robin execution, context cleanup above 60%, task scheduling and a final tester checking diffs against a requirements file. Says this enables extensive work but adds orchestration tokens and latency; on dual 16GB RX9060XT plus 64GB RAM, Flash-Next GSQ-RCO coder reportedly does better and finishes sooner despite slower token generation and partial offload.
- **Type:** detailed orchestration and alternative report
- **Why relevant (assessment):** Concrete workflow and hardware anecdote highlighting task completion rather than raw token speed.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Which tasks and success rates were compared; what models/quants and timing measurements underpin the Flash-Next comparison; what is the exact cleanup policy?
- **Transferability (inference):** Decomposition, explicit criteria and independent checks are testable patterns, but the 60% threshold, hardware fit and alternative-model superiority are setup-dependent.
- **Themes:** workflow, harness, context, reasoning, alternatives, hardware, methodology

<a id="c410"></a>

### C410 — u/jsbot-02

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx5f9r3nezk/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx5f9r3nezk/)

- **Faithful contribution:** Reports a mostly successful pelican-riding-a-bike test, with incorrect leg/pedal relationships, using Qwen3.8-27B-GSQ-RCO-GGUF Q3 on a 9800X3D, RX9070XT 16GB and 64GB DDR5 at roughly 30–40 tokens/s.
- **Type:** single-task setup report
- **Why relevant (assessment):** A concrete low-quant positive result with an admitted defect, but a visual demo does not test repository-scale autonomous coding.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What harness, prompt, generated artifact and correctness criteria were used; what does '30–40 tokens' measure exactly?
- **Transferability (inference):** Useful as a narrow Q3 counterexample, not evidence of reliable multi-file coding or transfer to a 3090.
- **Themes:** weights, hardware, methodology

<a id="c411"></a>

### C411 — u/Joozio

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx5uc3zz3c1/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx5uc3zz3c1/)

- **Faithful contribution:** Reports swapping a model-agnostic non-coding agent from Claude to Ollama-served Qwen9B with a one-line change. File lookup, memory recall and simple tools held up, while analysis/synthesis degraded; 4B was much worse and 9B was their practical floor. Asks whether the poster first fails at cross-file planning or individual edits.
- **Type:** adjacent comparative report and question
- **Why relevant (assessment):** Useful task-level distinction and dissent against blanket Ollama failure, explicitly adjacent rather than 27B coding evidence.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Actual question: does planning across files or individual editing fail first? Exact tasks, quant, hardware and measured comparisons are absent.
- **Transferability (inference):** Narrow retrieval/tool tasks may be separable from synthesis, but findings from 4B/9B non-coding agents do not establish a 27B coding ceiling.
- **Themes:** runtime, harness, workflow, reasoning, alternatives, methodology

<a id="c412"></a>

### C412 — u/Damn-Sky

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx5vscyrixw/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx5vscyrixw/)

- **Faithful contribution:** Reports Swift1.5 IQ3_XXS on 16GB VRAM with 132K context and DeepSeek harness working well for home use at about 46 tokens/s, with occasional errors and slower operation than Claude.
- **Type:** positive alternative setup report
- **Why relevant (assessment):** Specific low-bit/context counterexample; acceptable home-use errors differ from professional reliability requirements.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Exact model identity, hardware, resident memory/offload, tasks, actual context occupancy and speed measurement are missing.
- **Transferability (inference):** Do not transfer the advertised context or subjective success to stock Qwen27B or professional workloads; the model variant and harness may matter.
- **Themes:** alternatives, weights, hardware, context, harness

<a id="c413"></a>

### C413 — u/vintagevibes_

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx69edwx4tg/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx69edwx4tg/)

- **Faithful contribution:** Says Ollama never worked for their agentic tasks and reports LM Studio plus Claude Code CLI Q4_K_M on a 4090 succeeding at 60–70 tokens/s. Recommends it for a 3090, says sub-Q4 quants loop in tool calls in their experience, and notes the model installs things readily and fact-checks less than Claude, speculating prompts could fix this.
- **Type:** comparative setup report
- **Why relevant (assessment):** Concrete positive configuration with behavioral caveats; the Ollama attribution and prompting remedy are not isolated tests.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Which tasks, actual quant files, context and settings; was the same model/harness compared across servers; did prompting fix the autonomy/fact-checking issue?
- **Transferability (inference):** A 4090 test suggests a candidate 24GB configuration but not identical speed or reliability on a 3090; the sub-Q4 cutoff is anecdotal.
- **Themes:** runtime, harness, weights, hardware, workflow, sampling

<a id="c414"></a>

### C414 — u/fififijamie

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx69im9z63p/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx69im9z63p/)

- **Faithful contribution:** Reports good results mostly on small personal projects with a 24B oQ4e-mtp model on oMLX, 64GB unified memory and 262K context, usually with thinking disabled.
- **Type:** adjacent positive setup report
- **Why relevant (assessment):** Shows another local workflow can work with thinking off, but this is not the same model or memory architecture.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Which 24B model, tasks, actual occupied context and correctness checks were involved?
- **Transferability (inference):** Different model and unified-memory hardware make this an adjacent option, not a direct Qwen27B configuration fix.
- **Themes:** alternatives, weights, runtime, hardware, context, reasoning

<a id="c415"></a>

### C415 — u/sarp3d0n

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6amdc1zmo/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6amdc1zmo/)

- **Faithful contribution:** Reports moving from Ollama through llama.cpp to PolyStrata and obtaining 3x speed on an RTX5060 8GB/32GB RAM; now uses Tiel Coder35B A3B and suggests Swift1.5 for the poster's hardware.
- **Type:** runtime migration and alternative report
- **Why relevant (assessment):** Concrete hardware and speed anecdote, but model changes may confound the runtime comparison.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Which model was held constant for the 3x measurement; what quant, offload, task and latency metrics were used?
- **Transferability (inference):** This motivates comparing runtimes/MoE options, not assuming a 3x gain or fit for a 3090 with another model.
- **Themes:** runtime, alternatives, hardware, methodology

<a id="c416"></a>

### C416 — u/BlAcKdN

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6b8egtc4h/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6b8egtc4h/)

- **Faithful contribution:** Reports Qwen27B working well for light work through OpenCode and argues the harness may not be the culprit. Recommends llama.cpp over Ollama and case-specific tuning; reports rare loops on high thinking and offers to share configuration privately.
- **Type:** positive use report and diagnostic dissent
- **Why relevant (assessment):** Substantive dissent from harness-first explanations, with a limited light-work scope.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What exact llama.cpp configuration, quant, hardware, tasks and high-thinking failure traces were used?
- **Transferability (inference):** Light-task success and rare loops do not establish performance for autonomous larger tasks; runtime causality remains untested.
- **Themes:** harness, runtime, reasoning, workflow, methodology

<a id="c417"></a>

### C417 — u/bobish01

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6baubhrxf/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6baubhrxf/)

- **Faithful contribution:** Recommends Qwen Strata Flash125B for larger projects and instruction following; reports using ChatGPT to architect/plan, Qwen3.8 Flash to code and GPT for final bug fixing.
- **Type:** hybrid alternative workflow report
- **Why relevant (assessment):** Relevant alternative and division of labor, not evidence for stock 27B autonomous success.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What exact model/runtime/hardware, task outcomes and cloud intervention levels support the superiority claim?
- **Transferability (inference):** The hybrid workflow can be trialed, but a much larger model plus cloud planning/review is not a like-for-like 27B comparison.
- **Themes:** alternatives, runtime, workflow, reasoning

<a id="c418"></a>

### C418 — u/sumane12

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6bh1aoh45/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6bh1aoh45/)

- **Faithful contribution:** Recommends llama.cpp, DeepSeek harness and Q4 quant, with Claude Opus5.5 supplying objectives and instructions.
- **Type:** hybrid configuration recommendation
- **Why relevant (assessment):** Provides a concrete candidate stack while relying on frontier planning.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** What model variant, hardware, context, settings and evaluated tasks support this recommendation?
- **Transferability (inference):** Treat as a proposed hybrid experiment, not proof that Q4 is sufficient or that local autonomy matches Claude.
- **Themes:** runtime, harness, weights, workflow, alternatives

<a id="c419"></a>

### C419 — u/No_Oil_6152

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6bxqz7zj8/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6bxqz7zj8/)

- **Faithful contribution:** Requests temperature, KV cache and harness details; claims Qwen3.8 can produce good results but is very slow.
- **Type:** diagnostic request and capability claim
- **Why relevant (assessment):** Identifies omitted settings that can affect debugging without giving a tested remedy.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** What temperature, KV format/size and harness are actually being used; how is slowness measured?
- **Transferability (inference):** Settings disclosure transfers; the quality and slowness claims lack workload-specific evidence.
- **Themes:** sampling, kv, harness, runtime, methodology

<a id="c420"></a>

### C420 — u/webAd-8847

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6etug50o4/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6etug50o4/)

- **Faithful contribution:** Reports similar problems resolved through LM Studio's greater control and hours spent selecting model/settings/context, using VSCode Chat with a custom LM Studio endpoint.
- **Type:** runtime tuning report
- **Why relevant (assessment):** Concrete toolchain anecdote but no reproducible successful parameter set.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Which model, quant, hardware, context and settings changed; which changes actually fixed the failures?
- **Transferability (inference):** Supports budgeting tuning time, but changing models and parameters alongside runtime prevents attributing success solely to LM Studio.
- **Themes:** runtime, harness, context, workflow, methodology

<a id="c421"></a>

### C421 — u/nomorespamplz

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6ftbfzag1/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6ftbfzag1/)

- **Faithful contribution:** Claims llama.cpp plus a good harness and custom prompt would make even a smaller model outperform the poster's current results.
- **Type:** configuration claim
- **Why relevant (assessment):** Relevant proposed cause/remedy but lacks a named harness, prompt or test.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which smaller model, harness, custom prompt and matched task comparison justify the claim?
- **Transferability (inference):** A candidate hypothesis, not a general guarantee that runtime/prompt quality dominates model capability.
- **Themes:** runtime, harness, workflow, alternatives

<a id="c422"></a>

### C422 — u/immediate-drink-9876

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxbhmc3e00w/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxbhmc3e00w/)

- **Faithful contribution:** Asks which harness works best based on the other commenter's experience.
- **Type:** harness question
- **Why relevant (assessment):** Retains a substantive unresolved tool-selection question.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Actual question: which harness works best in the respondent's experience, and for which model/tasks?
- **Transferability (inference):** Harness ranking needs task/configuration context; the question itself provides no comparative evidence.
- **Themes:** harness, methodology

<a id="c423"></a>

### C423 — u/Ancient-Camel1636

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6isohm9i9/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6isohm9i9/)

- **Faithful contribution:** Says Qwen27B is capable though below frontier models and attributes total failure to setup. Recommends at least 128K and preferably around 200K context, compaction/handoff, low-overhead Pi, thinking budgets, minimal skills/MCP, frontier planning/advice/review, organized documentation and code indexing/retrieval tools.
- **Type:** broad workflow recommendations
- **Why relevant (assessment):** Substantive multi-layer advice, including an unsupported claim that sub-128K context is useless.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** What tasks establish the context threshold, Pi benefit or '90% local work' split; can 200K fit and remain coherent on the actual setup?
- **Transferability (inference):** Low-overhead/decomposition ideas can be tested; the universal context floor conflicts with short-context diagnostic advice and is not validated here.
- **Themes:** context, harness, reasoning, workflow, alternatives, methodology

<a id="c424"></a>

### C424 — u/floriv1999

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6iu372279/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6iu372279/)

- **Faithful contribution:** Suggests disabling rolling context and setting context size in the harness because otherwise prompts may fall out of the window, depending on runtime and harness.
- **Type:** context-retention recommendation
- **Why relevant (assessment):** A specific context-loss hypothesis that could explain degraded agent behavior.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which runtime/harness uses rolling context; what is retained or evicted; is prompt loss observable in a trace?
- **Transferability (inference):** Audit actual truncation/compaction semantics before changing settings; the behavior is implementation-specific.
- **Themes:** context, runtime, harness

<a id="c425"></a>

### C425 — u/Pretend_Engineer5951

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6kqwguvfn/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6kqwguvfn/)

- **Faithful contribution:** Calls Swift3.8-27B at 8-bit/xhigh excellent, recommends a second 3090 with FP8 vLLM tensor parallelism, and prefers OMP over Pi. Reports Pi with several extensions sent 26K tokens for a 'hi' prompt versus OMP's 12K because of extra tool instructions.
- **Type:** configuration and harness comparison report
- **Why relevant (assessment):** Provides an explicit prompt-overhead comparison and contradicts blanket Pi-lightweight and low-thinking prescriptions.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Were extension features and tools equivalent; what exact models/tasks and GPU configuration were tested; were 26K/12K counts reproduced?
- **Transferability (inference):** Audit enabled tools rather than universalizing the harness ranking; 8-bit/xhigh advice requires more hardware and conflicts with lower-quant positive reports.
- **Themes:** weights, reasoning, hardware, runtime, harness, context, methodology

<a id="c426"></a>

### C426 — u/Thutex

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6yiaketuo/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6yiaketuo/)

- **Faithful contribution:** Reports Qwen27B doing tasks well but slower than cloud on a laptop RTX5090 24GB using llama.cpp/Hermes; says repeated context compression degrades quality. Recommends mcpproxy/Markdown setup and potentially adding one or two 32GB Tesla V100s, claiming combined VRAM would make a large difference.
- **Type:** positive setup and hardware recommendations
- **Why relevant (assessment):** Same VRAM class with a useful compaction caveat, but hardware expansion claims are not demonstrated.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What quant, tasks, actual context and compression policy; do the suggested cards fit, interoperate and provide useful performance in this system?
- **Transferability (inference):** The laptop result does not establish desktop 3090 throughput; summed VRAM alone is not proof of practical multi-GPU compatibility or performance.
- **Themes:** hardware, runtime, harness, context, workflow

<a id="c427"></a>

### C427 — u/lacrem

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6yt3qubab/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx6yt3qubab/)

- **Faithful contribution:** Reports Qwen3.8-27B at about 20 tokens/s via LM Studio on a Mac Studio M2 Max with 64GB, says Flint is faster with similar reasoning, and recommends smaller prompt chunks rather than expecting DeepSeek1.7T behavior.
- **Type:** setup report and expectation advice
- **Why relevant (assessment):** Concrete throughput context and task-decomposition advice, with an unmeasured alternative comparison.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What quants, tasks, context and timing methods support the speed/reasoning comparison with Flint?
- **Transferability (inference):** Unified-memory Mac results do not predict a 3090 setup; chunking is testable but may not preserve cross-file task requirements automatically.
- **Themes:** hardware, runtime, workflow, alternatives, reasoning

<a id="c428"></a>

### C428 — u/ChemicalRoom2878

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx7dp1mb2cj/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx7dp1mb2cj/)

- **Faithful contribution:** Suggests Linux, unlocking the GPU's full TFLOPS potential and moving from Ollama to Unsloth could produce a different experience.
- **Type:** runtime/hardware recommendation
- **Why relevant (assessment):** Relevant performance suggestions, but 'unlocking TFLOPS' is not operationally defined.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** What GPU settings, Unsloth runtime/version and matched workload comparison are intended?
- **Transferability (inference):** Do not infer that unspecified GPU tuning or OS migration fixes reasoning quality; this is an untested recommendation.
- **Themes:** hardware, runtime, methodology

<a id="c430"></a>

### C430 — u/Crazyfucker73

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx7iz80r6oz/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx7iz80r6oz/)

- **Faithful contribution:** Claims Qwen27B requires at least 8-bit, more than 24GB VRAM, a decent harness and maximum reasoning to be useful; says they use Hermes.
- **Type:** universal configuration claims and limited anecdote
- **Why relevant (assessment):** Strong contrary prescription worth retaining because it conflicts with Q3/Q4 and medium/off-thinking successes.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** What hardware, exact quant, tasks and controlled comparisons establish these claimed requirements?
- **Transferability (inference):** Do not treat these asserted minimums as validated; Hermes use alone does not verify universal 8-bit/VRAM/max-thinking requirements.
- **Themes:** weights, hardware, harness, reasoning

<a id="c431"></a>

### C431 — u/sometimes_angery

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx7jq68tdpg/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx7jq68tdpg/)

- **Faithful contribution:** Guesses the poster may be using float8 given memory limits, asks the quant, and reports workplace float16 Qwen27B can complete tasks with blind spots; says int4 Flash Next performed better than float16 27B.
- **Type:** workplace model comparison report
- **Why relevant (assessment):** Concrete precision/model contrast argues that model choice may matter more than simply increasing bit depth.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Actual question: what quant is the poster using? Missing workplace hardware, tasks, context, scores and matched comparison details.
- **Transferability (inference):** An int4 larger-model win is plausible as a test candidate but not established generally; do not adopt the guessed float8 diagnosis.
- **Themes:** weights, hardware, alternatives, methodology

<a id="c433"></a>

### C433 — u/Sirlowcruz

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx8hbfnpi1s/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx8hbfnpi1s/)

- **Faithful contribution:** Suggests the model needs an agentic harness such as Hermes, asks quantization/reasoning mode, and says Q4 or lower makes this model behave oddly in their opinion.
- **Type:** harness advice and diagnostic questions
- **Why relevant (assessment):** Direct troubleshooting advice with an unsupported quant cutoff.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Actual question: what quantization and reasoning mode are being run? What observed failures justify the Q4 cutoff?
- **Transferability (inference):** Verify harness/tool support and test the actual quant; the cutoff conflicts with positive Q4 reports and is not a universal rule.
- **Themes:** harness, weights, reasoning

<a id="c434"></a>

### C434 — u/megadonkeyx

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx8i49l0mg4/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx8i49l0mg4/)

- **Faithful contribution:** Reports Strata and Qwen Next working very well on a dedicated headless Linux machine, with a custom harness developed over months for loop detection and thinking intervention.
- **Type:** custom-harness alternative report
- **Why relevant (assessment):** Shows that favorable outcomes may rely on substantial intervention engineering, not a drop-in model swap.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What model/quant, hardware, tasks and loop-detection/intervention policies were used; how often are interventions needed?
- **Transferability (inference):** Custom-loop handling is a candidate engineering pattern, but the result concerns Qwen Next and an undisclosed mature harness.
- **Themes:** runtime, alternatives, harness, reasoning, workflow

<a id="c435"></a>

### C435 — u/xapep

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx91i1tw6n6/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx91i1tw6n6/)

- **Faithful contribution:** Estimates 4-bit 27B weights at 15–16GB plus KV memory, claims spill to RAM yields very low speed and poor long-context behavior, and proposes rerunning the same prompt at 16K while watching VRAM/tokens per second. Recommends one file at a time, explicit paths and failing-test feedback; identifies as working on inference API serving.
- **Type:** diagnostic test proposal
- **Why relevant (assessment):** Concrete matched-prompt experiment separates capacity/performance concerns, but the claim that RAM spill itself causes quality collapse is not demonstrated.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Actual question: what are tokens/s at 16K versus 128K? Also missing quant, VRAM/offload measurements, agent loop and retained prompt content.
- **Transferability (inference):** The short/long-context comparison is useful; separate offload latency from truncation/quant/long-context quality rather than equating RAM spill with lost reasoning.
- **Themes:** weights, kv, context, hardware, runtime, harness, workflow, methodology

<a id="c436"></a>

### C436 — u/Slow-Secretary4262

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx91rw0hvoh/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx91rw0hvoh/)

- **Faithful contribution:** Says runtime changes and days of tuning can improve results but not approach Sonnet/DeepSeek/GLM, and suggests many low-budget local users enjoy optimization more than productive autonomous coding.
- **Type:** capability/economics dissent
- **Why relevant (assessment):** Retains substantive skepticism about practical value rather than reducing all dissatisfaction to misconfiguration.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** What workloads, configurations, quality measures and cost comparisons support the claimed ceiling or €5000 distinction?
- **Transferability (inference):** Treat as a practical-value opinion, not a measured capability bound or a reliable description of all local-model users.
- **Themes:** runtime, alternatives, economics, methodology

<a id="c437"></a>

### C437 — u/flapjack

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx9hq1a1wv9/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx9hq1a1wv9/)

- **Faithful contribution:** Claims 128K is tiny relative to Claude, requires significant context management, and estimates a Sonnet task taking 20 minutes could take 3–6 hours on the poster's setup.
- **Type:** context and latency claim
- **Why relevant (assessment):** Highlights end-to-end time overhead, but provides no timed run.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which task, settings, context occupancy and measured timings justify the 20-minute versus 3–6-hour estimate?
- **Transferability (inference):** Measure task completion and interventions directly; this timing ratio and the sufficiency of 128K cannot be generalized.
- **Themes:** context, workflow, economics, methodology

<a id="c438"></a>

### C438 — u/Future_Deer_7518

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx9ox1prq90/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx9ox1prq90/)

- **Faithful contribution:** Reports using Qwen3 Coder Instruct30B A3B UD-Q3_K_XL through llama.cpp/OpenCode on a Ryzen8700G iGPU/32GB RAM, since Q4 does not fit. Uses 30–90-line helper tasks at 11–19 tokens/s; poor prompts yield messy output while refined prompts often need one pass plus cleanup. Prefers architectural control/short feedback to slow dense27B and is considering a 128GB Ryzen AI395 upgrade but not at the current cost.
- **Type:** detailed constrained-hardware workflow report
- **Why relevant (assessment):** Concrete alternative, task scope and human-supervision evidence rather than autonomous coding parity.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What repeatable task outcomes and prompt differences underlie the first-pass claims; are proposed upgrade capabilities measured or anticipated?
- **Transferability (inference):** Useful example of small supervised tasks on CPU/iGPU, not direct proof of 27B behavior or the projected upgrade's fit/performance.
- **Themes:** alternatives, hardware, weights, runtime, harness, workflow, economics

<a id="c439"></a>

### C439 — u/Minimum_Site_1915

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx9per340ip/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx9per340ip/)

- **Faithful contribution:** Speculates that local models perform poorly on Roblox because Luau is too niche for sufficient model knowledge.
- **Type:** domain-knowledge hypothesis
- **Why relevant (assessment):** Raises task/domain knowledge as an alternative to configuration explanations, though the poster's domain is unknown.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Is the project actually Roblox/Luau; which models and reproducible tasks show the claimed knowledge limitation?
- **Transferability (inference):** Domain coverage should be tested, but this does not justify a blanket statement about all local models or all Luau work.
- **Themes:** knowledge, workflow, methodology

<a id="c440"></a>

### C440 — u/Top_Ingenuity_1830

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx9pq9r96zn/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx9pq9r96zn/)

- **Faithful contribution:** Recommends Pi.dev, suspects other tools add too much system context, suggests Claude-assisted tuning, and says the result is slowish but works.
- **Type:** harness recommendation and vague report
- **Why relevant (assessment):** Relevant context-overhead hypothesis with limited setup detail.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** Which runtime, model, settings, context accounting and tasks support the improvement?
- **Transferability (inference):** Audit actual prompt/tool overhead rather than assuming Pi is always smaller; cloud-assisted tuning changes the workflow.
- **Themes:** harness, context, workflow, alternatives

<a id="c441"></a>

### C441 — u/ThrowawayALAT

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx9rf3d8yoz/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx9rf3d8yoz/)

- **Faithful contribution:** Argues the problem is not the user but stronger, frequently updated industrial models and restricted public access, using broad analogies rather than technical evidence.
- **Type:** speculative capability dissent
- **Why relevant (assessment):** Retains the substantive frontier-gap dissent; the access and capability explanation is speculative and not diagnostic.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which models, restrictions, updates or matched task results support this explanation?
- **Transferability (inference):** Do not infer concrete model capabilities or causes from the analogies; this offers no tested local setup remedy.
- **Themes:** alternatives, methodology

<a id="c442"></a>

### C442 — u/Ok-Concentrate-5228

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx9u164tuap/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx9u164tuap/)

- **Faithful contribution:** Recommends a cloud GPU and at least 120B BF16 for professional work, while noting deployment time, vLLM flags and IDE matter. Suggests Claude planning with Qwen3.8 coding and says experience indicates Qwen must be explicitly prompted/skilled to test in a loop, unlike what they describe as innate frontier-model behavior.
- **Type:** deployment and hybrid workflow advice
- **Why relevant (assessment):** Substantive cost/scale alternative and test-loop guidance, but no hardware/task/cost evidence.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** What workloads and costs justify 120B BF16; which exact prompts/skills, runtime flags and tests produce reliable Qwen loops?
- **Transferability (inference):** Explicit testing is transferable as a workflow pattern; minimum model size/precision and innate frontier reliability are not established requirements.
- **Themes:** hardware, runtime, harness, workflow, alternatives, economics

<a id="c443"></a>

### C443 — u/Head_Evening_5697

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxa4hfzg4o0/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxa4hfzg4o0/)

- **Faithful contribution:** Suggests trying Gemma4 27B A4B with a claimed 1M context and reporting back.
- **Type:** alternative-model suggestion
- **Why relevant (assessment):** Retains a substantive alternative proposal without treating its advertised specifications as verified.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Is this exact model/specification available and correct; can it fit this hardware; how does it perform on the failed tasks?
- **Transferability (inference):** Candidate only: different model architecture and advertised context do not imply equal effective capacity or coding reliability.
- **Themes:** alternatives, context, hardware, methodology

<a id="c444"></a>

### C444 — u/boosnie

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxa6mpbmz6s/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxa6mpbmz6s/)

- **Faithful contribution:** Reports professional code analysis/coding with Pi, a single RTX3090 24GB and Swift-Qwen3.8-27B-Uncensored-Dynamic-MTP UD-Q4_K_XL in llama.cpp router mode at 160K context, with minor issues and about 110 generation/1250 prefill tokens/s on fresh context. Supplies GPU layers99, flash attention, one slot, MTP draft3, batch1024/ubatch512, K-cache q8_0/V-cache q4_0, Jinja, temperature1, top-p0.95, top-k20, min-p0 and neutral penalties; asserts total VRAM is the only relevant hardware specification.
- **Type:** detailed same-GPU configuration report
- **Why relevant (assessment):** One of the most reproducible positive 24GB/Q4 reports, directly challenging asserted 8-bit and Q8-V-cache minimums; its hardware-only assertion is overbroad.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What actual occupied context, memory breakdown, tasks/error rate, llama.cpp build and reproducible benchmarks support the figures? Full literal config remains in the corpus.
- **Transferability (inference):** A useful candidate configuration, not proof of 160K quality or reported speed on all 3090 systems; CPU, bandwidth, runtime build and task effects are not ruled out.
- **Themes:** runtime, weights, kv, template, sampling, context, harness, hardware, methodology

<a id="c445"></a>

### C445 — u/Ok_Parfait_5373

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxadhu7zfz6/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxadhu7zfz6/)

- **Faithful contribution:** In French, reports using the same model daily on the same GPU at 150 tokens/s without problems as a developer. Claims medium thinking is better for everyday tasks, suggests Swift, suspects too many skills in context, and recommends lean Pi-agent setup with only necessary context.
- **Type:** same-GPU positive report and advice
- **Why relevant (assessment):** Same-hardware anecdote and medium-thinking prescription conflict with claims that maximum reasoning/extra GPUs are essential.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What exact quant/runtime, task size, actual context and speed method; is excessive skill context observed or guessed?
- **Transferability (inference):** Useful candidate settings, but the claimed speed and medium-thinking advantage are not controlled or universally transferable.
- **Themes:** hardware, reasoning, context, harness, alternatives

<a id="c446"></a>

### C446 — u/Rogglando

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxafychgqea/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxafychgqea/)

- **Faithful contribution:** Says the hardware is adequate and recommends Strata CLI, Linux, a dedicated server, at least two preferably three slots, a two-hour tuning step and about 200K context. Suggests Qwen3.8 Flash Next Coding125B A6B spread across GPU/RAM/SSD and remote coding clients; contrasts this with a claim dense27B must stay entirely on GPU.
- **Type:** alternative deployment prescription
- **Why relevant (assessment):** Concrete architecture proposal, but no first-person run, fit measurement or validation of its dense-model residency claim.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Can the named model plus 200K context and multiple slots fit and perform on 24GB VRAM/32GB RAM/SSD; what does the tuning step entail?
- **Transferability (inference):** Treat tiered-memory MoE deployment as an experiment; dense models are not demonstrated here to require GPU-only residency, and multi-slot context increases resource needs.
- **Themes:** runtime, hardware, context, alternatives, harness, workflow

<a id="c447"></a>

### C447 — u/pinkwar

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxax0csoqzl/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxax0csoqzl/)

- **Faithful contribution:** Argues hardware should be bought only after finding a suitable model/setup using rented GPUs, and questions who approved purchasing without a proof of concept.
- **Type:** procurement/methodology critique
- **Why relevant (assessment):** Retains a useful evaluation-before-purchase point despite blame-oriented wording.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Actual question: was there a proof of concept and who approved purchase? More relevant gap: was a representative workload evaluated before selecting hardware?
- **Transferability (inference):** Workload-first proof-of-concept evaluation generalizes; it does not diagnose the current failure or establish that cloud tests reproduce local hardware behavior.
- **Themes:** methodology, hardware, economics

<a id="c448"></a>

### C448 — u/dc740

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxaydwsf3c5/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxaydwsf3c5/)

- **Faithful contribution:** Asserts the poster is using a heavily quantized Qwen and that this can differ greatly from the full version, asks for details, and adds criticism of AI-written posting.
- **Type:** quantization hypothesis and detail request
- **Why relevant (assessment):** Retains the substantive quantization issue while setting aside the personal/post-authorship criticism.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** What quant is actually used; is it substantially degraded on matched tasks relative to higher precision?
- **Transferability (inference):** Do not adopt the guessed quant or assume quantization is the entire cause without a like-for-like comparison.
- **Themes:** weights, methodology

<a id="c449"></a>

### C449 — u/Sensitive_Mountain97

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxb0crmh95v/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxb0crmh95v/)

- **Faithful contribution:** Reports using Ternary Bonsai2, described as compressed Qwen27B, and judges its coding much worse than Claude, even Sonnet3.5.
- **Type:** negative compressed-model report
- **Why relevant (assessment):** Substantive dissent, but the tested compressed derivative differs from the stock model under discussion.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What hardware, harness, task, quant/compression scheme and failure examples underpin the comparison?
- **Transferability (inference):** Do not transfer a compressed derivative's failures directly to all Qwen27B variants; compare exact artifacts on shared tasks.
- **Themes:** weights, alternatives, methodology

<a id="c450"></a>

### C450 — u/KEIY75

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxb37ix3s85/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxb37ix3s85/)

- **Faithful contribution:** Concludes it must be configuration because their 'heretic' Qwen reportedly built an entire Asterisk call center without problems; recommends llama.
- **Type:** positive task anecdote
- **Why relevant (assessment):** A concrete task claim but incomplete setup and no artifact, tests or task boundary.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** Which model/version/quant, hardware, harness and Asterisk functionality; was the call center deployed and tested?
- **Transferability (inference):** One unspecified positive project cannot prove the poster's failure is configuration or that another variant is equivalent.
- **Themes:** runtime, alternatives, workflow, methodology

<a id="c451"></a>

### C451 — u/AnticRaven

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxbdrs0egf9/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxbdrs0egf9/)

- **Faithful contribution:** Says they tried this and found overthinking, then calls Qwen3.8 Flash Next the best alternative.
- **Type:** negative reasoning anecdote and alternative
- **Why relevant (assessment):** Retains experience-based dissent and an alternative despite very little detail.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** What exact 'this' setup, reasoning mode, task and outcome; was Flash Next evaluated on the same workload?
- **Transferability (inference):** Overthinking is a reported symptom, not a demonstrated universal property; alternative superiority remains unmeasured.
- **Themes:** reasoning, alternatives, methodology

<a id="c452"></a>

### C452 — u/tuborgwarrior

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxbfat1dgo5/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxbfat1dgo5/)

- **Faithful contribution:** Suggests testing context choking/early automatic compaction and says a weaker model that sees the full task may sometimes outperform a stronger model with incomplete context.
- **Type:** context diagnostic hypothesis
- **Why relevant (assessment):** Identifies a plausible information-retention tradeoff without measured evidence.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Is compaction occurring early; what requirements or files are lost; does a fuller-context model improve the same task?
- **Transferability (inference):** Compare retained task information and quality, not parameter count alone; the proposed tradeoff needs workload-specific validation.
- **Themes:** context, harness, alternatives, methodology

<a id="c453"></a>

### C453 — u/TomFlatterhand

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxbhzgm6isi/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxbhzgm6isi/)

- **Faithful contribution:** In German, reports Qwen3.8-27B 8Q at a full 262144-token setting, argues hardware can matter and Claude-oriented project/docs structure might confuse other models, and says Qwen can code but Hermes repeatedly gets tangled. Is building a custom agent and recommends larger hardware/models, potentially multiple RTX6000 Pro cards.
- **Type:** high-context report and harness dissent
- **Why relevant (assessment):** Contrasts positive Hermes reports and adds documentation/harness confounds; actual GPU specification is not supplied.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What hardware/runtime/KV setup supports 262144; are tokens actually occupied; what Hermes failures and project-structure comparisons were observed?
- **Transferability (inference):** The stated configuration does not prove long-context comprehension; hardware expansion and documentation mismatch remain hypotheses, not established fixes.
- **Themes:** weights, context, hardware, harness, workflow, alternatives

<a id="c454"></a>

### C454 — u/Virtual_Rice7837

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxbzmcnchia/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxbzmcnchia/)

- **Faithful contribution:** Reports a 4090/ninfer setup with decent context and over 50 tokens/s but unacceptable .NET/Java coding quality despite extensive prompting/front-end experimentation. Large Blazor/Java app tasks failed and even targeted edits usually needed personal or frontier-model correction; preferred LibreChat. Supplies 131072 context/KV capacity, one concurrent request, int8 KV, MTP draft3, 32768 max output, preserve-thinking/vision and tiered continuation-cache flags.
- **Type:** detailed negative setup report
- **Why relevant (assessment):** Strong counterexample to 'only configuration' narratives: substantial runtime details, task domains and failed supervision economics, though no independently inspectable traces.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What exact weight artifact/quant, sampling/template, hardware memory use and reproducible task traces; what proportion of edits failed? Full literal flags remain in corpus.
- **Transferability (inference):** Important negative professional-workload evidence, but one model/runtime/front-end combination cannot establish a universal 27B ceiling or disprove every positive report.
- **Themes:** runtime, kv, context, harness, workflow, knowledge, alternatives, economics, methodology

<a id="c455"></a>

### C455 — u/anaNimrod

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxc2yjfgrkz/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxc2yjfgrkz/)

- **Faithful contribution:** Recommends a cloud agent coordinating the local model as a subagent, suggesting OpenCode's free-tier DeepSeek v4.1 Flash as a starting point.
- **Type:** hybrid orchestration recommendation
- **Why relevant (assessment):** Proposes a narrower role for the local model rather than fully autonomous replacement.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** What tasks, routing, supervision frequency, privacy requirements and actual free-tier limits support this setup?
- **Transferability (inference):** Cloud/local delegation is a testable workflow choice, not evidence that standalone local agents are universally ineffective.
- **Themes:** workflow, harness, alternatives, economics

<a id="c456"></a>

### C456 — u/moochine2

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxccjloran7/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxccjloran7/)

- **Faithful contribution:** Asks the quant and speculates it might be 1–2-bit, links an ISTA-DASLab GSQ-RCO27B alternative, recommends 64GB RAM to avoid memory exhaustion rather than promise speed, and suggests Strata with the 125B coder.
- **Type:** diagnostic question and upgrade/model advice
- **Why relevant (assessment):** Specific artifact and memory-capacity suggestions, but low-bit diagnosis and larger-model fit are unknown.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Actual question: which quant is in use? What memory use and task comparisons support the linked quant or 125B option on this hardware?
- **Transferability (inference):** More RAM can be evaluated for capacity, but does not establish a speed/quality gain; retain the source's distinction between capacity and acceleration.
- **Themes:** weights, hardware, alternatives, runtime, methodology

<a id="c457"></a>

### C457 — u/Jazzlike-Plate

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxcl6y6e10l/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxcl6y6e10l/)

- **Faithful contribution:** Reports a similar experience using Ollama and asks why that was a major mistake, having assumed the server made no difference.
- **Type:** runtime question and negative anecdote
- **Why relevant (assessment):** Direct unresolved challenge to blanket server-blame explanations.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** Actual question: why would Ollama make such a difference; what serving-layer behaviors alter outcomes? Missing exact model/settings and matched-runtime trace.
- **Transferability (inference):** Requires comparing templates, truncation, tool parsing and defaults rather than assuming server choice inherently changes model intelligence.
- **Themes:** runtime, template, context, harness, methodology

<a id="c458"></a>

### C458 — u/icecraft1337

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxdaud9kskg/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxdaud9kskg/)

- **Faithful contribution:** In German, suspects a harness problem and reports excellent results with a custom harness at 128K, Swift1.5 Qwen3.8-27B IQ4_XS, Q4 KV and llama.cpp; says Pi should also be a lightweight option.
- **Type:** detailed low-bit positive setup report
- **Why relevant (assessment):** Specific weight/KV/context example directly disputes claims that low-bit KV or Q4 weights are inherently unusable.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What hardware, custom-harness logic, actual context occupancy, tasks and success criteria were used?
- **Transferability (inference):** Useful counterexample candidate, not proof of reliable 128K comprehension or identical behavior in stock Qwen27B/other harnesses.
- **Themes:** harness, context, weights, kv, runtime, alternatives

<a id="c459"></a>

### C459 — u/Great_Airport_4495

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxdf7t7fg6c/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxdf7t7fg6c/)

- **Faithful contribution:** Claims high-quant Qwen27B or especially larger Flash Next can compare favorably with Opus4.5/4.6 but not Claude5.5 autonomy. Says 24GB allows at most Q4, requires close supervision, and insists KV should be at least 8-bit to avoid coherence problems.
- **Type:** capability and configuration claims
- **Why relevant (assessment):** Retains a nuanced frontier-gap view but the quant ceiling, capability ranking and KV floor are unsupported.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** What offload/context assumptions establish 'at most Q4'; which matched tasks support rankings and the 8-bit-KV requirement?
- **Transferability (inference):** Do not universalize the GPU-only quant ceiling or KV floor; successful mixed/Q4-KV reports here contradict a blanket requirement without resolving it.
- **Themes:** weights, hardware, kv, context, alternatives, workflow, methodology

<a id="c460"></a>

### C460 — u/Wolkenflitzer

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxdjdz0fpgj/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxdjdz0fpgj/)

- **Faithful contribution:** Recommends Qwen Flash Next with Strata and says it handled everything they tried.
- **Type:** positive alternative anecdote
- **Why relevant (assessment):** Substantive alternative endorsement with no task or configuration detail.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** What exact model/quant, hardware, tasks and failure criteria are hidden by 'everything'?
- **Transferability (inference):** A candidate alternative, not demonstrated superiority or fit on the poster's machine.
- **Themes:** alternatives, runtime, methodology

<a id="c461"></a>

### C461 — u/No_Ad_5933

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxdn96ygbz9/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxdn96ygbz9/)

- **Faithful contribution:** Reports Strata, Pi and Graphify codebase indexing on an RTX2080 Super8GB/32GB RAM supporting repository explanations and single-file scripts without issues; calls the model 'qwen-3.8-flash-next-coder 27B' and links the tools.
- **Type:** alternative setup and indexing report
- **Why relevant (assessment):** Concrete low-memory/narrow-task report with ambiguous model naming.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What exact model artifact is meant by 'Flash Next coder 27B'; what quant/offload, task size and repository-indexing effects were tested?
- **Transferability (inference):** Narrow script/repository-explanation success on a differently named model does not demonstrate multi-file autonomous coding or settle 27B capability.
- **Themes:** runtime, alternatives, hardware, harness, workflow, knowledge, methodology

<a id="c462"></a>

### C462 — u/PressTilde

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxedo6taaw3/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxedo6taaw3/)

- **Faithful contribution:** Links their Bantam Factory project and reports fixing 27B failures by constraining output and using a factory-style workflow with Q4_K_S or IQ4, calling it faster, more accurate and able to finish.
- **Type:** constrained-workflow implementation report
- **Why relevant (assessment):** Concrete project/workflow and low-bit positive claim, but performance comparison is unquantified.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What constraints, exact model/runtime/hardware, task set and before/after outcomes demonstrate improvement; is the linked implementation reproducible?
- **Transferability (inference):** Structured execution is a testable pattern; the existence of a link does not independently verify accuracy or establish all Q4 models work equally.
- **Themes:** workflow, harness, weights, methodology

<a id="c463"></a>

### C463 — u/ruineka

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxeg4kkg6ua/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxeg4kkg6ua/)

- **Faithful contribution:** Praises Qwen3.8-27B, describes adding another dual Intel Arc B60 48GB arrangement to their workstation and recommends DeepSeek harness based on the perceived payoff.
- **Type:** hardware/harness anecdote
- **Why relevant (assessment):** Substantive favorable hardware/harness experience, but the exact card/memory configuration is ambiguous.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What exact GPU arrangement, quant, tasks, throughput, context and measured quality underlie the praise?
- **Transferability (inference):** Different accelerator/runtime setup and unclear capacity make transfer to a single 3090 uncertain; praise alone is not reliability evidence.
- **Themes:** hardware, harness, workflow

<a id="c464"></a>

### C464 — u/BeatDistinct317

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxet1la76hx/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxet1la76hx/)

- **Faithful contribution:** Asks whether anyone knows or has rumors about Sonnet's parameter count/quantization, and speculates a model above 300B would explain why 27B should not compete.
- **Type:** model-size question and expectation hypothesis
- **Why relevant (assessment):** Retains a substantive unanswered comparison question while treating closed-model size speculation as unknown.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Actual questions: what parameter count and quantization does Sonnet use; are there rumors? No verified architecture data or matched-task evidence is supplied.
- **Transferability (inference):** Parameter speculation is not a measured capability comparison and cannot by itself establish what a 27B model should complete.
- **Themes:** weights, alternatives, methodology

<a id="c465"></a>

### C465 — u/FRackgfxhjxgfhj

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxeumcvmmjo/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxeumcvmmjo/)

- **Faithful contribution:** Says local deployment needs RAG, memory, tuning and setup rather than comparison to Claude, and calls Ollama plus OpenWebUI powerful.
- **Type:** setup recommendation and runtime dissent
- **Why relevant (assessment):** Direct dissent from categorical Ollama dismissal, though no workload or successful configuration is described.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which retrieval/memory/tuning settings, model, tasks and tool-loop support make the proposed stack effective?
- **Transferability (inference):** Treat as a candidate stack and setup hypothesis; chat/RAG capability is not the same as autonomous coding reliability.
- **Themes:** runtime, harness, workflow, knowledge, alternatives

<a id="c466"></a>

### C466 — u/robertotomas

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxez5v5cs69/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxez5v5cs69/)

- **Faithful contribution:** Recommends checking weight precision and KV bit depth, speculating Q4 KV may be responsible. Also lists faulty MTP/wrong predictive models, missing nvfp4 scaling factors, or mismatched current OpenAI protocol/runtime usage as possible causes.
- **Type:** configuration fault checklist
- **Why relevant (assessment):** Provides concrete untested failure hypotheses beyond raw model size.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Are MTP, nvfp4, Q4 KV or protocol mismatches actually present; what traces demonstrate each suspected fault?
- **Transferability (inference):** Audit only features in use; none of these hypothetical implementation errors is established in the poster's setup, and Q4 KV is not shown universally broken.
- **Themes:** weights, kv, runtime, harness, methodology

<a id="c467"></a>

### C467 — u/mechitworks

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxf7fsfmmjn/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxf7fsfmmjn/)

- **Faithful contribution:** Claims Ollama truncates when context exceeds what it can handle and Claude Code fills context quickly. Reports an nvfp4 Qwen3.8-27B on RTX5090 via vLLM/Pi at 180K with automatic compaction.
- **Type:** context-loss claim and positive setup report
- **Why relevant (assessment):** Concrete alternative stack and truncation hypothesis; no observed Ollama trace is provided.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Which Ollama version/configuration and retained messages demonstrate truncation; what artifact, KV format, occupied context and task results support the 180K report?
- **Transferability (inference):** Check configured windows and compaction end to end; a different GPU/runtime/quant report does not prove Ollama inherently fails or that 180K is fully coherent.
- **Themes:** runtime, context, harness, weights, hardware

<a id="c468"></a>

### C468 — u/nosimsol

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxftgg4o3ab/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxftgg4o3ab/)

- **Faithful contribution:** Reports Qwen3.8-27B FP8 on vLLM being accurate most of the time and comparable to Luna5.6.
- **Type:** positive precision/runtime comparison report
- **Why relevant (assessment):** Concrete precision/server pair but an otherwise unsupported capability comparison.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What is Luna5.6, what hardware/tasks/context are used and how is comparable accuracy measured?
- **Transferability (inference):** Anecdotal FP8 success is not a frontier-equivalence benchmark or proof that FP8 is necessary.
- **Themes:** weights, runtime, alternatives, methodology

<a id="c469"></a>

### C469 — u/thisisme_whoareyou

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxg24x4njj9/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxg24x4njj9/)

- **Faithful contribution:** Says newly begun tests of complex logic already fail before trying coding.
- **Type:** negative reasoning anecdote
- **Why relevant (assessment):** Substantive negative capability report without task/setup details.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** Which logic problems, model artifact, reasoning settings, prompts and expected answers failed?
- **Transferability (inference):** Retain as dissent but not a measured reasoning ceiling or diagnosis of coding-agent behavior.
- **Themes:** reasoning, methodology

<a id="c470"></a>

### C470 — u/Sizzin

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxg4cwwccki/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxg4cwwccki/)

- **Faithful contribution:** Warns a single 24GB system will struggle with multiple users and doubts Q4 for serious tasks, though small steps might work. Reports FP8/Pi strong enough for unattended overnight work and says stock FP8 beat alternatives in informal usage, explicitly without benchmarks. Claims Claude-oriented context is bloated and Flash Next better for niche knowledge.
- **Type:** autonomy report with precision/domain advice
- **Why relevant (assessment):** Concrete FP8/Pi success with an explicit non-benchmark caveat and concurrency/domain concerns.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What hardware, task scope, overnight failure rate, actual context/tool overhead and quant comparisons were used; were niche-domain claims tested?
- **Transferability (inference):** Do not transfer unattended confidence or FP8 superiority across tasks; the author explicitly limits evidence to informal use, and Q4 doubts conflict with positive Q4 reports.
- **Themes:** hardware, weights, harness, context, workflow, knowledge, alternatives, methodology

<a id="c471"></a>

### C471 — u/sadomazoku

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxgf6pnx3fl/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxgf6pnx3fl/)

- **Faithful contribution:** Attributes failure entirely to configuration, reporting Qwen Q4_K_M coding on a 24GB GPU with no RAM offload and no remaining need for frontier coding models. Recommends leaving Ollama, starting with llama.cpp and moving toward vLLM for a team.
- **Type:** same-memory positive setup report
- **Why relevant (assessment):** Direct counterexample to '24GB/Q4 cannot work', but no runtime settings, task examples or concurrency measurements.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What exact GPU, runtime/template/settings, context, tasks and success criteria support 'never any issue'; how was Ollama compared?
- **Transferability (inference):** Useful single-user configuration candidate, not proof of a 100% configuration cause or team-serving performance.
- **Themes:** weights, hardware, runtime, harness, workflow, methodology

<a id="c472"></a>

### C472 — u/bigb159

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxhdetmdiua/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxhdetmdiua/)

- **Faithful contribution:** Reports code/tool calls unreliable below Q6 in their experience and says limited VRAM makes concurrency painfully slow; suggests scheduling team usage or adding a GPU.
- **Type:** precision and concurrency anecdote
- **Why relevant (assessment):** Direct disagreement with Q4 successes and relevant multi-user capacity concern.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** Which model artifacts, harness, hardware, tasks and concurrency levels establish the Q6 threshold and slowdown?
- **Transferability (inference):** The threshold is experiential and setup-dependent; measure concurrent memory/latency before treating an extra GPU as sufficient.
- **Themes:** weights, hardware, harness, workflow, methodology

<a id="c473"></a>

### C473 — u/w1ldr3dx

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxhin83o6n9/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxhin83o6n9/)

- **Faithful contribution:** Requests the actual task/failure details and reports Swift1.5 Qwen3.8-27B Q5_K_M, xhigh reasoning, llama.cpp server and Pi on a 5090 successfully extending Steam Frame VR gamescope, KWin, Wacom drivers, wlserver and Xwayland for tablet/pen drawing use.
- **Type:** detailed complex-task success report
- **Why relevant (assessment):** One of the most task-specific positive reports, contradicting claims that xhigh necessarily derails 27B; no code/test evidence is included.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Actual challenge: what is the poster building and how exactly did it fail? Missing patch/test artifacts, context and degree of human intervention in the reported compositor work.
- **Transferability (inference):** Strong anecdotal candidate task, not independently verified autonomous success; Swift variant, Q5 and5090 hardware differ from stock Qwen on 3090.
- **Themes:** weights, reasoning, runtime, harness, hardware, workflow, methodology

<a id="c474"></a>

### C474 — u/flatfalafel

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxjur0zclgh/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxjur0zclgh/)

- **Faithful contribution:** Asks for beginner resources on llama.cpp after learning similar lessons.
- **Type:** learning-resource question
- **Why relevant (assessment):** Substantive unresolved setup/learning need, not a performance claim.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Actual question: which llama.cpp resources are appropriate for newcomers?
- **Transferability (inference):** No capability inference; a useful answer would need platform and desired server/model workflow context.
- **Themes:** runtime, workflow

<a id="c475"></a>

### C475 — u/International_Emu772

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxhishpppk0/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxhishpppk0/)

- **Faithful contribution:** Recommends GLM4.7 Flash as the best coding model for 24GB cards.
- **Type:** alternative-model recommendation
- **Why relevant (assessment):** Retains a concrete alternative but unsupported ranking.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which quant/context/hardware fit and matched coding tasks justify 'best'?
- **Transferability (inference):** A candidate to evaluate, not a proven ranking or guarantee of fitting every24GB workload.
- **Themes:** alternatives, hardware, methodology

<a id="c476"></a>

### C476 — u/Sufficient_Phone_242

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxhmhs5es2s/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxhmhs5es2s/)

- **Faithful contribution:** Reports having '3.7b' with two RTX3090s, claims around 200K context is needed, and says it is still not worthwhile because it makes more errors or is slower than paying $200/month.
- **Type:** negative cost/performance report
- **Why relevant (assessment):** Relevant practical dissent with hardware/cost framing, but model identity is ambiguous in the source.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What does '3.7b' denote; what model/quant, tasks, times, error costs and $200 subscription were compared?
- **Transferability (inference):** Do not silently reinterpret the model name or treat 200K as a validated minimum; total human time and subscription comparisons are workload-dependent.
- **Themes:** hardware, context, economics, alternatives, methodology

<a id="c477"></a>

### C477 — u/Certain_Series6810

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxiw8fahxnm/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxiw8fahxnm/)

- **Faithful contribution:** Says quant, harness and runtime all matter; recommends llama.cpp or vLLM, Pi or another lean harness, and quantization of 4-bit or higher.
- **Type:** configuration recommendation
- **Why relevant (assessment):** Concise multi-layer advice, not a reproducible result.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** Which exact model/settings, tasks and comparisons support the proposed 4-bit floor or stack choices?
- **Transferability (inference):** Useful experimental defaults, not established sufficient conditions for reliable coding.
- **Themes:** runtime, harness, weights, context

<a id="c478"></a>

### C478 — u/hopsec_

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxj12w7xk0y/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxj12w7xk0y/)

- **Faithful contribution:** Identifies context size as the main issue in their experience, says mainstream harnesses poorly handle constrained windows and some assume provider-side compaction, and describes an unreleased custom Qwen27B-focused Sidecar harness with a beta invitation.
- **Type:** custom-harness/context report
- **Why relevant (assessment):** Concrete development experience but no released artifact or outcome measurements in the corpus.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Which mainstream harness versions lack compaction; what window, tasks and measured results support Sidecar's advantage; is code available for review?
- **Transferability (inference):** Inspect actual compaction ownership rather than assuming provider/client behavior; unreleased implementation limits reproducibility.
- **Themes:** context, harness, runtime, workflow, methodology

<a id="c479"></a>

### C479 — u/humanpersonlol

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxj137mpuw5/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxj137mpuw5/)

- **Faithful contribution:** Speculates Sonnet5.5 is about700B and dismisses27B as benchmark-optimized and therefore weak.
- **Type:** model-size/capability speculation
- **Why relevant (assessment):** Retains a substantive, weakly supported dissent despite dismissive wording.
- **Evidence quality:** E0 unsupported opinion/question
- **Open questions / verification gaps:** What verified Sonnet architecture or evidence of benchmark optimization supports the claim; which real tasks were tested?
- **Transferability (inference):** Unknown closed-model size and 'benchmaxxed' labeling cannot establish a local model's practical task ceiling.
- **Themes:** alternatives, weights, methodology

<a id="c480"></a>

### C480 — u/fathergoat_adventure

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxj6ktus1wg/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxj6ktus1wg/)

- **Faithful contribution:** Reports good Qwen3.8-27B coding on a 4090 with ninfer at about 250K context, contrasting earlier unusable windows, repeated new sessions and degrading compaction. Believes a3090 implementation exists and suggests searching for it.
- **Type:** runtime/context improvement report
- **Why relevant (assessment):** Concrete24GB positive report, in tension with the negative4090/ninfer .NET/Java report in C454.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What weight/KV precision, actual occupied context, tasks, speed, memory/offload and exact 3090 compatibility support the account?
- **Transferability (inference):** Test the runtime on representative tasks; similar VRAM/context claims do not explain divergent quality or guarantee 3090 fit/speed.
- **Themes:** runtime, hardware, context, harness, workflow, methodology

<a id="c481"></a>

### C481 — u/mamjazzo

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxj83ew5ggz/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxj83ew5ggz/)

- **Faithful contribution:** Reports GPT-OSS20B doing well on16GB VRAM.
- **Type:** adjacent alternative setup report
- **Why relevant (assessment):** Concrete alternative/memory point but unspecified task or quant.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** What quant, runtime, hardware, context and coding tasks support 'pretty good'?
- **Transferability (inference):** Different model/task evidence is only a candidate alternative, not a demonstrated replacement for autonomous Qwen27B coding.
- **Themes:** alternatives, hardware, weights, methodology

<a id="c482"></a>

### C482 — u/darksteelsteed

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxjhyyyc49w/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxjhyyyc49w/)

- **Faithful contribution:** Claims Claude-oriented harness context can overwhelm a local model, recommends Pi/OMP/OpenCode and says using the wrong Qwen3.8 template was the main cause of their own initial failures.
- **Type:** template failure anecdote and harness advice
- **Why relevant (assessment):** Specific firsthand template-correction lead amid broader unsupported harness claims.
- **Evidence quality:** E1 vague first-person
- **Open questions / verification gaps:** Which exact template/runtime/model versions failed and succeeded; what prompt/token overhead was measured in the Claude harness?
- **Transferability (inference):** Verify rendered chat/tool templates and context size; the template anecdote does not establish that all Claude harness use breaks local models.
- **Themes:** template, harness, context, runtime, methodology

<a id="c483"></a>

### C483 — u/filliravaz

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxjldv1zzc0/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxjldv1zzc0/)

- **Faithful contribution:** Reports a security-focused Qwen3.8-27B variant working efficiently and approaching, though not matching, frontier quality through OpenCode. Believes the model needs a specific Jinja template and says correct temperatures/penalties strongly affect output.
- **Type:** domain-variant report and configuration advice
- **Why relevant (assessment):** Relevant template/sampling/harness lead, but a specialized variant and unspecified security tasks limit direct comparison.
- **Evidence quality:** E2 setup-specific first-person, not independently verified
- **Open questions / verification gaps:** Which variant/quant, hardware, template, sampling values and evaluated tasks support the claims; was a wrong-template comparison performed?
- **Transferability (inference):** Specialized security-model experience does not establish general coding parity; test exact templates and settings rather than treating the believed requirement as independently verified.
- **Themes:** alternatives, knowledge, harness, template, sampling, methodology

<a id="c485"></a>

### C485 — u/KnavishlyUncommon

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwjv7pf3jxg/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwjv7pf3jxg/)

- **Faithful contribution:** Asks which backend is being used; claims backend choice can determine agent behavior before model capability matters.
- **Type:** diagnostic question
- **Why relevant (assessment):** High: identifies an uncontrolled runtime variable.
- **Evidence quality:** E0
- **Open questions / verification gaps:** What backend are you running it through?; No comparative backend evidence supplied.
- **Transferability (inference):** Backend should be recorded in comparisons; no particular engine advantage established.
- **Themes:** runtime, harness, methodology

<a id="c486"></a>

### C486 — u/Major-Creative

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwjy0nkveeb/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwjy0nkveeb/)

- **Faithful contribution:** OP reports using Ollama for inference and still experimenting without a settled harness.
- **Type:** OP setup disclosure
- **Why relevant (assessment):** High: direct configuration disclosure, not a diagnosis.
- **Evidence quality:** E2
- **Open questions / verification gaps:** Which harnesses and versions were actually tested?; Ollama version, flags, model artifact and context allocation remain unspecified.
- **Transferability (inference):** Applies to this reported stack only; cannot attribute failures to Ollama from disclosure alone.
- **Themes:** runtime, harness

<a id="c487"></a>

### C487 — u/vogelvogelvogelvogel

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk3367s2hw/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk3367s2hw/)

- **Faithful contribution:** Recommends llama.cpp, speculative-decoding experiments and Pi instead of context-heavy Claude Code; asserts 27B benchmarks trail Sonnet 5.5 by roughly two versions and questions whether a single 3090 forces Q4.
- **Type:** recommendation and capability dissent
- **Why relevant (assessment):** High: runtime, harness, context and quantization hypotheses, mixed with disparagement.
- **Evidence quality:** E0
- **Open questions / verification gaps:** Which speculative-decoding configuration, quant and benchmark support the advice?; Actual single-3090 quant is not established.
- **Transferability (inference):** Test engine and harness independently; neither the benchmark ranking nor mandatory Q4 follows from this comment.
- **Themes:** runtime, harness, context, weights, hardware, alternatives, methodology

<a id="c488"></a>

### C488 — u/Ratiofarming

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk51wh0xic/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk51wh0xic/)

- **Faithful contribution:** Asks which tools/harnesses OP is currently using; the standalone wording does not identify the referent.
- **Type:** clarification question
- **Why relevant (assessment):** Medium: requests missing configuration detail.
- **Evidence quality:** E0
- **Open questions / verification gaps:** Okay, but which ones are you currently using?; Parent linkage is absent; exact referent unresolved.
- **Transferability (inference):** Preserve as a configuration question, not evidence about any tool.
- **Themes:** harness, methodology

<a id="c489"></a>

### C489 — u/Potential-Leg-639

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk6fpsmmch/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk6fpsmmch/)

- **Faithful contribution:** Rejects Ollama, recommends llama.cpp or adding 32GB RAM for Strata with Qwen3.8-Flash-Next, predicts about 100 tokens/s generation and 2000 tokens/s prefill; suggests vLLM and another 3090 for concurrent users.
- **Type:** runtime/hardware recommendation
- **Why relevant (assessment):** High: concrete alternative and performance predictions, not measured results.
- **Evidence quality:** E0
- **Open questions / verification gaps:** What exact quant, hardware, context and batch size produce the predicted rates?; How does Strata concurrency compare with vLLM under matched conditions?
- **Transferability (inference):** The suggested MoE model/engine is a different stack; speeds and concurrency cannot be transferred to dense 27B or a single 3090.
- **Themes:** runtime, hardware, alternatives, economics

<a id="c490"></a>

### C490 — u/Perfect-Campaign9551

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk6tmw9bj4/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk6tmw9bj4/)

- **Faithful contribution:** Dismisses Ollama and recommends llama.cpp or Strata without technical justification.
- **Type:** unsupported runtime recommendation
- **Why relevant (assessment):** Medium: weak but actionable runtime dissent.
- **Evidence quality:** E0
- **Open questions / verification gaps:** Which failure mechanism is being alleged?; Does Strata support the target model architecture?
- **Transferability (inference):** Candidate engines require compatibility checks; no demonstrated quality difference.
- **Themes:** runtime, alternatives

<a id="c491"></a>

### C491 — u/UraidDiag

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk7g768nfm/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk7g768nfm/)

- **Faithful contribution:** Reports building an entire app with what they call the same model on a MacBook Pro M5pro with 48GB; sometimes slow and under memory pressure but without OP-like failures; suspects insufficient VRAM and suggests a smaller model.
- **Type:** setup-specific firsthand report and hypothesis
- **Why relevant (assessment):** High: counterexample with different memory architecture.
- **Evidence quality:** E2
- **Open questions / verification gaps:** What exact model, quant, backend, harness and app were used?; Does OP actually exceed available memory?
- **Transferability (inference):** Different unified-memory hardware is not a matched replication; memory-pressure diagnosis remains speculative.
- **Themes:** hardware, weights, workflow, alternatives

<a id="c492"></a>

### C492 — u/overand

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlob09glnk/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlob09glnk/)

- **Faithful contribution:** Asserts a Q4_K_M quant would fit on OP’s GPU.
- **Type:** capacity counterclaim
- **Why relevant (assessment):** High: challenges blanket insufficient-VRAM diagnosis.
- **Evidence quality:** E0
- **Open questions / verification gaps:** What are the weight size, KV cache size, context and runtime overhead?
- **Transferability (inference):** Weight fit alone does not demonstrate whole-stack fit or quality at the requested context.
- **Themes:** weights, kv, context, hardware

<a id="c493"></a>

### C493 — u/vimaillig

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk9emyeu91/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk9emyeu91/)

- **Faithful contribution:** Asks which harness OP is testing; reports early satisfactory results on a 5090 using Unsloth and OpenCode and/or Pi.
- **Type:** setup-specific firsthand report and question
- **Why relevant (assessment):** High: harness-related counterexample with named GPU and tools.
- **Evidence quality:** E2
- **Open questions / verification gaps:** Which harness are you experimenting with?; Which exact model, quant, context, tasks and Unsloth component are involved?
- **Transferability (inference):** Named stack is a useful comparison candidate, not equivalent to a 3090 setup.
- **Themes:** hardware, runtime, harness, workflow

<a id="c495"></a>

### C495 — u/Prudent-Ad4509

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkwdf70hb5/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkwdf70hb5/)

- **Faithful contribution:** Reports experimenting with 27B on 8×3090 for about four agents at native precision and using OpenCode; claims 2×3090 enables acceptable lower-precision one/two-agent use, while one card is mainly useful for exploratory debugging. Recommends hosted subscriptions instead of hardware upgrades to save money.
- **Type:** setup-specific firsthand report and economic recommendation
- **Why relevant (assessment):** High: precision/concurrency claims and cost tradeoff.
- **Evidence quality:** E2
- **Open questions / verification gaps:** What exact model, precision, context and per-agent throughput were measured?; Were 2-GPU claims tested or projected?; Which usage and hardware costs underlie the subscription recommendation?
- **Transferability (inference):** Eight-GPU observations do not establish a two-GPU minimum for useful code; economics depend on workload and existing equipment.
- **Themes:** hardware, weights, context, harness, workflow, economics, alternatives

<a id="c497"></a>

### C497 — u/Un4giv3n-madmonk

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkd63t65k3/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkd63t65k3/)

- **Faithful contribution:** Reports barely noticing a difference between Opus 5.5, Sonnet and 27B on straight coding tasks.
- **Type:** vague firsthand capability comparison
- **Why relevant (assessment):** High: direct dissent to a large coding-capability gap.
- **Evidence quality:** E1
- **Open questions / verification gaps:** What tasks, prompts, artifacts, harness and success criteria were compared?
- **Transferability (inference):** Unspecified straight coding is not necessarily autonomous repository work; no general parity established.
- **Themes:** workflow, alternatives, methodology

<a id="c499"></a>

### C499 — u/zanar97862

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmsi25di8z/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmsi25di8z/)

- **Faithful contribution:** Challenges a Strata recommendation by asserting Strata is not a dense-model engine.
- **Type:** technical compatibility dissent
- **Why relevant (assessment):** High: potentially invalidates dense-27B engine advice.
- **Evidence quality:** E0
- **Open questions / verification gaps:** What model architectures and Strata version are supported?
- **Transferability (inference):** Verify architecture compatibility before transferring MoE engine recommendations to dense 27B.
- **Themes:** runtime, alternatives

<a id="c500"></a>

### C500 — u/PituSmart

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwuut4ni0m9/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwuut4ni0m9/)

- **Faithful contribution:** States Strata is for MoE inference.
- **Type:** technical compatibility clarification
- **Why relevant (assessment):** High: reinforces dense-versus-MoE distinction.
- **Evidence quality:** E0
- **Open questions / verification gaps:** Which architectures and version does this statement cover?
- **Transferability (inference):** Not evidence that switching dense 27B directly to Strata is supported.
- **Themes:** runtime, alternatives

<a id="c501"></a>

### C501 — u/zanar97862

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwwbpudoiw0/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwwbpudoiw0/)

- **Faithful contribution:** Agrees with the architecture distinction and expresses interest in dense-model optimizations.
- **Type:** technical feature wish
- **Why relevant (assessment):** Low: retains an explicit technical extension request.
- **Evidence quality:** E0
- **Open questions / verification gaps:** Are dense-model optimizations planned or available?
- **Transferability (inference):** A wish is not evidence of existing support or performance.
- **Themes:** runtime, alternatives

<a id="c504"></a>

### C504 — u/Dinth

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx5jezc0syr/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx5jezc0syr/)

- **Faithful contribution:** Asks whether recent versions have returned to mainline llama.cpp; product referent is unstated in the isolated comment.
- **Type:** runtime-version question
- **Why relevant (assessment):** High: challenges potentially stale backend criticism.
- **Evidence quality:** E0
- **Open questions / verification gaps:** Haven’t they gone back to mainline llama.cpp in the latest versions?; Which product, release and backend commit?
- **Transferability (inference):** Version-specific verification is needed; question does not establish that the switch occurred.
- **Themes:** runtime, methodology

<a id="c505"></a>

### C505 — u/FMAGF

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpkegv7sf9/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpkegv7sf9/)

- **Faithful contribution:** Asks whether Ollama is suitable for ordinary text generation and reasoning.
- **Type:** technical scope question
- **Why relevant (assessment):** Medium: separates plain inference from agentic use.
- **Evidence quality:** E0
- **Open questions / verification gaps:** Is Ollama fine for regular text generation and reasoning?
- **Transferability (inference):** Backend suitability may depend on workload; no answer is established by the question.
- **Themes:** runtime, reasoning, workflow

<a id="c506"></a>

### C506 — u/Smooth-Television-48

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwry23bgfqc/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwry23bgfqc/)

- **Faithful contribution:** Answers that Ollama is fine but may be slower and recommends Unsloth as an easy click-to-run integrated option.
- **Type:** runtime recommendation and qualification
- **Why relevant (assessment):** Medium: counters categorical Ollama rejection.
- **Evidence quality:** E0
- **Open questions / verification gaps:** Slower than what, on which model and settings?; Which Unsloth application/version is meant?
- **Transferability (inference):** No controlled speed or quality comparison supplied.
- **Themes:** runtime, workflow, alternatives

<a id="c507"></a>

### C507 — u/infiniti306

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwztp1spfhc/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwztp1spfhc/)

- **Faithful contribution:** Reports installing Ollama with Qwen 3 14B two days earlier and asks whether to switch.
- **Type:** setup disclosure and migration question
- **Why relevant (assessment):** Medium: practical migration question for a different model.
- **Evidence quality:** E2
- **Open questions / verification gaps:** Should I switch too?; What hardware, use case and problems motivate a switch?
- **Transferability (inference):** Different 14B model and unspecified hardware; cannot infer a need to migrate.
- **Themes:** runtime, weights, alternatives

<a id="c508"></a>

### C508 — u/sebt3

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx0famuazz9/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx0famuazz9/)

- **Faithful contribution:** Recommends Strata if RAM is sufficient, otherwise llama.cpp with a newer model; dismisses Qwen3 as outdated.
- **Type:** unsupported runtime/model recommendation
- **Why relevant (assessment):** Medium: proposes alternatives but offers no measurements.
- **Evidence quality:** E0
- **Open questions / verification gaps:** What hardware and RAM are available?; Which newer compatible model and task evaluation support the recommendation?
- **Transferability (inference):** Model-family age is not a measured task result; Strata advice needs architecture compatibility.
- **Themes:** runtime, hardware, weights, alternatives

<a id="c509"></a>

### C509 — u/username8914

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwo4qvtzqn5/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwo4qvtzqn5/)

- **Faithful contribution:** Counters blanket Ollama criticism, claiming it exposes llama.cpp and vLLM tuning while not supporting Strata; characterizes it as beginner-friendly.
- **Type:** technical dissent
- **Why relevant (assessment):** High: disputes engine-versus-wrapper diagnosis.
- **Evidence quality:** E0
- **Open questions / verification gaps:** Which Ollama versions expose which llama.cpp/vLLM settings?; Are identical artifacts, templates and parameters obtainable?
- **Transferability (inference):** API/parameter parity must be checked; no matched output comparison supplied.
- **Themes:** runtime, sampling, workflow, methodology

<a id="c510"></a>

### C510 — u/united_we_ride

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwulk0cza8x/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwulk0cza8x/)

- **Faithful contribution:** Says engine choice depends on hardware; lists llama.cpp/Unsloth Studio or vLLM, and Unsloth Desktop/Studio or Open WebUI for interfaces. Recommends Unsloth Studio for integrated tools, terminal access, skills and image generation, claiming it works better than Ollama.
- **Type:** software-stack recommendation
- **Why relevant (assessment):** Medium: names integration alternatives and separates engine/UI imperfectly.
- **Evidence quality:** E0
- **Open questions / verification gaps:** Which backend does each interface actually use in the relevant version?; What comparison supports better behavior?
- **Transferability (inference):** Feature convenience does not establish higher coding accuracy; verify backend/interface boundaries.
- **Themes:** runtime, harness, workflow, alternatives

<a id="c511"></a>

### C511 — u/External-Fun-8563

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwurn9zcxb6/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwurn9zcxb6/)

- **Faithful contribution:** Asks whether LM Studio is a good option or whether a newcomer wanting a decent UI should move directly to Unsloth.
- **Type:** UI/runtime selection question
- **Why relevant (assessment):** Medium: practical alternative-selection question.
- **Evidence quality:** E0
- **Open questions / verification gaps:** Is LM Studio not a good option?; Should I jump to Unsloth immediately for a decent UI?
- **Transferability (inference):** No quality deficiency in LM Studio is established by asking.
- **Themes:** runtime, workflow, alternatives

<a id="c512"></a>

### C512 — u/CLG-Rampage

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwv4uwdud2b/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwv4uwdud2b/)

- **Faithful contribution:** Claims LM Studio is acceptable but generally trails Unsloth in features and current llama.cpp versions.
- **Type:** version/feature comparison claim
- **Why relevant (assessment):** Medium: potential version-lag hypothesis.
- **Evidence quality:** E0
- **Open questions / verification gaps:** Which releases, features and backend commits were compared?
- **Transferability (inference):** Version lag is release-specific and not by itself proof of a coding-quality gap.
- **Themes:** runtime, alternatives, methodology

<a id="c513"></a>

### C513 — u/united_we_ride

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwv8cg3van7/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwv8cg3van7/)

- **Faithful contribution:** Reports moving from LM Studio to Open WebUI and then Unsloth; recommends Unsloth Desktop for a self-contained GUI or Studio for a web UI, citing broader features including image generation.
- **Type:** vague firsthand tool migration
- **Why relevant (assessment):** Medium: usable UI/workflow comparison, not a model test.
- **Evidence quality:** E1
- **Open questions / verification gaps:** Which releases and features mattered to coding outcomes?
- **Transferability (inference):** Personal interface preference does not establish improved model reasoning.
- **Themes:** runtime, workflow, alternatives

<a id="c514"></a>

### C514 — u/rororo99

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx5y2sew0x1/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx5y2sew0x1/)

- **Faithful contribution:** Asks what is wrong with Ollama and which solution is better.
- **Type:** technical justification question
- **Why relevant (assessment):** High: requests evidence behind categorical recommendations.
- **Evidence quality:** E0
- **Open questions / verification gaps:** What is bad about Ollama and what is a better solution?
- **Transferability (inference):** Requires a concrete failure mechanism and matched alternative, not popularity claims.
- **Themes:** runtime, alternatives, methodology

<a id="c515"></a>

### C515 — u/Repulsive_Initial308

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx62innfxk5/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx62innfxk5/)

- **Faithful contribution:** Claims most people try LM Studio after Ollama.
- **Type:** unsupported adoption/alternative claim
- **Why relevant (assessment):** Low: names an alternative without technical comparison.
- **Evidence quality:** E0
- **Open questions / verification gaps:** What evidence supports the adoption claim?; Does LM Studio solve the reported failure?
- **Transferability (inference):** Popularity, even if verified, would not imply coding-quality improvement.
- **Themes:** runtime, alternatives

<a id="c516"></a>

### C516 — u/rororo99

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx70cz1u0f6/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx70cz1u0f6/)

- **Faithful contribution:** Asks why migration is needed and reports Ollama with Open WebUI and OpenCode works fine.
- **Type:** stack-specific firsthand dissent
- **Why relevant (assessment):** High: counterexample to universal Ollama failure.
- **Evidence quality:** E2
- **Open questions / verification gaps:** But why?; Which model, hardware, context, tasks and runtime versions work fine?
- **Transferability (inference):** Named applications help reproduce the workflow, but absent model/hardware details limit comparison.
- **Themes:** runtime, harness, workflow, methodology

<a id="c517"></a>

### C517 — u/USArmy68Whiskey

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk00ddx8kh/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk00ddx8kh/)

- **Faithful contribution:** Reports disappointment using Qwen3.8 Flash even compared with GPT Luna; argues consumer-feasible local models remain weaker than lower-end frontier models and expectations from stronger models amplify the gap.
- **Type:** vague firsthand capability dissent
- **Why relevant (assessment):** High: model-capability alternative to setup-only explanations.
- **Evidence quality:** E1
- **Open questions / verification gaps:** What tasks, model artifact, quant, hardware and harness were compared?
- **Transferability (inference):** Flash is not necessarily dense 27B; broad local-versus-cloud conclusions exceed the report.
- **Themes:** weights, alternatives, hardware, workflow

<a id="c518"></a>

### C518 — u/575_Inverse

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkf2lzf7hg/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkf2lzf7hg/)

- **Faithful contribution:** Argues Qwen3.8-27B is not weak and that operator expertise is the only issue.
- **Type:** unsupported capability counterclaim
- **Why relevant (assessment):** High: explicit setup-only dissent.
- **Evidence quality:** E0
- **Open questions / verification gaps:** Which working configuration and matched tasks support an expertise-only explanation?
- **Transferability (inference):** No evidence excludes intrinsic capability limitations.
- **Themes:** workflow, methodology

<a id="c519"></a>

### C519 — u/USArmy68Whiskey

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkxs8hejdu/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkxs8hejdu/)

- **Faithful contribution:** Argues weaker models can work with constant guidance but better models need substantially less hand-holding.
- **Type:** workflow/capability counterclaim
- **Why relevant (assessment):** High: distinguishes assisted success from autonomy.
- **Evidence quality:** E0
- **Open questions / verification gaps:** How much intervention is required on matched tasks?
- **Transferability (inference):** Track human intervention separately from eventual task completion.
- **Themes:** workflow, harness, methodology

<a id="c520"></a>

### C520 — u/575_Inverse

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmudwmu84i/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmudwmu84i/)

- **Faithful contribution:** Asks whether the other user tells a model how an implementation should work and why.
- **Type:** workflow question
- **Why relevant (assessment):** Medium: surfaces disagreement about normal guidance versus hand-holding.
- **Evidence quality:** E0
- **Open questions / verification gaps:** Don’t you at least tell your model how you want something implemented and why?
- **Transferability (inference):** Define prompt specificity and permitted human input before comparing autonomy.
- **Themes:** workflow, methodology

<a id="c521"></a>

### C521 — u/KinkyMonitorLizard

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkaiqo84v9/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkaiqo84v9/)

- **Faithful contribution:** Claims medium reasoning effort causes poor results on an unspecified model and recommends none, low or xhigh.
- **Type:** reasoning-setting recommendation
- **Why relevant (assessment):** High: a proposed setting-dependent failure explanation.
- **Evidence quality:** E0
- **Open questions / verification gaps:** Which model and harness implement these effort levels?; What results demonstrate a medium-specific failure?
- **Transferability (inference):** Do not map these labels onto dense Qwen or Sonnet without establishing the actual referent and implementation.
- **Themes:** reasoning, sampling, harness, methodology

<a id="c522"></a>

### C522 — u/SkiBikeDad

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwl0q0ncqzo/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwl0q0ncqzo/)

- **Faithful contribution:** Counters the medium-effort warning, saying later benchmarks show medium is a useful middle ground between low and xhigh.
- **Type:** benchmark counterclaim
- **Why relevant (assessment):** High: directly disputes an effort-level diagnosis.
- **Evidence quality:** E0
- **Open questions / verification gaps:** Which model, benchmarks and versions support this?
- **Transferability (inference):** Uncited benchmarks do not settle the medium-effort question or establish model identity.
- **Themes:** reasoning, methodology

<a id="c524"></a>

### C524 — u/sudden_aggression

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpfw0i75pc/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpfw0i75pc/)

- **Faithful contribution:** Reports medium effort is fine in their experience and that excessive cache quantization hurts reasoning strength.
- **Type:** vague firsthand setting report
- **Why relevant (assessment):** High: distinguishes effort labels from KV precision.
- **Evidence quality:** E1
- **Open questions / verification gaps:** Which model, K/V types and tasks were compared?; Was cache precision changed independently of context and weights?
- **Transferability (inference):** Treat KV precision as a testable confound, not a universal effect from this unquantified report.
- **Themes:** reasoning, kv, methodology

<a id="c525"></a>

### C525 — u/PatienceSweaty33

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2jgoow8f6/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx2jgoow8f6/)

- **Faithful contribution:** Claims values can tolerate precision below Q8/INT8 but keys should be kept as high precision as the GPU allows.
- **Type:** KV precision recommendation
- **Why relevant (assessment):** High: proposes asymmetric K/V settings.
- **Evidence quality:** E0
- **Open questions / verification gaps:** Which model architecture, context and precision combinations were tested?
- **Transferability (inference):** Model-specific K/V sensitivity must be measured; no blanket safe value precision established.
- **Themes:** kv, hardware, reasoning

<a id="c528"></a>

### C528 — u/Ratiofarming

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx66wcn6c9s/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx66wcn6c9s/)

- **Faithful contribution:** Claims Claude or ChatGPT make finding setup information and configuring LLMs nearly trivial.
- **Type:** AI-assisted setup recommendation
- **Why relevant (assessment):** Medium: workflow alternative to manual configuration research.
- **Evidence quality:** E0
- **Open questions / verification gaps:** What setup was validated, and how were generated settings checked?
- **Transferability (inference):** AI can aid configuration research, but generated advice still requires runtime validation.
- **Themes:** workflow, methodology, alternatives

<a id="c529"></a>

### C529 — u/superbiche

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm9b6w4kv9/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm9b6w4kv9/)

- **Faithful contribution:** Praises QFN and calls 27B usable, while questioning single-24GB-GPU expectations at 120k context and asking how many users share the rig.
- **Type:** capacity/concurrency challenge
- **Why relevant (assessment):** High: identifies concurrency as another missing variable.
- **Evidence quality:** E0
- **Open questions / verification gaps:** How many people are trying to use the rig?; What does QFN refer to exactly, and what context is actually allocated/used?
- **Transferability (inference):** Per-user context and concurrency should be measured; does not prove the rig is inadequate for one user.
- **Themes:** hardware, context, runtime, alternatives

<a id="c530"></a>

### C530 — u/_RemyLeBeau_

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmlq4ecja8/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmlq4ecja8/)

- **Faithful contribution:** Requests a Hugging Face link to the model under discussion.
- **Type:** model-identity question
- **Why relevant (assessment):** Medium: asks for a reproducible artifact.
- **Evidence quality:** E0
- **Open questions / verification gaps:** Do you have an HF link?; Which model does the unstated referent identify?
- **Transferability (inference):** Artifact identity is necessary before transferring claims; no model can be inferred from this question alone.
- **Themes:** weights, alternatives, methodology

<a id="c531"></a>

### C531 — u/MarcusAurelius68

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwrubhbxy8z/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwrubhbxy8z/)

- **Faithful contribution:** Reports using Radiance with 2×R9700 and suggests it or Strata.
- **Type:** setup-specific serving-tool report
- **Why relevant (assessment):** Medium: names an alternative serving setup.
- **Evidence quality:** E2
- **Open questions / verification gaps:** Which model, quant, context and Radiance version are used?; What quality or speed was achieved?
- **Transferability (inference):** Different GPU pair and unknown model prevent equivalence with OP’s dense-27B setup.
- **Themes:** runtime, hardware, alternatives

<a id="c532"></a>

### C532 — u/_RemyLeBeau_

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwzbb89p7dw/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwzbb89p7dw/)

- **Faithful contribution:** Clarifies that Strata is an inference provider rather than a model, and that comparing QFN with 27B requires identifying the actual model.
- **Type:** model/runtime distinction
- **Why relevant (assessment):** High: prevents conflating a runtime with a model artifact.
- **Evidence quality:** E0
- **Open questions / verification gaps:** Which model is meant by QFN?
- **Transferability (inference):** Separate model, quant and runtime in every comparison.
- **Themes:** runtime, weights, alternatives, methodology

<a id="c533"></a>

### C533 — u/sinan_online

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmz7d2r8o2/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmz7d2r8o2/)

- **Faithful contribution:** Says harness choice is probably most important and recommends dev.pi based on favorable reports, explicitly without personal use.
- **Type:** hearsay harness recommendation
- **Why relevant (assessment):** High: salient diagnostic hypothesis with explicit non-use disclosure.
- **Evidence quality:** E0
- **Open questions / verification gaps:** Which harness is OP using?; What direct evidence supports the recommendation?
- **Transferability (inference):** Hearsay suggests a candidate test, not demonstrated superiority.
- **Themes:** harness, workflow, alternatives

<a id="c534"></a>

### C534 — u/Plastic-Stress-6468

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkglagel5x/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkglagel5x/)

- **Faithful contribution:** Claims 27B at 128k context on 24GB is severely degraded; recommends unquantized KV, at least Q8 weights and about 96GB pooled VRAM for concurrency.
- **Type:** precision/capacity recommendation
- **Why relevant (assessment):** High: explicit weights/KV/context hypothesis and hardware target.
- **Evidence quality:** E0
- **Open questions / verification gaps:** What actual weight/KV precision is OP using?; What matched results justify Q8 minimum, unquantized cache or 96GB?
- **Transferability (inference):** Capacity targets depend on context and concurrent slots; asserted quality minima are not verified.
- **Themes:** hardware, weights, kv, context, runtime

<a id="c535"></a>

### C535 — u/MainWrangler988

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkteq5edut/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkteq5edut/)

- **Faithful contribution:** Claims the local model exceeds a five-year-old LLM but that no local model is worth the time.
- **Type:** broad capability/economic dissent
- **Why relevant (assessment):** Low: substantive negative utility judgment without detail.
- **Evidence quality:** E0
- **Open questions / verification gaps:** Which models, tasks and time costs support this?
- **Transferability (inference):** No general local-model utility conclusion can be drawn.
- **Themes:** alternatives, economics, workflow

<a id="c537"></a>

### C537 — u/FragmentedHeap

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwr4wm38ote/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwr4wm38ote/)

- **Faithful contribution:** Claims using Claude is necessary to research the rapidly changing local-model ecosystem fast enough.
- **Type:** AI-assisted research recommendation
- **Why relevant (assessment):** Low: setup-workflow argument with absolute unsupported wording.
- **Evidence quality:** E0
- **Open questions / verification gaps:** What research task and accuracy standard were used?; Why would other information sources be insufficient?
- **Transferability (inference):** AI-assisted research may reduce effort, but necessity is not demonstrated.
- **Themes:** workflow, methodology, alternatives

<a id="c538"></a>

### C538 — u/Connect_Ad791

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwrfqkc3ezl/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwrfqkc3ezl/)

- **Faithful contribution:** Says local models do not refuse their nefarious code requests; no task or model is identified.
- **Type:** vague firsthand refusal-policy claim
- **Why relevant (assessment):** Low: an alternative use-case preference, not coding-accuracy evidence.
- **Evidence quality:** E1
- **Open questions / verification gaps:** Which model and request types were tested?
- **Transferability (inference):** Refusal behavior is distinct from coding correctness and autonomy; no cross-model generalization warranted.
- **Themes:** workflow, alternatives

<a id="c539"></a>

### C539 — u/FragmentedHeap

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwruisar4ps/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwruisar4ps/)

- **Faithful contribution:** Reports Claude built their uncensored Qwen3.8 Flash Next stack without refusing, and claims Claude can help build reverse-engineering engines even when declining to perform reverse engineering directly.
- **Type:** vague firsthand setup/refusal report
- **Why relevant (assessment):** Medium: cloud-assisted local stack construction and policy distinction.
- **Evidence quality:** E1
- **Open questions / verification gaps:** What exact stack and deliverables were built and verified?; Which refusal/assistance examples are reproducible?
- **Transferability (inference):** A reported successful setup is not evidence of unrestricted local capability or general provider policy.
- **Themes:** workflow, harness, alternatives

<a id="c540"></a>

### C540 — u/Connect_Ad791

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwu8lsmz89w/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwu8lsmz89w/)

- **Faithful contribution:** Asks which uncensored model is used and whether it is good; reports finding many poor quants before finding a good one and worries about wasted time.
- **Type:** model-identity question and vague firsthand quant report
- **Why relevant (assessment):** Medium: requests artifact identity and quality evidence.
- **Evidence quality:** E1
- **Open questions / verification gaps:** What uncensored model are you using?; Is it good?; Which quants were poor or good, and by what tests?
- **Transferability (inference):** Anecdotal quant-quality variation lacks artifact/version controls.
- **Themes:** weights, alternatives, methodology

<a id="c541"></a>

### C541 — u/FragmentedHeap

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwuy5osbr8g/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwuy5osbr8g/)

- **Faithful contribution:** Reports orcarouter/Qwen3.8-Flash-Next-Uncensored IQ4S via Strata on R9700 32GB, 128GB RAM, 7950X and 2TB NVMe: about 70 tokens/s with concurrency and nearly 3000 tokens/s prefill. Says a Tetris task took 2–3h versus Opus 5.5’s 20min. Predicts 2×R9700 can serve 4–8 sessions at 65 tokens/s each; recommends more RAM, CPU/cache/bandwidth and gives unverified GPU rankings and prices.
- **Type:** setup-specific firsthand performance report with projections
- **Why relevant (assessment):** High: detailed alternative stack, latency and hardware claims.
- **Evidence quality:** E2
- **Open questions / verification gaps:** What exact context, concurrent request count, versions, cache sizes and measurement method produced the reported rates?; Was the dual-GPU 4–8-session result measured or projected?; Was Tetris judged with identical prompts and acceptance tests?; CPU feature requirements, GPU rankings and dollar prices are not independently verified.
- **Transferability (inference):** A different MoE model and hardware stack; reported decode rate does not imply equal end-to-end coding speed, as the Tetris anecdote itself suggests.
- **Themes:** runtime, weights, hardware, context, workflow, reasoning, economics, alternatives, methodology

<a id="c544"></a>

### C544 — u/Badger-Purple

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm5vk1sujp/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm5vk1sujp/)

- **Faithful contribution:** Questions using 24GB for dense 27B and low precision at 128k; asserts half-precision weights occupy at least 27GB and speculates Sonnet 5.5 has hundreds of billions of parameters and higher serving precision.
- **Type:** capacity/capability challenge
- **Why relevant (assessment):** High: precision-memory concern, mixed with unsupported model-size speculation.
- **Evidence quality:** E0
- **Open questions / verification gaps:** What are the real artifact size, precision, cache allocation and offload?; The stated half-precision size is imprecise: 27B parameters at two bytes is about 54GB before overhead.; Sonnet parameter count and serving precision are not verified here.
- **Transferability (inference):** Use actual byte accounting rather than speculative frontier size; the comment alone does not prove harmful quantization.
- **Themes:** hardware, weights, kv, context, alternatives

<a id="c545"></a>

### C545 — u/JMowery

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwn2cj1wgww/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwn2cj1wgww/)

- **Faithful contribution:** Reports complex reverse engineering and coding working, sometimes after retries, and attributes OP’s problem to execution/setup.
- **Type:** vague firsthand capability counterexample
- **Why relevant (assessment):** High: reports eventual success but unspecified conditions.
- **Evidence quality:** E1
- **Open questions / verification gaps:** Which model artifact, hardware, harness, tasks and retry count?
- **Transferability (inference):** Eventual success with retries is not proof of autonomous first-pass performance or an OP misconfiguration.
- **Themes:** workflow, alternatives, methodology

<a id="c548"></a>

### C548 — u/Appropriate-Fun-3313

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwvt19fx86d/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwvt19fx86d/)

- **Faithful contribution:** Doubts that the referenced model can run on the stated specifications.
- **Type:** hardware feasibility dissent
- **Why relevant (assessment):** Medium: technical skepticism, though the model/spec referent is missing.
- **Evidence quality:** E0
- **Open questions / verification gaps:** Which model, quant and hardware are being challenged?; Is RAM/expert offload being considered?
- **Transferability (inference):** Do not convert a skeptical assertion into a capacity fact without identifying the stack.
- **Themes:** hardware, weights, runtime

<a id="c549"></a>

### C549 — u/Hypnonotic

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwwct3qz89x/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwwct3qz89x/)

- **Faithful contribution:** Recommends looking up Strata and claims it puts more model data in RAM than VRAM.
- **Type:** runtime memory-placement explanation
- **Why relevant (assessment):** High: counters GPU-only fit assumptions for an alternative engine.
- **Evidence quality:** E0
- **Open questions / verification gaps:** Which architecture and allocation policy are meant?
- **Transferability (inference):** RAM offload may change fit and speed; does not establish dense-27B support or a measured throughput.
- **Themes:** runtime, hardware, weights

<a id="c550"></a>

### C550 — u/Appropriate-Fun-3313

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwwl7a4j1k0/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwwl7a4j1k0/)

- **Faithful contribution:** Reports that running a 70B model is impractical on their allegedly better, unspecified hardware and predicts the disputed setup would be very slow even if it loads.
- **Type:** vague firsthand performance dissent
- **Why relevant (assessment):** Medium: emphasizes loading versus usable speed.
- **Evidence quality:** E1
- **Open questions / verification gaps:** What hardware, model architecture, runtime, quant and throughput were tested?
- **Transferability (inference):** A 70B result cannot be transferred directly to a sparse MoE stack.
- **Themes:** hardware, runtime, weights, alternatives

<a id="c551"></a>

### C551 — u/Hypnonotic

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwx6nm5b82p/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwx6nm5b82p/)

- **Faithful contribution:** Claims Strata keeps frequently used experts on GPU with remaining model data in RAM; recommends 64GB RAM/16GB VRAM for effective operation and calls 32GB/12GB the minimum.
- **Type:** runtime explanation and capacity recommendation
- **Why relevant (assessment):** High: concrete expert-offload hypothesis and hardware thresholds.
- **Evidence quality:** E0
- **Open questions / verification gaps:** For which model, quant, context and concurrency are the thresholds valid?; What measured throughput and cache-miss behavior support effective operation?
- **Transferability (inference):** Architecture-specific expert caching is not equivalent to fitting all dense weights in VRAM; thresholds need validation.
- **Themes:** runtime, hardware, weights, context

<a id="c552"></a>

### C552 — u/Appropriate-Fun-3313

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx28ebnulcy/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx28ebnulcy/)

- **Faithful contribution:** Says claimed performance differs from their experience, remains skeptical, and intends to test Strata.
- **Type:** vague firsthand performance dissent
- **Why relevant (assessment):** Low: retains an unresolved empirical disagreement, not a test result.
- **Evidence quality:** E1
- **Open questions / verification gaps:** What previous setup and throughput were observed?; What happened after testing Strata?
- **Transferability (inference):** Intent to test supplies no confirmation; prior unspecified experience is weak counterevidence.
- **Themes:** runtime, hardware, methodology

<a id="c553"></a>

### C553 — u/Ramona00

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx7gyphvdes/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx7gyphvdes/)

- **Faithful contribution:** Reports overcoming skepticism after finding Strata unusually fast and effective on gaming hardware, without specifications.
- **Type:** vague firsthand runtime praise
- **Why relevant (assessment):** Medium: experiential counterpoint to offload skepticism.
- **Evidence quality:** E1
- **Open questions / verification gaps:** What hardware, model, quant, context and measured speeds?
- **Transferability (inference):** Qualitative praise is not a reproducible speed result or a dense-model comparison.
- **Themes:** runtime, hardware, alternatives

<a id="c554"></a>

### C554 — u/Canadian_Border_Czar

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwsqf74owip/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwsqf74owip/)

- **Faithful contribution:** Asks for response latency for a Flash Next quant on 12GB and reports better results from Qwen3.5-9B, claiming its 7GB Q5 quant and 65k context fit entirely in GPU VRAM.
- **Type:** technical question and model-specific firsthand comparison
- **Why relevant (assessment):** High: smaller fully resident model as alternative to offloaded MoE.
- **Evidence quality:** E2
- **Open questions / verification gaps:** How long does your setup take to respond even once?; Which GPU, runtime and KV precision allow the claimed 65k fit?; What tasks were better and against which Flash Next configuration?
- **Transferability (inference):** Different model and context; compare total latency and task success, not parameter count alone.
- **Themes:** hardware, weights, kv, context, runtime, alternatives, methodology

<a id="c555"></a>

### C555 — u/sudden_aggression

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpe23k5ode/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpe23k5ode/)

- **Faithful contribution:** Reports Qwen3.8-27B on R9700 32GB with Hermes: successful coding iteration after days of tuning, 300k unified cache and 256k per slot for main work plus cron, Q8_0 K/Q4_0 V, research tools, Gitea and sandbox. Says 200k works but 128k is bad, asymmetric cache improves reasoning over Q4/Q4, and 3.8 is slower but smarter than 3.6, struggling to reach 50 tokens/s. Recommends llama.cpp over Ollama.
- **Type:** setup-specific firsthand workflow/settings report
- **Why relevant (assessment):** High: detailed counterexample and context/KV hypotheses.
- **Evidence quality:** E2
- **Open questions / verification gaps:** What weight quant, actual occupied context, runtime build and slot allocation were used?; How were 128k versus 200k and Q4/Q4 versus Q8/Q4 compared?; How do 300k unified and 256k-per-slot settings interact under simultaneous jobs?; What were task success rates and human interventions?
- **Transferability (inference):** This workload favors larger windows, contrary to advice elsewhere to shrink context; neither a universal 200k minimum nor KV causal benefit is established.
- **Themes:** runtime, harness, hardware, context, kv, reasoning, workflow, methodology

<a id="c556"></a>

### C556 — u/Own-Buy8294

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpl70k6vtu/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpl70k6vtu/)

- **Faithful contribution:** Recommends an asserted $8 one-month Grok Bot subscription to inspect and configure local-model settings automatically.
- **Type:** AI-assisted setup/economic recommendation
- **Why relevant (assessment):** Medium: proposed setup assistance, no demonstrated result.
- **Evidence quality:** E0
- **Open questions / verification gaps:** Which product, price, permissions and validated configuration changes are meant?
- **Transferability (inference):** Subscription cost and automatic setup competence are unverified; not a model-quality result.
- **Themes:** workflow, alternatives, economics

<a id="c557"></a>

### C557 — u/RemainAbove

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpsu3jn2ch/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwpsu3jn2ch/)

- **Faithful contribution:** Endorses paying an asserted $20 for one month of Claude Code for setup help and says they intend to use it to move off Ollama.
- **Type:** recommendation and migration intention
- **Why relevant (assessment):** Low: not an observed successful migration.
- **Evidence quality:** E0
- **Open questions / verification gaps:** Did the migration occur, and did matched coding results improve?; Which subscription and current price are meant?
- **Transferability (inference):** Intention and willingness to pay do not establish efficacy or economics.
- **Themes:** runtime, workflow, alternatives, economics

<a id="c558"></a>

### C558 — u/FragmentedHeap

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwqwb07bcf6/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwqwb07bcf6/)

- **Faithful contribution:** Recommends dual R9700, 192GB DDR5, Strata and Qwen3.8 Flash Next instead of dense 27B, asserting quantization badly harms dense quality and MoE expert loading supports 2–8 sessions above 60 tokens/s. Prescribes fast CPU features and larger 4-GPU/Threadripper options, estimates $40k, and urges AI-assisted setup amid rapid change.
- **Type:** alternative architecture/hardware prescription
- **Why relevant (assessment):** High: concrete but largely unsupported capacity, quality and cost claims.
- **Evidence quality:** E0
- **Open questions / verification gaps:** What setup actually measured the per-session rates and at what context/quant?; What evidence establishes the asserted quantization damage and CPU feature necessity?; What market/date supports the costs and claimed imminent model release?
- **Transferability (inference):** Switches model architecture and system budget; projected results are not an upgrade guarantee for OP.
- **Themes:** hardware, runtime, weights, context, alternatives, economics, workflow

<a id="c559"></a>

### C559 — u/Iajah

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx36rin46u8/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx36rin46u8/)

- **Faithful contribution:** Claims Qwen27B can eventually complete nearly any task with more guidance than Sonnet, but guesses OP’s hardware is inadequate and a single RTX6K remains necessary.
- **Type:** capability/capacity opinion
- **Why relevant (assessment):** High: strong capability claim coexists with unverified hardware minimum.
- **Evidence quality:** E0
- **Open questions / verification gaps:** Which tasks and interventions support near-universal completion?; Which RTX6K model and configuration, and why necessary?
- **Transferability (inference):** Neither universal task success nor a hardware minimum is demonstrated.
- **Themes:** hardware, workflow, alternatives

<a id="c560"></a>

### C560 — u/NonAwesomeDude

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwrrwy12tgg/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwrrwy12tgg/)

- **Faithful contribution:** Blames the setup and expresses greater trust in Qwen27B than any Claude model, without examples.
- **Type:** subjective capability counterclaim
- **Why relevant (assessment):** Medium: weak but explicit disagreement with capability-gap explanations.
- **Evidence quality:** E0
- **Open questions / verification gaps:** What tasks, artifacts and settings support the trust judgment?
- **Transferability (inference):** Preference does not isolate setup causality or establish model superiority.
- **Themes:** workflow, alternatives, methodology

<a id="c561"></a>

### C561 — u/OkMaintenance9799

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rws8qx4b2qt/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rws8qx4b2qt/)

- **Faithful contribution:** Recommends the Niko1221/Strata repository with Qwen3.8 Flash Next.
- **Type:** alternative-stack recommendation
- **Why relevant (assessment):** Medium: explicit engine/model combination, not merely a bare link.
- **Evidence quality:** E0
- **Open questions / verification gaps:** What compatible artifact, quant, hardware and measured result?
- **Transferability (inference):** Different MoE alternative; not evidence Strata can directly serve dense 27B.
- **Themes:** runtime, weights, alternatives

<a id="c562"></a>

### C562 — u/Qorsair

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwt1tj77rmt/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwt1tj77rmt/)

- **Faithful contribution:** Reports spending about $45/month on Gemini orchestration, Claude planning and Muse adversarial review without hitting caps. Claims comparable local multi-GPU hardware breaks even only after about five years excluding power, that single-3090 quant/context compromises hurt reasoning, and recommends cloud or asserted ZDR options Deepinfra/OpenRouter.
- **Type:** firsthand cost report and economic/capability argument
- **Why relevant (assessment):** High: workload economics and specialized multi-model workflow.
- **Evidence quality:** E2
- **Open questions / verification gaps:** What usage, model tiers, prices and hardware configuration produce the five-year estimate?; What local matched-task quality and speed are required?; Are ZDR terms verified for the exact provider/model route?
- **Transferability (inference):** One user’s spend is not a general break-even; privacy terms, labor, power and existing hardware need separate accounting.
- **Themes:** economics, alternatives, workflow, reasoning, hardware, weights, context, methodology

<a id="c563"></a>

### C563 — u/kirbyfanner

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwt3enmmfmr/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwt3enmmfmr/)

- **Faithful contribution:** Reports LM Studio plus VS Code GitHub Copilot BYOK on R9700 32GB, Q6 weights, 128k context and Q8 K/V: very fast/near-instant first token but frequent failures, hallucinations and loops. Says direct LM Studio is somewhat better and asks for setup-specific advice.
- **Type:** setup-specific firsthand failure report and question
- **Why relevant (assessment):** High: important counterexample to blaming only Ollama or low K/V precision.
- **Evidence quality:** E2
- **Open questions / verification gaps:** Any tips specific to that setup?; Which model artifact, LM Studio/backend/Copilot versions and prompts?; Are templates, tool schemas, reasoning parsing and actual context identical between direct and Copilot use?
- **Transferability (inference):** Different harness and GPU; fast inference does not prove good agent behavior, and the direct-versus-harness difference warrants controlled testing.
- **Themes:** runtime, harness, weights, kv, context, hardware, workflow, methodology

<a id="c565"></a>

### C565 — u/FudgeEducational2038

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1flzonauc/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1flzonauc/)

- **Faithful contribution:** Claims weight quantization is relatively safe because models are quantization-aware trained, even at q3_xxs, but sparse/linear attention is extremely sensitive to KV noise. Reports using q3_xxs with FP8 precision and asserts FP8 is better than Q8/INT8.
- **Type:** vague firsthand precision report and architecture claims
- **Why relevant (assessment):** High: directly contests weight-quantization explanations.
- **Evidence quality:** E1
- **Open questions / verification gaps:** Which exact model is QAT and uses the claimed attention types?; Does FP8 refer to K, V or another tensor, and in which backend?; What matched quality measurements support FP8 superiority and extreme weight compression?
- **Transferability (inference):** Quant format names and attention/QAT assumptions are model/backend-specific; do not generalize to OP’s artifact.
- **Themes:** weights, kv, runtime, reasoning, methodology

<a id="c566"></a>

### C566 — u/Savantskie1

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwy395eqh0k/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwy395eqh0k/)

- **Faithful contribution:** Challenges an apparent claim of 120GB VRAM on a 3090, interpreting the memory figure as VRAM.
- **Type:** hardware-interpretation challenge
- **Why relevant (assessment):** Low: technical misunderstanding corrected by C567.
- **Evidence quality:** E0
- **Open questions / verification gaps:** Was the stated 120GB system RAM or VRAM?
- **Transferability (inference):** Do not propagate the challenged memory interpretation as a reported configuration.
- **Themes:** hardware, methodology

<a id="c567"></a>

### C567 — u/Creative_Bookkeeper9

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwy4q7jl7z8/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwy4q7jl7z8/)

- **Faithful contribution:** Corrects the preceding interpretation: they said RAM, not VRAM.
- **Type:** firsthand configuration clarification
- **Why relevant (assessment):** Medium: important distinction for offload feasibility.
- **Evidence quality:** E1
- **Open questions / verification gaps:** What is the complete actual RAM/VRAM/model setup?
- **Transferability (inference):** System RAM and GPU memory must be recorded separately; this sentence alone supplies no verified capacity figure.
- **Themes:** hardware, runtime, methodology

<a id="c568"></a>

### C568 — u/Educational-Row-6782

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwwudvnhllw/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwwudvnhllw/)

- **Faithful contribution:** Claims cloud models use roughly $100k of hardware and a 3090 cannot produce the same results.
- **Type:** unsupported hardware/capability argument
- **Why relevant (assessment):** Medium: economic and capability dissent.
- **Evidence quality:** E0
- **Open questions / verification gaps:** What cloud deployment, cost and matched result support the claim?
- **Transferability (inference):** Hardware cost alone does not determine model accuracy; no comparable workload established.
- **Themes:** hardware, economics, alternatives

<a id="c569"></a>

### C569 — u/Turbulent_Office1340

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwxqjg0a5k3/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwxqjg0a5k3/)

- **Faithful contribution:** Recommends current Unsloth Studio with temperature 0.6, top-p 0.95, top-k 20, min-p 0, presence penalty 0, repetition penalty 1, context up to 256k if RAM permits, and UD-Q4_K_XL of unsloth/Qwen3.8-27B-GGUF. Suggests DavidAU/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF as a better model.
- **Type:** specific configuration/artifact recommendation
- **Why relevant (assessment):** High: unusually concrete sampling and artifact proposal.
- **Evidence quality:** E0
- **Open questions / verification gaps:** What template, thinking mode, backend version and exact files accompany these settings?; What evidence supports 256k operation and the alternate model’s superiority?
- **Transferability (inference):** Actionable candidate settings, not verified optimal defaults; memory use and quality require testing on the actual hardware.
- **Themes:** runtime, sampling, weights, context, hardware, alternatives

<a id="c570"></a>

### C570 — u/jjcsea

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwys2zg7t0h/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwys2zg7t0h/)

- **Faithful contribution:** Declares 3090/32GB RAM invalid for local LLMs and recommends 5090/64GB RAM or larger shared-memory architecture.
- **Type:** hardware recommendation
- **Why relevant (assessment):** Medium: broad capacity assertion without workload qualification.
- **Evidence quality:** E0
- **Open questions / verification gaps:** Which model, quant, context and success threshold require this upgrade?
- **Transferability (inference):** Hardware needs are workload-specific; the blanket rejection is not established.
- **Themes:** hardware, alternatives, economics

<a id="c571"></a>

### C571 — u/alonsojr1980-retry

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx0pm7jjtes/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx0pm7jjtes/)

- **Faithful contribution:** Argues small models struggle to make comprehensive plans and recommends stronger models for planning, smaller ones for execution/tool calls.
- **Type:** workflow division-of-labor hypothesis
- **Why relevant (assessment):** High: offers task decomposition rather than setup-only diagnosis.
- **Evidence quality:** E0
- **Open questions / verification gaps:** Which planning and execution tasks were evaluated?; Does handoff overhead outweigh any benefit?
- **Transferability (inference):** Planning/execution routing is a testable workflow, not a universal small-model limitation.
- **Themes:** workflow, reasoning, harness, alternatives

<a id="c572"></a>

### C572 — u/sod0

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1p246wy3o/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx1p246wy3o/)

- **Faithful contribution:** Counters that Qwen27B makes great plans and estimates Sonnet-level planning, while acknowledging Opus is better.
- **Type:** planning-capability counterclaim
- **Why relevant (assessment):** High: direct disagreement with C571.
- **Evidence quality:** E0
- **Open questions / verification gaps:** What plans, requirements, scoring rubric and model settings support the ranking?
- **Transferability (inference):** No controlled planning comparison supplied.
- **Themes:** workflow, reasoning, alternatives, methodology

<a id="c573"></a>

### C573 — u/sultan_papagani

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx29mvkwgbn/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx29mvkwgbn/)

- **Faithful contribution:** Expresses the view that local 27B is much worse than Sonnet 5.5; sarcastic framing provides no evidence.
- **Type:** capability dissent
- **Why relevant (assessment):** Low: weak but explicit comparative technical judgment.
- **Evidence quality:** E0
- **Open questions / verification gaps:** Which tasks and evaluation support the comparison?
- **Transferability (inference):** Retained as dissent, not a measured capability gap.
- **Themes:** alternatives, workflow

<a id="c574"></a>

### C574 — u/Gullible-Monitor-997

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3e9bvj1r4/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3e9bvj1r4/)

- **Faithful contribution:** In Italian, says the issue appears to be harness/agent behavior rather than hardware and recommends little-coder as an improvement over standard behavior.
- **Type:** harness diagnosis/recommendation
- **Why relevant (assessment):** High: explicit alternate causal explanation.
- **Evidence quality:** E0
- **Open questions / verification gaps:** Which little-coder project/version and what observed improvement?; What evidence rules out hardware or model settings?
- **Transferability (inference):** No setup or comparison is supplied; recommendation is a candidate harness test.
- **Themes:** harness, workflow, alternatives

<a id="c575"></a>

### C575 — u/Hunterxmalaa

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx7aazexg9t/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx7aazexg9t/)

- **Faithful contribution:** Argues 27B should not be expected to match Sonnet, citing claimed frontier parameter counts and asserting lower quantization compounds its capability limits; allows that Q8/BF16 with sufficient speed might help.
- **Type:** capability/quantization dissent
- **Why relevant (assessment):** High: challenges frontier-parity expectations, without matched evidence.
- **Evidence quality:** E0
- **Open questions / verification gaps:** What are verified frontier model sizes and serving precisions?; What matched coding results across quant levels support the claimed degradation?
- **Transferability (inference):** Parameter count and quant precision are incomplete capability proxies; no parity threshold established.
- **Themes:** weights, hardware, alternatives, methodology

<a id="c576"></a>

### C576 — u/ldn-ldn

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx81ggfil5x/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx81ggfil5x/)

- **Faithful contribution:** Claims Qwen is useless for serious coding and attacks those praising it; no task evidence is offered.
- **Type:** capability dissent with insult
- **Why relevant (assessment):** Low: retains substantive negative coding judgment, not the attack as evidence.
- **Evidence quality:** E0
- **Open questions / verification gaps:** What constitutes serious coding, and what failures were observed under what setup?
- **Transferability (inference):** No general incapacity follows from this unsupported claim.
- **Themes:** workflow, alternatives, methodology

<a id="c577"></a>

### C577 — u/Pixelplanet5

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx81o9s2v8i/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx81o9s2v8i/)

- **Faithful contribution:** Claims positive local-model tests use high-end hardware or short tasks, that fast memory for context is the key constraint, and that even 128GB unified-memory boxes leave too little context capacity and are slow. Predicts a Ryzen AI 495+ with 196GB unified memory as the first usable option.
- **Type:** evaluation critique and memory/hardware prediction
- **Why relevant (assessment):** High: raises benchmark duration/context confounds but overgeneralizes.
- **Evidence quality:** E0
- **Open questions / verification gaps:** Which test reports and model footprints support the claims?; What throughput and context requirements define usable?; Is the named future hardware configuration verified?
- **Transferability (inference):** Usable capacity depends on model size and KV architecture; no universal hardware floor or future product claim established.
- **Themes:** hardware, context, kv, methodology, alternatives

<a id="c578"></a>

### C578 — u/PhilippeEiffel

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx86hp2sk2p/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx86hp2sk2p/)

- **Faithful contribution:** Requests weight quant, KV quant and harness details, cites anti-Ollama material, and claims the native model is 54GB plus cache. Recommends beginning at BF16 weights and KV then reducing precision incrementally while checking quality; attributes failures to excessive quantization without measurements.
- **Type:** diagnostic checklist and precision-ablation proposal
- **Why relevant (assessment):** High: concrete missing variables and controlled tuning approach.
- **Evidence quality:** E0
- **Open questions / verification gaps:** What are the model quant size, KV quant size and harness?; Is a BF16 reference available, and which tasks/rubric determine acceptable quality?; What actual artifact and KV architecture are used?
- **Transferability (inference):** Stepwise precision ablation is transferable methodology; the asserted diagnosis is not established and BF16 need not fit the original rig.
- **Themes:** weights, kv, harness, runtime, hardware, methodology

<a id="c579"></a>

### C579 — u/Affectionate_Ripper

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx8qv9gb3j8/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx8qv9gb3j8/)

- **Faithful contribution:** Recommends model artifacts from Hugging Face user bartowski without naming a particular model or quant.
- **Type:** artifact-source recommendation
- **Why relevant (assessment):** Medium: potentially relevant to provenance/quant selection, but unspecific.
- **Evidence quality:** E0
- **Open questions / verification gaps:** Which repository, file, revision and quality comparison?
- **Transferability (inference):** Uploader choice alone is not evidence of compatibility or improved coding.
- **Themes:** weights, alternatives, methodology

<a id="c580"></a>

### C580 — u/FiringNerveEndings

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxk5v26p6ea/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxk5v26p6ea/)

- **Faithful contribution:** Asks whether OP uses an agent harness or direct inference calls, and whether AGENTS.md exists. Claims Claude Code adds system context, working-directory awareness and instruction-file reading; explicitly says they do not run a local model and are experimenting with harnesses.
- **Type:** harness diagnostic question with non-use disclosure
- **Why relevant (assessment):** High: distinguishes model endpoint from an agentic system.
- **Evidence quality:** E0
- **Open questions / verification gaps:** Are you using an agentic harness or making direct engine calls?; Do you have an AGENTS.md file?; Which prompts, file-loading behavior and tools does each side actually receive?
- **Transferability (inference):** Compare effective prompts/tool access, not just project-directory location; no firsthand local test is claimed.
- **Themes:** harness, template, workflow, context, methodology

<a id="c581"></a>

### C581 — u/majmichu

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxk3btu7f6p/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxk3btu7f6p/)

- **Faithful contribution:** Promotes their work-in-progress Local Quench harness and argues compact prompts/simple tools matter more than benchmarks. Reports using very compressed Bonsai 2 27B on 8GB VRAM, slow but working, and Q4_0 KV; advises not below Q4_K_M/NVFP4 for the discussed model, says Q8 KV is acceptable, and suggests smaller-model-oriented harnesses.
- **Type:** developer self-report and harness/precision recommendation
- **Why relevant (assessment):** High: named constrained setup and potential self-promotion/confounded advice.
- **Evidence quality:** E2
- **Open questions / verification gaps:** What exact Bonsai model, quant, backend, CPU offload, context and tasks worked?; How are Q4_0 KV results reconciled with the proposed weight precision floor?; What controlled tests show Local Quench or shorter prompts outperform alternatives?
- **Transferability (inference):** A different compressed model and custom harness on 8GB do not replicate OP; preserve self-promotion and prompt-length confounds.
- **Themes:** harness, template, context, weights, kv, hardware, workflow, alternatives, methodology

<a id="c582"></a>

### C582 — u/airdumb

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxk0ojenfz7/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxk0ojenfz7/)

- **Faithful contribution:** Reports building full web apps and managing infrastructure with one RTX5060ti 16GB, Qwen26B at 3bit and an EXL3 server.
- **Type:** setup-specific firsthand success report
- **Why relevant (assessment):** High: counterexample to broad 24GB-minimum and quant-incapacity claims.
- **Evidence quality:** E2
- **Open questions / verification gaps:** Which exact Qwen26B artifact, EXL3 version, harness, context and offload?; What tasks, tests and intervention levels define success?
- **Transferability (inference):** Different model/format/runtime; cannot treat as success for the exact dense-27B artifact.
- **Themes:** hardware, weights, runtime, harness, workflow, alternatives

<a id="c583"></a>

### C583 — u/AutomaticDriver5882

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxi6tzreoiq/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxi6tzreoiq/)

- **Faithful contribution:** Reports needing six GPUs before achieving results they considered comparable to Opus4.6, using Qwen Flash Next at 8-bit; attributes OP’s issue to insufficient GPU resources.
- **Type:** setup-specific but incomplete firsthand comparison
- **Why relevant (assessment):** High: multi-GPU MoE counterpoint with stated precision.
- **Evidence quality:** E2
- **Open questions / verification gaps:** Which six GPUs, runtime, RAM, context and tasks?; How was parity with Opus4.6 judged?
- **Transferability (inference):** Personal threshold for a different model does not establish a six-GPU requirement or isolate GPU causality.
- **Themes:** hardware, weights, runtime, alternatives, methodology

<a id="c585"></a>

### C585 — u/alonsojr1980-retry

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxihf4owrdt/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxihf4owrdt/)

- **Faithful contribution:** Proposes identical app-planning prompts for Qwen27B and Sonnet5.5, with Opus5.5 judging and scoring both; predicts parity only for shallow prompts or minimal requirements.
- **Type:** comparative evaluation proposal
- **Why relevant (assessment):** High: concrete planning test, with possible model-judge bias.
- **Evidence quality:** E0
- **Open questions / verification gaps:** What app requirements and scoring rubric should be fixed?; Will outputs be blinded/randomized and checked by independent or human assessment?; Which versions/settings and repeated runs?
- **Transferability (inference):** Paired prompts help control input; a single related provider’s judge and one task do not establish broad planning superiority.
- **Themes:** methodology, reasoning, workflow, alternatives

<a id="c586"></a>

### C586 — u/alonsojr1980-retry

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxicbp5399f/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxicbp5399f/)

- **Faithful contribution:** Says the compared model does not come near the other, without identifying models or evidence in the isolated sentence.
- **Type:** unelaborated capability dissent
- **Why relevant (assessment):** Low: preserves weak technical disagreement despite missing referent.
- **Evidence quality:** E0
- **Open questions / verification gaps:** Which models and task are being compared?; What result supports the gap?
- **Transferability (inference):** Do not assign a precise model ranking without parent context or supporting test.
- **Themes:** alternatives, methodology

<a id="c587"></a>

### C587 — u/kirbyfanner

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxjjwn4mpia/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxjjwn4mpia/)

- **Faithful contribution:** Asks whether the harness is bad and what the other user runs; reports generally liking it for frontier models and openness to changing.
- **Type:** vague firsthand harness report and question
- **Why relevant (assessment):** High: follows C563/C564’s Copilot discussion and requests a concrete alternative.
- **Evidence quality:** E1
- **Open questions / verification gaps:** Is it a bad harness?; What do you run?; Which locally served model behavior differs from frontier use in the same harness?
- **Transferability (inference):** Frontier success with a harness does not establish suitability for local tool schemas, prompts or reasoning formats.
- **Themes:** harness, workflow, alternatives, methodology

<a id="c588"></a>

### C588 — u/AutomaticDriver5882

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxibdl8061u/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxibdl8061u/)

- **Faithful contribution:** Asks about tokens per second; the isolated comment does not identify the setup.
- **Type:** performance question
- **Why relevant (assessment):** Medium: missing quantitative performance metric.
- **Evidence quality:** E0
- **Open questions / verification gaps:** What is the TPS?; Which model/setup and whether decode, prefill, per-session or aggregate?
- **Transferability (inference):** TPS requires stage, concurrency and context definitions; cannot infer speed here.
- **Themes:** runtime, hardware, methodology

<a id="c590"></a>

### C590 — u/MarcusAurelius68

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxcdq4fa8x0/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxcdq4fa8x0/)

- **Faithful contribution:** Clarifies that Strata and Radiance serve Qwen3.8 Flash Next; reports using Radiance and says it packages everything including the quant.
- **Type:** firsthand serving-stack clarification
- **Why relevant (assessment):** High: separates serving software from model and highlights bundled artifact choice.
- **Evidence quality:** E1
- **Open questions / verification gaps:** Which Radiance release and bundled quant are used?; How does the packaged artifact differ from Strata setups?
- **Transferability (inference):** Bundled quant provenance matters to comparisons; clarification is not a performance measurement.
- **Themes:** runtime, weights, alternatives, methodology

<a id="c591"></a>

### C591 — u/n4ru

**Direct permalink:** [https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx9hkpmcdr6/](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx9hkpmcdr6/)

- **Faithful contribution:** Asks why an unspecified factor would matter in this case.
- **Type:** technical relevance question with unresolved referent
- **Why relevant (assessment):** Low: retained conservatively as a potentially substantive challenge.
- **Evidence quality:** E0
- **Open questions / verification gaps:** Why would this matter in this case?; Parent linkage is absent; the factor being challenged cannot be identified from this text.
- **Transferability (inference):** No causal inference or specific technical position can be assigned without the referent.
- **Themes:** methodology

## 1.1 Exclusions ledger

All57 excluded IDs remain in the raw corpus.55 had readable text;2 were deleted. Reasons below explain exclusion from technical synthesis, not a judgment of the author.

| Ref | Author | Type | Reason / preserved contribution |
| --- | --- | --- | --- |

| <a id="c006"></a>[C006](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx7e28ki17m/) | Yok82 | joke | No diagnostic contribution. Jokes that llama.cpp is the next Debian. |

| <a id="c015"></a>[C015](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmd5oyp2g1/) | [unavailable] | deleted | Author and body unavailable; cannot assess. [deleted] |

| <a id="c018"></a>[C018](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnmx602h0g/) | _RemyLeBeau_ | privacy tangent | Unsupported privacy allegation outside reliability investigation; not adopted. Claims LM Studio sends information to a data lake and admits not knowing current comparison. |

| <a id="c019"></a>[C019](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwu947x0lnm/) | l1o2l | privacy tangent question | Unanswered in accessible subset; preserve as peripheral, not a reliability finding. Asks what information LM Studio allegedly sends. |

| <a id="c024"></a>[C024](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmeed7tl0g/) | [unavailable] | deleted | Author and body unavailable; cannot assess. [deleted] |

| <a id="c026"></a>[C026](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwtj65uw9lu/) | 6ft1in | reaction | No diagnostic contribution. Emoji reaction only. |

| <a id="c029"></a>[C029](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwklrc2eg0z/) | Repulsive_Initial308 | reaction | Adds no causal evidence. Laughs that Ollama was obvious. |

| <a id="c035"></a>[C035](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm0qskfhk5/) | ColaEuphoria | satirical analogy | No actionable setting or measured evidence. Compares Ollama to a game locked at 360p. |

| <a id="c036"></a>[C036](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnaxg2l7ds/) | cellcore667 | wordplay | No diagnostic contribution. Ollama/Baden wordplay and translation edit. |

| <a id="c037"></a>[C037](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwsq3yrdnds/) | rinmperdinck | joke | No diagnostic contribution. Makes a towers/Pentagon joke about the thread. |

| <a id="c038"></a>[C038](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxd867ose5g/) | Apprehensive_Stop314 | wordplay | No diagnostic contribution. Obama/Biden wordplay. |

| <a id="c040"></a>[C040](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwki9a643vo/) | vogelvogelvogelvogel | personal attack | Not evidence about the failure. Attacks OP's research effort. |

| <a id="c042"></a>[C042](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwketw3ojab/) | Creative_Diver3492 | reaction | No diagnostic contribution. Laughter only. |

| <a id="c049"></a>[C049](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwk9gmpqtuo/) | Ratiofarming | personal speculation | No technical detail beyond already identified unknowns. Speculates OP does not know the settings. |

| <a id="c050"></a>[C050](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwssg1jub34/) | pheoxs | sarcasm | No new observation or actionable evidence. Mocks the idea Q1 is better because smaller. |

| <a id="c052"></a>[C052](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwklsw5ddi8/) | StillOnTheInterweb | sarcasm | No diagnostic contribution. Sarcastic praise for Reddit advice. |

| <a id="c053"></a>[C053](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlz940zixx/) | superbiche | joke | No diagnostic contribution. Jokes that an LLM could research this. |

| <a id="c068"></a>[C068](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnkpj4us9t/) | Bagelsarenakeddonuts | crossreference | No additional substance; useful workflow captured at C066. Points to reply to InfiniteBlink. |

| <a id="c086"></a>[C086](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm4oapltpg/) | yellowsockss | meta criticism | No specific error or counterevidence identified. Claims nobody in the thread knows what they discuss. |

| <a id="c087"></a>[C087](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwnp9fq8zaa/) | notMyPenis | meta reaction | No diagnostic contribution. Agrees nobody knows what is going on. |

| <a id="c088"></a>[C088](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwolc5xy084/) | Connect_Ad791 | meta reaction | No actionable evidence beyond general uncertainty. Jokes that fast changes make everyone's knowledge stale. |

| <a id="c141"></a>[C141](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwrls0m4of5/) | Smooth-Television-48 | dismissal | No diagnostic contribution. Calls the post a Friday shitpost. |

| <a id="c142"></a>[C142](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rws4uecoyw4/) | theamazingo | authorship speculation | Irrelevant to reliability mechanism. Speculates AI wrote the post because of bold formatting. |

| <a id="c161"></a>[C161](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkn806tp5t/) | starkruzr | personal attack | No technical contribution. Accuses OP of doing no research. |

| <a id="c199"></a>[C199](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwrvtv340it/) | Smooth-Television-48 | reaction/joke | Pure agreement (easy mode), without added detail. No substantive technical contribution retained. |

| <a id="c210"></a>[C210](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmfd6nvbfl/) | InfiniteBlink | reaction/joke | Thanks only; no added substance. No substantive technical contribution retained. |

| <a id="c215"></a>[C215](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwp5utr93ts/) | InfiniteBlink | reaction/joke | Thanks and intent to explore later; no added technical substance. No substantive technical contribution retained. |

| <a id="c226"></a>[C226](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx8czh9ohb5/) | stupidio_the_return | reaction/joke | Endorsement of tools/pipelines without added details. No substantive technical contribution retained. |

| <a id="c227"></a>[C227](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxhod7fzq91/) | pioo84 | reaction/joke | Plumber joke only. No substantive technical contribution retained. |

| <a id="c232"></a>[C232](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx3u9tve36o/) | SenorPeterz | reaction/joke | Laughter only. No substantive technical contribution retained. |

| <a id="c238"></a>[C238](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwu6vug4ucg/) | Kalahdin | reaction/joke | Ellipsis-only reaction. No substantive technical contribution retained. |

| <a id="c250"></a>[C250](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmilqmb1k2/) | BonnieReborn | reaction/joke | Agreement only; no added substance. No substantive technical contribution retained. |

| <a id="c282"></a>[C282](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxafc9w9in5/) | FudgeEducational2038 | reaction/joke | Exactly-only agreement; no unambiguous added technical substance. No substantive technical contribution retained. |

| <a id="c332"></a>[C332](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rws2z26hg9v/) | Remote-Pineapple-541 | personal attack | Personal attack without substantive technical contribution. Criticizes the software team’s ability to follow documentation and troubleshoot without supplying a technical claim or remedy. |

| <a id="c344"></a>[C344](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwvd6k4tspt/) | dethstrobe | crossreference | Crossreference with no added substantive setup, outcome or analysis. Links another Reddit discussion and briefly says the commenter also had similar results, without describing them. |

| <a id="c352"></a>[C352](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwxcykx6aaq/) | ulysses_size | contact invitation | Contact invitation and reassurance without substantive setup, advice or outcome. Says the commenter was in a similar position three years earlier and invites a private message without supplying technical information. |

| <a id="c353"></a>[C353](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwxrl8rguqq/) | Turbulent_Office1340 | pure dismissal | Pure dismissal/personal attack without added substance. Dismisses the other commenters as uninformed without offering evidence or a technical argument. |

| <a id="c380"></a>[C380](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx44wgu73c4/) | goingsplit | reaction and notification request | Pure acknowledgment/notification request without added substantive research content. Thanks the preceding commenter and requests a ping if a setup project is created. |

| <a id="c429"></a>[C429](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx7ebxcbna9/) | rusl1 | personal attack/pure reaction | Excluded: personal dismissal with no substantive model/runtime claim. Dismisses the post as 'AI slop' without adding technical information. |

| <a id="c432"></a>[C432](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rx7laxa9mzn/) | AnxietyCorrect106 | joke/personal insult | Excluded: joke and insult, not an actual report of the poster's quantization. Makes a mocking one-bit-quant joke without substantive setup information. |

| <a id="c484"></a>[C484](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxjnuucjcmb/) | starwaver | pure agreement/reaction | Excluded: agreement-only crossreference with no added substantive information. Agrees that their experience with Qwen was similar without adding a task, setup, failure or other detail. |

| <a id="c494"></a>[C494](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkb8b3b7oj/) | Hood-Boy | excluded reaction/cross-reference | Bare stop-using-Ollama link, with no original technical claim; redundant cross-reference. Link not fetched. No retained technical contribution. |

| <a id="c496"></a>[C496](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmk8ynn2ch/) | Frail_Waif | excluded reaction/cross-reference | Reaction to downvotes and appreciation for an answer; no technical claim or question. No retained technical contribution. |

| <a id="c498"></a>[C498](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwkqm34f8v9/) | OrangeManSad | excluded reaction/cross-reference | Sarcastic agreement that 27B is miles above Sonnet; no substantive supporting claim beyond the reaction. No retained technical contribution. |

| <a id="c502"></a>[C502](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwppzgl36w4/) | ieatdownvotes4food | excluded reaction/cross-reference | Escalating engine list ending in Nintendo64s is a joke without a technical comparison. No retained technical contribution. |

| <a id="c503"></a>[C503](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwytdbkepwk/) | _RemyLeBeau_ | excluded reaction/cross-reference | Directs someone to documentation and disclaims product use, without identifying a substantive technical issue; redundant cross-reference. No retained technical contribution. |

| <a id="c523"></a>[C523](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwlb9wu6aw4/) | skifreek | excluded reaction/cross-reference | Thanks and intent to try advice, without a result or new technical detail. No retained technical contribution. |

| <a id="c526"></a>[C526](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmptuvelcy/) | ptear | excluded reaction/cross-reference | Personal reaction that a suggestion is always the answer; no technical content. No retained technical contribution. |

| <a id="c527"></a>[C527](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwmw9zw73qa/) | superbiche | excluded reaction/cross-reference | Rebukes asking questions already covered in threads/manuals; no distinct technical procedure or claim retained. No retained technical contribution. |

| <a id="c536"></a>[C536](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwm1yocgo80/) | BawbbySmith | excluded reaction/cross-reference | Pure hype accusation without an identifiable technical explanation or comparison. No retained technical contribution. |

| <a id="c542"></a>[C542](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwuhs9l4hi8/) | OneInspection927 | excluded reaction/cross-reference | Agreement that they did the same thing, without identifying the action or adding technical detail. No retained technical contribution. |

| <a id="c543"></a>[C543](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwq5tgvy7qa/) | Zenoran | excluded reaction/cross-reference | Dismissive fantasy remark with no technical argument. No retained technical contribution. |

| <a id="c546"></a>[C546](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rws6rvxr7ad/) | sQeeeter | excluded reaction/cross-reference | Off-topic question about a sexual joke/insult, not a technical question. No retained technical contribution. |

| <a id="c547"></a>[C547](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwsd80nb63p/) | UnrealizedLosses | excluded reaction/cross-reference | Insulting joke answering the preceding off-topic question. No retained technical contribution. |

| <a id="c564"></a>[C564](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rwvywa8v82r/) | SSarrrrrrrrrr | excluded reaction/cross-reference | Mocking Copilot reaction without a technical explanation or test; follow-up technical question is retained separately as C587. No retained technical contribution. |

| <a id="c584"></a>[C584](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxadg5p70de/) | B1g_BuddhAH | excluded reaction/cross-reference | Personal retort about an unspecified non-coding use case; no identifiable technical claim or question requiring retention. No retained technical contribution. |

| <a id="c589"></a>[C589](https://www.reddit.com/r/LocalLLM/comments/1xjvc08/local_qwen_27b_is_practically_unusable_for_coding/19rxewcjcvvs5/) | Smooth-Television-48 | excluded reaction/cross-reference | Dismissive reply to a speed question without a metric or technical explanation. No retained technical contribution. |


**Exclusion reason groups:** Reaction/joke/agreement/no additional substance: 27; Deleted/unreadable: 2; Peripheral privacy tangent: 2; Insult/dismissal/authorship speculation: 8; Redundant crossreference/no self-contained detail: 18. These groups partition57; specific reasons are in the ledger.


## 2. Comprehensive theme-to-comment map

Every qualifying C-ref appears in at least one row. Links lead to the individual entry and its direct Reddit permalink. This is a discussion map, not evidence-weighted consensus; detailed disagreements/tests follow.

| Theme | Qualifying comments |
| --- | --- |

| runtime | [C001](#c001), [C002](#c002), [C003](#c003), [C004](#c004), [C005](#c005), [C007](#c007), [C008](#c008), [C009](#c009), [C010](#c010), [C011](#c011), [C012](#c012), [C013](#c013), [C014](#c014), [C016](#c016), [C017](#c017), [C020](#c020), [C025](#c025), [C027](#c027), [C028](#c028), [C030](#c030), [C031](#c031), [C032](#c032), [C033](#c033), [C034](#c034), [C039](#c039), [C043](#c043), [C044](#c044), [C045](#c045), [C046](#c046), [C056](#c056), [C057](#c057), [C058](#c058), [C067](#c067), [C069](#c069), [C075](#c075), [C076](#c076), [C083](#c083), [C092](#c092), [C094](#c094), [C095](#c095), [C096](#c096), [C099](#c099), [C106](#c106), [C109](#c109), [C110](#c110), [C119](#c119), [C121](#c121), [C123](#c123), [C129](#c129), [C130](#c130), [C131](#c131), [C136](#c136), [C138](#c138), [C139](#c139), [C143](#c143), [C149](#c149), [C150](#c150), [C152](#c152), [C159](#c159), [C163](#c163), [C167](#c167), [C169](#c169), [C172](#c172), [C176](#c176), [C177](#c177), [C182](#c182), [C183](#c183), [C185](#c185), [C186](#c186), [C191](#c191), [C192](#c192), [C197](#c197), [C200](#c200), [C201](#c201), [C202](#c202), [C204](#c204), [C205](#c205), [C206](#c206), [C207](#c207), [C209](#c209), [C216](#c216), [C225](#c225), [C229](#c229), [C233](#c233), [C236](#c236), [C239](#c239), [C240](#c240), [C241](#c241), [C243](#c243), [C245](#c245), [C251](#c251), [C252](#c252), [C260](#c260), [C261](#c261), [C262](#c262), [C264](#c264), [C269](#c269), [C276](#c276), [C277](#c277), [C278](#c278), [C279](#c279), [C281](#c281), [C283](#c283), [C284](#c284), [C285](#c285), [C289](#c289), [C298](#c298), [C300](#c300), [C302](#c302), [C304](#c304), [C307](#c307), [C308](#c308), [C309](#c309), [C312](#c312), [C313](#c313), [C314](#c314), [C318](#c318), [C319](#c319), [C320](#c320), [C322](#c322), [C325](#c325), [C331](#c331), [C335](#c335), [C337](#c337), [C339](#c339), [C345](#c345), [C346](#c346), [C347](#c347), [C355](#c355), [C359](#c359), [C360](#c360), [C361](#c361), [C364](#c364), [C369](#c369), [C370](#c370), [C372](#c372), [C373](#c373), [C377](#c377), [C383](#c383), [C384](#c384), [C388](#c388), [C389](#c389), [C392](#c392), [C394](#c394), [C398](#c398), [C399](#c399), [C400](#c400), [C401](#c401), [C402](#c402), [C403](#c403), [C404](#c404), [C405](#c405), [C406](#c406), [C407](#c407), [C408](#c408), [C411](#c411), [C413](#c413), [C414](#c414), [C415](#c415), [C416](#c416), [C417](#c417), [C418](#c418), [C419](#c419), [C420](#c420), [C421](#c421), [C424](#c424), [C425](#c425), [C426](#c426), [C427](#c427), [C428](#c428), [C434](#c434), [C435](#c435), [C436](#c436), [C438](#c438), [C442](#c442), [C444](#c444), [C446](#c446), [C450](#c450), [C454](#c454), [C456](#c456), [C457](#c457), [C458](#c458), [C460](#c460), [C461](#c461), [C465](#c465), [C466](#c466), [C467](#c467), [C468](#c468), [C471](#c471), [C473](#c473), [C474](#c474), [C477](#c477), [C478](#c478), [C480](#c480), [C482](#c482), [C485](#c485), [C486](#c486), [C487](#c487), [C489](#c489), [C490](#c490), [C493](#c493), [C499](#c499), [C500](#c500), [C501](#c501), [C504](#c504), [C505](#c505), [C506](#c506), [C507](#c507), [C508](#c508), [C509](#c509), [C510](#c510), [C511](#c511), [C512](#c512), [C513](#c513), [C514](#c514), [C515](#c515), [C516](#c516), [C529](#c529), [C531](#c531), [C532](#c532), [C534](#c534), [C541](#c541), [C548](#c548), [C549](#c549), [C550](#c550), [C551](#c551), [C552](#c552), [C553](#c553), [C554](#c554), [C555](#c555), [C557](#c557), [C558](#c558), [C561](#c561), [C563](#c563), [C565](#c565), [C567](#c567), [C569](#c569), [C578](#c578), [C582](#c582), [C583](#c583), [C588](#c588), [C590](#c590) |

| sampling | [C046](#c046), [C047](#c047), [C069](#c069), [C083](#c083), [C097](#c097), [C132](#c132), [C137](#c137), [C157](#c157), [C171](#c171), [C234](#c234), [C235](#c235), [C294](#c294), [C298](#c298), [C314](#c314), [C345](#c345), [C346](#c346), [C399](#c399), [C405](#c405), [C413](#c413), [C419](#c419), [C444](#c444), [C483](#c483), [C509](#c509), [C521](#c521), [C569](#c569) |

| template | [C075](#c075), [C077](#c077), [C193](#c193), [C194](#c194), [C339](#c339), [C345](#c345), [C444](#c444), [C457](#c457), [C482](#c482), [C483](#c483), [C580](#c580), [C581](#c581) |

| kv | [C074](#c074), [C078](#c078), [C091](#c091), [C097](#c097), [C099](#c099), [C108](#c108), [C110](#c110), [C132](#c132), [C145](#c145), [C147](#c147), [C158](#c158), [C169](#c169), [C174](#c174), [C179](#c179), [C182](#c182), [C183](#c183), [C186](#c186), [C206](#c206), [C228](#c228), [C229](#c229), [C233](#c233), [C243](#c243), [C245](#c245), [C251](#c251), [C257](#c257), [C266](#c266), [C267](#c267), [C269](#c269), [C287](#c287), [C289](#c289), [C291](#c291), [C298](#c298), [C302](#c302), [C307](#c307), [C318](#c318), [C323](#c323), [C354](#c354), [C373](#c373), [C376](#c376), [C384](#c384), [C399](#c399), [C403](#c403), [C407](#c407), [C419](#c419), [C435](#c435), [C444](#c444), [C454](#c454), [C458](#c458), [C459](#c459), [C466](#c466), [C492](#c492), [C524](#c524), [C525](#c525), [C534](#c534), [C544](#c544), [C554](#c554), [C555](#c555), [C563](#c563), [C565](#c565), [C577](#c577), [C578](#c578), [C581](#c581) |

| weights | [C020](#c020), [C031](#c031), [C041](#c041), [C046](#c046), [C047](#c047), [C051](#c051), [C056](#c056), [C057](#c057), [C058](#c058), [C059](#c059), [C069](#c069), [C074](#c074), [C090](#c090), [C091](#c091), [C092](#c092), [C096](#c096), [C097](#c097), [C107](#c107), [C117](#c117), [C126](#c126), [C129](#c129), [C132](#c132), [C137](#c137), [C138](#c138), [C139](#c139), [C140](#c140), [C145](#c145), [C147](#c147), [C149](#c149), [C151](#c151), [C153](#c153), [C155](#c155), [C157](#c157), [C159](#c159), [C160](#c160), [C162](#c162), [C166](#c166), [C167](#c167), [C169](#c169), [C172](#c172), [C177](#c177), [C179](#c179), [C182](#c182), [C184](#c184), [C186](#c186), [C187](#c187), [C188](#c188), [C190](#c190), [C191](#c191), [C192](#c192), [C198](#c198), [C204](#c204), [C208](#c208), [C216](#c216), [C220](#c220), [C228](#c228), [C229](#c229), [C233](#c233), [C239](#c239), [C240](#c240), [C243](#c243), [C244](#c244), [C245](#c245), [C247](#c247), [C251](#c251), [C257](#c257), [C266](#c266), [C267](#c267), [C269](#c269), [C279](#c279), [C285](#c285), [C289](#c289), [C291](#c291), [C292](#c292), [C294](#c294), [C298](#c298), [C299](#c299), [C302](#c302), [C303](#c303), [C304](#c304), [C305](#c305), [C307](#c307), [C308](#c308), [C311](#c311), [C312](#c312), [C313](#c313), [C316](#c316), [C318](#c318), [C319](#c319), [C320](#c320), [C323](#c323), [C325](#c325), [C326](#c326), [C327](#c327), [C329](#c329), [C331](#c331), [C338](#c338), [C340](#c340), [C345](#c345), [C348](#c348), [C349](#c349), [C354](#c354), [C360](#c360), [C367](#c367), [C370](#c370), [C372](#c372), [C373](#c373), [C375](#c375), [C376](#c376), [C383](#c383), [C384](#c384), [C387](#c387), [C389](#c389), [C390](#c390), [C391](#c391), [C392](#c392), [C393](#c393), [C394](#c394), [C399](#c399), [C401](#c401), [C403](#c403), [C404](#c404), [C405](#c405), [C406](#c406), [C407](#c407), [C410](#c410), [C412](#c412), [C413](#c413), [C414](#c414), [C418](#c418), [C425](#c425), [C430](#c430), [C431](#c431), [C433](#c433), [C435](#c435), [C438](#c438), [C444](#c444), [C448](#c448), [C449](#c449), [C453](#c453), [C456](#c456), [C458](#c458), [C459](#c459), [C462](#c462), [C464](#c464), [C466](#c466), [C467](#c467), [C468](#c468), [C470](#c470), [C471](#c471), [C472](#c472), [C473](#c473), [C477](#c477), [C479](#c479), [C481](#c481), [C487](#c487), [C491](#c491), [C492](#c492), [C495](#c495), [C507](#c507), [C508](#c508), [C517](#c517), [C530](#c530), [C532](#c532), [C534](#c534), [C540](#c540), [C541](#c541), [C544](#c544), [C548](#c548), [C549](#c549), [C550](#c550), [C551](#c551), [C554](#c554), [C558](#c558), [C561](#c561), [C562](#c562), [C563](#c563), [C565](#c565), [C569](#c569), [C575](#c575), [C578](#c578), [C579](#c579), [C581](#c581), [C582](#c582), [C583](#c583), [C590](#c590) |

| context | [C059](#c059), [C066](#c066), [C070](#c070), [C073](#c073), [C074](#c074), [C076](#c076), [C079](#c079), [C085](#c085), [C091](#c091), [C092](#c092), [C094](#c094), [C099](#c099), [C100](#c100), [C107](#c107), [C108](#c108), [C110](#c110), [C123](#c123), [C124](#c124), [C125](#c125), [C127](#c127), [C128](#c128), [C134](#c134), [C143](#c143), [C148](#c148), [C153](#c153), [C158](#c158), [C160](#c160), [C164](#c164), [C166](#c166), [C168](#c168), [C169](#c169), [C170](#c170), [C172](#c172), [C175](#c175), [C176](#c176), [C177](#c177), [C179](#c179), [C181](#c181), [C183](#c183), [C186](#c186), [C188](#c188), [C190](#c190), [C191](#c191), [C196](#c196), [C206](#c206), [C212](#c212), [C219](#c219), [C221](#c221), [C223](#c223), [C225](#c225), [C228](#c228), [C229](#c229), [C234](#c234), [C239](#c239), [C243](#c243), [C251](#c251), [C252](#c252), [C254](#c254), [C255](#c255), [C257](#c257), [C265](#c265), [C266](#c266), [C267](#c267), [C268](#c268), [C276](#c276), [C279](#c279), [C290](#c290), [C291](#c291), [C292](#c292), [C293](#c293), [C294](#c294), [C296](#c296), [C298](#c298), [C302](#c302), [C304](#c304), [C307](#c307), [C310](#c310), [C319](#c319), [C321](#c321), [C323](#c323), [C324](#c324), [C329](#c329), [C333](#c333), [C334](#c334), [C335](#c335), [C346](#c346), [C347](#c347), [C349](#c349), [C358](#c358), [C363](#c363), [C367](#c367), [C368](#c368), [C371](#c371), [C373](#c373), [C374](#c374), [C375](#c375), [C377](#c377), [C379](#c379), [C383](#c383), [C384](#c384), [C399](#c399), [C400](#c400), [C403](#c403), [C407](#c407), [C409](#c409), [C412](#c412), [C414](#c414), [C420](#c420), [C423](#c423), [C424](#c424), [C425](#c425), [C426](#c426), [C435](#c435), [C437](#c437), [C440](#c440), [C443](#c443), [C444](#c444), [C445](#c445), [C446](#c446), [C452](#c452), [C453](#c453), [C454](#c454), [C457](#c457), [C458](#c458), [C459](#c459), [C467](#c467), [C470](#c470), [C476](#c476), [C477](#c477), [C478](#c478), [C480](#c480), [C482](#c482), [C487](#c487), [C492](#c492), [C495](#c495), [C529](#c529), [C534](#c534), [C541](#c541), [C544](#c544), [C551](#c551), [C554](#c554), [C555](#c555), [C558](#c558), [C562](#c562), [C563](#c563), [C569](#c569), [C577](#c577), [C580](#c580), [C581](#c581) |

| harness | [C011](#c011), [C046](#c046), [C047](#c047), [C048](#c048), [C060](#c060), [C064](#c064), [C065](#c065), [C066](#c066), [C074](#c074), [C075](#c075), [C079](#c079), [C081](#c081), [C082](#c082), [C083](#c083), [C084](#c084), [C085](#c085), [C094](#c094), [C095](#c095), [C096](#c096), [C098](#c098), [C110](#c110), [C118](#c118), [C120](#c120), [C123](#c123), [C127](#c127), [C128](#c128), [C130](#c130), [C132](#c132), [C133](#c133), [C134](#c134), [C145](#c145), [C151](#c151), [C157](#c157), [C159](#c159), [C160](#c160), [C163](#c163), [C167](#c167), [C169](#c169), [C170](#c170), [C175](#c175), [C177](#c177), [C179](#c179), [C182](#c182), [C184](#c184), [C185](#c185), [C186](#c186), [C191](#c191), [C192](#c192), [C193](#c193), [C194](#c194), [C195](#c195), [C197](#c197), [C206](#c206), [C207](#c207), [C211](#c211), [C212](#c212), [C213](#c213), [C214](#c214), [C216](#c216), [C219](#c219), [C222](#c222), [C223](#c223), [C225](#c225), [C229](#c229), [C249](#c249), [C255](#c255), [C256](#c256), [C260](#c260), [C261](#c261), [C264](#c264), [C265](#c265), [C270](#c270), [C276](#c276), [C278](#c278), [C288](#c288), [C289](#c289), [C294](#c294), [C295](#c295), [C296](#c296), [C297](#c297), [C298](#c298), [C300](#c300), [C302](#c302), [C306](#c306), [C308](#c308), [C309](#c309), [C310](#c310), [C311](#c311), [C312](#c312), [C317](#c317), [C319](#c319), [C321](#c321), [C323](#c323), [C327](#c327), [C328](#c328), [C329](#c329), [C330](#c330), [C331](#c331), [C333](#c333), [C339](#c339), [C342](#c342), [C347](#c347), [C351](#c351), [C354](#c354), [C355](#c355), [C356](#c356), [C363](#c363), [C370](#c370), [C371](#c371), [C372](#c372), [C377](#c377), [C379](#c379), [C381](#c381), [C382](#c382), [C383](#c383), [C384](#c384), [C385](#c385), [C386](#c386), [C389](#c389), [C396](#c396), [C397](#c397), [C399](#c399), [C400](#c400), [C403](#c403), [C404](#c404), [C406](#c406), [C408](#c408), [C409](#c409), [C411](#c411), [C412](#c412), [C413](#c413), [C416](#c416), [C418](#c418), [C419](#c419), [C420](#c420), [C421](#c421), [C422](#c422), [C423](#c423), [C424](#c424), [C425](#c425), [C426](#c426), [C430](#c430), [C433](#c433), [C434](#c434), [C435](#c435), [C438](#c438), [C440](#c440), [C442](#c442), [C444](#c444), [C445](#c445), [C446](#c446), [C452](#c452), [C453](#c453), [C454](#c454), [C455](#c455), [C457](#c457), [C458](#c458), [C461](#c461), [C462](#c462), [C463](#c463), [C465](#c465), [C466](#c466), [C467](#c467), [C470](#c470), [C471](#c471), [C472](#c472), [C473](#c473), [C477](#c477), [C478](#c478), [C480](#c480), [C482](#c482), [C483](#c483), [C485](#c485), [C486](#c486), [C487](#c487), [C488](#c488), [C493](#c493), [C495](#c495), [C510](#c510), [C516](#c516), [C519](#c519), [C521](#c521), [C533](#c533), [C539](#c539), [C555](#c555), [C563](#c563), [C571](#c571), [C574](#c574), [C578](#c578), [C580](#c580), [C581](#c581), [C582](#c582), [C587](#c587) |

| workflow | [C021](#c021), [C023](#c023), [C048](#c048), [C059](#c059), [C060](#c060), [C061](#c061), [C062](#c062), [C063](#c063), [C064](#c064), [C065](#c065), [C066](#c066), [C067](#c067), [C070](#c070), [C071](#c071), [C072](#c072), [C073](#c073), [C074](#c074), [C081](#c081), [C084](#c084), [C093](#c093), [C097](#c097), [C098](#c098), [C104](#c104), [C107](#c107), [C112](#c112), [C113](#c113), [C115](#c115), [C116](#c116), [C118](#c118), [C120](#c120), [C124](#c124), [C133](#c133), [C137](#c137), [C144](#c144), [C146](#c146), [C151](#c151), [C153](#c153), [C154](#c154), [C160](#c160), [C165](#c165), [C173](#c173), [C178](#c178), [C179](#c179), [C183](#c183), [C184](#c184), [C186](#c186), [C187](#c187), [C192](#c192), [C195](#c195), [C196](#c196), [C198](#c198), [C209](#c209), [C211](#c211), [C212](#c212), [C213](#c213), [C214](#c214), [C217](#c217), [C218](#c218), [C219](#c219), [C221](#c221), [C222](#c222), [C224](#c224), [C225](#c225), [C230](#c230), [C231](#c231), [C233](#c233), [C242](#c242), [C247](#c247), [C248](#c248), [C249](#c249), [C253](#c253), [C254](#c254), [C255](#c255), [C264](#c264), [C268](#c268), [C270](#c270), [C271](#c271), [C278](#c278), [C287](#c287), [C293](#c293), [C294](#c294), [C295](#c295), [C296](#c296), [C298](#c298), [C300](#c300), [C302](#c302), [C306](#c306), [C309](#c309), [C310](#c310), [C314](#c314), [C317](#c317), [C323](#c323), [C324](#c324), [C326](#c326), [C327](#c327), [C328](#c328), [C333](#c333), [C334](#c334), [C335](#c335), [C336](#c336), [C337](#c337), [C338](#c338), [C341](#c341), [C342](#c342), [C343](#c343), [C347](#c347), [C350](#c350), [C351](#c351), [C354](#c354), [C358](#c358), [C359](#c359), [C360](#c360), [C362](#c362), [C367](#c367), [C368](#c368), [C370](#c370), [C371](#c371), [C373](#c373), [C374](#c374), [C375](#c375), [C377](#c377), [C378](#c378), [C379](#c379), [C381](#c381), [C384](#c384), [C385](#c385), [C386](#c386), [C389](#c389), [C395](#c395), [C396](#c396), [C397](#c397), [C399](#c399), [C400](#c400), [C402](#c402), [C406](#c406), [C408](#c408), [C409](#c409), [C411](#c411), [C413](#c413), [C416](#c416), [C417](#c417), [C418](#c418), [C420](#c420), [C421](#c421), [C423](#c423), [C426](#c426), [C427](#c427), [C434](#c434), [C435](#c435), [C437](#c437), [C438](#c438), [C439](#c439), [C440](#c440), [C442](#c442), [C446](#c446), [C450](#c450), [C453](#c453), [C454](#c454), [C455](#c455), [C459](#c459), [C461](#c461), [C462](#c462), [C463](#c463), [C465](#c465), [C470](#c470), [C471](#c471), [C472](#c472), [C473](#c473), [C474](#c474), [C478](#c478), [C480](#c480), [C491](#c491), [C493](#c493), [C495](#c495), [C497](#c497), [C505](#c505), [C506](#c506), [C509](#c509), [C510](#c510), [C511](#c511), [C513](#c513), [C516](#c516), [C517](#c517), [C518](#c518), [C519](#c519), [C520](#c520), [C528](#c528), [C533](#c533), [C535](#c535), [C537](#c537), [C538](#c538), [C539](#c539), [C541](#c541), [C545](#c545), [C555](#c555), [C556](#c556), [C557](#c557), [C558](#c558), [C559](#c559), [C560](#c560), [C562](#c562), [C563](#c563), [C571](#c571), [C572](#c572), [C573](#c573), [C574](#c574), [C576](#c576), [C580](#c580), [C581](#c581), [C582](#c582), [C585](#c585), [C587](#c587) |

| reasoning | [C046](#c046), [C054](#c054), [C055](#c055), [C060](#c060), [C062](#c062), [C075](#c075), [C076](#c076), [C077](#c077), [C078](#c078), [C079](#c079), [C090](#c090), [C094](#c094), [C107](#c107), [C108](#c108), [C110](#c110), [C111](#c111), [C112](#c112), [C113](#c113), [C118](#c118), [C123](#c123), [C132](#c132), [C155](#c155), [C157](#c157), [C164](#c164), [C168](#c168), [C171](#c171), [C172](#c172), [C175](#c175), [C179](#c179), [C182](#c182), [C186](#c186), [C191](#c191), [C217](#c217), [C218](#c218), [C219](#c219), [C222](#c222), [C223](#c223), [C224](#c224), [C234](#c234), [C243](#c243), [C244](#c244), [C246](#c246), [C257](#c257), [C268](#c268), [C272](#c272), [C276](#c276), [C289](#c289), [C298](#c298), [C300](#c300), [C310](#c310), [C311](#c311), [C312](#c312), [C314](#c314), [C322](#c322), [C333](#c333), [C338](#c338), [C340](#c340), [C343](#c343), [C346](#c346), [C349](#c349), [C354](#c354), [C361](#c361), [C364](#c364), [C377](#c377), [C383](#c383), [C387](#c387), [C388](#c388), [C391](#c391), [C399](#c399), [C402](#c402), [C403](#c403), [C404](#c404), [C407](#c407), [C409](#c409), [C411](#c411), [C414](#c414), [C416](#c416), [C417](#c417), [C423](#c423), [C425](#c425), [C427](#c427), [C430](#c430), [C433](#c433), [C434](#c434), [C445](#c445), [C451](#c451), [C469](#c469), [C473](#c473), [C505](#c505), [C521](#c521), [C522](#c522), [C524](#c524), [C525](#c525), [C541](#c541), [C555](#c555), [C562](#c562), [C565](#c565), [C571](#c571), [C572](#c572), [C585](#c585) |

| knowledge | [C133](#c133), [C146](#c146), [C167](#c167), [C179](#c179), [C186](#c186), [C243](#c243), [C272](#c272), [C275](#c275), [C285](#c285), [C316](#c316), [C371](#c371), [C385](#c385), [C439](#c439), [C454](#c454), [C461](#c461), [C465](#c465), [C470](#c470), [C483](#c483) |

| hardware | [C007](#c007), [C013](#c013), [C014](#c014), [C020](#c020), [C047](#c047), [C061](#c061), [C082](#c082), [C091](#c091), [C092](#c092), [C093](#c093), [C099](#c099), [C100](#c100), [C101](#c101), [C102](#c102), [C103](#c103), [C105](#c105), [C108](#c108), [C109](#c109), [C114](#c114), [C117](#c117), [C118](#c118), [C122](#c122), [C123](#c123), [C125](#c125), [C126](#c126), [C129](#c129), [C135](#c135), [C144](#c144), [C145](#c145), [C148](#c148), [C152](#c152), [C153](#c153), [C156](#c156), [C158](#c158), [C166](#c166), [C167](#c167), [C169](#c169), [C172](#c172), [C173](#c173), [C178](#c178), [C180](#c180), [C182](#c182), [C183](#c183), [C189](#c189), [C190](#c190), [C197](#c197), [C198](#c198), [C204](#c204), [C206](#c206), [C216](#c216), [C219](#c219), [C223](#c223), [C225](#c225), [C228](#c228), [C229](#c229), [C236](#c236), [C237](#c237), [C239](#c239), [C240](#c240), [C241](#c241), [C242](#c242), [C251](#c251), [C252](#c252), [C253](#c253), [C254](#c254), [C255](#c255), [C256](#c256), [C257](#c257), [C258](#c258), [C263](#c263), [C264](#c264), [C265](#c265), [C266](#c266), [C267](#c267), [C268](#c268), [C276](#c276), [C277](#c277), [C279](#c279), [C280](#c280), [C281](#c281), [C283](#c283), [C284](#c284), [C285](#c285), [C286](#c286), [C288](#c288), [C289](#c289), [C290](#c290), [C291](#c291), [C292](#c292), [C293](#c293), [C296](#c296), [C298](#c298), [C300](#c300), [C301](#c301), [C302](#c302), [C303](#c303), [C304](#c304), [C305](#c305), [C307](#c307), [C308](#c308), [C311](#c311), [C312](#c312), [C313](#c313), [C314](#c314), [C318](#c318), [C319](#c319), [C320](#c320), [C322](#c322), [C323](#c323), [C325](#c325), [C326](#c326), [C327](#c327), [C329](#c329), [C331](#c331), [C333](#c333), [C334](#c334), [C335](#c335), [C337](#c337), [C346](#c346), [C347](#c347), [C350](#c350), [C354](#c354), [C357](#c357), [C361](#c361), [C362](#c362), [C364](#c364), [C365](#c365), [C366](#c366), [C367](#c367), [C368](#c368), [C370](#c370), [C373](#c373), [C383](#c383), [C384](#c384), [C389](#c389), [C394](#c394), [C397](#c397), [C399](#c399), [C400](#c400), [C402](#c402), [C404](#c404), [C408](#c408), [C409](#c409), [C410](#c410), [C412](#c412), [C413](#c413), [C414](#c414), [C415](#c415), [C425](#c425), [C426](#c426), [C427](#c427), [C428](#c428), [C430](#c430), [C431](#c431), [C435](#c435), [C438](#c438), [C442](#c442), [C443](#c443), [C444](#c444), [C445](#c445), [C446](#c446), [C447](#c447), [C453](#c453), [C456](#c456), [C459](#c459), [C461](#c461), [C463](#c463), [C467](#c467), [C470](#c470), [C471](#c471), [C472](#c472), [C473](#c473), [C475](#c475), [C476](#c476), [C480](#c480), [C481](#c481), [C487](#c487), [C489](#c489), [C491](#c491), [C492](#c492), [C493](#c493), [C495](#c495), [C508](#c508), [C517](#c517), [C525](#c525), [C529](#c529), [C531](#c531), [C534](#c534), [C541](#c541), [C544](#c544), [C548](#c548), [C549](#c549), [C550](#c550), [C551](#c551), [C552](#c552), [C553](#c553), [C554](#c554), [C555](#c555), [C558](#c558), [C559](#c559), [C562](#c562), [C563](#c563), [C566](#c566), [C567](#c567), [C568](#c568), [C569](#c569), [C570](#c570), [C575](#c575), [C577](#c577), [C578](#c578), [C581](#c581), [C582](#c582), [C583](#c583), [C588](#c588) |

| alternatives | [C004](#c004), [C022](#c022), [C023](#c023), [C030](#c030), [C031](#c031), [C054](#c054), [C059](#c059), [C060](#c060), [C079](#c079), [C080](#c080), [C081](#c081), [C089](#c089), [C096](#c096), [C098](#c098), [C099](#c099), [C100](#c100), [C101](#c101), [C104](#c104), [C105](#c105), [C106](#c106), [C117](#c117), [C119](#c119), [C121](#c121), [C122](#c122), [C131](#c131), [C133](#c133), [C136](#c136), [C137](#c137), [C140](#c140), [C146](#c146), [C147](#c147), [C148](#c148), [C149](#c149), [C150](#c150), [C151](#c151), [C155](#c155), [C156](#c156), [C157](#c157), [C165](#c165), [C167](#c167), [C173](#c173), [C174](#c174), [C185](#c185), [C189](#c189), [C201](#c201), [C204](#c204), [C205](#c205), [C209](#c209), [C216](#c216), [C220](#c220), [C223](#c223), [C225](#c225), [C229](#c229), [C236](#c236), [C237](#c237), [C239](#c239), [C241](#c241), [C242](#c242), [C243](#c243), [C246](#c246), [C253](#c253), [C254](#c254), [C255](#c255), [C256](#c256), [C259](#c259), [C262](#c262), [C264](#c264), [C268](#c268), [C270](#c270), [C275](#c275), [C276](#c276), [C277](#c277), [C279](#c279), [C283](#c283), [C285](#c285), [C286](#c286), [C292](#c292), [C293](#c293), [C295](#c295), [C297](#c297), [C299](#c299), [C301](#c301), [C302](#c302), [C304](#c304), [C305](#c305), [C308](#c308), [C311](#c311), [C312](#c312), [C313](#c313), [C315](#c315), [C316](#c316), [C318](#c318), [C319](#c319), [C320](#c320), [C323](#c323), [C326](#c326), [C327](#c327), [C329](#c329), [C331](#c331), [C333](#c333), [C334](#c334), [C335](#c335), [C336](#c336), [C337](#c337), [C339](#c339), [C340](#c340), [C341](#c341), [C343](#c343), [C346](#c346), [C347](#c347), [C348](#c348), [C350](#c350), [C354](#c354), [C357](#c357), [C358](#c358), [C360](#c360), [C361](#c361), [C362](#c362), [C364](#c364), [C367](#c367), [C368](#c368), [C369](#c369), [C371](#c371), [C372](#c372), [C374](#c374), [C375](#c375), [C377](#c377), [C381](#c381), [C386](#c386), [C387](#c387), [C388](#c388), [C389](#c389), [C395](#c395), [C400](#c400), [C404](#c404), [C406](#c406), [C409](#c409), [C411](#c411), [C412](#c412), [C414](#c414), [C415](#c415), [C417](#c417), [C418](#c418), [C421](#c421), [C423](#c423), [C427](#c427), [C431](#c431), [C434](#c434), [C436](#c436), [C438](#c438), [C440](#c440), [C441](#c441), [C442](#c442), [C443](#c443), [C445](#c445), [C446](#c446), [C449](#c449), [C450](#c450), [C451](#c451), [C452](#c452), [C453](#c453), [C454](#c454), [C455](#c455), [C456](#c456), [C458](#c458), [C459](#c459), [C460](#c460), [C461](#c461), [C464](#c464), [C465](#c465), [C468](#c468), [C470](#c470), [C475](#c475), [C476](#c476), [C479](#c479), [C481](#c481), [C483](#c483), [C487](#c487), [C489](#c489), [C490](#c490), [C491](#c491), [C495](#c495), [C497](#c497), [C499](#c499), [C500](#c500), [C501](#c501), [C506](#c506), [C507](#c507), [C508](#c508), [C510](#c510), [C511](#c511), [C512](#c512), [C513](#c513), [C514](#c514), [C515](#c515), [C517](#c517), [C528](#c528), [C529](#c529), [C530](#c530), [C531](#c531), [C532](#c532), [C533](#c533), [C535](#c535), [C537](#c537), [C538](#c538), [C539](#c539), [C540](#c540), [C541](#c541), [C544](#c544), [C545](#c545), [C550](#c550), [C553](#c553), [C554](#c554), [C556](#c556), [C557](#c557), [C558](#c558), [C559](#c559), [C560](#c560), [C561](#c561), [C562](#c562), [C568](#c568), [C569](#c569), [C570](#c570), [C571](#c571), [C572](#c572), [C573](#c573), [C574](#c574), [C575](#c575), [C576](#c576), [C577](#c577), [C579](#c579), [C581](#c581), [C582](#c582), [C583](#c583), [C585](#c585), [C586](#c586), [C587](#c587), [C590](#c590) |

| economics | [C012](#c012), [C020](#c020), [C021](#c021), [C022](#c022), [C059](#c059), [C063](#c063), [C064](#c064), [C072](#c072), [C080](#c080), [C089](#c089), [C095](#c095), [C098](#c098), [C102](#c102), [C103](#c103), [C105](#c105), [C114](#c114), [C117](#c117), [C125](#c125), [C137](#c137), [C144](#c144), [C148](#c148), [C151](#c151), [C154](#c154), [C177](#c177), [C180](#c180), [C189](#c189), [C195](#c195), [C212](#c212), [C214](#c214), [C219](#c219), [C248](#c248), [C263](#c263), [C286](#c286), [C292](#c292), [C301](#c301), [C334](#c334), [C343](#c343), [C357](#c357), [C360](#c360), [C367](#c367), [C368](#c368), [C370](#c370), [C374](#c374), [C375](#c375), [C436](#c436), [C437](#c437), [C438](#c438), [C442](#c442), [C447](#c447), [C454](#c454), [C455](#c455), [C476](#c476), [C489](#c489), [C495](#c495), [C535](#c535), [C541](#c541), [C556](#c556), [C557](#c557), [C558](#c558), [C562](#c562), [C568](#c568), [C570](#c570) |

| methodology | [C016](#c016), [C027](#c027), [C032](#c032), [C033](#c033), [C041](#c041), [C056](#c056), [C057](#c057), [C066](#c066), [C106](#c106), [C115](#c115), [C116](#c116), [C130](#c130), [C134](#c134), [C135](#c135), [C139](#c139), [C152](#c152), [C154](#c154), [C159](#c159), [C176](#c176), [C195](#c195), [C200](#c200), [C202](#c202), [C203](#c203), [C204](#c204), [C207](#c207), [C208](#c208), [C209](#c209), [C212](#c212), [C214](#c214), [C217](#c217), [C219](#c219), [C220](#c220), [C223](#c223), [C224](#c224), [C229](#c229), [C230](#c230), [C231](#c231), [C233](#c233), [C234](#c234), [C235](#c235), [C236](#c236), [C237](#c237), [C239](#c239), [C243](#c243), [C244](#c244), [C245](#c245), [C246](#c246), [C247](#c247), [C248](#c248), [C249](#c249), [C251](#c251), [C252](#c252), [C257](#c257), [C258](#c258), [C259](#c259), [C261](#c261), [C262](#c262), [C263](#c263), [C264](#c264), [C266](#c266), [C267](#c267), [C269](#c269), [C271](#c271), [C272](#c272), [C273](#c273), [C274](#c274), [C275](#c275), [C276](#c276), [C277](#c277), [C279](#c279), [C280](#c280), [C281](#c281), [C284](#c284), [C285](#c285), [C287](#c287), [C288](#c288), [C289](#c289), [C290](#c290), [C291](#c291), [C292](#c292), [C294](#c294), [C295](#c295), [C296](#c296), [C298](#c298), [C299](#c299), [C300](#c300), [C302](#c302), [C304](#c304), [C305](#c305), [C308](#c308), [C309](#c309), [C311](#c311), [C312](#c312), [C314](#c314), [C315](#c315), [C316](#c316), [C317](#c317), [C321](#c321), [C322](#c322), [C323](#c323), [C324](#c324), [C326](#c326), [C328](#c328), [C329](#c329), [C330](#c330), [C333](#c333), [C338](#c338), [C339](#c339), [C340](#c340), [C341](#c341), [C342](#c342), [C345](#c345), [C346](#c346), [C347](#c347), [C349](#c349), [C350](#c350), [C351](#c351), [C354](#c354), [C355](#c355), [C357](#c357), [C358](#c358), [C359](#c359), [C360](#c360), [C361](#c361), [C362](#c362), [C363](#c363), [C364](#c364), [C365](#c365), [C366](#c366), [C367](#c367), [C369](#c369), [C370](#c370), [C371](#c371), [C372](#c372), [C373](#c373), [C374](#c374), [C375](#c375), [C376](#c376), [C377](#c377), [C378](#c378), [C379](#c379), [C381](#c381), [C382](#c382), [C383](#c383), [C384](#c384), [C385](#c385), [C387](#c387), [C389](#c389), [C390](#c390), [C391](#c391), [C392](#c392), [C393](#c393), [C394](#c394), [C395](#c395), [C396](#c396), [C397](#c397), [C399](#c399), [C400](#c400), [C401](#c401), [C403](#c403), [C405](#c405), [C407](#c407), [C409](#c409), [C410](#c410), [C411](#c411), [C415](#c415), [C416](#c416), [C419](#c419), [C420](#c420), [C422](#c422), [C423](#c423), [C425](#c425), [C428](#c428), [C431](#c431), [C435](#c435), [C436](#c436), [C437](#c437), [C439](#c439), [C441](#c441), [C443](#c443), [C444](#c444), [C447](#c447), [C448](#c448), [C449](#c449), [C450](#c450), [C451](#c451), [C452](#c452), [C454](#c454), [C456](#c456), [C457](#c457), [C459](#c459), [C460](#c460), [C461](#c461), [C462](#c462), [C464](#c464), [C466](#c466), [C468](#c468), [C469](#c469), [C470](#c470), [C471](#c471), [C472](#c472), [C473](#c473), [C475](#c475), [C476](#c476), [C478](#c478), [C479](#c479), [C480](#c480), [C481](#c481), [C482](#c482), [C483](#c483), [C485](#c485), [C487](#c487), [C488](#c488), [C497](#c497), [C504](#c504), [C509](#c509), [C512](#c512), [C514](#c514), [C516](#c516), [C518](#c518), [C519](#c519), [C520](#c520), [C521](#c521), [C522](#c522), [C524](#c524), [C528](#c528), [C530](#c530), [C532](#c532), [C537](#c537), [C540](#c540), [C541](#c541), [C545](#c545), [C552](#c552), [C554](#c554), [C555](#c555), [C560](#c560), [C562](#c562), [C563](#c563), [C565](#c565), [C566](#c566), [C567](#c567), [C572](#c572), [C575](#c575), [C576](#c576), [C577](#c577), [C578](#c578), [C579](#c579), [C580](#c580), [C581](#c581), [C583](#c583), [C585](#c585), [C586](#c586), [C587](#c587), [C588](#c588), [C590](#c590), [C591](#c591) |


## 3. Discussion-driven taxonomy and evidence assessment

The following is **analysis**, not a restatement of proven causes. The preceding index separates each source contribution from this report's assessment. All qualifying comments are assigned to at least one theme in the comprehensive map below; a comment can have several themes. Repetition is not independent replication, and score/popularity cannot be used because the feeds omit scores. Same-author follow-ups are correlated observations. E2 is detailed self-report, **not** independently reproduced evidence; no comment in this review earns controlled/reproduced E3.

### 3.1 Identity, conversion and weight precision

**Discussion.** Missing identity is the starting problem: [C046](#c046), [C069](#c069), [C097](#c097), [C117](#c117), [C129](#c129), [C132](#c132), [C138](#c138)–[C139](#c139), [C294](#c294), [C345](#c345), [C376](#c376), [C401](#c401) and [C448](#c448) request exact artifacts or settings. OP identifies Qwen3.8-27B but not checkpoint/revision, quantizer or weight precision. [C208](#c208)'s assumption of Q4, [C431](#c431)'s float8 guess, and [C456](#c456)'s 1–2-bit speculation are not OP disclosures. [C390](#c390)–[C391](#c391) say quantizer quality can cause major differences and loops. Some recommendations are **different checkpoints**: Swift, Huihui/heretic/uncensored/security-tuned derivatives, distilled remixes, Flash Next, smaller MoEs and other families. A shared “27B” or “Q4” label does not hold the model constant.

**Disagreement/evidence.** [C187](#c187)–[C188](#c188), [C247](#c247), [C311](#c311), [C338](#c338), [C348](#c348), [C354](#c354), [C430](#c430) and [C472](#c472) favor higher precision; [C311](#c311) reports BF16 versus Q8/Q4 reasoning comparisons but supplies no test artifacts here. [C056](#c056), [C157](#c157), [C159](#c159), [C192](#c192), [C229](#c229), [C233](#c233), [C287](#c287)/C289, [C298](#c298), [C302](#c302), [C399](#c399) and [C444](#c444) report useful low-bit outcomes, often on derivatives, different tasks or custom inference builds. [C233](#c233) even finds Q2 better than their Q4 for a toy game; this is a confounded counterexample, not a recommendation to downgrade everyone. [C151](#c151)/C184/C188's NVFP4 quality-equivalence claims are not validated. [C186](#c186)'s EXL3/vLLM description and [C360](#c360)'s “vllm.cpp” naming need artifact/backend verification, not silent repair by the report.

**Questions.** Exact publisher/revision/conversion/hash? Genuine base model or derivative? Same multimodal components? Which weight format and group/mixed precision? Do reported gains survive identical tasks, sampler, template and budget? [C299](#c299) specifically asks Swift1.5 IQ3_XXS versus original Qwen Q4+ completion/accuracy; no controlled answer is established.

**Low-cost test/remedy candidate.** First identify the installed artifact and conversion metadata; retain a frozen failing task. Only then compare one alternative quant of the **same checkpoint**, if it fits. Measure accepted task completion, tool validity, false success, wall time and memory—not nominal bits or output style. Do not infer that switching to a finetune isolates quantization.

### 3.2 Serving engine, defaults, build and protocol

**Discussion.** Ollama criticism dominates many early comments, but [C001](#c001)'s correct runtime guess does not establish its cause. [C016](#c016)/C176 value exposed controls. Candidate servers/frontends include llama.cpp, vLLM, Unsloth Desktop/Studio, LM Studio/Bionic, oMLX/MLX, ninfer, HyperQwen, Strata/PolyStrata/Basalt, koboldcpp and SGLang/NIM/Dynamo ([C201](#c201)). These are not interchangeable layers. [C202](#c202) explicitly admits its Ollama-fork criticism may be stale. [C130](#c130) recommends supported Ollama launch workflows and official Qwen Code; [C261](#c261) and [C465](#c465) also resist a simple “Ollama cannot work” reading.

**Disagreement/evidence.** [C009](#c009)/C045/C209/C413/C420/C471 report improved outcomes after switching stacks, but artifact, cache, prompt, tools and defaults often change too. [C130](#c130) supplies counterproposals; [C509](#c509) says Ollama exposes tuning controls and [C516](#c516) reports Ollama/Open WebUI/OpenCode working. These claims are also unverified, but categorical incompatibility is not established. [C329](#c329) reports poor same-3090 results across several harnesses, whereas [C408](#c408) reports good 3090 use. [C563](#c563) reports fast but unreliable Q6/Q8-KV inference through LM Studio/Copilot on a32GB R9700; removing Ollama or raising cache precision does not, by itself, settle that counterexample. [C032](#c032)/C033 dispute Strata release stability; [C262](#c262) reports llama.cpp outperforming Strata. [C312](#c312) says vLLM works for a team but specific harnesses overthink; [C108](#c108)/C110/C177 demonstrate a separate Apple/oMLX path. [C152](#c152) raises an actual AMD-driver example; it is not evidence of an NVIDIA or Apple fault.

**Questions.** Runtime/build/backend version, OS/driver, exact API (chat/completions/Anthropic), client/provider translation, streaming/tool behavior, stop tokens and effective parameter overrides? Which single delta explains a switch's result? [C200](#c200) asks whether “optimization” means compiler optimization; [C206](#c206) asks what extra control direct llama.cpp offers when their server already exposes KV/context. These remain mechanism questions, not proof that a rewrite is required.

**Test/remedy candidate.** Log the actual request/response and loaded model identity before migrating. Compare a minimal stock client to the existing harness at identical inputs. If transport/template failures are demonstrated, test an alternate server in an isolated route while holding weights/settings fixed. No production route or configuration was changed for this investigation.

### 3.3 Template, tool parser, thinking flags and speculative paths

**Discussion.** [C075](#c075)/C077 suspect template/streaming errors; [C193](#c193) links fixed templates and [C194](#c194) asks whether they are still needed. [C345](#c345) explicitly asks API/template details; [C482](#c482) says a wrong template was their own major initial cause. [C466](#c466) adds faulty MTP/wrong predictor, missing NVFP4 scales and protocol mismatch as hypotheses; these are distinct mechanisms, not a generic “bad model” explanation. [C298](#c298)/C399/C444 include MTP and preserved-thinking configurations, but run different variants/builds. [C239](#c239)/C240 ask about disabling vision; whether it actually unloads components depends on the implementation, not the wording “vision off.”

**Evidence/disagreement.** No OP rendered prompt, wire trace, parser error, applied template diff, scaling-factor inspection or MTP ablation is supplied. [C482](#c482) is direct experience without a controlled trace. [C193](#c193)'s repository was not compatibility-tested. Current local metadata shows an explicit thinking control in the template, but saved campaign client “thinking off” does **not** prove it reached that branch; reasoning-token telemetry persisted.

**Questions.** Does the server template match the checkpoint and tools schema? Are calls parsed/executed and tool results returned correctly? Are reasoning and final text separated? What does the server do with the requested effort/enable_thinking? Are terminal stops, parser retries or speculative decoding producing the apparent loop? Does [C194](#c194)'s fixed-template advice apply to the current runtime revision?

**Test/remedy candidate.** Replay one tiny valid tool round-trip and one failing request with rendered template/wire data retained locally; inspect finish reason, tool arguments, tool output and reasoning usage. Compare requested versus effective reasoning mode. If MTP is enabled, disable only that feature for a paired trial. Do not install a community template or change format globally merely because its name sounds relevant.

### 3.4 Sampling and repetition controls

**Discussion.** [C046](#c046)/C083/C097/C132 request temperature and related settings. [C171](#c171) attributes loops to temperature/repetition penalties but admits coding inexperience and guesses temp0.3/no-think. [C157](#c157) points to model-card settings (mentions temp1); [C234](#c234) reports temp0.7/min_p0.05 helped; [C298](#c298)/C444 specify temp1/top_p0.95/top_k20/min_p0 with neutral penalties. [C346](#c346) recommends reuse penalties; [C483](#c483) says temperatures/penalties matter; [C569](#c569) supplies a different temperature0.6 recommendation. [C521](#c521) warns against medium effort, [C522](#c522)/C524 dispute that warning, and no matched benchmark is supplied here. These values are not a consensus recipe.

**Evidence/questions.** No controlled OP sampler experiment exists. Are client defaults overriding model defaults? Which values apply to the exact checkpoint/mode? Do outputs change because a sampler changes, a budget changes, or stochastic variance? In the local campaign, temperature0 was requested while current metadata defaults temperature1/top_k20/top_p0.95; other historical effective sampler values are not established.

**Test/remedy candidate.** Establish a single model/mode-recommended baseline after reading the exact artifact's documentation. Use fixed tasks, bounded repeats and frozen budgets; vary one sampler dimension. Inspect repetitive spans and completion correctness. Do not infer every loop needs a repeat penalty; penalties can also damage code/token repetition that is legitimately required.

### 3.5 KV cache precision versus weights

**Discussion.** [C078](#c078), [C108](#c108), [C147](#c147), [C174](#c174), [C245](#c245), [C269](#c269), [C354](#c354), [C459](#c459) and [C466](#c466) warn about aggressive KV quantization, sometimes recommending F16 or Q8 minimum. This is a separate precision axis from weights. [C169](#c169) openly frames lower cache precision as a quality/headroom tradeoff.

**Counterevidence.** [C179](#c179) reports Q4 K/V on RX6800; [C287](#c287)/C289 report Q4 KV success; [C233](#c233) uses q4_0 with a Q2 toy-game result; [C399](#c399) reports Q4_0 K/V; [C444](#c444) reports Q8 K/Q4 V on a 3090; [C458](#c458) uses Q4 KV with Swift. [C186](#c186) uses FP8. [C525](#c525) recommends higher precision for keys than values, and [C555](#c555) reports Q8 K/Q4 V improved over Q4/Q4 in their setup; [C565](#c565) makes broad QAT/FP8 superiority claims without matched evidence. These are unverified, task- and architecture-dependent reports, but they prevent endorsing “below Q8 always fails.” [C245](#c245)/C269 explanations about already-compressed/sparse attention are commenter mechanisms, not measured architectural proof here.

**Questions/test.** What exact K and V types are actually applied? Is cache on GPU, host or unified memory? Is it quantized only after a threshold? At fixed weight artifact and identical occupied context, compare the current cache with a higher-fidelity reference on a small task that fits; then expand context separately. Track recall of constraints, tool validity and task success as well as memory. An equal-VRAM comparison changing both weights and KV answers a different deployment tradeoff, not isolated cache causality. No local historical KV precision is established in the supplied evidence.

### 3.6 Configured, occupied and useful context; rolling windows and compaction

**Discussion.** OP advertises128K, not an observed rendered-prompt length. [C076](#c076)/C176/C467 dispute effective Ollama context; [C294](#c294)/C321/C335 emphasize skills/doc overhead. [C107](#c107)/C179/C294/C423 describe prompt bloat and missing working headroom. [C223](#c223)/C426/C452 suspect compaction losing constraints; [C424](#c424) raises rolling-context/harness settings; [C478](#c478) says some harnesses assume provider-side compaction. [C221](#c221)/C268/C374/C379/C423 suggest persistent Markdown/ADRs and fresh sessions. [C425](#c425) reports Pi+extensions sending26K for “hi” versus OMP12K, countering any universal claim that a brand name guarantees a light prompt.

**Disagreement.** [C094](#c094)/C124/C166/C181/C290/C349 demand very large windows, while [C169](#c169) proposes96K, [C182](#c182) reports80K, [C191](#c191) separates98K configured from66K actual, [C177](#c177) favors128K and [C435](#c435) suggests a diagnostic16K trial. [C107](#c107)'s half-window rule and [C409](#c409)'s60% cleanup threshold are personal heuristics. [C480](#c480) says large windows cured their workflow; [C079](#c079)/C123 still report loops after adjustments. A large maximum is neither occupied context nor proof of retrieval/comprehension at that length. Project LOC, cumulative multi-turn input and per-request tokens are different quantities.

**Questions/test.** Capture per-turn token accounting: system/tools/skills/docs/history/reasoning allowance, loaded capacity, output headroom, compaction events, retained constraints and finish reason. Start with a bounded task and relevant files; add controlled distractors or longer history to locate degradation. Test a concise handoff by checking whether an explicit requirements ledger survives. Then test whether increasing loaded context—not just advertised context—improves accepted completion at tolerable latency. Do not inflate every local task to256K or512K on the strength of universal Reddit claims.

### 3.7 Long thinking, thought loops, mode and budgets

**Discussion.** [C055](#c055)/C079/C123/C164/C300/C346/C451 report pathological or unproductive reasoning; [C075](#c075)/C224/C108/C110 distinguish long coherent reasoning that eventually succeeds. [C407](#c407) asks how long OP waited before calling it a loop. [C175](#c175) suggests a20K thinking stop; [C118](#c118)/C340/C387 advocate Swift variants to shorten reasoning. Swift success is a checkpoint intervention, not simply setting base-model thinking to off.

**Disagreement.** [C090](#c090)/C094/C111/C112/C172/C349/C430 favor high or retained reasoning; [C107](#c107)/C175/C179/C182/C186/C322/C404/C445 favor medium/low/off for some tasks. [C113](#c113) recommends off only for lookup; [C399](#c399) says3.8 needs thinking. [C473](#c473) reports xhigh Swift success on substantial systems/driver work. [C571](#c571) says strong models should plan and small models execute; [C572](#c572) disputes the planning limitation and [C585](#c585) proposes a blinded-judge-worthy paired planning test, not completed results. No mode is proven best for every task. [C311](#c311)'s higher-precision report suggests apparent overthinking may interact with quantization, but no artifacts isolate it.

**Questions/test.** Distinguish repeated identical states/calls, valid long search, lack of knowledge, ambiguous specs, context restart and stalled tools. Measure reasoning tokens, visible output, tool wait time, attempt count, finish reason and total wall time. Try low/medium versus current effort on the **same base checkpoint**, then compare a derivative separately. Use a stall/loop detector based on repeated state plus no progress, not words such as “hmm” alone ([C310](#c310)). Any cap needs an explicit “budget exhausted/parked” result rather than a false success. The local three artifact timeouts were not shown to hit their4096 output cap; treat elapsed-time budget as its own mechanism.

### 3.8 Harness, real tool access and environment

**Discussion.** Many comments recommend Pi/OpenCode/Hermes/Claude Code/Qwen Code/DeepSeek Harness/Bionic or custom agents. [C048](#c048)/C084/C098/C133 stress toolset and orchestration. [C167](#c167) reports hallucination with a broken Hermes container and better Pi results. [C411](#c411) distinguishes file/memory/tool competence from analysis/synthesis on a different9B model and asks where failure first occurs. [C466](#c466) raises protocol mismatch. [C195](#c195) prioritizes identifying failures; [C192](#c192) requires a sandbox for executing tests.

**Disagreement.** [C096](#c096)/C177 favor plain Pi over specific alternatives; [C295](#c295)/C327/C406/C413 show Claude Code can work; [C294](#c294)/C363 call it bloated; [C312](#c312) finds DeepSeek Harness/Claude Code sometimes overthink; [C317](#c317) favors DeepSeek; [C453](#c453) reports Hermes tangling; [C425](#c425) favors OMP over an extension-heavy Pi. These are configuration/workload reports, not a universal harness ranking. Marketing leads such as Atlas([C297](#c297)), localharness([C306](#c306)), Bantam Factory([C462](#c462)), unreleased Sidecar([C478](#c478)) and Optiq([C185](#c185)) are existing-solution leads, not reviewed recommendations or reasons to build a new agent.

**Questions/test.** Can the actual agent list/read the required files, search the repo, see current docs, execute permitted tests and inspect errors? Is the working directory/container correct? Are tool outputs truncated or denied? What automatic retries/compaction happen? Separate one simple tool call, one local edit+test, cross-file planning and long-horizon work. Compare lean versus current tool exposure using the **same tests and response normalization**. The local campaign intentionally denied shell/browser/web/spawn: it did not test a normal coding execution/debug loop.

### 3.9 Workflow, planning, specification and validation

**Discussion.** [C066](#c066)/C070–[C074](#c074)/C097/C212/C214/C217–[C219](#c219)/C268/C338/C374/C375/C409 advocate scoped stories, explicit interfaces, staged plan→implement→test, fresh workers, durable notes and review. [C179](#c179) recommends asking clarification questions before implementation. [C074](#c074) reports XML+CAPS prompts, unablated. [C196](#c196)'s “colocation of complexity” is too underspecified to prescribe. [C212](#c212)/C214 explain BMAD installation/skills and warn of token overhead for small projects; it is not needed merely to test one narrow bugfix.

**Cloud dependency.** [C060](#c060)/C066/C074/C154/C219/C302/C323/C326/C343/C374/C400/C406/C417/C418/C442 describe frontier planning, supervision, review or repair. [C062](#c062)/C064 report token savings without numbers; [C065](#c065) asks for exact local-subagent routing. [C066](#c066) separates scope precheck/coder/validator and notes doubled checks; [C409](#c409) adds serial/round-robin scheduling and a final tester. These describe useful **hybrid** systems, not proof of fully local professional autonomy.

**Questions/test.** Is the model failing task interpretation, architecture, an individual edit, tool execution, testing or final reporting? Can it complete one well-specified repository task with acceptance tests? Does an explicit relevant-files/interface/spec packet help? Compare with/without cloud-authored plans while charging planning/review time to the corresponding arm. Same-model reviewers share errors; use executable assertions and, where warranted, independent review. [C195](#c195)'s40% success/60% parked/zero false-positive claim concerns Qwen3-Coder30B-A3B, not the target dense27B, and lacks a denominator.

**Remedy candidate.** Right-size one task, preserve requirements, run appropriate tests and verify the artifact/diff, mark unresolved work honestly. Then assess whether decomposition overhead still saves human time. Do not create a multiagent factory before knowing whether basic edit+test succeeds.

### 3.10 Knowledge, niche stacks and retrieval

**Discussion.** [C146](#c146) reports20% correct on Drupal11 and speculates about training/LoRA; [C179](#c179)/C186 suggest current references and known library versions. [C133](#c133)/C167/C385 distinguish knowledge from reasoning. [C385](#c385) reports a domain skill improving a security task from~10/38 to27/38, but the evaluation was not reproduced. [C439](#c439) raises niche Luau knowledge. [C454](#c454) gives important negative .NET/Java/Blazor experience despite detailed ninfer settings and extensive experimentation. [C272](#c272)'s20-question closed-book test is a proposal with no model responses/answer key, not a benchmark result. [C275](#c275)'s future-release cure is speculation.

**Questions/test.** Are failures obsolete APIs, missing domain facts or inability to reason with supplied facts? Provide authoritative version-pinned documentation and a local compile/test oracle; compare closed-book versus that reference packet. Check whether retrieval actually reaches the model. Only consider LoRA after repeated residual errors and a representative held-out set; no thread evidence shows training guarantees100% Drupal11 success. Domain tests complement rather than replace multi-turn coding/tool evaluation.

### 3.11 Hardware fit, residency, multimodal overhead and concurrency

**Discussion.** OP: Ryzen5 5500,32GB DDR4,RTX3090 24GB. [C047](#c047)/C190/C334 ask or speculate about team sharing; none establishes actual OP concurrency. [C091](#c091)/C092/C145/C158/C307/C435 estimate memory pressure. [C020](#c020)/C216/C225/C337/C383 propose multi-GPU setups; [C014](#c014)/C066/C098/C105/C186 discuss concurrency, prefix caching or gateway scheduling. [C169](#c169) notes display VRAM; [C239](#c239)/C240 discuss vision. [C251](#c251) suggests host KV placement; [C125](#c125) reports spill reducing6 to1tok/s. [C102](#c102)/C263 raise SSD wear without writes/endurance measurements. [C566](#c566)/C567 explicitly correct RAM-versus-VRAM confusion. [C544](#c544)'s half-precision memory claim is imprecise: a27B×2-byte weight count is about54GB before overhead; use measured artifact bytes, not quoted rules.

**Disagreement.** [C126](#c126)'s parameter-billions≈VRAM-GB rule, [C180](#c180)'s256GB business minimum, [C228](#c228)'s32–36GB floor and [C430](#c430)'s8-bit minimum conflict with smaller-hardware reports [C179](#c179)/C182/C229/C298/C399/C444. [C099](#c099) claims a large model fits12GB+32GB using Strata; [C100](#c100)/C239 ask how and at what speed; [C101](#c101) points to SSD offload. [C277](#c277)–[C285](#c285) dispute10GB versus12GB minimum. [C444](#c444)'s “only VRAM matters” also overreaches: bandwidth, compute, system RAM/storage, prefill, backend, tools and concurrency can change latency and usable deployment.

**Questions/test.** Actual weight/cache/runtime/multimodal bytes, display reservations, host/unified allocations, offload/swap/I/O and per-slot capacity? How many simultaneous requests, and are cache/window allocations per slot or shared? Measure prefill, decode, time-to-first-token, total accepted-task latency and system contention at occupied context. Hardware normally limits fit/speed; intrinsic quality changes require a changed precision/model, lost/truncated context, runtime defect, or operational budget. Do not label slow CPU offload by itself as “lobotomized intelligence.”

**Remedy candidate.** Begin concurrency1. Confirm residency before interpreting failure. Schedule requests or use prefix caching only after baseline correctness. Do not purchase GPUs/RAM or recommend a paid hosted route from unmeasured capacity speculation; [C447](#c447) specifically urges proof of concept before hardware purchase.

### 3.12 Alternatives and expectation boundaries

**Discussion.** Flash Next/Coder via Strata is the most repeated alternative, with many hardware-specific speed reports ([C031](#c031),[C096](#c096),[C099](#c099),[C105](#c105),[C140](#c140),[C148](#c148),[C149](#c149),[C189](#c189),[C204](#c204),[C225](#c225),[C236](#c236),[C264](#c264),[C279](#c279),[C302](#c302),[C313](#c313),[C361](#c361),[C364](#c364),[C367](#c367),[C400](#c400),[C417](#c417),[C446](#c446),[C460](#c460)). [C118](#c118)/C157/C229/C243 prefer dense27B on some persistent/long tasks or report Flash drift. [C499](#c499)/C500/C501/C532/C590 specifically distinguish Strata/Radiance as serving software for a different MoE model rather than a drop-in dense27B fix; actual supported versions still need checking. Other leads include Qwen3.6-35B-A3B, Qwen3-Coder30B, smaller9B/12B, GLM/DeepSeek, Gemma, GPT-OSS, remix/Swift variants and domain-finetunes. Total, active and n-gram/lookup parameter counts are inconsistently reported (125/150/177/180B, and [C461](#c461)'s “Flash Next Coder27B” label); preserve these as source ambiguity, not one verified model identity.

**Capability/economics disagreement.** [C021](#c021)/C089/C098/C137/C144/C315/C436/C442 see a large frontier gap; [C115](#c115)/C159 report fixing frontier mistakes; [C184](#c184)/C395 claim near-Sonnet output with workflow; [C151](#c151) gives balanced5–10-prompt versus1 experience. [C541](#c541) reports Tetris taking2–3h versus Opus20min; [C562](#c562) gives a five-year hardware break-even claim from personal spending assumptions, not a financial study. [C177](#c177) reports~4h versus20min, [C333](#c333) estimates>1h versus2–5min, [C374](#c374)~30min versus5min, [C377](#c377) days versus hours, C3845–10× slower. These are unblinded task-dependent reports, not aggregate productivity measurements. Sonnet parameter-count speculation([C464](#c464)/C479), alleged secret-teacher claims([C316](#c316)), unsourced score ratios([C137](#c137)), and upcoming release forecasts([C080](#c080)/C137/C275) are not accepted facts.

**Test/remedy candidate.** If the same-checkpoint baseline is functional but misses utility targets, trial an already available alternative with identical representative tasks before spending money or building infrastructure. A larger MoE/finetune/hybrid may improve utility but does not explain why OP's original setup failed. Existing-solution leads were surveyed in the discussion; no plugin was installed, repository run, service purchased or custom harness built.

### 3.13 Measurement, honest failures and business value

**Discussion.** [C046](#c046)/C097/C134/C138/C345/C403/C473 request actual inputs/failed traces. [C135](#c135)/C272 propose tests, [C243](#c243) engine-divergence metrics, [C259](#c259) cloud head-to-heads, [C299](#c299) derivative-versus-base trials, [C314](#c314) one-flag-at-a-time tuning, [C195](#c195) honest parking. [C072](#c072) asks the crucial senior-effort-versus-manual-work question. [C066](#c066)/C098/C144/C154/C214/C301/C333/C367/C377/C389/C447/C476 include setup/maintenance/time/financial constraints. Configuring a server with cloud help can work([C020](#c020)/C027/C106/C152/C154), but [C041](#c041) warns generated advice may select poor defaults; [C305](#c305) warns stale model advice.

**Evidence standard.** Keep denominator, task difficulty and failure distribution, not just success screenshots/LOC. Passing some tests, compiling, LLM approval, generating millions of tokens([C342](#c342)), honest refusal and a correct unsupervised legacy refactor are different outcomes. Count human edits, retries, cloud planning/review, stalled tools, false success and total time. No thread-wide success rate or universally best engine/quant follows from this corpus.

**Test/remedy candidate.** Freeze representative real tasks and executable checks, record first-try/final success, false-success, correctly parked, tool validity, iterations, human minutes and wall time. Use identical string-normalization and artifact criteria across direct/harness arms. Include negative cases [C079](#c079)/C123/C146/C300/C329/C454/C563 and do not average toy games with professional legacy work as if equivalent.

## 4. Verified transfer to the user's local environment

This section uses the separately saved [environment-context.md](environment-context.md) and [environment-observation.json](environment-observation.json), not inference from Reddit. Its evidence timestamps are13:31UTC current observation and the earlier saved `20261031T061213Z` campaign. **No inference or fresh benchmark was run for this research.** The file contains precise primary-artifact citations and the full read-only provenance.

| Axis | Reddit OP | Verified local evidence | Consequence for transfer |
| --- | --- | --- | --- |
| Model identity | Qwen3.8-27B named; exact checkpoint/quant unknown | Catalog `qwen/qwen3.8-27b@4bit`, safetensors/MLX; current affine4bit,group64, architecture `qwen3_5`; upstream revision/hash not established | Same family label is established, identical weights/conversion are not |
| Hardware | RTX3090 24GB +32GBDDR4 | Current Apple M5Pro/Mac17,16,64GiB unified-memory host | CUDA/vLLM/ninfer/Strata recipes and discrete-VRAM budgets are not direct fixes |
| Serving | Ollama, unsettled harness (OP and [C486](#c486)) | Saved LMStudio/MLX OpenAI-compatible route; current catalog model not loaded | “Leave Ollama” does not diagnose this local environment |
| Context | Claims128K; actual occupied/loaded context unknown | Evaluated loaded context16,384; initial64,000 was a pre-campaign snapshot; advertised262,144 is maximum, not evaluated | Context/budget realism is directly relevant; do not call prior runs64K/262K |
| Reasoning/sampling | Unknown | Client requested thinkingoff/temperature0; reasoning tokens still observed; other effective samplers/rendered request unknown | Requested mode is not proven effective mode; inspect serialization/template before attributing loops |
| Small operational baseline | No reproducible OP task supplied |27/27 repeated tiny file/paired tasks pass | Narrow competence, not long coding reliability |
| Direct baseline | Not supplied |9/21 pass;12 fail on leading-newline exact-output contract, not wrong arithmetic/classes | Raw-versus-normalized scoring matters; agent arm used `.strip()` and direct arm did not |
| Longer artifact tasks | Vague autonomous coding failures | All3 selected PinchBench artifact-task executions timed out; hello-world file task artifact score1.0 but final executionfail; other2 artifactscore0 | Preserve operational failures; do not hide behind27/27 or call them all output-cap failures |
| Tool/permission scope | Says project docs accessible; actual tool loop unknown | Baseline permitted read/write/edit, denied shell/browser/web/spawn; no real repository compile/test loop demonstrated | Missing coding-tool capability and tiny fixtures limit what campaign proves |
| Production intervention | None established | Lean experiment9/9 matched trials still pass, selected median47.799→39.531s, rejected under retain threshold; production unchanged | Not a proven/deployed reliability remedy |

**Local-specific inference, not diagnosis:** highest-information checks are historical request/template/thinking translation, apples-to-apples scoring, loaded context/budget, and the point where time is spent on artifact-task timeouts. These have direct local evidence. A CUDA engine migration, GPU purchase, “Q8 minimum,” fully disabling reasoning or enlarging to256K do not yet have that evidence. Saved cumulative33,946 input across turns is not proof of one prompt overflowing16K; direct21 responses ending`stop` do not establish no truncation in every other workload.

## 5. Prioritized low-cost, high-information investigation roadmap

**Planning only; none of these interventions was executed.** Effort is rough human preparation/analysis time for a small bounded check, excluding download/inference wait. “Independence” identifies which competing explanations a result can distinguish. Reuse existing tools before building a custom harness. Preserve production behavior and stop tuning when a predeclared oracle has answered the question.

| Priority / investigation | Impact | Relevance | Evidence basis | Effort | Independence / information value | Risk / caveat |
| --- | --- | --- | --- | --- | --- | --- |
| P0a Freeze identity and effective state | High | Both OP and local | Repeated missing-data requests; local upstream hash/effective settings incomplete |15–30min | Removes artifact/version/precision confounds before changes | Low; read-only; keep credentials/private code out of shared traces |
| P0b Inspect one failed task end-to-end | Very high | Both; local timeouts especially | [C134](#c134),[C345](#c345),[C403](#c403),[C407](#c407),[C473](#c473); incomplete causal timing locally |20–45min | Separates model planning, tool denial/parser, waiting, reasoning and deadline failure | Low for saved logs; absence of a trace remains unknown |
| P0c Align the comparison oracle | High | Direct local evidence |12 direct failures were leading newlines; agent grader strips whitespace |10–20min | Separates strict contract adherence from semantic correctness | Report both raw and normalized results; do not silently excuse required contracts |
| P1a Tiny tool round-trip, then one real edit+test | High | Both; prior local suite lacked code execution/debug loop | [C167](#c167),[C192](#c192),[C411](#c411),[C466](#c466) |30–60min | Tests transport/environment and individual edits before architecture | Future execution needs a bounded sandbox; avoid broad permission grants merely to improve score |
| P1b Verify requested/effective thinking, template and API | High | Especially local | [C075](#c075),[C077](#c077),[C193](#c193),[C345](#c345),[C482](#c482); reasoning tokens despite requested off |20–45min plus paired trials | Tests translation/template separately from preferred reasoning effort | No global community-template replacement; sanitize wire logs |
| P1c Token ledger and context/compaction trial | High | Direct local16K evidence; OP128K unverified | [C179](#c179),[C294](#c294),[C321](#c321),[C424](#c424),[C452](#c452) |30–60min | Vary distractors/loaded capacity separately; check retained requirements | Memory/time; configured allocation is not occupied or useful context |
| P1d Separate wall-clock, token and loop budgets | High | Direct local timeout evidence | [C108](#c108),[C123](#c123),[C175](#c175),[C333](#c333); files task1816 output tokens below4096 cap |20–45min | Attributes time to reasoning, tools or engine; defines honest parking | Caps can truncate useful work; unfinished is not success |
| P2a Exact-model sampler baseline | Medium/high if loops persist | Both, variant dependent | [C157](#c157),[C171](#c171),[C234](#c234),[C298](#c298),[C569](#c569) disagree; local requestedtemp0 |20–40min plus bounded repeats | Single sampler delta with artifact/task/budget held fixed | Low; do not tune only one cherry-picked example |
| P2b Lean exposure and specific plan packet | High practical potential | Both | [C066](#c066),[C179](#c179),[C212](#c212),[C294](#c294),[C409](#c409); local lean trial not proven/retained |30–60min | Compares task/tool/doc scope under the same model and oracle | Must retain required constraints; count human preparation time |
| P2c Separate weight and KV fidelity | Conditional high | OP unknown; local4bit weights/KV unknown | High-precision advice conflicts with low-bit successes; [C299](#c299) asks clean comparison |1–3h plus resource cost | Same-checkpoint matrix separates weight from cache changes; equal-memory tradeoff is separate | Reference must fit; no universal bit equivalence or checkpoint swapping disguised as precision test |
| P2d Version-pinned domain reference packet | High for niche failures | When actual work stack is known | [C146](#c146),[C179](#c179),[C186](#c186),[C385](#c385),[C439](#c439),[C454](#c454) |30–60min | Closed-book versus supplied-doc same task isolates knowledge access | Verify retrieved content and executable tests before considering training |
| P3a Existing alternative harness/server | Medium, conditional | After transport/overhead evidence | [C130](#c130),[C176](#c176),[C295](#c295),[C312](#c312),[C425](#c425),[C482](#c482) |1–2h | Keep artifact/tool schema/budget stable where possible | Several defaults often change; local route must support actual Apple/MLX hardware |
| P3b Swift/base or alternative model trial | High utility potential; not original root-cause proof | After functional baseline | [C151](#c151),[C298](#c298),[C299](#c299),[C329](#c329),[C387](#c387),[C454](#c454) |1–3h plus resource cost | Same held-out tasks separate model/finetune utility from sampler effects | Check artifact, license and fit; no paid spend assumed |
| P3c Hybrid worker plus net ROI gate | High if autonomy ceiling remains | Business/legacy work | [C066](#c066),[C098](#c098),[C151](#c151),[C177](#c177),[C374](#c374),[C406](#c406),[C409](#c409); [C072](#c072) asks senior-effort cost |1–2h small trial design | Compare manual/current cloud/local/hybrid including planning, repair, human minutes and false success | Cloud dependency/private-code routing needs defined scope; token savings are not productivity proof |
| Later: serving scale, offload/MTP speed, training or hardware | Conditional | Only after correctness and bottleneck profile | [C047](#c047),[C066](#c066),[C098](#c098),[C239](#c239),[C299](#c299),[C466](#c466) |Hours–days | Tests performance/utility after identifying a bottleneck | Highest confounding/cost/maintenance; purchases and paid rentals were not authorized or made |

### 5.1 Suggested measurement packet and decision gates

**Minimal packet:** immutable model/conversion/runtime IDs; exact input/task+acceptance tests; requested/effective sampler/thinking/context; per-turn prompt/component counts; parsed calls/results/tool denials; finish reason; reasoning/final output tokens; memory/residency/slots; prefill/decode/TTFT/total time; artifacts/diff; human intervention and cloud help. Treat all unspecified fields as unknown, not defaults inferred from a product name.

**Gates:**

1. **Transport/tool gate:** correct one-tool round-trip and expected file visibility. If not, stop capability comparisons and resolve that boundary first.
2. **Bounded usefulness gate:** one representative small real edit passes tests and reports truthfully. Include a negative/unfinishable case to test honest parking.
3. **Context/budget gate:** the same task survives realistic docs/history and finishes within the chosen useful time envelope; compaction retains non-negotiable constraints.
4. **Generalization gate:** several held-out tasks across the user's stack, including multi-file/navigation and a known niche-API issue; preserve failures, not just demonstration wins.
5. **Utility gate:** accepted work per human minute and elapsed hour is competitive for the selected role. If not, route that role to a stronger model/hybrid or do it manually. This is a workload decision, not a verdict that the model is universally useless.

No new model load, code execution test, inference call, install, config/scheduler change, purchase, publication or external message was made for this report.

## 6. Categorized hypothesis and unanswered-question checklist

**Blocker** means missing evidence prevents a defensible causal diagnosis or fair comparison, not that the model cannot run. **Nonblocker** is a conditional hypothesis to test after a basic observable baseline. **Later** is an optimization, deployment or business decision. An unchecked premise is not accepted as true. Every indexed comment also retains its own open questions; the source-question registry preserves question wording and unresolved referents.

### 6.1 Blockers to diagnosis and fair comparison

- [ ] **B01 Exact OP artifact and effective configuration:** checkpoint/publisher/revision, weight quant, K/V precision, sampler, reasoning mode, server/build/API/template, harness and slots. The post and [C486](#c486) establish **Ollama and no settled harness**, not the other values. [C046](#c046),[C069](#c069),[C083](#c083),[C090](#c090),[C095](#c095),[C097](#c097),[C117](#c117),[C120](#c120),[C129](#c129),[C132](#c132),[C138](#c138),[C139](#c139),[C174](#c174),[C175](#c175),[C294](#c294),[C345](#c345),[C376](#c376),[C401](#c401),[C419](#c419),[C431](#c431),[C448](#c448),[C456](#c456),[C578](#c578).
- [ ] **B02 A representative failed task and actual received prompt/trace:** what did “basic” mean, and where did it first fail—understanding, cross-file planning, an individual edit, a tool, a test, or final reporting? [C097](#c097),[C134](#c134),[C403](#c403),[C407](#c407),[C411](#c411),[C473](#c473). Toy-game screenshots and proposed closed-book tests do not supply OP's reproduction.
- [ ] **B03 Effective context and budget:** loaded versus advertised capacity; occupied prompt components; reasoning/output headroom; truncation, rolling-context and compaction policy. [C076](#c076),[C085](#c085),[C107](#c107),[C127](#c127),[C169](#c169),[C170](#c170),[C179](#c179),[C294](#c294),[C321](#c321),[C424](#c424),[C425](#c425),[C452](#c452),[C467](#c467),[C478](#c478). Keep the local **16K evaluation**, initial64K snapshot and advertised262K capability distinct.
- [ ] **B04 Requested versus effective thinking/template/tool protocol:** local client “off” still produced reasoning tokens. Inspect rendered prompts and wire behavior. [C075](#c075),[C077](#c077),[C193](#c193),[C194](#c194),[C345](#c345),[C466](#c466),[C482](#c482).
- [ ] **B05 Local artifact-task timeout mechanism:** elapsed time spent reasoning, stalled engine/tool, denied capability, retries, context handling and per-task wall-clock limit are not separated. The records do not show that all three simply exhausted their4096-token output cap.
- [ ] **B06 Comparable oracle and completion definition:** raw versus normalized final strings; artifact creation versus correctness versus final completion. Local27/27 tiny tasks do not erase three broader timeouts. [C195](#c195),[C259](#c259),[C299](#c299),[C403](#c403) and local grader evidence.
- [ ] **B07 OP concurrency and resource assumption:** one machine per developer or shared; active users/requests, slots, per-slot context and memory? [C047](#c047),[C190](#c190),[C334](#c334),[C470](#c470),[C472](#c472),[C529](#c529). This blocks team-capacity conclusions, not single-task inspection.
- [ ] **B08 Coverage certification:** Atom omits parent/depth, scores and `more` markers. The eight-count discrepancy cannot be classified into removed versus omitted versus snapshot drift. All collected comments were reviewed; full Reddit-tree completeness is not certified.

### 6.2 Nonblocking, targeted hypotheses

- [ ] **N01 Sampler or repetition-control interaction:** [C157](#c157),[C171](#c171),[C234](#c234),[C298](#c298),[C346](#c346),[C444](#c444),[C483](#c483),[C569](#c569). Which exact checkpoint/mode defaults apply? Different numeric suggestions are not a consensus.
- [ ] **N02 Weight versus KV precision:** [C078](#c078),[C108](#c108),[C147](#c147),[C174](#c174),[C233](#c233),[C245](#c245),[C247](#c247),[C269](#c269),[C287](#c287),[C289](#c289),[C311](#c311),[C399](#c399),[C444](#c444),[C458](#c458),[C459](#c459),[C525](#c525),[C555](#c555),[C565](#c565). Can low-bit successes and high-bit improvements be reproduced with checkpoint, task and budget fixed? Do K and V need different treatment?
- [ ] **N03 Unproductive loops versus valid long search versus waiting:** how long did OP wait, what states/calls actually repeat, and what effort/budget changes help? [C079](#c079),[C108](#c108),[C110](#c110),[C123](#c123),[C164](#c164),[C175](#c175),[C224](#c224),[C300](#c300),[C407](#c407),[C454](#c454),[C473](#c473),[C521](#c521),[C522](#c522),[C524](#c524).
- [ ] **N04 Prompt overhead and compaction loss:** [C179](#c179),[C221](#c221),[C223](#c223),[C294](#c294),[C321](#c321),[C335](#c335),[C374](#c374),[C379](#c379),[C423](#c423),[C425](#c425),[C426](#c426),[C452](#c452),[C478](#c478),[C480](#c480). Does the actual “lean” setup preserve required constraints and leave working headroom?
- [ ] **N05 Functional tools and environment:** [C133](#c133),[C167](#c167),[C192](#c192),[C411](#c411),[C435](#c435),[C442](#c442),[C466](#c466),[C580](#c580). Can the agent read/search/edit/run the appropriate tests, receive errors and honor denials rather than hallucinate success?
- [ ] **N06 Specification, scope and validation:** [C066](#c066),[C070](#c070),[C073](#c073),[C074](#c074),[C097](#c097),[C212](#c212),[C214](#c214),[C217](#c217),[C218](#c218),[C219](#c219),[C268](#c268),[C338](#c338),[C374](#c374),[C375](#c375),[C409](#c409),[C571](#c571),[C572](#c572). Does a plan/scope packet help, and does the extra briefing/review still save senior effort ([C072](#c072))?
- [ ] **N07 Domain knowledge/current APIs:** Drupal11([C146](#c146)/C275), Luau([C439](#c439)), .NET/Java/Blazor([C454](#c454)), current libraries([C179](#c179)/C186), domain skills([C385](#c385)). Is authoritative reference access sufficient before considering training?
- [ ] **N08 Residency, offload, display and vision:** [C091](#c091),[C092](#c092),[C125](#c125),[C169](#c169),[C239](#c239),[C240](#c240),[C251](#c251),[C252](#c252),[C307](#c307),[C403](#c403),[C435](#c435),[C544](#c544),[C566](#c566),[C567](#c567). Do errors change, or just latency and task deadlines? What does disabling vision actually unload?
- [ ] **N09 Build/driver/API/MTP defects:** [C152](#c152),[C176](#c176),[C193](#c193),[C298](#c298),[C345](#c345),[C399](#c399),[C444](#c444),[C466](#c466),[C482](#c482). Is one controlled delta responsible, or several simultaneously changed components?
- [ ] **N10 Are fixed templates still needed?** [C194](#c194) asks this and whether they improve tool calling. Inspect the actual current template/runtime revisions; no demonstrated answer is supplied.
- [ ] **N11 Reproducible harness/configuration comparisons:** [C017](#c017)/C206 ask direct-llama.cpp benefits; [C422](#c422)/C356/C382/C587 ask which harness; [C082](#c082)/C288 ask hardware/agent details; [C067](#c067)/C204 ask a full repeatable configuration. Neither a universally best harness nor complete replication package is established.
- [ ] **N12 Fast inference but unreliable agents:** [C563](#c563)'s Q6/Q8-KV LM Studio/Copilot setup asks for targeted advice despite near-instant first token. Compare effective prompts/tools with direct inference; speed and higher precision alone are not correctness gates.

### 6.3 Later or conditional opportunities/questions

- [ ] **L01 Swift/base and precision head-to-head:** [C220](#c220) licensing, [C233](#c233) Q2/Q4 surprise, [C299](#c299) identical-task SwiftIQ3_XXS versus originalQ4+, [C303](#c303) whyQ8 rather than more, [C348](#c348)/C387 variant claims, [C530](#c530) artifact link request. Verify exact identity/license and held-out quality; no such trial was run here.
- [ ] **L02 Larger MoE and resource fit:** [C013](#c013) vLLM on dual3090; [C100](#c100)/C103/C104/C239 large-model fit/speed/coding; [C237](#c237) skepticism; [C253](#c253)/C27610GB use cases; [C278](#c278) API connection; [C281](#c281)/C283/C28410GB versus12GB minimum; C3045080 fit; C25824+12 layout; [C365](#c365)/C366 CPU correction; C55412GB response latency. Measure filled-context prefill/decode, resident bytes and accepted tasks rather than only “it loads.”
- [ ] **L03 Hybrid routing and replication:** [C061](#c061)/C063/C065 local Copilot subagent routing/savings; [C211](#c211) assignment; [C213](#c213) BMAD adoption; [C249](#c249) source availability; [C260](#c260) Codex/llama backend; [C271](#c271) example prompt; [C378](#c378) prompts/C379 full setup; [C396](#c396) workflow; [C504](#c504) unspecified mainline-version question; [C511](#c511) LM Studio versus Unsloth UI; [C520](#c520) specification-detail question. Partial architecture answers are not a complete versioned configuration or numeric ROI.
- [ ] **L04 Concurrency/gateway/cache/MTP speed work:** [C014](#c014),[C066](#c066),[C098](#c098),[C105](#c105),[C186](#c186),[C225](#c225),[C334](#c334),[C383](#c383),[C409](#c409),[C446](#c446),[C466](#c466),[C472](#c472),[C495](#c495),[C541](#c541),[C555](#c555),[C558](#c558). Verify per-slot capacity, filled-context behavior, schedule and single-task correctness before scaling.
- [ ] **L05 Evaluation instrumentation and generalization:** [C195](#c195) honest parking on a different model, [C243](#c243) engine divergence, [C259](#c259) cloud head-to-head, [C272](#c272) proposed closed-book test, [C299](#c299) controlled variant test, [C314](#c314) one flag at a time, [C585](#c585) paired planning with a model judge. Fix tasks/rubrics, blind/randomize judges where appropriate and include held-out failures.
- [ ] **L06 Net business value:** [C072](#c072),[C098](#c098),[C144](#c144),[C151](#c151),[C177](#c177),[C214](#c214),[C300](#c300),[C301](#c301),[C333](#c333),[C367](#c367),[C374](#c374),[C377](#c377),[C384](#c384),[C389](#c389),[C436](#c436),[C442](#c442),[C447](#c447),[C476](#c476),[C541](#c541),[C562](#c562). Include setup, senior review, repair, latency, maintenance, power and opportunity cost before buying hardware or renting inference.
- [ ] **L07 Public-project/release claims:** HyperQwen/ninfer([C136](#c136),[C143](#c143),[C197](#c197),[C318](#c318),[C373](#c373),[C480](#c480)), advertised platforms([C297](#c297),[C306](#c306),[C462](#c462),[C478](#c478),[C574](#c574),[C581](#c581)), future Qwen([C080](#c080),[C137](#c137),[C275](#c275)), parameter/teacher claims([C316](#c316),[C464](#c464),[C479](#c479)). Unverified leads, not prerequisites to start diagnosis. [C591](#c591)'s “why would this matter?” cannot be assigned a specific factor without its missing parent.
- [ ] **L08 Peripheral privacy question:** [C019](#c019) asks what LM Studio allegedly sends to a “data lake” after [C018](#c018)'s unsupported allegation. Preserved but excluded from reliability findings; not an established privacy issue.



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


## 8. Evidence limits, artifacts and review audit

- **Coverage:**591 IDs include589 readable bodies and2 deleted placeholders;534 qualifying and57 exclusions.599 was an earlier public counter, not a synchronized complete tree. More-node counts, unseen removals, tree depths and low-score completeness remain unknown. No comment score/popularity ranking was inferred.
- **Evidence:** linked code, tests, screenshots, benchmarks, model cards, products, releases and financial claims were not independently benchmarked or compatibility-certified. The source thread itself is the focus. A recipe or detailed firsthand report remains E2, not a reproduced fix. Runtime/quant/finetune/hardware changes are frequently confounded.
- **Scope:** initial independent reviewer covered C001–C198 only; separate nonoverlapping index passes covered C199–C300,C301–C400,C401–C484,C485–C591. The owner reviewed additional contributions, final-range disagreements and all consolidated records. The initial review is not represented as a second independent reading of all591.
- **No implementation:** only research-directory artifacts were written. No production configuration/scheduler/model/route/permission changed; no installation, fresh inference, spend, external message or public post occurred.
- **Primary saved artifacts:** [report](report.md), [normalized JSON corpus](comment-corpus.json), [readable full source corpus](comment-corpus.md), [all dispositions and assessments](qualifying-comment-index.json), [coverage](coverage.json), [question registry](source-question-registry.md), [initial-scope independent reviewer notes](reviewer-notes.md), [verified environment evidence](environment-context.md), [environment observation](environment-observation.json), [manifest](artifact-manifest.json). Original XML/HTML and retrieval logs are retained in the same directory.

## 9. Executive summary — last

1. **There is no supported single root cause for OP.** The thread establishes Ollama and an unsettled harness, but omits exact weights/KV/sampling/template/effective context and a reproducible failed task. “Ollama,” “24GB,” or “27B” alone is not a diagnosis.
2. **Useful local coding is credible; frontier-like autonomy is not established.** Detailed positive reports coexist with persistent loops, niche-stack failures, fast-but-unreliable agents, much greater supervision and large wall-clock gaps. Many successes include cloud planning/review or different fine-tunes/hardware. No universal Q8, F16-KV,256K or xhigh/off requirement survives the reported counterexamples.
3. **The user's local evidence points to different first questions.** It is an Apple/MLX4bit setup evaluated at16K, not OP's3090/Ollama setup. Tiny27/27 workflows,12 whitespace-contract direct failures and three broader timeouts measure different things. Client “thinking off” was not proven effective. Start with request/template/score/budget observability, not a CUDA migration or hardware purchase.
4. **Best next information per cost:** freeze identity; inspect one failed trace; align raw/normalized scoring; verify a tiny tool loop and real edit+test; measure effective thinking, context and timeout causes; then test scope/sampling, separate weights from KV, and only later compare an existing alternative model/harness or hybrid workflow with honest time/quality accounting.
5. **Coverage is substantial but explicitly qualified:**591 distinct comment IDs,589 readable bodies reviewed,534 qualifying entries,57 exclusions including2 deleted. Eight IDs' worth of public-counter discrepancy remains unclassified; hidden removals, `more` gaps, scores and a complete comment tree cannot be certified. All collected material and individual source links are preserved for audit.
