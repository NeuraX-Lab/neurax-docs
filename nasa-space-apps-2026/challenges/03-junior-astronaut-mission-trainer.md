# 03 — Build a Junior Astronaut Mission Trainer

**Difficulty:** Intermediate · Beginner/Youth  
**Subjects:** Games · Planets & Moons · Software · Space Exploration · Sun  
**NeuraX preliminary score:** **6.7/10 — Tier B-**  
**Status:** Summary available; full 2026 brief/resources expected 2026-10-28.

## Confirmed challenge intent

NASA wants an interactive game or application for students that makes the engineering trade-offs of running a lunar or Martian outpost tangible and fun. The published summary specifically mentions competing demands such as **life support, radiation shielding, power, and food production**, with choices affecting whether the mission succeeds or fails.

Sources:
- https://www.spaceappschallenge.org/2026/challenges/
- https://nasaspaceapps.ae/challenges

## Product interpretation

This should not become a spreadsheet with space graphics. The learning outcome is understanding **trade-offs and coupled systems**. A strong game should make the player feel that improving one subsystem consumes resources or creates consequences elsewhere.

A useful design loop is:

`observe state → choose action → spend scarce resource → simulate consequences → explain why → adapt`

## NeuraX concept: “Outpost Control”

The player manages a small Moon or Mars base across a sequence of mission days/sols.

### State variables

- crew health/safety;
- oxygen/water/food;
- stored electrical energy;
- solar generation;
- radiation exposure;
- habitat integrity;
- spare mass/materials;
- science/productivity score.

### Player decisions

Examples:

- allocate energy between life support, science and food production;
- schedule EVAs around environmental hazards;
- spend mass/resources on shielding versus equipment;
- expand crew capacity versus conserve reserves;
- respond to a dust/radiation/power event.

The educational layer should explain **why** a decision succeeded or failed using NASA-backed facts rather than arbitrary game rules.

## Candidate data/content — verify 2026-10-28

Potential resource categories include:

- lunar/Martian environment conditions;
- solar illumination / power assumptions;
- radiation information;
- life-support concepts;
- mission architecture / habitat trade-off references.

The official full brief may supply simplified values or specific NASA educational resources. Use those instead of inventing realism that cannot be defended.

## Technical approach

### Simulation engine

Keep it deterministic and explainable:

- state vector;
- action costs/effects;
- event system;
- success/failure conditions;
- difficulty tuning through parameters.

A lightweight rules engine is better than an ML model for the core simulation.

### Frontend

- control-room style dashboard;
- clear resource meters;
- event cards;
- decision modal with predicted trade-offs;
- post-decision explanation;
- end-of-mission debrief showing which systems caused success/failure.

### AI opportunity

Optional rather than central:

- adaptive tutor explaining trade-offs;
- difficulty adaptation based on player behavior;
- natural-language debrief grounded in simulation logs;
- NPC mission-control assistant.

Avoid AI making authoritative engineering calculations unless those calculations are defined and testable.

## 48-hour MVP

1. Choose **one destination** (Moon *or* Mars).
2. Implement 4 coupled systems: power, life support, food, radiation.
3. Build 6–10 mission events.
4. Create a 10-turn mission loop with clear win/loss criteria.
5. Add educational explanations after each decision.
6. Test balance with scripted play-throughs.

## Evaluation

For a game, success is not only correctness of code. Test:

- Is there more than one viable strategy?
- Do decisions produce understandable consequences?
- Are the scientific explanations accurate?
- Can a new player understand the system in <2 minutes?
- Does the player learn at least 2–3 real mission trade-offs?

## Team fit

### Strengths
- Hiếu can implement the state engine and polished web interface.
- Hưng/Việt can help model constraints, testing and adaptive tutor features.
- Tiểu An can contribute strongly to physical-system thinking, game flow and user testing.

### Gap

The team does not currently have a dedicated game designer or space-systems engineer. Balance and educational UX can take more time than expected, and AI/ML expertise is not required for the core solution.

## Risks

- Building too many systems and ending with an unbalanced prototype.
- Scientific numbers that look realistic but are arbitrary.
- “Game” becomes a dashboard with buttons and no meaningful decision strategy.
- Excessive 3D/graphics work.
- Similarity to many other resource-management games.

## Scorecard

| Dimension | Score / 10 | Comment |
|---|---:|---|
| Team fit | 7.0 | Technically feasible; game design is the main gap. |
| AI/data leverage | 5.0 | Useful only as a secondary layer. |
| GIS/EO leverage | 2.0 | Little opportunity. |
| 48h feasibility | 8.0 | Strong if simulation scope is aggressively limited. |
| Demo/story impact | 8.5 | Interactive game is easy to present. |
| NASA-data centrality | 6.5 | Depends on how strongly rules are grounded in NASA resources. |
| Differentiation ceiling | 6.5 | Strong UX/design needed to stand out. |

## Recommendation

**Good fallback, not a primary NeuraX target.** Choose it if the team wants a fun education/product challenge with low data-engineering risk. For NeuraX's current ambitions, Earth-observation/data-analysis challenges make better use of the team's technical strengths.
