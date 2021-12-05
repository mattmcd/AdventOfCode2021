import numpy as np
from day_template import read_input

x_test = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


def parse_input(in_str):
    lines = np.array(
        [[pos[0].split(','), pos[1].split(',')]
         for pos in [
             line.split(' -> ') for line in in_str.split('\n')
         ]
         ], dtype=int)
    return lines


def part_01(x, include_diag=False):
    pos_diff = np.array([-1, 1]) @ x
    if not include_diag:
        ind_h_v = (pos_diff == 0).any(axis=1)
        y = x[ind_h_v, ...].copy()
    else:
        y = x.copy()

    x_max, y_max = np.max(np.max(y, axis=0), axis=0)
    # Have x go across cols, y down rows
    crossing = np.zeros((y_max+1, x_max+1), dtype=int)
    for i in range(y.shape[0]):
        # print(y[i, ...])
        start = y[i, 0, :]
        end = y[i, 1, :]
        if start[0] == end[0]:
            # Same x coordinates
            s = min(start[1], end[1])
            e = max(start[1], end[1])
            crossing[s:e+1, start[0]] += 1
        elif start[1] == end[1]:
            # Same y coordinates
            s = min(start[0], end[0])
            e = max(start[0], end[0])
            crossing[start[1], s:e+1] += 1
        else:
            # Diagonal lines
            step = (pos_diff[i, :] > 0)*1 + (pos_diff[i, :] < 0)*-1
            n_step = int(np.abs(pos_diff[i, 1] / step[0]))
            for j in range(n_step+1):
                crossing[start[1] + j*step[1], start[0] + j*step[0]] += 1

        # print(crossing)

    n_max = np.sum(crossing >= 2)
    return n_max


def part_02(x):
    return part_01(x, include_diag=True)


if __name__ == '__main__':
    print(f'Part 1 test: {part_01(parse_input(x_test))}')
    print(f'Part 2 test: {part_02(parse_input(x_test))}')
    x = parse_input(read_input(5))
    print(f'Part 1: {part_01(x)}')
    print(f'Part 2: {part_02(x)}')
