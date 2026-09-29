# Graph schema reference

The canonical snapshot is `station-mall-graph.json` (`schemaVersion: "1.0"`). Keep its IDs and field names intact when making derived exports.

## Top-level collections

- `stations`: canonical railway stations. `id`, `nameZh`, `nameEn`, `aliases`, `lines`, `layout`, `sourceRefs`, `reviewStatus`, and `evidence` are the main fields. `layout.x/y` are schematic drawing positions, not WGS84.
- `malls`: extracted place/building nodes. IDs use the `building-*` prefix. `category` may remain the generic `building`; do not relabel a node as a mall without separate evidence. `imageX/imageY` are source-image pixels only. `coordinateReviewed` concerns image placement, not geography.
- `railEdges`: schematic railway connections, distinct from walkway evidence.
- `stationWalkEdges`: separate station-to-station records, including same-physical-station relations.
- `walkEdges`: source station/building or building/building walking-relation records. `sourceCrop` is a pointer into the originating project; the crop files are not included in this package. `sourceRegion` can be approximate or incorrect, and remains raw provenance rather than a verified address. Each keeps `from`/`to` references, `relation`, `mode`, `reviewStatus`, endpoint and topology flags, source crop/region, waypoints, and evidence. `waypoints` are not geographic unless an independent schema explicitly says so; this snapshot has no WGS84 geometry.
- `stationMallIndex` and `mallStationIndex`: convenience indexes. They are derived lookups, not stronger evidence than the referenced edge records.
- `sources`, `scope`, `idPolicy`, and `qualityPolicy`: provenance, declared counts, ID/coordinate constraints, and display rules.

## Review status

Preserve statuses literally. `candidate` is unresolved. `image_confirmed` means an image relationship was reviewed; it does not prove current access, surface continuity, route accessibility, or full rain protection. `official_access_only` records official access/location evidence only. Review evidence and route-coverage evidence are separate claims.

When summarizing an indexed relation, inspect every referenced `edgeId`. A multi-edge `via` relation is confirmed only if the direct station-to-first-place edge and every subsequent covered relationship are independently confirmed. Never promote a candidate first edge because a later building-to-building edge is confirmed.

## Geographic data

No `lat`/`lng` fields are present in this snapshot. Never derive them from image pixels, schematic layout positions, labels, guessed centroids, or UI positions. A future geographic addition must carry an independent source, verification date, and explicit review state. Keep it separate from image-coordinate review.
