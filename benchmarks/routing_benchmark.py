import csv, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mos import PatternGraph, Node
from mos.core.scheduler import Scheduler
from mos.core.graph_executor import GraphExecutor
from mos.adapters.cpu_adapter import CPUAdapter
from mos.adapters.opencl_adapter import OpenCLAdapter
from mos.adapters.airllm_adapter import AirLLMAdapter

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(BASE_DIR, "reports", "benchmark_runs.csv")
os.makedirs(os.path.dirname(OUT), exist_ok=True)

rows = []
for run in range(1, 6):
    g = PatternGraph(f"benchmark_run_{run}")
    g.add(Node("transform_data", pattern="transform", input={"cities": [[12,5],[18,22],[7,31],[29,16],[36,28],[42,7]]}, output="normalized_cities"))
    g.add(Node("search_route", pattern="search", input="normalized_cities", output="candidate_route"))
    g.add(Node("rank_results", pattern="infer", input="candidate_route", output="final_report"))
    g.link("transform_data", "search_route")
    g.link("search_route", "rank_results")
    scheduler = Scheduler([CPUAdapter(), OpenCLAdapter(), AirLLMAdapter()])
    executor = GraphExecutor(g, scheduler)
    start = time.perf_counter()
    results, _ = executor.run()
    total = time.perf_counter() - start
    for r in results:
        rows.append({"run": run, "node": r["node"], "pattern": r["pattern"], "adapter": r["adapter"], "time_seconds": r["time_seconds"], "total_runtime_seconds": total})

with open(OUT, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["run","node","pattern","adapter","time_seconds","total_runtime_seconds"])
    writer.writeheader()
    writer.writerows(rows)

print(f"Benchmark report written to: {OUT}")
