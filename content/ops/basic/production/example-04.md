# experimental-hutch-python — the safety boundary

This is the most ambitious skill -- and the most instructive about where safety belongs.

LCLS beamlines are controlled through `hutch-python`, an IPython-based session running on DAQ nodes.  The skill lets an AI agent assist with beamline operations through a bridge:

```
┌─────────┐    SSH tunnel (2 hops)    ┌───────────┐
│ AI agent│◄─────────────────────────►│  IPython  │
│ on SDF  │  JSON over netcat:9999    │  on DAQ   │
│         │                           │  node     │
│         │  {"code": "motor.mv(5)"}  │           │
│         │  ──────────────────────►  │  executes │
│         │                           │  on real  │
│         │  {"status": "ok",         │  beamline │
│         │   "result": "5.0"}        │  hardware │
│         │  ◄──────────────────────  │           │
└─────────┘                           └───────────┘
```

The safety architecture has two layers:

**Tooling-level safety (strong):**
- The bridge requires a two-hop SSH tunnel (SDF -> psdev -> hutch-daq) -- you can't accidentally connect without deliberate infrastructure setup
- The bridge is a separate process that must be manually launched in the IPython session
- Network isolation: the AI runs on SDF, not on the DAQ node

**SKILL-file-level safety (weaker, model-dependent):**
- Read-only commands (`.position`, `.read()`, `wm_*()`) execute directly
- Write commands (`.mv()`, `RE(scan)`, `daq.begin()`) require explicit user confirmation before execution:

  > **I'd like to execute the following command:**
  > ```python
  > motor_x.mv(10.5)
  > ```
  > This will move motor_x from its current position to 10.5.
  >
  > **Shall I proceed?**

This skill honestly illustrates the framework's own principle: **safety should be in the tooling, not the model.**  The SSH tunnel requirement (tooling-level) is robust -- it's a physical infrastructure gate.  The confirmation protocol (SKILL-file-level) depends on the model following instructions, which is weaker.  The right next step is to build the confirmation into the bridge itself -- a cryptographic token, a hardware interlock, or a default-deny mode that requires explicit unlock.

**Pattern: When the stakes are high, don't rely on the AI following instructions.  Build safety into the tooling infrastructure.  Use the AI's judgment for convenience, not for safety.**
