"""
Practical 8: Graph Traversal using DFS and BFS.
"""

from collections import deque


class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self.adj = {}

    def add_edge(self, u, v):
        self.adj.setdefault(u, [])
        self.adj.setdefault(v, [])
        self.adj[u].append(v)

        if not self.directed:
            self.adj[v].append(u)

    def dfs_recursive(self, start):
        visited = set()
        order = []

        def visit(node):
            visited.add(node)
            order.append(node)
            for neighbor in self.adj.get(node, []):
                if neighbor not in visited:
                    visit(neighbor)

        visit(start)
        return order

    def dfs_iterative(self, start):
        visited = set()
        order = []
        stack = [start]

        while stack:
            node = stack.pop()
            if node in visited:
                continue

            visited.add(node)
            order.append(node)

            # Reverse keeps traversal deterministic for this example.
            stack.extend(reversed(self.adj.get(node, [])))

        return order

    def bfs(self, start):
        visited = {start}
        order = []
        queue = deque([start])

        while queue:
            node = queue.popleft()
            order.append(node)

            for neighbor in self.adj.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return order


def main():
    graph = Graph()

    edges = [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("C", "D"),
        ("D", "E"),
        ("E", "F"),
    ]

    for u, v in edges:
        graph.add_edge(u, v)

    print("Graph edges:", edges)
    print("DFS (recursive) from A:", graph.dfs_recursive("A"))
    print("DFS (iterative) from A:", graph.dfs_iterative("A"))
    print("BFS from A:", graph.bfs("A"))


if __name__ == "__main__":
    main()
