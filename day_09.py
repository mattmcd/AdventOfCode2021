import numpy as np
from day_template import read_input


x_test = """2199943210
3987894921
9856789892
8767896789
9899965678"""


def parse_input(in_str):
    return np.array([np.array([el for el in line], dtype=int) for line in in_str.split('\n')])


def find_mins(y):
    m, n = y.shape
    lt_right = np.hstack([y[:, :-1] < y[:, 1:], np.ones((m, 1), dtype=bool)])
    lt_left = np.hstack([np.ones((m, 1), dtype=bool), y[:, 1:] < y[:, :-1]])
    lt_down = np.vstack([y[:-1, :] < y[1:, :], np.ones((1, n), dtype=bool)])
    lt_up = np.vstack([np.ones((1, n), dtype=bool), y[1:, :] < y[:-1, :]])
    ind = lt_right & lt_left & lt_down & lt_up
    return ind


def find_basin(y, start):
    basin = np.zeros_like(y, dtype=bool)
    basin[start[0], start[1]] = True
    min_val = y[start[0], start[1]]
    ind_r, ind_c = np.nonzero(basin)
    res_r = ind_r.tolist()
    res_c = ind_c.tolist()
    for i in range(1, 10 - min_val):
        # Possible new basin elements
        new_ind = np.argwhere(y == (min_val + i))
        new_r = []
        new_c = []
        for j in new_ind:
            if np.any(np.abs(np.array(res_r) - j[0]) == 1) and np.any(np.abs(np.array(res_c) - j[1]) == 1):
                new_r.append(j[0])
                new_c.append(j[1])
        res_r += new_r
        res_c += new_c
    return res_r, res_c


def part_01(x):
    y = parse_input(x)
    lt_all = find_mins(y)
    return np.sum(y[lt_all] + 1)


def part_02(x):
    y = parse_input(x)
    ind = find_mins(y)
    basin_start = np.argwhere(ind)

    return 0


if __name__ == '__main__':
    p1 = part_01
    p2 = part_02
    print(f'Part 1 test: {p1(x_test)}, expected 15')
    print(f'Part 2 test: {p2(x_test)}, expected 1134')
    x = read_input(9)
    print(f'Part 1: {p1(x)}')
    print(f'Part 2: {p2(x)}')
