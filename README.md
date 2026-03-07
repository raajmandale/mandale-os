<p align="center">
  <img src="docs/banner.svg" width="900">
</p>

# M-OS Runtime

Pattern Graph Runtime for Hybrid Compute (CPU / OpenCL / AI)
# M-OS — Pattern Based Runtime System

M-OS is a **Pattern State Transition Runtime** that automatically routes workloads
to different compute backends.

Instead of running programs as processes, M-OS executes **Pattern Graphs**.

Patterns represent computational intent.

Examples:

- transform
- search
- infer
- optimize

---
## Quick Demo

Run the canonical pattern graph runtime:

```bash
python examples/demo_pattern_graph.py

## Architecture

![Architecture](docs/assets/svg/mos_architecture.svg)

Pipeline:

PatternGraph → Runtime → Scheduler → Adapter → Compute Backend

Adapters currently included:

- CPU
- OpenCL
- AirLLM

---

# Pattern Graph

Example pattern graph:

![Pattern Graph](docs/assets/svg/mos_pattern_graph.svg)

Example pipeline:


transform → search → infer


Each stage may execute on a different compute backend.

---

# Execution Model

![Execution Flow](docs/assets/svg/mos_execution_flow.svg)

Steps:

1. Load PatternGraph
2. Scheduler chooses backend
3. Adapter executes compute
4. Results stored in runtime store
5. Reports generated

---

# Repository Structure


mos_repo
│
├── mos/
│ ├── core/
│ ├── adapters/
│ ├── routing/
│ ├── cli/
│ └── utils/
│
├── demo/
│ └── mos_visual_runtime.py
│
├── examples/
│ ├── hybrid_pipeline.py
│ └── pstg_demo.json
│
├── benchmarks/
│ └── routing_benchmark.py
│
├── docs/
│ ├── architecture.md
│ ├── pstg_model.md
│ └── assets/svg/
│
├── reports/
│
└── tests/


---

# Quick Start

Clone the repo:


git clone https://github.com/yourname/mos

cd mos


Install requirements:


pip install -r requirements.txt


---

# Run the M-OS Demo Runtime

Run the visual runtime demo:


python demo/mos_visual_runtime.py


This will:

- build a pattern graph
- schedule workloads
- execute adapters
- generate runtime reports

---

# View Runtime Report

Open:


reports/runtime_visualization.html


You will see:

- pattern pipeline
- execution results
- backend routing
- runtime metrics

---

# Pattern Graph Example

Run example pipeline:


python examples/hybrid_pipeline.py


This demonstrates:

- multi-stage graph execution
- adapter scheduling
- runtime store

---

# Benchmark Scheduler

Run benchmark:


python benchmarks/routing_benchmark.py


Output will be generated:


reports/benchmark_runs.csv


---

# Interactive Graph Viewer

Open in browser:


docs/pattern_graph_viewer.html


This visualizes pattern graphs interactively.

---

# Runtime Timeline

Example runtime timeline:

![Timeline](docs/assets/svg/mos_timeline.svg)

Shows how time is spent per stage.

---
## Interactive Runtime Explorer
Open docs/runtime_explorer.html
to explore the Pattern State Transition Graph interactively.

# Adapter API

Adapters implement:


supports(pattern)
estimate_cost(pattern)
run(data)
summarize(result)


Example:


mos/adapters/cpu_adapter.py


---

# Tests

Run basic runtime tests:


python -m pytest tests/


---

# Research

See:


research/mos_runtime_paper.md


for the conceptual runtime model.

---

# License

MIT License