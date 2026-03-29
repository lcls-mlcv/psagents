# JSON schema for one tool call

**Goal:** Make one tool’s inputs machine-checkable.

## Steps (local)

1. Pick a single tool (even hypothetical): e.g. `create_ticket`.
2. Write a JSON object with required fields, types, and one optional field.
3. Add one invalid example and say why it should be rejected.

## What you are practicing

The boundary between “LLM output” and “validated tool args” that builders rely on.
