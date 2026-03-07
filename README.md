<p align="center">
  <img src="docs/assets/svg/mos_architecture.svg" width="900">
</p>

# M-OS Runtime

**Pattern Graph Runtime for Hybrid Compute (CPU / OpenCL / AI)**

M-OS is a **Pattern State Transition Runtime (PSTG)** that routes computational workloads across heterogeneous compute backends.

Instead of executing programs as static processes, M-OS executes **Pattern Graphs**.

---

# Concept

Patterns represent **computational intent**.

Examples:

- transform
- search
- infer
- optimize

These patterns are connected into **Pattern Graphs**, which the runtime executes through a scheduling pipeline.

---

# Runtime Pipeline


PatternGraph → Runtime → Scheduler → Adapter → Compute Backend


Adapters currently included:

- CPU
- OpenCL
- AirLLM

---

# Quick Demo

Run the canonical pattern graph example.


python examples/demo_pattern_graph.py


Expected runtime flow:


PatternGraph → Runtime → Scheduler → Adapter → Compute


---

# Architecture

<p align="center">
  <img src="docs/assets/svg/mos_architecture.svg" width="850">
</p>

M-OS is structured into five layers:

| Layer | Responsibility |
|------|----------------|
| PatternGraph | Describes computation as patterns |
| Runtime | Executes graph nodes |
| Scheduler | Determines execution order |
| Adapter | Connects runtime to compute backend |
| Backend | CPU / OpenCL / AI execution |

---

# Pattern Graph Example

<p align="center">
  <img src="docs/assets/svg/pattern_graph.svg" width="850">
</p>

Example flow:


transform_data → search_route → rank_results → infer → optimize


---

# Run Tests


python -m pytest tests/


---

# Benchmark

Benchmark scripts are located in:


benchmarks/


Run example benchmark:


python benchmarks/runtime_benchmark.py


---

# Repository Structure


mos/
├ core
│ ├ pstg.py
│ ├ runtime.py
│ ├ scheduler.py
│ └ graph_executor.py
│
├ adapters
│ ├ cpu_adapter.py
│ ├ opencl_adapter.py
│ └ airllm_adapter.py


Supporting folders:


benchmarks/
demo/
docs/
examples/
tests/
research/


---

# Research

Conceptual runtime model:


research/mos_runtime_paper.md


---

# License

MIT License