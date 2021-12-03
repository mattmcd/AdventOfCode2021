import numpy as np
from day_template import read_input

x_test = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""


def parse_input(in_str):
    return np.array(
        [np.array([int(b) for b in s])
         for s in in_str.split('\n')]
    )


def most_common(x):
    return 1 * ((2 * x.sum(axis=0) // x.shape[0]) >= 1)


def least_common(x):
    return 1 * ((2 * x.sum(axis=0) // x.shape[0]) < 1)


def part_01(x):
    n_row, n_col = x.shape
    bit_value = 2**(np.arange(n_col)[::-1])
    gamma_rate = most_common(x) @ bit_value
    epsilon_rate = least_common(x) @ bit_value
    res = gamma_rate * epsilon_rate
    return res


def part_02(x):
    n_row, n_col = x.shape
    sum_row = x.sum(axis=0)
    bit_value = 2 ** (np.arange(n_col)[::-1])
    # ox_rate
    ox_set = x
    ox_most_common = most_common(ox_set)
    for i in range(n_col):
        ox_set = ox_set[ox_set[:, i] == ox_most_common[i], :]
        ox_most_common = most_common(ox_set)
        if len(ox_set) == 1:
            break
    co2_set = x
    co2_least_common = least_common(co2_set)
    for i in range(n_col):
        co2_set = co2_set[co2_set[:, i] == co2_least_common[i], :]
        co2_least_common = least_common(co2_set)
        if len(co2_set) == 1:
            break
    ox_val = ox_set.flat @ bit_value
    co2_val = co2_set.flat @ bit_value

    return ox_val * co2_val


if __name__ == '__main__':
    x = parse_input(read_input(3))
    print(f'Part 1: {part_01(x)}')
    print(f'Part 2: {part_02(x)}')
