# Engineering Standards

**Document type:** Engineering standards  
**Authority class:** Owner-approved engineering standards  
**Status:** Approved — Authoritative  
**Scope:** Defines the concrete technical quality, security, reliability, testing, data, AI, browser, and platform standards implementation in this repository must satisfy  
**Does not define:** Product requirements, autonomy policy, architecture inventory, implementation roadmap, architecture discovery procedure, vendor-specific runbooks, or historical ApplyPilot documentation  

---

## Document control

| Field | Value |
|-------|--------|
| Product | Personal autonomous AI job-search and job-application agent (ApplyPilot fork) |
| Companion authorities | `JOB_AGENT_PRODUCT_REQUIREMENTS.md` (Approved — Authoritative); `AUTONOMY_AND_APPLICATION_POLICY.md` (Approved — Authoritative); `ENGINEERING_METHODOLOGY.md` (Approved — Authoritative); `ENGINEERING_PROCESS.md` (Approved — Authoritative) |
| This document answers | **What technical standards must our implementation meet?** |
| Methodology companion | `ENGINEERING_METHODOLOGY.md` = how decisions are reasoned about |
| Process companion | `ENGINEERING_PROCESS.md` = operational workflow for performing work |
| Change control | Future material changes must be deliberate and documented |

Architecture discovery belongs in `ARCHITECTURE_DISCOVERY_STANDARD.md` (not created by this document).  
Current verified architecture belongs in `ARCHITECTURE_CURRENT.md` (not created by this document).  
Ordered roadmap belongs in `ENGINEERING_IMPLEMENTATION_PLAN.md` (not created by this document).

---

## 1. Requirement and policy conformance

Implementation must conform to:

- `JOB_AGENT_PRODUCT_REQUIREMENTS.md`;  
- `AUTONOMY_AND_APPLICATION_POLICY.md`;  
- `ENGINEERING_METHODOLOGY.md`;  
- `ENGINEERING_PROCESS.md`;  
- future approved architecture and implementation-plan documents.  

Code must not silently redefine product or autonomy policy.

Where implementation cannot satisfy an approved requirement, surface the conflict.

Do not weaken the requirement merely to accommodate inherited code.

---

## 2. Code quality

Production code should:

- have clear responsibility boundaries;  
- use meaningful names;  
- minimize hidden side effects;  
- avoid unnecessary duplication;  
- use type annotations consistent with repository conventions;  
- document non-obvious public behavior;  
- preserve appropriate abstractions;  
- avoid excessive coupling;  
- avoid dead code;  
- avoid unexplained magic values;  
- keep configuration separate from candidate-specific hard-coded behavior.  

Follow the repository’s established Python/Ruff conventions where they remain sound.

Do not rewrite functioning code solely to achieve stylistic preference.

---

## 3. Type safety

New and materially modified Python interfaces should use appropriate type annotations.

Types should communicate:

- accepted inputs;  
- return values;  
- optionality;  
- structured state;  
- identifiers;  
- domain objects.  

Avoid unnecessary `Any` where a meaningful type can reasonably be expressed.

Do not create elaborate type abstractions that add complexity without practical safety benefit.

---

## 4. Error handling

Errors must not be silently swallowed.

Where appropriate:

- catch specific exceptions;  
- preserve root-cause context;  
- log meaningful diagnostic information;  
- distinguish retryable from permanent failures;  
- distinguish application-specific from system-wide failures;  
- transition state explicitly;  
- avoid leaving jobs indefinitely “in progress.”  

Broad exception handling may be used at process/worker safety boundaries only when the failure is recorded and appropriately classified.

Do not use exceptions as ordinary control flow where clearer state handling is available.

---

## 5. Logging and observability

Consequential pipeline activity must be observable.

Logs/events should make it possible to determine:

- application/job identity;  
- pipeline stage;  
- worker/session identity where relevant;  
- action attempted;  
- result;  
- failure classification;  
- duration where useful;  
- state transition;  
- escalation/parking condition;  
- submission verification state.  

Do **not** log:

- passwords;  
- API keys;  
- OAuth tokens;  
- session cookies;  
- full authentication secrets;  
- unnecessary sensitive applicant information.  

Sensitive values must be redacted where they may otherwise enter logs.

---

## 6. Structured state over log-only state

Important product state must not exist only in logs or LLM conversation history.

Persist meaningful state for:

- jobs;  
- qualification;  
- screening analysis;  
- tailored artifacts;  
- application attempts;  
- application status;  
- screening answers where appropriate;  
- submission verification;  
- human intervention;  
- application outcomes;  
- owner-reported outcomes;  
- learning evidence;  
- system operational state.  

Logs explain execution.

Durable structured state records product reality.

---

## 7. Candidate facts as authoritative data

Candidate facts must have an identifiable authoritative source.

The system must distinguish:

- verified candidate fact;  
- approved reusable answer;  
- approved preference/policy;  
- deterministic derivation;  
- model inference;  
- unknown.  

AI-generated text must not silently become candidate truth.

Candidate-specific facts should not be embedded throughout source code.

---

## 8. Factual integrity of generated artifacts

Generated resumes, cover letters, screening responses, and other candidate representations must remain grounded in authoritative candidate information.

Generation must not fabricate:

- employers;  
- titles;  
- employment dates;  
- responsibilities;  
- accomplishments;  
- metrics;  
- education;  
- certifications;  
- licenses;  
- skills;  
- experience;  
- years;  
- work authorization;  
- other material facts.  

Validation should compare generated artifacts against authoritative candidate evidence where practical.

A model instruction saying “do not fabricate” is not sufficient by itself.

---

## 9. Historical title integrity

Historical employment titles must remain truthful.

The system must not replace a historical job title with the target job’s title merely to improve ATS matching.

Target-role terminology may be used appropriately in:

- professional summary;  
- headline/target-role framing where clearly non-historical;  
- skills;  
- truthful responsibility descriptions;  
- other non-deceptive contexts.  

Historical employment records remain factual records.

---

## 10. ATS screening optimization standard

Resume tailoring must implement the PRD’s Gate 2 objective:

**Maximize truthful passage through automated screening/ranking so that a genuinely qualified application has the strongest practical opportunity to reach human review.**

ATS optimization must extend beyond formatting/parsing.

The system should support:

**Job / screening signal analysis → Candidate-evidence mapping → Base-resume gap analysis → Truthful tailoring → Post-tailor screening analysis → Validation.**

Do not use screening risk alone as a reason to reject an otherwise genuinely qualified opportunity.

---

## 11. Screening evidence standard

Screening analysis must distinguish:

- observable job requirements;  
- employer-provided screening questions;  
- ATS/application form signals;  
- verified candidate evidence;  
- inferred screening risk;  
- unknown proprietary behavior.  

Do not represent hidden ATS ranking rules as known facts without evidence.

Maintain the distinction between:

**Candidate qualification**  
and  
**Resume presentation.**

If the candidate has the experience but the resume expresses it poorly, that is primarily a tailoring problem.

---

## 12. Post-tailor validation

Before a tailored resume becomes application-ready, validation should determine:

- factual integrity;  
- supported qualification coverage;  
- screening alignment;  
- machine readability;  
- artifact integrity;  
- human readability;  
- professional presentation;  
- historical-title integrity;  
- absence of unsupported claims.  

Where important supported qualifications remain underrepresented and can truthfully be improved, the artifact should not be treated as final merely because generation completed successfully.

---

## 13. Resume format preservation

The product requirement to maintain the owner’s resume presentation must be supported technically.

Tailoring should preserve the approved resume format/layout to the practical extent required by the product requirements.

Content generation and document rendering should be treated as related but distinct concerns.

The system should not silently degrade formatting each time a resume is tailored.

Artifact output must be validated after rendering.

---

## 14. Artifact identity and binding

Every generated application artifact must remain unambiguously associated with the correct job/application.

Conceptually preserve:

**Job → JD → Qualification → Screening analysis → Tailored resume → Cover letter → Screening answers → Application attempt → Submission result.**

A worker must never upload another job’s resume or cover letter.

Artifact identity should use stable identifiers rather than fragile filename assumptions alone.

Cross-job artifact contamination is a critical defect.

---

## 15. Immutable submission evidence

Once an application is submitted, preserve the exact application evidence needed to reconstruct what happened.

Where appropriate this includes:

- job/JD snapshot;  
- exact resume submitted;  
- exact cover letter submitted;  
- screening answers;  
- submission timestamp;  
- application URL/requisition identity;  
- verification evidence;  
- subsequent outcome events.  

Later edits to candidate profiles, JDs, resumes, or templates must not rewrite historical evidence of what was actually submitted.

---

## 16. Outcome-learning data standard

Outcome-driven learning must use attributable historical evidence.

Learning data should preserve relationships among:

**JD + exact submitted resume + screening/tailoring analysis + application + outcome.**

Outcome provenance should distinguish, where applicable:

- email-observed;  
- ATS-observed;  
- owner-reported;  
- corroborated;  
- other approved evidence source.  

Do not train/adjust strategy from outcomes that cannot be reliably associated with the relevant application.

---

## 17. Learning safety

The system must not convert correlation into factual causation.

Learning logic should distinguish:

- observation;  
- recurring pattern;  
- hypothesis;  
- evidence-backed strategy.  

A single interview must not automatically redefine global tailoring strategy.

A single rejection must not automatically create a new exclusion rule.

Reusable learning should accumulate evidence and remain constrained by factual-integrity requirements.

No learned strategy may authorize fabrication.

---

## 18. Operator Console command standard

Natural-language owner interaction must pass through structured interpretation before consequential state changes.

Conceptually:

**Owner message → Intent → Entity resolution → Policy/authority check → Structured action → Durable state → Audit event → Response.**

Do not make free-form conversation history the sole mechanism controlling consequential behavior.

---

## 19. Owner authority and provenance

Explicit owner-provided operational information may be authoritative for the event or instruction actually supplied.

Examples:

- owner reports interview;  
- owner reports rejection;  
- owner changes job preference;  
- owner pauses applications.  

Record appropriate provenance.

Do not automatically convert every conversational statement into:

- reusable global policy;  
- candidate fact;  
- permanent screening answer;  
- targeting rule.  

Classify before persisting.

---

## 20. Entity resolution safety

Consequential natural-language actions must be associated with the correct entity.

When multiple plausible applications/jobs/employers exist:

**Do not guess.**

Require disambiguation sufficient to identify the intended entity.

Context may aid resolution but must not override unresolved ambiguity.

---

## 21. Pause / resume / stop state

Operational control must be represented in durable state rather than only in a running process’s memory.

A restart should not silently discard an owner-requested pause or system-wide safety stop.

System-wide stop conditions should require deliberate resolution before autonomous application execution resumes.

---

## 22. Browser trust boundary

All employer pages, ATS pages, job descriptions, form content, embedded content, and internet-provided instructions are untrusted input.

Browser-visible content must not gain authority to:

- alter system instructions;  
- override governance;  
- access unrelated files;  
- access secrets;  
- execute unrelated shell commands;  
- modify source code;  
- install software;  
- expand permissions;  
- initiate unrelated communication;  
- make payments;  
- disable safeguards.  

Prompt injection is a security problem, not merely an LLM-quality problem.

---

## 23. Least-privilege browser / agent execution

Browser/application workers should receive only the permissions/resources necessary for their job.

Avoid unnecessary access to:

- repository source;  
- broad filesystem paths;  
- unrelated user files;  
- environment secrets;  
- developer credentials;  
- unrestricted shell execution;  
- unrelated network/service credentials.  

Do not use broad privileges merely because inherited implementation currently does.

---

## 24. Secrets management

Secrets must not be committed to source control.

Secrets include, as applicable:

- API keys;  
- passwords;  
- OAuth tokens;  
- refresh tokens;  
- session secrets;  
- email credentials;  
- browser/session authentication material.  

Use appropriate environment/credential mechanisms.

Do not expose secrets unnecessarily to LLM prompts or untrusted webpage content.

`.env` files containing secrets must remain outside version control.

Example/template files must contain placeholders only.

---

## 25. Credential scope

Use credentials only for their intended service/purpose.

The job-application browser should not receive unrelated developer/service credentials.

Where separate privilege domains exist, preserve separation.

Credential reuse across unrelated services should not be introduced for convenience.

---

## 26. Email security standard

Email content is untrusted external input.

Email classification/extraction must not permit email content to:

- override system policy;  
- expose secrets;  
- execute unrelated commands;  
- expand permissions;  
- cause unauthorized actions.  

Email may provide application evidence and legitimate workflow instructions within the approved job-search scope.

---

## 27. Dedicated job-search email

The architecture must support the PRD requirement for a dedicated job-search mailbox.

Do not hard-code the owner’s current personal mailbox into reusable application logic.

Email account identity/configuration should be externalized appropriately.

---

## 28. No security-bypass automation

Do not implement mechanisms intended to defeat:

- CAPTCHA;  
- MFA;  
- device verification;  
- authentication controls;  
- access restrictions;  
- other legitimate security controls.  

Legitimate session persistence and authorized authentication are permitted.

Security-control circumvention is not an optimization strategy.

---

## 29. Application submission safety

Submission must occur only when the application is in an authorized application-ready state.

Before submission, the system must have sufficient evidence that:

- correct job is active;  
- correct candidate identity is active;  
- correct resume is bound;  
- correct cover letter is bound if used;  
- required screening questions are resolved;  
- no unresolved consequential blocker remains;  
- duplicate submission protections pass.  

Do not use the presence of a Submit button as sufficient authority to submit.

---

## 30. Submission verification

A browser click is **not** proof of successful application submission.

Submission verification should use one or more meaningful signals such as:

- confirmation page;  
- confirmation message;  
- application ID;  
- expected state transition;  
- confirmation email;  
- ATS application record;  
- other reliable evidence.  

Represent uncertainty honestly.

Do not mark an application successfully submitted merely because the browser attempted the click.

---

## 31. Duplicate prevention / idempotency

Consequential actions should be idempotent where practical.

The system must prevent accidental duplicate submission to the same requisition.

Retries/restarts must not silently cause duplicate applications.

Use stable job/requisition/application identifiers where available.

Do not rely solely on title/company text matching when stronger identifiers exist.

---

## 32. Application state machine

Application state transitions must be explicit and valid.

Avoid ambiguous combinations such as simultaneously treating the same application as:

- pending;  
- submitted;  
- failed;  
- parked  

without a defined model.

State transitions should support:

- retries;  
- parking;  
- resume;  
- submission;  
- verification;  
- outcomes;  
- intervention;  
- system restart.  

The exact schema belongs in architecture/implementation.

---

## 33. Failure isolation

A job-specific failure should not normally stop unrelated applications.

Workers should isolate:

- job state;  
- browser/session state;  
- artifacts;  
- errors.  

System-wide execution should stop when required by approved safety policy.

Do not convert every exception into a global failure.

Do not allow systemic safety failures to be treated as ordinary job failures.

---

## 34. Retry standard

Retries must be bounded and reason-aware.

Do not retry indefinitely.

Distinguish:

- transient network/browser error;  
- rate limit;  
- authentication failure;  
- validation failure;  
- CAPTCHA/MFA;  
- permanent application error;  
- systemic defect.  

Use backoff where appropriate.

Do not retry actions where duplication could create external consequences without idempotency protection.

---

## 35. Concurrency standard

Concurrent workers must maintain isolation.

No worker may accidentally consume another worker’s:

- job;  
- resume;  
- cover letter;  
- browser state;  
- screening answers;  
- application state;  
- credentials/session identity where isolation is required.  

Concurrency must have deterministic acquisition/locking/state semantics.

Throughput must not compromise correctness.

---

## 36. Database / persistence standard

Persistent data changes must be deliberate.

Once operational data exists:

- use explicit schema evolution/migration practices;  
- preserve historical application evidence;  
- define defaults/nullability;  
- maintain state integrity;  
- test restart/recovery;  
- avoid silent destructive mutation.  

SQLite/WAL may remain if architecture discovery establishes it satisfies requirements.

Do not mandate a database replacement merely because another technology could be used.

---

## 37. Transactional integrity

Where multiple persistent changes collectively represent one consequential operation, use appropriate transactional behavior.

Examples may include:

- acquiring an application for a worker;  
- recording submission state;  
- binding final artifacts;  
- transitioning from parked to resumed;  
- recording owner outcome updates.  

Avoid partial state that falsely represents completion.

---

## 38. Windows compatibility standard

Supported production/development behavior for this deployment must work on the owner’s Windows environment.

New code must not introduce unnecessary Linux-only assumptions.

Use cross-platform mechanisms where practical for:

- paths;  
- home directories;  
- temporary directories;  
- subprocesses;  
- executable discovery;  
- environment variables;  
- process management.  

Do not use `/proc`, bash utilities, Unix-only paths, or Linux-specific browser packages without an explicitly justified platform abstraction/fallback.

---

## 39. Windows path standard

Use platform-aware path handling such as `pathlib` or equivalent appropriate abstractions.

Avoid constructing filesystem paths through hard-coded `/` or Unix home paths when platform-aware handling is required.

Do not assume virtual environments use `bin/`.

Do not assume executables have Unix names/locations.

---

## 40. Subprocess standard

Subprocess execution must account for Windows semantics.

Avoid shell-dependent commands where direct process invocation is practical.

When shell use is unavoidable:

- document why;  
- handle quoting safely;  
- avoid injection;  
- validate Windows behavior.  

Do not construct shell commands from untrusted webpage/job/email content.

---

## 41. Browser runtime standard

Browser automation must use a documented supported runtime for Windows.

For Chrome / Chrome for Testing / Playwright / Patchright / Claude Code browser integration:

- consult current official documentation;  
- use supported versions;  
- verify executable discovery;  
- verify launch behavior;  
- verify session behavior;  
- verify CDP behavior where relied upon.  

Do not preserve inherited Linux browser techniques merely because they currently exist.

---

## 42. External vendor integration standard

For external APIs/SDKs/services:

- use current documented interfaces;  
- handle authentication appropriately;  
- handle documented rate limits/errors;  
- record dependency/version assumptions where material;  
- avoid relying on undocumented behavior when a supported interface exists.  

When undocumented behavior is unavoidable, label and test the assumption.

---

## 43. AI provider abstraction

Where practical, domain logic should not be unnecessarily coupled to a single LLM provider.

Provider-specific behavior should remain behind an appropriate abstraction where the inherited architecture already supports or benefits from it.

Do not require every model to produce identical behavior without validation.

Provider fallback must not silently reduce factual/safety guarantees.

---

## 44. Structured AI output

For consequential machine-consumed LLM results, prefer structured validated output over free-form parsing where practical.

Examples:

- qualification decisions;  
- screening analysis;  
- intent classification;  
- entity resolution;  
- application-question mapping;  
- outcome classification.  

Validate required fields/types before changing consequential product state.

Do not trust malformed model output merely because it is syntactically recoverable.

---

## 45. AI uncertainty

LLM confidence is not authority.

When model reasoning cannot reliably resolve:

- candidate fact;  
- consequential application question;  
- entity identity;  
- policy decision;  

follow the autonomy policy.

Do not tune prompts to force certainty where evidence is missing.

---

## 46. Model / API cost standard

Track material AI/API consumption sufficiently to understand operational cost.

Prefer:

- deterministic pre-filtering;  
- appropriate model tiers;  
- caching of stable analysis where safe;  
- avoiding duplicate processing.  

Do not sacrifice factual integrity, qualification quality, screening quality, or security solely to minimize model cost.

---

## 47. Testing standard

Material production behavior must have appropriate automated coverage.

Testing should include, as applicable:

- unit tests;  
- integration tests;  
- regression tests;  
- state-transition tests;  
- persistence/restart tests;  
- concurrency tests;  
- artifact-binding tests;  
- factual-integrity tests;  
- screening/tailoring tests;  
- browser tests;  
- security-boundary tests.  

Tests should validate behavior/invariants rather than merely implementation details.

---

## 48. Regression test requirement

A verified defect that is reasonably reproducible should normally receive a regression test when practical.

The test should fail for the original defect and pass after the correction.

Do not rely solely on manual memory of past failures.

---

## 49. ATS / screening test corpus

The system should eventually maintain a representative test corpus for qualification and resume screening/tailoring behavior.

The corpus should include cases such as:

- strong fit with terminology mismatch;  
- strong fit with relevant experience buried;  
- preferred qualification absent;  
- genuine mandatory qualification absent;  
- AI sales vs sales engineering ambiguity;  
- equivalent consulting terminology;  
- years-of-experience interpretation;  
- title/function mismatch;  
- legitimate hard eligibility conflict.  

Tests should verify that the system distinguishes:

**candidate-fit problems**  
from  
**resume-presentation problems.**

Do not encode fabricated candidate facts merely to make test cases pass.

---

## 50. Operator Console testing

Natural-language control requires tests for:

- intent classification;  
- entity resolution;  
- ambiguity handling;  
- durable state updates;  
- pause/resume;  
- owner-reported outcomes;  
- application lookup;  
- artifact lookup;  
- policy enforcement;  
- audit events.  

Test ambiguous employer/application scenarios explicitly.

---

## 51. Outcome-learning testing

Learning behavior should be tested to ensure:

- correct outcome/application association;  
- submitted artifact snapshots remain stable;  
- owner-reported provenance is preserved;  
- positive progression is recognized;  
- isolated outcomes do not automatically become universal strategy;  
- learned strategy cannot bypass factual integrity.  

---

## 52. Security testing

Before unattended autonomous operation, test relevant trust boundaries.

Include representative adversarial cases such as:

- job description containing prompt injection;  
- ATS page attempting to instruct agent to reveal local data;  
- page content requesting unrelated file access;  
- malicious email instructions;  
- attempts to cause unrelated shell execution;  
- attempts to expose secrets;  
- cross-job artifact confusion.  

Security testing must validate behavior, not merely inspect prompts.

---

## 53. Real ATS validation

Automated tests alone cannot prove browser automation against real ATS systems.

Use the controlled validation ladder from `ENGINEERING_PROCESS.md`.

Validate representative ATS/application flows incrementally.

Do not require perfect universal ATS coverage before controlled production.

Do not claim support for an ATS solely because its homepage loads.

---

## 54. Test data safety

Tests should not accidentally submit real applications or send real external communications.

Use:

- mocks;  
- fixtures;  
- dry-run behavior;  
- synthetic forms;  
- test accounts/environments where available.  

Real external actions require explicit controlled authorization.

---

## 55. Dependency standard

Dependencies must be:

- justified;  
- maintained sufficiently for intended use;  
- compatible with the supported runtime;  
- reviewed against official documentation;  
- tested after material upgrade.  

Avoid duplicate dependencies providing substantially the same capability without demonstrated need.

---

## 56. Configuration standard

Environment-specific and candidate-specific behavior belongs in configuration/data where appropriate.

Configuration should be:

- validated;  
- documented;  
- explicit;  
- fail-safe where missing values affect consequential behavior.  

Do not silently fall back to dangerous defaults.

---

## 57. Safe defaults

Defaults should favor:

- factual integrity;  
- non-submission when consequential state is unresolved;  
- bounded retries;  
- secure credential handling;  
- failure isolation;  
- explicit uncertainty;  
- preserved historical evidence.  

Safe defaults must not be confused with excessive manual approval.

Routine qualified applications should remain autonomous once required gates are satisfied.

---

## 58. Performance standard

Optimize measured bottlenecks.

Prioritize correctness and safety before throughput.

Parallelism, streaming, caching, and batching may be used when they preserve:

- job isolation;  
- state integrity;  
- artifact integrity;  
- provider limits;  
- submission safety.  

Do not optimize application volume by weakening qualification or validation.

---

## 59. Documentation standard

Material current behavior should be documented after validation.

Documentation must distinguish:

**Current verified behavior**  
from  
**Planned behavior.**

Code comments should explain non-obvious reasoning rather than restating syntax.

Do not leave stale architecture documentation after validated material changes.

---

## 60. Change review standard

Before handoff of consequential code changes:

- inspect diff;  
- inspect Git status;  
- verify intended files only;  
- check for secrets;  
- run proportional tests;  
- report failures;  
- report unvalidated behavior;  
- identify documentation changes.  

Do not call work complete based solely on code generation.

---

## 61. No false success states

Do not represent:

- generated as validated;  
- attempted as submitted;  
- email received as interviewed;  
- model inference as candidate fact;  
- correlation as causation;  
- browser click as application success;  
- parked as failed;  
- failed as rejected;  
- unknown as false.  

State names and UI language must reflect actual evidence.

---

## 62. Critical invariants

At minimum:

1. Candidate facts are never fabricated.  
2. Historical submitted evidence is not silently rewritten.  
3. A resume is never submitted to the wrong job.  
4. A duplicate application is not knowingly submitted to the same requisition.  
5. Browser/email content cannot override governing authority.  
6. Secrets are not exposed to untrusted content.  
7. Unknown consequential facts are not guessed.  
8. Job-specific failures do not unnecessarily stop unrelated work.  
9. Systemic safety failures do stop affected autonomous execution.  
10. Submission is not considered successful without evidence.  
11. Owner-requested pause/system stop survives restart.  
12. Outcome learning does not manufacture causation.  
13. Resume screening optimization never authorizes fabrication.  
14. Ambiguous owner instructions do not modify the wrong application.  
15. Windows is a supported operating environment for this deployment.  

---

## 63. Relationship to other governance documents

| Document | Answers |
|----------|---------|
| `JOB_AGENT_PRODUCT_REQUIREMENTS.md` | What the product must do |
| `AUTONOMY_AND_APPLICATION_POLICY.md` | What the agent is authorized to do |
| `ENGINEERING_METHODOLOGY.md` | How engineering decisions are reasoned about |
| `ENGINEERING_PROCESS.md` | Operational workflow for engineering work |
| `ENGINEERING_STANDARDS.md` | Concrete technical requirements implementation must satisfy |
| `ARCHITECTURE_DISCOVERY_STANDARD.md` | Method for consequential architecture discovery |
| `ARCHITECTURE_CURRENT.md` | Verified current architecture |
| `ENGINEERING_IMPLEMENTATION_PLAN.md` | Ordered roadmap |

Documents other than the four approved companions and this standards document are listed for authority clarity only and are **not** created by this task.

---

## 64. Document status / change control

| Field | Value |
|-------|--------|
| Authority class | Owner-approved engineering standards |
| Status | Approved — Authoritative |
| Authoritativeness | Authoritative |
| Change control | Future material changes must be deliberate and documented |

---

*End of ENGINEERING_STANDARDS.md*  
*Status: Approved — Authoritative.*
