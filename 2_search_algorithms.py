"""
Program 2: Implementation and Time Analysis of
Linear Search and Binary Search Algorithms
"""

import time
import random


# ---------------- Linear Search ----------------
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# ---------------- Binary Search (Iterative) ----------------
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# ---------------- Binary Search (Recursive) ----------------
def binary_search_recursive(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)


# ---------------- Time Analysis ----------------
def time_it(func, *args):
    start = time.perf_counter()
    result = func(*args)
    end = time.perf_counter()
    return result, end - start


def main():
    sizes = [1000, 10000, 100000, 500000]

    print("Correctness check:")
    sample = [5, 2, 9, 1, 7, 3]
    sorted_sample = sorted(sample)
    print("Array:", sample, "| Sorted:", sorted_sample)
    print("Linear search for 7:", linear_search(sample, 7))
    print("Binary search for 7 (sorted):", binary_search(sorted_sample, 7))
    print("Binary search recursive for 7 (sorted):",
          binary_search_recursive(sorted_sample, 7))

    print("\nTime Analysis (seconds), searching for worst-case element:")
    header = f"{'Size':<10}{'Linear Search':<18}{'Binary Search':<18}{'Binary (Recursive)':<20}"
    print(header)

    for size in sizes:
        arr = list(range(size))          # already sorted, unique values
        target = -1                      # worst case: not present -> full scan
        _, t_linear = time_it(linear_search, arr, target)
        _, t_binary = time_it(binary_search, arr, target)
        _, t_binary_rec = time_it(binary_search_recursive, arr, target)
        print(f"{size:<10}{t_linear:<18.6f}{t_binary:<18.6f}{t_binary_rec:<20.6f}")


if __name__ == "__main__":
    main()