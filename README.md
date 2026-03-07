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

## 🚀 60-Second Quickstart

Get M-OS running in less than a minute.

### 1. Clone the repository

    git clone https://github.com/raajmandale/mos-runtime.git
    cd mos-runtime

### 2. Install dependencies

    pip install -r requirements.txt

### 3. Run the demo

    python cli/mos.py run examples/graph_opt.yaml

### Example Output

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


---

# 🧠 Architecture

<p align="center">
<img src="docs/assets/svg/mos_architecture.svg" width="900">
</p>

M-OS is built as a layered runtime architecture.

| Layer | Responsibility |
|------|---------------|
| PatternGraph | describes computation patterns |
| Runtime | executes graph nodes |
| Scheduler | determines execution order |
| Adapter | connects runtime to hardware |
| Backend | CPU / GPU / AI compute |

---

# 🔗 Pattern Graph Example

<p align="center">
<img src="docs/assets/svg/mos_pattern_graph.svg" width="900">
</p>

Example execution pattern:

Transform → Search → Optimize → Simulate → Aggregate

Each stage becomes a node in the **PatternGraph**, allowing the runtime to schedule execution deterministically.

---

# ⚙️ Execution Flow

<p align="center">
<img src="docs/assets/svg/mos_execution_flow.svg" width="900">
</p>

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

---

# ⏱ Execution Timeline

<p align="center">
<img src="docs/assets/svg/mos_timeline.svg" width="900">
</p>

This timeline illustrates how multiple pattern nodes are executed across runtime stages.

---

# 📂 Project Structure

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
    ├ docs/
    │   └ assets/svg
    │
    └ cli/

---

# 🔍 Why Pattern-Based Runtime

Traditional compute systems are:

• imperative  
• hardware-specific  
• difficult to reproduce  

M-OS introduces:

• pattern-driven execution  
• deterministic runtime graphs  
• portable compute routing  

This model works well for:

• AI pipelines  
• HPC workflows  
• optimization engines  
• simulation systems

---

# 🗺 Roadmap

Current stage

    v0 — Pattern Runtime Core

Next stages

    v1 — Distributed scheduler
    v2 — GPU execution backend
    v3 — AI runtime adapters
    v4 — Hybrid compute orchestration

---

# 📊 Status

Research prototype.  
Architecture baseline locked under **M-OS v0**.

---

# 👤 Author

Raaj Mandale  
Founder — ERANEST Technoware Pvt Ltd

---

# 📄 License

MIT License

---

# 📚 Citation

If you use M-OS in research:

    @software{mandale_mos_runtime_2026,
      author  = {Raaj Mandale},
      title   = {M-OS: Pattern Runtime for Hybrid Compute},
      year    = {2026},
      url     = {https://github.com/raajmandale/mos-runtime},
      version = {v0.1}
    }