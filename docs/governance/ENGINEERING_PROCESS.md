# Engineering Process

**Document type:** Engineering process / operational workflow  
**Authority class:** Owner-approved engineering process  
**Status:** Approved — Authoritative  
**Scope:** Defines the repeatable operational workflow Cursor/developers must follow when performing engineering work in this repository  
**Does not define:** Product requirements, autonomy/application policy, current architecture inventory, implementation roadmap, coding-style rules, or vendor-specific implementation procedures  

---

## Document control

| Field | Value |
|-------|--------|
| Product | Personal autonomous AI job-search and job-application agent (ApplyPilot fork) |
| Companion authorities | `JOB_AGENT_PRODUCT_REQUIREMENTS.md` (Approved — Authoritative); `AUTONOMY_AND_APPLICATION_POLICY.md` (Approved — Authoritative); `ENGINEERING_METHODOLOGY.md` (Approved — Authoritative) |
| This document answers | **What process do we follow when we actually do engineering work?** |
| Methodology companion | `ENGINEERING_METHODOLOGY.md` defines how we *think* about engineering; this document defines the *sequence* by which that methodology is executed |
| Change control | Future material process changes must be deliberate and documented |

Concrete technical standards belong in `ENGINEERING_STANDARDS.md` (not created by this document).  
Architecture discovery requirements belong in `ARCHITECTURE_DISCOVERY_STANDARD.md` (not created by this document).  
Current verified architecture belongs in `ARCHITECTURE_CURRENT.md` (not created by this document).  
Ordered project work belongs in `ENGINEERING_IMPLEMENTATION_PLAN.md` (not created by this document).

---

## 1. Default engineering workflow

The default lifecycle is:

**Request → Repository state → Governing authority → Current implementation analysis → External documentation check when applicable → Dependency / impact analysis → Proposed approach → Owner approval when required → Implementation → Testing → Runtime / behavioral validation → Documentation → Git review → Stop / handoff.**

Do not collapse analysis and implementation into one uncontrolled step for consequential work.

---

## 2. Phase 0 — Understand the request

Before acting:

- restate internally what outcome is requested;  
- identify whether the request is:  
  - analysis;  
  - architecture/discovery;  
  - implementation;  
  - debugging;  
  - testing;  
  - validation;  
  - documentation;  
  - configuration;  
  - dependency work;  
  - operational execution.  

Determine whether the request authorizes modification.

If the owner requests analysis only:

**Do not modify.**

If the owner requests a plan only:

**Do not implement.**

Do not infer implementation authority from a request to investigate.

---

## 3. Phase 1 — Establish repository state

Before consequential repository work:

1. Identify current branch.  
2. Run `git status`.  
3. Identify existing modified/untracked files.  
4. Distinguish pre-existing owner work from changes related to the current task.  
5. Do not overwrite, discard, reset, stash, or otherwise alter unrelated owner work without explicit authorization.  
6. Confirm the intended scope of files/components.  

If repository state is unexpected, surface it before proceeding when it could create risk.

Never casually use destructive Git commands to obtain a clean tree.

---

## 4. Phase 2 — Identify governing authority

Determine which approved sources govern the task.

At minimum consider:

- `JOB_AGENT_PRODUCT_REQUIREMENTS.md`;  
- `AUTONOMY_AND_APPLICATION_POLICY.md`;  
- `ENGINEERING_METHODOLOGY.md`;  
- `ENGINEERING_PROCESS.md` once approved;  
- `ENGINEERING_STANDARDS.md` once approved;  
- `ARCHITECTURE_CURRENT.md` once approved;  
- `ENGINEERING_IMPLEMENTATION_PLAN.md` once approved;  
- current official vendor documentation where applicable;  
- current code/tests as implementation evidence.  

Identify the requirement, policy, defect, architecture decision, or implementation-plan item that justifies the work.

If the requested change conflicts with an approved governing document:

**Stop** and surface the conflict.

Do not silently modify policy through implementation.

---

## 5. Phase 3 — Analyze current implementation

Before modifying consequential behavior:

- locate relevant code;  
- trace call paths;  
- inspect configuration;  
- inspect persistence/schema where applicable;  
- inspect tests;  
- inspect error handling;  
- inspect adjacent components;  
- inspect Git history when provenance matters;  
- identify current behavior;  
- identify assumptions;  
- identify known failure modes;  
- identify existing abstractions that should be preserved.  

Do not rely only on filenames or documentation summaries.

Read the implementation necessary to understand the behavior being changed.

For a bug, reproduce or establish evidence of the failure where practical before fixing it.

---

## 6. Phase 4 — Official external documentation check

If work involves an external platform, service, API, SDK, framework, browser/runtime, authentication mechanism, or material dependency:

Consult **current official vendor documentation** before making consequential implementation decisions.

This check occurs at the relevant stages:

| Stage | When |
|-------|------|
| **A. Architecture/readiness** | Before locking design assumptions |
| **B. Implementation** | Before coding against vendor behavior |
| **C. Debugging** | When vendor behavior is implicated |
| **D. Validation** | When supported behavior/limits matter |

Examples include:

- Anthropic / Claude / Claude Code;  
- Google Gemini;  
- OpenAI;  
- Gmail / Google APIs;  
- Playwright;  
- Patchright;  
- Chrome / Chrome for Testing;  
- Python libraries;  
- ATS/vendor interfaces or documented behaviors.  

Record material vendor constraints/requirements relevant to the decision.

Do not substitute:

- memory;  
- old blog posts;  
- inherited README statements;  
- stale code comments;  
- prior assumptions  

for current official documentation.

---

## 7. Phase 5 — Dependency, impact, and risk analysis

Before implementation determine:

**What changes?**  
**What depends on it?**  
**What could break?**  
**What must remain unchanged?**  
**What evidence will prove success?**

Consider as applicable:

- callers;  
- downstream consumers;  
- data/schema;  
- candidate facts;  
- resume artifacts;  
- browser workers;  
- sessions;  
- ATS behavior;  
- credentials;  
- email;  
- concurrency;  
- persistence;  
- restart/recovery;  
- security;  
- tests;  
- Windows/runtime compatibility;  
- AI/API cost;  
- logs/observability.  

For consequential cross-cutting changes, use the architecture discovery process rather than performing ad hoc analysis.

---

## 8. Phase 6 — Propose before implementing

For consequential changes, produce a concise proposed approach before editing.

The proposal should identify:

- problem/current behavior;  
- governing requirement;  
- root cause or current architectural limitation where known;  
- proposed change;  
- affected components;  
- preserved behavior;  
- risks;  
- tests/validation;  
- documentation impact.  

Do not present speculative details as facts.

If multiple materially different approaches exist, explain the tradeoff.

Prefer a recommendation rather than forcing the owner to design the technical solution.

---

## 9. Owner approval gate

For consequential implementation, wait for owner approval of the proposed approach unless the owner has explicitly authorized implementation in the original request.

Examples that normally require approval before implementation include:

- architecture changes;  
- security changes;  
- credential handling;  
- new dependencies;  
- schema/state-machine changes;  
- autonomous authority changes;  
- resume truthfulness/validation changes;  
- submission behavior;  
- email authorization;  
- concurrency architecture;  
- Windows/browser runtime architecture;  
- material cost changes;  
- removal/replacement of inherited subsystems.  

Do not ask the owner to decide technical details that engineering can responsibly recommend.

Present the recommendation and obtain approval for the consequential direction.

---

## 10. Implementation branch / change boundary

Before code implementation:

- confirm the intended branch strategy;  
- do not assume work should occur directly on main;  
- create/use the approved feature branch when directed by the implementation plan or owner;  
- verify repository state after branch change;  
- maintain a clear task boundary.  

Do not combine unrelated work into the same implementation change.

---

## 11. Phase 7 — Implement the smallest sound change

Implementation should:

- satisfy the governing requirement;  
- preserve useful inherited behavior;  
- respect approved architecture;  
- respect autonomy policy;  
- maintain security boundaries;  
- avoid unrelated cleanup;  
- avoid speculative features;  
- remain reviewable.  

Do not introduce temporary bypasses that silently become production behavior.

If implementation reveals that the approved approach is materially wrong:

**Stop,**  
report the evidence,  
and revise the approach before continuing.

---

## 12. Phase 8 — Static and automated validation

Run the appropriate existing quality checks for the changed area.

Examples may include:

- targeted tests;  
- full tests where justified;  
- lint;  
- formatting checks;  
- type checks;  
- schema/migration checks;  
- security tests;  
- unit tests;  
- integration tests.  

Do not blindly run every possible test for every trivial documentation change.

Use proportional validation.

Report exactly what was run and the result.

Do not hide skipped/failing tests.

---

## 13. Phase 9 — Runtime / behavioral validation

For behavior that cannot be established by static tests alone, validate the actual runtime behavior.

Examples:

- browser launch;  
- ATS navigation;  
- resume upload;  
- session persistence;  
- submission verification;  
- Gmail tracking;  
- concurrent workers;  
- restart recovery;  
- Windows-specific behavior;  
- Chrome / Chrome for Testing integration.  

Use safe/dry-run/sandbox behavior where available before real consequential actions.

Do not use a real job application merely because a lower-risk validation path was skipped.

---

## 14. Windows baseline readiness gate

This project is being operated on Windows while significant inherited development/hardening occurred on Linux.

Before substantive feature implementation and before any real autonomous application submission, perform a dedicated Windows runtime/readiness assessment.

This assessment must examine, as applicable:

- Python runtime and invocation;  
- virtual environment layout;  
- filesystem/path handling;  
- `~/.applypilot` or equivalent home-directory resolution;  
- temporary-file handling;  
- subprocess invocation and quoting;  
- shell/bash dependencies;  
- executable discovery;  
- Node/npx invocation;  
- Claude Code invocation;  
- Chrome discovery;  
- Chrome for Testing;  
- Playwright/Patchright;  
- browser launch arguments;  
- extension/CDP behavior;  
- process signaling/termination;  
- `/proc` dependencies;  
- Linux-specific commands/utilities;  
- file permissions/executable assumptions;  
- Git hooks;  
- environment-variable loading;  
- persistent browser/session paths;  
- concurrency/process behavior.  

For external runtime/browser behavior, consult current official vendor documentation.

Classify each discovered issue:

- already cross-platform;  
- Windows-compatible as-is;  
- Windows configuration required;  
- code change required;  
- obsolete inherited approach;  
- unknown requiring validation.  

Do **not** assume that Linux-specific implementation is required merely because inherited code uses it.

Prefer currently supported Windows-native behavior where it satisfies requirements.

WSL may be evaluated if technically useful, but do not make WSL mandatory without demonstrated need and owner approval.

---

## 15. Windows baseline validation

Before major functional modifications make failure attribution difficult, establish a known Windows baseline as far as safely practical.

The baseline should determine which inherited capabilities can currently run on Windows and which cannot.

Where safe and appropriate, validate progressively:

1. Python/package environment.  
2. CLI startup.  
3. Configuration loading.  
4. Database access.  
5. Non-AI/local pipeline behavior.  
6. AI provider connectivity only when authorized/configured.  
7. Browser launch.  
8. Browser automation dry-run.  
9. Session handling.  
10. Application dry-run behavior.  

Do **not** submit a real application as part of baseline validation.

Document verified failures rather than immediately attributing every failure to Windows.

The resulting Windows remediation work must be represented explicitly in the implementation plan.

---

## 16. Security gate before real applications

No real autonomous application submission should occur until known critical security/trust-boundary issues relevant to application execution have been remediated or explicitly resolved.

This includes the inherited risks identified during repository audit involving privileged browser/LLM operation, credentials/secrets, untrusted webpage content, and local worker/API exposure.

Security readiness must be validated, not assumed.

A desire to begin applying sooner does not override this gate.

---

## 17. Controlled application validation ladder

When the system reaches application testing, progress through increasing consequence.

Recommended conceptual order:

| Level | Activity |
|-------|----------|
| **1** | Unit/static validation |
| **2** | Local/synthetic form tests where available |
| **3** | Browser dry-run against representative real application workflows without submission |
| **4** | Controlled end-to-end dry-run with correct candidate artifacts and screening logic |
| **5** | One owner-authorized real qualified application |
| **6** | Verify browser/application evidence and expected confirmation behavior |
| **7** | Small controlled batch across representative ATS types |
| **8** | Expanded autonomous operation |
| **9** | Continuous unattended operation after reliability/security gates are met |

Do not jump directly from “browser launches” to continuous mass application.

---

## 18. Real application change control

Real application submission is a consequential external action.

Before the first real application:

- candidate facts must be configured and verified;  
- target-job qualification must be validated;  
- resume tailoring truthfulness must be validated;  
- correct artifact binding must be validated;  
- screening-question policy must be operational;  
- security gate must be satisfied;  
- Windows/browser readiness must be satisfied;  
- submission verification must have a defined operational mechanism;  
- duplicate prevention must be operational;  
- owner must explicitly authorize the first real controlled submission.  

After the controlled validation phase proves the approved autonomous policy is working, routine qualified applications should **not** require individual owner approval.

This preserves the PRD’s maximum-safe-autonomy objective.

---

## 19. Debugging process

When debugging:

1. Capture the observed failure.  
2. Preserve relevant logs/evidence.  
3. Identify the failing layer.  
4. Reproduce where practical.  
5. Distinguish fact from hypothesis.  
6. Check official vendor documentation if vendor behavior is implicated.  
7. Identify root cause.  
8. Propose the smallest sound fix.  
9. Implement after the appropriate approval gate.  
10. Add/adjust regression coverage.  
11. Reproduce the original scenario.  
12. Verify the failure is resolved.  
13. Verify adjacent behavior was not broken.  
14. Document material architectural findings.  

Do not shotgun-edit multiple components hoping the problem disappears.

---

## 20. Security incident process

If engineering discovers evidence of:

- credential leakage;  
- secret exposure;  
- prompt-injection privilege escape;  
- incorrect candidate identity;  
- systemic wrong-artifact submission;  
- systemic fabrication;  
- unauthorized external action;  
- corrupted application state;  
- other system-wide safety failure;  

**Stop** affected autonomous execution.

Preserve evidence.

Do not continue operating merely to reproduce the issue against additional real applications.

Classify whether the issue is:

- local/application-specific;  
- component-specific;  
- system-wide.  

Follow the autonomy policy’s system-wide stop principle.

---

## 21. Dependency change process

Before adding/upgrading/replacing a material dependency:

1. Establish the requirement.  
2. Inspect existing dependency usage.  
3. Consult current official documentation.  
4. Verify supported platform/runtime versions.  
5. Evaluate Windows compatibility.  
6. Evaluate maintenance/security implications.  
7. Determine affected code/tests.  
8. Determine migration/rollback implications.  
9. Obtain approval where consequential.  
10. Implement.  
11. Validate.  
12. Update dependency documentation if material.  

Do not perform broad dependency upgrades merely because newer versions exist.

---

## 22. Schema / persistence change process

Before material persistent-state changes:

- identify current schema/state;  
- identify existing data impact;  
- define migration;  
- define defaults/nullability;  
- define compatibility;  
- define rollback/recovery where appropriate;  
- define state-transition implications;  
- define restart behavior;  
- add validation/tests.  

Persistent state changes must not be treated as ordinary local refactors once real application data exists.

---

## 23. Documentation update process

After validated material changes, determine whether documentation must be updated.

Potential documents include:

- `ARCHITECTURE_CURRENT.md`;  
- `ENGINEERING_IMPLEMENTATION_PLAN.md`;  
- technical runbooks;  
- configuration documentation;  
- `CHANGELOG.md` when appropriate.  

Do not rewrite approved product requirements or autonomy policy merely to match implementation.

If implementation legitimately requires a governance change, surface it separately for owner approval.

Documentation must distinguish verified current behavior from planned behavior.

---

## 24. Git review before handoff

At the end of an implementation task:

1. Run `git status`.  
2. Run an appropriate diff review.  
3. Confirm only intended files changed.  
4. Check for accidental secrets/credentials.  
5. Check for generated/temp files that should not be committed.  
6. Summarize modifications.  
7. Summarize tests/validation.  
8. Identify unresolved issues.  
9. Do not claim clean completion if evidence is incomplete.  

Commit/push only when authorized by the owner or governing implementation workflow.

---

## 25. Handoff / stop point

At the end of each bounded task, report:

- what was requested;  
- what was changed;  
- what was not changed;  
- files affected;  
- validation performed;  
- results;  
- remaining risks/blockers;  
- recommended next action;  
- Git status.  

Then **stop**.

Do not opportunistically begin the next work package without authorization.

---

## 26. Analysis-only task template

For analysis-only requests, the process should be:

**Verify repository state → Read governing documents → Inspect relevant code/tests → Consult official docs if applicable → Report current behavior → Identify risks/gaps → Recommend approach → Do not modify → Stop.**

---

## 27. Implementation task template

For approved implementation:

**Verify branch/status → Read governing requirement → Confirm approved approach → Check official docs → Implement bounded change → Run targeted tests → Run proportional broader validation → Perform runtime validation when needed → Review diff → Update appropriate docs → Report → Stop.**

---

## 28. Bug-fix task template

For debugging:

**Verify state → Establish failure → Trace root cause → Check official docs if relevant → Propose fix → Approval if consequential → Implement → Regression test → Reproduce original failure → Validate adjacent behavior → Report → Stop.**

---

## 29. Documentation-only task template

For documentation work:

**Verify state → Identify authority → Read source material → Create/modify only authorized document → Check for unsupported claims → Review diff → Report → Stop.**

Do not modify code during documentation-only work unless separately authorized.

---

## 30. Proportionality

Not every task requires every process stage at maximum depth.

A typo fix may require only:

- repository state;  
- authority/scope;  
- edit;  
- diff review.  

A browser-security redesign may require:

- architecture discovery;  
- official vendor documentation;  
- threat/risk analysis;  
- proposal;  
- approval;  
- implementation;  
- automated tests;  
- adversarial/runtime validation;  
- architecture documentation.  

Apply rigor according to consequence.

Do not use proportionality as justification to skip necessary safety or validation gates.

---

## 31. Process summary

**Understand the request → Verify repository state → Identify authority → Understand current reality → Verify external behavior → Analyze impact/risk → Propose → Approve → Implement → Test → Validate real behavior → Document → Review Git state → Report → Stop.**

---

## 32. Relationship to other governance documents

| Document | Answers |
|----------|---------|
| `JOB_AGENT_PRODUCT_REQUIREMENTS.md` | What the product must do |
| `AUTONOMY_AND_APPLICATION_POLICY.md` | What the autonomous agent is authorized to do |
| `ENGINEERING_METHODOLOGY.md` | How engineering reasoning and decisions are made |
| `ENGINEERING_PROCESS.md` | The operational workflow for performing engineering work |
| `ENGINEERING_STANDARDS.md` | Concrete technical quality/security/testing/coding rules |
| `ARCHITECTURE_DISCOVERY_STANDARD.md` | Required method for consequential architectural discovery |
| `ARCHITECTURE_CURRENT.md` | Verified description of current system architecture |
| `ENGINEERING_IMPLEMENTATION_PLAN.md` | Approved ordered roadmap to reach the product requirements |

Documents other than the three approved companions and this process document are listed for authority clarity only and are **not** created by this task.

---

## 33. Document status / change control

| Field | Value |
|-------|--------|
| Authority class | Owner-approved engineering process |
| Status | Approved — Authoritative |
| Authoritativeness | Authoritative |
| Change control | Future material process changes must be deliberate and documented |

---

*End of ENGINEERING_PROCESS.md*  
*Status: Approved — Authoritative.*
