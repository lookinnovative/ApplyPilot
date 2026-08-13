# Job Agent Product Requirements

**Document type:** Product Requirements Document (PRD)  
**Authority class:** Owner-approved product requirements  
**Status:** Approved — Authoritative  
**Scope:** Defines *what* the ApplyPilot fork must ultimately do and what constitutes product success  
**Does not define:** Implementation plans, architecture, engineering process, coding standards, vendor documentation summaries, or inherited ApplyPilot behavior as product truth  

---

## Document control

| Field | Value |
|-------|--------|
| Product | Personal autonomous AI job-search and job-application agent (ApplyPilot fork) |
| Classification | OWNER-APPROVED PRODUCT REQUIREMENTS — Approved — Authoritative |
| Relationship to code | Current ApplyPilot implementation is evidence of the starting point, not the definition of the product |
| Conflict rule | Where current implementation differs from these requirements, the requirement wins unless explicitly revised by the owner later |
| Change control | Future material changes to product requirements must be deliberate and documented |
| Amendments | **2026-08-13** — Owner-approved product clarification: ATS Screening & Resume Optimization Intelligence (Gate 2 affirmative objective; pre-/post-tailor screening analysis; distinguish candidate fit from resume presentation; screening risk alone is not automatic disqualification). Status remains Approved — Authoritative. <br><br> **2026-08-13** — Owner-approved product clarification: Operator Console & Natural-Language Agent Control (owner-facing conversational operating interface; structured durable state as system of record; owner-reported offline outcomes; multi-source outcome evidence; application progression model; outcome-driven learning from exact submitted resume/JD pairs without fabricating causation). Status remains Approved — Authoritative. |

This document must **not** become an implementation plan, architecture specification, engineering-process document, coding-standard document, vendor-documentation summary, a copy of the inherited ApplyPilot README, a copy of Jobscan methodology, or a description limited by what the inherited code currently supports.

Do not invent implementation decisions in order to satisfy a product requirement.

---

## 1. Product mission

The product is a **personal autonomous AI job-search and job-application agent**.

Its eventual closed-loop mission is:

1. Continuously discover jobs  
2. Retrieve sufficiently complete job descriptions  
3. Determine genuine candidate/job fit  
4. Reject unsuitable jobs  
5. Prioritize strong matches  
6. Analyze observable screening requirements against verified candidate facts  
7. Truthfully tailor the resume for screening alignment and human review  
8. Re-evaluate and validate the tailored resume (including post-tailor screening analysis)  
9. Generate a cover letter when appropriate or required  
10. Navigate the employer’s actual application process  
11. Create/login to applicant accounts when appropriate  
12. Answer screening questions  
13. Submit the application  
14. Independently verify submission  
15. Monitor application-related email and other authorized outcome signals  
16. Accept owner-reported offline outcomes through the Operator Console  
17. Classify employer responses and application progression  
18. Update application state  
19. Learn from outcome evidence without fabricating causation  
20. Allow the owner to query, instruct, and control the agent through the Operator Console  
21. Replenish the pipeline  
22. Continue  

Routine human involvement should be minimal.

Normal day-to-day operation should occur through the **Operator Console / Natural-Language Agent Interface** (§18), not through engineering tools.

### 1.1 What the product is not

The system is **not** intended to be primarily:

- a job-search coach;
- a resume-writing assistant requiring manual operation;
- a dashboard requiring individual approval of every job;
- a browser macro;
- an indiscriminate mass-application bot;
- a product the owner must operate via Cursor, Claude Code, CLI, source-code editing, or direct database tools for routine use.  

---

## 2. Target-job intelligence

A central product requirement is accurately distinguishing genuinely desirable roles from superficially similar roles.

### 2.1 Target category (positive)

The target category includes work such as:

- AI Sales Consulting  
- AI Solutions Consulting  
- AI Business Consulting  
- AI Transformation  
- AI Enablement  
- consultative AI solution selling  
- AI adoption/advisory work  
- client discovery  
- business requirements discovery  
- AI use-case identification  
- executive/client workshops  
- stakeholder engagement  
- translating AI capabilities into business outcomes  
- business transformation involving AI  
- client-facing AI solution development  
- pre-sales work when predominantly consultative rather than engineering-heavy  

### 2.2 Negative category (must distinguish)

The system must distinguish the target category from roles whose **substantive responsibilities** center on:

- AI Sales Engineering  
- Solutions Engineering  
- AI Engineering  
- ML Engineering  
- production coding  
- production Python development  
- model development  
- data engineering  
- production pipelines  
- infrastructure ownership  
- cloud implementation  
- SDK/API implementation  
- deployment engineering  
- hands-on technical implementation as the principal job function  

### 2.3 Evaluation rules

- Job title alone is insufficient.  
- The agent must evaluate the substantive responsibilities and requirements contained in the job description.  
- A role must **not** be rejected merely because a title contains a word such as “Sales,” “Solutions,” “Consultant,” or “Engineer.”  
- Likewise, a role must **not** qualify merely because its title contains “AI.”  

### 2.4 Known-good exemplars

The product must support one or more owner-approved real job descriptions as known-good job exemplars / reference profiles.

Those exemplars should help the system understand what a genuinely strong target opportunity looks like semantically.

The owner should be able to designate positive and negative targeting examples conversationally through the Operator Console (§18.10), with durable structured targeting evidence when appropriate.

---

## 3. Authoritative candidate facts

The system must maintain an authoritative source of verified candidate facts.

This can include, as appropriate:

- identity/contact information;  
- employment history;  
- actual historical job titles;  
- dates;  
- responsibilities;  
- accomplishments;  
- skills;  
- education;  
- certifications;  
- location;  
- work authorization;  
- sponsorship requirements;  
- travel preferences;  
- relocation preferences;  
- compensation rules;  
- approved screening-question answers;  
- other reusable applicant facts.  

### 3.1 Governing principle

The agent may select, reorder, emphasize, summarize, and truthfully rephrase verified experience.

The agent may **never** fabricate applicant facts.

This prohibition includes inventing or materially falsifying:

- employers;  
- historical job titles;  
- dates;  
- responsibilities;  
- skills;  
- certifications;  
- education;  
- accomplishments;  
- metrics;  
- compensation history;  
- work authorization;  
- eligibility answers;  
- or other candidate facts.  

---

## 4. Job discovery

The product must support continuous discovery of relevant opportunities from multiple sources.

Discovery must not depend exclusively on a manually maintained list of employers.

The product should be capable of discovering opportunities from:

- job-search sources;  
- employer career sites;  
- ATS-hosted postings;  
- other approved discovery sources.  

The product must:

- normalize discovered jobs;  
- deduplicate equivalent postings where practical;  
- associate jobs with their actual employer/application destination;  
- retrieve sufficiently complete job-description content before final qualification;  
- recognize when an opportunity is no longer accepting applications where practical;  
- distinguish freshness from actual availability.  

Job age may influence priority but should **not** automatically eliminate an otherwise excellent opportunity solely because it exceeds an arbitrary inherited age threshold if the position remains open.

---

## 5. Job qualification and prioritization

The agent must determine genuine candidate/job fit before expensive tailoring/application work occurs.

Qualification must support:

- positive fit criteria;  
- negative fit criteria;  
- hard exclusions;  
- preferences;  
- semantic analysis of job responsibilities;  
- candidate factual alignment;  
- known-good job exemplars;  
- owner-defined constraints.  

The system must **not** inherit another developer’s score threshold, geography, company cap, target-role assumptions, or search strategy as product requirements.

Qualification should prioritize precision over indiscriminate application volume.

### 5.1 Candidate fit versus resume presentation

Qualification and resume screening optimization answer different questions:

| Question | Meaning |
|----------|---------|
| **Candidate fit** | Do the authoritative candidate facts support this opportunity? |
| **Resume presentation / screening alignment** | Is that support presented in the strongest truthful way for this particular opportunity? |

Do **not** allow weak base-resume wording to masquerade as lack of candidate qualification.

This distinction is particularly important for semantically related experience that may be described differently across employers.

Only a genuine qualification/eligibility conflict or other approved qualification rule should disqualify the opportunity.

Poor initial resume expression is a **tailoring / screening-alignment problem**, not automatically a candidate-fit failure.

See **§9 ATS Screening & Resume Optimization Intelligence**.

---

## 6. Three-gate optimization

Every application should be prepared to perform effectively across three gates simultaneously.

### 6.1 Gate 1 — Knockout / eligibility screening

The system must truthfully handle application questions involving matters such as:

- work authorization;  
- sponsorship;  
- geography;  
- relocation;  
- travel;  
- compensation;  
- years of experience;  
- certifications;  
- required experience;  
- employer-specific eligibility requirements.  

### 6.2 Gate 2 — ATS / automated / algorithmic screening

Gate 2 has an **affirmative** objective:

**Maximize truthful passage through automated screening/ranking so that a genuinely qualified application has the best practical opportunity to reach human review.**

When the candidate’s verified experience truthfully supports the opportunity, the system should actively tailor the resume to maximize its ability to pass legitimate automated/ATS screening and reach human review.

This remains subject to absolute factual-integrity requirements. The system must **never** fabricate a qualification merely to pass automated screening.

ATS / automated screening optimization is therefore **not** limited to:

- file parsing;  
- formatting;  
- keywords;  
- document readability;  
- detecting potential automated-screening problems;  
- identifying likely knockouts;  
- or rejecting an otherwise strong-fit opportunity because the base resume may not initially present the candidate in the terminology or structure most favorable to automated screening.  

It includes identifying how the employer/job appears to evaluate candidates from **observable** evidence and ensuring that the candidate’s **real** relevant qualifications are sufficiently explicit in the submitted resume.

Application materials should:

- parse reliably;  
- align semantically with the job description;  
- contain relevant terminology where truthful;  
- emphasize the most relevant legitimate experience;  
- make required experience explicit rather than merely implied where the candidate facts support it;  
- avoid harmful keyword stuffing;  
- avoid formatting that materially damages machine parsing;  
- never fabricate qualifications to improve automated matching.  

The architecture must not assume that an ATS vendor’s published description of its own product completely describes every automated screening, ranking, filtering, or employer-configured decision that may occur before human review.

Detailed capability requirements are in **§9 ATS Screening & Resume Optimization Intelligence**.

### 6.3 Gate 3 — Human review

Application materials must remain:

- credible;  
- natural;  
- professionally written;  
- internally consistent;  
- visually professional;  
- persuasive;  
- factually defensible.  

### 6.4 Optimize the three gates together

The resume/application should simultaneously address:

| Gate | Affirmative objective |
|------|------------------------|
| **Gate 1 — Knockout / eligibility** | Truthfully satisfy factual eligibility questions where the candidate qualifies |
| **Gate 2 — ATS / automated / algorithmic screening** | Present the candidate’s legitimate qualifications so they have the strongest practical opportunity to survive automated screening/ranking and reach human review |
| **Gate 3 — Human review** | Remain credible, persuasive, natural, professionally formatted, internally consistent, and factually defensible |

Optimization for Gate 2 must not damage Gate 3.

Human readability must not be used as an excuse to ignore Gate 2.

**Truthfulness governs all three gates.**

---

## 7. Resume tailoring

The system must create a genuinely job-specific resume from verified candidate facts.

Tailoring is the primary mechanism for remediating **supported but underrepresented**, **terminology-misaligned**, or **buried** qualifications identified by screening analysis (§9).

It may:

- select the most relevant legitimate experience;  
- reorder emphasis;  
- rephrase truthful experience;  
- surface relevant skills;  
- use appropriate terminology from the job description;  
- translate equivalent candidate experience into terminology aligned with the employer’s language where truthful;  
- tailor the professional summary;  
- tailor emphasis to the specific opportunity;  
- emphasize relevant responsibilities and accomplishments;  
- improve semantic alignment;  
- make required experience explicit rather than merely implied where factually supported;  
- ensure important legitimate qualifications are machine-detectable and human-readable;  
- increase appropriate prominence of verified supporting evidence.  

It must **not** alter historical truth merely to increase matching.

It must **not**:

- invent experience;  
- invent skills;  
- invent accomplishments;  
- invent metrics;  
- invent employers;  
- invent education;  
- invent certifications;  
- invent licenses;  
- invent years of experience;  
- change historical employment titles into false target titles;  
- falsely claim a requirement is satisfied.  

In particular, an actual historical employment title must **not** be changed into the target job title if that was not the candidate’s real title.

If appropriate, the resume may separately identify a target role without misrepresenting employment history.

The system should preserve an approved professional resume format unless a validated application/ATS requirement requires a different safe representation.

---

## 8. Resume validation

A tailored resume must pass validation before submission.

Validation requirements should include, at the product level:

- factual integrity;  
- consistency with authoritative candidate facts;  
- job-description alignment;  
- screening-oriented validation (whether important supported qualifications identified during screening analysis remain insufficiently represented);  
- document integrity;  
- machine/ATS readability;  
- successful extraction/parsing where applicable;  
- human readability;  
- professional presentation;  
- absence of factual overstatement or fabrication introduced by tailoring.  

A resume that fails a required validation gate must not be submitted automatically.

If a legitimate screening weakness remains and can be corrected using verified candidate facts, the resume should be eligible for another controlled tailoring pass before submission.

Jobscan numeric thresholds are **not** hard-coded into these product requirements unless explicitly approved later.

Any future measurable ATS/screening score thresholds should be established only after baseline testing/evidence and owner approval.

---

## 9. ATS Screening & Resume Optimization Intelligence

This is a first-class product capability governing Gate 2 and the resume preparation loop.

### 9.1 Affirmative Gate 2 objective

When the candidate’s verified experience truthfully supports the opportunity, the system should actively tailor the resume to maximize its ability to pass legitimate automated/ATS screening and reach human review.

The product objective is **not** merely to make the resume ATS-readable, detect screening problems, identify knockouts, or reject an otherwise strong-fit opportunity because the base resume is initially poorly aligned with observable screening criteria.

Fabrication remains prohibited under all circumstances.

### 9.2 Conceptual preparation loop

**Job / observable screening requirements → Base resume + authoritative candidate facts → Gap analysis → Truthful tailoring → Tailored resume → Post-tailor screening analysis → Validation → Application.**

Required sequence for qualified opportunities progressing to application:

**Pre-tailor screening analysis → Truthful resume optimization → Post-tailor screening analysis.**

### 9.3 Pre-tailor screening analysis

Before final resume tailoring, the system should analyze the actual job description and other legitimate available application information for observable screening dimensions.

These may include:

- required skills;  
- preferred skills;  
- responsibilities;  
- experience areas;  
- role/function alignment;  
- seniority;  
- industry/domain terminology;  
- AI terminology;  
- sales/consulting terminology;  
- years-of-experience requirements;  
- education;  
- certifications;  
- licenses;  
- location;  
- work authorization;  
- sponsorship;  
- travel;  
- onsite/hybrid/remote requirements;  
- other material candidate-selection signals.  

The purpose is **not** to invent hidden ATS rules.

The purpose is to determine what observable qualifications and concepts are likely to matter to screening and whether the candidate’s truthful evidence is being presented effectively.

### 9.4 Candidate-evidence mapping

The system should compare those screening dimensions against authoritative candidate facts and the current/base resume.

At the product level, distinguish conditions such as:

| Condition | Meaning |
|-----------|---------|
| **Supported and already well represented** | Candidate has verified supporting experience and the resume expresses it clearly |
| **Supported but underrepresented** | Candidate has verified supporting experience, but it is not sufficiently visible/emphasized |
| **Supported using different terminology** | Candidate has verified equivalent/relevant experience, but the resume expresses it using terminology materially different from the job description |
| **Supported but buried** | Candidate has verified relevant experience, but its location/emphasis may cause automated or human screening to miss its importance |
| **Not supported** | Candidate facts do not establish the qualification |
| **True factual / eligibility conflict** | A mandatory requirement conflicts with authoritative candidate facts and cannot truthfully be corrected through resume tailoring |

### 9.5 Do not turn screening risk into automatic disqualification

If the candidate genuinely has relevant qualifying experience but the base resume does not present it effectively for the specific job:

**Do not** reject the opportunity merely because the initial resume appears weak against the screening criteria.

Instead:

**Identify the presentation gap → Find verified supporting candidate evidence → Tailor the resume truthfully → Re-evaluate the tailored resume.**

Only a genuine qualification/eligibility conflict or other approved qualification rule should disqualify the opportunity.

Poor initial resume expression is a tailoring problem, not automatically a candidate-fit failure.

### 9.6 Post-tailor screening analysis

After the resume is tailored, the system should perform another screening-oriented evaluation before submission.

The post-tailor analysis should ask:

- Are important truthful qualifications now explicit?  
- Are relevant job-description concepts represented where factually supported?  
- Is critical experience still merely implied when it can truthfully be made explicit?  
- Are important supported qualifications buried?  
- Is terminology unnecessarily misaligned with the employer’s terminology?  
- Does the document remain credible to a human reviewer?  
- Has any tailoring introduced factual overstatement or fabrication?  
- Does the document remain machine-readable?  

If a legitimate screening weakness remains and can be corrected using verified candidate facts, the resume should be eligible for another controlled tailoring pass before submission.

### 9.7 Observable screening signals versus unknown proprietary algorithms

The product must not claim knowledge of an employer’s proprietary screening algorithm when that information is unavailable.

Distinguish:

| Category | Examples |
|----------|----------|
| **Observable evidence** | Job description; required/preferred qualifications; application questions; employer-provided requirements; ATS form structure; actual screening questions encountered; legitimate application behavior; later observed application outcomes |
| **Unknown / proprietary behavior** | Hidden ranking weights; undisclosed employer filters; proprietary ATS scoring algorithms; undocumented screening rules |

The system may reason about screening risk from evidence.

It must not present speculation about hidden algorithms as established fact.

Product terminology should prefer: ATS Screening & Resume Optimization Intelligence; automated screening; screening risk; screening alignment; screening optimization; observable screening signals.

Do not make “ATS bias” the formal technical name of the capability. The owner may colloquially refer to the problem as ATS bias, but product documentation must distinguish measurable screening behavior from unverified claims about hidden algorithms.

### 9.8 Application-form screening intelligence

Screening intelligence must not stop at the job description.

During application execution, the agent may encounter additional employer screening questions or requirements that reveal candidate-selection criteria not apparent in the original posting.

Where appropriate, those signals should:

- be evaluated against authoritative candidate facts;  
- inform the current application;  
- be recorded for auditability;  
- inform future screening/tailoring intelligence where legitimately reusable.  

The agent must still comply with `AUTONOMY_AND_APPLICATION_POLICY.md`:

Unknown factual answers must not be fabricated.

### 9.9 Outcome-based screening intelligence

Establish a future product requirement to learn from application outcomes without falsely claiming causation.

Across sufficient application history, the system should eventually be capable of identifying patterns such as:

- unusually rapid rejection;  
- repeated rejection among otherwise high-fit applications;  
- differences in outcomes across resume presentation strategies;  
- recurring screening questions;  
- recurring qualification terminology;  
- ATS/employer-specific patterns;  
- other potentially meaningful screening signals.  

The system may surface these as:

- **Observed pattern**, or  
- **Possible screening factor**  

when supported by evidence.

It must **not** automatically conclude “ATS bias caused this rejection” without evidence sufficient to establish that conclusion.

Observed correlation is not proof of causation.

The purpose of outcome learning is to improve truthful qualification, tailoring, and screening strategy over time.

Outcome-driven learning from exact submitted resume/JD pairs and multi-source progression evidence is specified further in **§19 Application Outcome Progression & Learning**.

---

## 10. Cover letters

The product must be capable of generating job-specific cover letters when:

- the employer requires one;  
- the application process requests one;  
- or policy determines one is materially beneficial.  

Cover letters must be grounded in:

- verified candidate facts;  
- the actual job description;  
- defensible employer/job information.  

The system must not fabricate:

- company problems;  
- company initiatives;  
- candidate accomplishments;  
- candidate metrics;  
- relationships;  
- experiences;  
- or other unsupported claims.  

Jobscan cover-letter methodology may remain reference material but is **not** automatically a binding product requirement.

---

## 11. Application execution

The product must be capable of navigating real-world application workflows, including:

- job-board application flows;  
- employer career sites;  
- ATS-hosted application systems;  
- account creation where appropriate;  
- login;  
- session reuse where appropriate;  
- resume upload;  
- cover-letter upload;  
- multi-page forms;  
- screening questions;  
- dropdowns;  
- radio buttons;  
- checkboxes;  
- required acknowledgements;  
- validation errors;  
- final submission.  

The system must not assume every employer uses the same questions or workflow.

---

## 12. ATS-agnostic application architecture

The product requirement is **not** limited to a short list of ATS vendors.

An unsupported or previously unseen ATS must **not** automatically mean an unsupported job.

The application capability should be ATS-agnostic by default, with specialized platform knowledge/adapters added where they materially improve reliability.

### 12.1 Layer 1 — General application agent

The agent should be capable of reasoning over unfamiliar application pages using page semantics:

- identify form fields;  
- understand labels;  
- map verified candidate facts to fields;  
- select appropriate options;  
- upload the correct application artifacts;  
- navigate multi-step forms;  
- identify validation errors;  
- handle account/login state;  
- identify submission controls;  
- determine whether submission succeeded.  

### 12.2 Layer 2 — ATS-specific intelligence

For frequently encountered platforms, the system may use specialized knowledge involving:

- login/account behavior;  
- sessions;  
- field patterns;  
- navigation patterns;  
- known quirks;  
- successful prior application paths;  
- reusable ATS/site knowledge.  

### 12.3 Coverage awareness (not exhaustive adapter mandate)

Initial high-priority platforms for **explicit validation** should include:

- Workday  
- Greenhouse  
- Lever  
- iCIMS  
- Oracle / Taleo / Oracle Recruiting  
- SAP SuccessFactors  
- SmartRecruiters  
- Ashby  

Other systems may include, without making this list exhaustive:

- ADP Recruiting  
- UKG Recruiting  
- Dayforce  
- Jobvite  
- Workable  
- BambooHR  
- JazzHR  
- Avature  
- Eightfold  
- Phenom  
- Cornerstone  
- PageUp  
- Paycom  
- Paycor  
- Paylocity  
- Bullhorn  
- Breezy HR  
- Rippling  
- Teamtailor  
- proprietary/custom employer application sites  

These names define **coverage awareness**, not a requirement to build a bespoke automation implementation for every vendor.

### 12.4 Unfamiliar systems

For unfamiliar systems:

1. Qualified job  
2. Follow application destination  
3. General application agent attempts application  
4. If successful, verify and persist the result  
5. Preserve reusable knowledge where appropriate  

If the agent cannot safely proceed:

1. Park that individual application  
2. Record the blocker  
3. Continue processing other qualified jobs  

The entire pipeline must not stop merely because one ATS/application cannot be completed.

Product success should ultimately be measured more by successful autonomous completion across qualified jobs than by the raw number of named ATS adapters.

---

## 13. Screening-question intelligence

The system must maintain reusable application-question knowledge.

Desired hierarchy:

1. **Known factual answer** → answer automatically.  
2. **Previously approved equivalent question** → retrieve approved answer and answer automatically.  
3. **Answer safely derivable from authoritative candidate facts** → answer automatically only where permitted by autonomy policy.  
4. **Unknown factual question** → never fabricate.  
5. **Ambiguous, sensitive, consequential, or high-risk question** → park/escalate according to policy.  

When human intervention supplies an approved reusable answer, the system should be capable of retaining that knowledge for appropriate future applications.

---

## 14. Human intervention

Human-in-the-loop behavior should be an exception path rather than the normal operating model.

A single blocked application must not stop unrelated applications.

Desired behavior:

1. Application cannot safely proceed  
2. Park application  
3. Record exact blocker/context  
4. Continue processing other jobs  
5. Surface parked application for intervention through the Operator Console (§18.12)  

After intervention, the application should be capable of resuming where practical.

Reusable knowledge learned from intervention should be retained when appropriate and approved.

The owner should not ordinarily need to inspect logs or invoke internal commands to discover that intervention is required.

---

## 15. Submission verification

Clicking a Submit button is **not** sufficient evidence of successful application.

The product must independently establish and persist evidence that an application was successfully submitted.

Verification may ultimately use multiple signals, including:

- post-submit browser state;  
- ATS/employer confirmation state;  
- confirmation identifier where available;  
- application history/state where available;  
- confirmation email;  
- other reliable evidence.  

The system must distinguish:

- **attempted**  
- from **submitted**  
- from **verified submitted**  

---

## 16. Dedicated job-search email

The product will use a dedicated Gmail account for job-search/application activity rather than the operator’s general-purpose personal mailbox.

The same dedicated applicant email identity should be used consistently where appropriate across:

- candidate profile;  
- resumes;  
- cover letters;  
- ATS accounts;  
- application forms;  
- application confirmations;  
- recruiter communications;  
- assessments;  
- interview invitations;  
- application-status communications.  

Email access must be limited to permissions necessary for the approved job-application and tracking functions.

Actual Gmail connection/authentication architecture is **not** defined by this document and must be addressed later under security/implementation governance.

Gmail/email tracking is an **automatic evidence source**. It is **not** the owner’s primary interface with the agent and is **not** the sole source of application outcomes. Owner-reported offline events and the Operator Console are specified in §18 and §19.

---

## 17. Email and response tracking

The system must associate application-related communications with the correct application where practical.

It should be capable of distinguishing meaningful communication types such as:

- account verification;  
- application confirmation;  
- rejection;  
- recruiter outreach;  
- screening/assessment request;  
- interview request;  
- scheduling communication;  
- additional-information request;  
- offer-related communication;  
- other material application-status communication.  

These events should update or inform the application’s state.

Email-derived evidence is one part of multi-source outcome tracking (§19). Interview progression must not be defined solely as receiving a particular Gmail message.

---

## 18. Operator Console & Natural-Language Agent Control

This is a first-class product capability.

The finished autonomous job-search agent requires a normal owner-facing interface through which the owner can communicate with, control, question, update, and provide real-world outcome information to the running agent.

The product must not merely run autonomously in the background with no owner operating experience.

### 18.1 Owner-facing operating interface

The finished product must provide an owner-facing operating interface suitable for normal daily use — the **Operator Console / Natural-Language Agent Interface**.

For routine job-search operations, the owner should **not** need to use:

- Cursor;  
- Claude Code;  
- Python commands;  
- shell / PowerShell;  
- SQLite / database commands;  
- internal pipeline commands;  
- source-code editing.  

The existing CLI may remain available as an engineering/diagnostic/administrative interface (§18.16).

The Operator Console is the normal owner-facing interface.

### 18.2 Natural-language communication

The owner should be able to communicate with the running agent in ordinary natural language.

The system should interpret owner messages into appropriate product intents such as:

- query;  
- instruction;  
- preference update;  
- exclusion;  
- positive target example;  
- negative target example;  
- status request;  
- explanation request;  
- application lookup;  
- artifact lookup;  
- pause;  
- resume;  
- outcome update;  
- HITL response;  
- reusable knowledge;  
- one-time information.  

Illustrative examples (not an exhaustive command list):

- “What jobs did you apply to today?”  
- “Why did you apply to this job?”  
- “Show me the resume you submitted to Microsoft.”  
- “Stop applying to sales engineer jobs.”  
- “Do not apply to jobs requiring more than 25% travel.”  
- “This is exactly the kind of job I want.”  
- “Use this job description as a positive example.”  
- “Pause applications.” / “Resume applications.”  
- “Show me applications that need my attention.”  
- “Microsoft called me. I have a recruiter interview Friday.”  
- “I got rejected by Salesforce.”  
- “I interviewed with them today.”  
- “I’m moving to the hiring manager.”  
- “That recruiter screen went well.”  
- “I received an offer.”  
- “That job is no longer something I want.”  

Do not require the owner to memorize rigid commands for routine use.

Structured UI controls may supplement natural-language interaction where useful, but should not replace the conversational operating model.

The interface should behave like communication with an autonomous agent being managed by its owner, not like operating a collection of scripts.

### 18.3 Conversation is the interface — structured state is the system of record

This distinction is mandatory.

| Role | Meaning |
|------|---------|
| **Natural-language conversation** | The human interface |
| **Structured durable state** | The system of record for consequential product state |

Conversation history alone must **not** become the authoritative persistence mechanism for consequential product state.

Conceptually:

**Owner message → Intent / entity resolution → Policy / authority check → Structured action → Durable state update → Audit record → Owner confirmation / response.**

Examples:

- “Don’t apply to sales engineer jobs.” → appropriate durable targeting/exclusion rule.  
- “Microsoft called. I have an interview Friday.” → application outcome/progression event associated with the correct application.  
- “Pause applications.” → durable operational state change.  

Do not rely on an LLM merely remembering a prior conversation.

### 18.4 Application / entity resolution

The Operator Console must resolve conversational references against durable application/job/employer state.

Examples of resolvable entities:

- employer;  
- job title;  
- application;  
- recruiter;  
- date;  
- submitted resume;  
- job description;  
- application outcome.  

If the owner says “Microsoft called me. I have a recruiter interview Friday.” and exactly one active Microsoft application clearly matches, the system should be capable of associating the event with that application.

If multiple plausible applications exist, the agent must **not** guess.

It should ask a concise disambiguation question or present the likely applications for selection.

The same principle applies to statements such as “I interviewed with them today.”

Conversational context may help identify “them,” but consequential durable updates must be tied to a sufficiently resolved entity/application.

### 18.5 Owner-reported outcomes

The product must explicitly support **owner-reported application outcomes**.

This is necessary because important recruiting events may occur outside channels the agent can automatically observe.

Examples include:

- phone calls;  
- SMS / text messages;  
- recruiter conversations;  
- in-person conversations;  
- networking introductions;  
- external scheduling systems;  
- verbal interview progression;  
- verbal rejection;  
- verbal offer/progression information.  

The owner must be able to report these through natural language.

The system should convert this information into structured application history when the relevant application can be reliably identified.

### 18.6 Owner-reported information as authoritative owner evidence

When the owner explicitly reports an event that occurred outside automatically observable channels, the system should treat the owner’s report as authoritative evidence that the owner-reported event occurred.

Record provenance such as:

**SOURCE: OWNER_REPORTED**

This does not mean every owner statement becomes a permanent global rule.

Distinguish:

- owner-reported application event;  
- owner preference;  
- reusable candidate fact;  
- reusable screening answer;  
- one-time information;  
- conversational commentary.  

Apply the appropriate autonomy/knowledge policy before converting information into reusable global knowledge.

### 18.7 Explanation / inspection

Through the Operator Console, the owner should be able to ask the agent why it acted.

Examples:

- “Why did you apply to this?”  
- “Why did you reject this job?”  
- “Why did this score highly?”  
- “What did you change in my resume?”  
- “Which resume did you submit?”  
- “What screening risks did you identify?”  
- “Why is this application parked?”  

The system should answer from durable evidence/audit state where possible, not invent a post-hoc explanation.

### 18.8 Artifact access

The owner should be able to retrieve or inspect relevant artifacts through the normal operating interface.

Examples:

- original JD;  
- job URL;  
- qualification analysis;  
- tailored resume;  
- cover letter;  
- screening analysis;  
- screening questions/answers;  
- submission evidence;  
- application history;  
- recruiter/interview progression.  

The exact UI presentation is an architecture/design decision.

The product requirement is that normal inspection must not require database queries or filesystem hunting.

### 18.9 Operational control

The Operator Console must support high-level operational control.

At minimum, the owner should be able to:

- pause autonomous applications;  
- resume autonomous applications;  
- see whether the system is running;  
- see whether the system is paused;  
- see applications requiring human attention;  
- see system-wide stop conditions;  
- inspect recent activity.  

The exact technical control mechanism is not specified by this PRD.

### 18.10 Owner targeting feedback

The Operator Console should allow the owner to teach the system about desired and undesired opportunities conversationally.

Examples:

- “This is exactly the type of job I want.”  
- “This is close, but too engineering-heavy.”  
- “Do not apply to roles like this.”  
- “This JD is an excellent example of my target.”  
- “This job is called AI Sales, but it is really Sales Engineering.”  

Such feedback should be capable of becoming structured targeting evidence when appropriate.

The system must distinguish:

- a reusable targeting preference;  
- an example job/JD;  
- a one-time decision about a particular application.  

Do not assume every conversational comment is a permanent rule.

### 18.11 Consequential natural-language actions

Natural language must not bypass existing policy/authority controls.

For consequential actions, the system must:

- resolve the intended action;  
- resolve affected entity/entities;  
- apply authorization/policy;  
- avoid acting on unresolved ambiguity;  
- record the resulting action;  
- preserve auditability.  

Examples:

- “Pause applications” can be executed as an operational control.  
- “Withdraw all my applications” is a materially different consequential action and remains governed by `AUTONOMY_AND_APPLICATION_POLICY.md`.  

Conversational convenience must not expand agent authority.

The Operator Console must operate within `AUTONOMY_AND_APPLICATION_POLICY.md`. It does not supersede that policy.

### 18.12 HITL through the operator experience

Where human intervention is legitimately required under `AUTONOMY_AND_APPLICATION_POLICY.md`, the Operator Console should provide a normal path for resolving it.

Examples:

- unknown factual question;  
- ambiguous application association;  
- CAPTCHA;  
- MFA;  
- login/account issue;  
- policy-required owner decision.  

### 18.13 Confirmation should be proportional

Do not turn the Operator Console into a confirmation-heavy manual workflow.

The agent should not ask for confirmation for every routine instruction merely because it arrived through natural language.

Confirmation/disambiguation should be used where needed because:

- the target is ambiguous;  
- the action is consequential and policy requires approval;  
- information conflicts with existing authoritative state;  
- the agent cannot safely determine owner intent.  

The product objective remains maximum safe autonomy.

### 18.14 Auditability of owner interactions

Consequential owner instructions and resulting structured actions should be auditable.

Where appropriate preserve:

- timestamp;  
- owner instruction;  
- interpreted intent;  
- affected application/job/rule;  
- resulting state change;  
- provenance;  
- whether clarification/confirmation was required.  

Do not require indefinite storage of irrelevant conversational chatter merely for audit purposes.

The architecture should distinguish operational/audit events from ordinary conversation history.

### 18.15 Privacy / data minimization

Do not expand access to personal communication channels merely because additional automation is technically possible.

The system should obtain job-search outcome information through the minimum necessary authorized channels.

For example, owner-reported phone/text outcomes can solve the V1 requirement without requiring autonomous access to the owner’s entire personal SMS or phone history.

Any future integration with additional communication channels must be deliberate and authorized.

### 18.16 CLI relationship

The inherited CLI remains useful for:

- engineering;  
- debugging;  
- diagnostics;  
- maintenance;  
- controlled testing;  
- administrative operation.  

It should not be the required normal interface for the owner once the Operator Console is available.

The product should separate:

| Interface | Purpose |
|-----------|---------|
| **Owner operating experience** | Operator Console / natural-language agent control |
| **Engineering / maintenance interface** | CLI and related diagnostic tools |

### 18.17 Implementation boundary

Do **not** prescribe a specific frontend framework, chat framework, database schema, model, or deployment architecture in this PRD.

Those decisions belong in architecture discovery and the implementation plan.

The product requirement is capability and behavior.

However, the eventual architecture must support:

- natural-language interaction;  
- durable structured state;  
- application/entity resolution;  
- policy enforcement;  
- auditability;  
- artifact inspection;  
- owner-reported outcomes;  
- operational controls;  
- outcome-driven learning.  

---

## 19. Application Outcome Progression & Learning

### 19.1 Multi-source outcome evidence

Application outcome tracking must not depend solely on Gmail.

The product should support outcome evidence from sources such as:

| Category | Examples |
|----------|----------|
| **Automatically observed** | Dedicated job-search email; ATS/application status where available; scheduling/interview communications where integrated; calendar events where later integrated and authorized |
| **Owner reported** | Phone calls; texts; verbal recruiter communication; interviews; other offline/out-of-band events |
| **Corroborated** | Owner reports an interview and a subsequent email/calendar invitation confirms it; multiple legitimate signals support the same progression state |

The system should retain source/provenance.

Do not require automatic corroboration before accepting a clear owner-reported event.

### 19.2 Application outcome / progression model

The product should maintain meaningful structured application progression rather than a binary applied/rejected model.

The exact technical state model will be determined during architecture/implementation, but product requirements should support distinctions such as:

- discovered;  
- qualified;  
- tailored;  
- submitted;  
- submission confirmed;  
- recruiter outreach;  
- recruiter screen requested;  
- recruiter screen scheduled;  
- recruiter screen completed;  
- assessment requested;  
- assessment completed;  
- hiring-manager interview requested;  
- hiring-manager interview scheduled;  
- hiring-manager interview completed;  
- later-stage interview;  
- final interview;  
- rejected;  
- withdrawn;  
- offer-related progression;  
- offer;  
- hired;  
- unknown / no response.  

Do not require these exact database enum values in the PRD.

The product requirement is to preserve meaningful progression evidence sufficient for tracking and learning.

### 19.3 Interview-stage detection

The product must recognize interview progression from both:

A. automatically observed evidence; and  
B. owner-reported evidence.  

Do not define “interview reached” solely as receiving a particular Gmail message.

Differentiate useful progression strengths where practical.

For example:

| Progression | Relative strength |
|-------------|-------------------|
| Recruiter interest / outreach | Positive evidence |
| Scheduled recruiter screen | Stronger progression evidence |
| Hiring-manager interview | Stronger still |
| Later-stage / final interview | Stronger still |
| Offer | High-strength positive outcome |

These distinctions should eventually inform outcome-driven learning.

### 19.4 Historical freeze of submitted application evidence

For every submitted application, preserve sufficient historical evidence to associate outcomes with the application that generated them.

At minimum, conceptually preserve/freeze:

- original job description used for the application;  
- job metadata;  
- employer;  
- ATS/source where known;  
- qualification analysis;  
- pre-tailor screening analysis;  
- exact tailored resume submitted;  
- cover letter submitted, if any;  
- relevant screening questions/answers;  
- submission evidence;  
- submission date/time;  
- subsequent progression/outcome events;  
- provenance of those outcome events.  

Do not allow later resume edits or job-description changes to destroy the historical record of what was **actually** submitted.

### 19.5 Learn from interview-producing resume / JD pairs

This is a first-class product objective.

When an application reaches meaningful positive progression such as recruiter screen, interview, later-stage interview, or offer, the learning system should be capable of analyzing:

**The job description + the exact resume that was submitted + the candidate’s verified facts + the screening/tailoring decisions + the observed outcome.**

The purpose is to identify evidence-backed patterns that may improve future:

- job qualification;  
- screening analysis;  
- terminology alignment;  
- experience emphasis;  
- professional summary strategy;  
- skill emphasis;  
- accomplishment emphasis;  
- resume structure;  
- tailoring decisions.  

Example conceptual learning:

For similar AI consulting roles, applications that progress may consistently make certain verified experience more explicit than applications that do not.

That pattern may become useful evidence for future tailoring.

### 19.6 Learning must not overfit single outcomes

One interview does **not** prove that a particular word, resume structure, or tailoring decision caused the interview.

One rejection does **not** prove the resume caused the rejection.

The learning system must distinguish:

**Observation → Pattern → Hypothesis → Evidence-backed strategy**

and should strengthen conclusions as evidence accumulates.

Avoid uncontrolled strategy changes based on isolated outcomes.

### 19.7 Positive and negative outcomes

The system should learn from both:

| Category | Examples |
|----------|----------|
| **Positive progression** | Recruiter response; recruiter screen; interview; later-stage interview; offer |
| **Negative / non-progression** | Rapid rejection; later rejection; no response; failed screening; application abandoned/parked where relevant |

Negative outcomes are evidence but must not automatically be attributed to resume quality or ATS behavior.

The system should compare sufficiently similar applications before drawing strategic conclusions.

### 19.8 Outcome signal strength

The product should support the concept that outcomes have different evidentiary strength.

For example:

| Signal | Evidentiary note |
|--------|------------------|
| Application confirmation | Proof of receipt, but weak/no evidence of resume effectiveness |
| Recruiter outreach | Positive progression evidence |
| Scheduled recruiter screen | Stronger evidence |
| Hiring-manager interview | Stronger evidence |
| Later-stage / final interview | Stronger evidence |
| Offer | Very strong positive progression evidence |

The precise weighting/model should be determined through architecture and empirical validation rather than invented in the PRD.

Do not create arbitrary numerical weights now.

---

## 20. Continuous closed-loop operation

The finished product must not require the operator to manually run every pipeline stage repeatedly.

The eventual autonomous loop is:

**Discover → qualify → prepare → validate → apply → verify → track → replenish → repeat.**

The system should recover appropriately after restart and maintain durable application/job state.

Continuous operation must respect:

- safety controls;  
- resource controls;  
- retry policy;  
- parked applications;  
- application eligibility;  
- duplicate prevention;  
- security policy;  
- Operator Console operational controls (pause/resume/system-wide stop visibility).  

Owner interaction with the running autonomous loop should normally occur through the Operator Console (§18), not by manually reissuing pipeline stage commands.

---

## 21. Security and trust

Because the agent processes untrusted internet content while handling applicant information and potentially controlling a browser, security is a **product requirement** rather than merely an implementation concern.

The finished system must protect:

- applicant PII;  
- credentials;  
- authentication tokens;  
- browser sessions;  
- email authorization;  
- resumes;  
- screening answers;  
- generated documents;  
- application history.  

Untrusted job descriptions, employer pages, ATS pages, and form content must not be allowed to:

- redefine the agent’s mission;  
- override governing instructions;  
- exfiltrate secrets;  
- or cause unrelated system actions.  

Unattended operation must not be enabled until the required security controls are satisfied.

Specific security architecture belongs in later governance/architecture documents.

---

## 22. Auditability and application record

For every application, the system should retain sufficient evidence to reconstruct what occurred.

This should include, where appropriate:

- source job;  
- employer;  
- job title;  
- application URL;  
- job description used for qualification;  
- qualification/fit result;  
- reason for qualification;  
- pre-tailor screening analysis / candidate-evidence mapping where performed;  
- exact tailored resume submitted (historical freeze; §19.4);  
- post-tailor screening analysis where performed;  
- cover letter submitted, if any;  
- screening questions encountered;  
- answers submitted;  
- timestamps;  
- application attempts;  
- blockers/interventions;  
- submission result;  
- verification evidence;  
- subsequent relevant communications;  
- owner-reported outcome events and provenance;  
- application-state / progression transitions;  
- consequential Operator Console instructions and resulting structured actions (§18.14).  

Do not allow later resume edits or job-description changes to destroy the historical record of what was actually submitted.

---

## 23. Failure isolation and recovery

Failure of one job/application must not halt the entire autonomous job-search system unless a system-wide safety condition requires shutdown.

The system should distinguish:

- job-specific failure;  
- ATS-specific failure;  
- credential/session failure;  
- temporary service failure;  
- AI-provider failure;  
- security/safety failure;  
- system-wide failure.  

Recoverable failures should be retried according to policy.

Unsafe or unresolved applications should be parked rather than guessed through.

---

## 24. Success criteria

The product must eventually have measurable success criteria covering areas such as:

- target-job discovery precision;  
- rejection of clearly unsuitable engineering-heavy roles;  
- factual accuracy;  
- resume validation reliability;  
- improvement from base-resume screening alignment to tailored-resume screening alignment;  
- truthful representation of supported qualifications;  
- avoidance of fabricated qualifications;  
- ability to distinguish candidate-fit gaps from resume-presentation gaps;  
- Gate 2 optimization without degradation of Gate 3 quality;  
- eventual progression of qualified applications through automated screening toward human/recruiter engagement where measurable;  
- owner can operate the agent without routine CLI/database/source-code interaction;  
- natural-language instructions can become correct durable state/actions;  
- ambiguous application references are safely disambiguated;  
- owner-reported offline outcomes can be associated with the correct application;  
- interview-stage progression can be captured from automatic and owner-reported sources;  
- exact submitted resume/JD pairs remain associated with outcomes;  
- interview-producing applications can contribute to future tailoring intelligence;  
- learning does not fabricate causality from isolated outcomes;  
- owner can inspect why applications were selected, tailored, submitted, parked, or rejected;  
- pause/resume and human-attention controls are accessible through the owner interface;  
- consequential owner actions remain auditable;  
- autonomous application completion rate;  
- submission-verification reliability;  
- screening-question automation rate;  
- HITL frequency;  
- duplicate-application prevention;  
- email/application correlation;  
- continuous-operation reliability;  
- security/safety compliance.  

Numerical thresholds are **not** invented in this document unless already explicitly approved.

The implementation plan may later establish measurable validation targets after baseline evidence exists.

---

## 25. Non-goals / out of scope

For the initial autonomous application product, do not expand scope into a general career-management platform.

Unless explicitly added later, the following are **not** core V1 requirements:

- interview coaching;  
- STAR-story coaching;  
- virtual interview presentation coaching;  
- salary negotiation coaching;  
- networking automation;  
- LinkedIn content creation;  
- personal-brand management;  
- generic career coaching;  
- autonomous recruiter messaging unrelated to an active application;  
- indiscriminate mass application.  

Post-application functionality is included only where necessary to identify and track meaningful employer responses, capture owner-reported progression, support outcome-driven learning, and hand off successful opportunities to the operator through the Operator Console.

The Operator Console is **not** a license to expand into interview coaching, negotiation coaching, or general career-platform features listed above.

---

## 26. Relationship to inherited ApplyPilot

The inherited ApplyPilot repository is the implementation starting point.

This PRD distinguishes:

| Concept | Meaning |
|---------|---------|
| **Required product behavior** | Defined by this document |
| **Currently implemented behavior** | What the inherited codebase does today — evidence only |

Do not weaken a product requirement simply because inherited ApplyPilot does not currently satisfy it.

Do not describe inherited developer-specific settings as our requirements.

Examples of inherited settings that are **not** automatically requirements include:

- score thresholds;  
- job-age thresholds;  
- geography;  
- Seattle-specific discovery;  
- company application caps;  
- previous candidate profile;  
- previous target roles;  
- previous salary preferences;  
- previous model-cost optimization choices.  

---

## 27. Relationship to Jobscan guidelines

`docs/guidelines/jobscan/**` is attributed reference/research material.

It may inform future implementation and validation decisions.

It is **not** automatically product authority.

Do not make Jobscan numeric thresholds or methodology binding requirements unless explicitly approved.

---

## 28. Required vs currently implemented (orientation)

This section orients readers; it does **not** change requirements.

| Area | Product requirement (this PRD) | Inherited starting point (evidence only) |
|------|--------------------------------|------------------------------------------|
| Closed-loop continuous autonomy | Required end state | Stages are largely CLI-driven; full loop not continuous by default |
| Target-job intelligence for AI consulting vs engineering-heavy roles | Required | Scoring/prefilters oriented to a different candidate persona |
| Authoritative facts / no fabrication | Required | Partial fact pinning exists; gaps remain |
| Title truthfulness (no historical title inflation) | Required | Inherited tailor guidance includes verbatim target-title matching |
| ATS Screening & Resume Optimization Intelligence (pre-/post-tailor; fit ≠ presentation) | Required | Tailoring exists; affirmative Gate 2 screening loop and fit-vs-presentation distinction not product-complete |
| Operator Console & Natural-Language Agent Control | Required | Extension popup/options and CLI exist; not a normal owner conversational operating interface |
| Owner-reported offline outcomes + multi-source progression | Required | Gmail tracking exists; owner-reported phone/text/verbal outcomes and progression model not product-complete |
| Outcome-driven learning from exact submitted resume/JD pairs | Required | Not product-complete; historical freeze and evidence-backed learning required |
| Independent submission verification | Required | Success often trusts agent result signals |
| ATS-agnostic Layer 1 + selective Layer 2 | Required | Strongest on some platforms; not product-complete |
| Dedicated job-search Gmail identity | Required | Tracking exists; identity policy is ours; email is not sole outcome source |
| Security as product gate for unattended operation | Required | Known trust-boundary gaps in starting code |

Where rows conflict, **this PRD wins** until the owner revises it.

---

*End of JOB_AGENT_PRODUCT_REQUIREMENTS.md*  
*Status: Approved — Authoritative.*
