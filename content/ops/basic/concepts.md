# Build Tools, Not Agents

*A tooling-first approach to AI agents for experimental science*

---

Everyone wants an AI agent.  The instinct is to fine-tune a model on your domain data, or build a custom agent framework that defines exactly what the agent can and cannot do.  Both are expensive, both lock you in, and both miss where the real leverage is.

This document argues that an AI agent is three layers -- and you should only invest in one of them.

For canonical definitions of key terms (agent, model, harness, tooling, RAG, SKILL, MCP), see the [Core Terms Glossary](glossary.md).


## The Three Layers

```
┌─────────────────────────────────────────────────────────┐
│  (1) Model                                              │
│                                                         │
│  Claude, GPT, Llama, Gemini, ...                        │
│  Keep it general.  Don't fine-tune.                     │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  (2) Harness                                            │
│                                                         │
│  Claude Code, OpenCode, LangGraph, CrewAI, ...          │
│  Keep it swappable.  Don't over-customize.              │
│                                                         │
├─────────────────────────────────────────────────────────┤
│  (3) Tooling                      <── invest here       │
│                                                         │
│  CLI tools, databases, cron pipelines, search indexes,  │
│  shell wrappers, documentation (including SKILL files   │
│  that teach the AI how to use the tools)                │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

**The model** is the foundation.  You don't build it -- you rent it. Fine-tuning couples you to a specific model version; when the next generation arrives, your fine-tuning is gone and you pay the evaluation cost all over again.  A general model, given good tools, performs well enough.

**The harness** is the orchestration layer -- the thing that connects the model to your tools, manages conversation, and controls permissions. Today it might be Claude Code; tomorrow it might be something better. Don't embed your domain logic here.  If the harness dies, your investment should survive.

**The tooling** is where all the value lives.  CLI tools that query databases.  Cron jobs that keep data fresh.  Search indexes that make documentation discoverable.  Shell wrappers that isolate environments. These are things you would build anyway -- they serve human users just as well as AI agents.  The AI is a multiplier on tooling that already has value.

The key insight: **better tooling enables both human agents and AI agents.**  A CLI tool that queries your experiment database is useful to a scientist typing commands in a terminal.  It's also useful to an AI agent that translates natural language into those same commands.  The investment pays off either way.


## SKILL Files Are Man Pages, Not Fine-Tuning

The obvious objection: "Your SKILL files contain domain-specific schemas, query strategies, fallback logic, and naming conventions.  That's model customization, not tooling."

It's not.  Here's the litmus test: **does it travel with the tool or with the model?**

```
Fine-tuning                          SKILL file (man page)
─────────────                        ─────────────────────
Coupled to model version             Coupled to the tool
Dies when you switch models           Works with any model
Encoded in weights (opaque)          Encoded in text (readable)
Requires evaluation pipeline         Requires a text editor
Amortizes token cost                 Costs tokens at runtime
Cannot be version-controlled         Lives in git
Cannot be read by humans             Readable by anyone
```

A SKILL file is the AI equivalent of a man page.  It teaches the user -- human or AI -- how to use the tool.  It describes the interface, the expected inputs, the known gotchas, and the common workflows.  Nobody would call `man grep` "shell customization."  It's part of grep.

The token cost at runtime is real, but manageable.  A single skill invocation loads one SKILL file, not all of them.  And unlike fine-tuning, you never lose your investment when the model upgrades.


## The Practical Takeaway

If you want an AI agent for X, don't start with the agent.  Start with the tool.

```
Step 1: Build a CLI tool that does X
        ┌──────────────────────────────┐
        │  $ my-tool query "..."       │
        │  $ my-tool search "..."      │
        │  $ my-tool status            │
        └──────────────────────────────┘
        A human can use this right now.

Step 2: Write a man page (SKILL file)
        ┌──────────────────────────────┐
        │  What the tool does          │
        │  What commands are available │
        │  What the schema looks like  │
        │  What the gotchas are        │
        │  What the safety rules are   │
        └──────────────────────────────┘
        A human would read this too.

Step 3: Hand both to an AI harness
        ┌──────────────────────────────┐
        │  The AI reads the man page,  │
        │  invokes the tool, and       │
        │  interprets the output.      │
        └──────────────────────────────┘
        Now you have an agent.
```

You didn't fine-tune a model.  You didn't build a framework.  You built a tool that works for humans and wrote documentation that works for both humans and AI.  If the model improves, your agent gets better for free. If the harness changes, you move the man page.  Your investment is in the tool -- and the tool was worth building anyway.

---

*This document reflects experience from the LCLS OpenCode deployment at SLAC National Accelerator Laboratory, where ~15 AI skills serve scientists and engineers across experiment operations, data analysis, and facility computing.  The deployment runs on the S3DF HPC cluster using general-purpose language models with no fine-tuning.  The deployment serves experimental science workflows, not large-scale simulation.*
