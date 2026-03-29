# Coder: Agent Loop Implementation Notes

This track is for implementing agent loops, tool integrations, and safety checks in code.

## What to implement

- A loop that alternates between:
  - context gathering (observe)
  - decision making (plan)
  - tool execution (act)
  - checks (verify)
- A tool interface with:
  - input validation
  - structured outputs
  - audit logging

## Example: a typed loop (pseudo-code)

```python
def run_agent(initial_state):
    state = observe(initial_state)

    while not state.is_done:
        plan = llm.plan(state)
        tool_result = tool_registry.execute(plan.tool, plan.args)
        state = verify(state, plan, tool_result)

    return state.summary
```

## Safety checklist for code

- Validate tool arguments before calling
- Make "irreversible" actions explicit and gated
- Record every tool call (inputs + outputs)
- Use timeouts and retry rules
- Add evaluation hooks (what you expected vs what happened)

## Next

When you have an ops workflow in mind, start prototyping the loop and plug in real tools.

