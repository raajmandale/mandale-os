<p align="center">
  <img src="docs/assets/svg/mos_architecture.svg" width="1000">
</p>

<h1 align="center">M-OS</h1>

<p align="center">
<b>Pattern Runtime for Hybrid Compute</b><br>
Deterministic execution for CPU / GPU / AI compute pipelines
</p>

<p align="center">

![status](https://img.shields.io/badge/status-research-blue)
![runtime](https://img.shields.io/badge/runtime-pattern--graph-green)
![compute](https://img.shields.io/badge/compute-CPU%20%7C%20GPU%20%7C%20AI-purple)
![version](https://img.shields.io/badge/version-v0.1-orange)

</p>

---

# What is M-OS

M-OS is a **pattern-based runtime system** designed to execute complex computation in a structured and deterministic way.

Instead of writing long procedural pipelines, M-OS represents computation as **patterns connected in a graph**.

Think of it like:

Traditional systems  
→ execute commands step-by-step

M-OS  
→ executes **structured patterns of computation**

This approach makes large compute systems easier to reason about and reproduce.

---

# Why This Matters

Modern compute systems (AI, HPC, simulation) suffer from:

- complex pipeline orchestration  
- unpredictable execution order  
- hardware-specific implementations  
- difficulty reproducing results

M-OS introduces a new model where computation is expressed as **Pattern Graphs**.

This enables:

✔ deterministic execution  
✔ hardware-agnostic compute routing  
✔ reproducible workflows  
✔ structured optimization pipelines  

---

## 60-Second Quickstart

### Clone the repository

```bash
git clone https://github.com/raajmandale/mos-runtime.git
cd mos-runtime
Install dependencies
pip install -r requirements.txt
Run demo
python cli/mos.py run examples/graph_opt.yaml
Example Output
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
Architecture
<p align="center"> <img src="docs/assets/svg/mos_architecture.svg" width="900"> </p>

M-OS runtime consists of five core layers:

Layer	Responsibility
PatternGraph	describes computation patterns
Runtime	executes graph nodes
Scheduler	determines execution order
Adapter	connects runtime to hardware
Backend	CPU / GPU / AI compute
Pattern Graph Example
<p align="center"> <img src="docs/assets/svg/mos_pattern_graph.svg" width="900"> </p>

Execution example:

Transform → Search → Optimize → Simulate → Aggregate

Each stage becomes a node in the PatternGraph, and the runtime scheduler determines how these nodes execute.

Execution Flow
<p align="center"> <img src="docs/assets/svg/mos_execution_flow.svg" width="900"> </p>

Runtime pipeline:

PatternGraph
   ↓
Scheduler
   ↓
Runtime
   ↓
Adapter
   ↓
Backend Compute
Execution Timeline
<p align="center"> <img src="docs/assets/svg/mos_timeline.svg" width="900"> </p>

This diagram illustrates how multiple pattern nodes execute across time.

Project Structure
mos-runtime
│
├ core/
│   ├ pattern_graph
│   ├ runtime
│   └ scheduler
│
├ adapters/
│   ├ cpu
│   ├ opencl
│   └ ai
│
├ examples/
│
├ docs/
│   └ assets/svg
│
└ cli/
Why Pattern-Based Runtime

Traditional compute systems are:

imperative

hardware-specific

difficult to reproduce

M-OS introduces:

pattern-driven execution

deterministic runtime graphs

portable compute routing

This makes M-OS suitable for:

AI pipelines

HPC workflows

optimization systems

simulation engines

Roadmap

Current stage:

v0 — Pattern Runtime Core

Next stages:

v1 — distributed scheduler
v2 — GPU routing
v3 — AI backend adapters
v4 — hybrid compute orchestration
Status

Research prototype.

Architecture baseline locked under M-OS v0.

Author

Raaj Mandale
Founder — ERANEST Technoware Pvt Ltd

License

MIT License

Citation
@software{mandale_mos_runtime_2026,
  author  = {Raaj Mandale},
  title   = {M-OS: Pattern Runtime for Hybrid Compute},
  year    = {2026},
  url     = {https://github.com/raajmandale/mos-runtime},
  version = {v0.1}
}