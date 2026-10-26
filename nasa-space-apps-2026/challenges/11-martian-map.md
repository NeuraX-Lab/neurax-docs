# 11 — Interplanetary Survival Guide: Martian Map

**Difficulty:** Intermediate  
**Subjects:** Human Exploration · Mars · Planets & Moons · Software · Space Exploration  
**NeuraX preliminary score:** **8.4/10 — Tier A**  
**Current v2 position:** **#6 provisional candidate**  
**Status:** Summary available; full 2026 brief/resources expected 2026-10-28.

## Confirmed challenge intent

NASA has mapped and studied Mars through many robotic missions and many different data products. The challenge asks teams to create a **layered, integrated view of a Martian location or route** that combines information from multiple NASA science missions and could help a future human explorer plan and perform a successful Marswalk while conducting science.

The published summary explicitly mentions route/destination details, current-condition updates, safety, and science needs.

Sources:
- https://www.spaceappschallenge.org/2026/challenges/
- https://nasaspaceapps.ae/challenges

## Why this fits NeuraX

This is a strong **geospatial product-integration and route-simulation challenge**. It can demonstrate:

- geospatial raster/vector integration;
- terrain analysis;
- route scoring;
- multi-objective optimization;
- data fusion;
- user-centered software;
- optional AI explanation/planning.

The use case is easy to understand: **“Can an astronaut safely get from A to B and still accomplish science objectives?”**

## NeuraX concept: “MarsWalk Navigator”

`choose start + destination/science target → inspect terrain/environment layers → generate/compare route candidates → show risk/science trade-offs → export mission brief`

### Potential map layers

Depending on official resources:

- elevation/terrain;
- slope;
- high-resolution imagery;
- rock/geology/mineral context;
- thermal/environmental context;
- hazard areas;
- science-interest sites;
- communication/line-of-sight proxy if appropriate;
- rover/mission landmarks.

## Candidate NASA data families — verify on 2026-10-28

Potential resources include MOLA, CTX, HiRISE, THEMIS, CRISM, rover/lander observations and NASA Planetary Data System resources. The official brief should determine which products are expected and whether sample route areas are provided.

## Route-planning approach

A transparent cost surface is sufficient if well justified.

Example:

`cost = w1*distance + w2*slopeRisk + w3*hazard + w4*uncertainty - w5*scienceValue`

Then use Dijkstra/A* over a raster/grid or graph.

The strongest simulation angle is to let user constraints change the route:

- oxygen/time budget;
- safest vs fastest;
- science-priority weighting;
- slope tolerance;
- emergency-return mode.

A science-heavy EVA and an emergency return route should not optimize the same objective.

## Technical decomposition

### Data preprocessing
- choose local ROI;
- harmonize CRS/grid/resolution;
- derive slope from DEM;
- convert science/hazard layers into normalized scores;
- cache web-ready tiles.

### Route engine
- start/end selection;
- multi-layer cost calculation;
- candidate route generation;
- resource constraints;
- route statistics and explanation.

### Backend
- layer metadata;
- route request;
- route profile/time/distance/risk output;
- cached scenario support.

### Frontend
- layered Mars map;
- start/end placement;
- route comparison;
- elevation/slope profile;
- science/hazard stops;
- resource budget controls;
- astronaut “mission brief.”

## AI/ML opportunity

Optional but useful:

- natural-language mission goal → route preference weights;
- ranking science stops;
- summarizing route risks from computed metrics;
- CV/terrain classification if labels/resources make it realistic.

Avoid putting an LLM in charge of path geometry or safety-critical calculations.

## 48-hour MVP

1. Pick **one local Mars region** with good data coverage.
2. Load 3–4 layers only.
3. Create a grid cost surface.
4. Generate safest vs science-rich/shortest routes.
5. Add an oxygen/time budget and let it constrain feasible routes.
6. Build map + route profile.
7. Prepare one scripted Marswalk scenario.

## Evaluation

- route should avoid synthetic/known high-cost zones;
- unit tests for slope/cost calculations;
- compare shortest path vs risk-aware path;
- sensitivity to weight/resource changes;
- inspect data alignment;
- expose missing/low-resolution zones rather than hiding them.

## Team fit

- **Hưng:** multi-objective scoring/optimization and evaluation.
- **Việt:** data integration and scenario logic.
- **Bích:** GIS/environmental interpretation where transferable, though planetary geology remains a gap.
- **Hiếu:** map, route service and UI.
- **Tiểu An:** mission/hardware operational constraints and physical-system framing.

## Risks

- Different resolution/projection/coverage across Mars datasets.
- Using “current conditions” without suitable localized data.
- Spending too much time on 3D.
- Presenting a heuristic route as operationally safe.
- Too many mission layers cluttering the product.

## Recommendation

**Important dark horse.** It has one of the strongest native simulations in the 14 challenges. It could rise materially if NASA supplies well-aligned layers or a recommended ROI on 2026-10-28.
