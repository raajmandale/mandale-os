import time

class Runtime:
    def __init__(self, scheduler):
        self.scheduler = scheduler

    def execute(self, graph):
        ordered = graph.topological_order()
        data_store = {}
        results = []
        for idx, node in enumerate(ordered, start=1):
            adapter = self.scheduler.select_backend(node.pattern, node.constraints, node.backend)
            input_value = node.input
            if isinstance(input_value, str) and input_value in data_store:
                input_value = data_store[input_value]
            start = time.perf_counter()
            output = adapter.run(node, input_value)
            elapsed = time.perf_counter() - start
            output_key = node.output or node.name
            data_store[output_key] = output
            results.append({
                "index": idx,
                "node": node.name,
                "pattern": node.pattern,
                "adapter": adapter.name,
                "time_seconds": elapsed,
                "input_key": node.input if isinstance(node.input, str) else "",
                "output_key": output_key,
                "summary": adapter.summarize(output),
            })
        return results, data_store
