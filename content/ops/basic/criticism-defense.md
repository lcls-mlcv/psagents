# Criticism and Defense

Any framework that claims "don't do X" should withstand scrutiny.  Here are the strongest challenges to this approach, presented honestly.


### "You have no mechanism for multi-tool orchestration"

**The attack:** A question like "Why did experiment LY2523 have anomalous detector readings, and is this related to the DAQ configuration changes documented in Confluence last month?" requires querying the elog database, the DAQ logs, and the Confluence docs.  Your framework has no workflow graph, no shared state, no way to pipe one skill's output into another. This is exactly what LangGraph solves.

**The defense:** The model handles this today.  In a single conversation, the AI queries the elog database, then the DAQ logs, then searches Confluence -- using the same tools it would use for single-skill queries. The model's in-context reasoning is the orchestrator.  This works because our tasks are primarily information retrieval with synthesis, not multi-hour pipelines requiring checkpointing and rollback.

We concede: if you need *guaranteed* multi-step workflows with error recovery and audit trails, a workflow engine is more reliable than hoping the model self-organizes correctly.  But for the query-and-synthesize pattern that dominates scientific computing, the general model handles orchestration well enough.


### "Your beamline control safety is in the SKILL file, not in tooling"

**The attack:** The confirmation protocol for beamline commands lives in the SKILL file, enforced by the model's compliance with instructions.  A sufficiently creative prompt could bypass it.  By your own framework's logic, this should be tooling-level safety.

**The defense:** This is correct.  The SSH tunnel requirement is genuine tooling-level safety.  The confirmation protocol is not.  The skill is labeled `[EXPERIMENTAL]` for exactly this reason.  The right fix is to build confirmation into the bridge itself -- require a cryptographic token, add a hardware interlock, or make the bridge read-only by default. This critique strengthens the framework: the fix is more tooling, not more model safety or more harness logic.


### "Context window creates a ceiling at scale"

**The attack:** At 15 skills, you can load 1-2 SKILL files per query. At 100+ skills, the harness needs a routing layer to decide which SKILL files to load.  That router is a harness-level component, contradicting "keep the harness thin."

**The defense:** The routing already exists: the one-line skill descriptions in the harness configuration serve as a lightweight index. As skill count grows, this can be extended with a search index over skill descriptions -- which is just another tool (and one we already have: `docs-index` could index SKILL files the same way it indexes documentation).  The architecture accommodates scale within its own principles; it just needs one more tool.


### "You have no feedback loop"

**The attack:** There's no instrumentation for skill quality.  No logging of which skills are invoked, no way to detect incorrect outputs, no A/B testing for SKILL file modifications.  Without feedback, quality depends on the maintainer's intuition.

**The defense:** This is a legitimate gap.  The fix is consistent with the framework: build a logging tool.  A SQLite database recording skill invocations, queries issued, and outcomes.  That's tooling, not model customization or framework engineering.  The framework doesn't prevent this; it just hasn't been built yet.
