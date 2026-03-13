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

**CascadeSort** decomposes an input sequence into sorted subsequences (called *runs*) and recombines them into a single sorted sequence using a **Min-Heap** data structure.

The key insight is that most real-world data already contains partial order — CascadeSort identifies and exploits this structure instead of ignoring it.

---

## Algorithm Logic

CascadeSort works on the principle that any list of numbers is composed of pre-existing sorted subsequences that can be identified and extracted. Unlike other algorithms, these sequences do not need to consist of contiguous values in memory — they can be "picked" throughout the entire list.

The process consists of two main phases:

1. **Partitioning** — The input sequence is analyzed to extract chains of elements that satisfy the ascending order condition. Each extracted chain forms a subsequence ready for the next phase.
2. **Merging** — All identified subsequences are merged using a Min-Heap, which allows for the constant extraction of the minimum element among all subsequence heads, ensuring efficient merging into a final sorted sequence.

---

## Complexity Analysis

The algorithm's performance varies based on the adopted partitioning strategy.

### Vanilla Case (Original Version)

The partitioning function attempts to extract the longest possible sorted sequence by iteratively filtering the remaining elements.

| Case | Time Complexity | Space Complexity |
|------|----------------|-----------------|
| Worst Case | $O(n^2)$ | $O(n)$ |
| Avarage Case | $O(n \log k)$ | $O(n)$ |
| Best Case | $O(n)$ | $O(n)$ |

> ⚠️ In the worst case (descending order), the algorithm must repeatedly scan the remaining data, leading to quadratic cost in the partitioning phase.

---

### Optimized Case (Timsort Logic)

By implementing a **linear (one-pass) partitioning**, efficiency improves drastically.

| Case | Time Complexity | Space Complexity |
|------|----------------|-----------------|
| Worst Case | $O(n \log n)$ | $O(n)$ |
| Avarage Case | $O(n \log k)$ | $O(n)$ |
| Best Case | $O(n)$ | $O(n)$ |

- **Partitioning**: $O(n)$
- **Merging** $k$ subsequences via Min-Heap: $O(n \log k)$, where $k \le n$
- **Adaptivity**: Particularly efficient on partially sorted data, since cost depends on the number of natural *runs* present in the original data.

---

## Usage Example

Import the `CascadeSort` function and pass any list of comparable elements:

```python
from CascadeSort import CascadeSort

# Definition of an unsorted sequence
data = [12, 1, 5, 8, 3, 4, 10, 2, 7, 9]

# Execution of the algorithm
sorted_data = CascadeSort(data)

print(f"Original: {data}")
print(f"Sorted:   {sorted_data}")
```

**Output:**
```
Original: [12, 1, 5, 8, 3, 4, 10, 2, 7, 9]
Sorted:   [1, 2, 3, 4, 5, 7, 8, 9, 10, 12]
```

---

## License

This project is licensed under the [MIT License](LICENSE).
