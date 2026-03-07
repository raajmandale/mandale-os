class CostModel:
    def evaluate(self, adapter, pattern, constraints=None):
        return adapter.estimate_cost(pattern, constraints or {})
