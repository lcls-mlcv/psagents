# Advanced User: Reliability & Evaluation

This track focuses on how to use agents responsibly and effectively in operational settings.

## Key themes

- Prompting patterns that reduce ambiguity
- Evaluation and feedback loops
- Guardrails for safety and correctness

## Prompt design checklist

When you ask an agent to do something, specify:

1. The goal (what "done" means)
2. Inputs (what the agent can rely on)
3. Constraints (what must not be violated)
4. Tools (what actions are allowed)
5. Failure behavior (what to do when uncertain)

## Example: structured request (conceptual JSON)

```json
{
  "goal": "Generate a maintenance checklist",
  "context": {
    "asset_type": "pump",
    "constraints": ["minimize downtime", "follow SOP-123"]
  },
  "tools_allowed": ["read_sop", "query_inventory", "create_ticket"],
  "verification": ["check_sop_compliance", "confirm_required_fields"]
}
```

## Evaluation loop

Operational agents should be measured continuously using metrics such as:

- task success rate
- tool error rate
- time-to-resolution
- post-check compliance (did it follow SOPs?)

## Next

Open **Builder** to start turning these patterns into repeatable workflows.

