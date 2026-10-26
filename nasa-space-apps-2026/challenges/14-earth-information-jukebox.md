# 14 — The Earth Information Jukebox

**Difficulty:** Intermediate · Beginner/Youth  
**Subjects:** Arts & Multimedia · Earth Science · Software  
**NeuraX preliminary score:** **7.4/10 — Tier B+**  
**Current v2 position:** **#11**  
**Status:** Summary available; full 2026 brief/resources expected 2026-10-28.

## Confirmed challenge intent

NASA's Earth Information Center (EIC) creates visualizations of our changing planet. The challenge asks teams to make Earth science more accessible and multisensory by translating visual information into sound: build an **“Earth Jukebox”**—an interface, script, or application that pairs EIC visual frames with **dynamic sonifications generated in real time**.

Sources:
- https://www.spaceappschallenge.org/2026/challenges/
- https://nasaspaceapps.ae/challenges

## What makes this challenge interesting

A strong entry should create a mapping between Earth-science information and sound that is:

- understandable;
- repeatable;
- meaningful rather than arbitrary;
- useful for accessibility and/or pattern exploration;
- engaging in a live demo.

## NeuraX concept: “Earth Resonance”

An interactive EIC viewer where the user selects an Earth-science visualization and explores it visually and sonically.

### Timeline sonification

As time advances through frames, selected global/regional statistics control sound parameters.

### Spatial scan

A cursor or scan line moves across the image/map. Pixel/region values are translated to sound so users can hear gradients, hotspots, boundaries or change.

### Compare mode

Two regions or timestamps produce contrasting sound signatures while the visual frames remain linked.

The mapping must be documented so sound encodes data rather than acting as soundtrack.

## Candidate official resources — verify 2026-10-28

The challenge explicitly centers on **Earth Information Center visual frames**, but the full resource list should clarify:

- which EIC visualizations/frames are provided;
- whether raw underlying values are available or only images/video frames;
- metadata, color scales and units;
- expected sonification examples/libraries;
- accessibility guidance.

Sonifying underlying numerical data is more scientifically defensible than inferring values from rendered colors unless the color mapping is precisely known.

## Sonification design principles

### Preserve semantics

Use sound parameters with intuitive or learnable relationships to data.

### Keep dimensions separable

Possible dimensions include pitch, loudness, rhythm/event rate, timbre, stereo position and duration.

### Make the mapping inspectable

A user should be able to pause and see:

`data value → normalized value → sound parameter`

### Avoid misleading aesthetics

Separate **data encoding** from optional artistic accompaniment.

## AI/ML opportunity

AI is not required, but NeuraX could add a secondary layer:

- identify interesting regions/times for sonification;
- summarize the data pattern in text alongside sound;
- personalize sound mapping;
- cluster temporal patterns and assign consistent audio motifs.

Generative music should not obscure the underlying data encoding.

## Technical decomposition

### Data/image adapter
- load EIC frames and metadata;
- access raw values where possible;
- normalize values consistently;
- define regions/time steps.

### Sonification engine
- deterministic data-to-audio mapping;
- Web Audio API or equivalent real-time synthesis;
- user-selectable mapping presets;
- playback/scrub controls.

### Frontend
- EIC visual frame;
- timeline;
- play/pause/scrub;
- legend for sound encoding;
- spatial scan control;
- accessibility options;
- compare mode.

## 48-hour MVP

1. Choose **one EIC dataset/story** with a clear temporal or spatial pattern.
2. Confirm raw numeric data or faithful color/value mapping.
3. Define only 2–3 sonification dimensions.
4. Build deterministic real-time playback synchronized with the visual frame.
5. Add spatial or temporal exploration.
6. Create an explicit audio legend/tutorial.
7. Test whether users can extract information from sound.

## Evaluation

Useful tests include:

- can users distinguish high vs low values through audio?
- can users detect a peak/change point without seeing the visualization?
- is the mapping consistent and learnable?
- does audio preserve ordering/trends from the source data?
- accessibility/usability feedback from real users where possible.

## Team fit

- **Hiếu:** interactive web/audio implementation.
- **Hưng/Việt:** data normalization, anomaly extraction, evaluation and optional intelligent navigation.
- **Bích:** Earth-science interpretation and meaningful environmental variable selection.
- **Tiểu An:** hardware/audio interface experimentation could be possible, though not required.

### Gaps

- no confirmed audio/sonification specialist;
- no dedicated accessibility expert;
- less use of the team's strongest ML/simulation advantage.

## Risks

- producing attractive music that carries little data;
- sonifying RGB colors rather than scientific values;
- too many audio dimensions becoming noise;
- accessibility claims without user testing;
- venue/browser audio issues during judging.

## Recommendation

**Creative second-tier option with excellent demo potential.** It becomes much more attractive if NASA supplies underlying numeric EIC data and strong accessibility/sonification resources, but it currently underuses NeuraX's simulation/AI/hardware combination relative to the top candidates.
