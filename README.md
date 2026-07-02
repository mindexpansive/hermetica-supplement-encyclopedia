# Hermetica Supplement & Ingredient Encyclopedia — Open Dataset

An evidence-curated, openly-licensed dataset of supplement and botanical ingredient
profiles plus supplement–drug interaction data, published by
[Hermetica Superfoods](https://hermeticasuperfoods.com).

> **Live API & browsable encyclopedia:** https://ingredients.hermeticasuperfoods.com
> **One-box search / interaction checker:** https://ingredients.hermeticasuperfoods.com/search

## What's in it

| Dataset | Records | Description |
|---|---:|---|
| **Ingredients** | 15,659 | Evidence-scored profiles: benefits, mechanism of action, dosing, safety, category, PubMed citation IDs |
| **Interactions** | 121,278 | Pairwise supplement–drug / supplement–supplement interaction records with severity, mechanism, and plain-English guidance |
| **Substances** | 493 | Canonical substance nodes (supplements + common medications) underpinning the interaction graph |
| **Strong-evidence entries** | 1,717 | Tier-1 profiles (evidence score ≥ 7) |

All counts are live as of publication and grow over time — the canonical source is the API below.

## How to get the data

The dataset is served live (always current) from the encyclopedia API under CC BY-NC-SA 4.0:

```bash
# Full ingredient dataset (newline-delimited JSON)
curl https://ingredients.hermeticasuperfoods.com/api/dataset/ingredients.jsonl

# Full interaction dataset
curl https://ingredients.hermeticasuperfoods.com/api/dataset/interactions.jsonl

# CSV variants
curl https://ingredients.hermeticasuperfoods.com/api/dataset/ingredients.csv
curl https://ingredients.hermeticasuperfoods.com/api/dataset/interactions.csv

# Structured JSON API (search, per-ingredient, interaction pairs, PubMed cites)
curl "https://ingredients.hermeticasuperfoods.com/api/v1/search?q=ashwagandha"
curl "https://ingredients.hermeticasuperfoods.com/api/v1/stats"
```

Or reproduce a local copy:

```bash
python3 scripts/fetch_dataset.py --out ./data
```

A 50-row sample of each dataset lives in [`data/`](./data) so you can inspect the
schema without downloading the full corpus.

## Schema (ingredients)

Each ingredient record includes (non-exhaustive): `slug`, `name`, `canonical_name`,
`category`, `evidence_score` (0–10), `short_answer`, `health_benefits`, `mechanism_of_action`,
`dosage`, `safety`, `pubmed_ids`, `url`. See the sample file for the exact live shape.

## Schema (interactions)

Each interaction record includes: `substance_a`, `substance_b`, `severity`
(`contraindicated` / `major` / `moderate` / `minor` / `safe`), `mechanism`,
`plain_english`, `citation_count`, `url`.

## License

**CC BY-NC-SA 4.0** — Creative Commons Attribution-NonCommercial-ShareAlike 4.0.
You may share and adapt for non-commercial use with attribution. See [`LICENSE`](./LICENSE).

## How to cite

See [`CITATION.cff`](./CITATION.cff). Short form:

> Hermetica Superfoods Research Team (2026). *Hermetica Supplement & Ingredient
> Encyclopedia Dataset.* https://ingredients.hermeticasuperfoods.com

## Disclaimer

Educational reference only — not medical advice. Interaction severities and evidence
scores are derived from published research (PubMed-indexed) and automated curation.
Always consult a healthcare professional before combining supplements with medication.
