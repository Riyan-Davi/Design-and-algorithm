"""
Program 3: Implementation of Max-Heap Sort Algorithm
"""

import time
import random


def heapify(arr, n, i):
    """Ensure the subtree rooted at index i is a max-heap, arr has size n."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def build_max_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


def heap_sort(arr):
    a = arr.copy()
    n = len(a)

    # Step 1: Build a max heap
    build_max_heap(a)

    # Step 2: Repeatedly extract the maximum element
    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]   # move current root (max) to the end
        heapify(a, i, 0)          # heapify the reduced heap

    return a


def time_it(func, arr):
    start = time.perf_counter()
    func(arr)
    end = time.perf_counter()
    return end - start


def main():
    sample = [12, 11, 13, 5, 6, 7, 1, 9]
    print("Original array:", sample)
    print("Max-Heap Sorted array:", heap_sort(sample))

    print("\nTime Analysis (seconds):")
    sizes = [100, 1000, 10000, 50000]
    for size in sizes:
        arr = [random.randint(0, 100000) for _ in range(size)]
        elapsed = time_it(heap_sort, arr)
        print(f"Size: {size:<10} Time: {elapsed:.6f} sec")


if __name__ == "__main__":
    main()