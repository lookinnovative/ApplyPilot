# Engineering Methodology

**Document type:** Engineering methodology  
**Authority class:** Owner-approved engineering methodology  
**Status:** Approved — Authoritative  
**Scope:** Defines the permanent engineering philosophy used to reason about, design, modify, debug, validate, and evolve this ApplyPilot fork  
**Does not define:** Product requirements, autonomy policy, step-by-step workflow, current architecture inventory, implementation roadmap, coding-style rules, vendor-specific procedures, or historical ApplyPilot decision logs  

---

## Document control

| Field | Value |
|-------|--------|
| Product | Personal autonomous AI job-search and job-application agent (ApplyPilot fork) |
| Companion authorities | `JOB_AGENT_PRODUCT_REQUIREMENTS.md` (Approved — Authoritative); `AUTONOMY_AND_APPLICATION_POLICY.md` (Approved — Authoritative) |
| This document answers | **How do we think about engineering this system?** |
| Change control | Future material changes must be deliberate and documented |

Detailed operational workflow belongs in `ENGINEERING_PROCESS.md` (not created by this document).  
Concrete coding/testing/security rules belong in `ENGINEERING_STANDARDS.md` (not created by this document).  
Current architecture belongs in `ARCHITECTURE_CURRENT.md` (not created by this document).  
The ordered build roadmap belongs in `ENGINEERING_IMPLEMENTATION_PLAN.md` (not created by this document).

---

## 1. Core engineering objective

Engineering exists to implement the approved product requirements and autonomy policy faithfully, safely, maintainably, and with evidence.

The inherited ApplyPilot repository is a valuable implementation starting point.

It is **not** the product authority.

The methodology must preserve useful inherited architecture where appropriate rather than rebuilding working systems unnecessarily.

At the same time, inherited behavior must not be preserved merely because it already exists.

The engineering objective is:

**Understand → Verify → Preserve what is sound → Change what is necessary → Validate → Document the result.**

---

## 2. Authority before implementation

Engineering decisions must begin with the applicable authority.

At the current governance level, distinguish:

1. Applicable legal/license obligations.  
2. Owner-approved product requirements.  
3. Owner-approved autonomy/application policy.  
4. Current official vendor documentation for vendor behavior.  
5. Approved engineering methodology/process/standards once created.  
6. Verified executable code and tests as evidence of current behavior.  
7. Approved current-architecture documentation once created.  
8. Inherited ApplyPilot documentation.  
9. Historical specs/plans.  
10. Jobscan and other external reference/research material.  

Different authorities answer different questions.

Examples:

- **Product requirements** define what the product must accomplish.  
- **Autonomy policy** defines what the agent is authorized to do.  
- **Official vendor documentation** defines current supported vendor behavior.  
- **Code/tests** establish what the inherited/current implementation actually does.  
- **Historical documentation** may explain intent but cannot override verified current behavior or approved requirements.  

When authorities conflict, the conflict must be surfaced and resolved rather than silently choosing whichever source is convenient.

---

## 3. Documentation-first engineering

This project follows documentation-first engineering.

Before consequential implementation:

- determine the governing requirement;  
- determine the applicable autonomy/policy boundary;  
- understand the current architecture;  
- consult current official vendor documentation where external systems are involved;  
- identify affected components and dependencies;  
- define intended behavior;  
- define validation evidence;  
- then implement.  

Documentation-first does **not** mean writing speculative documentation instead of examining code.

It means architecture and implementation decisions should be grounded before changes are made.

---

## 4. Official vendor documentation is authoritative for vendor behavior

For every external platform, API, SDK, framework, browser technology, ATS integration mechanism, authentication mechanism, or other material external dependency:

Current official vendor documentation must be consulted at the relevant architecture, implementation, debugging, and validation gates.

Examples may include:

- Anthropic / Claude / Claude Code;  
- Google Gemini;  
- OpenAI;  
- Gmail / Google APIs;  
- Playwright;  
- Patchright;  
- Chrome / Chrome for Testing;  
- Python libraries;  
- ATS/vendor APIs or documented platform behavior where applicable.  

Do not rely solely on:

- inherited code;  
- README statements;  
- historical implementation plans;  
- old blog posts;  
- remembered behavior;  
- assumptions from prior versions.  

Existing code tells us what the repository currently attempts.

Official documentation tells us what the vendor currently supports.

If current official documentation and inherited implementation disagree, investigate before changing or operating the system.

---

## 5. Analysis before modification

Do not begin consequential work by immediately editing code.

First establish:

- current Git/repository state;  
- relevant requirement;  
- relevant policy;  
- affected architecture;  
- current implementation behavior;  
- dependencies;  
- tests;  
- known risks;  
- expected result.  

For unfamiliar or cross-cutting areas, perform architecture discovery before implementation.

The amount of discovery should be proportional to the risk and scope of the change.

Avoid both extremes:

- modifying first and understanding later;  
- performing endless analysis for a trivial isolated change.  

---

## 6. Root-cause engineering

When something fails, diagnose the underlying cause before applying a fix.

Do not normalize:

- symptom patches;  
- arbitrary retries;  
- sleeps added without evidence;  
- broad exception swallowing;  
- disabling validation;  
- weakening security;  
- bypassing safeguards;  
- hard-coded special cases without architectural justification;  
- changing thresholds merely to make a test pass.  

Debugging should establish:

**Observed failure → Evidence → Root cause → Smallest sound correction → Regression validation.**

If the root cause cannot yet be established, state that explicitly.

Do not present a hypothesis as a verified diagnosis.

---

## 7. Preserve before replace

This is an inherited mature codebase with useful existing capability.

Prefer:

- understanding existing abstractions;  
- reusing sound components;  
- extending appropriate boundaries;  
- correcting isolated weaknesses;  
- preserving proven behavior.  

Do not rewrite subsystems simply because a different design appears cleaner.

Replacement should require a demonstrated reason such as:

- inability to satisfy approved requirements;  
- unsafe architecture;  
- obsolete/unsupported dependency;  
- unmaintainable coupling;  
- repeated reliability failure;  
- fundamentally incorrect abstraction.  

When replacing something, identify what useful behavior must be preserved.

---

## 8. Minimum necessary change

Prefer the smallest change that correctly satisfies the requirement and preserves architectural integrity.

This does **not** mean:

- patch around the problem;  
- avoid necessary refactoring;  
- preserve bad architecture indefinitely.  

It means:

Do not broaden scope without reason.

Avoid unrelated cleanup during focused implementation unless the cleanup is necessary to make the change safe or correct.

Keep changes reviewable and attributable to a defined requirement or defect.

---

## 9. Requirement traceability

Material engineering work should be traceable to:

- an approved product requirement;  
- an approved autonomy/policy requirement;  
- a verified defect;  
- a security requirement;  
- an approved architecture decision;  
- an implementation-plan item.  

Avoid features created simply because they are technically interesting.

For significant changes, it should be possible to answer:

**Why does this exist?**

and point to the governing requirement or verified problem.

---

## 10. Facts, inferences, hypotheses, and unknowns

Engineering analysis must distinguish:

| Label | Meaning |
|-------|---------|
| **FACT** | Directly established through code, tests, runtime evidence, repository state, or authoritative documentation |
| **INFERENCE** | Reasoned interpretation supported by evidence but not directly established |
| **HYPOTHESIS** | Plausible explanation requiring validation |
| **UNKNOWN** | Insufficient evidence |

Do not collapse these categories.

This is especially important when working with:

- browser automation;  
- ATS behavior;  
- AI model behavior;  
- anti-bot behavior;  
- email correlation;  
- external services;  
- undocumented employer application behavior.  

---

## 11. Evidence-based validation

A change is not complete because:

- code compiles;  
- a command returned zero;  
- an LLM says it looks correct;  
- a browser clicked a button;  
- a developer believes it should work.  

Validation must correspond to the behavior being changed.

Examples:

- resume tailoring requires artifact/factual validation;  
- submission requires submission evidence;  
- browser changes require browser/runtime validation;  
- concurrency changes require isolation/concurrency validation;  
- security changes require boundary/adversarial validation;  
- ATS-specific fixes require representative ATS validation;  
- persistence changes require restart/recovery validation.  

Use the strongest practical evidence available.

---

## 12. Tests as engineering evidence

Automated tests are evidence, not ceremony.

Tests should protect:

- requirements;  
- regressions;  
- critical invariants;  
- safety boundaries;  
- state transitions;  
- failure isolation.  

Do not write tests that merely reproduce implementation details without validating meaningful behavior.

A failing legitimate test is evidence to investigate.

Do not weaken a valid test merely because the implementation does not pass it.

Likewise, passing tests do not prove behavior outside what those tests actually exercise.

---

## 13. Security by design

Security is architectural for this product because an AI-controlled browser processes untrusted internet content while handling applicant data and credentials.

Security must not be bolted on after autonomous operation is enabled.

Engineering must maintain explicit trust boundaries among:

- governing instructions;  
- candidate facts;  
- LLM reasoning;  
- browser/page content;  
- email content;  
- credentials/secrets;  
- local filesystem;  
- subprocess/tool authority;  
- external services.  

Untrusted content is data, not authority.

Privilege should be minimized.

Secrets should be exposed only where necessary.

A security control must not be weakened merely to increase application completion rate.

---

## 14. Safe autonomy over manual workarounds

The product objective is autonomous operation.

When the system cannot perform a routine action autonomously, engineering should determine whether the problem represents:

- missing reusable knowledge;  
- missing generalized capability;  
- ATS-specific reliability issue;  
- authentication/session issue;  
- security limitation;  
- genuine need for human judgment.  

Do not normalize manual workarounds for problems that should be solved architecturally.

At the same time, do not automate a decision that legitimately requires human authority merely to reduce HITL frequency.

---

## 15. General capability before brittle special cases

Prefer generalized capabilities where the problem is fundamentally general.

For example:

- semantic form understanding;  
- authoritative candidate-fact mapping;  
- generalized artifact binding;  
- generalized submission verification;  
- generalized failure isolation.  

Use ATS/site-specific handling when it materially improves reliability or handles genuinely platform-specific behavior.

Avoid an architecture that requires bespoke hard-coded automation for every employer.

But do not force a generalized abstraction where platform-specific behavior demonstrably requires specialized handling.

---

## 16. Failure is information

Failures encountered during controlled operation are engineering evidence.

A failed application should produce enough information to determine:

- what failed;  
- where it failed;  
- why it failed if known;  
- whether it is job-specific;  
- ATS-specific;  
- systemic;  
- security-related;  
- transient;  
- reproducible.  

Do not hide failure merely to improve apparent success metrics.

Failure classification should help improve the system.

---

## 17. Observability before unattended operation

A continuously autonomous system must be observable.

Before relying on unattended behavior, engineering should ensure sufficient telemetry exists to determine:

- what the agent is doing;  
- which job/application is active;  
- what state it is in;  
- what artifacts it used;  
- why it made consequential decisions;  
- whether it succeeded;  
- whether it parked;  
- whether it failed;  
- whether a system-wide stop condition occurred.  

Do not build autonomy that cannot be reconstructed after the fact.

---

## 18. Idempotency and durable state

Continuous operation requires protection against duplicate and inconsistent actions.

Where consequential operations occur, engineering should consider:

- durable state;  
- idempotency;  
- duplicate prevention;  
- restart recovery;  
- retry semantics;  
- transaction boundaries;  
- worker isolation.  

This is especially important for:

- application submission;  
- account creation;  
- screening answers;  
- artifact generation;  
- email correlation;  
- state transitions.  

---

## 19. Concurrency requires isolation

Parallelism is valuable only when jobs cannot contaminate one another.

Concurrent workers must preserve correct association among:

**Job → Job description → Candidate context → Tailored resume → Cover letter → Screening answers → Browser session → Application result.**

Cross-job artifact or state contamination is a critical defect.

Concurrency improvements must not trade correctness for throughput.

---

## 20. Cost-aware, not cost-dominated

AI/API/browser-agent cost matters and should be observable.

Prefer:

- deterministic filtering before expensive AI;  
- appropriate model selection;  
- caching/reuse where safe;  
- avoiding unnecessary repeated calls;  
- avoiding expensive processing for jobs already known to be unsuitable.  

However, cost optimization must not weaken:

- qualification quality;  
- factual integrity;  
- security;  
- submission verification;  
- required application quality.  

Optimize measured bottlenecks rather than prematurely degrading quality to save hypothetical cost.

---

## 21. Configuration over personal hard-coding

Candidate-specific facts and preferences should live in appropriate configuration/data structures rather than source code.

Do not hard-code into reusable architecture:

- candidate identity;  
- target geography;  
- compensation;  
- target roles;  
- personal exclusions;  
- relocation preferences;  
- travel preferences;  
- demographic answers;  
- employer preferences;  
- arbitrary inherited developer rules.  

Architecture should remain reusable even though this deployment is for one owner’s personal job search.

---

## 22. Cross-platform engineering

The current operating environment is Windows, while substantial inherited development occurred on Linux.

Do not assume Unix-specific behavior.

When implementing or modifying:

- paths;  
- subprocesses;  
- browser discovery;  
- Chrome / Chrome for Testing;  
- virtual environments;  
- temporary directories;  
- process signaling;  
- scripts;  
- Git hooks;  
- environment-variable loading;  

explicitly account for the supported runtime environment.

Where practical, preserve cross-platform behavior rather than replacing one platform assumption with another.

---

## 23. Dependency discipline

Do not add, replace, or upgrade dependencies casually.

Before a material dependency change:

- establish the requirement;  
- inspect existing dependency use;  
- consult current official documentation;  
- determine compatibility;  
- understand security/maintenance implications;  
- identify migration impact;  
- identify validation requirements.  

Prefer existing sound dependencies when they satisfy the requirement.

Avoid introducing overlapping libraries without a demonstrated need.

---

## 24. Data and schema discipline

Persistent application/job state is product-critical.

Schema changes must consider:

- existing data;  
- migrations;  
- backwards compatibility where appropriate;  
- defaults;  
- nullable/required behavior;  
- restart behavior;  
- state-machine semantics;  
- auditability.  

Do not use silent schema mutation as a substitute for deliberate migration strategy when the system reaches operational use.

---

## 25. No silent policy changes through code

Implementation must not silently change product or autonomy policy.

Examples:

- changing a qualification threshold that materially changes which jobs are eligible;  
- allowing previously escalated questions to auto-answer;  
- changing what constitutes verified submission;  
- granting new browser/system authority;  
- changing financial authority;  
- weakening factual validation;  
- enabling new outbound communications.  

If implementation exposes a need to change governing policy, stop and surface the decision.

Update policy only through explicit owner-approved governance change.

---

## 26. Documentation must follow verified reality

Documentation should describe verified architecture and behavior.

Do not document intended behavior as though it already exists.

Clearly distinguish:

- current implementation;  
- planned implementation;  
- requirement;  
- historical behavior.  

After a material architecture change is validated, update the appropriate current architecture/engineering documentation so future work does not rely on stale assumptions.

---

## 27. No false completion

Do not report work as complete when:

- required validation was not performed;  
- runtime behavior was not tested where necessary;  
- a known blocker remains;  
- only part of the requirement was implemented;  
- tests were skipped without disclosure;  
- external behavior remains unverified.  

Report exactly what is:

- implemented;  
- validated;  
- partially validated;  
- unvalidated;  
- blocked.  

---

## 28. Proportional engineering

Use rigor proportional to consequence.

Examples:

A documentation typo does not require architecture discovery.

A change to resume truthfulness, browser privileges, credential handling, submission state, concurrency, or autonomous decision authority does.

Avoid bureaucracy for trivial changes.

Avoid casual changes to high-consequence systems.

---

## 29. Continuous improvement from real operation

Controlled real-world operation should feed engineering improvement.

When the agent encounters:

- a new ATS;  
- a new screening-question type;  
- a failure mode;  
- a new verification signal;  
- a recurring manual intervention;  
- an unexpected employer workflow;  

capture the evidence.

Then determine whether it should become:

- reusable knowledge;  
- generalized capability;  
- ATS-specific handling;  
- test coverage;  
- policy clarification;  
- architecture improvement.  

Do not automatically turn every exception into a permanent special case.

---

## 30. Methodology summary

**Authoritative requirement → Current reality → Official external behavior → Risk / dependency analysis → Smallest sound design → Implementation → Proportional validation → Document verified result → Learn from operation.**

---

## 31. Relationship to other governance documents

| Document | Answers |
|----------|---------|
| `JOB_AGENT_PRODUCT_REQUIREMENTS.md` | What the product must do |
| `AUTONOMY_AND_APPLICATION_POLICY.md` | What the autonomous agent is allowed to do |
| `ENGINEERING_METHODOLOGY.md` | How engineering reasoning and decision-making are performed |
| `ENGINEERING_PROCESS.md` | The operational sequence Cursor/developers follow while doing work |
| `ENGINEERING_STANDARDS.md` | Concrete technical quality/security/testing/coding standards |
| `ARCHITECTURE_DISCOVERY_STANDARD.md` | Required discovery method for consequential architectural work |
| `ARCHITECTURE_CURRENT.md` | Verified description of the system as it currently exists |
| `ENGINEERING_IMPLEMENTATION_PLAN.md` | Approved ordered roadmap for reaching the product requirements |

Documents other than the PRD, autonomy policy, and this methodology are listed for authority clarity only and are **not** created by this task.

---

## 32. Document status / change control

| Field | Value |
|-------|--------|
| Authority class | Owner-approved engineering methodology |
| Status | Approved — Authoritative |
| Authoritativeness | Authoritative |
| Change control | Future material changes must be deliberate and documented |

---

*End of ENGINEERING_METHODOLOGY.md*  
*Status: Approved — Authoritative.*
