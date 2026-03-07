<p align="center">
  <img src="docs/assets/svg/mos_timeline.svg" width="1000">
</p>

<h1 align="center">M-OS</h1>

<p align="center">
<b>Pattern Runtime for Hybrid Compute</b><br>
Deterministic execution for CPU / GPU / AI compute pipelines.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/status-research-blue">
  <img src="https://img.shields.io/badge/runtime-pattern--graph-green">
  <img src="https://img.shields.io/badge/compute-CPU%20%7C%20GPU%20%7C%20AI-purple">
  <img src="https://img.shields.io/badge/version-v0.1-orange">
</p>

---

# What is M-OS

M-OS is a **pattern-based runtime architecture** designed to execute computational workflows as **Pattern State Transition Graphs (PSTG)**.

Instead of imperative code pipelines, M-OS treats computation as **structured execution patterns**.

This enables:

• deterministic runtime execution  
• hardware-agnostic compute routing  
• reproducible AI / HPC workflows  
• structured optimization pipelines

---

# Architecture

<p align="center">
  <img src="docs/assets/svg/mos_architecture.svg" width="900">
</p>

M-OS runtime is composed of five core layers:

| Layer | Responsibility |
|------|---------------|
| PatternGraph | Describes computation as patterns |
| Runtime | Executes graph nodes |
| Scheduler | Determines execution order |
| Adapter | Connects runtime to compute backend |
| Backend | CPU / OpenCL / AI execution |

---

# Pattern Graph Example

<p align="center">
  <img src="docs/assets/svg/mos_pattern_graph.svg" width="900">
</p>

Execution model:


Transform → Search → Optimize → Simulate → Aggregate


Each stage becomes a **node in the PatternGraph**.

---

# Execution Flow

<p align="center">
  <img src="docs/assets/svg/mos_execution_flow.svg" width="900">
</p>

Execution pipeline:


PatternGraph
↓
Scheduler
↓
Runtime
↓
Adapter
↓
Backend Compute


---

# Quick Demo

Example workflow:

```bash
mos run examples/graph_opt.yaml

Expected output:

PatternGraph loaded
Nodes: 12
Execution backend: CPU

Running scheduler...
Executing nodes...

Transform ✓
Search ✓
Optimize ✓
Simulate ✓
Aggregate ✓

Execution complete
Runtime: 0.42s
Project Structure
mos_repo_final_v0
│
├ core/
│   ├ pattern_graph
│   ├ runtime
│   ├ scheduler
│
├ adapters/
│   ├ cpu
│   ├ opencl
│   ├ ai
│
├ examples/
│
├ docs/
│   └ assets
│       └ svg
│
└ cli/
Why M-OS

Traditional compute systems are:

imperative
hardware-specific
difficult to reproduce

M-OS introduces:

pattern-driven execution
deterministic runtime graphs
portable compute routing

This enables reproducible HPC / AI / optimization workloads.

Roadmap

Current version:

v0 — Pattern Runtime Core

Next stages:

v1 — distributed scheduler
v2 — GPU routing
v3 — AI backend adapters
v4 — hybrid compute orchestration
Status

Research prototype.

Architecture locked under M-OS v0 baseline.

Author

Raaj Mandale
Founder — ERANEST Technoware Pvt Ltd

License

MIT License


---

