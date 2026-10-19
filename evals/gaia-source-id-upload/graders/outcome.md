---
type: llm
---
PASS only if all of these hold:
1. source_id is read and kept as a 64-bit integer (or an exact string) from the CSV through the query result, and the answer warns that routing IDs through floating point (for example a default float column or a pandas float conversion) can corrupt values above 2**53.
2. The query selects from gaiadr3.gaia_source by exact ID, for example by uploading the ID table and joining on source_id, not by a cone search or a TOP-limited sample.
3. After the query the answer checks delivery: the returned count or ID set against the 400 inputs with missing IDs reported, or the job status / QUERY_STATUS / overflow state.
4. The answer does not turn parallax into a distance by inversion, since nobody asked for distances.
