# CascadeSort

> An adaptive sorting algorithm that leverages the partial order already present in a data sequence.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## Table of Contents

- [Overview](#overview)
- [Algorithm Logic](#algorithm-logic)
- [Complexity Analysis](#complexity-analysis)
- [Usage Example](#usage-example)
- [License](#license)

---

## Overview

**CascadeSort** decomposes an input sequence into sorted subsequences and recombines them into a single sorted sequence using a **Min-Heap** data structure.

The key insight is that most real-world data already contains partial order — CascadeSort identifies and exploits this structure instead of ignoring it.

---

## Algorithm Logic

CascadeSort works on the principle that any list of numbers is composed of pre-existing sorted subsequences that can be identified and extracted. Unlike other algorithms, these sequences do not need to consist of contiguous values in memory — they can be "picked" throughout the entire list.

The process consists of two main phases:

1. **Partitioning** — The input sequence is analyzed to extract chains of elements that satisfy the ascending order condition. Each extracted chain forms a subsequence ready for the next phase.
2. **Merging** — All identified subsequences are merged using a Min-Heap, which allows for the constant extraction of the minimum element among all subsequence heads, ensuring efficient merging into a final sorted sequence.

---

## Complexity Analysis

The algorithm's performance varies based on the adopted **partitioning strategy**.

### Vanilla Version

The partitioning function attempts to extract the longest possible sorted sequence by iteratively filtering the remaining elements.

| Case | Time Complexity | Space Complexity |
|------|----------------|-----------------|
| Worst Case | $O(n^2)$ | $O(n)$ |
| Avarage Case | $O(n \log k)$ | $O(n)$ |
| Best Case | $O(n)$ | $O(n)$ |

> ⚠️ In the worst case (descending order), the algorithm must repeatedly scan the remaining data, leading to quadratic cost in the partitioning phase.

---

### Optimized Version

By implementing a **linear (one-pass) partitioning**, efficiency improves drastically. Like the idea of ​​Timsort implemented natively in Python.

| Case | Time Complexity | Space Complexity |
|------|----------------|-----------------|
| Worst Case | $O(n \log n)$ | $O(n)$ |
| Avarage Case | $O(n \log k)$ | $O(n)$ |
| Best Case | $O(n)$ | $O(n)$ |

- **Partitioning**: $O(n)$
- **Merging** $k$ subsequences via Min-Heap: $O(n \log k)$, where $k \le n$
- **Adaptivity**: Particularly efficient on partially sorted data, since cost depends on the number of natural *runs* present in the original data.

---

## Example of execution

```
Original: [12, 1, 5, 8, 3, 4, 10, 2, 7, 9]

- Partitioning Phase
Iter 1:
[12]                                        ordered sub-sequence
[1, 5, 8, 3, 4, 10, 2, 7, 9]                remained sequence

Iter 2:
[12]                                        ordered sub-sequence
[1, 5, 8, 10]                               ordered sub-sequence
[3, 4, 2, 7, 9]                             remained sequence

Iter 3:
[12]                                        ordered sub-sequence
[1, 5, 8, 10]                               ordered sub-sequence
[3, 4, 7, 9]                                ordered sub-sequence
[2]                                         ordered sub-sequence

- Merge Phase
[12]            [1, 5, 8, 10]    [3, 4, 7, 9]    [2]
  |               |                |              |
 (12)            (1)              (3)            (2)
  \               \               /              /
   \ .Add()        \ .Add()      / .Add()       / .Add()
    \               \           /              /
     >-------------- [ MIN-HEAP ] ------------<
                          |
                          | .Pop()
                          |
              Sorted Output: [1, 2, 3, 4, ...]

Sorted:   [1, 2, 3, 4, 5, 7, 8, 9, 10, 12]
```

---

## License

This project is licensed under the [MIT License](LICENSE).
