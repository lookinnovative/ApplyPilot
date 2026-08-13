# Engineering Implementation Plan

**Document type:** Engineering implementation plan  
**Authority class:** Owner-approved engineering implementation plan  
**Status:** Approved — Authoritative  
**Scope:** Ordered, dependency-aware plan to move ApplyPilot from verified current architecture to safe, useful, continuous autonomous job-application operation  
**Does not define:** New product requirements, new autonomy policy, or silent architecture rewrites  

---

## Document control

| Field | Value |
|-------|--------|
| Product | Personal autonomous AI job-search and job-application agent (ApplyPilot fork) |
| Inputs (Approved — Authoritative) | Documents 1–7: PRD, Autonomy Policy, Methodology, Process, Standards, Architecture Discovery Standard, Architecture Current |
| Target runtime | Windows-first for this deployment |
| Discovery | Complete — this plan consumes `ARCHITECTURE_CURRENT.md`; it does **not** re-discover |
| Change control | Material scope/order/gate changes require deliberate documented change control. Routine implementation detail inside an approved work package does not require rewriting governance unless architecture, policy, scope, or gates change |
| Authoritativeness | Authoritative |

---

## 1. Purpose

This plan answers:

**What exactly must we build, fix, harden, validate, and prove — and in what order — to get ApplyPilot from its verified current state to safe, useful, continuous autonomous job application operation?**

It is implementation-oriented, incremental, reuse-first, production-gated, and Windows-first. It is **not** another PRD, another architecture discovery, a speculative rewrite, a calendar schedule, or a promise of arbitrary completion dates.

---

## 2. Authority and evidence basis

| Source | Role in this plan |
|--------|-------------------|
| `JOB_AGENT_PRODUCT_REQUIREMENTS.md` | Required target product behavior |
| `AUTONOMY_AND_APPLICATION_POLICY.md` | Decision authority and park/HITL/security rules |
| `ENGINEERING_METHODOLOGY.md` | How to engineer (reuse-first, evidence-based, incremental) |
| `ENGINEERING_PROCESS.md` | Validation ladder, Windows baseline, security-before-real-apply |
| `ENGINEERING_STANDARDS.md` | Concrete technical standards |
| `ARCHITECTURE_DISCOVERY_STANDARD.md` | Discovery method (already applied) |
| `ARCHITECTURE_CURRENT.md` | Verified current architecture, blockers, disposition, uncertainties |

**Rules for this plan:**

- Do not silently change architecture findings.  
- Do not invent requirements merely because they seem useful.  
- Prefer preserve/harden/adapt over rewrite unless disposition says otherwise.  
- No arbitrary day/week/hour estimates.

---

## 3. Priority principle and progression

Earliest **safe** path to useful operation:

```
SAFE WINDOWS BASELINE
→ CORRECT CANDIDATE / JOB QUALIFICATION
→ TRUSTWORTHY RESUME + APPLICATION ARTIFACTS
→ SECURE APPLICATION EXECUTION
→ VERIFIED FIRST APPLICATION
→ CONTROLLED ATS EXPANSION
→ OUTCOME TRACKING
→ OPERATOR CONSOLE
→ CONTINUOUS ORCHESTRATION
→ OUTCOME-DRIVEN LEARNING
→ UNATTENDED PRODUCTION READINESS
```

**Implementation does not jump from WP0.1 to WP1.1.** After this plan is approved, complete or explicitly satisfy **WP0.2–WP0.5** first. Then begin substantive Phase 1 implementation at **WP1.1** (P0 security + Windows execution baseline).

Do **not** begin with Operator Console polish, Gmail, outcome learning, broad ATS expansion, Firecrawl, Anthropic Skills, claude-mem, Vercel, or generalized refactoring unless a blocker proves one is required earlier (none does).

---

## 4. Plan status table

Status values: `NOT STARTED` · `IN PROGRESS` · `BLOCKED` · `VALIDATING` · `COMPLETE` · `DEFERRED`

| ID | Title | Phase | Status |
|----|-------|-------|--------|
| WP0.1 | Governance set freeze and plan baseline | 0 | COMPLETE *(governance docs 1–8 approved — Authoritative)* |
| WP0.2 | Implementation branch and clean Git baseline | 0 | NOT STARTED |
| WP0.3 | Environment inventory (Python/Node/Claude/browser) | 0 | NOT STARTED |
| WP0.4 | Proportional test baseline and known failures | 0 | NOT STARTED |
| WP0.5 | Prevent inherited developer data as production candidate config | 0 | NOT STARTED |
| WP1.1 | Claude least-privilege execution boundary | 1 | NOT STARTED |
| WP1.2 | Secret isolation (prompts, env, logs) | 1 | NOT STARTED |
| WP1.3 | Local worker HTTP API security | 1 | NOT STARTED |
| WP1.4 | CapSolver remove/disable; security challenges → HITL | 1 | NOT STARTED |
| WP1.5 | Windows browser/CfT/CDP/extension runtime | 1 | NOT STARTED |
| WP1.6 | Windows process/path/tooling remediation | 1 | NOT STARTED |
| WP1.7 | Phase 1 baseline validation (no real submit) | 1 | NOT STARTED |
| WP2.1 | Authoritative structured candidate profile | 2 | NOT STARTED |
| WP2.2 | Remove inherited Seattle/IC-engineering persona | 2 | NOT STARTED |
| WP2.3 | JD-substantive qualification engine | 2 | NOT STARTED |
| WP2.4 | Qualification evidence persistence | 2 | NOT STARTED |
| WP2.5 | Full JD integrity for qualification | 2 | NOT STARTED |
| WP2.6 | Qualification corpus gate | 2 | NOT STARTED |
| WP3.1 | Pre-tailor ATS screening analysis | 3 | NOT STARTED |
| WP3.2 | Historical title integrity + truthful positioning | 3 | NOT STARTED |
| WP3.3 | Truthful tailoring engine adapt | 3 | NOT STARTED |
| WP3.4 | Post-tailor screening analysis + validation | 3 | NOT STARTED |
| WP3.5 | Resume format preservation (content vs render) | 3 | NOT STARTED |
| WP3.6 | Parse-back / machine-readability validation | 3 | NOT STARTED |
| WP3.7 | Jobscan methodology runtime consumption | 3 | NOT STARTED |
| WP3.8 | Gate 2 resume intelligence gate | 3 | NOT STARTED |
| WP4.1 | Stable application identity binding | 4 | NOT STARTED |
| WP4.2 | Immutable submitted artifact snapshots | 4 | NOT STARTED |
| WP4.3 | Duplicate / requisition identity prevention | 4 | NOT STARTED |
| WP4.4 | Explicit attempt/submit/verify state machine | 4 | NOT STARTED |
| WP4.5 | Transaction integrity for consequential transitions | 4 | NOT STARTED |
| WP4.6 | Artifact/state integrity gate | 4 | NOT STARTED |
| WP5.1 | Dry-run must not mark applied; pre-submit stop | 5 | NOT STARTED |
| WP5.2 | Minimal independent submission verification | 5 | NOT STARTED |
| WP5.3 | Controlled dry-run application campaign | 5 | NOT STARTED |
| WP5.4 | First controlled real application (owner-authorized) | 5 | NOT STARTED |
| WP5.5 | Gate D evidence review | 5 | NOT STARTED |
| WP6.1 | ATS capability/validation registry | 6 | NOT STARTED |
| WP6.2 | Controlled validation — Greenhouse/Lever/Ashby | 6 | NOT STARTED |
| WP6.3 | Workday: lift blanket manual exclusion via validation | 6 | NOT STARTED |
| WP6.4 | Controlled validation — iCIMS and major enterprise ATSes | 6 | NOT STARTED |
| WP6.5 | Indeed-type / custom / unknown ATS fallback | 6 | NOT STARTED |
| WP6.6 | Multi-ATS controlled production gate | 6 | NOT STARTED |
| WP7.1 | Search/discovery config for owner target profile | 7 | NOT STARTED |
| WP7.2 | Source health, dedupe, stale/dead-source handling | 7 | NOT STARTED |
| WP7.3 | Discovery quality metrics | 7 | NOT STARTED |
| WP7.4 | Seattle YAML migrate → archive disposition | 7 | NOT STARTED |
| WP8.1 | Dedicated job-search Gmail OAuth integration | 8 | NOT STARTED |
| WP8.2 | Application–email correlation with evidence thresholds | 8 | NOT STARTED |
| WP8.3 | Outcome states + multi-source provenance | 8 | NOT STARTED |
| WP8.4 | Owner-reported outcomes | 8 | NOT STARTED |
| WP8.5 | Gmail/outcome tracking security gate | 8 | NOT STARTED |
| WP9.1 | Operator Console local-first shell + hardened backend | 9 | NOT STARTED |
| WP9.2 | Console operational surfaces (funnel, jobs, artifacts, HITL) | 9 | NOT STARTED |
| WP9.3 | Natural-language control pipeline | 9 | NOT STARTED |
| WP9.4 | Durable pause/resume/stop via Console | 9 | NOT STARTED |
| WP9.5 | Operator Console gate | 9 | NOT STARTED |
| WP10.1 | Durable continuous orchestration loop | 10 | NOT STARTED |
| WP10.2 | Backpressure, pacing, limits, credit/quota stop | 10 | NOT STARTED |
| WP10.3 | Worker lifecycle + HITL parking in loop | 10 | NOT STARTED |
| WP10.4 | Continuous autonomy extended-session gate | 10 | NOT STARTED |
| WP11.1 | Learning evidence set completeness | 11 | NOT STARTED |
| WP11.2 | Pattern accumulation without false causation | 11 | NOT STARTED |
| WP11.3 | Proposed strategy updates + owner visibility | 11 | NOT STARTED |
| WP11.4 | Outcome-learning safety gate | 11 | NOT STARTED |
| WP12.1 | Adversarial security validation suite | 12 | NOT STARTED |
| WP12.2 | Reliability / restart / concurrency validation | 12 | NOT STARTED |
| WP12.3 | Observability + backup/recovery | 12 | NOT STARTED |
| WP12.4 | Unattended production readiness gate | 12 | NOT STARTED |
| WP-X.1 | Cross-cutting test matrix maintenance | X | NOT STARTED |
| WP-X.2 | Cross-cutting documentation updates | X | NOT STARTED |
| WP-X.3 | Official vendor documentation re-check at gates | X | NOT STARTED |
| WP-X.4 | Cost observability instrumentation | X | NOT STARTED |
| WP-X.5 | Historical/developer-specific cleanup (non-blocking) | X | NOT STARTED |

---

## 5. Maturity levels / first-use boundary

This plan preserves **all** work packages and production-quality requirements. It distinguishes three maturity levels so the first controlled proof is not blocked by broader production maturity, **without** weakening safety, factual integrity, candidate correctness, or submission integrity.

| Level | Name | Intent |
|-------|------|--------|
| **1** | FIRST CONTROLLED REAL APPLICATION | Deliberate proof of the inherited/adapted application path under owner supervision (Gate D) |
| **2** | CONTROLLED / AUTONOMOUS PRODUCTION APPLICATIONS | System may autonomously apply at production scale under policy (requires full **Gate B** + Gates C/E as applicable — not merely one successful proof) |
| **3** | CONTINUOUS / UNATTENDED OPERATION | Closed-loop replenishment and sustained unattended readiness (Gates F / G) |

### 5.1 FIRST CONTROLLED REAL APPLICATION (Gate D)

A supervised, owner-authorized proof for **one** selected qualified job on a validated ATS flow. Completing Gate D does **not** by itself authorize autonomous production-scale applying.

#### Non-negotiable before WP5.4 may execute

**Phase 0**

- WP0.2 — implementation branch / clean Git baseline  
- WP0.3 — Windows environment inventory  
- WP0.4 — known test baseline  
- WP0.5 — inherited developer persona/config isolation  

**Phase 1 — entire Gate A path**

- WP1.1 — least-privilege Claude execution  
- WP1.2 — secret isolation  
- WP1.3 — local worker API security where used by the apply path  
- WP1.4 — CapSolver removed/disabled; security challenges → HITL  
- WP1.5 — Windows browser/CfT/CDP runtime  
- WP1.6 — Windows process/path/tooling remediation necessary for the execution path  
- WP1.7 — Gate A validation  

**Phase 2 — selected-application qualification (Checkpoint B-FCA qualification)**

- WP2.1 — authoritative candidate profile **sufficient for the application**  
- WP2.2 — inherited Seattle/IC-engineering persona removed from qualification  
- WP2.3 — JD-substantive qualification operational  
- WP2.4 — qualification evidence **sufficient to explain why this job is qualified**  
- WP2.5 — full JD integrity **sufficient for the selected job**  

**Phase 3 — selected-application Gate 2 (Checkpoint B-FCA resume)**

- WP3.2 — historical employment titles protected  
- WP3.3 — truthful resume tailoring operational  
- WP3.4 — factual-integrity validation operational  
- WP3.1 + WP3.4 — pre/post screening analysis **sufficient to validate the selected resume against the selected JD**  
- WP3.5 **FCA portion** — selected resume presentation preserved correctly for submission  
- WP3.6 **FCA portion** — generated resume machine-readable enough for the **selected validated ATS**  
- WP3.7 **FCA portion** — Jobscan methodology use **sufficient for the selected application** (no unsupported guarantees)  
- Exact resume reviewed/validated before submission (owner + system validation)  

**Phase 4**

- WP4.1 — stable job/application/artifact identity  
- WP4.2 — exact submitted-artifact snapshot capability  
- WP4.3 — duplicate/requisition protection  
- WP4.4 — explicit ATTEMPTED / SUBMITTED / VERIFIED SUBMITTED distinction  
- WP4.5 — consequential state transition integrity **sufficient for the first application**  
- WP4.6 — integrity gate for the selected-application path (feeds Gate C)  

**Phase 5**

- WP5.1 — dry-run cannot mark applied/submitted; pre-submit stop  
- WP5.2 — minimal independent submission verification operational  
- WP5.3 — controlled dry-run campaign completed (Gate C)  
- HITL operational (from WP1.4 + apply path)  
- Explicit owner authorization for WP5.4  
- WP5.5 — Gate D evidence review after submit  

**Checkpoint B-FCA** (First Controlled Application Readiness) is the named narrower checkpoint for Level 1. It does **not** replace or weaken full **Gate B**.

#### Explicitly not required to complete Gate D (continue after first controlled proof)

These remain **in the plan** and are required for Level 2 (autonomous production) and/or full Gate B — they are **not deleted**:

| Work | Why it may continue after Gate D |
|------|----------------------------------|
| **WP2.6** full qualification corpus gate | Full multi-case corpus proves autonomous routing maturity; selected-job explainable qualification (WP2.3–WP2.5) is enough for one supervised proof |
| **WP3.5** maturity portion | Generalized content-vs-render architecture for all future templates/variants beyond correctly preserving the selected resume |
| **WP3.6** maturity portion | Generalized parse-back validation across many output/ATS combinations beyond machine readability for the selected validated ATS |
| **WP3.7** maturity portion | Mature reusable Jobscan methodology runtime architecture beyond sufficient methodology use for the selected application |
| **WP3.8** full Gate 2 resume intelligence gate | Closes full **Gate B** for autonomous production resume readiness across the corpus — not a substitute for selected-job validation before WP5.4 |
| Phases **6–12** | Broad ATS expansion, discovery productization, Gmail, Operator Console, continuous orchestration, outcome learning, unattended hardening — except defects that block Gate D |

**Ambiguity rule:** If an FCA vs maturity split inside WP3.5 / WP3.6 / WP3.7 cannot be made safely without ambiguity, keep the **entire** work package before Gate D. Safety and truthfulness take priority over speed. Do **not** automatically defer these WPs wholesale.

**Not deferred past first real submission (non-negotiable):** security/least-privilege/secrets/local API harden/CapSolver removal/HITL; candidate truth; JD-substantive qualification for the selected job; historical-title integrity; factual-integrity validation; duplicate prevention; submission verification (attempted≠submitted≠verified); artifact binding/snapshots.

### 5.2 CONTROLLED / AUTONOMOUS PRODUCTION APPLICATIONS (Level 2)

Before the system autonomously applies at production scale under policy, require:

- Full **Gate B** (including WP2.6 corpus + WP3.5–WP3.8 maturity completions as applicable)  
- Gate C patterns proven beyond the single first job as needed  
- **Gate E** multi-ATS controlled production path as applicable  
- No reliance on “we got lucky once at Gate D” as production readiness  

### 5.3 CONTINUOUS / UNATTENDED OPERATION (Level 3)

- **Continuous:** Phase **6** (enough ATS coverage), Phase **7** (discovery replenishment), Phase **8** (tracking), Phase **9** (owner control), Phase **10** (orchestrator), **Gate F**  
- **Unattended:** Phase **11** (as data allows; may defer learning with owner acceptance), Phase **12**, **Gate G** — Phase 12 security/reliability/observability **must not** be deferred  

---

## 6. Production gates and checkpoints

| Gate / Checkpoint | Name | Must prove | Maturity role |
|-------------------|------|------------|---------------|
| **A** | Windows / Security Baseline | Windows launch of pipeline + browser + Claude with approved permissions; CapSolver disabled; secrets isolated; local API hardened where used by apply path; HITL security-challenge path works; **no real submit** | Required before Gate D |
| **B-FCA** | First Controlled Application Readiness | Selected job: JD-substantive qualification with explainable evidence; historical titles protected; truthful tailor + factual validation; pre/post screening sufficient for selected JD/resume; selected resume presentation + machine readability for selected ATS; Jobscan methodology sufficient for selected app; exact resume reviewed/validated | Narrower checkpoint for Level 1 only — **does not weaken Gate B** |
| **B** | Qualification + Resume Readiness | Full controlled corpus routes correctly; full Gate 2 loop maturity (WP2.6 + WP3.1–WP3.8 as specified); historical titles intact; presentation/parse-back/methodology architecture ready for autonomous production use | Required for Level 2 autonomous production — **not redefined downward for Gate D** |
| **C** | Dry-Run Application Readiness | End-to-end dry-run for the selected application: select → qualify → prepare → navigate → upload → screening → HITL if needed → **PRE-SUBMIT STOP**; dry-run never writes `applied`/`submitted`; artifacts bound; ATTEMPTED ≠ SUBMITTED ≠ VERIFIED SUBMITTED states exist | Required before Gate D |
| **D** | First Real Application Authorized | Owner-authorized Level-5 submit on qualified job; evidence distinguishes ATTEMPTED / SUBMITTED / VERIFIED SUBMITTED; immutable artifacts preserved | Level 1 proof — not autonomous production authorization |
| **E** | Multi-ATS Controlled Production | Evidence-backed registry entries for multiple ATSes; Workday not permanently abandoned; unknown ATS not silently discarded; small batch across representative ATSes | Level 2 |
| **F** | Continuous Autonomy | Durable loop discover→…→track→replenish without repeated manual stage commands; pause/stop durable; job-level park; systemic stop observable | Level 3 continuous |
| **G** | Unattended Production Readiness | Adversarial security + reliability + concurrency + backup criteria met; separate from “controlled applications OK” | Level 3 unattended |

---

# PHASE 0 — Baseline / governance / repository control

### WP0.1 — Governance set freeze and plan baseline

| Field | Content |
|-------|---------|
| Objective | Preserve Documents 1–7 as Approved — Authoritative inputs; establish this plan as the implementation ordering authority once approved |
| Why required | Prevent silent requirement/architecture drift during implementation |
| Current-state evidence | Docs 1–7 Approved — Authoritative (`ARCHITECTURE_CURRENT.md` §43 handoff) |
| Scope | Document control only; no code |
| Reuse | Entire governance set |
| Dependencies | None |
| Tests | N/A |
| Validation gate | Documents 1–7 status confirmed Approved |
| Completion criteria | Plan exists; governance frozen as inputs |
| Documentation | This file |
| Out of scope | Re-discovery; requirement invention |
| Status | COMPLETE |

### WP0.2 — Implementation branch and clean Git baseline

| Field | Content |
|-------|---------|
| Objective | Establish implementation branch strategy and a clean baseline before consequential edits |
| Why required | Methodology: reviewable, incremental changes |
| Scope | Branch naming, protection of `main` as agreed, no force-push; commit only when owner requests |
| Implementation requirements | Record strategy in engineering notes; do not delete historical files for “cleanup” |
| Dependencies | WP0.1 |
| Validation gate | Branch strategy agreed; working tree understood |
| Out of scope | Deleting Seattle YAMLs or historical docs |

### WP0.3 — Environment inventory (Python/Node/Claude/browser)

| Field | Content |
|-------|---------|
| Objective | Record supported/assumed versions on the Windows target host |
| Why required | Process Windows baseline; U1/U2 unknowns |
| Scope | Python/venv, Node/npx, Claude Code CLI, Chrome/CfT, Playwright/Patchright, openssl optional |
| Implementation requirements | Written inventory; gaps feed WP1.5–WP1.6 |
| Dependencies | WP0.2 |
| Validation gate | Inventory complete; no install beyond owner-authorized setup |
| Out of scope | Installing CapSolver; configuring Gmail |

### WP0.4 — Proportional test baseline and known failures

| Field | Content |
|-------|---------|
| Objective | Run existing test suite; record pass/fail before implementation |
| Why required | Standards: know baseline; avoid blaming new work for pre-existing failures |
| Scope | `pytest` (or project equivalent) inventory; list known failures |
| Dependencies | WP0.3 |
| Validation gate | Baseline report filed |
| Out of scope | Mass test rewrites |

### WP0.5 — Prevent inherited developer data as production candidate config

| Field | Content |
|-------|---------|
| Objective | Ensure Seattle/IC-eng persona, Seattle employer research YAMLs, and prior-developer profile assumptions cannot silently become this owner’s production candidate/search truth |
| Why required | `ARCHITECTURE_CURRENT.md` §5, §35–36; PRD §5, §26 |
| Scope | Checklist + config hygiene; mark research YAMLs as non-runtime; no deletion |
| Dependencies | WP0.1; coordinate with WP0.2–WP0.4 |
| Validation gate | Explicit separation documented: research vs runtime registries vs owner profile |
| Out of scope | Inventing Atlanta employer YAML equivalents |

**Phase 0 Gate:** WP0.2–WP0.5 are **completed or explicitly satisfied** before substantive Phase 1 implementation (WP1.1+) proceeds. Implementation must **not** jump from WP0.1 to WP1.1. Baseline ready without treating inherited targeting as product truth.

---

# PHASE 1 — P0 security + Windows execution baseline

> **Gate A.** Must complete before any real application submission. Depends on Phase 0 Gate (WP0.2–WP0.5).

### WP1.1 — Claude least-privilege execution boundary

| Field | Content |
|-------|---------|
| Objective | Remove/replace unsafe broad authority such as inherited `--permission-mode bypassPermissions` |
| Why required | `ARCHITECTURE_CURRENT.md` §10, §15 P0; Standards least-privilege; Policy browser trust |
| Current-state evidence | `apply/launcher.py` spawns Claude with `bypassPermissions` |
| Scope | Least-privilege permission mode / allowlist; deny arbitrary shell/repo/credential authority from untrusted page/JD content |
| Reuse | PRESERVE Claude + Playwright MCP spine; HARDEN permissions |
| Implementation requirements | Approved permission model; untrusted ATS/JD content cannot obtain arbitrary shell, repository write, filesystem beyond job artifacts, credentials, unrelated tools |
| Dependencies | **WP0.2–WP0.5 completed or explicitly satisfied**; WP0.3 inventory available |
| Tests | Unit/integration asserting spawn flags; adversarial prompt fixtures (static) |
| Validation gate | Part of Gate A |
| Completion criteria | Production apply path does not use bypassPermissions (or equivalent broad authority) |
| Out of scope | Rewriting the entire apply agent |

### WP1.2 — Secret isolation (prompts, env, logs)

| Field | Content |
|-------|---------|
| Objective | Stop placing secrets in prompts unnecessarily; strip unrelated env secrets from Claude/MCP children; redact logs |
| Why required | §15 P0/P1; CapSolver key/passwords/profile in `prompt.py` |
| Scope | Prompt builders, subprocess env allowlist, log redaction |
| Implementation requirements | Define minimum secret surface for apply worker; passwords/API keys not in prompts unless unavoidable and then minimized; CapSolver key eliminated with WP1.4 |
| Dependencies | WP1.1 (coord), WP1.4 |
| Tests | Prompt snapshot tests without secret material; env inheritance tests |
| Validation gate | Gate A |
| Out of scope | Full secrets manager product |

### WP1.3 — Local worker HTTP API security

| Field | Content |
|-------|---------|
| Objective | Remediate unauthenticated localhost worker APIs (`7380+wid`), permissive CORS `*`, plaintext password exposure |
| Why required | §15 P0; §20 reuse-as-backend after harden |
| Scope | Authn for control plane; CORS lockdown; never return plaintext passwords to clients; secret redaction in API responses |
| Reuse | Extension options / worker HTTP as future Console backend **after** harden |
| Dependencies | WP1.2 |
| Tests | Unauthenticated access denied; password fields masked; CORS policy tests |
| Validation gate | Gate A |
| Out of scope | Full Operator Console UI |

### WP1.4 — CapSolver remove/disable; security challenges → HITL

| Field | Content |
|-------|---------|
| Objective | Remove/disable CapSolver from production apply path; route CAPTCHA/MFA/device verification/security challenges to HITL |
| Why required | Resolved disposition `ARCHITECTURE_CURRENT.md` §14, §36–37, U4; Autonomy Policy no CAPTCHA bypass |
| Current-state evidence | CapSolver in apply prompt/path |
| Scope | Production path disable/removal; preserve historical record that capability existed; HITL path for security challenges |
| Implementation requirements | No CapSolver key in prompts/env for production apply; challenges park to HITL; not a future optimization option |
| Dependencies | WP1.2 |
| Tests | Assert CapSolver not injected; HITL trigger for challenge markers (fixture) |
| Validation gate | Gate A |
| Out of scope | Building CapSolver alternatives |

### WP1.5 — Windows browser/CfT/CDP/extension runtime

| Field | Content |
|-------|---------|
| Objective | Windows-native Chrome for Testing install/discovery; extension load; CDP; headed apply path |
| Why required | §11, §38; `install_cft.py` linux64-only; U1 |
| Scope | `config.get_chrome_path`, `scripts/install_cft.py`, extension load validation on chosen build |
| Reuse | PRESERVE Chrome + extension + CDP design; ADAPT for Windows |
| Implementation requirements | Prefer Windows CfT path; do not mandate WSL; validate extension loads |
| Dependencies | WP0.3 |
| Tests | Smoke: Chrome launches; CDP port responds; extension present when headed |
| Validation gate | Gate A / Process progressive baseline |
| Out of scope | WSL as default |

### WP1.6 — Windows process/path/tooling remediation

| Field | Content |
|-------|---------|
| Objective | Fix `/proc` reconnect assumptions; Linux-only notify/focus utilities; path/venv/temp/process signaling |
| Why required | §11, §38 |
| Scope | Reconnect without `/proc`; no-op or Windows equivalents for notify-send/wmctrl/xdotool; document silent failures |
| Dependencies | WP1.5 |
| Tests | Process cleanup via taskkill path; reconnect behavior documented/tested where feasible |
| Validation gate | Gate A |
| Out of scope | Full Linux parity for desktop notifications |

### WP1.7 — Phase 1 baseline validation (no real submit)

| Field | Content |
|-------|---------|
| Objective | Prove Gate A end-to-end without submitting |
| Why required | Process §14–16 |
| Scope | Launch pipeline pieces; browser worker; Claude with approved permissions; secret isolation checks; HITL security-challenge dry path |
| Dependencies | WP1.1–WP1.6 |
| Validation gate | **Gate A** |
| Completion criteria | Checklist signed; **no real application submitted** |
| Out of scope | Qualification rewrite (Phase 2) |

---

# PHASE 2 — Candidate truth + qualification engine

> Correct inherited developer-specific targeting before any real application and before autonomous job selection.  
> **Checkpoint B-FCA (qualification):** selected-job readiness for Gate D.  
> **Gate B (qualification half):** full corpus maturity (WP2.6) for Level 2 autonomous production — **not** weakened for Gate D.

### WP2.1 — Authoritative structured candidate profile

| Field | Content |
|-------|---------|
| Objective | Structured authoritative candidate data: identity, work history, historical titles/dates, skills, experience, education/certs, location, work auth, preferences, approved reusable answers, target-role profile |
| Why required | PRD factual integrity; §6 gaps |
| Scope | Profile schema/config separation: CANDIDATE FACT / PREFERENCE / TARGETING POLICY / INFERENCE / UNKNOWN |
| Reuse | `profile.json` / wizard — ADAPT; do not scatter candidate logic in source |
| Dependencies | Phase 1 Gate A |
| Tests | Schema validation; separation of fact vs preference |
| Validation gate | **Required for Checkpoint B-FCA** (profile sufficient for the selected application); also feeds full Gate B |
| Out of scope | Fabricating missing history |

### WP2.2 — Remove inherited Seattle/IC-engineering persona

| Field | Content |
|-------|---------|
| Objective | Replace hard-coded Senior/Staff IC eng + Seattle + Go/Kotlin/Python/Java scoring persona |
| Why required | §6, §37; PRD §2, §5 |
| Current-state evidence | `scoring/scorer.py` persona and prefilter |
| Scope | Config-driven owner persona; remove Seattle defaults as product truth |
| Implementation requirements | Do **not** merely reverse the old blacklist |
| Dependencies | WP2.1 |
| Tests | Scorer prompts/fixtures contain consulting persona, not IC-eng Seattle |
| Validation gate | **Required before WP5.4** (Checkpoint B-FCA) |
| Out of scope | Deleting research YAMLs (WP7.4) |

### WP2.3 — JD-substantive qualification engine

| Field | Content |
|-------|---------|
| Objective | Qualify from actual JD responsibilities/requirements; titles as signals only |
| Why required | Approved role-classification clarification in `ARCHITECTURE_CURRENT.md` §6 |
| Scope | Replace hard title-final rejection for Sales Engineer / Solutions Engineer / Pre-sales / AE/AM with JD analysis |
| Implementation requirements | Engineering-heavy SE/Solutions Engineer → normally reject; pure non-fitting sales → normally reject; AI consulting/advisory/transformation/enablement/solution-selling with imperfect titles → evaluate substantively; title alone final only under independently approved deterministic eligibility rules; exemplar-job support per PRD |
| Dependencies | WP2.2 |
| Tests | Selected-job fixtures for Checkpoint B-FCA; full corpus in WP2.6 for Gate B |
| Validation gate | **Required operational before WP5.4** (Checkpoint B-FCA) |
| Out of scope | Auto-qualifying any title containing “AI” |

### WP2.4 — Qualification evidence persistence

| Field | Content |
|-------|---------|
| Objective | Persist structured explainability: why qualified/rejected, mandatory conflicts, preferred gaps, title signals, role classification, confidence/unknowns |
| Why required | PRD Gate 1; Console “why rejected”; learning later |
| Scope | DB/structured fields or artifact JSON bound to job |
| Dependencies | WP2.3 |
| Tests | Persistence round-trip; explainability fixtures |
| Validation gate | **Before WP5.4:** evidence sufficient to explain why the **selected** job is qualified. Broader corpus evidence matures with WP2.6 / Gate B |
| Out of scope | ML ranking |

### WP2.5 — Full JD integrity for qualification

| Field | Content |
|-------|---------|
| Objective | Ensure qualification uses sufficient/full JD content (address 6000-char truncation risk) |
| Why required | §6 FACT truncation |
| Scope | Scoring/enrichment inputs; chunking or higher limits with evidence |
| Dependencies | WP2.3 |
| Tests | Long-JD fixture not silently under-qualified |
| Validation gate | **Before WP5.4:** full JD integrity **sufficient for the selected job**. General long-JD hardening continues toward Gate B as needed |
| Out of scope | Paying for Firecrawl (DEFER) |

### WP2.6 — Qualification corpus gate

| Field | Content |
|-------|---------|
| Objective | Controlled corpus proves explainable correct routing for autonomous production qualification |
| Scope | Cases: obvious target; obvious engineering rejection; ambiguous Solutions Engineer; ambiguous Account Executive; AI consulting unusual title; missing mandatory; terminology mismatch; location/work-auth conflict |
| Dependencies | WP2.1–WP2.5 |
| Validation gate | **Gate B (qualification)** — required for Level 2 autonomous production |
| Completion criteria | Corpus pass criteria met before autonomous production-scale apply selection |
| First-controlled note | **Not required to complete Gate D** if Checkpoint B-FCA qualification (WP2.1–WP2.5 for the selected job) is satisfied. Work package is **not deleted** — it remains mandatory for full Gate B / Level 2 |

---

# PHASE 3 — ATS screening + resume intelligence

> Implement approved Gate 2.  
> **Checkpoint B-FCA (resume):** selected JD/resume validation for Gate D.  
> **Gate B (resume half):** full WP3.5–WP3.8 maturity — **not** weakened for Gate D.

### WP3.1 — Pre-tailor ATS screening analysis

| Field | Content |
|-------|---------|
| Objective | Analyze JD/screening signals before tailoring: critical terminology, mandatory/preferred quals, hard skills, business terms, title/function signals, ATS parsing risks, supported candidate evidence |
| Why required | PRD §6.2, §9; gap §7 |
| Scope | New analysis artifact bound to job; evidence mapping categories per PRD |
| Dependencies | Phase 2 Checkpoint B-FCA qualification (WP2.1–WP2.5); full Gate B qualification (WP2.6) for autonomous production maturity |
| Tests | Selected-job analysis for Checkpoint B-FCA; broader fixtures toward Gate B |
| Validation gate | **Before WP5.4:** analysis sufficient for the selected JD. Broader corpus maturity continues toward Gate B |
| Out of scope | Claiming proprietary ATS algorithm knowledge |

### WP3.2 — Historical title integrity + truthful positioning

| Field | Content |
|-------|---------|
| Objective | Remove inherited behavior that can rewrite historical employment titles to the target job title; allow truthful target-title positioning outside employment history |
| Why required | §7, §37; PRD historical title integrity |
| Current-state evidence | Tailor prompt can require target title verbatim |
| Scope | `scoring/tailor.py` + validator rules |
| Implementation requirements | Never falsify historical employment records; may use target title in heading/summary/positioning/skills context when appropriate |
| Dependencies | WP2.1 |
| Tests | Regression: historical titles unchanged; positioning may mention target role |
| Validation gate | **Required before WP5.4** — not deferred |
| Out of scope | Changing owner’s real past titles |

### WP3.3 — Truthful tailoring engine adapt

| Field | Content |
|-------|---------|
| Objective | Improve representation of truthful existing experience; no fabrication |
| Why required | Gate 2 affirmative objective |
| Scope | Tailor prompts/validators; use pre-tailor analysis |
| Reuse | ADAPT existing tailor/validator/DOCX |
| Dependencies | WP3.1, WP3.2 |
| Tests | Factual integrity suite; no invented metrics/employers |
| Validation gate | **Required before WP5.4** — truthful tailoring operational |
| Out of scope | Fabricating to pass ATS |

### WP3.4 — Post-tailor screening analysis + validation

| Field | Content |
|-------|---------|
| Objective | Post-tailor analysis + validation: factual integrity, coverage, screening alignment, historical titles, machine/human readability, artifact integrity |
| Why required | PRD Gate 2 loop |
| Scope | Fail → no auto-submit path |
| Dependencies | WP3.3 |
| Tests | Reject fabricated/unsupported claims |
| Validation gate | **Required before WP5.4** — factual-integrity validation + post-screening sufficient for selected JD/resume |
| Out of scope | Screening risk alone as auto-disqualify for fit (PRD: presentation ≠ fit) |

### WP3.5 — Resume format preservation (content vs render)

| Field | Content |
|-------|---------|
| Objective | Separate CONTENT MODEL from DOCUMENT RENDERING; preserve owner-approved presentation; avoid cumulative degradation |
| Why required | PRD / Standards; §7 |
| Scope | DOCX/PDF render path |
| Dependencies | WP3.3 |
| Tests | Visual/structure fixtures; golden render where practical |
| **FCA-required portion (before WP5.4)** | Selected resume presentation preserved correctly for the chosen application; no unsafe formatting degradation for that submit |
| **Maturity portion (Gate B / Level 2)** | Generalized rendering architecture covering future templates/variants |
| Ambiguity rule | If FCA vs maturity cannot be split safely, complete the **entire** WP before Gate D |
| Out of scope | Arbitrary redesign of resume brand; automatically deferring this entire WP past Gate D |

### WP3.6 — Parse-back / machine-readability validation

| Field | Content |
|-------|---------|
| Objective | Where practical, validate generated PDF/DOCX machine readability |
| Why required | Gate 2; §7 missing parse-back |
| Scope | Extract text/structure; fail or warn per policy |
| Dependencies | WP3.5 |
| Tests | Parse-back fixtures |
| **FCA-required portion (before WP5.4)** | Generated resume machine-readable enough for the **selected validated ATS** |
| **Maturity portion (Gate B / Level 2)** | Generalized parse-back validation across output/ATS combinations |
| Ambiguity rule | If FCA vs maturity cannot be split safely, complete the **entire** WP before Gate D |
| Out of scope | Guaranteeing every ATS parser behavior; automatically deferring this entire WP past Gate D |

### WP3.7 — Jobscan methodology runtime consumption

| Field | Content |
|-------|---------|
| Objective | Decide how `docs/guidelines/jobscan/**` guidance is consumed at runtime without unsupported guarantees |
| Why required | §7 Jobscan docs not loaded; hand-copied rules |
| Scope | Provenance-tagged methodology; not hard product law thresholds unless later approved |
| Dependencies | WP3.1 |
| Tests | Guidance source attribution in analysis where used |
| **FCA-required portion (before WP5.4)** | Methodology use **sufficient for the selected application** without unsupported guarantees |
| **Maturity portion (Gate B / Level 2)** | Mature reusable runtime methodology architecture |
| Ambiguity rule | If FCA vs maturity cannot be split safely, complete the **entire** WP before Gate D |
| Out of scope | Paying Jobscan API unless later approved; automatically deferring this entire WP past Gate D |

### WP3.8 — Gate 2 resume intelligence gate

| Field | Content |
|-------|---------|
| Objective | Prove truthful tailoring, no historical-title fabrication, keyword alignment, readable output, preserved presentation, post-tailor improvement, no unsupported claims — at **full Gate B** maturity |
| Dependencies | WP3.1–WP3.7 (including maturity portions) |
| Validation gate | **Gate B complete** (resume half) — required for Level 2 autonomous production |
| First-controlled note | **Not required to complete Gate D** if Checkpoint B-FCA resume requirements (§5.1) are satisfied for the selected job. Work package is **not deleted** |
| Out of scope | Real submit; redefining Gate B downward to equal Checkpoint B-FCA |

**Also in Phase 3 (cover letters, subordinate):** Adapt cover generation to use tailored resume when cover is generated; conditional policy per PRD — implement as part of WP3.3–WP3.5 unless split later without changing gates. For Gate D, cover handling follows PRD conditional policy for the selected ATS/job.

---

# PHASE 4 — Artifact identity + submission state integrity

> Required before real submissions (Gate D). Feeds **Gate C**. Does not wait on full Gate B corpus maturity when Checkpoint B-FCA is met.

### WP4.1 — Stable application identity binding

| Field | Content |
|-------|---------|
| Objective | Stable binding: JOB ↔ JD ↔ qualification ↔ screening analysis ↔ tailored resume ↔ cover ↔ Q&A ↔ attempt ↔ evidence ↔ outcome |
| Why required | §22 learning readiness; PRD artifact freeze |
| Scope | Identity keys; schema; APIs |
| Dependencies | Checkpoint B-FCA (selected-application qualification + resume readiness) |
| Tests | Binding integrity tests |
| Validation gate | **Required before WP5.4** |
| Out of scope | Multi-device sync |

### WP4.2 — Immutable submitted artifact snapshots

| Field | Content |
|-------|---------|
| Objective | Freeze exact JD, resume, cover, screening answers, requisition identity, timestamps; later edits must not rewrite history |
| Why required | §7 overwrite risk; §22 |
| Scope | Snapshot store separate from working tailored files |
| Dependencies | WP4.1 |
| Tests | Mutate working resume → snapshot unchanged |
| Out of scope | ML feature store |

### WP4.3 — Duplicate / requisition identity prevention

| Field | Content |
|-------|---------|
| Objective | Strengthen identity; prevent retries/restarts from duplicate submissions |
| Why required | §34; Standards |
| Scope | URL normalize + requisition/employer keys; apply acquire guards |
| Dependencies | WP4.1 |
| Tests | Concurrent acquire; retry idempotency |
| Out of scope | Cross-board perfect dedupe guarantees |

### WP4.4 — Explicit attempt/submit/verify state machine

| Field | Content |
|-------|---------|
| Objective | Explicit states distinguishing at least discovered, enriched, qualified, rejected, prepared, applying, needs-human, attempted, submitted, verified-submitted, failed, withdrawn/closed, later outcomes |
| Why required | PRD §15; §16 verification gap; §19 state gaps |
| Current-state evidence | RESULT inference → applied; `verification_confidence` unused |
| Scope | ADAPT `jobs.state` / transitions; **never conflate ATTEMPTED / SUBMITTED / VERIFIED SUBMITTED** |
| Dependencies | WP4.1 |
| Tests | Transition matrix tests; illegal transitions rejected |
| Out of scope | Abandoning SQLite |

### WP4.5 — Transaction integrity for consequential transitions

| Field | Content |
|-------|---------|
| Objective | Protect consequential transitions; reduce force=True drift |
| Why required | §23–24 |
| Scope | Transactional updates for apply/verify |
| Dependencies | WP4.4 |
| Tests | Crash mid-transition fixtures where practical |
| Validation gate | **Before WP5.4:** integrity **sufficient for the first application**; broader hardening continues as needed |
| Out of scope | Distributed DB |

### WP4.6 — Artifact/state integrity gate

| Field | Content |
|-------|---------|
| Objective | Prove wrong resume cannot be selected for another job; duplicate blocked; interrupted app recovers safely; immutable snapshot survives later changes |
| Dependencies | WP4.1–WP4.5 |
| Validation gate | Feeds **Gate C**; **required for the selected-application path before WP5.4** |
| Out of scope | Real submit |

---

# PHASE 5 — First real application readiness

> **Critical production gate.** Not “just another milestone.”

### WP5.1 — Dry-run must not mark applied; pre-submit stop

| Field | Content |
|-------|---------|
| Objective | Fix dry-run → `applied` leak; enforce pre-submit stop in dry-run |
| Why required | §15 P1; §39.6 |
| Scope | `result_handlers` / launcher dry-run paths |
| Dependencies | WP4.4 |
| Tests | Dry-run never reaches submitted/applied |
| Validation gate | Gate C |

### WP5.2 — Minimal independent submission verification

| Field | Content |
|-------|---------|
| Objective | Verification evidence architecture independent of agent RESULT phrases |
| Why required | §16; PRD attempted≠submitted≠verified |
| Scope | Browser confirmation signals, IDs, history; confidence field used honestly; phrase inference insufficient alone |
| Dependencies | WP4.4 |
| Tests | Fixture pages → correct verification class |
| Validation gate | Gate C/D |
| Out of scope | Perfect ATS API verification for all vendors |

### WP5.3 — Controlled dry-run application campaign

| Field | Content |
|-------|---------|
| Objective | Exercise for the **selected** application: select → qualify → prepare → navigate → upload → screening → HITL if needed → **PRE-SUBMIT STOP** |
| Why required | Process Levels 3–4 |
| Dependencies | Gate A; Checkpoint B-FCA; WP4.1–WP4.6; WP5.1–WP5.2; WP1.4 HITL |
| Validation gate | **Gate C** |
| Completion criteria | Dry-run campaign checklist complete; dry-run never writes applied/submitted; **no real submit** |
| Out of scope | Throughput optimization; requiring full Gate B corpus completion |

### WP5.4 — First controlled real application (owner-authorized)

| Field | Content |
|-------|---------|
| Objective | One genuinely qualified application on supported/validated ATS flow with owner visibility — Level 1 proof, not autonomous production authorization |
| Why required | Process Level 5; §39.7 |
| Scope | Explicit owner authorization record; preserve exact artifacts; capture submission evidence; verify resulting state; exact resume reviewed/validated before submission |
| Dependencies | **Gate C**; Checkpoint B-FCA; non-negotiable list in §5.1; CapSolver disabled; HITL operational; explicit owner authorization |
| Validation gate | **Gate D** (with WP5.5) |
| Completion criteria | Purpose is prove system, not maximize volume; ATTEMPTED / SUBMITTED / VERIFIED SUBMITTED remain distinct |
| Out of scope | Batch apply; treating Gate D as full Gate B or Level 2 readiness |

### WP5.5 — Gate D evidence review

| Field | Content |
|-------|---------|
| Objective | Confirm ATTEMPT / SUBMISSION / VERIFIED SUBMISSION distinguished by evidence |
| Dependencies | WP5.4 |
| Validation gate | **Gate D** |
| Out of scope | Declaring autonomous production or unattended readiness |

**Phase 5 prerequisite checklist:** See §5.1 non-negotiables. Maps to `ARCHITECTURE_CURRENT.md` §39 without requiring full Gate B corpus/maturity completions that §5.1 explicitly allows to continue after the first controlled proof.

---

# PHASE 6 — ATS validation + expansion

> After Gate D. **Gate E.**

### WP6.1 — ATS capability/validation registry

| Field | Content |
|-------|---------|
| Objective | Durable registry so “supported” means evidence-backed capabilities |
| Why required | §12 overclaim risk; U3 |
| Scope | Per-ATS: discovery/enrich/detect/login/session/fill/upload/screening/HITL/submit/verify |
| Dependencies | Gate D |
| Out of scope | Claiming S without validation |

### WP6.2 — Controlled validation — Greenhouse/Lever/Ashby

| Field | Content |
|-------|---------|
| Objective | Validate strongest inherited paths |
| Reuse | PRESERVE + HARDEN detect/session/successful_paths; gate memos on verified submit |
| Dependencies | WP6.1 |
| Validation | Levels 4–7 as appropriate |

### WP6.3 — Workday: lift blanket manual exclusion via validation

| Field | Content |
|-------|---------|
| Objective | Address `sites.yaml` `manual_ats` / `myworkdayjobs.com` skip; do **not** permanently abandon Workday |
| Why required | §12–13, §36 Workday ADAPT; discovery already exists |
| Scope | Controlled validation before autonomous production enablement |
| Dependencies | WP6.1, Gate D |
| Completion criteria | Explicit enable/disable based on evidence, not inherited fear alone |
| Out of scope | Enabling Workday without validation |

### WP6.4 — Controlled validation — iCIMS and major enterprise ATSes

| Field | Content |
|-------|---------|
| Objective | Oracle/Taleo, SuccessFactors, SmartRecruiters, ADP, UKG, Jobvite — validate relevant capabilities |
| Strategy | Prefer Layer 1 generic agent reliability; Layer 2 only where evidence shows need |
| Dependencies | WP6.1 |

### WP6.5 — Indeed-type / custom / unknown ATS fallback

| Field | Content |
|-------|---------|
| Objective | QUALIFIED JOB → unknown/unvalidated ATS → generic agent when policy allows **OR** park/HITL → preserve opportunity |
| Why required | PRD ATS-agnostic; §13 |
| Implementation requirements | **Do not silently discard** qualified jobs solely because ATS is unfamiliar |
| Dependencies | WP6.1, WP1.4 HITL |

### WP6.6 — Multi-ATS controlled production gate

| Field | Content |
|-------|---------|
| Objective | Small batch across representative ATSes; registry updated |
| Validation gate | **Gate E** |
| Out of scope | Unattended continuous loop (Phase 10) |

---

# PHASE 7 — Discovery quality + continuous supply

### WP7.1 — Search/discovery config for owner target profile

| Field | Content |
|-------|---------|
| Objective | Owner-aligned search config; fix schema drift (`sites` vs `boards`, location accept patterns) |
| Why required | §5 schema drift; Amazon/Costco Seattle hardcodes → ADAPT |
| Scope | searches.yaml / registries; broad discovery useful to consulting targets |
| Dependencies | WP2.1–WP2.2 |
| Out of scope | Hand-maintained Atlanta YAML twin of Seattle research files |

### WP7.2 — Source health, dedupe, stale/dead-source handling

| Field | Content |
|-------|---------|
| Objective | Dedup, stale-job, dead-source, source health; JobSpy/HN/Workday/Greenhouse/Lever/Ashby/direct where useful |
| Reuse | PRESERVE scrapers + ADAPT |
| Dependencies | WP7.1 |

### WP7.3 — Discovery quality metrics

| Field | Content |
|-------|---------|
| Objective | Track discovered/enriched/duplicate/stale/qualified/rejected/apply-ready — not raw count alone |
| Dependencies | WP7.2, WP2.4 |

### WP7.4 — Seattle YAML migrate → archive disposition

| Field | Content |
|-------|---------|
| Objective | MIGRATE useful ATS identifiers into runtime registries → ARCHIVE research files; do not delete during migrate; do not invent Atlanta replacements |
| Why required | §5, §35–36 |
| Dependencies | WP7.1 |
| Out of scope | Using Seattle YAMLs as runtime config |

---

# PHASE 8 — Dedicated job-search Gmail + outcome tracking

> Owner creates dedicated Gmail separately. **Does not block Gate D.**

### WP8.1 — Dedicated job-search Gmail OAuth integration

| Field | Content |
|-------|---------|
| Objective | OAuth/scopes/token handling per current official Google docs; narrow scopes; tokens not exposed to browser agents |
| Why required | PRD §16–17; §18 tracking |
| Current-state evidence | `tracking/` + Gmail MCP; one-shot `track` |
| Reuse | PRESERVE + ADAPT |
| Dependencies | Gate D recommended before prioritizing; not a Gate D blocker |
| Out of scope | Configuring the account in this planning task |

### WP8.2 — Application–email correlation with evidence thresholds

| Field | Content |
|-------|---------|
| Objective | Correlate with employer/requisition/title/sender/timing; no weak ambiguous state mutation |
| Dependencies | WP8.1, WP4.1 |

### WP8.3 — Outcome states + multi-source provenance

| Field | Content |
|-------|---------|
| Objective | Confirmation, recruiter outreach/screen, interview stages, rejection, offer, other approved outcomes with provenance |
| Dependencies | WP8.2, WP4.4 |

### WP8.4 — Owner-reported outcomes

| Field | Content |
|-------|---------|
| Objective | Phone/text/in-person/offline reporting with `OWNER_REPORTED` provenance |
| Why required | PRD §18–19; gap §19 |
| Dependencies | WP8.3; Console WP9.3 for NL path preferred |

### WP8.5 — Gmail/outcome tracking security gate

| Field | Content |
|-------|---------|
| Objective | Prove tracking cannot confuse applications; malicious email cannot become agent authority |
| Dependencies | WP8.1–WP8.4 |
| Validation | Phase 8 gate |
| Out of scope | Email as sole outcome source |

---

# PHASE 9 — Operator Console

> Local-first V1. **Do not assume Vercel.** Does not block Gate D.

### WP9.1 — Operator Console local-first shell + hardened backend

| Field | Content |
|-------|---------|
| Objective | Owner-facing shell using hardened worker/API backend; extend `view.py` / HITL; engineering CLI remains engineering-only |
| Why required | PRD §18; §20 reuse |
| Reuse | EXTEND dashboard; REUSE AS BACKEND after WP1.3; EXTEND HITL |
| Dependencies | WP1.3; Gate D recommended |
| Out of scope | Vercel hosting assumption; Cursor as daily UI |

### WP9.2 — Console operational surfaces

| Field | Content |
|-------|---------|
| Objective | Status, funnel, jobs, qualification, resumes, covers, application state, submission evidence, HITL, outcomes, failures, pause/resume, safe config |
| Implementation requirements | No secret exposure |
| Dependencies | WP9.1, WP4.*, WP8.4 as available |

### WP9.3 — Natural-language control pipeline

| Field | Content |
|-------|---------|
| Objective | OWNER MESSAGE → INTENT → ENTITY RESOLUTION → POLICY CHECK → STRUCTURED ACTION → DURABLE STATE → AUDIT → RESPONSE |
| Why required | PRD §18; Policy NL must not expand authority |
| Scope | Example intents: pause/resume, what happened, show resume, interview/rejection reports, exclusions, why rejected, retry |
| Implementation requirements | Ambiguity → clarify; no arbitrary SQL/state mutation from raw NL |
| Dependencies | WP9.1–WP9.2, WP2.4 |
| Tests | Intent/entity/ambiguity/policy/audit suite |

### WP9.4 — Durable pause/resume/stop via Console

| Field | Content |
|-------|---------|
| Objective | Durable system-wide pause/stop and application-specific park; survive restart |
| Why required | §40; Standards pause/stop |
| Dependencies | WP9.3, WP10.1 coordination |

### WP9.5 — Operator Console gate

| Field | Content |
|-------|---------|
| Objective | Prove intent, entity resolution, ambiguity, policy, persistence, restart, auditability |
| Validation gate | Phase 9 gate (supports Gate F/G) |
| Out of scope | Blocking first controlled application |

---

# PHASE 10 — Continuous autonomous orchestration

> Close orchestration gap. **Gate F.**

### WP10.1 — Durable continuous orchestration loop

| Field | Content |
|-------|---------|
| Objective | DISCOVER → ENRICH → QUALIFY → PREPARE → APPLY → VERIFY → TRACK → REPLENISH → REPEAT without repeated manual stage commands |
| Why required | §4 FACT no closed loop; PRD continuous autonomy |
| Current-state evidence | `pipeline.STAGE_ORDER` excludes apply/track; `apply --continuous` apply-only; `track` one-shot |
| Scope | ADD orchestrator; safe restart; job-level failure isolation |
| Dependencies | Gates D–E strongly recommended; WP9.4 for pause/stop |
| Out of scope | Maximizing volume over quality |

### WP10.2 — Backpressure, pacing, limits, credit/quota stop

| Field | Content |
|-------|---------|
| Objective | Queue backpressure; rate/provider limits; application pacing; period limits where approved; reliable credit/quota stop |
| Why required | §40.5; Autonomy resource stops |
| Dependencies | WP10.1 |

### WP10.3 — Worker lifecycle + HITL parking in loop

| Field | Content |
|-------|---------|
| Objective | Browser-worker lifecycle; park-don’t-halt; continue other jobs |
| Dependencies | WP10.1, WP1.4, WP9.2 |

### WP10.4 — Continuous autonomy extended-session gate

| Field | Content |
|-------|---------|
| Objective | Controlled extended session proves self-replenishment without repeated manual stage commands |
| Validation gate | **Gate F** |
| Completion criteria | Does **not** alone declare unattended production readiness |
| Out of scope | Gate G |

---

# PHASE 11 — Outcome-driven learning

> Only after trustworthy application/outcome data. **Not ML-by-default.**

### WP11.1 — Learning evidence set completeness

| Field | Content |
|-------|---------|
| Objective | Ensure JD + exact submitted resume + context + outcome evidence sets exist (depends on WP4.2, WP8.*) |
| Why required | §22 not ready; PRD §19 |
| Dependencies | Material volume of Gate D+ applications with outcomes |
| Out of scope | Choosing fine-tuning architecture |

### WP11.2 — Pattern accumulation without false causation

| Field | Content |
|-------|---------|
| Objective | OUTCOME → resolve application → evidence set → analysis → patterns → threshold → proposed update |
| Safety | No causation from one interview/rejection; no fabricated facts; no rewrite of historical artifacts; owner comments ≠ automatic global policy |
| Dependencies | WP11.1 |

### WP11.3 — Proposed strategy updates + owner visibility

| Field | Content |
|-------|---------|
| Objective | Console visibility: emerging patterns, what changed, why, supporting evidence |
| Dependencies | WP11.2, WP9.2 |

### WP11.4 — Outcome-learning safety gate

| Field | Content |
|-------|---------|
| Objective | Prove learning proposals are evidence-thresholded and non-destructive |
| Dependencies | WP11.1–WP11.3 |
| Out of scope | Unsupervised auto-rewrite of candidate facts |

---

# PHASE 12 — Production hardening / unattended readiness

> **Gate G.** Separate from controlled-applications OK.

### WP12.1 — Adversarial security validation suite

| Field | Content |
|-------|---------|
| Objective | Malicious JD/ATS/email injection; local file/secret exfil attempts; unrelated shell; cross-job artifact confusion |
| Why required | §40.3; Process before L9; Standards adversarial tests |
| Dependencies | Gate F strongly recommended |
| Validation gate | Gate G |

### WP12.2 — Reliability / restart / concurrency validation

| Field | Content |
|-------|---------|
| Objective | Browser/worker crash, network, DB lock, model exhaustion, session/Gmail expiry, HITL, interrupted submit, duplicate prevention; multi-worker without wrong artifacts/session collision/state corruption |
| Dependencies | WP12.1 coordination |
| Validation gate | Gate G |

### WP12.3 — Observability + backup/recovery

| Field | Content |
|-------|---------|
| Objective | Owner can see what agent is doing/did/failed/HITL/submitted/verified/outcomes; backup SQLite, profile, evidence, artifacts, config, learned evidence |
| Why required | §32 blind spots; §40.8 |
| Dependencies | WP9.2, WP10.1 |
| Validation gate | Gate G |

### WP12.4 — Unattended production readiness gate

| Field | Content |
|-------|---------|
| Objective | Explicit criteria for SAFE FOR CONTROLLED APPLICATIONS (already Gate D/E) **and separately** SAFE FOR CONTINUOUS UNATTENDED OPERATION |
| Validation gate | **Gate G** |
| Completion criteria | Do not collapse controlled vs unattended into one milestone |
| Out of scope | Declaring success from a single extended test alone |

---

# Cross-cutting workstreams

### WP-X.1 — Testing matrix

Map across phases: unit, integration, regression, state transition, persistence, restart, concurrency, browser, artifact binding, factual integrity, qualification corpus, ATS screening corpus, Operator Console NL, outcome learning, security/adversarial. Require regression tests for verified defects where practical.

### WP-X.2 — Documentation updates

After validated implementation, update docs distinguishing **current verified behavior** vs **planned**. Update `ARCHITECTURE_CURRENT.md` when material architecture changes become verified. Update this plan’s status table without rewriting historical facts.

### WP-X.3 — Official vendor documentation re-check

At each gate involving Anthropic/Claude Code, Playwright, Chrome/CfT, Google/Gmail, Gemini, OpenAI, ATS vendor docs, or new services — re-check **current** official documentation. Do not rely solely on discovery-era notes.

### WP-X.4 — Cost observability

Instrument LLM API, Claude Code, optional job-data/enrichment services, future hosting/storage. Do not prematurely optimize pennies during security/reliability work. Do not introduce paid services without evidence-based need and owner approval where appropriate.

### WP-X.5 — Historical / developer-specific cleanup

Later, evidence-based disposition (KEEP / ARCHIVE / REMOVE / MIGRATE-GENERALIZE) for Seattle YAMLs (after WP7.4), `docs/superpowers/**`, stale human-review strings, version/CHANGELOG drift, tracked `CLAUDE.md` hygiene. **Do not delete merely because old. Do not preserve misleading dead configuration indefinitely.**

---

## 7. Candidate technology disposition (carry-forward)

| Technology | Disposition (`ARCHITECTURE_CURRENT.md`) | Plan placement |
|------------|-------------------------------------------|----------------|
| Playwright MCP | ADOPT (already) + HARDEN | Phase 1 harden; pin/`--strict-mcp-config`; upgrade only with regression (U9) |
| Anthropic Skills | EVALUATE LATER / ENGINEERING-ONLY first | Not adopted for product runtime in Phases 0–5; evaluate only if a concrete packaging need appears after Gate D |
| Firecrawl | EVALUATE LATER / DEFER | Not in first-use path; optional Phase 7 enrich evaluation if Patchright path insufficient |
| claude-mem | REJECT (product runtime) | Engineering-only optional; never product system of record |
| planning-with-files | ENGINEERING-ONLY | Engineering sessions only |

**Do not install** any of these merely because they were evaluated.

---

## 8. Blocker traceability

| Blocker (`ARCHITECTURE_CURRENT.md`) | Phase | Work package(s) | Remediation | Gate |
|-------------------------------------|-------|-----------------|-------------|------|
| Windows CfT install/path linux-only | 1 | WP1.5 | Windows CfT install + `get_chrome_path` | A |
| Extension load on chosen Chrome | 1 | WP1.5, WP1.7 | Validate CfT vs Stable | A |
| PATH: Python/Node/Claude/openssl | 0–1 | WP0.3, WP1.6 | Inventory + remediate | A |
| Silent failures notify-send/focus/`/proc` | 1 | WP1.6 | Windows-safe paths; document | A |
| P0 `bypassPermissions` + secrets in prompts | 1 | WP1.1, WP1.2 | Least privilege + secret isolation | A / before D |
| P0 localhost API auth/CORS/passwords | 1 | WP1.3 | Harden API | A / before D |
| P0 CapSolver production path | 1 | WP1.4 | REMOVE/DISABLE; HITL | A / before D |
| P0 prompt injection surface | 1, 12 | WP1.1, WP12.1 | Privilege reduce + adversarial suite | A; G for unattended |
| Persona/scoring rewrite + JD-substantive qualification | 2 | WP2.1–WP2.6 | Replace IC-eng; JD analysis | B / before D |
| Historical title integrity + factual tailor policy | 3 | WP3.2–WP3.4 | Fix prompt/validator | B-FCA / before D (full Gate B maturity continues via WP3.5–WP3.8) |
| Full qualification corpus / Gate 2 maturity | 2–3 | WP2.6, WP3.5–WP3.8 maturity | Autonomous production readiness | **B** (Level 2; not required to finish Gate D) |
| Submission verification mechanism | 4–5 | WP4.4, WP5.2 | Independent verify states | C/D |
| Windows browser/extension readiness | 1 | WP1.5–WP1.7 | Baseline validation | A / before D |
| Dry-run must not write `applied` | 5 | WP5.1 | Fix result path | C / before D |
| Owner-authorized Level 5 controlled submit | 5 | WP5.4–WP5.5 | Process gate | D |
| Continuous orchestrator + durable pause/stop | 9–10 | WP9.4, WP10.1–WP10.4 | ADD loop + durable control | F |
| Prompt-injection security testing (unattended) | 12 | WP12.1 | Adversarial suite | G |
| Operator Console HITL path (or equivalent) | 9 | WP9.1–WP9.2 | Console HITL | F/G *(equivalent HITL exists for Gate D via current HITL after Phase 1)* |
| Credit/quota stop reliability | 10 | WP10.2 | Systemic stop | F/G |
| Outcome tracking + owner-reported | 8–9 | WP8.3–WP8.4, WP9.3 | Multi-source outcomes | F recommended; G |
| Artifact binding + immutable submissions | 4 | WP4.1–WP4.2 | Snapshots | C/D; learning 11 |
| Observability of system-wide stop | 9–12 | WP9.4, WP12.3 | Console + ops visibility | F/G |

### High-risk findings → work

| High-risk | Phase | WP |
|-----------|-------|-----|
| Phrase-inferred success | 4–5 | WP4.4, WP5.2 |
| Shared ATS sessions across employers | 6, 12 | WP6.x session design; WP12.2 |
| Env secret inheritance | 1 | WP1.2 |
| Wizard/profile plaintext password practice | 1–2 | WP1.2, WP2.1 hygiene |
| Cover grounded on base resume | 3 | WP3.3/cover adapt |
| Quality LLM only if `LLM_MODEL_QUALITY` set | 2–3 | WP2/WP3 config harden |

---

## 9. Requirement traceability (major PRD → plan)

| Requirement | Phase / WP |
|-------------|------------|
| Continuous autonomy | 10 / WP10.1–WP10.4; Gate F |
| Gate 1 qualification | 2 / WP2.1–WP2.5 → Checkpoint B-FCA / Gate D; WP2.6 → full Gate B / Level 2 |
| Gate 2 ATS/resume optimization | 3 / WP3.1–WP3.4 + FCA portions of WP3.5–WP3.7 → Checkpoint B-FCA / Gate D; WP3.5–WP3.8 maturity → full Gate B / Level 2 |
| Factual integrity | 2–3, 5 / WP2.1, WP3.3–WP3.4, WP5.3 — **required before Gate D** |
| Historical title integrity | 3 / WP3.2 — **required before Gate D** |
| ATS-agnostic application | 5–6 / WP5.3–WP5.4, WP6.1–WP6.5 |
| HITL | 1, 5, 9 / WP1.4, WP5.3, WP9.2 |
| Submission verification | 4–5 / WP4.4, WP5.2–WP5.5 |
| Duplicate prevention | 4 / WP4.3 |
| Dedicated Gmail | 8 / WP8.1–WP8.5 |
| Owner-reported outcomes | 8–9 / WP8.4, WP9.3 |
| Operator Console | 9 / WP9.1–WP9.5 |
| Natural-language control | 9 / WP9.3 |
| Outcome learning | 11 / WP11.1–WP11.4 (after data) |
| Windows support | 0–1 / WP0.3, WP1.5–WP1.7; Gate A |
| Security/trust boundaries | 1, 12 / WP1.1–WP1.4, WP12.1; Gates A/G |

---

## 10. Implementation order (what we build first)

1. **WP0.2–WP0.5** — **must complete or be explicitly satisfied before WP1.1** (no jump from WP0.1 → WP1.1)  
2. **WP1.1 → WP1.7** — **first substantive implementation:** security + Windows (**Gate A**)  
3. **WP2.1–WP2.5** — qualification for Checkpoint B-FCA (selected-job readiness)  
4. **WP3.1–WP3.4** + **FCA-required portions of WP3.5–WP3.7** — resume/Gate 2 for Checkpoint B-FCA  
5. **WP4.1–WP4.6** — artifacts/state (**Gate C** prep) — required before Gate D  
6. **WP5.1–WP5.3** — dry-run (**Gate C**) then **WP5.4–WP5.5** (**Gate D** first controlled real application)  
7. **Complete full Gate B** (WP2.6 + WP3.5–WP3.8 maturity portions as applicable) before Level 2 autonomous production-scale applying  
8. Then WP6 → WP7 → WP8 → WP9 → WP10 → WP11 → WP12 as gated above (Levels 2–3)  

---

## 11. Decisions still requiring owner input (non-CapSolver)

CapSolver disposition is **resolved** (REMOVE/DISABLE). Remaining owner inputs:

| # | Decision | When needed |
|---|----------|-------------|
| O1 | Explicit authorization for Gate D first real application (employer/job selection) | Before WP5.4 |
| O2 | Authoritative candidate profile content / exemplars / preferences | Phase 2 |
| O3 | Cover-letter mandatory vs conditional policy details if not fully fixed in PRD for every ATS | Phase 3/5 |
| O4 | Application pacing / daily limits preferences | Phase 10 |
| O5 | Whether to evaluate Firecrawl if enrich gaps remain after Phase 7 hardening | After evidence |
| O6 | Dedicated Gmail account creation timing (owner action outside engineering) | Before WP8.1 runtime |
| O7 | Console UX preferences within local-first constraint | Phase 9 |
| O8 | Deferral acceptance if outcome learning delayed while seeking Gate G | Phase 11–12 |

No conflict discovered that requires amending Documents 1–7. CapSolver and title/qualification clarifications already reconciled in approved `ARCHITECTURE_CURRENT.md`.

---

## 12. Explicit non-goals for early phases

- Operator Console visual polish before Gate A–D  
- Gmail before first controlled application path  
- Outcome learning before immutable evidence + outcomes  
- Broad ATS expansion before Gate D  
- New discovery providers / Firecrawl by default  
- Anthropic Skills / claude-mem / planning-with-files as product runtime  
- Vercel-hosted Console V1  
- Generalized repo-wide refactoring  
- Inventing Atlanta employer YAML catalogs from Seattle research files  
- Arbitrary calendar estimates  

---

## Document status / change control

| Field | Value |
|-------|--------|
| Authority class | Owner-approved engineering implementation plan |
| Status | Approved — Authoritative |
| Authoritativeness | Authoritative |
| Change control | Material scope/order/gate changes require deliberate documented change control. Routine implementation detail inside an approved work package does not require rewriting governance unless it materially changes architecture, policy, scope, or gates |
| Next | Begin **WP0.2–WP0.5**, then Phase 1 (WP1.1+) |

---

*End of ENGINEERING_IMPLEMENTATION_PLAN.md*  
*Status: Approved — Authoritative.*
