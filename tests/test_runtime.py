import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mos import PatternGraph, Node
from mos.core.scheduler import Scheduler
from mos.core.graph_executor import GraphExecutor
from mos.adapters.cpu_adapter import CPUAdapter
from mos.adapters.opencl_adapter import OpenCLAdapter
from mos.adapters.airllm_adapter import AirLLMAdapter

def test_demo_execution():
    g = PatternGraph("test_graph")
    g.add(Node("transform_data", pattern="transform", input={"cities": [[0,0],[1,1],[2,2]]}, output="normalized_cities"))
    g.add(Node("search_route", pattern="search", input="normalized_cities", output="candidate_route"))
    g.add(Node("rank_results", pattern="infer", input="candidate_route", output="final_report"))
    g.link("transform_data", "search_route")
    g.link("search_route", "rank_results")
    scheduler = Scheduler([CPUAdapter(), OpenCLAdapter(), AirLLMAdapter()])
    executor = GraphExecutor(g, scheduler)
    results, data_store = executor.run()
    assert len(results) == 3
    assert "final_report" in data_store
