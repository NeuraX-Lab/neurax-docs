# 13 — Space Mission Design Game

**Difficulty:** Intermediate · Beginner/Youth  
**Subjects:** Games  
**NeuraX preliminary score:** **6.5/10 — Tier B-**  
**Current v2 position:** **#10**  
**Status:** Summary available; full 2026 brief/resources expected 2026-10-28.

## Confirmed challenge intent

Space missions require trade-offs across mission objectives, spacecraft design, instruments, launch vehicles, budgets, power, mass, communications, and orbital constraints. NASA asks teams to build an **interactive game** in which players design, manage, and simulate a complete mission while making engineering decisions and observing how those decisions affect mission success.

Sources:
- https://www.spaceappschallenge.org/2026/challenges/
- https://nasaspaceapps.ae/challenges

## Core product problem

The challenge is fundamentally about **systems thinking**. A strong game needs interconnected constraints so that there is no single obvious “max everything” strategy.

`mission objective → choose architecture/components → consume budget/mass/power → check constraints → simulate operations/events → score science/mission success → explain trade-offs`

## NeuraX concept: “Mission Architect”

A browser-based mission design game where the player receives a mission brief—e.g., lunar orbiter, Mars science orbiter, asteroid flyby—and assembles a mission under limited resources.

### Player choices

- mission destination/objective;
- spacecraft bus class;
- payload/instruments;
- launch vehicle;
- power system;
- communication system;
- propellant/maneuver margin;
- optional redundancy/reliability upgrades.

### Constraint dashboard

Show live budgets:

- total cost;
- launch mass;
- power generation/consumption;
- data generation/downlink capacity;
- mission duration;
- risk/reliability proxy;
- science score.

## Candidate NASA resources — verify 2026-10-28

The full brief may provide component data, simplified formulas, mission examples, launch-vehicle information or learning resources. Those should drive the game model rather than invented “realistic” values.

## Simulation design

### Recommended: constraint model, not full physics simulator

Use transparent rules such as:

- `total_mass <= launch_capacity`
- `peak_power_demand <= available_power`
- `daily_data_generation <= storage + downlink_capacity`
- mission-specific instrument requirements;
- simple delta-v/trajectory budget only if expected by the full brief;
- events whose probabilities depend on design choices.

### Scoring

Use multiple objectives:

- science return;
- mission reliability;
- budget efficiency;
- schedule/complexity;
- constraint violations.

A post-mission debrief should explain the largest contributors to success/failure.

## AI/ML opportunity

Low for the core system. Optional uses:

- tutor explaining trade-offs;
- adaptive scenarios;
- natural-language mission brief converted to objectives;
- automated debrief from deterministic simulation logs.

## 48-hour MVP

1. Support **one mission type**.
2. Create 12–20 component cards across 4–5 categories.
3. Implement mass, power, budget and data/communication constraints.
4. Add a short mission simulation with 3–5 events.
5. Provide success/failure debrief.
6. Test multiple viable strategies.

## Team fit

- **Hiếu:** game engine/web implementation.
- **Hưng/Việt:** constraint modeling, optimization/balance analysis and testing.
- **Tiểu An:** strong physical-system/hardware perspective for spacecraft trade-offs.
- **Bích:** limited direct domain leverage unless mission/environment scenarios create a role.

### Main gaps

- no dedicated game designer;
- no confirmed spacecraft systems/orbital-mechanics specialist;
- mission balancing/content design can consume more time than expected.

## Risks

- scope explosion across entire mission lifecycle;
- arbitrary component values/game rules;
- building a configuration form rather than a game;
- trajectory/orbital mechanics becoming too sophisticated;
- graphics/polish competing with simulation correctness.

## Recommendation

**Strong native simulation, but not a preferred NeuraX challenge.** It is attractive if the official brief supplies a clean simplified engineering model; otherwise game balance and systems-domain work may consume the event while underusing Environmental Science/GIS.
