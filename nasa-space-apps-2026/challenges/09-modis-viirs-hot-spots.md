# 09 — Harmonization of MODIS and VIIRS Hot Spots

**Difficulty:** Advanced · Intermediate  
**Subjects:** Earth Science · Software  
**NeuraX preliminary score (v1):** **9.3/10 — Tier S / former #1**  
**Current v2 position:** **#3 provisional candidate**  
**Status:** Summary available; full 2026 brief/resources expected 2026-10-28.

## Confirmed challenge intent

Satellite sensors have recorded active-fire hotspots for more than two decades, but the historical record is split across sensors whose detections cannot simply be compared one-to-one. NASA asks teams to create a **web application that harmonizes MODIS and VIIRS hotspot records into a burning-activity calendar**, so emergency responders, scientists, fire managers, and land managers can examine historical patterns, unusual conditions, and critical periods for a selected area of interest.

Sources:
- https://www.spaceappschallenge.org/2026/challenges/
- https://nasaspaceapps.ae/challenges

## Why it remains a strong NeuraX fit

- NASA data is unquestionably central.
- The scientific problem is concrete: **cross-sensor harmonization**, not vague “use AI for wildfire.”
- It uses geospatial processing, time-series/statistics, software, visualization and environmental interpretation.
- The output has identifiable users and decisions.
- A useful MVP can be narrowed to one region while retaining a path to global scale.
- The demo can be immediately understood: select an area → see a consistent fire calendar/history → detect unusual activity.

## NeuraX concept evolution

### v1 concept: “FireChronicle”

`draw/select AOI → choose historical period → harmonize MODIS + VIIRS → burning calendar → historical baseline → anomaly/critical-period analysis`

### v2 direction: “NeuraX FireSense”

`MODIS + VIIRS → sensor harmonization → historical burning calendar → anomaly detection → optional elevated-activity forecast → scenario exploration`

The scientific contribution must remain **harmonization**. Forecasting/simulation should only be included if the full brief/resources support it and the team can defend the environmental assumptions.

## The real technical problem: harmonization

MODIS and VIIRS differ in sensor characteristics, spatial resolution, detection behavior, overpass timing, and record periods. A credible solution must avoid concatenating two CSVs and calling the result harmonized.

Candidate issues include:

- different spatial footprints/resolution;
- differing detection confidence/attributes;
- duplicate or near-duplicate detections;
- changing observation opportunity through time;
- sensor overlap period that can be used for calibration/comparison;
- temporal aggregation choice;
- AOI area normalization;
- missing/unequal coverage.

## Candidate data

The official challenge clearly centers on:

- **MODIS active-fire/hotspot observations**;
- **VIIRS active-fire/hotspot observations**.

NASA FIRMS is a likely access ecosystem, but exact products/files/APIs and required attributes must be taken from the 2026-10-28 official resources.

## Candidate harmonization strategy

### Phase 1 — common schema

Normalize timestamp/date, location, sensor/platform, confidence/quality, comparable thermal attributes, day/night and AOI membership.

### Phase 2 — common spatial representation

Aggregate to a grid or AOI statistic that does not pretend the sensors have identical native resolution.

### Phase 3 — overlap-period calibration

Compare sensor families during overlap and estimate a mapping/normalization if supported by the brief.

Possible approaches:

- empirical ratio by region/season;
- regression/calibration model;
- quantile mapping;
- stratification by land-cover or fire regime;
- uncertainty interval rather than a single corrected count.

### Phase 4 — burning calendar

- day-of-year × year heatmap;
- monthly/weekly climatology;
- median/percentile baseline;
- anomaly score;
- critical-period indicator.

## AI/ML opportunity

Useful options:

- anomaly detection against historical fire climatology;
- clustering AOIs by fire-season behavior;
- event segmentation from dense hotspot points;
- forecast-like risk context only if allowed and supported by data;
- natural-language summary generated from computed statistics.

A transparent statistical harmonization baseline will likely be stronger than deep learning for the core challenge.

## Simulation/prediction extension

A defensible extension could estimate **elevated burning-activity risk**, rather than claiming exact wildfire ignition prediction, using harmonized history plus relevant environmental variables. A scenario mode could vary temperature/rainfall/humidity assumptions and show how risk changes.

This is an extension, not currently confirmed as the core challenge requirement.

## 48-hour MVP

1. Pick **one fire-prone region** with a long record.
2. Ingest manageable MODIS + VIIRS hotspot subsets.
3. Normalize them into one common schema.
4. Use overlap years to quantify cross-sensor differences.
5. Implement one defensible harmonization method.
6. Generate a multi-year burning calendar and seasonal baseline.
7. Build an AOI dashboard with map + calendar + anomaly comparison.
8. Prepare one case study where harmonization reveals something raw split records obscure.

## Evaluation

- compare sensor behavior during overlap before/after harmonization;
- measure residual discrepancy between aggregate records;
- evaluate stability across regions/seasons;
- sensitivity to grid size and temporal aggregation;
- compare simple concatenation baseline vs harmonized result;
- sanity-check known large fire seasons/events;
- show uncertainty rather than hiding disagreement.

A powerful demo line remains: **“Here is the discontinuity if we naively switch sensors; here is how our method reduces it.”**

## Team fit — current baseline

- **Hưng:** harmonization/statistics, modeling, evaluation, research framing.
- **Việt:** data engineering, anomaly/risk modeling and visual analytics.
- **Bích:** fire/environment interpretation, GIS validation and guardrails against confusing thermal anomaly with wildfire impact.
- **Hiếu:** AOI web app, API, mapping and deployment.
- **Tiểu An:** optional local sensing / physical-system extension if useful, but hardware is not native to the core challenge.

## Why it moved from #1 to #3 in v2

Public 2026 concepts already cover combinations of MODIS/VIIRS reconciliation, fire calendars, environmental variables, prediction and risk mapping. That reduces differentiation for a generic `harmonization + AI + dashboard` pitch.

Also, prediction/simulation currently appears to be an **extension** of the published challenge summary, while Field Shift has decision/scenario exploration closer to its core.

## Risks

- Treating hotspot count as burned area or fire severity without justification.
- Sensor differences not fully addressed.
- Duplicate detections/observation opportunities biasing counts.
- Calling an anomaly an operational “early warning” without evidence.
- Spending too much time on prediction and not enough on the core harmonization problem.
- Insufficient differentiation from other 2026 teams.

## Recommendation

**Still a Top 3 candidate.** It remains one of NeuraX's strongest scientific/data projects, but the final selection should depend on the full 2026-10-28 definition of harmonization, supplied data/resources, and whether NeuraX can state a differentiator beyond the approaches already visible publicly.
