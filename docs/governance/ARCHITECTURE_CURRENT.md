# Architecture Current

**Document type:** Verified current-architecture description  
**Authority class:** Owner-approved architecture discovery output (not product authority)  
**Status:** Approved — Authoritative  
**Scope:** Evidence-based description of what this ApplyPilot fork **actually does today**, how it works, what can be reused, and gaps versus approved product requirements  
**Governing method:** `ARCHITECTURE_DISCOVERY_STANDARD.md` (Approved — Authoritative)  
**Does not define:** Implementation plan, target design alone, or silent changes to PRD/policy  

---

## Document control

| Field | Value |
|-------|--------|
| Product | Personal autonomous AI job-search and job-application agent (ApplyPilot fork) |
| Discovery date | 2026-08-13 |
| Evidence basis | Static code/config/test inspection; prior repository audit; current official vendor documentation for candidate technologies and Playwright MCP |
| Runtime validation | **Not performed** in this task (no installs, credentials, or pipeline execution authorized) |
| Companion authorities | Documents 1–6 Approved — Authoritative |
| Change control | Future material updates require re-discovery of affected areas and deliberate review |

### Evidence labels used in this document

| Label | Meaning |
|-------|---------|
| **FACT** | Directly established from current code, config, or tests |
| **DOCUMENTED** | Stated by inherited docs/comments/changelog; not independently proven |
| **INFERENCE** | Reasoned interpretation from evidence |
| **UNKNOWN** | Insufficient evidence; needs runtime or external validation |

---

## 1. Executive architecture summary

**FACT —** ApplyPilot is a Python 3.11+ package (`applypilot` CLI) with:

1. **Tier 1/2 pipeline** — discover → enrich → score → tailor → cover → pdf (`pipeline.STAGE_ORDER`).  
2. **Tier 3 apply** — Claude Code subprocess + Playwright MCP over CDP into per-worker Chrome (+ extension when headed).  
3. **Tracking** — separate `applypilot track` Gmail scan/classify/match loop.  

**FACT —** There is **no** in-repo orchestrator that continuously closes:

discover → qualify → prepare → apply → verify → track → replenish → repeat.

**FACT —** Queue selection remains largely **artifact-column-driven**, while a parallel **state machine** (`jobs.state` + `job_state_transitions`) is audit/secondary and frequently force-updated.

**FACT —** Scoring/prefilter and employer registries encode a prior developer’s **Seattle senior IC engineering** search strategy — wrong product persona (IC eng vs approved AI consulting/advisory/enablement target).

**FACT —** The inherited scorer hard-rejects titles including Sales Engineer, Solutions Engineer, Pre-sales, AE/AM. The approved product **does** generally intend to reject engineering-heavy SE/Solutions Engineer roles and pure sales roles that do not fit the target profile — but **title alone must not be the final qualification determination**; substantive JD analysis must decide fit unless an independently approved deterministic eligibility rule applies.

**FACT —** Highest concrete security risks: Claude `--permission-mode bypassPermissions` with secrets in prompts; unauthenticated localhost worker APIs with `Access-Control-Allow-Origin: *` returning plaintext passwords. Inherited CapSolver CAPTCHA automation exists in the apply path and is **not** part of the approved production architecture (must be removed/disabled; security challenges → HITL).

**FACT —** Windows is partially supported for paths/process kill; Chrome for Testing install/preference and several desktop integrations are Linux-oriented — **UNKNOWN** end-to-end without runtime validation.

---

## 2. Repository topology

```
src/applypilot/
  cli.py, __main__.py, pipeline.py, config.py, database.py, llm.py, view.py
  discovery/     jobspy, workday, greenhouse, lever, ashby, amazon, costco,
                 builtin, hackernews, smartextract, url_normalize, ats_common
  enrichment/    detail.py (Patchright)
  scoring/       scorer, tailor, cover_letter, validator, pdf, json_resume
  apply/         launcher, orchestrator, hitl, result_handlers, chrome, prompt,
                 successful_paths, human_review, dashboard, extension/
  tracking/      gmail_client, triage, classifier, matcher, ghosting, markdown_gen
  wizard/        init.py
  config/        employers.yaml, sites.yaml, greenhouse/lever/ashby registries, examples
tests/           ~30 modules / ~338 test functions
scripts/         install_cft.py (linux64), gmail_oauth.py, smoke_cft.py, qa_tailored_docs.py
docs/            governance/, guidelines/jobscan/, seattle_employers_*.yaml, superpowers/
```

**FACT —** Entry: `pyproject.toml` → `applypilot.cli:app`; `python -m applypilot`.

---

## 3. Current end-to-end pipeline

| Stage | Entry | Modules | Continuous? |
|-------|-------|---------|-------------|
| Discover | `pipeline._run_discover` | JobSpy, Workday, Greenhouse, Lever, Ashby, Amazon, Costco, BuiltIn, HN, SmartExtract | Finite crawl |
| Enrich | `enrichment.detail.run_enrichment` | JSON-LD → CSS → LLM; Patchright | Finite / stream poll |
| Score | `scoring.scorer.run_scoring` | Prefilter + LLM | Finite / stream poll |
| Tailor | `scoring.tailor.run_tailoring` | LLM JSON → validate → DOCX/PDF | Finite / stream poll |
| Cover | `scoring.cover_letter.run_cover_letters` | Quality LLM + reject path | Finite / stream poll |
| PDF | `scoring.pdf.batch_convert` | Tailored-dir only (default limit 50) | Finite |
| Apply | `cli.apply` → `orchestrator.main` → `launcher.run_job` | Claude Code + Chrome | Polling workers (see §5) |
| Track | `cli.track` → `tracking.run_tracking` | Gmail MCP | **One-shot** per invocation |

**FACT —** Apply and track are **not** members of `STAGE_ORDER`.

**FACT —** `run --stream` runs concurrent finite stage threads; discovery runs once then downstream polls until pending=0 (`pipeline.py`).

---

## 4. Current autonomy model

| Question | Answer |
|----------|--------|
| End-to-end continuous closed loop without manual stage commands? | **No (FACT)** |
| What exists | Finite `run` / `run --stream`; apply workers poll DB; track is one-shot |
| What breaks the loop | No scheduler; track not continuous; Tier 2/3 gates; HITL/credit stops; no replenish orchestration |
| `apply --continuous` | Polls apply-ready queue only; does **not** rediscover/score/tailor |
| INFERENCE | Plain `applypilot apply` with default `limit=None` also behaves as continuous (limit→0) |

**Required (PRD):** continuous closed loop.  
**Current:** external supervisor would be required.

---

## 5. Discovery architecture

### Active sources (FACT — wired in `_run_discover`)

| Source | Registry/API | Notes |
|--------|--------------|-------|
| JobSpy | Indeed + LinkedIn defaults | ZipRecruiter removed (Cloudflare 403); docstring/README still mention it |
| Workday | `config/employers.yaml` | CXS API; may not emit initial state transitions |
| Greenhouse | `greenhouse_employers.yaml` | boards-api; `ats_common` transitions |
| Lever | `lever_employers.yaml` | public JSON API |
| Ashby | `ashby_employers.yaml` | posting API |
| Amazon | hard-coded Seattle/WA filter | public search.json |
| Costco | hard-coded Seattle location | retail noise scored later |
| BuiltIn | config cities/categories | HTML SSR |
| Hacker News | Algolia + Firebase + LLM | location prefilter |
| SmartExtract | `sites.yaml` | Patchright + optional LLM |

### Seattle employer YAMLs

| File | Runtime refs | Tests | Docs |
|------|--------------|-------|------|
| `docs/seattle_employers_v1.yaml` | **None** | **None** | Research / greenhouse comments |
| `docs/seattle_employers_v2.yaml` | **None** | **None** | Research |
| `docs/seattle_employers_v3_megacorps.yaml` | **None** | **None** | Research; candidate-specific fields |

**Disposition recommendation:** **MIGRATE** still-useful ATS identifiers into runtime registries → then **ARCHIVE** as provenance. Do **not** KEEP as runtime config. Do **not** REMOVE until migration. Do **not** invent Atlanta replacements merely because Seattle files exist.

### Config schema drift (FACT)

- JobSpy expects `sites` + flat `location_accept`.  
- Example YAML uses `boards` + nested `accept_patterns`.  
- Wizard emits neither consistently.  
**INFERENCE —** Fresh installs can silently mis-filter locations.

---

## 6. Qualification / scoring architecture

**Path:** `scoring/scorer.py` → `get_jobs_by_stage("pending_score")`.

| Aspect | Current behavior |
|--------|------------------|
| Deterministic filter | `_check_ineligible` title/location/desc patterns |
| LLM | Fast client; JD truncated to **6000** chars |
| Company field | Still `COMPANY: {job['site']}` (aggregators as employer) |
| Defaults | `min_score=8`, age 14d (`config.DEFAULTS`) |
| Persona | Hardcoded Seattle Senior/Staff IC eng + Go/Kotlin/Python/Java |
| Sales/SE titles | **FACT —** Hard-rejected by title string (`Sales Engineer`, `Solutions Engineer`, Pre-sales, AE/AM) before substantive JD evaluation |
| Prefilter label bug | Role mismatches reported as “non-US geography in title” |
| State | Transitions to `scored` / `low_score` / `archived`; queue still column-derived |

**Architectural gap (role classification):** The approved product **generally wants** to reject engineering-heavy Sales Engineer / Solutions Engineer roles and pure quota-carrying sales roles that lack AI consulting/advisory/enablement fit. Titles may be strong positive or negative signals. The defect in the inherited architecture is **not** that those role classes are treated as negative — it is that **title alone is treated as final qualification**. Target behavior must evaluate actual JD responsibilities/requirements (e.g. hands-on coding/architecture/APIs/deployment → normally reject; title containing Sales/Solutions/Pre-sales/AE/AM whose responsibilities substantially match the approved consulting profile → evaluate from JD, not auto-reject by title) except where an independently approved deterministic eligibility rule applies.

**Other gaps vs PRD:** No exemplar-job semantic scoring; persona/scoring still IC-engineering-centered rather than AI consulting/advisory; JD truncated; aggregator `site` used as company.

---

## 7. Resume / ATS optimization architecture

**Path:** `resume.txt` + `profile.resume_facts` → `tailor.py` → JSON validate → optional judge → DOCX/PDF → `tailored_resumes/`.

| Gate 2 PRD need | Current |
|-----------------|---------|
| Pre-tailor screening analysis | **Missing** as product capability |
| Evidence mapping (supported/underrepresented/…) | **Missing** |
| Affirmative maximize truthful passage | Partial keyword/title emphasis only |
| Post-tailor screening analysis | **Missing** |
| Historical title integrity | **Contradicted** — inherited tailor prompt can require the target job title verbatim in a way that risks rewriting historical employment titles. Approved direction: historical employment titles must not be falsified; truthful use of the target title in non-historical positioning (heading, summary, objective/positioning, skills/contextual language) remains permitted for ATS optimization |
| Factual integrity | Partial (`resume_facts`, watchlist); “related tools” allowed; judge advisory on final retry |
| Jobscan docs | **Not loaded**; rules hand-copied into code |
| Parse-back validation | **Missing** |
| Exact submitted freeze | **Missing** — re-tailor overwrites same URL-hash filename |
| Format preservation | DOCX renderer exists; degradation risk **UNKNOWN** without corpus tests |

**Cover letters:** use **base** `resume.txt`, not tailored resume; hard validation rejects; inline convert.  
**PDF stage:** scans `TAILORED_DIR` only — not full cover pipeline.

---

## 8. Cover-letter / document rendering

- **FACT —** Generated when cover stage runs; quality LLM; company via `display_company()`.  
- **FACT —** Failed drafts → `_CL_rejected.txt` + `cover_failed`.  
- **FACT —** Apply acquisition does **not** require `cover_letter_path`.  
- **INFERENCE —** Cover PDF via resume parser path may mis-render prose (known prior audit concern).  
- **UNKNOWN —** Runtime cover DOCX quality without execution.

---

## 9. Browser / Claude application architecture

```
orchestrator.worker_loop
  → chrome.launch_chrome (subprocess Chrome + CDP)
  → launcher.run_job
       → build_prompt (secrets, QA, paths, CapSolver)
       → claude --strict-mcp-config --permission-mode bypassPermissions
       → @playwright/mcp@0.0.75 connects to CDP
       → stream-json parse RESULT:*
  → mark_result / transition_state
```

| Component | Role today |
|-----------|------------|
| Claude Code | Form reasoning agent; filesystem; MCP browser tools |
| Playwright MCP | Browser automation over CDP (pinned 0.0.75) |
| Patchright | Enrichment/PDF/smartextract/**tests** — **not** production apply launch |
| Chrome | Direct `Popen`; extension when headed |
| Chrome for Testing | Preferred **Linux only** in `get_chrome_path` |
| Extension | Stealth MAIN-world, action log, popup, options |
| Sessions | `chrome-sessions/{ats}` whitelist copy |
| successful_paths | Per-ATS tool memo; keep-fastest; 30d |
| HITL | `hitl._run_hitl`; banner + Done; stdin fallback one worker |
| Result | Explicit RESULT lines + phrase inference |

**Official docs note (Playwright MCP):** Microsoft `@playwright/mcp` is the supported package; Node ≥18/20 per current docs; ApplyPilot pins `0.0.75` and uses `--strict-mcp-config` to avoid Docker MCP shadowing (**FACT** in launcher comments/code).

---

## 10. Claude Code execution architecture

| Item | Finding |
|------|---------|
| Spawn | `claude --model … -p --mcp-config … --strict-mcp-config --permission-mode bypassPermissions --no-session-persistence --output-format stream-json` |
| Env | Copy of parent; strips `ANTHROPIC_API_KEY`, `CLAUDECODE`, `CLAUDE_CODE_ENTRYPOINT` |
| Secrets still in env | Gemini/OpenAI/CapSolver/etc. may remain (**FACT**) |
| Secrets in prompt | CapSolver key, account passwords, profile (**FACT** — `prompt.py`) |
| Gmail MCP | Read allowed; many write tools disallowed |
| Billing assumption | Strip API key → Max plan (**DOCUMENTED/INFERENCE** — vendor policy can change; **UNKNOWN** current Anthropic rules without fresh Max-plan validation) |
| Abstraction | **None** — hard-coded `claude` command |

---

## 11. Windows runtime architecture

| Area | Classification |
|------|----------------|
| `pathlib` / `APP_DIR` / SQLite | Windows-compatible as-is |
| Chrome Stable discovery | Configuration/runtime — finds Stable |
| CfT preference / `install_cft.py` | Code change required (linux64-only) |
| Extension on Chrome 137+ | Likely code change / CHROME_PATH to CfT — **UNKNOWN** until runtime |
| `taskkill` / netstat cleanup | Windows-compatible as-is |
| `/proc` reconnect | Code change required |
| `notify-send` / wmctrl/xdotool | Obsolete on Windows / silent fail |
| `--ozone-platform=x11` | Unknown/ignored? |
| openssl for extension key | Configuration required or fallback static key |
| Claude/npx on PATH | Unknown until runtime |
| End-to-end apply on Windows | **UNKNOWN — needs validation** |

**WSL:** Not required by evidence; evaluate only if Windows-native browser path fails after remediation (**not mandatory**).

---

## 12. ATS capability matrix

Legend: **S**=supported path exists · **P**=partial (detect/session/generic agent) · **U**=unsupported/manual · **?=unknown needs validation**

| ATS / flow | Discover | Detect | Session | Form fill | Upload | Screening | Submit | Verify | Outcome |
|------------|----------|--------|---------|-----------|--------|-----------|--------|--------|---------|
| Greenhouse | S | S | S | P/? | P/? | P/? | P/? | U | P (email) |
| Lever | S | S | S | P/? | P/? | P/? | P/? | U | P |
| Ashby | S | S | S | P/? | P/? | P/? | P/? | U | P |
| Workday | S (API) | S | S | **U** (manual_ats skip) | U | U | U | U | P |
| iCIMS | — | S | S | P (prompt rules) | P/? | P/? | P/? | U | P |
| Taleo/Oracle | — | S | S | P/? | P/? | P/? | P/? | U | P |
| SuccessFactors | — | S | S | P/? | P/? | P/? | P/? | U | P |
| SmartRecruiters | — | S | S | P/? | P/? | P/? | P/? | U | P |
| ADP / UKG / Jobvite | — | S | S | P/? | P/? | P/? | P/? | U | P |
| Indeed/LinkedIn Easy Apply | JobSpy | weak | — | often manual | — | — | — | U | P |
| Custom employer sites | SmartExtract/? | none | none | generic Claude | P/? | P/? | P/? | U | ? |
| Unknown redirect ATS | — | none | none | generic Claude attempt | ? | ? | ? | U | ? |

**FACT —** `sites.yaml` `manual_ats` includes `myworkdayjobs.com` — acquire skips before automation.  
**FACT —** Dedicated apply prompt rules exist for Greenhouse, Lever, iCIMS, Workday (but Workday skipped).  
**INFERENCE —** “Supported” in marketing sense ≠ validated end-to-end success; most cells are **PARTIAL/?** without runtime ATS corpus.

---

## 13. Unknown ATS fallback

**FACT —** Undetected hosts still get Claude + Playwright MCP with generic prompt (iframe ATS shortcut, form fill, CapSolver, HITL).  
**FACT —** No session overlay / successful_path key when `detect_ats` returns empty.  
**FACT —** Failures → park/fail/HITL via result handlers — not silent discard of all unknowns.  
**Gap vs PRD:** Generic Layer 1 exists in spirit; weak verification, security, and durable learning; Workday explicitly excluded from auto-apply despite discovery.  
**Target direction (CAPTCHA):** Inherited CapSolver automation must be removed/disabled from the production apply path; CAPTCHA/MFA/device-verification challenges route to approved HITL only.

---

## 14. Account / session / credential architecture

| Store | Location | Notes |
|-------|----------|-------|
| Profile password | `~/.applypilot/profile.json` | Wizard solicits plaintext (**FACT**) |
| ATS accounts | SQLite `accounts` | Plaintext; options API returns full passwords |
| Chrome sessions | `chrome-sessions/{ats}` | Shared per ATS slug, not per employer |
| Gmail OAuth | `~/.gmail-mcp/*.json` | Desktop app; scopes modify + settings.basic |
| Apply env | Inherited to Claude | CapSolver key/env may be present (**FACT** — inherited) |

**MFA/CAPTCHA — current vs target:**

| | |
|--|--|
| **CURRENT ARCHITECTURE (FACT)** | CapSolver capability is wired into the apply prompt/path; HITL park also exists |
| **TARGET DIRECTION (approved governance)** | Automated CAPTCHA solving / CAPTCHA circumvention is **not** part of production application architecture. CapSolver must be **REMOVED/DISABLED** from the production apply path. CAPTCHA, MFA, device verification, or comparable security-control challenges must route to approved HITL |

---

## 15. Security / trust boundaries

### Trust boundary map (FACT/INFERENCE)

| Untrusted input | Enters | Privileged effect |
|-----------------|--------|-------------------|
| JD / page a11y tree / forms | Claude prompt + tools | Browser actions, file read/write, shell via bypassPermissions |
| Email bodies | Classifier LLM; apply Gmail read tools | State transitions; potential injection |
| Extension action logs | Post-HITL prompt | Model steering |

### P0 (before real apply)

1. **`bypassPermissions` + secrets in prompt** (including inherited CapSolver key, passwords, profile).  
2. **Unauthenticated localhost API** (`7380+wid`) with CORS `*` and plaintext password GET.  
3. **Prompt injection** — instructional defenses only.  
4. **Inherited CapSolver production path** — must be removed/disabled before real apply; CAPTCHA/MFA → HITL only.  

### P1 (before unattended)

5. Env secret inheritance into Claude/MCP children (including CapSolver remnants).  
6. Shared ATS sessions across employers.  
7. Dry-run can mark `applied`.  
8. Success inference from phrases.  
9. Wizard/profile plaintext password practice vs governance.

---

## 16. Submission verification

```
RESULT:APPLIED|SUCCESS|ALREADY_APPLIED  → applied
else _infer_result_from_output(phrases) → applied
```

**FACT —** No independent DOM/email/ID verifier.  
**FACT —** `verification_confidence` column unused.  
**Gap vs PRD:** ATTEMPTED ≠ SUBMITTED ≠ VERIFIED SUBMITTED **not implemented**.

---

## 17. Q&A / screening-question architecture

- **FACT —** Exact normalized MD5 match; no semantic equivalence engine.  
- **FACT —** Sources: agent / human / profile; accept on applied.  
- **FACT —** Novel Q → `SCREENING_Q` + TUI HITL.  
- **Gap vs policy:** Hierarchy exists partially; missing safe-derivation policy engine and equivalence.

---

## 18. Gmail / tracking architecture

- **FACT —** `applypilot track` one-shot; MCP `@gongrzhe/server-gmail-autoauth-mcp@1.1.11`.  
- **FACT —** Triage → selective LLM classify → weighted match (≥40) → label → ghosting (7d) → markdown.  
- **FACT —** Classifier confidence not persisted.  
- **FACT —** No dedicated tracking tests.  
- **Official Google docs:** OAuth scopes/token lifecycle must be re-validated before dedicated mailbox architecture finalization (**UNKNOWN** vs current MCP behavior).  
- **PRD:** Dedicated mailbox required; email not sole outcome source — owner-reported path **missing**.

---

## 19. Outcome / state architecture

**FACT —** 23 `VALID_STATES` including `responded`, `interview`, `offer`, `rejected`, `ghosted`.  

**Missing vs PRD progression model:** recruiter-screen scheduled/completed, HM interview stages, assessment stages, owner-reported provenance, corroboration objects, immutable application snapshots.

Tracking maps: confirmation/follow_up→responded; interview→interview; offer→offer; rejection→rejected; ghosted→ghosted.

---

## 20. Operator Console reuse assessment

| Component | Recommendation |
|-----------|----------------|
| `view.py` HTML dashboard | **EXTEND** presentation; migrate to canonical `state` |
| `apply/dashboard.py` Rich TUI | **ENGINEERING-ONLY** / preserve for operators |
| Extension options + worker HTTP API | **REUSE AS BACKEND** after **HARDEN** (auth, CORS, secret redaction) |
| CLI `status`/`qa`/`creds`/`track` | **ENGINEERING-ONLY** + metrics source |
| HITL banner/Done/action-log | **EXTEND** into console HITL surface |
| Natural-language control | **ADD NEW CAPABILITY** (none today) |

**Do not** treat current dashboard as sufficient owner console.

---

## 21. Natural-language control readiness

**FACT —** No `OWNER MESSAGE → INTENT → ENTITY → POLICY → ACTION → STATE → AUDIT` pipeline exists.

Reusable structured operations (candidates): pause/resume flags (new), mark applied/failed, Q&A store, prefs write, acquire status queries, artifact path lookup — must be wrapped behind policy-checked service boundary (**ADD**).

---

## 22. Outcome-learning readiness

| Required evidence | Present? |
|-------------------|----------|
| JD snapshot (`_JOB.txt`) | Partial — can be overwritten |
| Exact submitted resume freeze | **No** |
| Pre/post screening analysis | **No** |
| Screening Q/A with provenance | Partial |
| Outcome + provenance | Email only; no owner-reported |
| Versioned candidate profile | **No** |

**INFERENCE —** Cannot safely learn from interview-producing resume/JD pairs without new immutable application artifact store.

**Do not** select ML stack yet — data binding missing first.

---

## 23. Persistence / database architecture

- **FACT —** SQLite + WAL; thread-local connections; `ensure_columns` ALTER migrations.  
- **FACT —** `transition_state` does not always own transactions; many `force=True`.  
- **FACT —** Acquisition/locking in `launcher.acquire_job`.  
- **SQLite sufficiency:** Adequate for single-user local agent **INFERENCE**; pressure points = concurrent writers, large blobs, multi-device.  
- **Do not replace** without evidence.

---

## 24. Concurrency architecture

- **FACT —** Per-worker Chrome profile, CDP/HTTP ports, work dirs, MCP configs.  
- **FACT —** Company + ATS-family mutex in acquire.  
- **FACT —** Resume copies per worker after wipe.  
- **Risks:** shared ATS sessions; successful_path false positives; stream pending loops; dry-run→applied; no Windows reconnect.

---

## 25. LLM / provider architecture

| Call | Intended client | Caveat |
|------|-----------------|--------|
| Score, HN, enrich fallback, judge, classifier | fast | OK |
| Tailor, cover | `quality=True` | **Only quality chain if `LLM_MODEL_QUALITY` set** — else fast (**FACT**) |
| Fallback | Gemini → OpenAI → DeepSeek → Anthropic | Local-only broken |

Model IDs in code may be stale vs vendor current offerings — **re-validate before production** (**UNKNOWN** without live provider docs check per model).

---

## 26. Cost architecture

| Center | Class |
|--------|-------|
| Gemini/OpenAI/Anthropic Tier 2 | Current required (if used) |
| Claude Code Max / API Tier 3 | Current required for apply |
| JobSpy / board scraping | Current (mostly free/local) |
| CapSolver | Inherited current capability — **must not remain** in production cost/architecture (REMOVE/DISABLE; CAPTCHA → HITL) |
| Gmail API via MCP | Current if tracking |
| Firecrawl etc. | Future optional |
| Operator Console hosting | Future if non-local |
| Storage of artifacts | Current local disk |

No dollar estimates without telemetry (**UNKNOWN**).

---

## 27. Dependency architecture

| Dependency | Constraint | Role | Notes |
|------------|------------|------|-------|
| playwright | ≥1.40 | PDF/enrich + npm 1.60 test | Overlaps Patchright |
| patchright | ≥1.50 | Enrich/PDF/smartextract | Not apply launch |
| @playwright/mcp | 0.0.75 pin | Apply browser | Official Microsoft package; pin vs `@latest` |
| python-jobspy | ≥1.1 / separate install | Discovery | Fragile pins historically |
| mcp | ≥1.9 | MCP clients | |
| python-docx / pypdf | floors | Artifacts | |
| httpx, typer, rich, pyyaml, pandas, bs4 | floors | Core | No lockfile |

---

## 28. Candidate technology evaluation

Evaluated against **current official/project documentation** (2026-08-13 web review). **Not installed.**

| Technology | Role vs ApplyPilot | Verdict | Reasoning |
|------------|-------------------|---------|-----------|
| **Anthropic Agent Skills** | Folders of procedural instructions (`SKILL.md`); API/Claude Code support ([Anthropic engineering / platform skills docs](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)) | **EVALUATE LATER** / **ENGINEERING-ONLY** first | Useful for packaging apply/screening procedures; does **not** replace durable state, security sandbox, or Operator Console. Runtime product use needs design after trust-boundary hardening. |
| **Playwright MCP** | Already core apply path (`@playwright/mcp`) ([playwright.dev/mcp](https://playwright.dev/docs/getting-started-mcp)) | **ADOPT (already)** + **HARDEN** | Keep pinned/strict-mcp-config; upgrade path must be tested; do not add duplicate MCP servers (Docker interference already documented). |
| **Firecrawl** | Hosted scrape/extract API ([docs.firecrawl.dev](https://docs.firecrawl.dev)) | **EVALUATE LATER** | Could help enrichment/discovery reliability; adds cost, vendor lock-in, PII/JD egress; overlaps Patchright/SmartExtract. Not needed for V1 core if enrich hardened. |
| **claude-mem** | Third-party Claude Code memory plugin ([github.com/thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)); billing/harness policy risks noted in project issues | **REJECT** for product runtime; **ENGINEERING-ONLY** optional | Conversation memory ≠ durable application state. Conflicts with “conversation is not system of record.” Extra subprocess/billing complexity. |
| **planning-with-files** | Agent skill writing `task_plan.md` etc. ([github.com/OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files)) | **ENGINEERING-ONLY** | Helps Cursor/Claude Code engineering sessions; not a product Operator Console or application state store. |

---

## 29. Configuration architecture

| Source | Contents |
|--------|----------|
| `~/.applypilot/.env` | API keys |
| `profile.json` | Candidate + password field |
| `searches.yaml` | Queries/locations (schema inconsistent) |
| Package YAML registries | Employers/sites/ATS |
| `company_limits.yaml` | Caps |
| `config.DEFAULTS` | Funnel magic numbers |
| CLI flags | min-score, workers, stream, dry-run, no-hitl |
| DB state | Runtime truth for jobs |

Precedence is ad hoc — **INFERENCE:** env + CLI override defaults; scrapers disagree on search schema.

---

## 30. Data classification

| Class | Store | Sensitivity |
|-------|-------|-------------|
| Candidate facts | profile, resume.txt | High |
| Secrets | .env, accounts, gmail-mcp, CapSolver in prompts | Critical |
| Job/JD | SQLite, `_JOB.txt` | Medium |
| Artifacts | tailored_resumes, cover_letters | High |
| Q&A | SQLite | High |
| Outcomes | tracking_emails, state | Medium |
| Owner NL instructions | **N/A** | — |
| Learning evidence | **N/A** | — |
| Logs | logs/, worker logs | High (may contain secrets) |

---

## 31. Failure / recovery

| Failure | Behavior |
|---------|----------|
| Browser crash | HITL may recover; Windows reconnect **unsupported** |
| Worker crash | Job may stick in_progress until stale-lock clear |
| Machine restart | Apply continuous must be restarted manually; pause not durable product control |
| Model 429 | Fallback + cooldown |
| Gmail token expiry | Reauth via options/script; track may fail |
| ATS session expiry | Clear session + login HITL |
| CAPTCHA/MFA | **Current:** CapSolver and/or HITL park. **Target:** HITL only (CapSolver removed/disabled) |
| DB lock | retry helpers in places |
| Interrupted submit | Ambiguous — may infer applied incorrectly |

---

## 32. Observability

| Surface | Sees |
|---------|------|
| `status` CLI | Funnel/legacy stages |
| HTML dashboard | Cards, resumes, logs, tracking |
| Rich apply dashboard | Workers/cost |
| Extension popup | Live worker control |
| Apply logs | Tool stream (line-buffered) |
| Blind spots | Verification evidence, owner NL audit, learning, true continuous loop health, Windows extension load |

---

## 33. HITL architecture

- Unified `_run_hitl`; parks `needs_human`; banner Done; action-log resume.  
- Screening Q via terminal TUI.  
- Standalone `human-review` **deleted**; stale messages remain.  
- Gap: Operator Console HITL path **missing**.

---

## 34. Duplicate / identity handling

- URL normalize + Greenhouse canonicalize (`url_normalize.py`).  
- Apply-time duplicate `application_url` check.  
- Company key resolution for caps.  
- Tailored filename = URL hash prefix.  
- Residual risk: cross-board same req; dry-run applied; Workday manual vs re-entry.

---

## 35. Developer-specific / historical artifacts

| Artifact | Disposition |
|----------|-------------|
| `docs/seattle_employers_v*.yaml` | MIGRATE→ARCHIVE |
| `docs/superpowers/**` | ARCHIVE (historical plans) |
| `docs/guidelines/jobscan/**` | KEEP as reference research |
| Scorer Seattle/IC persona + hard title rejection | REPLACE persona; ADAPT qualification so titles are signals, not sole final determination (eng-heavy SE/Solutions Engineer and pure sales remain intended negatives when JD confirms) |
| Amazon/Costco Seattle hardcodes | ADAPT to config |
| `CLAUDE.md` tracked despite gitignore | ENGINEERING hygiene — untrack/local |
| Changelog stuck at 0.3.0 / version 0.2.0 | DOCUMENTATION remediation |
| Stale human-review strings | HARDEN cleanup |

---

## 36. Preserve / harden / adapt / replace / remove / add / defer matrix

| Subsystem | Recommendation | Rationale |
|-----------|----------------|-----------|
| Pipeline stages CLI | PRESERVE | Sound conveyor |
| Stream mode | PRESERVE + HARDEN | Fix pending-loop / selector drift |
| Discovery scrapers + registries | PRESERVE + ADAPT | Generalize geo; fix schemas |
| Seattle YAML research | MIGRATE then ARCHIVE | Not runtime |
| Scorer | REPLACE persona + ADAPT qualification architecture | Wrong IC-eng persona; hard title rejection must become JD-substantive evaluation (eng-heavy SE/Solutions Engineer and pure sales remain intended negatives) |
| Tailor/validator/DOCX | ADAPT | Gate 2 loop; preserve historical employment titles; allow truthful non-historical target-title positioning |
| CapSolver apply integration | REMOVE / DISABLE | Inherited CAPTCHA automation not allowed in production; challenges → HITL |
| Cover | ADAPT | Use tailored resume; conditional policy |
| Claude+Playwright MCP apply | PRESERVE + HARDEN | Core value; security/permissions |
| Patchright enrich | PRESERVE | Works for Tier 2 browser |
| Extension | PRESERVE + HARDEN | Stealth/action-log; auth options API |
| Localhost worker API | HARDEN (auth/CORS) or REPLACE surface | P0 |
| successful_paths | PRESERVE + HARDEN | Gate on verified submit |
| State machine | ADAPT | Make authoritative or sync |
| SQLite | PRESERVE | Sufficient for personal agent |
| Gmail tracking | PRESERVE + ADAPT | Dedicated mailbox; persist confidence |
| HTML dashboard | EXTEND → console backend | Not final UI |
| Operator Console NL | ADD | Required by PRD |
| Outcome learning store | ADD | Immutable artifacts first |
| Continuous orchestrator | ADD | Required by PRD |
| Workday auto-apply | ADAPT (remove blanket manual or justify) | Discovery exists; apply blocked |
| Firecrawl | DEFER | Optional enrich |
| claude-mem | REJECT (product) | Wrong abstraction |
| planning-with-files | ENGINEERING-ONLY | Dev sessions |

---

## 37. Gap analysis vs approved PRD / policy

| Approved requirement | Current architecture |
|----------------------|----------------------|
| Continuous closed loop | Missing orchestrator |
| AI consulting vs eng-heavy / pure-sales intelligence | Inherited scorer uses IC-eng persona + **hard title rejection** for Sales Engineer / Solutions Engineer / Pre-sales / AE/AM. Approved intent still treats engineering-heavy SE/Solutions Engineer and non-fitting pure sales as negatives, but requires **substantive JD analysis** — title alone must not be final qualification (except independently approved deterministic eligibility rules) |
| Exemplar jobs | Missing |
| Gate 2 pre/post screening loop | Missing |
| Historical employment title integrity | Inherited tailor prompt can require target title verbatim in a way that risks rewriting historical titles. Approved: no false historical titles; truthful target-title positioning outside employment history remains allowed |
| Attempted≠submitted≠verified | Missing |
| Operator Console NL | Missing |
| Owner-reported outcomes | Missing |
| Outcome learning on frozen artifacts | Missing |
| ATS-agnostic Layer 1 | Partial generic Claude |
| Workday applications | Manual skip |
| Dedicated mailbox | Configurable but not productized |
| Max safe autonomy + minimal HITL | HITL works; security blocks unattended |
| Autonomy: no fabrication | Partial validators |
| Autonomy: no automated CAPTCHA solving | **FACT —** CapSolver exists in inherited apply path. **Target —** remove/disable; CAPTCHA/MFA/security challenges → HITL only (resolved by approved governance; not an open owner decision) |
| Windows supported deployment | Partial; CfT gap |

**Governance conflicts with code:** Implementation does not redefine PRD (PRD wins). Conflicts are **implementation gaps**. CapSolver vs approved “no automated CAPTCHA solving / circumvention” is a **resolved disposition**: REMOVE/DISABLE from production apply architecture.

---

## 38. Blockers before Windows baseline

1. Windows Chrome for Testing install/path story (`install_cft.py` linux-only).  
2. Validate extension load on chosen Chrome build.  
3. PATH readiness: Python venv, Node/npx, Claude Code, openssl optional.  
4. Document silent failures (notify-send, focus, /proc).  

---

## 39. Blockers before first real application

1. P0 security (permissions, localhost API, secrets in prompts).  
2. Candidate persona/scoring rewrite: replace IC-eng persona; replace hard title-final rejection with JD-substantive qualification (engineering-heavy SE/Solutions Engineer and non-fitting pure sales remain intended negatives).  
3. Tailor policy: forbid rewriting historical employment titles; allow truthful non-historical target-title positioning; factual validation.  
4. Submission verification mechanism (even minimal).  
5. Windows browser/extension readiness.  
6. Dry-run must not write `applied`.  
7. Owner-authorized Level 5 controlled submit (process).  
8. Remove/disable CapSolver (and CapSolver secrets) from production apply path; ensure CAPTCHA/MFA/device verification route to HITL only.

---

## 40. Blockers before continuous unattended operation

1. All §39 items.  
2. Continuous orchestrator + durable pause/stop.  
3. Security testing of prompt-injection boundaries.  
4. Operator Console HITL path (or equivalent).  
5. Credit/quota stop reliability.  
6. Outcome tracking + owner-reported path.  
7. Artifact binding + immutable submissions.  
8. Observability of system-wide stop.

---

## 41. Uncertainty register

| # | Question | Why it matters | Resolve by | Blocks? |
|---|----------|----------------|------------|---------|
| U1 | Does Windows Stable Chrome load the extension post-137? | Apply stealth/HITL/options | Runtime with CfT vs Stable | Yes for baseline |
| U2 | Current Claude Max vs API billing rules for this harness | Cost/auth | Official Anthropic docs + controlled probe | Apply cost |
| U3 | Live ATS success rates per vendor | Matrix accuracy | Controlled dry-run corpus | Claimed support |
| U4 | *(resolved)* CapSolver / automated CAPTCHA | Disposition fixed by approved governance: REMOVE/DISABLE from production; CAPTCHA/MFA → HITL | Engineering removal + HITL path verification | Yes until removed |
| U5 | Cover letter DOCX render quality | Gate 3 | Runtime render fixture | Cover ship |
| U6 | Gmail MCP refresh during `track` | Tracking reliability | Runtime with tokens | Track |
| U7 | Stream infinite-loop on capped pending | Ops reliability | Runtime/stream test | Stream mode |
| U8 | Whether `verification_confidence` ever had writers | Schema cleanup | DB archaeology optional | No |
| U9 | Playwright MCP 0.0.75 vs current MCP tool schema | Upgrade risk | Diff official changelog + regression | Apply upgrade |
| U10 | Local LLM primary path | Offline Tier 2 | Code+runtime | Optional |

---

## 42. Recommended target-architecture direction

1. **Harden current apply spine** (Claude + Playwright MCP + Chrome + extension) rather than rewrite — after security and Windows CfT.  
2. **Add durable product services** for: continuous orchestration, Operator Console command bus, immutable application records, Gate 2 screening analysis, owner-reported outcomes.  
3. **Reconfigure Tier 2** around the approved AI consulting/advisory/enablement persona and exemplar jobs; keep enrich/tailor/DOCX engines. Qualification must use **substantive JD analysis**; titles are signals. Engineering-heavy Sales Engineer / Solutions Engineer and non-fitting pure sales remain intended negatives when the JD confirms that character. Title alone must not be final except under independently approved deterministic eligibility rules.  
4. **Resume positioning:** allow truthful target-title use in non-historical sections; **never** rewrite historical employment titles to falsely claim a prior role.  
5. **Make verification a first-class state** independent of agent RESULT lines.  
6. **Treat localhost/extension control plane as a privileged API** requiring auth.  
7. **Remove/disable CapSolver** and any automated CAPTCHA solving from production apply; route CAPTCHA/MFA/device verification to HITL.  
8. **Keep SQLite** until multi-user/sync evidence demands otherwise.  
9. **ATS strategy:** Layer 1 generic agent + Layer 2 memos for frequent ATSes; lift Workday manual ban only with validated path.  

---

## 43. Handoff requirements for `ENGINEERING_IMPLEMENTATION_PLAN.md`

The implementation plan should order work using this document’s:

- §36 disposition matrix  
- §38–40 blocker gates (Windows → first real apply → unattended)  
- §41 uncertainties with resolution tasks  
- Process validation ladder (Levels 1–9)  
- PRD Gate 2 + Operator Console + outcome-learning as capability workstreams  
- CapSolver REMOVE/DISABLE + HITL-only security-challenge path (resolved disposition; not an open policy choice)  
- Qualification architecture: JD-substantive role fit; titles as signals; eng-heavy SE/Solutions Engineer and non-fitting pure sales remain negatives  
- Historical employment title integrity + permitted non-historical target-title positioning  
- No dependency on Seattle YAML as runtime  

Do **not** create the implementation plan in this task.

---

## Document status / change control

| Field | Value |
|-------|--------|
| Authority class | Owner-approved architecture discovery output (not product authority) |
| Status | Approved — Authoritative |
| Authoritativeness | Authoritative |
| Runtime validation | Deferred items marked UNKNOWN |
| Change control | Future material updates require re-discovery of affected areas and deliberate review |
| Next | `ENGINEERING_IMPLEMENTATION_PLAN.md` |

---

*End of ARCHITECTURE_CURRENT.md*  
*Status: Approved — Authoritative.*
