from pathlib import Path
import json,re,xml.etree.ElementTree as E,collections,hashlib,datetime
p=Path(__file__).parent
corpus=json.loads((p/'comment-corpus.json').read_text());by={c['ref']:c for c in corpus};rows=[]
for name in ['index-001-198.json','index-199-300.json','index-301-400.json','index-401-484.json','index-485-591.json']:
 rows.extend(json.loads((p/name).read_text()))
assert len(rows)==591 and len({r['ref'] for r in rows})==591
assert {r['ref'] for r in rows}==set(by)-{'OP'}
for r in rows:
 for field in ['author','permalink']:assert r[field]==by[r['ref']][field],(r['ref'],field)
 for field in ['contribution','type','relevance','evidence','open_questions','transferability','themes']:assert field in r,(r['ref'],field)
 if r['disposition']=='qualifying':assert r['themes'],r['ref']
rows.sort(key=lambda r:int(r['ref'][1:]));qual=[r for r in rows if r['disposition']=='qualifying'];exc=[r for r in rows if r['disposition']=='excluded']
assert len(qual)==534 and len(exc)==57
ns={'a':'http://www.w3.org/2005/Atom'};seen=set();feedrows=[];versions={}
feeds=['rss-response','rss-limit500.xml','rss-limit1000.xml','rss-old.xml','rss-new.xml','rss-controversial.xml','rss-top.xml','rss-confidence.xml']
for filename in feeds:
 es=E.fromstring((p/filename).read_bytes()).findall('a:entry',ns);ids={e.findtext('a:id',namespaces=ns) for e in es if e.findtext('a:id',namespaces=ns).startswith('t1_')}
 feedrows.append({'file':filename,'entries_including_post':len(es),'comment_ids':len(ids),'new_comment_ids':len(ids-seen),'sha256':hashlib.sha256((p/filename).read_bytes()).hexdigest()});seen|=ids
 for e in es:
  i=e.findtext('a:id',namespaces=ns);b=e.findtext('a:content',namespaces=ns);versions.setdefault(i,{}).setdefault(b,[]).append(filename)
assert seen=={c['id'] for c in corpus if c['ref']!='OP'}
variants={next(c['ref'] for c in corpus if c['id']==i):[{'body_html':b,'sources':fs} for b,fs in v.items()] for i,v in versions.items() if len(v)>1}
(p/'comment-body-variants.json').write_text(json.dumps(variants,indent=2,ensure_ascii=False))
coverage={'canonical_url':by['OP']['permalink'],'title':'Local Qwen 27B is practically unusable for coding tasks. Are we doing something wrong?','collection_last_success_utc':'2026-10-31T13:40:43.128659+00:00','post_count':1,'distinct_comment_ids':591,'readable_comment_bodies':589,'deleted_placeholders':2,'removed_placeholders_observed':0,'removed_total':'unknown','qualifying_comments':534,'excluded_total':57,'readable_excluded':55,'displayed_comment_counter':599,'displayed_counter_source':'embed-response contains View 599 comments; earlier snapshot than final RSS union','counter_minus_collected_ids':8,'counter_discrepancy_explanation':'Unknown: omitted/hidden/deleted/removed items or temporal drift; not eight proven removed comments.','more_nodes_observed_in_atom':0,'more_node_total':'unknown: Atom does not serialize Reddit morechildren markers','parent_ids_available':False,'comment_scores_available':False,'comment_depths_available':False,'low_score_coverage_certified':False,'full_tree_completeness_certified':False,'review_complete_for_collected_corpus':True,'body_variant_count':len(variants),'feeds':feedrows,'independent_reviewer_scope':'C001–C198 only; partition indexers reviewed remaining fixed non-overlapping ranges','no_implementation_or_config_changes':True}
(p/'coverage.json').write_text(json.dumps(coverage,indent=2));(p/'qualifying-comment-index.json').write_text(json.dumps(rows,indent=2,ensure_ascii=False))
def arr(v):return v if isinstance(v,list) else [v]
def linked(s):
 s=str(s)
 return re.sub(r'(?<![\w/])C(\d{3})(?!\d)',lambda m:'[C'+m[1]+'](#c'+m[1]+')',s)
def codequote(s):return '\n'.join('> '+line for line in s.splitlines())
def questions(r):
 c=by[r['ref']];return '?' in c['body'] or 'question' in r['type'].lower() or 'request' in r['type'].lower()
questionrows=[r for r in qual if questions(r)];qparts=['## 7. Source-question registry\n\nThis registry conservatively includes every qualifying source comment containing a question mark or indexed as a question/request. Full source bodies are quoted, so rhetorical questions and ambiguous pronouns are not silently reinterpreted. It is a preservation registry, not a list of proven unanswered technical facts. OP+C486 answer the engine name (Ollama) and say the harness is unsettled; many other responses provide suggestions without a verified resolution. No parent IDs are available to prove reply relationships. The index assessment lists remaining gaps.\n']
for r in questionrows:
 qparts.append('### '+r['ref']+' — '+r['author']+'\n\n[Direct source]('+r['permalink']+') · [Index assessment](#'+r['ref'].lower()+')\n\n'+codequote(by[r['ref']]['body'])+'\n\n**Remaining questions / verification:** '+'; '.join(arr(r['open_questions']))+'\n')
qparts.append('### Peripheral excluded question, preserved explicitly\n\nC019 asks what information LM Studio allegedly sends after C018\'s unsubstantiated allegation. It is unanswered in the collected evidence, excluded from reliability findings, and not accepted as a privacy finding. [C019 source]('+by['C019']['permalink']+')\n')
registry='\n'.join(qparts);(p/'source-question-registry.md').write_text(registry)
header=f'''# Local Qwen 27B coding reliability: exhaustive review of the accessible Reddit corpus

**Thread:** [{coverage['title']}]({coverage['canonical_url']})  
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
| Duplicate body versions |{len(variants)} differing bodies found across successful feed snapshots |

The share URL resolved to the canonical thread above. Normal HTML returned a challenge shell; browser displayed **“Prove your humanity”** with reCAPTCHA, and that route was not advanced. Public JSON/API requests returned403; old Reddit redirected to login. The ordinary public Atom endpoint succeeded. Rate-limited429 attempts were not treated as content; later retries followed the stated reset. No challenge/login/security control was bypassed and no cookies were imported. Five comment sort orders, plus different feed limits, were collected and unioned by exact Reddit comment ID. Last three ranking views added no IDs beyond591. This improves recall but does not reveal invisible IDs or reconstruct `morechildren`.

**Honest limitation:** the requested complete tree, exact removed count and exact continuation-gap count are not verifiable from the accessible interfaces. No content, deleted author, score, parent, or gap count has been invented to close that difference. Feeds flatten comments: apparent exchanges are discussed cautiously, not reconstructed as a proven tree. Source permalinks are those supplied by Reddit's feed; every permalink was not separately browser-opened through the challenge.

### 0.2 Successful source inventory

| Saved source | Entries including post | Comment IDs | New IDs added to union |
| --- | ---: | ---: | ---: |
'''
for f in feedrows:header+=f"| [{f['file']}]({f['file']}) |{f['entries_including_post']}|{f['comment_ids']}|{f['new_comment_ids']}|\n"
header+='''
Raw XML, failed-attempt logs, initial HTML, embed HTML, normalized JSON/Markdown corpus, index JSON and coverage JSON are retained alongside this report. `artifact-manifest.json` provides sizes and SHA256 hashes. Stable refs C001–C591 were assigned on first encounter and never renumbered: they do **not** encode time, depth, popularity or relevance. OP is separate from C486, the OP's collected clarification comment.

### 0.3 OP disclosures, not assumed diagnoses

The original post states Ryzen5 5500,32GBDDR4,RTX3090 24GB; Qwen3.8-27B with a claimed128K context; comparison with Claude Sonnet5.5 Medium; instruction difficulty, repetitive reasoning/loops and inability to finish allegedly simple coding tasks in the same project/docs. The edit and C486 identify **Ollama** and an unsettled harness. Exact weight/KV quant, effective sampler/thinking, runtime build, applied template, actual occupied context, concurrency and a failed task trace are not supplied. No other user's guesses fill these gaps.

OP's five questions are preserved: capability/configuration;24GB/128K hardware limits; inference/quant/context choices; similar-size local alternatives; actual experiences with coding-agent harnesses. The post also asks whether expectations or setup are wrong and requests legacy-codebase experience. Full original text is the OP record in [comment-corpus.md](comment-corpus.md).

### 0.4 Index/evidence rules

“Contribution” is a faithful summary of the commenter, not this report asserting the claim is true. “Relevance,” “open questions” and “transferability” are analysis and explicitly distinct. E0 = question, proposal or unsupported assertion; E1 = vague firsthand report; E2 = setup/task-specific firsthand account or concrete recipe **without independent verification**. E3 would require controlled/reproduced evidence and is not attained here. Counts are dispositions, not votes or independent experiments. Several comments by one author are correlated; a recommendation repeated by many authors is still not a causal test.

Exclusions cover empty reactions, jokes, insults, redundant bare crossreferences, privacy tangent and unreadable deleted records. Borderline methodological dissent/questions were retained conservatively, even when low relevance. All534 qualifying entries come next, **before synthesis**.

## 1. Individual qualifying-comment index

'''
parts=[header]
for r in qual:
 parts.append(f"<a id=\"{r['ref'].lower()}\"></a>\n\n### {r['ref']} — u/{r['author']}\n\n**Direct permalink:** [{r['permalink']}]({r['permalink']})\n\n- **Faithful contribution:** {r['contribution']}\n- **Type:** {r['type']}\n- **Why relevant (assessment):** {r['relevance']}\n- **Evidence quality:** {r['evidence']}\n- **Open questions / verification gaps:** {'; '.join(arr(r['open_questions']))}\n- **Transferability (inference):** {r['transferability']}\n- **Themes:** {', '.join(r['themes'])}\n")
parts.append('## 1.1 Exclusions ledger\n\nAll57 excluded IDs remain in the raw corpus.55 had readable text;2 were deleted. Reasons below explain exclusion from technical synthesis, not a judgment of the author.\n\n| Ref | Author | Type | Reason / preserved contribution |\n| --- | --- | --- | --- |\n')
for r in exc:
 reason=r.get('exclusion_reason') or r['relevance'];parts.append(f"| <a id=\"{r['ref'].lower()}\"></a>[{r['ref']}]({r['permalink']}) | {r['author']} | {r['type']} | {str(reason).replace('|','/')} {r['contribution'].replace('|','/')} |\n")
counts=collections.Counter()
for r in exc:
 if by[r['ref']]['body']=='[deleted]':k='Deleted/unreadable'
 elif 'privacy' in r['type']:k='Peripheral privacy tangent'
 elif any(x in (r['type']+' '+r.get('exclusion_reason','')).lower() for x in ['crossreference','cross-reference','cross reference','bare link']):k='Redundant crossreference/no self-contained detail'
 elif any(x in (r['type']+' '+r.get('exclusion_reason','')).lower() for x in ['attack','insult','dismiss','authorship']):k='Insult/dismissal/authorship speculation'
 else:k='Reaction/joke/agreement/no additional substance'
 counts[k]+=1
parts.append('\n**Exclusion reason groups:** '+ '; '.join(k+': '+str(v) for k,v in counts.items())+'. These groups partition57; specific reasons are in the ledger.\n')
parts.append('\n## 2. Comprehensive theme-to-comment map\n\nEvery qualifying C-ref appears in at least one row. Links lead to the individual entry and its direct Reddit permalink. This is a discussion map, not evidence-weighted consensus; detailed disagreements/tests follow.\n\n| Theme | Qualifying comments |\n| --- | --- |\n')
themes=['runtime','sampling','template','kv','weights','context','harness','workflow','reasoning','knowledge','hardware','alternatives','economics','methodology']
for t in themes:parts.append('| '+t+' | '+', '.join('['+r['ref']+'](#'+r['ref'].lower()+')' for r in qual if t in r['themes'])+' |\n')
parts.append('\n'+linked((p/'synthesis.md').read_text()))
parts.append('\n'+registry)
parts.append('''
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
''')
report='\n'.join(parts)
# Link refs in framing paragraphs as well; never reprocess index headings/URLs or existing link targets.
(p/'report.md').write_text(report)
(p/'coverage.md').write_text(header[:header.index('## 1. Individual')])
(p/'qa.json').write_text(json.dumps({'comment_records':len(rows),'qualifying':len(qual),'excluded':len(exc),'source_question_comments':len(questionrows),'all_refs_unique':True,'all_source_author_links_match':True,'all_qualifying_have_required_fields_and_themes':True,'feed_union_matches_corpus':True,'body_variants':len(variants),'all_children_terminal':True,'executive_summary_last':True,'exclusion_groups':counts},indent=2))
manifest=[]
for f in sorted(p.iterdir()):
 if f.is_file() and f.name!='artifact-manifest.json':manifest.append({'file':f.name,'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
(p/'artifact-manifest.json').write_text(json.dumps(manifest,indent=2))
print(json.dumps({'report_bytes':len(report.encode()),'corpus_entries':len(corpus),'readable_comments':589,'qualifying':len(qual),'excluded':len(exc),'source_question_comments':len(questionrows),'feeds':feedrows,'exclusion_groups':counts},indent=2))
