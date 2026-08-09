# Design and Analysis of Algorithms — Lab Programs

This repository contains Python implementations and time analysis for core Design and Analysis of Algorithms (DAA) lab experiments.

## Programs

| # | File | Description |
|---|------|-------------|
| 1 | [`1_sorting_algorithms.py`](./1_sorting_algorithms.py) | Bubble Sort, Selection Sort, Insertion Sort, Merge Sort, Quick Sort — with runtime comparison across increasing input sizes |
| 2 | [`2_search_algorithms.py`](./2_search_algorithms.py) | Linear Search, Binary Search (iterative & recursive) — with runtime comparison |
| 3 | [`3_heap_sort.py`](./3_heap_sort.py) | Max-Heap Sort using `heapify` and `build_max_heap` |
| 4 | [`4_factorial.py`](./4_factorial.py) | Factorial — iterative vs recursive implementation, with runtime comparison |
| 5 | [`5_knapsack.py`](./5_knapsack.py) | 0/1 Knapsack Problem solved using Dynamic Programming |

## How to Run

Each file is standalone and can be run directly with Python 3:

```bash
python 1_sorting_algorithms.py
python 2_search_algorithms.py
python 3_heap_sort.py
python 4_factorial.py
python 5_knapsack.py
```

Each script prints:
- A correctness check on a small sample input
- A time analysis table comparing algorithm performance across different input sizes

## Requirements

- Python 3.x (no external libraries needed — uses only `time`, `random`, and `sys` from the standard library)

## Author

Riyan Davi

