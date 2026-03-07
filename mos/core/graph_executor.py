from .runtime import Runtime
class GraphExecutor:
    def __init__(self, graph, scheduler):
        self.runtime = Runtime(scheduler)
        self.graph = graph
    def run(self):
        return self.runtime.execute(self.graph)
