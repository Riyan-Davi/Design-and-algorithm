"""
Program 9: Implementation of Prim's Algorithm
(Minimum Spanning Tree)
"""

import heapq


def prims_mst(graph, start):
    """
    graph: dict of {node: [(neighbor, weight), ...]}
    start: starting node

    Returns the list of MST edges as (u, v, weight) and the total weight.
    """
    visited = set([start])
    edges = [(weight, start, neighbor) for neighbor, weight in graph[start]]
    heapq.heapify(edges)

    mst_edges = []
    total_weight = 0

    while edges and len(visited) < len(graph):
        weight, u, v = heapq.heappop(edges)
        if v in visited:
            continue

        visited.add(v)
        mst_edges.append((u, v, weight))
        total_weight += weight

        for neighbor, w in graph[v]:
            if neighbor not in visited:
                heapq.heappush(edges, (w, v, neighbor))

    return mst_edges, total_weight


def main():
    # Undirected weighted graph as adjacency list
    graph = {
        'A': [('B', 2), ('C', 3)],
        'B': [('A', 2), ('C', 1), ('D', 1)],
        'C': [('A', 3), ('B', 1), ('D', 4)],
        'D': [('B', 1), ('C', 4), ('E', 5)],
        'E': [('D', 5)],
    }

    print("Graph adjacency list:")
    for node, neighbors in graph.items():
        print(f"  {node}: {neighbors}")

    mst_edges, total_weight = prims_mst(graph, 'A')

    print("\nMinimum Spanning Tree edges:")
    for u, v, w in mst_edges:
        print(f"  {u} - {v} : weight {w}")

    print(f"\nTotal weight of MST: {total_weight}")


if __name__ == "__main__":
    main()