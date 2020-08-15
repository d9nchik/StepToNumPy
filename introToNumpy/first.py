import numpy as np


def custom_sum(arg1, arg2):
    if isinstance(arg1, list) and isinstance(arg2, list):
        return 'Both arguments are lists, not arrays'
    elif isinstance(arg1, list) or isinstance(arg2, list):
        return 'One argument is a list'
    else:
        return arg1 + arg2


def collect_info(array: np.ndarray):
    return 'Shape: {}; dimensions: {}; length: {}; size: {}'.format(array.shape, array.ndim, len(array), array.size)
