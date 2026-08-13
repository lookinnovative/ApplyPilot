# Architecture Discovery Standard

**Document type:** Architecture discovery standard  
**Authority class:** Owner-approved architecture discovery standard  
**Status:** Approved — Authoritative  
**Scope:** Defines the mandatory process for discovering, validating, and documenting architecture before consequential architecture decisions or implementation  
**Does not define:** The ApplyPilot architecture itself, product requirements, autonomy policy, implementation roadmap, coding standards, or vendor-specific runbooks  

---

## Document control

| Field | Value |
|-------|--------|
| Product | Personal autonomous AI job-search and job-application agent (ApplyPilot fork) |
| Companion authorities | `JOB_AGENT_PRODUCT_REQUIREMENTS.md`; `AUTONOMY_AND_APPLICATION_POLICY.md`; `ENGINEERING_METHODOLOGY.md`; `ENGINEERING_PROCESS.md`; `ENGINEERING_STANDARDS.md` (all Approved — Authoritative) |
| This document answers | **How must we determine what the system actually does, what external platforms support, what constraints exist, what is inherited vs intentional, and what architecture should be preserved, changed, replaced, or added?** |
| Output of discovery | Sufficient evidence to produce `ARCHITECTURE_CURRENT.md` and hand off to `ENGINEERING_IMPLEMENTATION_PLAN.md` |
| Change control | Future material changes require deliberate review and documented change control |

This is a permanent engineering-governance standard.

It is **not** the ApplyPilot architecture itself.

| Document | Role |
|----------|------|
| `ARCHITECTURE_DISCOVERY_STANDARD.md` | How architecture discovery must be performed |
| `ARCHITECTURE_CURRENT.md` | Resulting verified description of this repository’s architecture |
| `ENGINEERING_IMPLEMENTATION_PLAN.md` | Ordered work from verified current architecture to the approved target product |

Do **not** create `ARCHITECTURE_CURRENT.md` or `ENGINEERING_IMPLEMENTATION_PLAN.md` while only establishing this standard.

Do **not** begin the actual architecture discovery merely by creating this document.

---

## 1. Core principle

Architecture decisions must be based on verified evidence, not:

- README claims;  
- inherited documentation alone;  
- filenames;  
- comments;  
- changelog claims;  
- developer assumptions;  
- model memory;  
- package presence;  
- code snippets viewed in isolation;  
- “it should work”;  
- “the library supports it”;  
- apparent feature completeness.  

The repository must be investigated as an operating system.

For every consequential subsystem determine:

| Category | Meaning |
|----------|---------|
| **Claimed behavior** | What docs/README/changelog/comments assert |
| **Implemented behavior** | What code/config actually do |
| **Tested behavior** | What automated tests exercise |
| **Runtime-validated behavior** | What controlled runtime evidence establishes |
| **Required behavior** | What approved PRD/policy/standards require |

Do not collapse these categories.

---

## 2. Authority hierarchy

Architecture discovery must respect the existing governance hierarchy.

At minimum:

1. Owner-approved product requirements.  
2. Owner-approved autonomy/application policy.  
3. Owner-approved engineering methodology.  
4. Owner-approved engineering process.  
5. Owner-approved engineering standards.  
6. Current official vendor/platform documentation for external-system behavior.  
7. Verified repository implementation.  
8. Automated tests and controlled runtime evidence.  
9. Inherited project documentation.  
10. Historical assumptions/comments/changelog claims.  

Where an inherited implementation conflicts with an approved requirement, the inherited implementation does not redefine the requirement.

Where repository code conflicts with current official vendor behavior, investigate and document the discrepancy.

---

## 3. Documentation-first external platform discovery

For every external platform, API, SDK, framework, service, browser technology, or tool relied upon by the architecture:

**Consult current official documentation.**

This must occur:

- during initial architecture discovery;  
- before approving a consequential integration design;  
- again at relevant implementation gates;  
- during debugging where vendor behavior is material;  
- during validation before declaring the integration complete.  

Official vendor documentation is the authority for vendor-supported behavior.

Existing project code, inherited docs, old blog posts, model memory, or previous implementation assumptions must not substitute for current official documentation.

Record:

- official source consulted;  
- relevant capability;  
- relevant limitation;  
- authentication model;  
- supported platform/runtime;  
- material version requirement;  
- rate/usage limitation where relevant;  
- deprecated behavior;  
- uncertainty requiring empirical validation.  

Do not prescribe a particular citation storage format unless needed.

---

## 4. Code-trace discovery

Do not infer architecture from directory structure alone.

For each consequential capability, trace the actual execution path.

Conceptually:

**Entry point → Configuration → Domain logic → External dependencies → Persistence → Side effect → State transition → Error path → Observability.**

Identify:

- entry points;  
- call chains;  
- state ownership;  
- database interactions;  
- filesystem interactions;  
- subprocesses;  
- browser execution;  
- network calls;  
- model calls;  
- credentials;  
- concurrency;  
- retry behavior;  
- failure behavior.  

Trace sufficiently to distinguish working implementation from architectural scaffolding.

Repository structure categories that discovery must govern include, without treating the list as exhaustive:

- CLI / pipeline orchestration;  
- discovery scrapers and employer registries;  
- enrichment;  
- scoring / qualification;  
- resume tailoring / cover / document rendering;  
- validation;  
- apply launcher / orchestrator / HITL / result handlers;  
- Chrome / extension / CDP;  
- LLM client;  
- database / state machine;  
- tracking / Gmail;  
- configuration / wizard;  
- tests / scripts / CI.  

---

## 5. Claim-to-code verification

Important inherited claims must be verified against implementation.

Examples include claims such as:

- “supports Workday”;  
- “supports Greenhouse”;  
- “persists sessions”;  
- “uses LLM fallback”;  
- “tracks Gmail”;  
- “handles CAPTCHA with HITL”;  
- “supports five workers”;  
- “works on Windows”;  
- “supports Claude Code Max billing”;  
- “prevents duplicate applications”;  
- “tailors resumes”;  
- “validates fabrication”;  
- “supports multiple ATS systems.”  

For each material claim determine whether it is:

| Result | Meaning |
|--------|---------|
| **Verified** | Established by code/tests/runtime evidence |
| **Partially verified** | Some capability exists; claim overstates completeness |
| **Unverified** | Insufficient evidence |
| **Contradicted** | Evidence conflicts with the claim |
| **Obsolete** | Once true; no longer reflects implementation |
| **Not applicable** | Claim does not apply to this fork’s target |

Do not treat changelog presence as proof.

---

## 6. Test discovery

Inspect tests as architectural evidence.

Determine:

- what behavior is tested;  
- what is mocked;  
- what reaches real dependencies;  
- what platforms are exercised;  
- what failure modes are covered;  
- whether tests reflect current implementation;  
- whether tests prove the claimed behavior.  

Passing tests do not prove behavior outside their test boundary.

Explicitly identify consequential behavior with little/no meaningful test coverage.

---

## 7. Runtime validation

Where static inspection cannot establish behavior, architecture discovery may require controlled runtime validation.

Runtime validation must follow `ENGINEERING_PROCESS.md` and `AUTONOMY_AND_APPLICATION_POLICY.md`.

Do not perform uncontrolled real job submissions merely to learn architecture.

Use:

- dry-run;  
- synthetic fixtures;  
- test forms;  
- controlled test accounts;  
- safe read-only operations;  
- authorized staged validation  

where practical.

Clearly distinguish:

**Statically verified**  
from  
**Runtime verified.**

---

## 8. Inherited vs target architecture

For each major subsystem, distinguish:

| Layer | Meaning |
|-------|---------|
| **Inherited current architecture** | What exists now |
| **Approved product requirement** | What must ultimately exist |
| **Target architecture** | Architecture chosen to satisfy the requirement |

Do not redesign simply because the code is inherited.

Do not preserve inherited architecture simply because it already exists.

Evaluate each subsystem as:

**Preserve / Preserve + harden / Adapt / Replace / Remove / Add new capability / Defer.**

Require evidence/reasoning for consequential decisions.

---

## 9. Reuse-first standard

Architecture discovery should actively identify reusable inherited capability.

Before proposing replacement, determine:

- does it already satisfy the requirement?  
- can it satisfy the requirement with bounded hardening?  
- are its defects localized?  
- are its dependencies still supported?  
- is replacement risk greater than repair risk?  

Avoid unnecessary reconstruction.

But reuse is not mandatory when inherited design violates product, security, platform, or reliability requirements.

---

## 10. Current platform reality

Architecture discovery must explicitly identify the actual deployment/development environment.

For this project, Windows support is an approved engineering requirement.

Discovery must therefore examine actual Windows implications rather than treating Linux behavior as sufficient.

Investigate:

- filesystem paths;  
- home-directory assumptions;  
- virtualenv executable locations;  
- subprocess behavior;  
- shell assumptions;  
- process signals;  
- executable discovery;  
- browser discovery;  
- browser profiles;  
- CDP;  
- Playwright/Patchright behavior;  
- Claude Code invocation;  
- Node/npx invocation;  
- environment propagation;  
- temporary files;  
- locking;  
- concurrency.  

Classify Linux-only assumptions as:

- irrelevant;  
- portable as-is;  
- requires abstraction;  
- requires Windows implementation;  
- blocker.  

Do not assume Windows incompatibility merely from Unix-looking code.

Verify it.

---

## 11. Blocker classification

Architecture discovery must identify genuine blockers separately from ordinary implementation work.

A **blocker** means the approved product cannot proceed through the relevant gate without resolving it.

Classify findings where useful as:

| Class | Meaning |
|-------|---------|
| **Blocker** | Must resolve before the relevant gate |
| **High risk** | Serious; may become a blocker |
| **Required remediation** | Must fix for product conformance |
| **Normal implementation** | Planned product work |
| **Optional improvement** | Beneficial, not required for gate |
| **Deferred** | Explicitly postponed with rationale |

Do not label every defect a blocker.

Do not minimize genuine blockers as technical debt.

---

## 12. Security architecture discovery

Security discovery must trace trust boundaries.

At minimum examine:

- browser/ATS content;  
- job descriptions;  
- email content;  
- LLM prompts;  
- LLM outputs;  
- local filesystem;  
- source repository;  
- secrets;  
- credentials;  
- browser sessions;  
- subprocesses;  
- shell access;  
- external APIs;  
- candidate data;  
- generated artifacts.  

Determine where untrusted data can cross into privileged execution.

Specifically investigate prompt-injection exposure from:

- job descriptions;  
- employer pages;  
- ATS pages;  
- embedded page content;  
- emails.  

Do not assume prompt instructions alone establish a security boundary.

---

## 13. Secrets / credential discovery

Identify:

- what credentials exist;  
- where they are loaded;  
- which process receives them;  
- which subprocess inherits them;  
- whether browser/page content can influence privileged processes;  
- whether secrets can enter prompts/logs;  
- whether credentials are unnecessarily broad.  

Do not expose actual secret values in discovery documentation.

Document credential classes and flows, not secret contents.

---

## 14. Browser automation discovery

Treat browser automation as a first-class architecture subsystem.

Trace:

- browser launcher;  
- browser/runtime selection;  
- executable discovery;  
- Playwright/Patchright/CDP use;  
- browser profile/session persistence;  
- login persistence;  
- ATS navigation;  
- form interpretation;  
- uploads;  
- screening answers;  
- submit behavior;  
- HITL;  
- CAPTCHA/MFA behavior;  
- submission verification;  
- worker isolation;  
- cleanup/recovery.  

Determine what Claude Code is actually responsible for versus what deterministic application code controls.

Do not infer this from README diagrams alone.

---

## 15. Claude Code / agent execution discovery

Because inherited ApplyPilot uses Claude Code subprocesses for auto-apply, discovery must determine:

- how subprocesses are spawned;  
- exact responsibilities;  
- available tools;  
- MCP configuration;  
- browser access;  
- filesystem access;  
- environment inheritance;  
- API key handling;  
- Max-plan/API billing assumptions;  
- timeout behavior;  
- concurrency;  
- output/result protocol;  
- failure recovery;  
- security boundaries.  

Consult current official Claude/Anthropic documentation where behavior is vendor-dependent.

Do not assume inherited billing/tooling behavior remains current.

---

## 16. ATS architecture discovery

Architecture discovery must determine what “ATS support” actually means in the inherited system.

Do not treat all ATS systems as equivalent.

For each supported or targeted ATS/application class, determine applicable layers such as:

- discovery;  
- enrichment;  
- job identification;  
- qualification;  
- application navigation;  
- account creation/login;  
- session persistence;  
- form filling;  
- document upload;  
- screening questions;  
- CAPTCHA/MFA;  
- submission;  
- verification;  
- outcome/status tracking.  

Include investigation of at least the ATS/application classes required by the approved PRD.

This includes, where applicable:

- Indeed-type/native quick-apply flows;  
- Workday;  
- Greenhouse;  
- Lever;  
- iCIMS;  
- Taleo/Oracle;  
- SAP SuccessFactors;  
- SmartRecruiters;  
- Ashby;  
- ADP recruiting flows;  
- UKG recruiting flows;  
- Jobvite;  
- custom employer career sites;  
- redirect/unknown ATS flows.  

Do **not** claim universal support.

The discovery result should identify, at the appropriate capability level:

**Supported / Partial / Unsupported / Unknown/needs validation.**

---

## 17. Unknown ATS fallback discovery

Investigate what happens when a qualified job routes to an ATS/application system without a dedicated adapter.

Determine whether the inherited architecture:

- can navigate generically;  
- parks the application;  
- fails;  
- skips it;  
- requires owner intervention;  
- incorrectly marks it unsupported.  

Target architecture should preserve qualified opportunities where practical rather than silently discarding them solely because the ATS is unfamiliar.

Do not define the final fallback architecture in this standard.

Require that architecture discovery address it.

---

## 18. Account / session architecture discovery

Investigate ATS account and session behavior.

Determine:

- when accounts are required;  
- how credentials are sourced;  
- how sessions are persisted;  
- whether persistence works per ATS/domain;  
- how expiration is detected;  
- how MFA is handled;  
- how owner intervention resumes execution;  
- whether multiple employer portals conflict;  
- whether sessions survive application restarts.  

Do not assume “session persistence” is one universal mechanism.

---

## 19. Job discovery architecture

Trace every actual discovery source.

Determine:

- which sources are active;  
- which are optional;  
- which depend on third-party scraping libraries;  
- what configuration drives them;  
- deduplication;  
- employer-specific catalogs;  
- location filtering;  
- search query generation;  
- stale/dead sources;  
- source-specific limitations.  

Identify developer-specific inherited search data separately from reusable architecture.

Specifically inspect inherited files such as:

- `docs/seattle_employers_v1.yaml`  
- `docs/seattle_employers_v2.yaml`  
- `docs/seattle_employers_v3_megacorps.yaml`  

Determine:

- whether runtime code references them;  
- whether tests reference them;  
- whether docs reference them;  
- whether they contain reusable architecture or only previous-developer targeting data.  

Do **not** delete, move, or replace them during discovery.

Record a later disposition recommendation:

**Keep / Archive / Remove / Migrate/generalize.**

Do **not** create an Atlanta (or other geography) replacement merely because Seattle files exist.

---

## 20. Qualification / scoring discovery

Trace:

**JD → Extraction/enrichment → Candidate profile → Scoring prompt/model → Structured result → Score persistence → Qualification threshold → Downstream routing.**

Determine:

- what is deterministic;  
- what is LLM-based;  
- what evidence is supplied;  
- what thresholds exist;  
- what hard-coded candidate assumptions exist;  
- what location/salary/title logic exists;  
- what can incorrectly reject qualified jobs.  

Compare against the approved PRD’s Gate 1 requirements.

---

## 21. ATS screening / resume optimization discovery

Trace current tailoring behavior.

Determine:

- how the base resume is represented;  
- how candidate facts are represented;  
- how JD requirements are extracted;  
- how tailoring prompts work;  
- what validation occurs;  
- what “fabrication detection” actually validates;  
- how titles are handled;  
- how keywords/terminology are handled;  
- how resume format is rendered/preserved;  
- whether post-tailor ATS/screening analysis exists;  
- whether the exact submitted artifact is preserved.  

Compare against Gate 2 requirements.

Do not assume current tailoring equals ATS optimization.

---

## 22. Document / resume rendering discovery

Determine:

- source resume format;  
- structured resume representation;  
- PDF/DOCX generation path;  
- fonts/layout dependencies;  
- platform dependencies;  
- output naming;  
- artifact identity;  
- upload selection;  
- rendering validation.  

Determine whether repeated tailoring can degrade layout or create cross-job artifact risk.

---

## 23. Screening question / Q&A discovery

Trace the inherited Q&A knowledge base.

Determine:

- schema;  
- storage;  
- retrieval;  
- exact-match/fuzzy/LLM behavior;  
- source/provenance;  
- approval status;  
- candidate-fact boundaries;  
- unknown-question behavior;  
- learning/update behavior.  

Compare against the autonomy policy.

Do not treat previously answered questions as automatically reusable unless policy allows it.

---

## 24. Email / Gmail discovery

Trace the inherited Gmail capability end to end.

Determine:

- authentication method;  
- scopes;  
- account assumptions;  
- message search;  
- classification;  
- application matching;  
- status transitions;  
- false-positive risks;  
- test coverage;  
- whether it is polling or event-driven;  
- token persistence;  
- Windows implications;  
- failure handling.  

Consult current official Google/Gmail documentation before target architecture decisions.

The approved product will use a dedicated job-search mailbox.

Do not hard-code an account during discovery.

---

## 25. Outcome tracking discovery

Determine what outcome states currently exist and how they are produced.

Trace:

**Email / ATS / owner event → Classification → Application resolution → State transition → Persistence → Learning signal.**

Identify gaps between inherited behavior and approved requirements for:

- recruiter outreach;  
- recruiter screen;  
- interviews;  
- later-stage interviews;  
- rejection;  
- offer;  
- owner-reported outcomes;  
- provenance.  

---

## 26. Operator Console discovery

The Operator Console is a new approved product requirement.

Discovery must determine what existing components can be reused for it.

Inspect:

- current HTML dashboard;  
- CLI;  
- database access layer;  
- status reporting;  
- artifact viewers;  
- human-review helpers / local HTTP server behavior;  
- configuration mechanisms;  
- state transitions.  

Determine what can be:

**Preserved / Extended / Reused as backend / Replaced / Left as engineering-only.**

Do not assume the current HTML dashboard is sufficient.

Do not choose the final frontend framework in this standard.

---

## 27. Natural-language control discovery

Determine the architecture needed to support:

**Owner message → Intent → Entity resolution → Policy check → Structured action → Durable state → Audit → Response.**

Identify which existing domain operations can safely be exposed as structured actions.

Determine where new application services/command boundaries are required.

Natural-language generation must not directly mutate arbitrary database state.

---

## 28. Outcome-learning architecture discovery

Determine what data already exists to support learning from actual application outcomes.

Inspect whether the system preserves:

- original JD;  
- candidate profile/version;  
- screening analysis;  
- exact submitted resume;  
- cover letter;  
- screening answers;  
- application timestamps;  
- ATS;  
- outcome;  
- outcome provenance.  

Identify missing historical binding/versioning.

Determine what architecture would be necessary to compare interview-producing application/resume/JD combinations over time without corrupting candidate truth.

Do not select a machine-learning technique merely because the feature is called “learning.”

Evaluate deterministic/statistical/LLM-assisted approaches based on actual data volume and requirements.

---

## 29. Persistence / database discovery

Trace the SQLite architecture.

Determine:

- schema;  
- migration behavior;  
- WAL use;  
- thread-local connections;  
- transaction boundaries;  
- concurrency behavior;  
- locking;  
- state machine representation;  
- historical artifact references;  
- restart/recovery;  
- backup needs;  
- data retention.  

Evaluate whether SQLite remains sufficient.

Do **not** replace SQLite merely because the product uses autonomous agents.

Require evidence for any database migration recommendation.

---

## 30. Concurrency discovery

Trace:

- worker acquisition;  
- locking;  
- job partitioning;  
- browser/session isolation;  
- artifact isolation;  
- database writes;  
- retry interactions;  
- global-stop behavior;  
- credit exhaustion behavior.  

Identify races that could cause:

- duplicate submission;  
- wrong resume upload;  
- state corruption;  
- credential/session collision.  

---

## 31. LLM architecture discovery

Trace all model use.

Determine:

- providers;  
- models;  
- fast/quality tiers;  
- fallback order;  
- structured vs free-form outputs;  
- token limits;  
- retry/cooldown;  
- API-key handling;  
- cost;  
- deterministic preprocessing;  
- model-specific assumptions.  

Consult current official provider documentation for target decisions.

Do not assume model names or free-tier availability remain current.

---

## 32. Cost architecture discovery

Identify all potentially material operating costs:

- LLM APIs;  
- Claude Code usage;  
- job-data providers;  
- email/API usage where applicable;  
- browser infrastructure;  
- hosting if Operator Console becomes a service;  
- storage;  
- optional external services.  

Separate:

**Current required cost / Optional cost / Future cost.**

Do not invent cost estimates without evidence.

---

## 33. Dependency discovery

Inventory consequential dependencies.

For each material dependency determine:

- purpose;  
- version constraint;  
- maintenance status;  
- Windows support;  
- known architectural role;  
- whether it duplicates another dependency;  
- whether it is still needed;  
- whether official docs support current usage.  

Pay special attention to browser/scraping packages and dependencies installed outside normal package metadata.

---

## 34. Configuration discovery

Identify all configuration sources:

- environment variables;  
- `.env` / user config;  
- profile JSON;  
- YAML;  
- package defaults;  
- hard-coded values;  
- CLI flags;  
- database state.  

Determine precedence.

Identify duplicated/conflicting configuration.

Separate:

**Product policy / Candidate data / Search config / Runtime config / Secrets / Developer-specific data.**

---

## 35. Data classification

Architecture discovery should classify important data categories.

At minimum:

- candidate facts;  
- candidate preferences;  
- credentials/secrets;  
- job data;  
- job descriptions;  
- generated resumes;  
- cover letters;  
- screening answers;  
- application records;  
- outcome evidence;  
- owner instructions;  
- learning evidence;  
- logs.  

Identify persistence location and sensitivity.

---

## 36. Failure / recovery discovery

For each consequential subsystem determine:

- failure modes;  
- retry behavior;  
- parked state;  
- restart behavior;  
- partial-state behavior;  
- manual recovery;  
- observability.  

Pay particular attention to:

- browser crash;  
- worker crash;  
- machine restart;  
- network failure;  
- model exhaustion;  
- Gmail auth expiration;  
- ATS session expiration;  
- CAPTCHA/MFA;  
- database lock;  
- interrupted submission.  

---

## 37. Observability discovery

Determine what can currently be observed through:

- logs;  
- database;  
- status CLI;  
- dashboard;  
- apply logs;  
- browser state;  
- email tracking.  

Identify where the operator cannot determine what happened.

Target architecture must support truthful operational status.

---

## 38. Human-in-the-loop discovery

Trace current HITL mechanisms.

Determine:

- trigger conditions;  
- parked-job representation;  
- browser persistence;  
- local HTTP server behavior;  
- resume mechanism;  
- timeout;  
- multiple concurrent HITL cases;  
- Windows behavior;  
- owner visibility.  

Compare against the approved Operator Console requirements.

---

## 39. Duplicate / identity discovery

Determine how the system identifies:

- jobs;  
- requisitions;  
- companies;  
- applications;  
- artifacts.  

Trace URL normalization and deduplication.

Determine whether retries or cross-source discovery could produce duplicate applications.

---

## 40. Historical / developer-specific artifacts

Identify files that are:

- historical experiments;  
- previous-developer personal data;  
- obsolete setup artifacts;  
- dead configuration;  
- temporary debugging tools;  
- architecture documentation that no longer reflects runtime.  

Do not remove them during discovery.

Recommend later disposition with evidence.

---

## 41. Architecture decision evidence

Every consequential architecture recommendation should identify:

- requirement being satisfied;  
- current implementation;  
- evidence;  
- problem/gap;  
- options considered;  
- recommended direction;  
- reuse impact;  
- migration risk;  
- validation needed.  

Do not require formal ADRs for every trivial decision.

Use proportional rigor.

---

## 42. Uncertainty register

Architecture discovery must maintain explicit unresolved questions.

For each material uncertainty record:

- question;  
- why it matters;  
- current evidence;  
- what would resolve it;  
- whether it blocks architecture;  
- whether it can be deferred.  

Do not hide uncertainty inside confident prose.

---

## 43. Architecture discovery output

The eventual architecture discovery should provide enough evidence to create:

`docs/governance/ARCHITECTURE_CURRENT.md`

That document should be capable of describing:

- verified current architecture;  
- major execution flows;  
- persistence;  
- external integrations;  
- browser/agent architecture;  
- security/trust boundaries;  
- Windows compatibility;  
- ATS capability matrix;  
- reusable inherited components;  
- gaps against approved requirements;  
- blockers;  
- uncertainties;  
- recommended target direction.  

Do **not** create `ARCHITECTURE_CURRENT.md` in this task.

---

## 44. Implementation-plan handoff

Architecture discovery must be sufficiently complete that the subsequent:

`docs/governance/ENGINEERING_IMPLEMENTATION_PLAN.md`

can be based on evidence rather than speculation.

The implementation plan should eventually be able to distinguish:

- prerequisite remediation;  
- preserved architecture;  
- security hardening;  
- Windows remediation;  
- new product capability;  
- ATS expansion;  
- validation gates;  
- production-readiness gates.  

Do **not** create the implementation plan now.

---

## 45. Stop conditions for discovery

Architecture discovery must stop and surface the issue rather than inventing an answer when:

- official vendor behavior cannot be established;  
- repository behavior cannot be traced;  
- runtime validation would require an unauthorized consequential action;  
- required credentials are unavailable;  
- multiple architecture interpretations remain materially plausible;  
- an approved governance conflict is discovered.  

Uncertainty is an acceptable discovery result.

Guessing is not.

---

## 46. Proportionality

Do not turn architecture discovery into endless analysis.

Investigate deeply enough to make the consequential architecture decision safely.

Avoid spending equivalent effort on:

- dead utility code;  
- inconsequential formatting helpers;  
- trivial constants  

as on:

- submission;  
- browser security;  
- candidate facts;  
- ATS behavior;  
- Windows compatibility;  
- persistence;  
- credentials;  
- autonomous actions.  

---

## 47. Required discovery phases

Define a reusable phased discovery process.

Use approximately these phases, adapting terminology if needed:

| Phase | Focus |
|-------|--------|
| **1 — Governance / requirement baseline** | Read authoritative requirements and identify architecture obligations |
| **2 — Repository / execution mapping** | Map entry points, components, data, configuration, persistence, dependencies, and major flows |
| **3 — External platform validation** | Consult current official vendor documentation for consequential integrations |
| **4 — Code / test / runtime verification** | Trace actual implementation and validate important assumptions proportionally |
| **5 — Gap / risk / reuse analysis** | Compare current architecture with approved requirements |
| **6 — Target architecture recommendations** | Identify preserve/harden/adapt/replace/remove/add/defer decisions |
| **7 — Architecture handoff** | Produce verified architecture documentation, blocker/uncertainty register, and sufficient evidence for implementation planning |

Do not treat phases as rigid bureaucracy when work can safely overlap.

---

## 48. Discovery completion criteria

Architecture discovery is complete enough for implementation planning only when:

- major product flows are traced;  
- consequential external integrations are checked against current official docs;  
- Windows compatibility is assessed;  
- security trust boundaries are understood;  
- browser/Claude execution is understood;  
- persistence/state is understood;  
- ATS coverage is characterized;  
- resume/screening behavior is understood;  
- Gmail/outcome tracking is understood;  
- Operator Console reuse/new-work boundary is understood;  
- outcome-learning data gaps are understood;  
- major blockers are identified;  
- material uncertainties are recorded;  
- preserve/adapt/replace recommendations are evidence-backed.  

Do not require every minor code path to be documented.

---

## 49. Relationship to governance set

| Document | Answers |
|----------|---------|
| `JOB_AGENT_PRODUCT_REQUIREMENTS.md` | What the product must do |
| `AUTONOMY_AND_APPLICATION_POLICY.md` | What the agent is authorized to do |
| `ENGINEERING_METHODOLOGY.md` | How engineering decisions are reasoned about |
| `ENGINEERING_PROCESS.md` | How engineering work is executed |
| `ENGINEERING_STANDARDS.md` | Concrete technical requirements |
| `ARCHITECTURE_DISCOVERY_STANDARD.md` | Mandatory method for discovering and validating architecture |
| `ARCHITECTURE_CURRENT.md` | Verified resulting architecture |
| `ENGINEERING_IMPLEMENTATION_PLAN.md` | Ordered roadmap from current architecture to target product |

---

## 50. Document status / change control

| Field | Value |
|-------|--------|
| Authority class | Owner-approved architecture discovery standard |
| Status | Approved — Authoritative |
| Authoritativeness | Authoritative |
| Change control | Future material changes require deliberate review and documented change control |

---

*End of ARCHITECTURE_DISCOVERY_STANDARD.md*  
*Status: Approved — Authoritative.*
