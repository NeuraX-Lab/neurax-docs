# 01 — Abandoned but not Forgotten

**Official title:** Abandoned but not Forgotten: Storytelling about NASA's Discarded Equipment on the Moon and Mars  
**Difficulty:** Intermediate · Beginner/Youth  
**Subjects:** Astrophysics · Planets & Moons · Space Exploration  
**NeuraX preliminary score:** **6.0/10 — Tier C+**  
**Status:** Summary available; full 2026 brief/resources expected 2026-10-28.

## Confirmed challenge intent

NASA asks participants to tell the story of hardware left across the solar system—particularly equipment on the Moon and Mars, as well as hardware continuing into deep space—and introduce school-age space enthusiasts to the hardware and the science it enabled.

The core problem is therefore **science communication and educational storytelling**, not primarily prediction, optimization, or scientific analysis.

Sources:
- https://www.spaceappschallenge.org/2026/challenges/
- https://nasaspaceapps.ae/challenges

## What a competitive solution probably needs — NeuraX interpretation

A strong entry should be more than a static museum page. The product should make historical hardware explorable and connect four things clearly:

1. **Where is/was the hardware?**
2. **What mission problem did it solve?**
3. **What science did it produce?**
4. **What happened after the mission ended?**

For a school-age audience, the interaction and narrative hierarchy matter more than technical density. An effective product might use a solar-system map/timeline, short mission stories, before/after states, science discoveries, and age-appropriate explanations.

## NeuraX product concept

### “Space Relics Atlas”

An interactive story atlas in which users travel between Moon/Mars/deep-space artifacts. Selecting a relic opens a compact narrative:

`mission → hardware → location/status → key science → legacy → quiz/exploration prompt`

Possible differentiators:

- timeline + spatial view rather than cards only;
- “then vs now” mission status;
- science concepts linked to each object;
- narrated/accessible mode;
- a small grounded Q&A assistant restricted to curated mission records.

The AI component should remain optional. A generic chatbot would add little value unless answers are grounded in a verified mission corpus and designed for children.

## Candidate data/resources — verify after 2026-10-28

Official resource links are not yet published in the full brief. Likely useful source families include:

- NASA mission pages and mission archives;
- NASA image/video libraries;
- Lunar/Mars mission location data where available;
- NASA Solar System Exploration pages;
- mission fact sheets and science-result summaries.

**Do not scrape arbitrary web sources into an educational knowledge base without provenance.** The product should be able to show where a fact came from.

## Technical decomposition

### Data/content
- Curated catalog of 10–30 artifacts for MVP.
- Fields: mission, object/hardware, destination, coordinates if meaningful, launch/operation/end dates, status, science contribution, media, source URL.

### Backend
- Simple content API or static JSON/Markdown content store.
- Optional retrieval layer for grounded Q&A.

### Frontend
- Spatial/timeline navigation.
- Story cards with progressive disclosure.
- Quiz or “mission detective” loop for engagement.

### AI/ML opportunity
- Low-to-medium.
- Best use: grounded summarization at multiple reading levels, semantic search, or question answering over a curated corpus.
- Avoid making generative AI the product's core if it cannot be evaluated for factuality.

## 48-hour MVP

1. Select 8–12 iconic pieces of NASA hardware.
2. Build a curated structured dataset with citations.
3. Implement a timeline + Moon/Mars/deep-space navigation screen.
4. Build one polished story flow per artifact.
5. Add a small knowledge quiz and/or grounded search.
6. Demo one artifact end-to-end and show how the same system scales.

## Evaluation

Because this is an educational/storytelling challenge, evaluation should focus on:

- factual accuracy;
- source provenance;
- reading-level suitability;
- completion/engagement of the story flow;
- usability with the intended age group;
- accessibility.

If AI Q&A is included, create a small question set and measure answer correctness/source support.

## Team fit

### Strengths
- Hưng/Việt can build retrieval, semantic search, content transformation or data tooling if needed.
- Hiếu can own the product/web implementation.
- Tiểu An's product/business/communication perspective is especially useful for audience and story design.

### Weaknesses
- The challenge underuses NeuraX's strongest AI/data/geospatial capabilities.
- Winning quality may depend heavily on UX, illustration, storytelling and educational design—areas where a dedicated designer/educator would help more than another ML engineer.

## Main risks

- Producing a technically impressive system that is less engaging than a simpler, better-designed story experience.
- Hallucinated mission facts from an LLM.
- Spending time on 3D/animation instead of narrative quality.
- Weak differentiation: many teams may build timeline/map/gallery experiences.

## Scorecard

| Dimension | Score / 10 | Comment |
|---|---:|---|
| Team fit | 6.0 | Buildable, but not the team's natural specialty. |
| AI/data leverage | 3.0 | AI is optional rather than intrinsic. |
| GIS/EO leverage | 2.0 | Spatial display helps, but geospatial science is not central. |
| 48h feasibility | 9.0 | A polished MVP is realistic. |
| Demo/story impact | 8.5 | Strong if UX/content is excellent. |
| NASA-data centrality | 7.0 | NASA archives are central to factual storytelling. |
| Differentiation ceiling | 6.0 | Differentiation is mainly design/story quality. |

## Recommendation

**Do not prioritize for NeuraX unless the team explicitly wants an education/storytelling project.** It is safe and feasible, but it gives up much of the team's technical advantage. Keep it as a fallback if the full technical challenges turn out to have unusable data or excessive setup requirements.
