# 12 — Planet X and SPHEREx

**Difficulty:** Advanced  
**Subjects:** Astrophysics · Planets & Moons · Software  
**NeuraX preliminary score:** **7.8/10 — Tier B+**  
**Current v2 position:** **#13**  
**Status:** Summary available; full 2026 brief/resources expected 2026-10-28.

## Confirmed challenge intent

NASA's SPHEREx mission has been mapping the whole sky every six months in **102 near-infrared bands**, producing imagery/data for more than a billion objects. Objects such as comets, asteroids, stars, brown dwarfs and potentially new planets can reveal themselves through change or apparent motion between observations. NASA asks for a **public-facing web tool** that displays SPHEREx sky imagery and makes temporal changes easy for anyone to inspect.

Sources:
- https://www.spaceappschallenge.org/2026/challenges/
- https://nasaspaceapps.ae/challenges

## Important interpretation

The title says “Planet X,” but the published summary does **not** require a team to discover a new planet. The confirmed deliverable is a public-facing temporal exploration tool for SPHEREx imagery. Any automated candidate-detection feature should therefore be framed as helping users inspect change, not as claiming discovery without scientific validation.

## NeuraX concept: “SPHEREx Blink”

A web sky viewer designed around the classic astronomy “blink comparator” idea, modernized for multi-epoch/multi-band SPHEREx data.

### Core interaction

`navigate/search sky → choose two epochs → blink/swipe/difference → inspect candidate moving/changing sources → view multi-band evidence → save/share candidate`

### Optional AI assistance

Rather than “AI discovers Planet X,” use AI to **rank interesting candidate changes** for human inspection.

Candidate ranking factors could include:

- positional shift between epochs;
- brightness change;
- consistency across nearby bands;
- source morphology/quality flags;
- cross-match status with known objects if official resources permit.

## Candidate data/resources — verify after 2026-10-28

The full resource package should clarify which SPHEREx products are expected, access methods, file formats/coordinate metadata, sample sky regions, expected handling of 102 bands and whether catalogs are in scope.

Potential implementation technologies may involve FITS, WCS/sky coordinates, catalog cross-matching and web-suitable image pyramids—but these are contingent on supplied products.

## Analytical possibilities

### Baseline

- align images to a common sky coordinate frame;
- normalize display/brightness appropriately;
- enable blink/swipe/difference views;
- show timestamps/bands/source metadata.

### Candidate change detection

- image differencing after registration;
- source detection per epoch;
- nearest-neighbor/cross-epoch matching;
- motion vectors;
- variability score;
- quality/artifact rejection.

## 48-hour MVP

1. Use **one or a few small sky regions**, not the whole archive.
2. Load two epochs with a manageable subset of bands.
3. Implement coordinate-aligned blink/difference.
4. Add a basic candidate-change detector or precomputed candidate list.
5. Build candidate inspection cards with temporal/multi-band plots.
6. Validate against known moving/variable objects if examples are provided.

## Evaluation

- image registration residual/error;
- recovery of known moving/variable examples;
- false positives from artifacts/noise;
- candidate ranking precision on a manually labeled small set;
- coordinate-transform verification.

## Team fit

- **Hưng/Việt:** CV/change detection, candidate ranking and evaluation.
- **Hiếu:** sky viewer/API.
- **Bích:** limited direct domain advantage.
- **Tiểu An:** limited native hardware contribution.

## Domain gaps

- astronomy data formats and World Coordinate System concepts;
- interpreting motion/variability scientifically;
- artifact rejection;
- potentially very large data volume.

## Recommendation

**High-upside AI/data project but weaker whole-team fit.** It becomes more attractive if the full brief provides prepared cutouts, catalog helpers or example moving objects that sharply reduce astronomy/data-engineering overhead.
