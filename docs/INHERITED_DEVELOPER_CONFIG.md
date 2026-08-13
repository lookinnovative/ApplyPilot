# Inherited Developer Configuration — Isolation Notice

**Status:** Active isolation checklist for WP0.5  
**Authority:** Complements Approved governance (`ARCHITECTURE_CURRENT.md`, `ENGINEERING_IMPLEMENTATION_PLAN.md`)  
**Does not authorize:** Treating any item below as this fork owner’s production candidate truth  

---

## Separation of concerns

| Class | What it is | Authoritative for production candidate? | Disposition |
|-------|------------|-----------------------------------------|-------------|
| **Owner runtime profile** | `~/.applypilot/profile.json`, `resume.txt`, owner-authored answers | **Yes** (when created by this owner) | Create/maintain in WP2.1 — **not present** until owner init |
| **Owner search config** | `~/.applypilot/searches.yaml` | **Yes** (when authored for this owner) | Must be owner-customized; do not treat package examples as final |
| **Package discovery registries** | `src/applypilot/config/{employers,greenhouse_employers,lever_employers,ashby_employers}.yaml` | **No** as candidate profile; **Yes** as current discovery code inputs | Prior-developer Seattle/geo targeting — generalize in Phase 2/7 (not WP0.5 rewrite) |
| **Hard-coded scorer/prompt persona** | `scoring/scorer.py`, parts of `apply/prompt.py`, Amazon/Costco location defaults | **No** | Replace in **WP2.2** / adapt discovery in later WPs — do not treat as owner persona |
| **Research / historical YAMLs** | `docs/seattle_employers_v1.yaml`, `v2.yaml`, `v3_megacorps.yaml` | **No** | **Non-runtime.** Migrate useful ATS IDs later (WP7.4); then archive. Do not delete in WP0.5. Do not invent Atlanta replacements here. |
| **Examples** | `profile.example.json`, `src/applypilot/config/searches.example.yaml` | **No** | Templates only — IC-engineering-oriented example queries are **not** this product’s approved consulting target |

---

## WP0.5 isolation (completed here)

1. Research Seattle employer YAMLs marked **NON-RUNTIME / NOT PRODUCTION CANDIDATE CONFIG**.  
2. Example search + profile templates marked **EXAMPLE ONLY**.  
3. Package discovery registries marked **prior-developer targeting, not candidate profile**.  
4. Scorer module annotated that embedded Seattle/IC-eng persona is **not** owner production truth (replacement = WP2.2).  
5. No Atlanta substitute catalogs created. No new hard-coded owner persona introduced.

---

## Deferred to Phase 2 (required before autonomous qualification)

| Work package | Responsibility |
|--------------|----------------|
| **WP2.1** | Authoritative structured candidate profile for this owner (facts / preferences / targeting policy separated) |
| **WP2.2** | Remove inherited Seattle/IC-engineering persona from scoring/prefilter; config-driven owner persona |
| **WP2.3** | JD-substantive qualification (titles as signals; eng-heavy SE/Solutions Engineer and non-fitting pure sales remain intended negatives when JD confirms) |

Discovery geography/registry generalization beyond this isolation notice is further handled in Phase 7 (e.g. WP7.1, WP7.4) and must not be mistaken for candidate-profile authority.
