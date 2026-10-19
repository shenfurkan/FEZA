---
type: llm
---
PASS only if all of these hold:
1. The answer says measure returns value multiplied by self.scale.
2. The answer says scale is the class-level annotated attribute with default 2.0 (an instance attribute of the same name would take precedence).
3. The answer is brief: a few sentences or a short list, with no generated AST skeleton or index, and no classification questions, reality check or results-report template.
