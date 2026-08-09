"""
Program 1: Implementation and Time Analysis of Sorting Algorithms
Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, Quick Sort
"""

import time
import random


# ---------------- Bubble Sort ----------------
def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a


# ---------------- Selection Sort ----------------
def selection_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


# ---------------- Insertion Sort ----------------
def insertion_sort(arr):
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


# ---------------- Merge Sort ----------------
def merge_sort(arr):
    a = arr.copy()
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return _merge(left, right)


def _merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# ---------------- Quick Sort ----------------
def quick_sort(arr):
    a = arr.copy()
    _quick_sort_helper(a, 0, len(a) - 1)
    return a


def _quick_sort_helper(a, low, high):
    if low < high:
        pi = _partition(a, low, high)
        _quick_sort_helper(a, low, pi - 1)
        _quick_sort_helper(a, pi + 1, high)


def _partition(a, low, high):
    pivot = a[high]
    i = low - 1
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    return i + 1


# ---------------- Time Analysis ----------------
def time_it(func, arr):
    start = time.perf_counter()
    func(arr)
    end = time.perf_counter()
    return end - start


def main():
    sizes = [100, 500, 1000, 2000]
    algorithms = {
        "Bubble Sort": bubble_sort,
        "Selection Sort": selection_sort,
        "Insertion Sort": insertion_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort,
    }

    # Correctness demo
    sample = [64, 25, 12, 22, 11, 90, 5]
    print("Original array:", sample)
    for name, func in algorithms.items():
        print(f"{name}: {func(sample)}")

    print("\nTime Analysis (seconds) on random arrays:")
    header = f"{'Size':<8}" + "".join(f"{name:<18}" for name in algorithms)
    print(header)

    for size in sizes:
        arr = [random.randint(0, 100000) for _ in range(size)]
        row = f"{size:<8}"
        for name, func in algorithms.items():
            elapsed = time_it(func, arr)
            row += f"{elapsed:<18.6f}"
        print(row)


if __name__ == "__main__":
    main()