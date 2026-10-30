# NASA Space Apps 2026 — NeuraX Challenge Reassessment v2

> Historical snapshot. Current decision guidance: [v3 — full briefs and six members](v3-full-brief-six-members.md). Five-member assumptions and release expectations below are preserved as history, not current status. Competitor/winner claims below lack source-by-source records and are not used as verified evidence in v3.

> **Date:** 2026-10-26  
> **Status:** Pre-release reassessment before the complete 2026 challenge statements/resources scheduled for 2026-10-28.  
> **Supersedes for decision-making:** the original preliminary ranking; the original ranking remains valuable as a historical snapshot.

## Why this reassessment exists

The first ranking was produced before the team composition was fully settled and before reviewing patterns from recent NASA Space Apps winners and the public concepts of other 2026 teams.

Since then:

- **Vo Thi Ngoc Bich — Environmental Science** has become part of the active team rather than a conditional candidate.
- NeuraX now has a clearer five-person multidisciplinary structure: **AI ×2 + Environmental Science + Software Engineering + Hardware**.
- The team wants a project with strong **practical impact, simulation/scenario exploration, measurable technical depth, and a compelling live demo**.
- Recent winner patterns suggest that technical complexity alone is not enough; strong projects tend to connect NASA data to a concrete user decision or action.
- Some 2026 challenge spaces already show strong public competition, which affects differentiation.

This reassessment therefore asks a stricter question:

> **Which challenge lets this exact NeuraX team build the strongest end-to-end system, rather than merely the strongest model or dashboard?**

---

## Evaluation lens v2

The v2 ranking emphasizes nine factors:

1. **Team coverage** — can all core disciplines contribute naturally?
2. **Practical impact** — is there a real user and consequential decision?
3. **NASA-data centrality** — would the product lose its core value without NASA/open space data?
4. **AI/data depth** — is there a meaningful modeling problem rather than decorative AI?
5. **Simulation / decision-support potential** — can users explore alternatives, scenarios, or future states?
6. **Environmental / GIS leverage** — does Bích's domain background become a core advantage?
7. **Software / demo quality** — can Hiếu build a visible, interactive end-to-end system?
8. **Hardware opportunity** — can Tiểu An contribute naturally without making hardware a dependency?
9. **Differentiation and 48-hour feasibility** — can the team stand out while still shipping a credible MVP?

### Winner-pattern principle

A recurring structure in strong NASA Space Apps projects is:

`real user problem → NASA data → scientific/modeling layer → prediction/optimization/simulation → decision → action → visual proof/demo`

This is not an official NASA formula and should not be treated as one. It is a design heuristic derived from reviewing recent high-performing project patterns.

---

## Updated preliminary ranking

These are **NeuraX internal decision scores**, not NASA scores.

| Rank | Challenge | v2 fit | Current interpretation |
| ---: | --- | ---: | --- |
| **1** | **Field Shift: Adapting Farms with NASA Data** | **92/100** | Best overall multidisciplinary fit. Strong natural space for prediction, optimization, crop-rotation scenario simulation, environmental validation, WebGIS, and optional sensing. |
| **2** | **Identify Earth Locations that Analog the Permanent Moon Base Locations and Mars** | **89/100** | Strongest space-forward systems concept. AI similarity/ranking + GIS + mission-constraint simulation + possible hardware field-validation concept. |
| **3** | **Harmonization of MODIS and VIIRS Hot Spots** | **89/100** | Excellent scientific/data fit with strong evaluation and map demo, but public competitor concepts already cover harmonization + weather + prediction, reducing differentiation. |
| **4** | **Dancing with the SARs** | **86/100** | NISAR surface-change analysis is visually strong and well aligned with environmental/GIS expertise, but SAR preprocessing/domain burden is substantial and scenario simulation is less native. |
| **5** | **Be An Earth System Trend Detective!** | **85/100** | Strong research/statistics challenge with interpretable modeling and environmental relevance; risk of becoming generic analytics without a sharp user decision loop. |
| **6** | **Interplanetary Survival Guide: Martian Map** | **85/100** | Excellent route/hazard/science trade-off simulation and highly memorable demo; planetary data integration and validation add domain burden. |
| **7** | **Create Health Monitoring Software for Astronauts on Space Missions** | **78/100** | Good AI/sensor/software potential, but medical validity, safety framing, and data constraints create a high-risk domain surface. |
| **8** | **CLPS Lunar Mission Browser / Lunar Landing Site Navigator** | **74/100** | Strong native simulation around landing date/site and visibility, but geometry/ephemeris validation may absorb too much hackathon time. |
| **9** | **Flame in Freefall** | **73/100** | Good AI/retrieval opportunity, but combustion grounding is a domain gap and an AI-dashboard implementation can be difficult to differentiate. |
| **10** | **Space Mission Design Game** | **72/100** | Simulation is native, but balancing a game and scientific constraints can consume the entire event. |
| **11** | **The Earth Information Jukebox** | **72/100** | Creative, accessible and demo-friendly, but it underuses the team's strongest AI/environment/hardware combination unless sonification is technically substantive. |
| **12** | **Build a Junior Astronaut Mission Trainer** | **70/100** | Straightforward to prototype and present, but educational game design is not NeuraX's strongest differentiator. |
| **13** | **Planet X and SPHEREx** | **67/100** | Interesting AI/data problem, but astrophysics and large-data complexity are less aligned with current team domain strengths. |
| **14** | **Abandoned but not Forgotten** | **55/100** | Good storytelling opportunity but uses comparatively little of the team's technical and environmental capability. |

> The narrow gaps between the top challenges are intentionally treated as provisional. The 2026-10-28 full briefs/resources can change the ranking materially.

---

# Top 3 concepts before the full release

## 1. Field Shift — **NeuraX AgroTwin**

### Working thesis

> **Simulate tomorrow's farm before farmers have to live through it.**

### Core system

`NASA Earth observations + soil/crop context + climate signals → risk/suitability models → crop-rotation optimization → what-if climate simulation → farmer decision`

### Why it fits the team

- **Hưng — AI:** predictive modeling, multi-objective optimization, evaluation.
- **Việt — AI:** suitability/risk modeling, anomaly detection, explainability, scenario engine.
- **Bích — Environmental Science:** crop/soil/environmental validity, Earth-observation interpretation, sustainability assumptions.
- **Hiếu — SE:** farm-polygon/WebGIS workflow, APIs, backend, simulation UI, deployment.
- **Tiểu An — Hardware:** optional soil-moisture/temperature/humidity field node for local context or validation.

### Strong demo loop

1. Select a farm/region and current crop/rotation.
2. Show current climate/soil-related indicators from NASA/open data.
3. Compare multiple rotation strategies.
4. Move scenario controls such as temperature, rainfall, or dry-season duration.
5. Recompute risk/water/stability scores.
6. Explain why the recommended strategy changes.

### Why it currently ranks first

Simulation and decision support are **native to the problem**, rather than an extension added after the core challenge. Environmental Science becomes a central validation role, and hardware can contribute as an optional local-sensing extension without becoming a dependency.

### Main risks to verify on 2026-10-28

- exact official deliverables;
- official NASA datasets and spatial/temporal resolution;
- whether crop/soil data necessary for a credible recommendation is available and permitted;
- danger of making agronomic recommendations beyond what the data supports;
- feasibility of validating recommendations within a hackathon.

---

## 2. Earth Analog Locations — **NeuraX TerraTwin**

### Working thesis

> **Find the best place on Earth to test tomorrow's Moon and Mars missions.**

### Core system

`Earth + Moon/Mars environmental/geospatial variables → interpretable similarity model → candidate Earth analog ranking → mission/hardware constraints → scenario-specific test-site recommendation`

### Simulation opportunity

A user changes mission or equipment constraints such as:

- slope tolerance;
- temperature range;
- aridity;
- terrain roughness;
- dust sensitivity;
- isolation/access requirements.

The ranking of Earth analog sites updates immediately.

### Why it fits

It uses AI/data, environmental/GIS reasoning, software, and hardware-testing thinking very naturally. It is also the most obviously space-mission-oriented option among the current top three.

### Main risks

- availability and compatibility of Earth/Moon/Mars variables;
- defining similarity without arbitrary weights;
- validating that an analog is useful for a mission rather than merely visually similar;
- competitor overlap around map/ranking concepts.

---

## 3. MODIS + VIIRS — **NeuraX FireSense**

### Working thesis

> **Turn two generations of satellite fire observations into a trustworthy historical record and explainable fire-risk intelligence.**

### Core system

`MODIS + VIIRS → sensor harmonization → historical burning calendar → anomaly detection → optional elevated-activity forecast → scenario exploration`

### What remains excellent about it

- rigorous measurable data-science problem;
- very strong NASA-data centrality;
- excellent geospatial visualization;
- clear evaluation opportunities during sensor overlap;
- Bích can improve interpretation of wildfire vs agricultural/other thermal patterns;
- easy-to-understand before/after harmonization demo.

### Why it moved from #1 to #3

The public 2026 competitive space already contains concepts involving combinations of:

- MODIS/VIIRS reconciliation;
- fire calendars;
- weather variables;
- hazard prediction/risk mapping.

Therefore `harmonization + AI prediction + dashboard` is not sufficient differentiation by itself. In addition, future prediction/simulation appears to be an **extension** of the currently published challenge summary, whereas Field Shift's decision/scenario nature is closer to the core problem.

### Main risks

- overclaiming wildfire prediction from thermal-anomaly data;
- insufficient differentiation;
- spending too much time on forecasting and too little on the challenge's core harmonization problem;
- full brief may constrain or strengthen the scope on 2026-10-28.

---

# Dark horses

## Dancing with the SARs

Could move into the top 2 if NASA provides clean, analysis-ready NISAR products and a sharply defined decision/application scenario. It offers excellent change-detection and before/after visual storytelling, but SAR domain complexity is a serious execution risk.

## Martian Map

Could move upward if the full resources make terrain/hazard routing straightforward. A resource-constrained route planner can provide one of the strongest simulations in the entire challenge set: safest vs fastest vs highest-science-value routes under oxygen/time/terrain constraints.

---

# Decision policy for 2026-10-28

Do **not** choose the final challenge based on the v2 scores alone.

For at least the current top six, verify:

1. exact official problem statement;
2. required deliverable/output;
3. official resource and dataset links;
4. data accessibility and licensing;
5. spatial/temporal resolution and missing-data constraints;
6. realistic ground truth/evaluation strategy;
7. whether the proposed AI work is actually necessary;
8. whether simulation is supported by the challenge rather than bolted on;
9. whether one end-to-end demo path can work during the event;
10. how crowded the public competitor space is;
11. whether NeuraX has a differentiator that can be stated in one sentence.

## Recommended technical spike before final lock

For the top three, run a small proof-of-feasibility test after the official resources are released:

- **Field Shift:** load one official NASA variable for one agricultural region and produce one interpretable field/region metric.
- **Earth Analog:** load one Earth variable plus one Moon/Mars comparison variable and rank a tiny set of candidate locations.
- **MODIS/VIIRS:** load overlapping hotspot data and quantify one real sensor discontinuity/harmonization baseline.

The challenge that produces the strongest combination of **usable data + defensible science + differentiated demo + team coverage** should become the final choice.

---

## Decision log

### v1 — 2026-10-26 initial research

1. MODIS/VIIRS
2. Dancing with the SARs
3. Earth Analog Locations
4. Earth System Trend Detective
5. Field Shift

### v2 — 2026-10-26 team/winner/competition reassessment

1. **Field Shift**
2. **Earth Analog Locations**
3. **MODIS/VIIRS**
4. **Dancing with the SARs**
5. **Earth System Trend Detective**
6. **Martian Map**

### Next decision point

**2026-10-28:** full challenge/resource audit and ranking v3.
