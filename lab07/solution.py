import numpy as np

def reshape_rows(values, width):
    if len(values) % width != 0:
        return []

    arr = np.asarray(values).reshape(-1, width)

    return arr.tolist()


def block(matrix, rows, columns):
    if not matrix or not rows or not columns:
        return []

    arr = np.asarray(matrix)

    idx = np.ix_(rows, columns)
    sub_arr = arr[idx]

    return sub_arr.tolist()


def column_means(matrix):
    if not matrix:
        return []

    arr = np.asarray(matrix, dtype=float)
    means = np.mean(arr, axis=0)

    return [round(x, 6) for x in means]


def column_range(matrix, column):
    if not matrix:
        return 0.0

    arr = np.asarray(matrix, dtype=float)
    col_data = arr[:, column]

    range_val = np.max(col_data) - np.min(col_data)
    return round(float(range_val), 6)
