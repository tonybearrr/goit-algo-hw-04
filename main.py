"""Sorting benchmark: generate datasets and measure sorting times."""
import timeit
from typing import Callable, List
from datasets import DATASETS
from algorithms import ALGORITHMS


DEFAULT_SIZES: List[int] = [1000, 3000] # sizes of the datasets
DEFAULT_DISTS: List[str] = ["random", "reversed", "sorted"]
DEFAULT_ALGOS: List[str] = ["timsort", "merge", "insertion"]
DEFAULT_SEED: int = 42 # seed for random number generator

def time_algo(
    algo: Callable[[List[int]], List[int]],
    data: List[int]
) -> float:
    """Measure time with timeit; return best average seconds per run."""
    number = 2 # number of runs per algorithm
    repeat = 2 # number of times to repeat the experiment
    timer = timeit.Timer(lambda: algo(data))
    times = timer.repeat(repeat=repeat, number=number)
    best_total = min(times)
    return best_total / number


def run_benchmark(
    sizes: List[int],
    dists: List[str],
    algos: List[str],
    seed: int,
) -> None:
    """Generate datasets, run algorithms, print timings table."""
    # header
    print(f"\n\nSeed = {seed}")
    print(f"Algorithms: {', '.join(algos)}")
    print()
    header = f"{'size':>7}  {'dist':>15}  " + "  ".join(f"{a:>10}" for a in algos)
    print(header)
    print("-" * len(header))

    for size in sizes:
        for dist in dists:
            gen = DATASETS[dist]
            data = gen(size, seed)
            timings = []
            for a in algos:
                algo = ALGORITHMS[a]
                elapsed = time_algo(algo, data)
                timings.append(elapsed)
            row = f"{size:7d}  {dist:>15}  " + "  ".join(f"{t:10.6f}" for t in timings)
            print(row)


def main() -> None:
    """Entry point: run benchmark with defaults."""
    run_benchmark(DEFAULT_SIZES, DEFAULT_DISTS, DEFAULT_ALGOS, DEFAULT_SEED)


if __name__ == "__main__":
    main()
