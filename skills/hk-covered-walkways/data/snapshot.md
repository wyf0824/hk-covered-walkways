# Data snapshot

Snapshot date: 2026-09-29 (Asia/Hong_Kong)

The packaged canonical graph is schema version 1.0 and contains 98 stations, 126 building records, and 110 source walk edges. It also contains 124 rail edges and 2 separate same-station walk/transfer records. The graph's IDs, scope, and provenance fields are preserved. `data/stations.json` and `data/places.json` add name-search URLs to copies of each source record; they retain all original fields.

Observed source statuses in the 110 `walkEdges`:

| Status | Count | Interpretation |
|---|---:|---|
| `candidate` | 93 | Retained for further review; do not treat as a confirmed connection. |
| `image_confirmed` | 13 | Source-image relationship reviewed; not proof of a currently usable, fully covered route. |
| `official_access_only` | 4 | Official source supports an access or location relationship; it does not verify a covered walking path. |

`sourceCrop` values refer to crop images in the originating project; those images are not packaged, so their visual evidence cannot be rechecked from this bundle. Some `sourceRegion` labels are approximate or inaccurate. Do not treat those labels or missing crop references as verified place geography; see the separately dated `official-checks.json`.

There are 106 edges marked `validEndpointIds: true` and 4 marked false. Preserve invalid endpoint records for audit; do not expose them as canonical station/building UI links without resolving their identities.

The 126 building records include 24 with `coordinateReviewed: true`; this flag refers to a point reviewed on the source image. It does not mean latitude/longitude was verified. The graph contains no WGS84 coordinate fields in its current station/building schema. Two APM records (`building-apm` and `building-kwun-tong-apm`) remain unresolved duplicates and must not be merged.

`official-checks.json` is a separate 2026-09-29 supplement for MOKO–Mong Kok East, Pioneer Centre–Prince Edward, apm–Kwun Tong, and Festival Walk–Kowloon Tong. It records official identity, address and listed exits alongside separate connection and coverage claims. These checks do not modify the graph's `reviewStatus`, prove real-world edge geometry, or prove a route is covered end to end.
