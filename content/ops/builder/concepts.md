# Builder: Workflow & Tool Orchestration

Builders turn ideas into reusable agent workflows that can be run safely in operations.

## What you will build

- A tool-using workflow that follows a reliable loop
- Structured I/O between steps
- Clear error handling and retries

## A common architecture

1. Intake: validate inputs
2. Retrieve: pull relevant SOPs/data
3. Decide: choose next tool/action
4. Execute: call tools with validated parameters
5. Verify: confirm compliance and outcomes
6. Report: summarize results and actions taken

## Example: a tool pipeline (conceptual YAML)

```yaml
workflow:
  validate_inputs: true
  steps:
    - name: load_sop
      tool: read_sop
      inputs: { sop_id: "{{ sop_id }}" }
    - name: propose_checklist
      tool: llm
      inputs: { sop_text: "{{ load_sop.output }}" }
    - name: verify
      tool: compliance_checker
      inputs: { checklist: "{{ propose_checklist.output }}" }
```

## Exercises

1. Pick an ops workflow (e.g., “generate work order”).
2. Define the allowed tools.
3. Write down what gets verified before any irreversible action.

## Next

Open **Coder** for implementation-level guidance.

