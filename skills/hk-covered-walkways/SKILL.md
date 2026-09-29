---
name: hk-covered-walkways
description: Browse and derive Hong Kong station, place, and covered-walkway data with the complete JSON exports and Google Maps name-search URLs. Use the self-contained graph and exports in this skill package; preserve provenance and review states, and never infer geography or route coverage from map appearance alone.
---

# Hong Kong covered-walkways data workflow

## Packaged data

This skill is self-contained. Its complete graph is `data/station-mall-graph.json`; the full derived exports are `data/stations.json` and `data/places.json`. Browse the complete tables in [STATIONS.md](STATIONS.md) and [PLACES.md](PLACES.md). The package also includes [official checks](data/official-checks.json), [schema and status reference](data/schema-reference.md), [snapshot notes](data/snapshot.md), and [Festival Walk verification](data/verification/festival-walk-verification.md). Do not rely on files outside this skill directory.

Run `python3 generate.py` from this skill directory to regenerate its station/place JSON exports and Markdown tables from the packaged graph. Keep the top-level repository `data/` as the primary sharing entry point; this skill copy is deliberately self-contained for installation and reuse.

## Review a place or connection

Separate these claims: a place exists; a station serves or is near it; an official page gives an address or entrance; an image shows a relationship; and a continuous path is covered. Evidence for one does not establish the others.

For official checks, record the entity and claim, exact official URL, relevant wording or page section, date checked, and narrow status supported. Use `official_access_only` for an official access/location statement without route-coverage evidence. Use image review status only for what an available source image visibly supports. Packaged `sourceCrop` references point to omitted source-image files, so do not claim to have rechecked those images here. Keep unknown, conflicting, and candidate evidence explicit.

For `via` relations, require an independently reviewed station-to-first-place edge and reviewed evidence for each additional covered segment. Retain the full ordered edge ID chain. Never promote a candidate first edge because a later segment is confirmed.

Preserve every canonical ID, source field, `reviewStatus`, `evidence`, and duplicate record. In particular, `building-apm` and `building-kwun-tong-apm` are unresolved same-name APM records; keep both and do not merge them. Festival Walk's separate official checks do not add a node or edge to the current graph.

## Geographic coordinates and covered status

Do not infer latitude/longitude from `imageX/imageY`, schematic `layout.x/y`, screen positions, labels, proximity, or a guessed building center. Add geography only when an independent source provides a specific location and the coordinate is separately checked; record the source and review date. Image-coordinate review is not geographic-coordinate review.

Do not call a relation fully covered because it is indoors, above a station, nearby, shown with a connecting line, or described as official access. Confirm actual route segments and uncovered gaps from suitable evidence. Where evidence is absent, leave coverage unknown or candidate and describe only the narrower verified fact.

Google Maps URLs in derived records are ordinary name searches, not verified entrances, precise pins, or custom overlays. Station queries use the Chinese station name plus `港鐵站 香港`; place queries use the Chinese name plus `香港`. Do not add API keys or imply that search results verify a route.

## Included resources

- [Graph schema and status definitions](data/schema-reference.md)
- [Snapshot counts and known limits](data/snapshot.md)
- [Official-check supplement](data/official-checks.json)
- [Station table](STATIONS.md) and [place table](PLACES.md)
- [Station JSON](data/stations.json) and [place JSON](data/places.json)
