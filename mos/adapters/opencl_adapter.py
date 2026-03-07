import itertools, math
from .base_adapter import BaseAdapter
class OpenCLAdapter(BaseAdapter):
    name = "OpenCL"
    def supports(self, pattern):
        return pattern in {"search","optimize","transform"}
    def estimate_cost(self, pattern, constraints=None):
        return float({"transform":40,"search":25,"optimize":20}.get(pattern,90))
    def _distance(self, a, b):
        return math.sqrt((a["x"]-b["x"])**2 + (a["y"]-b["y"])**2)
    def run(self, node, data):
        if node.pattern == "search":
            cities = data.get("cities", [])
            n = len(cities)
            if n < 2:
                return {"route": [], "cost": 0.0}
            ids = [c["id"] for c in cities]
            best_route = None
            best_cost = float("inf")
            for perm in itertools.permutations(ids):
                cost = 0.0
                for i in range(len(perm)-1):
                    a = cities[perm[i]]
                    b = cities[perm[i+1]]
                    cost += self._distance(a,b)
                cost += self._distance(cities[perm[-1]], cities[perm[0]])
                if cost < best_cost:
                    best_cost = cost
                    best_route = list(perm)
            return {"route": best_route, "cost": round(best_cost, 4), "city_count": n}
        return data
