"""
Program 11: Implementation of Floyd-Warshall Algorithm
(All-Pairs Shortest Path)
"""

INF = float('inf')


def floyd_warshall(graph):
    """
    graph: 2D list (n x n) adjacency matrix where graph[i][j] is the
    weight of edge i->j, or INF if there is no direct edge.
    Diagonal should be 0.

    Returns the shortest-distance matrix between all pairs of vertices.
    """
    n = len(graph)
    dist = [row[:] for row in graph]  # deep copy

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


def print_matrix(matrix, labels):
    header = "     " + "".join(f"{label:>6}" for label in labels)
    print(header)
    for i, row in enumerate(matrix):
        row_str = f"{labels[i]:>4} " + "".join(
            f"{'INF':>6}" if val == INF else f"{val:>6}" for val in row
        )
        print(row_str)


def main():
    labels = ['A', 'B', 'C', 'D']
    #        A    B    C    D
    graph = [
        [0,   3,   INF, 7],   # A
        [8,   0,   2,   INF], # B
        [5,   INF, 0,   1],   # C
        [2,   INF, INF, 0],   # D
    ]

    print("Original adjacency matrix (weights):")
    print_matrix(graph, labels)

    dist = floyd_warshall(graph)

    print("\nShortest distances between every pair of vertices:")
    print_matrix(dist, labels)


if __name__ == "__main__":
    main()