# 04 — CLPS Lunar Mission Browser / Lunar Landing Site Navigator

**Published overview name:** CLPS Lunar Mission Browser  
**Current official challenge page heading:** Lunar Landing Site Navigator  
**Difficulty:** Advanced · Intermediate  
**Subjects:** Human Exploration · Moon · Software · Space Exploration  
**NeuraX preliminary score:** **7.6/10 — Tier B+**  
**Status:** Summary available; full 2026 brief/resources expected 2026-10-28.

> **Naming note:** The 2026 all-challenges overview currently labels this challenge “CLPS Lunar Mission Browser,” while the linked NASA Space Apps challenge page is headed “Lunar Landing Site Navigator.” Treat these as the same challenge unless NASA changes the naming in the full release.

## Confirmed challenge intent

Missions near the Moon's south pole have difficult illumination and communication geometry. NASA asks for an intuitive tool that allows mission planners, educators, and the public to compare candidate landing sites and dates while visualizing the **Sun and Earth relative to the local horizon**, helping assess solar-power potential and direct-to-Earth communication windows.

Official page currently available:
- https://www.spaceappschallenge.org/2026/challenges/lunar-landing-site-navigator/

## Why the challenge is technically interesting

This is not merely a map problem. A credible tool combines:

- lunar position/topography;
- time/date;
- Sun/Moon/Earth geometry;
- local horizon obstruction;
- power and communication implications;
- interactive visualization.

The judging value likely comes from turning specialist calculations into an interface that makes mission constraints understandable quickly.

## NeuraX product concept

### “LunaWindow”

A mission-browser interface where the user selects:

1. landing site(s);
2. candidate date/time range;
3. mission duration.

The app produces:

- local 3D/2.5D terrain context;
- Sun elevation/azimuth over time;
- Earth elevation/azimuth over time;
- approximate illumination windows;
- direct-to-Earth visibility windows;
- side-by-side site/date scorecards;
- explanation of why one window is more favorable.

A polished comparison mode could be the central demo: two sites, same date, visibly different power/comms opportunities.

## Candidate resources — verify on 2026-10-28

Likely technical ingredients include:

- lunar topography / digital elevation products, potentially LRO/LOLA-derived;
- planetary geometry/ephemerides, potentially NASA/JPL SPICE or Horizons-style data;
- CLPS mission/site context supplied in the official challenge resources;
- lunar coordinate/reference information.

These are **candidate technologies**, not confirmed required resources until the full brief is released.

## Computational approach

At a conceptual level:

1. Convert candidate landing coordinates into a local reference frame.
2. Obtain Sun and Earth direction vectors as a function of time.
3. Derive local azimuth/elevation.
4. Use local terrain/DEM to estimate horizon angle by azimuth.
5. Mark a body as visible when its elevation is above the terrain horizon.
6. Aggregate visible intervals into power/comms windows.

For the hackathon, scientific honesty matters: if terrain-horizon modeling is simplified, say so and quantify the approximation.

## Technical decomposition

### Geometry service
- date/time → Sun/Earth positions;
- site coordinates → local frame;
- visibility computation;
- window aggregation.

### Terrain/geospatial service
- retrieve/preprocess local lunar DEM;
- horizon profile calculation;
- optional slope/terrain context.

### Backend
- site/date query;
- cached time-series results;
- comparison endpoint.

### Frontend
- lunar map / site selector;
- horizon polar plot or sky-view diagram;
- time-series of Sun/Earth elevation;
- site comparison cards;
- “good power / good comms / trade-off” explanation.

## AI/ML opportunity

Low-to-medium. This is fundamentally a geometry/mission-planning visualization problem. AI should not be forced in.

Potential useful additions:

- natural-language query for site/date comparison;
- ranking candidate windows under user-defined weights;
- explanation layer generated only from computed metrics.

## 48-hour MVP

1. Support a small predefined set of candidate sites.
2. Use official/supplied terrain data at manageable resolution.
3. Calculate Sun/Earth elevation over a selected interval.
4. Implement a simplified but documented horizon model.
5. Render one comparison dashboard.
6. Add a “best windows” summary based on transparent thresholds.

Avoid building a full mission-planning suite.

## Evaluation

- Compare ephemeris results with a trusted reference for sampled timestamps.
- Test known coordinate/time cases.
- Verify horizon calculations on synthetic terrain.
- Unit-test visibility interval logic.
- Show sensitivity to DEM resolution / terrain approximation.

## Team fit

### Strengths
- Hiếu: application engineering and visualization.
- Hưng/Việt: numerical logic, ranking/optimization, validation and data processing.
- Tiểu An: hardware/mission-system perspective and presentation flow.

### Gaps
- Orbital/planetary geometry and lunar geodesy are not current core expertise.
- A mistake in reference frames or horizon geometry can silently produce beautiful but wrong results.

## Risks

- SPICE/ephemeris learning curve.
- Large lunar raster/DEM handling.
- Reference-frame mistakes.
- 3D visualization consuming time without improving correctness.
- Ambiguous relationship between CLPS-specific requirements and the generic navigator concept until the full brief arrives.

## Scorecard

| Dimension | Score / 10 | Comment |
|---|---:|---|
| Team fit | 7.5 | Strong software/data ability, but domain learning is nontrivial. |
| AI/data leverage | 6.0 | Numerical/data work is strong; ML is not central. |
| GIS/EO leverage | 8.5 | Terrain + spatial geometry are central. |
| 48h feasibility | 6.5 | Feasible only with tightly controlled scope/resources. |
| Demo/story impact | 9.0 | Very visual and mission-relevant. |
| NASA-data centrality | 9.0 | NASA lunar/geometry data should be fundamental. |
| Differentiation ceiling | 8.5 | Excellent UX around hard geometry can stand out. |

## Recommendation

**Promising but specialist-risky.** Keep in the second shortlist. It becomes much more attractive if the 2026-10-28 resource package provides ready-to-use site coordinates, DEM subsets, geometry examples, or APIs that reduce setup cost.
