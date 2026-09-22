"""
Program 12: Implementation of the Travelling Salesman Problem (TSP)
Using Dynamic Programming with Bitmasking (Held-Karp algorithm)
"""

import time

INF = float('inf')


def tsp_dp(dist):
    """
    dist: n x n distance matrix, dist[i][j] = distance from city i to city j.
    Assumes the tour starts and ends at city 0.

    Returns (minimum_cost, best_path) using the Held-Karp DP approach.
    """
    n = len(dist)
    # dp[mask][i] = minimum cost to have visited the set of cities in 'mask',
    # ending at city i (mask always includes city 0 and city i)
    dp = [[INF] * n for _ in range(1 << n)]
    parent = [[-1] * n for _ in range(1 << n)]

    dp[1][0] = 0  # start at city 0, only city 0 visited (bit 0 set)

    for mask in range(1 << n):
        for u in range(n):
            if dp[mask][u] == INF:
                continue
            if not (mask & (1 << u)):
                continue
            for v in range(n):
                if mask & (1 << v):
                    continue  # already visited
                new_mask = mask | (1 << v)
                new_cost = dp[mask][u] + dist[u][v]
                if new_cost < dp[new_mask][v]:
                    dp[new_mask][v] = new_cost
                    parent[new_mask][v] = u

    # Close the tour: return to city 0 from every possible last city
    full_mask = (1 << n) - 1
    best_cost = INF
    best_last = -1
    for u in range(1, n):
        if dp[full_mask][u] + dist[u][0] < best_cost:
            best_cost = dp[full_mask][u] + dist[u][0]
            best_last = u

    # Reconstruct path (the parent chain already terminates at city 0)
    path = []
    mask = full_mask
    u = best_last
    while u != -1:
        path.append(u)
        prev = parent[mask][u]
        mask ^= (1 << u)
        u = prev
    path.reverse()

    return best_cost, path


def main():
    # Distance matrix between 4 cities (0, 1, 2, 3)
    dist = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0],
    ]

    print("Distance matrix:")
    for row in dist:
        print(" ", row)

    start = time.perf_counter()
    min_cost, path = tsp_dp(dist)
    end = time.perf_counter()

    print(f"\nMinimum tour cost: {min_cost}")
    print("Optimal path:", " -> ".join(map(str, path)) + " -> 0")
    print(f"\nTime taken: {end - start:.6f} sec")


if __name__ == "__main__":
    main()