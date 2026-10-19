---
type: llm
---
PASS only if all of these hold:
1. The code builds an astropy Time on the TDB scale from the BTJD values using the 2457000-day offset, e.g. Time(2457000, btjd, format="jd", scale="tdb"), a BJDREFI/BJDREFF two-part construction, or an equivalent that keeps the offset and the small values as separate parts.
2. The answer says BTJD is an offset of BJD_TDB, so the values are already barycentric and no additional barycentric or light-travel-time correction should be applied.
3. The answer does not claim that converting a time to TDB with .tdb by itself produces a barycentric BJD.
4. The answer names at least one product check: header keywords such as TIMESYS, TIMEREF/TREFPOS or BJDREFI/BJDREFF, or masked/NaN TIME values or quality-flagged cadences.
