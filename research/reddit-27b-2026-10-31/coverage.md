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

