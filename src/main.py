import numpy as np


def compute_stats(arr: np.ndarray) -> dict:
    return {
        'shape': arr.shape,
        'mean': float(arr.mean()),
        'std': float(arr.std()),
        'sum': float(arr.sum()),
    }


def main() -> None:
    # Simple demo: random 3x3 matrix
    rng = np.random.default_rng(42)
    data = rng.normal(loc=0.0, scale=1.0, size=(3, 3))
    stats = compute_stats(data)

    print('Data:')
    print(np.array2string(data, precision=3))
    print('\nStats:')
    for k, v in stats.items():
        print(f'{k}: {v}')


if __name__ == '__main__':
    main()
    ## change test sss
