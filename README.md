# NeuraX Knowledge Base

`neurax-docs` is the shared research and decision repository for **NeuraX-Lab**.

It answers **why** we choose a direction and **what** we should build. Product implementation belongs in the corresponding project repository, such as [`nasasac26-neurax`](https://github.com/NeuraX-Lab/nasasac26-neurax).

## Current focus

### NASA Space Apps Challenge 2026

NeuraX is evaluating all 14 published 2026 challenges before locking the final project. The current research is intentionally versioned because the complete challenge statements/resources are expected on **2026-10-28**.

Current provisional shortlist after the 2026-10-26 team reassessment:

1. **Field Shift: Adapting Farms with NASA Data** — working concept: *NeuraX AgroTwin*
2. **Earth Analog Locations** — working concept: *NeuraX TerraTwin*
3. **Harmonization of MODIS and VIIRS Hot Spots** — working concept: *NeuraX FireSense*

These are not final selections. See the ranking history and decision log for the reasoning.

## Repository map

```text
neurax-docs/
├── team/
│   └── team-profile.md
├── governance/
│   └── repository-strategy.md
└── nasa-space-apps-2026/
    ├── README.md
    ├── challenges/
    ├── rankings/
    ├── competitor-research/
    ├── past-winners/
    ├── decision-log.md
    └── final-selection.md
```

## Documentation ownership

- **`neurax-docs`** — team baseline, challenge research, rankings, competitor/winner research, decisions and selection rationale.
- **`nasasac26-neurax`** — frontend/backend/AI/geospatial implementation, architecture, methodology, APIs, data pipeline, deployment and demo assets.
- **`NeuraX-Lab/.github`** — organization profile and shared community defaults.

## Evidence convention

NASA Space Apps 2026 research separates:

- **Confirmed** — stated in official NASA Space Apps material or the published challenge overview.
- **Candidate / verify** — plausible datasets, APIs, methods or interpretations that must be checked against the full brief.
- **NeuraX proposal** — our own solution concept, not an official NASA requirement.

## Team

See [`team/team-profile.md`](team/team-profile.md) for the team baseline used in challenge-fit scoring.
