# 08 — Flame in Freefall: AI-Powered Fire Safety Insights from Microgravity Combustion Data

**Difficulty:** Advanced · Intermediate  
**Subjects:** Space Exploration  
**NeuraX preliminary score:** **8.0/10 — Tier A-**  
**Status:** Summary available; full 2026 brief/resources expected 2026-10-28.

## Confirmed challenge intent

NASA has accumulated decades of microgravity combustion experiments. The challenge asks for an **interactive AI-powered dashboard** that helps users find, summarize, rank, interpret, and turn these results into fire-safety insights for human space exploration.

Official page:
- https://www.spaceappschallenge.org/2026/challenges/flame-in-freefall/

## Why this is attractive for NeuraX

Among all 14 challenges, this is probably the most explicit **AI knowledge-system** challenge. It naturally supports:

- document/data ingestion;
- structured extraction;
- semantic search;
- ranking;
- retrieval-augmented generation;
- evidence-grounded summarization;
- dashboard visualization.

However, a generic “upload PDFs → chatbot” submission would be weak. The challenge specifically asks for **fire-safety insight**, so the system needs domain-aware structure and trustworthy provenance.

## NeuraX concept: “MicroFlame Insight Engine”

An evidence-grounded research dashboard that transforms experiment records into comparable “evidence cards.”

### User flow

`ask a fire-safety question → retrieve relevant experiments → rank evidence → compare conditions/results → synthesize insight → show sources and uncertainty`

The answer should contain **source-linked experimental evidence**, not only prose.

## Candidate data/resources — verify on 2026-10-28

The full resource package is crucial. Potential resource types may include:

- experiment descriptions and metadata;
- technical reports/publications;
- tabular experimental measurements;
- images/video;
- mission/experiment identifiers;
- NASA fire-safety or combustion knowledge resources.

Do not build an ingestion pipeline around assumed sources until the official corpus is known.

## Recommended AI architecture

### 1. Ingestion and normalization

Convert supplied resources into a common schema including experiment, conditions, measured outputs, findings, limitations and source citation.

### 2. Retrieval

Use hybrid retrieval if feasible:

- keyword/BM25-style search for exact technical terms;
- embedding retrieval for semantic similarity;
- metadata filters for experiment conditions.

### 3. Ranking

Rank experiments by query relevance and transparent metadata/evidence criteria.

### 4. Grounded synthesis

LLM output should be generated from retrieved evidence and include citations/experiment IDs. The model should explicitly say when evidence is insufficient or conflicting.

### 5. Comparison view

A side-by-side table of experiment conditions and outcomes may be more valuable than another chatbot pane.

## 48-hour MVP

1. Ingest a **small, high-quality subset** of the official corpus.
2. Define the experiment schema manually before automating extraction.
3. Build hybrid or semantic retrieval.
4. Create 15–30 benchmark questions with known relevant sources.
5. Add evidence-grounded synthesis with citations.
6. Build a comparison screen for 2–4 experiments.
7. Demo one safety question from query → evidence → synthesis.

## Evaluation

A serious AI submission should measure more than “the chatbot looks good.”

Suggested checks:

- retrieval recall@k / hit rate;
- citation correctness;
- faithfulness of generated claims to retrieved sources;
- metadata extraction accuracy;
- manual review of ranking;
- explicit abstention when sources do not support an answer.

## Team fit

- **Hưng/Việt:** RAG/retrieval, ranking, structured extraction, evaluation.
- **Hiếu:** dashboard/search application and deployment.
- **Bích:** limited direct domain overlap; can support scientific-evidence discipline but not combustion expertise.
- **Tiểu An:** hardware/fire-safety systems perspective may help framing, but the core remains knowledge software.

## Domain gap

Combustion/fire science is a meaningful gap. The team can build the information system, but deciding which experimental variables/findings matter requires careful reading or a mentor.

## Risks

- Building a generic RAG chatbot with little domain structure.
- Hallucinated safety claims.
- Poorly parsed tables/figures/PDFs.
- No objective retrieval/evaluation benchmark.
- Attempting to ingest the entire corpus instead of curating a demonstrable slice.
- “Ranking” evidence using an opaque LLM score with no defensible meaning.

## Recommendation

**Best AI-first option, but not the strongest overall five-person team fit.** Keep it in the shortlist if the official corpus is unusually clean or if NeuraX decides to prioritize AI research over environmental/GIS/simulation breadth.
