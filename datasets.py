"""Datasets for sorting benchmark."""
from typing import Callable, Dict, List
import random


def gen_random(size: int, seed: int) -> List[int]:
    """Random ints of given size using seed."""
    random.seed(seed)
    return [random.randint(0, size * 10) for _ in range(size)]


def gen_sorted(size: int, _seed: int) -> List[int]:
    """Ascending range"""
    return list(range(size))


def gen_reversed(size: int, _seed: int) -> List[int]:
    """Descending range"""
    return list(range(size, 0, -1))


DATASETS: Dict[str, Callable[[int, int], List[int]]] = {
    "random": gen_random,
    "sorted": gen_sorted,
    "reversed": gen_reversed,
}
