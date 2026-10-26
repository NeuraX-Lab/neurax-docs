# 07 — Field Shift: Adapting Farms with NASA Data

**Difficulty:** Advanced · Intermediate  
**Subjects:** Arts & Multimedia · Earth Science · Software  
**NeuraX preliminary score (v1):** **8.6/10 — Tier A+**  
**Current v2 position:** **#1 provisional candidate**  
**Status:** Summary available; full 2026 brief/resources expected 2026-10-28.

## Confirmed challenge intent

Farmers face changing temperature and rainfall, water shortages, extreme weather, and declining soil health. NASA asks for a **decision-support tool** that combines NASA Earth observations with local soil information, crop characteristics, and farmer priorities to help explore **crop-rotation strategies** that can strengthen soil health and climate resilience.

Sources:
- https://www.spaceappschallenge.org/2026/challenges/
- https://nasaspaceapps.ae/challenges

## Why this fits NeuraX

This is not just an agriculture dashboard. It is a multi-criteria decision problem combining:

- Earth-observation signals;
- local/context data;
- crop knowledge;
- farmer goals;
- temporal planning;
- uncertainty and trade-offs.

That creates a natural role for data science, optimization/recommendation, geospatial analysis, environmental validation, software, and explainable decision support.

## NeuraX concept evolution

### v1 concept: “RotationShift”

A farmer or advisor selects a field/region, current crop history, available crop options, and priorities such as:

- conserve water;
- improve soil health;
- reduce climate risk;
- maintain yield/income proxy;
- diversify rotation;
- avoid high-input sequences.

The tool produces several candidate rotation plans rather than one opaque “best crop,” then explains the trade-offs.

### v2 direction: “NeuraX AgroTwin”

The concept expands into a focused **scenario-based farm decision twin**:

`NASA Earth observations + soil/crop context + climate signals → risk/suitability models → crop-rotation optimization → what-if climate simulation → farmer decision`

The key improvement is not adding more features; it is making the user able to test **future scenarios and alternatives** before acting.

Example scenario controls:

- temperature +2 °C;
- rainfall −20%;
- longer dry season;
- farmer priority shifts from yield stability to water conservation.

The system recomputes risk/trade-offs and explains why a different rotation may become preferable.

## Candidate NASA/environment data — verify 2026-10-28

Depending on official resources, plausible signals include:

- precipitation history/anomalies (e.g., GPM-family products);
- soil moisture (e.g., SMAP-family products);
- temperature/land-surface indicators;
- vegetation/phenology indicators;
- evapotranspiration or drought-related products if supplied;
- extreme-event/climate context;
- local soil datasets and crop characteristics from non-NASA sources specified by the challenge.

These are **candidate inputs only** until NASA releases the full resource list.

## Decision-model approach

A good hackathon system should be interpretable. Possible pipeline:

1. Convert EO data into field/region-level features.
2. Characterize recent climate and water stress.
3. Encode crop/rotation constraints.
4. Score candidate sequences against farmer priorities.
5. Return multiple Pareto-like alternatives with explanations.
6. Re-run the scoring/optimization under user-defined climate scenarios.

### Useful methods

- weighted multi-criteria decision analysis;
- rule-constrained ranking;
- simple optimization over rotation sequences;
- scenario analysis under dry/normal/wet conditions;
- clustering fields/regions by environmental profile;
- uncertainty-aware score ranges.

A black-box recommender trained without credible labels would be weaker than a transparent model grounded in agronomic constraints.

## Technical decomposition

### Geospatial/EO pipeline
- field/AOI selection;
- retrieve historical EO variables;
- temporal aggregation/anomalies;
- regional features.

### Crop/soil knowledge layer
- crop water/climate characteristics;
- soil compatibility;
- rotation constraints/benefits;
- local soil properties.

### Decision and simulation engine
- candidate sequence generation;
- hard constraints;
- preference weights;
- score + explanation;
- scenario comparison;
- multi-objective optimization where justified.

### Frontend
- map/field selection;
- farmer priority controls;
- environmental history summary;
- rotation option cards;
- trade-off visualization;
- climate scenario controls;
- “why this plan?” panel.

### Optional hardware extension

A small field node could provide local context such as soil moisture, temperature or humidity. It should remain optional: the product must work from NASA/open data even if the hardware prototype is unavailable.

## 48-hour MVP

Do not try to support every crop globally.

1. Pick **one region and a small crop set** supported by available data.
2. Build EO features for climate/water context.
3. Define a small, cited crop/rotation knowledge table.
4. Generate 2–3 season rotation sequences.
5. Score sequences under 3–4 user priorities.
6. Add one or two simple what-if climate scenarios.
7. Build a map + option-comparison dashboard.
8. Demo how changing farmer priorities or climate assumptions changes the recommendation.

## Evaluation

- Test scoring logic on handcrafted scenarios where expected preferences are known.
- Sensitivity analysis to priority weights.
- Verify EO-derived features against source data.
- Have Bích/domain sources inspect crop/environmental assumptions.
- Explain clearly what is heuristic versus scientifically validated.
- Compare recommendation stability across plausible scenario perturbations.

## Team fit — current five-person baseline

- **Hưng — AI:** predictive/risk modeling, multi-objective optimization, evaluation.
- **Việt — AI:** suitability model, explainability, anomaly/scenario engine.
- **Bích — Environmental Science:** crop/soil/environment validity, GIS/EO interpretation and sustainability assumptions.
- **Hiếu — SE:** farm-polygon/WebGIS workflow, backend, APIs, simulation UI and deployment.
- **Tiểu An — Hardware:** optional local sensing / physical field-node concept and hardware–software integration.

This is currently the most balanced challenge for using all five disciplines **without forcing them**.

## Risks

- Agronomy knowledge gap beyond environmental science: crop rotation is not reducible to satellite data alone.
- Local soil/crop datasets may be inconsistent across regions.
- Overclaiming yield/soil-health outcomes.
- Too many crops/regions/variables.
- Recommendations that are mathematically neat but impractical for real farmers.
- Simulation becoming arbitrary if scenario-response assumptions are not evidence-backed.

## Recommendation

**Current provisional #1 in v2.** The main reason is that decision support and scenario exploration are native to the challenge, Environmental Science is core rather than decorative, AI/optimization can be meaningful, the software demo is clear, and hardware can be an optional differentiator. The 2026-10-28 official resource package still has to prove that a scientifically defensible MVP is feasible.
