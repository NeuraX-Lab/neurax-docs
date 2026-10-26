# 10 — Identify Earth Locations that Analog the Permanent Moon Base Locations and Mars

**Difficulty:** Advanced · Intermediate · Beginner/Youth  
**Subjects:** Earth Science · Planets & Moons · Software · Space Exploration  
**NeuraX preliminary score (v1):** **8.9/10 — Tier A+**  
**Current v2 position:** **#2 provisional candidate**  
**Status:** Summary available; full 2026 brief/resources expected 2026-10-28.

## Confirmed challenge intent

Future landing sites and permanent base locations depend on characteristics such as topography, geology, environment, and available resources. Earth analog sites allow mission teams to test equipment and methods before flight, but terrestrial analogs are not fully characterized.

NASA asks teams to use **open Earth, Moon, and Mars data from NASA and other space agencies** to identify and characterize new terrestrial analog sites across deserts, polar areas, volcanic/arid terrain, caves, and other environments sharing lunar or Martian characteristics.

Sources:
- https://www.spaceappschallenge.org/2026/challenges/
- https://nasaspaceapps.ae/challenges

## Why this is a strong NeuraX fit

This is a **cross-planet geospatial similarity / site-discovery problem** combining:

- multimodal spatial data;
- feature engineering;
- similarity/ranking;
- explainability;
- map visualization;
- environmental interpretation;
- hardware/mission-testing perspective;
- a natural research extension after the hackathon.

## NeuraX concept: “TerraTwin”

A user selects a target lunar/Martian environment or specifies target characteristics. The system searches Earth candidate locations and returns **ranked analog sites with evidence explaining why each site is similar**.

### v2 extension — mission-specific simulation

Instead of one static similarity score, the user defines the mission/testing need:

- slope tolerance;
- temperature range;
- aridity;
- terrain roughness;
- dust sensitivity;
- isolation/access constraints;
- equipment-specific environmental requirements.

The Earth-site ranking updates as these constraints change.

This changes the product from “find places that look like Mars” into **“find the Earth test environment that best matches this mission or hardware test.”**

## Explainable output

For every candidate Earth analog, show similarity by dimension rather than only one score:

- elevation / relief;
- slope / roughness;
- temperature regime;
- aridity / precipitation;
- surface material/geology proxy;
- vegetation scarcity;
- environmental proxies where scientifically defensible;
- accessibility/logistics, clearly separated from physical similarity.

## Candidate data families — verify 2026-10-28

### Earth candidates
Potential families may include terrain/elevation, land-surface temperature, vegetation/land cover, precipitation/aridity and approved geological/surface sources.

### Moon candidates
Possible resources include LRO imagery, LOLA topography/elevation and other products listed by the official challenge.

### Mars candidates
Possible resources include MOLA topography, THEMIS, CTX/HiRISE and relevant PDS/mineralogical products.

These remain candidate families until the official full resource list is released.

## Scientific design choice: feature similarity before image similarity

A tempting approach is computer-vision embeddings for “places that look like Mars.” This risks scientifically meaningless matches because sensor, resolution, spectral and imaging geometry differ.

### Baseline — interpretable physical feature vector

For target and candidate locations, compute standardized features such as:

`[slope, elevation variance, roughness, temperature statistics, aridity, vegetation, albedo/surface proxy, ...]`

Then use:

- weighted normalized distance;
- cosine similarity after meaningful scaling;
- Mahalanobis distance if correlations matter;
- multi-criteria ranking.

### Advanced

- unsupervised clustering of Earth environmental regimes;
- metric learning if valid labeled analog pairs exist;
- multimodal embeddings combining raster + tabular features;
- uncertainty-aware ranking;
- diversity constraints for geographically distinct candidates.

## Technical decomposition

### Planetary target processing
- define target ROI;
- extract environmental/terrain characteristics;
- normalize feature definitions across datasets.

### Earth candidate database
- tiling or curated candidate set;
- precomputed features;
- spatial index;
- data-quality/provenance fields.

### Similarity / simulation engine
- user or mission constraint weights;
- normalized comparison;
- candidate filtering;
- ranking;
- explanation per feature;
- scenario-specific re-ranking.

### Frontend
- Moon/Mars target map;
- Earth results map;
- linked side-by-side terrain imagery;
- feature comparison;
- mission/test requirement controls;
- provenance for every layer.

### Optional hardware angle

Tiểu An can frame or prototype a field-sensing payload for validating candidate analog environments. Hardware should support the “test mission hardware on Earth first” narrative rather than being added decoratively.

## 48-hour MVP

1. Choose **one target environment**, Moon or Mars.
2. Choose 4–6 defensible features.
3. Precompute a limited Earth candidate set.
4. Implement weighted similarity ranking.
5. Add 2–4 mission/hardware constraints that re-rank sites.
6. Build side-by-side map/feature comparison.
7. Validate known analog sites as a sanity check.
8. Surface 2–3 plausible new candidates and explain why.

## Evaluation

- **known analog retrieval:** do established analog sites rank highly?
- ablation: which features drive ranking?
- sensitivity to weights/mission constraints;
- environmental/GIS plausibility review;
- compare physical-feature similarity vs naive visual similarity;
- uncertainty/data-coverage reporting.

## Team fit — current baseline

- **Hưng:** similarity methodology, ML/optimization, evaluation.
- **Việt:** spatial feature pipeline, modeling and scenario engine.
- **Bích:** environmental feature selection, GIS validity and interpretation.
- **Hiếu:** interactive Earth/planetary map and API.
- **Tiểu An:** hardware test constraints, sensing concept and field-system perspective.

This is one of the strongest challenges for integrating all five roles while remaining visibly “space mission” oriented.

## Risks

- Comparing incomparable variables across planets.
- “Looks like Mars” becoming the criterion.
- Global raster preprocessing too large for the weekend.
- Geology/resource similarity being hard to standardize.
- False precision in a single similarity percentage.
- Scope explosion across Moon + Mars + all Earth.

## Recommendation

**Current provisional #2.** TerraTwin may become #1 if the 2026-10-28 resource package gives clean target variables and comparison datasets. It has stronger native hardware/space identity than Field Shift and stronger multidisciplinary breadth than MODIS/VIIRS, but scientific cross-planet comparability is the key risk.
