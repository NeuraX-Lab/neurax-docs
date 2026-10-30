# NeuraX Repository Strategy

> **Decision date:** 2026-10-26  
> **Decision:** Use a hybrid repository model: separate team/research/decision knowledge from product implementation.

## Organization structure

```text
NeuraX-Lab/
├── .github/                # organization profile and shared community files
├── neurax-docs/            # team knowledge, research, decisions, competition analysis
├── nasasac26-neurax/       # NASA Space Apps 2026 product/code
└── vaic-2026-template/     # existing repository
```

## Rule of ownership

### `neurax-docs` answers **WHY / WHAT SHOULD WE BUILD?**

Examples:

- team profile and capability matrix;
- all 14 NASA Space Apps challenge dossiers;
- ranking history and reassessments;
- competitor research;
- previous Global/Local winner research;
- challenge-selection rationale;
- decision logs;
- research/pitch notes that are not implementation-specific.

### `nasasac26-neurax` answers **HOW DID WE BUILD IT?**

Examples:

- product source code;
- frontend/backend;
- AI/model implementation;
- geospatial processing;
- data pipelines;
- technical architecture;
- methodology of the selected solution;
- API/deployment documentation;
- demo assets.

### `.github` answers **WHO IS NEURAX AS AN ORGANIZATION?**

Examples:

- public organization profile;
- shared issue/PR templates where appropriate;
- shared contributing/community defaults.

## Target product layout after challenge selection

```text
nasasac26-neurax/
├── frontend/
├── backend/
├── ai/
│   ├── models/
│   ├── inference/
│   ├── experiments/
│   └── notebooks/
├── data/
│   ├── raw/
│   ├── processed/
│   └── sample/
├── geospatial/
├── scripts/
├── docs/
│   ├── architecture.md
│   ├── methodology.md
│   ├── data-pipeline.md
│   ├── api.md
│   └── deployment.md
├── demo/
├── .github/workflows/
├── README.md
├── LICENSE
├── .gitignore
└── docker-compose.yml
```

Directories should be created only when needed.

## 2026-10-30 — preparation-phase clarification

The user explicitly requested docs and Mermaid architecture planning inside `neurax-docs` before product implementation. Proposed architecture, data contracts, member setup, hardware BOMs and scope/optimization decisions therefore live under `nasa-space-apps-2026/planning/` for this phase. These are proposals, not as-built specifications. When implementation begins, maintain the actual architecture/methodology in `nasasac26-neurax` and link back to these decisions.

Reusable repo-local planning skills live in `.agents/skills/`, indexed by [skills-catalog.md](skills-catalog.md). They contain Markdown instructions only and do not deploy code, create external tasks or run scheduled jobs.

## Branch strategy

### Product repository

```text
main
└── dev
    ├── feat/frontend-dashboard
    ├── feat/backend-api
    ├── feat/ai-pipeline
    └── feat/geospatial
```

Feature branches merge into `dev`; stable demo-ready work moves from `dev` to `main`.

### Documentation repository

Use lightweight topic branches for substantial research or structural changes, for example:

```text
main
├── research/2026-challenge-audit
├── research/past-winners
└── docs/team-update
```

## Migration policy

1. Copy research into `neurax-docs` first.
2. Verify every destination file.
3. Remove duplicated research from the product repo only after verification.
4. Keep technical/product documentation in `nasasac26-neurax`.
5. Avoid maintaining duplicate authoritative copies.
6. Link the product README back to the knowledge repository for challenge-selection rationale.
