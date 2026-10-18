# QC Laboratory Capacity, Staffing Gap and CAPEX Assessment — Sample Report

Oct 17, 2026 · @Reza

**Deliverable 1 of 2 — Sample Assessment Report.** Deliverable 2 (Laboratory Unit Head Questionnaire) is issued as a separate document.

> **Important — illustrative values only.** Every number in this report (volumes, hours, utilization, headcount, costs) is **hypothetical** and exists only to demonstrate the method. None of it describes a real company, a measured result or a supplier quotation. **Do not use any value in this report for budget approval or purchasing.** Each figure must be replaced with verified company data collected through the questionnaire and central records.

**Data labels used throughout**

| Label | Meaning |
| --- | --- |
| \[H\] | Hypothetical value used to demonstrate a calculation |
| \[A\] | Planning assumption — must be confirmed or replaced by the company |
| \[V\] | Verified data — none exists in this sample; reserved for the company-specific version |
| \[C\] | Data to be collected (questionnaire or central records) |

Currency: all costs are in **k HCU** (thousands of hypothetical currency units). They are order-of-magnitude placeholders, not prices.

## Table of contents

1. Executive summary
2. Scope, assumptions and methodology
3. Laboratory organization and workload
4. Testing demand and workload model
5. Instrument capacity and shortage assessment
6. Staffing capacity and shortage assessment
7. Combined capacity and bottleneck analysis
8. CAPEX assessment and investment plan
9. OPEX and financial considerations
10. Scenarios and recommendations
11. Implementation roadmap
12. Limitations and data validation
13. Appendices
    1. Appendix A — Test–method workload calculation (extract)
    2. Appendix B — Instrument capacity calculation sheets
    3. Appendix C — Staff capacity calculation sheets
    4. Appendix D — Microbiology incubator and facility capacity
    5. Appendix E — Minimum company data required

## 1. Executive summary

In this hypothetical case the laboratories can absorb today's demand. They cannot absorb the forecast demand for year 3 without targeted action: HPLC, dissolution and microbiology incubation reach or exceed their planning limits. Chemical data review is already the main cause of slow turnaround. In aggregate, staff hours look balanced (99% of available hours are needed), but this hides gaps in specific roles and competencies.

**Purpose and scope.** The assessment tests whether the people, instruments, facilities and workflows of the Chemical, Physical and Microbiological QC laboratories can meet current demand (baseline year Y0) and forecast demand over a three-year horizon (Y1–Y3). It identifies shortages, bottlenecks and investment needs. It also sets out the data that unit heads must supply (Deliverable 2) to turn this sample into a real assessment.

**Demand \[H\].** Baseline workload is about 44,300 analyst hours a year across the three units. Forecast growth to Y3 is +30% in the Chemical lab, +25% in the Physical lab and +20% in the Microbiological lab. Drivers are two new oral solid products in Y2 and higher batch volumes \[A\].

**Principal gaps \[H\].**

- **HPLC:** 79% utilization at baseline, 102% forecast in Y3 against an 80% planning limit. One of eight systems is out of service and obsolete.
- **Dissolution:** 82% now and 107% forecast against a 75% limit. A further 2009 bath is out of vendor support.
- **Chemical data review:** 3,400 review hours are needed against 2,128 available. This queue, not instrument time, is the main driver of release turnaround.
- **Microbiology:** the 30–35 °C incubators are at 108% of routine capacity in peak months. Only two analysts are qualified for sterility testing. Sterility isolator demand reaches 76% of sessions against a 70% limit.
- **Single points of failure:** GC headspace (one unit), FTIR (one unit), sterility isolator (one unit) and the media-preparation autoclave (one unit).

**Most significant risks.** Delayed batch release when review queues and HPLC peaks coincide. Loss of sterility-testing capability if either qualified analyst is absent. Missed stability pull-point timelines. Rising repeat and investigation workload as utilization approaches 100%.

**Proposed actions and cost \[H\].** Three scenarios are compared in Section 10. The recommended path is **Scenario B, Targeted Capacity Expansion**. It costs about **363 k HCU CAPEX** (including a 10% contingency \[A\]) and about **165 k HCU incremental annual OPEX**, adds **2 FTE** above approved headcount, and fills the 3 vacancies already approved. Scenario C items (about 612 k HCU more CAPEX including contingency) are held back until defined demand triggers are met.

**Decisions required from management.**

1. Approve the data-collection phase (questionnaire plus central records, 6–8 weeks) before any purchase is committed.
2. Authorize immediate no-CAPEX actions (Scenario A): reviewer cross-authorization, scheduling changes, filling approved vacancies, and an outsourced sterility backup contract.
3. Pre-approve Scenario B budget envelopes, released item by item once verified data confirm each gap.
4. Agree the demand triggers that would release Scenario C items.

**Executive summary table \[H\]**

| Laboratory Unit | Main Constraint | Evidence Required | Proposed Action | Priority |
| --- | --- | --- | --- | --- |
| Chemical | Second-person data review capacity | Review queue age from LIMS/CDS; review hours per sequence; reviewer authorization list | Authorize 2 senior analysts as reviewers; recruit 1 senior analyst/reviewer | Immediate |
| Chemical | HPLC capacity and one obsolete system | CDS run logs (12 months); downtime and repair records; vendor end-of-support notice; method–instrument matrix | Replace HPLC-05; run overnight sequences; add a 9th HPLC only if Y2 utilization is above 85% | High |
| Chemical | GC headspace single point of failure | Residual-solvent test volume; GC-01 downtime history; validation status on GC-02 | Fit headspace sampler to GC-02 and validate the method on it | High |
| Physical | Dissolution bath capacity and obsolescence | Bath logbooks; runs per month and peak; mechanical qualification records; support status | Add 1 bath with autosampler; cross-train 2 analysts; replace the 2009 bath in Y2 | High |
| Microbiological | Incubator capacity at peak; sterility competency coverage | Incubator loading records; EM plate counts by month; gowning and aseptic qualification records | Add one 30–35 °C incubator; qualify 2 more isolator operators; fill vacancy; outsourced sterility backup | Immediate |
| Microbiological | Media autoclave single point of failure | Autoclave cycle logs; breakdown history; media-prep schedule | Backup arrangement now; evaluate a second autoclave in Scenario C | Medium |

## 2. Scope, assumptions and methodology

Capacity is assessed separately for each resource: method-qualified analysts, reviewers, instruments and facilities. It is then compared with workload built bottom-up from test–method demand. Headcount and instrument counts alone are never treated as capacity.

### 2.1 Assessment period and planning horizon

- **Baseline (Y0):** the most recent 12 complete months of actual data \[C\]. In this sample, Y0 values are \[H\].
- **Forecast:** Y1, Y2 and Y3, based on the approved production plan and product portfolio changes \[C\].
- **Outlook:** a qualitative Y5 view for long-lead items such as facilities, isolators and autoclaves.

### 2.2 Testing categories in scope

| Category | Included | Notes |
| --- | --- | --- |
| Raw materials (APIs, excipients) | Yes | Including reduced testing under supplier qualification where approved |
| Packaging materials | Yes, if tested by QC | Often Physical lab; confirm \[C\] |
| In-process control (IPC) samples | Yes | Include only IPC done by QC labs, not by production |
| Finished products (release) | Yes |  |
| Stability samples | Yes | Pull schedule from the stability protocol register |
| Environmental and personnel monitoring | Yes | Sampling time and plate reading counted |
| Water and utilities monitoring | Yes | Purified water, WFI, clean steam, compressed gases where applicable |
| Cleaning validation and verification samples | Yes, if tested by QC |  |
| Method validation, verification and transfer | Yes, as non-routine workload |  |
| Investigations (OOS, OOT, deviations) | Yes, as non-routine workload |  |
| R&D or external customer testing | Only if QC labs perform it | Must be listed separately |

### 2.3 Laboratory units in scope

- **Chemical Laboratory:** identity, assay, impurities, residual solvents, water content and the chemical end of dissolution where applicable. Also reference standards, reagents and solution preparation.
- **Physical Laboratory:** appearance, physical and pharmacotechnical tests, including dissolution, disintegration, hardness, friability, pH, density and viscosity.
- **Microbiological Laboratory:** microbial limits, sterility and endotoxins (where applicable), environmental and water monitoring, media preparation, growth promotion and identification.

The actual split of tests between units varies between companies. For example, dissolution may sit in the Physical or the Chemical lab. It must be confirmed in Section A of the questionnaire.

### 2.4 Data collection approach

| Data | Collected centrally (QC management, QA, Planning, Finance, HR, Engineering) | Supplied by each unit head |
| --- | --- | --- |
| Production plan and forecast batch numbers | Planning / Supply Chain | — |
| Product portfolio changes and launches | Regulatory / Portfolio management | Impact on methods and tests |
| Sample volumes and turnaround history | LIMS extract (QC systems owner) | Validation of the extract; context |
| Stability pull schedule | Stability coordinator | — |
| Instrument run hours and audit-trail data | CDS / instrument software extract | Confirmation; non-networked instrument logbooks |
| Calibration, maintenance and qualification schedules | Engineering / metrology system | Actual downtime experience |
| Headcount, vacancies, leave, sickness (aggregate) | HR | Role allocation and method authorizations |
| Training and authorization records | Training system / QA | Competency matrix review |
| Deviations, OOS, OOT, CAPA counts | QA system | Hours per event |
| Cost data (salaries, service contracts, consumables) | Finance / Procurement | Consumable usage per method |
| Method-level times (prep, run, review) | — | Questionnaire Section E, preferably timed observations |
| Bottlenecks, risks, investment requests | — | Questionnaire Sections F–J |

### 2.5 Capacity estimation method

1. Build the test–method matrix: every product or material × test × method, with annual sample demand.
2. For each row, separate four time elements: analyst hands-on time, instrument occupancy time, data processing and documentation time, and review and approval time.
3. Sum instrument occupancy by instrument group. Sum labor by role and by competency (method authorization).
4. Add non-routine workload once, using the rules in Section 4.4.
5. Calculate available instrument hours and qualified analyst hours.
6. Compare demand with capacity at a planning limit that suits each resource (Section 5.2). Then check peaks, redundancy and turnaround, not only annual averages.

### 2.6 Time and availability assumptions \[A\]

| Parameter | Assumed value | Basis / to be confirmed |
| --- | --- | --- |
| Working days per year | 250 | 365 − 104 weekend days − 11 public holidays \[A\] |
| Standard shift | 8 h, one day shift | Weekend coverage for microbiology monitoring \[A\] |
| Gross contracted hours per FTE | 2,000 h | 250 × 8 h |
| Annual leave | 200 h (25 days) | HR policy \[C\] |
| Sickness and other absence | 64 h (8 days) | HR aggregate data \[C\] |
| Training (GMP, method, refresher) | 60 h | Training plan \[C\] |
| Meetings, administration, housekeeping, GMP walk-downs | 156 h | Time-allocation survey \[C\] |
| **Effective productive hours per FTE** | **1,520 h (76% of gross)** | Used for all FTE calculations |
| HPLC/GC scheduled operating hours | 5,000 h per system (20 h × 250 days) | Assumes unattended overnight sequences are permitted and practised \[C\] |
| Dissolution bath scheduled hours | 2,500 h (10 h × 250 days) | Attended runs; autosampler-equipped baths may run longer \[C\] |
| Single-shift benchtop instruments (UV, FTIR, KF) | 2,000 h |  |
| Incubators | 365 days, continuous | Capacity is measured in shelf positions, not hours |
| Planned downtime (PM, calibration, requalification) | Per instrument group, Section 5 | Engineering schedule \[C\] |

### 2.7 Limitations

- All values are \[H\] or \[A\]. Conclusions show the method, not the answer.
- Self-reported method times can be optimistic or pessimistic by 20–40%. Timed observations or CDS timestamps are needed for the high-volume methods.
- Annual averages hide peaks (campaigns, stability pull clusters, shutdown EM). Monthly profiles are required.
- Forecast demand depends on the production plan, which carries its own uncertainty. Sensitivity at ±15% is recommended for key resources.
- Facility constraints (space, HVAC, utilities) are assessed qualitatively unless engineering surveys are available.

## 3. Laboratory organization and workload

The hypothetical company makes oral solid dosage forms (tablets, capsules), non-sterile oral liquids and one small sterile ophthalmic line \[H\]. The three units below depend on one another. The Physical lab's dissolution output and the Chemical lab's sample flow both feed the same release decision, and microbiology results set the final release date for the sterile and liquid products.

### 3.1 Unit profiles \[H\]

| Item | Chemical Laboratory | Physical Laboratory | Microbiological Laboratory |
| --- | --- | --- | --- |
| Main functions | Identity, assay, impurities, residual solvents, water content; reference standards and reagents; analytical documentation | Appearance and pharmacotechnical tests; dissolution and disintegration; IPC support for production campaigns | Microbial limits; sterility and endotoxins (ophthalmic line); EM and personnel monitoring; water microbiology; media; identification |
| Workload drivers | Batches released; raw material lots; stability pulls; new methods | Batches released; IPC pulls per campaign; stability pulls | Batches (liquids and sterile); EM plan (locations × frequency); water points; media batches |
| Major techniques | HPLC/UPLC, GC (incl. headspace), UV-Vis, FTIR, Karl Fischer, titration | Dissolution baths (UV or HPLC finish), disintegration, hardness/thickness, friability, pH, density, viscosity, LOD, sieve analysis | Membrane filtration, plate count, isolator sterility testing, kinetic chromogenic LAL, incubation, autoclaving, biosafety cabinets |
| Dependencies | Receives dissolution samples for HPLC finish; supplies reference standards to the Physical lab | Needs Chemical lab HPLC time for HPLC-finish dissolution methods | Needs production/Engineering for cleanroom access; media autoclave shared with decontamination |
| Approved / actual headcount (analysts + reviewers) | 16 / 14 + 1 temporary | 7 / 7 | 10 / 9 |

Headcount here includes reviewers and supervisors with a review role. Section 6 splits it by role.

### 3.2 Illustrative inventory of testing activities

This list is an example only. The actual test portfolio must be confirmed with the company through questionnaire Sections A and E.

| Unit | Activity | Typical sample categories | Main equipment | Key workload note |
| --- | --- | --- | --- | --- |
| Chemical | Assay and related substances by HPLC/UPLC | FP, stability, RM (API) | HPLC/UPLC with CDS | Sequence-based; instrument time much larger than hands-on time |
| Chemical | Residual solvents by GC headspace | API, some excipients | GC with headspace sampler | Long run times; only one headspace unit |
| Chemical | Identification (FTIR, UV, chemical tests) | RM, FP | FTIR, UV-Vis | Short tests at high volume |
| Chemical | Water content (KF), titrations, wet chemistry | RM, FP | KF titrators, autotitrators | Manual; hands-on intensive |
| Chemical | Dissolution HPLC finish | FP, stability | HPLC | Competes with assay for HPLC time |
| Chemical | Reference standards, reagents, solutions | Support | Balances, glassware | Often not counted; typically 5–10% of analyst time \[A\] |
| Physical | Appearance and organoleptic examination | All | Visual inspection station | Short, high volume |
| Physical | pH, density, viscosity, refractive index | Liquids | pH meter, densitometer, viscometer | One viscometer |
| Physical | Dissolution | Tablets, capsules | Dissolution baths, UV | Bath occupancy plus attended sampling |
| Physical | Disintegration | Tablets, capsules | Disintegration testers | Low utilization |
| Physical | Hardness, friability, weight variation, dimensions | IPC, FP | Hardness/thickness tester, friabilator, balances | Campaign peaks |
| Physical | Loss on drying, particle size (sieve) | Granules, RM | Moisture balance, sieve shaker |  |
| Microbiological | Microbial enumeration and specified organisms | Liquids, RM, some solids | BSC, incubators | Incubation 3–7 days; labor only at set-up and reading |
| Microbiological | Sterility test | Ophthalmic FP | Isolator, canister system, incubators | 14-day incubation; isolator decontamination cycle |
| Microbiological | Bacterial endotoxins | Ophthalmic FP, WFI | Kinetic reader | One reader; gel-clot as backup |
| Microbiological | EM and personnel monitoring | Grade A/B and C/D areas | Air sampler, plates, incubators | Weekend sampling required |
| Microbiological | Water microbiology | PW, WFI points | Filtration manifold, incubators | Daily and weekly points |
| Microbiological | Media preparation and growth promotion | Support | Autoclave, incubators | One media autoclave |
| Microbiological | Microbial identification | Excursions, OOS | Outsourced \[H\] | Turnaround depends on contract lab |

## 4. Testing demand and workload model

Workload is calculated per test–method row and then summed by resource. Each row must state its workload unit and keep the four time elements separate: hands-on, instrument occupancy, documentation and review.

### 4.1 Workload units

| Unit | Definition | Example |
| --- | --- | --- |
| Sample | One physical sample as received or pulled | One batch of Product A tablets for release |
| Test | One specification test on one sample | Assay on one batch |
| Test unit | The unit the time standard is written for; stated per row | One combined assay + related substances preparation set |
| Sample preparation | One set of weighings and dilutions | Duplicate preparations = 2 preparations, 1 test |
| Analytical sequence (run) | One instrument sequence including blanks, standards, SST and brackets | 6 samples + 12 overhead injections |
| Batch (analytical) | Samples tested together under one set-up | 6 vessels = one dissolution run |
| Plate | One EM, water or count plate (microbiology) | One settle plate |
| Session | One isolator or cleanroom use, including decontamination | One sterility test session |

Time standards may be per sample or per sequence. In this sample, sequence and batch overhead (equilibration, SST, blanks, brackets, washes, cleaning) is **allocated pro rata to samples**, using the typical batch size. For example, 14 h of HPLC occupancy per 6-sample sequence gives 2.4 h per sample (rounded). The company model should keep sequence overhead as a separate field so that the effect of batch size can be tested.

### 4.2 Core formulas

```latex
\text{Annual Test Units} = \text{Annual Samples} \times \text{Test Units per Sample}
```

```latex
\text{Required Instrument Hours}_{g} = \sum_{\text{rows using group } g} \text{Annual Test Units} \times \text{Instrument Occupancy per Unit}
```

```latex
\text{Required Analyst Hours}_{r} = \sum_{\text{rows}} \text{Test Units} \times (\text{Hands-on} + \text{Documentation}) + \text{Non-routine Hours}_{r} + \text{Support Hours}_{r}
```

```latex
\text{Required Review Hours} = \sum_{\text{rows}} \text{Review Events} \times \text{Review Time per Event}
```

Here g is an instrument group and r is a role and competency combination (for example, "HPLC-authorized analyst"). Review is kept as a separate resource because it is done by a smaller, specifically authorized group.

### 4.3 Test–method matrix (extract) \[H\]

Times are hours per test unit, with sequence or batch overhead allocated. Microbiology incubation is not labor and is shown as days of incubator occupancy. Annual hours are calculated in Appendix A.

| Product or Material | Sample Category | Test | Method | Laboratory Unit | Tests per Sample | Samples per Year | Annual Test Units | Instrument Required | Analyst Hands-on Time (h/unit) | Instrument Occupancy Time (h/unit) | Documentation and Review Time (h/unit) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Product A 10 mg tablets | FP release | Assay + related substances | QC-HPLC-012 | Chemical | 1 | 320 | 320 | HPLC (DAD) | 1.5 | 2.4 | 0.6 + 0.25 review |
| Product A 10 mg tablets | Stability | Assay + related substances | QC-HPLC-012 | Chemical | 1 | 180 | 180 | HPLC (DAD) | 1.5 | 2.4 | 0.6 + 0.25 review |
| Product A 10 mg tablets | FP release | Dissolution (6 vessels, UV finish) | PHY-DIS-004 | Physical | 1 | 320 | 320 | Dissolution bath + UV | 2.0 | 1.5 (bath) | 0.5 + 0.2 review |
| Product B oral solution | FP release | pH, density, appearance | PHY-GEN-001 | Physical | 3 | 150 | 450 | pH meter, densitometer | 0.3 | 0.1 | 0.1 + 0.05 review |
| API X | RM release | Identification | CHM-IR-002 | Chemical | 1 | 260 | 260 | FTIR | 0.5 | 0.3 | 0.2 + 0.1 review |
| API X | RM release | Residual solvents | GC-HS-005 | Chemical | 1 | 260 | 260 | GC + headspace | 0.8 | 1.8 | 0.4 + 0.2 review |
| Excipients (various) | RM release | ID and water content | Various (FTIR, KF) | Chemical | 2 | 900 | 1,800 | FTIR, KF titrator | 0.4 | 0.2 | 0.15 + 0.05 review |
| Product A 10 mg tablets | IPC | Hardness, weight variation, thickness | PHY-IPC-002 | Physical | 3 | 1,200 | 3,600 | Hardness/thickness tester, balance | 0.25 | 0.2 | 0.05 |
| Product B oral solution | FP release | TAMC/TYMC + specified organisms | MIC-MLT-003 | Microbiological | 2 | 150 | 300 | BSC; incubators | 1.5 | 5 d incubation | 0.4 + 0.2 review |
| Purified water | Routine monitoring | TAMC (membrane filtration) | MIC-WAT-001 | Microbiological | 1 | 2,600 | 2,600 | Filtration manifold; incubators | 0.35 | 5 d incubation | 0.1 + 0.03 review |
| Grade A/B areas (ophthalmic line) | EM | Settle, contact and active air plates | MIC-EM-002 | Microbiological | 1 (per plate) | 18,000 plates | 18,000 | Air sampler; incubators | 0.08 | 5 d (dual temperature) | 0.03 |
| Ophthalmic solution C | FP release | Sterility test (isolator) | MIC-STE-001 | Microbiological | 1 | 260 | 260 | Isolator; canisters; incubators | 4.0 | 1 session (5 h) + 14 d incubation | 0.8 + 0.3 review |
| Ophthalmic solution C | FP release | Bacterial endotoxins (kinetic) | MIC-BET-001 | Microbiological | 1 | 260 | 260 | Kinetic reader | 1.0 | 1.5 | 0.3 + 0.1 review |

The complete company model would contain every product × test × method row (typically several hundred). Section 5 and Section 6 totals are therefore larger than the sum of this extract.

### 4.4 Non-routine workload without double counting

Use one rule per workload type and apply it once.

| Workload type | Recommended estimation basis | Double-counting rule |
| --- | --- | --- |
| Repeat testing and invalid runs | Repeat rate per method from CDS/LIMS (e.g. 4% of sequences \[H\]) applied as a multiplier on that method's instrument and analyst time | Do not add again if historical method times already include repeats |
| Investigations (OOS, OOT, lab deviations) | Count per year × average hours per phase (e.g. Phase I lab investigation 12 h \[H\]); retesting hours go to the retest row | Investigation hours are labor only; retest instrument time is counted under the method multiplier or here, never both |
| Stability testing | Own matrix rows from the stability pull schedule, by month | Not part of release volumes; exclude stability from any "per batch" multiplier |
| Method validation, verification, transfer | Project list × estimated hours by phase (protocol, execution, report) | Planned projects only; unplanned work stays in investigations |
| Reference standards, reagents, solution prep, media prep | Own support rows (per batch of solution/media) or a percentage of testing time if no data exist | Exclude from per-test hands-on times if listed separately |
| Instrument housekeeping (column changes, performance checks) | Instrument "other unavailable hours" (Section 5) | Not counted as workload demand |
| Peaks | Monthly profile; capacity is checked against the peak month as well as the annual total | Peak is a check, not an addition to the annual figure |

### 4.5 Sequencing and batching effects (chromatography)

One HPLC sequence for QC-HPLC-012 \[H\] contains 2 equilibration/blank injections, 6 SST injections, 2 bracketing standards every 6 sample injections, and the sample injections, followed by a 1 h wash. At 30 min per injection, 6 samples in duplicate give 12 sample injections plus 12 overhead injections, plus equilibration and wash: about 14 h of occupancy. The same sequence with 12 samples (24 sample + 16 overhead injections) takes about 22 h. Per sample this is about 1.8 h instead of 2.4 h, but the batch must wait longer for samples to accumulate. The model must therefore record both the typical and the maximum practical batch size. It should also test whether larger batches would conflict with turnaround targets.

### 4.6 Microbiology-specific rules

- **Incubation is not labor.** Analyst time is counted only for set-up, observation points (for example day 3 and day 5 reads) and final reading. Each observation is a separate labor element of minutes per plate.
- **Incubators are capacity in shelf positions over time** (plate-days), not hours. See Appendix D.
- **Sterility tests occupy the isolator for a whole session**, including the decontamination cycle. Canisters then occupy incubator space for 14 days, with observation points during the period.
- **EM sampling time** includes gowning, travel and time in the cleanroom, and depends on production schedules and weekend coverage.
- **Controlled environments and segregation**: positive controls, growth promotion and identification work may need dedicated incubators or rooms. This reduces the capacity that can be pooled.

## 5. Instrument capacity and shortage assessment

In the hypothetical data, four equipment groups show a capacity gap by Y3: HPLC, dissolution, 30–35 °C incubators and the media autoclave. Four more are single points of failure without a capacity gap: GC headspace, FTIR, the sterility isolator and the endotoxin reader. The remaining groups have spare capacity.

### 5.1 Data captured per instrument or equipment group

For each item the register records: equipment type and ID; quantity installed and operational; age, condition and vendor support status; qualification and calibration status; scheduled operating hours; planned downtime; actual utilization (from CDS, audit trails or logbooks); required hours under baseline and forecast demand; backlog and turnaround impact; redundancy; compatibility with approved methods (configuration, detector, column oven, software version); and required additional capacity. The questionnaire (Section D) collects the item-level data. Appendix B holds the calculation sheets.

### 5.2 Calculation and planning limits

```latex
\text{Available Annual Instrument Hours} = \text{Scheduled Operating Hours} - \text{Planned Downtime} - \text{Other Unavailable Hours}
```

```latex
\text{Instrument Utilization (\%)} = \frac{\text{Required Instrument Hours}}{\text{Available Annual Instrument Hours}} \times 100
```

```latex
\text{Minimum Instruments} = \left\lceil \frac{\text{Required Hours}}{\text{Available Hours per Unit} \times \text{Planning Limit}} \right\rceil
```

A single utilization threshold is not appropriate for all equipment. The planning limit is the utilization above which turnaround and reliability degrade for that type of work.

| Equipment type | Planning limit \[A\] | Reason |
| --- | --- | --- |
| HPLC/UPLC (sequenced, overnight runs) | 80% | Long unattended runs absorb variation; still needs slack for repeats, priority samples and breakdowns |
| GC (incl. headspace) | 75% | Fewer units, longer method-specific set-up |
| Attended benchtop (dissolution, FTIR, KF) | 75% | Analyst must be present; campaign peaks; set-up between methods |
| Incubators (shelf positions) | 80% average, 95% peak month | Continuous operation; segregation needs; peaks from shutdowns and EM campaigns |
| Sterility isolator (sessions) | 70% | Decontamination cycles, glove and leak tests, requalification and urgent releases need reserve |
| Autoclave (cycles) | 75% | Media and decontamination loads compete; failed cycles must be repeated |

### 5.3 Instrument capacity table \[H\]

Available hours per unit: HPLC 5,000 − 240 planned − 500 other = 4,260 h. GC 5,000 − 200 − 500 = 4,300 h. Dissolution 2,500 − 60 − 190 = 2,250 h. Single-shift benchtop 2,000 − 100 − 100 = 1,800 h, except disintegration, hardness and viscometer 1,900 h (2,000 − 50 − 50). Forecast growth is +30% for Chemical, +25% for Physical and +20% for Microbiological equipment (sterility: 260 to 341 sessions, from the product plan).

| Instrument Category | Installed | Operational | Available Hours/Year | Required Hours/Year (Y0 → Y3) | Utilization (Y0 → Y3) | Forecast Gap | Recommended Action |
| --- | --- | --- | --- | --- | --- | --- | --- |
| HPLC/UPLC | 8 | 7 | 29,820 | 23,500 → 30,550 | 79% → 102% | 9 operational units needed at 80%; gap of 2 | Replace obsolete HPLC-05 (restores 4,260 h). Increase overnight sequences. Add a 9th system only if Y2 utilization is above 85% |
| GC (1 of 2 with headspace) | 2 | 2 | 8,600 (headspace: 4,300) | 3,900 → 5,070 (headspace: 2,400 → 3,120) | 45% → 59% (headspace 56% → 73%) | No capacity gap; redundancy gap | Add headspace sampler to GC-02 and validate GC-HS-005 on it |
| FTIR | 1 | 1 | 1,800 | 1,200 → 1,560 | 67% → 87% | Above 75% by Y2; single point of failure | Agree a backup ID route now (validated alternative or contract lab); second FTIR in Scenario C |
| UV-Vis | 2 | 2 | 3,600 | 900 → 1,170 | 25% → 33% | None | No action |
| Karl Fischer titrators | 3 | 3 | 5,400 | 1,900 → 2,470 | 35% → 46% | None | No action |
| Dissolution baths | 4 | 4 (1 out of vendor support) | 9,000 | 7,400 → 9,620 | 82% → 107% | 6 baths needed at 75%; gap of 2 | Add 1 bath with autosampler (Scenario B). Replace the 2009 bath (Y2). Second added bath only if the Y3 forecast is confirmed |
| Disintegration testers | 2 | 2 | 3,800 | 1,100 → 1,375 | 29% → 36% | None | No action |
| Hardness/thickness testers | 2 | 2 | 3,800 | 1,500 → 1,875 | 39% → 49% (peak month about 70%) | None | Schedule IPC around campaign peaks |
| Viscometer | 1 | 1 | 1,900 | 1,000 → 1,250 | 53% → 66% | Single point of failure (low volume) | Priority repair clause in the service contract |
| Sterility isolator (sessions) | 1 | 1 | 450 sessions | 260 → 341 sessions | 58% → 76% | Above 70% by Y3; single point of failure | Outsourced sterility backup contract; qualify more operators; feasibility study for a second isolator |
| Endotoxin kinetic reader | 1 | 1 | 1,800 | 390 → 470 | 22% → 26% | Single point of failure | Keep validated gel-clot backup and reagent stock |
| Incubators 30–35 °C (positions, routine) | 3 (1 kept for segregated work) | 3 | 1,000 positions | 863 → 1,036 average positions | 86% → 104% average; peak 108% → 130% | About 300 positions needed | Add one 500-position incubator |
| Incubators 20–25 °C (positions) | 2 | 2 | 1,000 positions | 603 → 724 | 60% → 72%; peak 75% → 90% | Watch | Review in Y2 |
| Media / decontamination autoclave (cycles) | 1 | 1 | 450 cycles | 380 → 456 cycles | 84% → 101% | Above 75% now; single point of failure | Buy ready-to-use media for high-volume plates; contract backup; second autoclave in Scenario C |

The simple annual-hour calculation is not enough in four situations, all present in this sample:

- **Specific configuration:** two HPLC methods \[H\] need UPLC pressure capability, and only 2 of 7 operational systems qualify. These methods must be modelled against those 2 systems, not the pool of 7.
- **Parallel processing:** stability pull clusters need several systems at once in the same week, even when the annual total fits.
- **Dedicated equipment:** the GC headspace unit and the incubator kept for segregated work cannot be pooled.
- **Urgent turnaround:** priority release samples need an available system within hours, which requires reserve capacity beyond the annual average.

### 5.4 Shortage classification

| Shortage type | Definition | Example in this sample \[H\] | Typical response |
| --- | --- | --- | --- |
| Capacity shortage | Required hours exceed available hours at the planning limit | HPLC and dissolution in Y3; 30–35 °C incubators at peak | Scheduling first, then added capacity |
| Reliability and redundancy shortage | Capacity is enough on average, but one failure stops a test | GC headspace, FTIR, isolator, endotoxin reader, autoclave | Backup method or contract lab; second unit only if risk justifies it |
| Qualification or compliance limitation | Equipment exists but is not qualified, overdue or out of support | HPLC-05 (obsolete, no parts); 2009 dissolution bath | Replacement or requalification |
| Technology or method compatibility gap | Equipment cannot run an approved method | UPLC-only methods limited to 2 systems | Targeted upgrade; method transfer or revalidation |
| Turnaround caused by workflow | Delay is in queues (review, sample receipt, scheduling), not equipment | Chemical data review queue (Section 6) | Process and authorization changes, not CAPEX |

## 6. Staffing capacity and shortage assessment

In the hypothetical data, total staff hours almost match demand at baseline: 44,300 required against 44,688 available. Yet three roles are short today (Chemical reviewers, Microbiology analysts, and supervisors with review duties), and HPLC, Physical and Microbiology analysts are short by Y3. The aggregate figure is misleading because hours cannot move freely between roles and method authorizations.

### 6.1 Staff capacity model

```latex
\text{Available Qualified Hours}_{r} = \text{Authorized Headcount}_{r} \times \text{Effective Productive Hours per FTE} \times \text{Allocation to Role}_{r}
```

```latex
\text{Required FTE}_{r} = \frac{\text{Total Required Annual Labor Hours}_{r}}{\text{Effective Annual Productive Hours per FTE}}
```

Effective productive hours are 1,520 h per FTE \[A\] (Section 2.6). Allocation to role applies where one person splits time. In this sample, reviewers spend 70% of their productive time on review and supervisors spend 50% \[A\]. The rest is supervision, training, investigations and meetings.

Required labor hours by role include:

- hands-on preparation and analysis;
- data processing and documentation (LIMS entry, worksheets, calculations);
- non-routine work (investigations, validations and transfers), assigned to the role that actually does it;
- support activities (solution and media preparation, reference standards, EM sampling);
- review and approval, held as its own role.

### 6.2 Staffing table \[H\]

Available hours = current authorized headcount × 1,520 h × role allocation. Gap = available FTE minus required FTE (negative = shortage).

| Laboratory Unit | Role | Current Headcount | Available Productive Hours | Required Hours (Y0 → Y3) | Calculated FTE Requirement (Y0 → Y3) | Estimated Gap (FTE, Y0 → Y3) | Competency Constraint | Recommendation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Chemical | Analyst, chromatography (HPLC/GC) | 8 (approved 10; 2 vacancies) | 12,160 | 11,400 → 14,800 | 7.5 → 9.7 | +0.5 → −1.7 | Only 3 of 8 authorized for GC-HS-005; 2 for UPLC methods | Fill 2 vacancies now (Y3 margin +0.3). Authorize 2 more on GC-HS and UPLC. +1 analyst in Scenario C |
| Chemical | Analyst, wet chemistry / spectroscopy | 4 + 1 temporary | 7,600 | 6,100 → 7,930 | 4.0 → 5.2 | +1.0 → −0.2 | Temporary analyst authorized for KF and wet chemistry only | Use the current surplus to cross-train 2 analysts on HPLC methods |
| Chemical | Senior analyst / data reviewer | 2 | 2,128 (70% allocation) | 3,400 → 4,420 | 2.2 → 2.9 (at full-time review) | −1,272 h → −2,292 h | Review authorization limited to 2 people | Authorize 2 senior analysts as reviewers (20% each, 608 h). Recruit 1 senior analyst/reviewer (Scenario B) |
| Physical | Analyst | 6 | 9,120 | 8,300 → 10,375 | 5.5 → 6.8 | +0.5 → −0.8 | Only 3 of 6 authorized for dissolution | Cross-train 2 analysts on dissolution now. +1 analyst in Scenario C |
| Physical | Supervisor / reviewer | 1 | 760 (50% allocation) | 900 → 1,125 | — | −140 h → −365 h | Sole approver | Delegate routine IPC review to 1 authorized senior analyst |
| Microbiological | Analyst | 8 (approved 9; 1 vacancy) | 12,160 | 13,100 → 15,720 | 8.6 → 10.3 | −0.6 → −2.3 | Only 2 qualified for isolator sterility testing; weekend EM rota needs 2 qualified staff | Fill vacancy now with an aseptically qualified candidate. Qualify 2 more isolator operators. +1 analyst (B), +1 (C) |
| Microbiological | Supervisor / reviewer | 1 | 760 (50% allocation) | 1,100 → 1,320 | — | −340 h → −560 h | Sole approver of sterility results | Authorize a second reviewer for EM and water data |
| **Total** |  | **30 + 1 temporary** | **44,688** | **44,300 → 55,690** |  |  |  |  |

The total row shows why headcount is not capacity. In aggregate, the labs appear 99% loaded at baseline with 388 spare hours. In reality, the Chemical reviewers carry a 1,272-hour shortfall while the wet chemistry group has a surplus it is not authorized to use on HPLC or review work.

### 6.3 Worked example — Chemical data review \[H\]

1. Review events per year: 2,600 HPLC/GC sequences and test sets, plus 3,000 short-test records.
2. Review time: 1.0 h per sequence and 0.27 h per short-test record. 2,600 × 1.0 + 3,000 × 0.27 = 2,600 + 810 = 3,410, rounded to 3,400 h.
3. Available: 2 reviewers × 1,520 h × 70% = 2,128 h.
4. Shortfall: 3,400 − 2,128 = 1,272 h, equal to about 0.84 FTE of full-time review.
5. Effect: the review queue grows by roughly 25 h per working week (1,272 h ÷ 50 weeks) \[H\]. It is currently absorbed by reviewer overtime and by data waiting 3–5 days for approval.
6. Option without hiring: authorize 2 senior HPLC analysts as reviewers at 20% each. This adds 608 h but removes the same hours from the HPLC analyst pool. That is affordable only once the 2 vacancies are filled. The residual gap of 664 h at Y0 rises by Y3, which justifies 1 dedicated senior reviewer in Scenario B.

### 6.4 Adjustments the simple FTE calculation needs

- **Specialized competencies:** calculate FTE per method family (HPLC, GC-HS, dissolution, isolator), not just per unit. A surplus in one family cannot cover a shortage in another until training is complete.
- **Workload peaks:** test the peak month at 1.25 × the average \[A\]. Physical lab IPC peaks reach about 1.4 × during campaigns \[H\].
- **Coverage:** weekend EM and water sampling need 2 qualified microbiologists every weekend day, about 104 days a year. That is a rota constraint even when annual hours fit.
- **Supervisory duties:** supervisors carry review, investigations, training and audits. Count only their testing or review share as capacity.
- **Non-transferable responsibilities:** sterility result approval, reference standard qualification and CDS administration need named, qualified people and at least one trained backup each.
- **Training of new recruits:** typical time to independent authorization \[A\] is 4–6 months for an HPLC analyst, 3–6 months for an isolator operator (including aseptic qualification), and 6–12 months for a data reviewer. During training, a recruit adds no capacity and uses about 15–20% of a trainer's time.
- **Single-person dependencies:** isolator sterility testing (2 people), GC-HS (3 people), sterility result approval (1 person), and CDS system administration (1 person, Chemical lab).

## 7. Combined capacity and bottleneck analysis

The Chemical Laboratory is the most constrained unit in this sample. Its review queue limits release turnaround today, and HPLC capacity will limit it from Y2. Microbiology is next, constrained by competency coverage and incubator space rather than total hours. The Physical lab's dissolution constraint is real by Y3, but part of it is a dependency on Chemical lab HPLC time for HPLC-finish methods.

### 7.1 Integrated findings \[H\]

| Question | Finding in this sample | Evidence still needed |
| --- | --- | --- |
| Most constrained units | Chemical (review now, HPLC from Y2); Microbiological (sterility competency, incubators at peak) | Queue ageing by step from LIMS timestamps |
| Methods with the highest workload | QC-HPLC-012 assay/RS (release + stability) is about 5% of HPLC hours in the extract alone; EM plates are the largest microbiology labor item | Full matrix ranking by hours |
| Equipment shared by multiple methods | HPLC pool (about 40 methods \[H\]); dissolution baths (12 methods); 30–35 °C incubators (EM, water, MLT) | Method–instrument assignment list |
| Work waiting for analysts | Chemical data review; dissolution testing when only 3 authorized analysts are present | Queue time per step, analyst rota |
| Work delayed by instrument availability | HPLC in stability pull weeks; isolator when decontamination cycles collide with urgent release | CDS idle versus queued time; isolator log |
| Dependencies between units | HPLC-finish dissolution (Physical → Chemical); reference standards (Chemical → Physical); microbiology result sets the final release date for liquids and steriles | Release timeline analysis per product |
| Peak workload periods | Q4 production campaign (+25–40% IPC and release); stability pull clusters in Jan, Apr, Jul, Oct; annual shutdown EM | Monthly volumes for 24 months |
| Critical activities with no qualified backup | Sterility result approval (1 person); CDS administration (1 person); GC headspace unit; media autoclave | Competency matrix; equipment register |
| Impact on release, stability, investigations, turnaround | Median release turnaround 9 working days against a 7-day target \[H\]; 4% of stability pulls tested outside the protocol window \[H\]; investigations average 34 days against a 30-day target \[H\] | LIMS turnaround by product; stability compliance report; QA investigation ageing |

### 7.2 Bottleneck table \[H\]

| Constraint | Root Cause (hypothesis) | Supporting Metric | Operational Impact | Short-Term Mitigation | Long-Term Solution |
| --- | --- | --- | --- | --- | --- |
| Chemical data review | Only 2 authorized reviewers; review time per sequence high because of manual audit-trail checks | 3,400 h required vs 2,128 h available; data waits 3–5 days for review | Release turnaround above target; reviewer overtime; risk of rushed review | Authorize 2 senior analysts as reviewers; daily review slot; prioritize release over stability | 1 senior reviewer; review-by-exception tools in CDS; audit-trail review procedure |
| HPLC capacity (Y2–Y3) | Growth +30%; 1 system out of service; overnight sequences used on about half of nights | 79% → 102% utilization; queue during stability pull weeks | Missed stability windows; release delays at peaks | Plan stability pulls across weeks; run overnight sequences every night; larger batches where turnaround allows | Replace HPLC-05; 9th system if trigger met; consider UPLC transfer of long methods |
| Dissolution capacity | Growth +25%; 3 of 6 analysts authorized; 1 bath out of support | 82% → 107% utilization; IPC peaks 1.4 × average | Batch release waits for dissolution in campaign months | Cross-train 2 analysts; extend bath hours to 10 h a day; schedule IPC pulls | 1 bath with autosampler; replace 2009 bath |
| Sterility testing coverage | 2 qualified operators; single isolator | 58% → 76% of sessions; 2 qualified people | Release of the ophthalmic line stops when either operator is absent | Outsourced backup contract; qualify 2 more operators | Feasibility study for a second isolator if the sterile portfolio grows |
| 30–35 °C incubator space | EM, water and MLT share 1,000 positions; 1 unit kept for segregated work | 86% average, 108% peak month | Plates double-stacked or work deferred in peak months | Stagger EM campaigns; tighten plate-removal discipline after final read | 1 additional incubator |
| Media autoclave | 1 unit for media and decontamination | 84% of cycles now; 101% by Y3 | Media shortages delay MLT and EM | Ready-to-use media for high-volume plates; contract backup sterilization | Second autoclave (Scenario C) |

A utilization figure shows where to look. It does not prove a cause. High HPLC utilization could come from real demand, from long or inefficient methods, from repeat runs, or from systems left idle between short sequences while still "booked". Each hypothesis above must be confirmed before investment with: queue time per workflow step (receipt, preparation, instrument, review, approval) from LIMS/CDS timestamps; repeat and invalid run rates per method; booked versus actual run time; staff rota against queue; and 2–4 weeks of timed observation for the top 10 methods.

## 8. CAPEX assessment and investment plan

The illustrative register totals **330 k HCU for Scenario B items** and **556 k HCU for the further Scenario C items**. With a 10% contingency \[A\], that is 363 k HCU and 612 k HCU, or 975 k HCU for both. All costs are hypothetical placeholders, not supplier quotations.

### 8.1 CAPEX register \[H\]

| Investment Item | Laboratory Unit | Justification | Quantity | Unit Cost (k HCU) | Installation and Qualification Cost (k HCU) | Total Estimated CAPEX (k HCU) | Expected Capacity Gain | Priority | Dependencies |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 HPLC system (quaternary pump, DAD, autosampler) replacing HPLC-05 | Chemical | Obsolete, out of service, no parts; utilization 79% → 102% | 1 | 85 | 15 (IQ/OQ/PQ) | 100 | Restores 4,260 h/yr | B — High | C5; method equivalency check for assigned methods |
| C2 Headspace autosampler for GC-02 | Chemical | Single point of failure for residual solvents | 1 | 40 | 8 | 48 | Second qualified headspace route (4,300 h/yr availability) | B — High | GC-HS-005 validated on GC-02 (C7) |
| C3 Dissolution bath, 8 vessels, with autosampler | Physical | 82% → 107% utilization | 1 | 70 | 12 (incl. mechanical qualification) | 82 | +2,250 h/yr (more if run unattended) | B — High | Bench space; method verification on new bath |
| C4 Incubator 30–35 °C, about 500 positions | Microbiological | 86% average, 108% peak occupancy | 1 | 18 | 6 (temperature mapping, OQ/PQ) | 24 | +500 positions | B — High | Power supply; monitoring system connection |
| C5 CDS licence and computerized-system validation for C1 | Chemical | Data integrity; audit trail; access control | 1 | 6 | 5 (CSV) | 11 | Enables C1 | B — High | IT; CSV procedure |
| C6 Network connection of standalone instruments (UV, KF, FTIR) to a central data server | Chemical / Physical | Audit-trail and raw data retention gaps on standalone systems | 1 package | 30 | 5 (CSV) | 35 | Compliance; review time saving to be measured (estimate about 150 h/yr) | B — High (compliance) | IT infrastructure; supplier software versions |
| C7 Training, method transfer and validation (B items) | All | Method verification on C1 and C3; GC-HS-005 validation on GC-02; operator training | 1 | 30 | — | 30 | Needed to make B items usable | B — High | C1–C4 installed |
| **Subtotal Scenario B** |  |  |  |  |  | **330** |  |  |  |
| C8 Additional HPLC system | Chemical | Y3 forecast 102% even with C1 | 1 | 85 | 15 | 100 | +4,260 h/yr | C — Trigger: Y2 utilization above 85% | C9; bench and utilities (C14) |
| C9 CDS licence and CSV for C8 | Chemical | As C5 | 1 | 6 | 5 | 11 | Enables C8 | C | C8 |
| C10 Second FTIR | Chemical | 67% → 87%; single point of failure for raw material ID | 1 | 45 | 8 | 53 | +1,800 h/yr; redundancy | C — Medium | Spectral library transfer |
| C11 Replacement of the 2009 dissolution bath | Physical | Out of vendor support | 1 | 45 | 10 | 55 | None (reliability) | C — Medium (Y2) | Method verification |
| C12 Second additional dissolution bath | Physical | Y3 forecast needs 6 baths | 1 | 70 | 12 | 82 | +2,250 h/yr | C — Trigger: Y3 volumes confirmed | Bench space (C14) |
| C13 Second autoclave (media) | Microbiological | 84% → 101% of cycles; single point of failure | 1 | 120 | 25 (IQ/OQ/PQ, load mapping) | 145 | +450 cycles/yr; redundancy | C — Medium-High | Steam, drainage and room (C14) |
| C14 Laboratory refurbishment and utilities | Chemical / Microbiological | Space, power, exhaust, steam and drainage for C8, C12 and C13 | 1 | 60 | — | 60 | Enables C8, C12, C13 | C | Engineering survey |
| C15 Training, method transfer and validation (C items) | All | As C7 | 1 | 25 | — | 25 | Needed to make C items usable | C | C8–C13 |
| C16 Feasibility study for a second sterility isolator | Microbiological | Isolator 76% by Y3; single point of failure | 1 | 25 | — | 25 | Decision input only | C — Medium | Sterile portfolio plan |
| **Subtotal Scenario C items** |  |  |  |  |  | **556** |  |  |  |
| Contingency 10% \[A\] | All | Price, scope and qualification uncertainty | — | — | — | 33 (B) + 56 (C) | — | — | — |
| **Total incl. contingency** |  |  |  |  |  | **363 (B); 975 (B + C)** |  |  |  |

C7 and C15 (training, method transfer, validation) may be booked as OPEX under the company's accounting policy. They are shown here because they are one-time implementation costs of the investment.

### 8.2 From budgetary estimate to approved investment

Every figure above is a budgetary placeholder \[H\]. Before approval, each item needs:

1. A user requirement specification (URS) tied to the approved methods it must run.
2. At least two supplier quotations, including delivery lead time (often 3–9 months for analytical systems, longer for autoclaves and isolators \[A\]).
3. Installation requirements: space, power, gases, exhaust, steam, network, and an Engineering estimate.
4. Qualification and validation scope (IQ/OQ/PQ, CSV, temperature mapping) and its cost.
5. Data integrity requirements: audit trail, user management, backup and archiving.
6. Procurement information: framework agreements, currency and taxes.
7. Recurring costs (service contract, consumables, licences) for Section 9.

## 9. OPEX and financial considerations

In this sample, recurring OPEX outweighs CAPEX within about three years. Scenario B adds about 165 k HCU a year against 363 k HCU of CAPEX, and 125 k HCU of that is staff. Investment decisions should therefore be compared on total cost over the planning horizon, not on purchase price.

### 9.1 OPEX elements and how to collect them

| Cost element | One-time or recurring | Source | Illustrative basis \[H\] |
| --- | --- | --- | --- |
| Consumables and reagents (columns, solvents, vials, filters) | Recurring | Purchasing history per cost centre; usage per method | About 12 k HCU/yr per fully used HPLC; 4 k HCU/yr per dissolution bath |
| Reference standards | Recurring | Standards register; pharmacopoeial and secondary standard purchases | Driven by methods, not instruments; changes with new products |
| Microbiological media and ready-to-use plates | Recurring | Media prep records; supplier invoices | Ready-to-use plates cost more per plate but save autoclave cycles and labor |
| Service and maintenance contracts | Recurring | Contracts register | About 7–8% of purchase price per year \[A\] |
| Calibration and qualification (external) | Recurring | Metrology schedule; vendor PQ invoices | Per instrument per year |
| Utilities and environmental controls | Recurring | Engineering allocation | Relevant for autoclaves, incubators and HVAC changes |
| Software licences and support | Recurring | IT | CDS licence support about 1.5 k HCU/yr per connection |
| Training | One-time per person, plus recurring refresher | Training plan | About 6 k HCU per new hire (trainer time and courses) |
| Recruitment | One-time | HR | About 8 k HCU per hire |
| Personnel | Recurring | HR / Finance (loaded cost) | Analyst 55 k HCU/yr; senior analyst/reviewer 70 k HCU/yr |
| Overtime | Recurring | Payroll | Current reviewer and microbiology overtime |
| Outsourced testing | Recurring | Contract lab invoices | Sterility backup retainer 15 k HCU/yr plus a per-test fee; identifications |

### 9.2 Incremental annual OPEX by scenario \[H\]

Incremental to the current approved budget. Filling the 3 approved vacancies (about 165 k HCU/yr) is already budgeted and is not counted again.

| Element (k HCU/yr) | Scenario A | Scenario B | Scenario C (cumulative) |
| --- | --- | --- | --- |
| Additional staff above approved headcount | 0 | 125 (1 senior reviewer, 1 microbiology analyst) | 290 (B + 3 analysts) |
| Overtime | 20 | 0 | 0 |
| Service, support and licences for new equipment | 0 | 15 | 40 |
| Consumables for added capacity | 0 | 4 | 20 |
| Outsourced sterility backup retainer | 15 | 15 | 15 |
| Scheduling / workload visibility tool | 5 | 5 | 5 |
| **Total recurring** | **40** | **164 (about 165)** | **370** |
| One-time OPEX (recruitment, training) | 15 (cross-training) | 28 | 70 |

### 9.3 Comparison of options

| Option | Typical use in this sample | Cost profile | Main limitation |
| --- | --- | --- | --- |
| 1. Existing-resource optimization | Review authorization, overnight sequences, stability pull levelling, IPC scheduling | Low CAPEX and OPEX | Does not close Y3 HPLC and dissolution gaps |
| 2. Recruitment or cross-training | Reviewers, dissolution and isolator competencies | Recurring personnel cost; 3–12 months to become effective | Needs trainer time and suitable candidates |
| 3. Additional instruments | Dissolution, incubator, HPLC (conditional) | CAPEX plus 7–8%/yr service plus consumables | Space, qualification, and needs authorized analysts to run them |
| 4. Equipment replacement | HPLC-05, 2009 dissolution bath | CAPEX; no capacity gain beyond restoring the original | Method equivalency work |
| 5. Outsourcing selected tests | Sterility overflow and backup; identifications; peak residual solvents | Per-test fee; no CAPEX | Contract lab qualification, sample logistics, turnaround, oversight workload |
| 6. Combined solution | Scenario B | Balanced | Needs coordinated scheduling of hiring, delivery and qualification |

### 9.4 Cost-per-test, payback and ROI — assumptions and limits

```latex
\text{Cost per Test} = \frac{\text{Annualized CAPEX} + \text{Annual OPEX (labor, service, consumables, utilities)}}{\text{Annual Test Units}}
```

Annualized CAPEX = purchase plus qualification cost ÷ useful life (for example 10 years \[A\]), or an annuity at the company's cost of capital.

**Worked comparison — sterility overflow \[H\].** By Y3, 341 sessions exceed the 70% isolator limit (315 sessions) by about 26, or about 30 tests a year allowing for peaks. Outsourcing these at 0.6 k HCU per test plus the 15 k HCU retainer costs about 33 k HCU/yr. A second isolator would need a CAPEX in the order of several hundred k HCU (to be set by the C16 feasibility study), plus room, qualification, operators and about 30 k HCU/yr service. On these placeholder figures outsourcing is cheaper. A second isolator would only become justified by a larger sterile portfolio or by a turnaround or supply-risk requirement that outsourcing cannot meet.

Limits of these calculations:

- No financial benefit is claimed unless an explicit model links the investment to a measurable cost avoided (overtime, outsourcing fees, stock held awaiting release) or revenue protected. In this sample those benefits are not quantified.
- Cost per test depends heavily on volume assumptions. Utilization below plan raises it sharply.
- Compliance-driven items (data integrity, replacement of unsupported equipment) are justified by risk, not payback, and should not be ranked on ROI.
- Release delay costs (inventory carrying cost, missed shipments) can be large but must come from Supply Chain and Finance, not from QC estimates.

## 10. Scenarios and recommendations

The recommendation in this sample is Scenario A immediately, then Scenario B released item by item once verified data confirm each gap. Scenario C items are held behind demand triggers. Scenario A alone leaves HPLC at 102% and dissolution at 107% by Y3. Scenario B brings both below 100% but still above their planning limits. Scenario C is needed only if the Y3 forecast is confirmed.

### 10.1 Scenario definitions

**Scenario A — Optimize existing resources.** Authorize 2 senior analysts as Chemical reviewers. Run overnight HPLC sequences every night. Level stability pulls across weeks. Schedule IPC around campaigns. Cross-train 2 wet chemistry analysts on HPLC, 2 Physical analysts on dissolution and 2 microbiologists on isolator sterility testing. Fill the 3 approved vacancies. Introduce a shared scheduling board for instruments and reviews. Set up an outsourced sterility backup contract and buy ready-to-use media for high-volume plates.

**Scenario B — Targeted capacity expansion.** Scenario A, plus CAPEX items C1–C7: HPLC-05 replacement, GC-02 headspace, one dissolution bath with autosampler, one incubator, CDS/CSV, and data integrity connection of standalone instruments. Recruit 1 senior Chemical reviewer and 1 microbiology analyst.

**Scenario C — Forecast-based expansion.** Scenario B, plus items C8–C16: 9th HPLC, second FTIR, dissolution bath replacement and expansion, second autoclave, utilities and refurbishment, and an isolator feasibility study. Recruit 1 more analyst each in the Chemical, Physical and Microbiological labs. Long-lead items (autoclave, utilities) must start 12–18 months before the capacity is needed.

### 10.2 Scenario comparison \[H\]

| Criterion | Scenario A — Optimize | Scenario B — Targeted expansion | Scenario C — Forecast-based expansion |
| --- | --- | --- | --- |
| Estimated CAPEX (incl. 10% contingency) | 0 | 363 k HCU | 975 k HCU (cumulative) |
| Annual OPEX (incremental) | 40 k HCU | 165 k HCU | 370 k HCU |
| Additional FTE (above approved) | 0 (3 vacancies filled) | +2 | +5 |
| Expected capacity at Y3 demand | HPLC 102%; dissolution 107%; incubators 104%; review gap about −1,700 h | HPLC 90%; dissolution 86%; incubators 69%; review gap about −390 h | HPLC 80%; dissolution 71%; incubators 69%; autoclave 51%; review gap closed with process changes |
| Implementation time | 0–3 months (training effect 3–6 months) | 6–12 months | 12–24 months |
| Key risks | Gains not sustained; Y3 shortfall; burnout from overtime | Hiring delays; qualification slippage; still little reserve for peaks | Over-capacity if the forecast does not materialize; facility work disrupts testing |
| Advantages | Fast, cheap, reversible; produces better data for B and C | Closes current and near-term gaps; removes key single points of failure | Covers the full forecast with reserve; resilient |
| Limitations | Cannot create instrument hours beyond the installed base | HPLC and dissolution remain above planning limits in Y3 | Highest cost; depends on forecast accuracy |

### 10.3 Ranked recommendations \[H\]

Ranking considers urgency, compliance impact, operational impact and investment requirement, in that order.

| Rank | Action | Urgency | Compliance impact | Operational impact | Investment | Timing |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Collect and verify data (questionnaire plus central records) before committing CAPEX | High | Medium | Enables all decisions | Low (internal time) | Immediate |
| 2 | Authorize additional Chemical reviewers; set a daily review slot | High | Medium (review quality) | High (release turnaround) | None | Immediate |
| 3 | Fill the 3 approved vacancies; qualify 2 more isolator operators | High | High (sterility coverage) | High | Budgeted | Immediate |
| 4 | Outsourced sterility backup contract; ready-to-use media | High | High (business continuity) | Medium | 15 k HCU/yr plus fees | Immediate |
| 5 | Connect standalone instruments to a central data server (C6) | Medium | High (data integrity) | Low | 35 k HCU | Medium term (0–12 months) |
| 6 | Replace HPLC-05 (C1, C5) | High | Medium (unsupported equipment) | High | 111 k HCU | Medium term |
| 7 | GC-02 headspace (C2) | Medium | Low | High (single point of failure) | 48 k HCU | Medium term |
| 8 | Dissolution bath with autosampler (C3); incubator (C4) | Medium | Low | High | 106 k HCU | Medium term |
| 9 | Recruit senior Chemical reviewer and microbiology analyst | Medium | Medium | High | 125 k HCU/yr | Medium term |
| 10 | Scenario C items, released by trigger (Section 11.3) | Low until triggered | Varies | High at Y3 | 612 k HCU | Long term (12–36 months) |

No purchase should be committed on the basis of this sample. Ranks 5–9 are proposals to verify, and rank 10 depends on confirmed demand.

## 11. Implementation roadmap

The roadmap runs about 18 months from data collection to verified results. No equipment is specified or ordered before data are verified (G1) and management approves (G2). Scenario A actions and filling approved vacancies start in week 1 because they need no investment decision.

&#91;embedded content: Implementation roadmap · 7 phases, 3 gates, parallel staffing stream \[H timings\]\]

Timings are illustrative \[A\]. Supplier lead times, facility work and recruitment markets set the real dates.

### 11.1 Phase deliverables

| Phase | Main deliverable | Responsible |
| --- | --- | --- |
| Data collection and verification | Completed questionnaires; central data extracts; validation log of discrepancies | QC unit heads; QC systems; HR; Planning |
| Workload and capacity calculations | Consolidated model; gap table with confidence levels | Central QC planning / project lead |
| Technical review by unit heads | Signed-off workload, capacity and gap figures per unit | Unit heads |
| Finance and procurement review | Budgetary quotations; total cost of ownership; scenario recommendation | Finance; Procurement; QC head |
| Management approval (G2) | Approved CAPEX, OPEX and headcount by item | Site leadership |
| Specifications and purchasing | URS per item; supplier selection; purchase orders | QC; Engineering; Procurement |
| Facility preparation and installation | Utilities and space ready; installed equipment (IQ) | Engineering |
| Qualification and validation (G3) | OQ/PQ, CSV, mapping, method verification reports; equipment released | QC; QA; Validation |
| Staff recruitment and training | Hires on board; training and authorization records | HR; unit heads |
| Post-implementation verification | KPI report against baseline and targets | QC head; QA |

### 11.2 Performance indicators \[H targets\]

| Indicator | Definition | Baseline \[H\] | Target \[H\] |
| --- | --- | --- | --- |
| Release turnaround time | Working days from sample receipt to QC approval, median and 90th percentile | 9 days median | 7 days median |
| Backlog | Samples or tests past their due date at month end | 140 tests | Below 50 tests |
| Review queue age | Working days from data complete to review complete | 3–5 days | 1–2 days |
| Instrument availability | Available hours ÷ scheduled hours, per group | HPLC 85% | Above 90% |
| Utilization | Required ÷ available hours, per group | Section 5 | Below planning limit |
| Repeat testing rate | Repeated sequences or tests ÷ total | 4% | Below 3% |
| Overdue maintenance and calibration | Items past due date | 3 | 0 |
| Qualified staff coverage | Critical methods with at least 2 authorized analysts ÷ critical methods | 70% | 100% |
| Stability pull compliance | Pulls tested within the protocol window | 96% | Above 99% |
| Investigation closure time | Days from opening to closure, lab investigations | 34 days | 30 days or less |

### 11.3 Triggers that release Scenario C items

- **9th HPLC (C8):** HPLC utilization above 85% for 3 consecutive months after HPLC-05 is replaced, or a confirmed launch adding more than 3,000 HPLC hours a year \[H\].
- **Second dissolution bath (C12):** dissolution utilization above 80% for 3 months after C3 is installed and 5 analysts are authorized.
- **Second autoclave (C13):** media and decontamination cycles above 85% after ready-to-use media are introduced, or two unplanned outages in 12 months.
- **Second isolator (C16 outcome):** sterile portfolio growth beyond the Y3 forecast, or outsourced turnaround that fails release targets.

## 12. Limitations and data validation

This sample cannot support a purchase decision. Every finding rests on \[H\] and \[A\] values. In a real assessment, the findings that drive money must be verified first and given a confidence level.

### 12.1 Limitations of an assessment based on incomplete or estimated data

- **Self-reported times** may be off by 20–40%. Hands-on and review times are often underestimated and instrument times overestimated.
- **Hidden work** (solution preparation, LIMS entry, reference standards, cleaning, logbooks) is often missing from method times. Leaving it out can understate labor need by 10–20% \[A\].
- **Annual averages** hide peak months, and peaks drive turnaround.
- **Booked versus used** instrument time: scheduling systems record bookings, not actual runs. CDS audit trails are more reliable.
- **Forecasts** carry production-plan uncertainty. A ±15% change in volume moves HPLC from 102% to between 87% and 118% in Y3 \[H\].
- **Non-routine workload** (investigations, transfers) varies a lot from year to year. Use at least 2 years of history.
- **Competency data** may not match reality if authorization records are not maintained.
- **Costs** are placeholders until quoted.

### 12.2 Findings that require verification before an investment decision \[H\]

| Finding | Verification needed | Source | Confidence now | Confidence required |
| --- | --- | --- | --- | --- |
| HPLC utilization 79% → 102% | 12 months of CDS run logs; method–instrument assignment; repeat rate | CDS audit trail; LIMS | Low | High before C8; Medium before C1 |
| HPLC-05 cannot be repaired | Vendor end-of-support letter; repair history | Engineering; vendor | Medium | High |
| Dissolution utilization 82% → 107% | Bath logbooks; runs per month; peak profile | Logbooks; LIMS | Low | High before C3 |
| Review shortfall of 1,272 h | Review timestamps; review events per year; time study | LIMS/CDS; observation | Low | Medium before hiring |
| Incubator peak 108% | Incubator loading records; EM plan; plate counts per month | Microbiology records | Low | Medium before C4 |
| Sterility demand 260 → 341 sessions | Sterile batch plan; sessions per batch | Planning; Microbiology | Low | High before C16 |
| Effective hours 1,520 per FTE | HR absence data; time-allocation survey | HR; questionnaire | Low | Medium |
| Forecast growth rates | Approved production plan; launch plan | Planning; Portfolio | Low | High before any Scenario C item |
| Costs | Supplier quotations; Engineering estimates | Procurement | None | Quotation-based |

**Confidence levels.** *High*: from system records, reconciled across sources. *Medium*: from records with gaps, or from a time study on a sample of runs. *Low*: an estimate or opinion with no supporting record.

### 12.3 Validation steps for collected data

1. Cross-check questionnaire volumes against LIMS sample counts (tolerance ±10% \[A\]).
2. Cross-check instrument hours against CDS or audit-trail run times.
3. Reconcile analyst hours: the sum of allocated hours per person must not exceed their productive hours.
4. Check that review and testing hours are not counted twice.
5. Check stability rows against the stability protocol register.
6. Confirm competency claims against training and authorization records.
7. Record every discrepancy and its resolution in a validation log.

## 13. Appendices

All appendix values are \[H\] and continue the worked examples in Sections 4–6.

### Appendix A — Test–method workload calculation (extract) \[H\]

Analyst hours = Annual Test Units × (hands-on + documentation). Review hours are a separate resource. Instrument figures are hours unless stated otherwise.

| Row | Product / test | Annual Test Units | Hands-on h | Documentation h | Analyst h total | Review h | Instrument occupancy |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R1 | Product A release — assay/RS | 320 | 480 | 192 | 672 | 80 | 768 h HPLC |
| R2 | Product A stability — assay/RS | 180 | 270 | 108 | 378 | 45 | 432 h HPLC |
| R3 | Product A release — dissolution | 320 | 640 | 160 | 800 | 64 | 480 h dissolution bath |
| R4 | Product B — pH, density, appearance | 450 | 135 | 45 | 180 | 23 | 45 h pH meter / densitometer |
| R5 | API X — FTIR identification | 260 | 130 | 52 | 182 | 26 | 78 h FTIR |
| R6 | API X — residual solvents | 260 | 208 | 104 | 312 | 52 | 468 h GC headspace |
| R7 | Excipients — ID and water content | 1,800 | 720 | 270 | 990 | 90 | 360 h FTIR / KF |
| R8 | Product A IPC — hardness, weight, thickness | 3,600 | 900 | 180 | 1,080 | — (in IPC record) | 720 h tester / balance |
| R9 | Product B — TAMC/TYMC + specified organisms | 300 | 450 | 120 | 570 | 60 | 300 tests × 5 d incubation |
| R10 | Purified water — TAMC | 2,600 | 910 | 260 | 1,170 | 78 | 2,600 plates × 5 d |
| R11 | Grade A/B EM plates | 18,000 | 1,440 | 540 | 1,980 | — (in batch EM review) | 18,000 plates × 5 d |
| R12 | Ophthalmic C — sterility | 260 | 1,040 | 208 | 1,248 | 78 | 260 isolator sessions + 14 d incubation |
| R13 | Ophthalmic C — endotoxins | 260 | 260 | 78 | 338 | 26 | 390 h kinetic reader |
| **Total (extract)** |  |  | **7,583** | **2,317** | **9,900** | **622** |  |

The extract covers about 22% of the 44,300 baseline analyst hours. The full matrix also includes the remaining products, support rows and non-routine rows from Section 4.4.

### Appendix B — Instrument capacity calculation sheets \[H\]

**B1. HPLC/UPLC (per operational system)**

| Line | Item | Hours |
| --- | --- | --- |
| 1 | Scheduled operating hours (20 h × 250 days) | 5,000 |
| 2 | Preventive maintenance (2 visits × 24 h) | 48 |
| 3 | Monthly performance checks and calibration (12 × 4 h) | 48 |
| 4 | Requalification (annual / after repair) | 40 |
| 5 | CDS and software maintenance windows | 24 |
| 6 | Site shutdown | 80 |
| 7 | **Planned downtime (2–6)** | **240** |
| 8 | Column changes and equilibration outside sequences | 150 |
| 9 | Unplanned repairs and troubleshooting | 250 |
| 10 | Priming, mobile phase changeover, gaps between sequences | 100 |
| 11 | **Other unavailable (8–10)** | **500** |
| 12 | **Available hours per system (1 − 7 − 11)** | **4,260** |
| 13 | Operational systems | 7 |
| 14 | **Available hours, group** | **29,820** |

**B2. HPLC required hours**

| Component | Y0 hours | Y3 hours (× 1.30) |
| --- | --- | --- |
| Routine release and raw material testing | 13,200 | 17,160 |
| Stability | 6,300 | 8,190 |
| Dissolution HPLC finish (for Physical lab) | 1,800 | 2,340 |
| Method validation and transfer | 1,250 | 1,625 |
| Repeat and invalid runs (4% of routine) | 950 | 1,235 |
| **Total** | **23,500** | **30,550** |
| Utilization (÷ 29,820) | 79% | 102% |
| Minimum systems at 80% (÷ \[4,260 × 0.80 = 3,408\]) | 6.9 → 7 | 8.96 → 9 |

**B3. Dissolution bath (per bath):** scheduled 2,500 h; planned downtime 60 h (mechanical qualification 2 × 16 h, preventive maintenance 16 h, temperature and speed calibration 12 h); other unavailable 190 h. Available 2,250 h × 4 baths = 9,000 h. Required 7,400 h (Y0) → 9,620 h (Y3). At a 75% limit: 9,620 ÷ (2,250 × 0.75 = 1,688) = 5.7 → 6 baths.

**B4. Sterility isolator:** 250 days × 2 sessions = 500 sessions, less 50 sessions for glove integrity tests, decontamination cycle checks, preventive maintenance and requalification = 450. Required 260 → 341. Utilization 58% → 76%; the 70% limit equals 315 sessions.

**B5. Media / decontamination autoclave:** 250 days × 2 cycles = 500, less 50 for maintenance, requalification and failed cycles = 450 cycles. Required 380 (260 media + 120 decontamination) → 456 (Y3). Utilization 84% → 101%.

### Appendix C — Staff capacity calculation sheets \[H\]

**C1. Effective productive hours per FTE**

| Item | Hours |
| --- | --- |
| Gross contracted (250 days × 8 h) | 2,000 |
| Annual leave | −200 |
| Sickness and other absence | −64 |
| Training | −60 |
| Meetings, administration, housekeeping | −156 |
| **Effective productive hours** | **1,520** |

**C2. Microbiology analyst required hours (Y0)**

| Activity | Hours |
| --- | --- |
| EM and personnel monitoring (sampling, reading, data entry) | 4,600 |
| Water microbiology | 1,900 |
| Microbial limits testing | 1,200 |
| Sterility testing | 1,400 |
| Bacterial endotoxins | 450 |
| Media preparation and growth promotion | 1,800 |
| Excursion investigations and OOS | 650 |
| Identification handling (outsourced samples, results) | 300 |
| Validation, method verification and other projects | 800 |
| **Total** | **13,100** |
| Required FTE (÷ 1,520) | 8.6 |
| Available (8 × 1,520) | 12,160 h = 8.0 FTE |
| Gap | −0.6 FTE |

Coverage check: weekend EM and water sampling needs 2 qualified analysts on about 104 weekend days, about 4 h each \[H\], or 832 h a year. These hours are included above, but the rota needs at least 6 analysts qualified for weekend work to keep each person to about 1 weekend in 3.

**C3. Chemical reviewer** — see Section 6.3.

### Appendix D — Microbiology incubator and facility capacity \[H\]

Incubator capacity is measured in shelf positions occupied over time:

```latex
\text{Average Positions Occupied} = \frac{\text{Plates per Year} \times \text{Average Incubation Days}}{365}
```

| Incubator group | Positions available | Plates per year (Y0 → Y3) | Average incubation days | Average positions (Y0 → Y3) | Average occupancy | Peak month (× 1.25) |
| --- | --- | --- | --- | --- | --- | --- |
| 30–35 °C routine (2 of 3 units) | 1,000 | 70,000 → 84,000 | 4.5 | 863 → 1,036 | 86% → 104% | 108% → 130% |
| 20–25 °C | 1,000 | 40,000 → 48,000 | 5.5 | 603 → 724 | 60% → 72% | 75% → 90% |
| Segregated unit (GPT, positive controls, sterility canisters) | 500 (third 30–35 °C unit) | Sterility: 260 tests × 2 canisters × 14 d = 7,280 canister-days | 14 | about 20 canisters + GPT load | Not pooled | — |

With one additional 500-position incubator (C4), routine 30–35 °C capacity becomes 1,500 positions: 69% average and 86% peak at Y3 demand.

Facility constraints are recorded qualitatively unless surveyed: biosafety cabinet slots, cleanroom access windows set by production, the isolator room, the media preparation area and segregation of positive-control work.

### Appendix E — Minimum company data required

The minimum data needed to turn this sample into a company-specific assessment:

1. Product and material list by unit, with sample categories (RM, packaging, IPC, FP, stability, EM, water, cleaning).
2. Approved specifications and the test–method list per product and material, with method IDs.
3. 24 months of LIMS sample and test counts by month, product, test and unit.
4. Stability protocol register and the 3-year pull schedule.
5. EM and water monitoring plans (locations, frequencies, plates per session).
6. Approved production plan and launch plan for Y1–Y3.
7. Method time standards (hands-on, instrument, documentation, review) for the top methods by volume, verified by timed observation or CDS data.
8. Typical and maximum batch or sequence sizes, and repeat or invalid run rates per method.
9. Equipment register: ID, type, model, installation year, status, qualification and calibration dates, service contract, support end date.
10. 12 months of instrument run hours (CDS audit trails, logbooks) and downtime records.
11. Incubator, isolator and autoclave loading and cycle records.
12. Headcount by role: approved, actual, vacancies, temporary staff, shift patterns.
13. Competency and authorization matrix (analyst × method).
14. HR aggregate absence, leave, overtime and turnover data.
15. Time allocation per role (testing, preparation, documentation, review, investigations, training, administration).
16. Counts and average effort of OOS, OOT, deviations, investigations and CAPA.
17. Turnaround times and backlog by month, and target turnaround times by sample type.
18. Outsourced testing volumes, costs and turnaround.
19. Cost data: loaded salary by role, service contracts, consumables by method, utilities, licences.
20. Facility data: available space, utilities capacity, HVAC and cleanroom constraints.
21. Unit head questionnaires (Deliverable 2), completed and signed.
