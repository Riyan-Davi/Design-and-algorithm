"""
Program 5: Implementation of 0/1 Knapsack Problem
Using Dynamic Programming
"""

import time


def knapsack_dp(weights, values, capacity):
    n = len(weights)
    # dp[i][w] = max value using first i items with capacity w
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    # Backtrack to find selected items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]
    selected_items.reverse()

    return dp[n][capacity], selected_items


def main():
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5

    print("Weights:", weights)
    print("Values :", values)
    print("Capacity:", capacity)

    start = time.perf_counter()
    max_value, items = knapsack_dp(weights, values, capacity)
    end = time.perf_counter()

    print(f"\nMaximum value obtainable: {max_value}")
    print("Items included (0-indexed):", items)
    for idx in items:
        print(f"  Item {idx}: weight={weights[idx]}, value={values[idx]}")

    print(f"\nTime taken: {end - start:.6f} sec")


if __name__ == "__main__":
    main()