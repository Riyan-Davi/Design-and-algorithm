"""
Program 4: Implementation and Time Analysis of Factorial Program
Using Iterative and Recursive Methods
"""

import time
import sys

sys.setrecursionlimit(10000)


# ---------------- Iterative Factorial ----------------
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# ---------------- Recursive Factorial ----------------
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


# ---------------- Time Analysis ----------------
def time_it(func, n):
    start = time.perf_counter()
    func(n)
    end = time.perf_counter()
    return end - start


def main():
    n = 10
    print(f"Factorial of {n} (Iterative): {factorial_iterative(n)}")
    print(f"Factorial of {n} (Recursive): {factorial_recursive(n)}")

    print("\nTime Analysis (seconds):")
    values = [100, 500, 1000, 3000]
    header = f"{'n':<8}{'Iterative':<18}{'Recursive':<18}"
    print(header)

    for val in values:
        t_iter = time_it(factorial_iterative, val)
        t_rec = time_it(factorial_recursive, val)
        print(f"{val:<8}{t_iter:<18.8f}{t_rec:<18.8f}")


if __name__ == "__main__":
    main()