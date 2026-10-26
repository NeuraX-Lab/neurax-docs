# 06 — Dancing with the SARs

**Difficulty:** Advanced · Intermediate  
**Subjects:** Earth Science  
**NeuraX preliminary score:** **9.0/10 — Tier S-**  
**Status:** Summary available; full 2026 brief/resources expected 2026-10-28.

## Confirmed challenge intent

Earth's surface changes through natural processes and human activity: wetland loss, wildfire, earthquakes, agriculture, glacier motion and more. NASA asks teams to build an **interactive application using radar remote-sensing data from the NASA–ISRO Synthetic Aperture Radar (NISAR) mission** to track and visualize one or more types of surface change at locations around the world.

Sources:
- https://www.spaceappschallenge.org/2026/challenges/
- https://nasaspaceapps.ae/challenges

## Why this is a top NeuraX candidate

The challenge naturally combines:

- Earth observation;
- geospatial data processing;
- change detection;
- AI/ML if useful;
- interactive maps;
- a highly visible real-world impact story.

It gives NeuraX room to show real technical depth while still producing a visual demo judges can understand immediately.

The main issue is **SAR expertise**. Radar imagery behaves very differently from optical imagery; a naive “subtract two pictures” system can be misleading.

## NeuraX product concept: “SARShift”

A focused change-monitoring application for **one change type** rather than a generic global SAR viewer.

Potential focus areas:

- flood/wetland extent change;
- wildfire/burn-area structural change;
- agricultural activity;
- glacier/ice movement;
- earthquake/deformation-related change if the supplied data products support it.

User flow:

`choose event/region → select before/after dates → compute/display change layer → inspect hotspots → quantify changed area → explain signal and confidence`

For a hackathon, choosing one phenomenon with strong sample data is much stronger than trying to support every type named in the summary.

## Candidate NISAR data path — verify on 2026-10-28

The full NASA resource list is critical here. Candidate data/product considerations may include:

- NISAR L-band and/or S-band SAR products;
- calibrated/backscatter products rather than raw radar data where possible;
- geocoded products suitable for rapid web mapping;
- event/reference regions supplied by the challenge;
- NASA Earthdata / DAAC access path specified in the official resources.

**Key decision gate:** if the official challenge expects teams to start from complex low-level SAR products, hackathon preprocessing risk increases sharply. If analysis-ready/geocoded samples are provided, this becomes one of NeuraX's strongest choices.

## SAR-specific technical considerations

A credible solution should understand at least these concepts:

- radar backscatter is sensitive to geometry, roughness, moisture and structure;
- speckle/noise affects pixel-wise comparisons;
- incidence angle / acquisition geometry can confound change;
- different polarizations/bands may respond differently;
- preprocessing and co-registration matter;
- “change” in radar intensity is not automatically the physical phenomenon of interest.

Do not claim semantic causes from a backscatter difference alone unless supported by additional evidence.

## Analytical approaches

Depending on the official products and selected phenomenon:

### Simple baseline
- normalize comparable acquisitions;
- calculate log-ratio / difference;
- threshold robustly;
- clean regions morphologically;
- summarize area and spatial distribution.

### More advanced options
- time-series change metrics;
- unsupervised clustering of change signatures;
- supervised change classification if labels exist;
- segmentation model if training data is realistic;
- multi-source fusion with optical/land-cover/context data as supporting evidence.

A transparent baseline + good evaluation is preferable to an unvalidated deep-learning model.

## Technical decomposition

### Preprocessing/data
- region/date query;
- product download/subsetting;
- CRS/reprojection if required;
- normalization/filtering;
- tiled or cloud-optimized output for web display.

### Analytics
- before/after or time-series comparison;
- change score;
- threshold/classification;
- region statistics;
- confidence/quality flags.

### Backend
- AOI/date request;
- cached processed layers;
- statistics API;
- event metadata.

### Frontend
- interactive map;
- swipe/before-after viewer;
- change overlay;
- timeline;
- area/statistics cards;
- click-to-inspect radar signal/time series.

## 48-hour MVP

1. Choose **one phenomenon and 1–3 regions** with verified NISAR data.
2. Preprocess a small set before the main UI work.
3. Implement a simple, scientifically defensible change metric.
4. Produce a web-ready change raster/vector layer.
5. Build a map with before/after swipe + highlighted changes.
6. Add changed-area statistics and a short explanation.
7. Validate against an independent event/known map if possible.

## Evaluation

Potential evaluation approaches:

- compare detected regions with known event footprints or independent data;
- manually inspect representative changed/unchanged samples;
- report precision/recall/IoU only if credible ground truth exists;
- sensitivity analysis for threshold choices;
- compare simple baseline versus ML method;
- clearly distinguish radar-signal change from confirmed land-cover/process change.

## Team fit

- **Hưng:** change-detection method, evaluation, ML/representation options, scientific framing.
- **Việt:** data processing, modeling/visual analytics, demo narrative.
- **Hiếu:** map application, backend processing orchestration and deployment.
- **Bích:** environmental/GIS interpretation and validation.
- **Tiểu An:** hardware/sensing perspective and impact story where relevant.

## Risks

- SAR learning curve and terminology.
- Large files / slow downloads.
- Data-access/authentication friction.
- Wrong preprocessing invalidates analysis.
- Visually impressive but scientifically weak change maps.
- Trying to solve multiple phenomena simultaneously.

## Scorecard

| Dimension | Score / 10 | Comment |
|---|---:|---|
| Team fit | 9.0 | Excellent overall, with SAR expertise as the one major gap. |
| AI/data leverage | 8.5 | Strong change-detection opportunity without forcing AI. |
| GIS/EO leverage | 10.0 | Core of the problem. |
| 48h feasibility | 7.5 | Highly dependent on product level/data accessibility. |
| Demo/story impact | 9.5 | Before/after surface change is immediately understandable. |
| NASA-data centrality | 10.0 | NISAR is explicitly central. |
| Differentiation ceiling | 9.5 | Strong research + visual + impact ceiling. |

## Recommendation

**Strong candidate.** If the 2026-10-28 full brief provides analysis-ready NISAR products or manageable samples, NeuraX should seriously reconsider its position in the Top 3. If the data pipeline is too low-level/heavy for a 48-hour build, Field Shift, Earth Analog or MODIS/VIIRS remain safer.
