from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
from .patterns import PATTERNS

class GraphError(Exception):
    pass

@dataclass
class Node:
    name: str
    pattern: str
    input: Any = None
    output: Optional[str] = None
    backend: str = "auto"
    constraints: Dict[str, Any] = field(default_factory=dict)
    meta: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        if self.pattern not in PATTERNS:
            raise GraphError(f"Invalid pattern '{self.pattern}'")

class PatternGraph:
    def __init__(self, name: str):
        self.name = name
        self._nodes: Dict[str, Node] = {}
        self._edges: Dict[str, List[str]] = {}

    def add(self, node: Node):
        if node.name in self._nodes:
            raise GraphError(f"Duplicate node name '{node.name}'")
        self._nodes[node.name] = node
        self._edges.setdefault(node.name, [])

    def link(self, source: str, target: str):
        if source not in self._nodes or target not in self._nodes:
            raise GraphError("Unknown node in link")
        self._edges.setdefault(source, []).append(target)

    def topological_order(self):
        indegree = {name: 0 for name in self._nodes}
        for _, targets in self._edges.items():
            for tgt in targets:
                indegree[tgt] += 1
        queue = [name for name, deg in indegree.items() if deg == 0]
        ordered = []
        while queue:
            name = queue.pop(0)
            ordered.append(name)
            for tgt in self._edges.get(name, []):
                indegree[tgt] -= 1
                if indegree[tgt] == 0:
                    queue.append(tgt)
        if len(ordered) != len(self._nodes):
            raise GraphError("Cycle detected in PatternGraph")
        return [self._nodes[name] for name in ordered]

    def inspect(self):
        lines = [f"PatternGraph: {self.name}", ""]
        ordered = self.topological_order()
        for i, node in enumerate(ordered):
            lines.append(f"{node.name}  [{node.pattern}]")
            if i < len(ordered) - 1:
                lines.append("    ↓")
        return "\n".join(lines)
