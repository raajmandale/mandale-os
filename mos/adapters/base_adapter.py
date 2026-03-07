class BaseAdapter:
    name = "base"
    def supports(self, pattern):
        raise NotImplementedError
    def estimate_cost(self, pattern, constraints=None):
        return 100.0
    def run(self, node, data):
        raise NotImplementedError
    def summarize(self, output):
        text = str(output)
        return text if len(text) <= 100 else text[:97] + "..."
