---
type: llm
---
PASS only if all of these hold:
1. The answer proposes a compact names-and-ranges index (or an equivalent symbol map) kept in an ignored or scratch location, with a way to regenerate it.
2. The answer proposes a short pointer for the project's instruction file (AGENTS.md, CLAUDE.md or equivalent) and says the index content itself does not go into that file.
3. The pointer or setup includes a staleness rule: regenerate or verify the index after edits, for example by comparing a stored file hash.
4. The answer asks for approval, or says it would wait for approval, before editing the instruction file.
5. The answer does not claim measured token savings or quality gains.
