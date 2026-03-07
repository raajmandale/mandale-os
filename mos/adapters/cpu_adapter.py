from .base_adapter import BaseAdapter
class CPUAdapter(BaseAdapter):
    name = "CPU"
    def supports(self, pattern):
        return True
    def estimate_cost(self, pattern, constraints=None):
        return float({"transform":20,"search":60,"infer":90,"optimize":70,"aggregate":15,"generate":50,"simulate":45,"route":10}.get(pattern,80))
    def run(self, node, data):
        if node.pattern == "transform":
            coords = data.get("cities", []) if isinstance(data, dict) else []
            normalized = [{"id": i, "x": float(x), "y": float(y)} for i, (x, y) in enumerate(coords)]
            return {"cities": normalized, "count": len(normalized)}
        if node.pattern == "aggregate":
            return {"count": len(data) if hasattr(data, "__len__") else 1}
        return data
