"""
Program 10: Implementation of Kruskal's Algorithm
(Minimum Spanning Tree)
"""


class DisjointSet:
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}
        self.rank = {node: 0 for node in nodes}

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])  # path compression
        return self.parent[node]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False  # already in the same set -> would form a cycle

        # union by rank
        if self.rank[root_u] < self.rank[root_v]:
            root_u, root_v = root_v, root_u
        self.parent[root_v] = root_u
        if self.rank[root_u] == self.rank[root_v]:
            self.rank[root_u] += 1

        return True


def kruskals_mst(nodes, edges):
    """
    nodes: list of all vertex names
    edges: list of (u, v, weight)

    Returns the list of MST edges and the total weight.
    """
    edges_sorted = sorted(edges, key=lambda e: e[2])
    ds = DisjointSet(nodes)

    mst_edges = []
    total_weight = 0

    for u, v, weight in edges_sorted:
        if ds.union(u, v):
            mst_edges.append((u, v, weight))
            total_weight += weight

    return mst_edges, total_weight


def main():
    nodes = ['A', 'B', 'C', 'D', 'E']
    edges = [
        ('A', 'B', 2),
        ('A', 'C', 3),
        ('B', 'C', 1),
        ('B', 'D', 1),
        ('C', 'D', 4),
        ('D', 'E', 5),
    ]

    print("Vertices:", nodes)
    print("Edges (u, v, weight):", edges)

    mst_edges, total_weight = kruskals_mst(nodes, edges)

    print("\nMinimum Spanning Tree edges:")
    for u, v, w in mst_edges:
        print(f"  {u} - {v} : weight {w}")

    print(f"\nTotal weight of MST: {total_weight}")


if __name__ == "__main__":
    main()