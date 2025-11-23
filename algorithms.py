"""Sorting algorithms and registry for benchmark."""
from typing import Callable, Dict, List


def insertion_sort(arr: List[int]) -> List[int]:
    """Insertion sort; returns new sorted list."""
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def merge_sort(arr: List[int]) -> List[int]:
    """Merge sort; returns new sorted list."""
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left: List[int], right: List[int]) -> List[int]:
    """Merge two sorted lists."""
    i = j = 0
    merged: List[int] = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    if i < len(left):
        merged.extend(left[i:])
    if j < len(right):
        merged.extend(right[j:])
    return merged


def python_sorted(arr: List[int]) -> List[int]:
    """Wrapper for built-in sorted()."""
    return sorted(arr)


ALGORITHMS: Dict[str, Callable[[List[int]], List[int]]] = {
    "insertion": insertion_sort,
    "merge": merge_sort,
    "timsort": python_sorted,  # Python's built-in sorted()
}
