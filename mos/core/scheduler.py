class Scheduler:
    def __init__(self, adapters):
        self.adapters = adapters

    def select_backend(self, pattern, constraints=None, backend_hint="auto"):
        constraints = constraints or {}
        if backend_hint and backend_hint != "auto":
            for adapter in self.adapters:
                if adapter.name.lower() == backend_hint.lower():
                    return adapter
            raise ValueError(f"Requested backend '{backend_hint}' not available")
        candidates = [a for a in self.adapters if a.supports(pattern)]
        if not candidates:
            raise ValueError(f"No adapter supports pattern '{pattern}'")
        scored = sorted(((a.estimate_cost(pattern, constraints), a) for a in candidates), key=lambda x: x[0])
        return scored[0][1]
