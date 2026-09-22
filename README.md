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
| 6 | [`6_matrix_chain_multiplication.py`](./6_matrix_chain_multiplication.py) | Matrix Chain Multiplication solved using Dynamic Programming |
| 7 | [`7_coin_change.py`](./7_coin_change.py) | Coin Change (Making Change) Problem solved using Dynamic Programming |
| 8 | [`8_graph_dfs_bfs.py`](./8_graph_dfs_bfs.py) | Graph implementation with Depth First Search (DFS) and Breadth First Search (BFS) |
| 9 | [`9_prims_algorithm.py`](./9_prims_algorithm.py) | Prim's Algorithm for Minimum Spanning Tree |
| 10 | [`10_kruskals_algorithm.py`](./10_kruskals_algorithm.py) | Kruskal's Algorithm for Minimum Spanning Tree |
| 11 | [`11_floyd_warshall.py`](./11_floyd_warshall.py) | Floyd-Warshall Algorithm for All-Pairs Shortest Path |
| 12 | [`12_travelling_salesman.py`](./12_travelling_salesman.py) | Travelling Salesman Problem solved using Dynamic Programming (Held-Karp / bitmasking) |

## How to Run

Each file is standalone and can be run directly with Python 3:

```bash
python 1_sorting_algorithms.py
python 2_search_algorithms.py
python 3_heap_sort.py
python 4_factorial.py
python 5_knapsack.py
python 6_matrix_chain_multiplication.py
python 7_coin_change.py
python 8_graph_dfs_bfs.py
python 9_prims_algorithm.py
python 10_kruskals_algorithm.py
python 11_floyd_warshall.py
python 12_travelling_salesman.py
```

Each script prints:
- A correctness check on a small sample input
- A time analysis table comparing algorithm performance across different input sizes

## Requirements

- Python 3.x (no external libraries needed — uses only `time`, `random`, and `sys` from the standard library)

## Author

Riyan Davi