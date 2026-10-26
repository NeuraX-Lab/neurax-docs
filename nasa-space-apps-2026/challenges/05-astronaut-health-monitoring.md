# 05 — Create Health Monitoring Software for Astronauts on Space Missions

**Difficulty:** Intermediate  
**Subjects:** Human Exploration · Software · Space Exploration  
**NeuraX preliminary score:** **7.2/10 — Tier B**  
**Status:** Summary available; full 2026 brief/resources expected 2026-10-28.

## Confirmed challenge intent

Long-duration missions expose astronauts to hazards including radiation, isolation/confinement, altered gravity, and a hostile closed environment. The published summary highlights possible immune, bone, cardiovascular, and behavioral-health effects. NASA asks for software that gathers health indicators and helps astronauts **evaluate and act on their health status** when they may carry more responsibility for recognizing changes themselves.

Sources:
- https://www.spaceappschallenge.org/2026/challenges/
- https://nasaspaceapps.ae/challenges

## Core product problem

The hard part is not creating a dashboard of heart rate and sleep. The product must transform longitudinal indicators into **safe, interpretable, actionable situational awareness** while acknowledging uncertainty and avoiding unsupported medical diagnosis.

For a hackathon entry, the safest framing is a **decision-support / monitoring prototype**, not a diagnostic medical device.

## NeuraX concept: “CrewHealth Sentinel”

A longitudinal monitoring dashboard that organizes multiple indicators into:

- personal baseline;
- recent deviation;
- trend over mission time;
- confidence/data-quality status;
- transparent alert reason;
- recommended next step from a curated protocol library.

Example interaction:

`metric deviation detected → show baseline comparison → show contributing indicators → explain why alert fired → link to protocol/checklist → log astronaut response`

## Candidate indicators/resources — verify after full brief

NASA may provide specific datasets, protocols, or sensor indicators on 2026-10-28. Until then, do not assume a required data schema.

Candidate indicator categories for system design only:

- heart rate / resting heart rate;
- sleep duration/quality;
- activity / workload;
- body mass or musculoskeletal indicators;
- radiation exposure;
- mood/cognitive self-report;
- environmental/context variables.

Potential NASA research ecosystems such as Human Research Program or space-biology resources may become relevant, but the official challenge resource list should drive implementation.

## Analytical approach

### Prefer personal-baseline anomaly detection

Astronaut health is longitudinal and individual. Instead of fixed universal thresholds only:

- estimate a baseline period;
- calculate rolling deviations;
- detect sustained changes rather than single noisy readings;
- combine multiple weak signals cautiously;
- expose the evidence behind alerts.

Possible techniques:

- robust z-score / median absolute deviation;
- EWMA / CUSUM-style drift detection;
- simple multivariate anomaly score;
- trend detection;
- missing-data and sensor-quality flags.

### Avoid

- black-box “disease prediction” without validated labels;
- LLM diagnosis;
- fabricated clinical thresholds;
- presenting synthetic data as medically validated evidence.

## Technical decomposition

### Data layer
- timestamped observation schema;
- unit normalization;
- quality/missingness flags;
- baseline vs mission-period context.

### Analytics
- baseline estimator;
- trend/deviation module;
- alert rules;
- confidence/explanation payload.

### Backend
- ingest observations;
- return longitudinal summaries;
- generate explainable alerts;
- protocol lookup.

### Frontend
- crew overview;
- individual timeline;
- alert triage;
- contributing-signal breakdown;
- “what should I check next?” workflow.

### AI opportunity

Moderate-to-high, but constrained by safety:

- anomaly detection;
- multimodal trend summarization;
- retrieval over an official protocol/knowledge corpus;
- natural-language summaries generated from structured data with explicit citations.

## 48-hour MVP

1. Use a small official or clearly synthetic multi-day crew dataset.
2. Pick 4–6 indicators.
3. Build personal baseline + deviation detection.
4. Implement 2–3 transparent alert patterns.
5. Create one astronaut-facing timeline and alert-explanation screen.
6. Connect alerts to a curated action/checklist resource.
7. Clearly label synthetic/illustrative components.

## Evaluation

- Inject known synthetic anomalies and check detection.
- Measure false alerts on stable periods.
- Test robustness to missing samples.
- Verify every alert has a human-readable reason.
- Separate software evaluation from any claim of medical validity.

## Team fit

### Strengths
- Hưng/Việt: anomaly/trend detection, evaluation, explainability.
- Hiếu: monitoring dashboard and data pipeline.
- Tiểu An: hardware/sensing and workflow perspective.

### Major gap

No confirmed medical/physiology specialist. This makes domain validation and responsible claims the biggest risk, not coding.

## Risks

- Health/safety claims exceeding evidence.
- No suitable open longitudinal astronaut dataset.
- Scope exploding across many physiological systems.
- Generic smartwatch dashboard with a space theme.
- LLM hallucination in recommended actions.

## Scorecard

| Dimension | Score / 10 | Comment |
|---|---:|---|
| Team fit | 7.5 | Software/AI fit, but major medical-domain gap. |
| AI/data leverage | 9.0 | Strong longitudinal anomaly-analysis opportunity. |
| GIS/EO leverage | 2.0 | Not relevant. |
| 48h feasibility | 8.0 | Technically feasible with a narrow monitoring scope. |
| Demo/story impact | 8.0 | Clear human-exploration narrative. |
| NASA-data centrality | 7.0 | Depends heavily on the official data/resources supplied. |
| Differentiation ceiling | 7.5 | Explainability + mission context can differentiate. |

## Recommendation

**Interesting AI/software challenge, but not a top NeuraX pick without a domain mentor or strong official medical resource package.** If the full brief provides well-defined indicators, protocols, and sample data, the score can rise substantially.
