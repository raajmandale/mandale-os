from .base_adapter import BaseAdapter
class AirLLMAdapter(BaseAdapter):
    name = "AirLLM"
    def supports(self, pattern):
        return pattern in {"infer","generate"}
    def estimate_cost(self, pattern, constraints=None):
        return float({"infer":15,"generate":18}.get(pattern,100))
    def run(self, node, data):
        if node.pattern == "infer":
            route = data.get("route", [])
            cost = data.get("cost", 0.0)
            quality = "strong" if cost < 300 else "moderate"
            explanation = f"M-OS selected a hybrid execution path and produced a {quality} route covering {len(route)} cities with total closed-loop cost {cost}."
            return {"route": route, "cost": cost, "quality": quality, "explanation": explanation}
        if node.pattern == "generate":
            return {"text": "Generated output from offline demo adapter."}
        return data
