# M-OS

**Pattern Runtime for Hybrid Compute**

Deterministic execution for CPU / GPU / AI compute pipelines.

---

## System Architecture

<p align="center">
<img src="docs/assets/svg/mos_architecture.svg" width="900">
</p>

Conceptual difference: traditional systems schedule processes; **M-OS schedules patterns.**

---

![status](https://img.shields.io/badge/status-research-blue)
![runtime](https://img.shields.io/badge/runtime-pattern--graph-green)
![compute](https://img.shields.io/badge/compute-CPU%20%7C%20GPU%20%7C%20AI-purple)
![version](https://img.shields.io/badge/version-v0.1-orange)

---

# Overview

M-OS is a **pattern-driven runtime system** designed to execute computation using structured pattern graphs rather than imperative pipelines.

The system enables deterministic execution across heterogeneous compute environments including:

- CPU  
- GPU  
- AI inference engines  
- future hybrid compute backends  

Instead of scheduling processes, **M-OS schedules patterns**.

---

# 60-Second Quickstart

Clone the repository:

```bash
git clone https://github.com/raajmandale/mos-runtime.git
cd mos-runtime

Install dependencies:

pip install -r requirements.txt

Run demo:

python cli/mos.py run examples/graph_opt.yaml

Expected output:

PatternGraph loaded
Nodes: 12
Execution backend: CPU
Running scheduler...
Executing nodes...
Execution complete
Architecture

M-OS runtime consists of five core layers.

Layer	Responsibility
PatternGraph	describes computation patterns
Runtime	executes graph nodes
Scheduler	determines execution order
Adapter	connects runtime to hardware
Backend	CPU / GPU / AI compute
Pattern Execution Model

Execution is represented as a Pattern State Transition Graph.

Example flow:

Transform → Search → Optimize → Simulate → Aggregate

Each stage becomes a node in the runtime graph.

Project Structure
mos-runtime
│
├ core
│   ├ pattern_graph
│   ├ runtime
│   └ scheduler
│
├ adapters
│   ├ cpu
│   ├ opencl
│   └ ai
│
├ examples
├ docs
└ cli
Roadmap

Current version

v0 — pattern runtime core

Future development

v1 — distributed scheduler
v2 — GPU execution backend
v3 — AI runtime adapters
v4 — hybrid compute orchestration
Status

Research prototype.

Author

Raaj Mandale
Founder — ERANEST Technoware Pvt Ltd

License

MIT License

Citation

If you use M-OS in research, please cite:

@software{mandale_mos_runtime_2026,
  author  = {Raaj Mandale},
  title   = {M-OS: Pattern Runtime for Hybrid Compute},
  year    = {2026},
  url     = {https://github.com/raajmandale/mos-runtime},
  version = {v0.1}
}