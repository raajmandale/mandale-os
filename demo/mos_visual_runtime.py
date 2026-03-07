import csv
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mos.core.pstg import PatternGraph, Node
from mos.core.scheduler import Scheduler
from mos.core.graph_executor import GraphExecutor
from mos.adapters.cpu_adapter import CPUAdapter
from mos.adapters.opencl_adapter import OpenCLAdapter
from mos.adapters.airllm_adapter import AirLLMAdapter

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXAMPLES_DIR = os.path.join(BASE_DIR, "examples")
REPORTS_DIR = os.path.join(BASE_DIR, "reports")

def ensure_reports_dir():
    os.makedirs(REPORTS_DIR, exist_ok=True)

def load_adapters():
    return [CPUAdapter(), OpenCLAdapter(), AirLLMAdapter()]

def load_graph_from_json(path):
    with open(path, "r", encoding="utf-8") as f:
        payload = json.load(f)
    graph = PatternGraph(payload["name"])
    for raw in payload["nodes"]:
        graph.add(Node(name=raw["name"], pattern=raw["pattern"], input=raw.get("input"), output=raw.get("output")))
    for source, target in payload["edges"]:
        graph.link(source, target)
    return graph, payload

def write_csv(results, filename):
    with open(filename, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["index","node","pattern","adapter","time_seconds","input_key","output_key","summary"])
        writer.writeheader()
        writer.writerows(results)

def write_json(results, final_output, filename):
    payload = {"results": results, "final_output": final_output}
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)

def write_html(graph_name, results, final_output, filename):
    total_ms = sum(r["time_seconds"] * 1000 for r in results)
    nodes_html = []
    colors = {"CPU":"#4F8EF7", "OpenCL":"#2BB673", "AirLLM":"#8F5BFF"}
    for r in results:
        color = colors.get(r["adapter"], "#777")
        nodes_html.append(
            '<div class="node" style="border-color:{c}; box-shadow:0 0 0 6px {c}22;">'
            '<div class="badge" style="background:{c};">{a}</div>'
            '<div class="title">{n}</div>'
            '<div class="pattern">{p}</div>'
            '<div class="time">{t:.2f} ms</div>'
            '</div>'.format(c=color, a=r["adapter"], n=r["node"], p=r["pattern"], t=r["time_seconds"]*1000)
        )
    flow = '<div class="arrow">→</div>'.join(nodes_html)
    final_html = ''.join('<div><b>{}</b>: {}</div>'.format(k,v) for k,v in final_output.items())
    table_rows = ''.join(
        '<tr><td>{}</td><td>{}</td><td>{}</td><td>{:.2f}</td><td>{}</td></tr>'.format(
            r["index"], r["node"], r["adapter"], r["time_seconds"]*1000, r["output_key"]
        ) for r in results
    )
    html = '''
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>M-OS Visual Runtime Report</title>
<style>
body {{ font-family: Arial, sans-serif; margin: 0; background: #0b1020; color: #e8eefc; }}
.wrap {{ max-width: 1100px; margin: 0 auto; padding: 32px 24px 56px; }}
.panel {{ background: #131a2b; border: 1px solid #27314a; border-radius: 18px; padding: 22px; margin-bottom: 22px; }}
h1 {{ margin-top: 0; }}
.small {{ color: #a8b2c7; }}
.flow {{ display: flex; align-items: center; justify-content: center; gap: 14px; flex-wrap: wrap; }}
.node {{ width: 230px; background: #0f1627; border: 2px solid #23304e; border-radius: 18px; padding: 18px; text-align: center; }}
.badge {{ display: inline-block; color: white; font-weight: 700; border-radius: 999px; padding: 6px 10px; font-size: 12px; margin-bottom: 12px; }}
.title {{ font-size: 18px; font-weight: 700; }}
.pattern {{ color: #a8b2c7; margin-top: 4px; }}
.time {{ font-size: 22px; font-weight: 800; margin-top: 12px; }}
.arrow {{ font-size: 40px; color: #90a0b8; font-weight: 700; }}
.kpi {{ display: grid; grid-template-columns: repeat(4,1fr); gap: 14px; }}
.kbox {{ background:#0f1627; border:1px solid #23304e; border-radius:16px; padding:16px; }}
.knum {{ font-size: 28px; font-weight: 800; }}
table {{ width:100%; border-collapse: collapse; }}
th, td {{ border-bottom: 1px solid #24314d; padding: 12px 10px; text-align: left; }}
th {{ color:#a8b2c7; }}
code {{ background:#1a2338; color:#d6e3ff; padding:2px 6px; border-radius:6px; }}
</style>
</head>
<body>
<div class="wrap">
<div class="panel">
<h1>M-OS Visual Runtime Report</h1>
<div class="small">Pattern-aware hybrid compute runtime demonstration for <code>{graph_name}</code>.</div>
<div class="kpi">
<div class="kbox"><div class="small">Total Runtime</div><div class="knum">{total_ms:.2f} ms</div></div>
<div class="kbox"><div class="small">Stages</div><div class="knum">{stages}</div></div>
<div class="kbox"><div class="small">Backends</div><div class="knum">3</div></div>
<div class="kbox"><div class="small">Final Quality</div><div class="knum" style="font-size:18px">{quality}</div></div>
</div>
</div>

<div class="panel">
<h2>Pattern Graph + Backend Routing</h2>
<div class="small">This is the execution path of the demo workload.</div>
<div class="flow">{flow}</div>
</div>

<div class="panel">
<h2>Execution Table</h2>
<table>
<thead><tr><th>#</th><th>Stage</th><th>Backend</th><th>Time (ms)</th><th>Output Key</th></tr></thead>
<tbody>{table_rows}</tbody>
</table>
</div>

<div class="panel">
<h2>Final Result</h2>
{final_html}
</div>
</div>
</body>
</html>
'''.format(graph_name=graph_name, total_ms=total_ms, stages=len(results), quality=final_output.get("quality", "-"), flow=flow, table_rows=table_rows, final_html=final_html)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)

def run_demo():
    ensure_reports_dir()
    graph, payload = load_graph_from_json(os.path.join(EXAMPLES_DIR, "pstg_demo.json"))
    print("=" * 36)
    print(" M-OS Visual Runtime v0")
    print(" Pattern Execution Viewer")
    print("=" * 36)
    print()
    print(graph.inspect())
    print()
    executor = GraphExecutor(graph, Scheduler(load_adapters()))
    results, data_store = executor.run()
    final_output = data_store.get("final_report", {})
    csv_path = os.path.join(REPORTS_DIR, "benchmark.csv")
    json_path = os.path.join(REPORTS_DIR, "routing_log.json")
    html_path = os.path.join(REPORTS_DIR, "runtime_visualization.html")
    write_csv(results, csv_path)
    write_json(results, final_output, json_path)
    write_html(payload["name"], results, final_output, html_path)
    print("[M-OS] Backend Selection + Execution")
    for row in results:
        print("{} -> {} ({:.2f} ms)".format(row["node"], row["adapter"], row["time_seconds"] * 1000))
    print()
    print("[M-OS] Generated:")
    print(" ", csv_path)
    print(" ", json_path)
    print(" ", html_path)

def main():
    run_demo()

if __name__ == "__main__":
    main()
