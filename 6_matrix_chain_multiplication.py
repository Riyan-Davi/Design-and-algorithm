"""
Program 6: Implementation of Chain Matrix Multiplication
Using Dynamic Programming
"""

import time


def matrix_chain_order(dims):
    """
    dims: list of matrix dimensions such that matrix i has dimensions
    dims[i-1] x dims[i]. For n matrices, len(dims) = n + 1.

    Returns:
        m: DP table where m[i][j] = minimum number of scalar
           multiplications needed to compute the product of matrices i..j
        s: table to reconstruct the optimal parenthesization
    """
    n = len(dims) - 1  # number of matrices
    m = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    s = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    # chain_length is the number of matrices being multiplied together
    for chain_length in range(2, n + 1):
        for i in range(1, n - chain_length + 2):
            j = i + chain_length - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                cost = (m[i][k] + m[k + 1][j] +
                        dims[i - 1] * dims[k] * dims[j])
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m, s


def print_optimal_parens(s, i, j):
    """Reconstruct and return the optimal parenthesization as a string."""
    if i == j:
        return f"M{i}"
    else:
        left = print_optimal_parens(s, i, s[i][j])
        right = print_optimal_parens(s, s[i][j] + 1, j)
        return f"({left} x {right})"


def main():
    # Example: matrices with dimensions
    # M1: 10x30, M2: 30x5, M3: 5x60, M4: 60x10, M5: 10x20, M6: 20x5
    dims = [10, 30, 5, 60, 10, 20, 5]
    n = len(dims) - 1

    print("Matrix dimensions:")
    for i in range(1, n + 1):
        print(f"  M{i}: {dims[i - 1]} x {dims[i]}")

    start = time.perf_counter()
    m, s = matrix_chain_order(dims)
    end = time.perf_counter()

    print(f"\nMinimum number of scalar multiplications: {m[1][n]}")
    print("Optimal parenthesization:", print_optimal_parens(s, 1, n))
    print(f"\nTime taken: {end - start:.6f} sec")


if __name__ == "__main__":
    main()

