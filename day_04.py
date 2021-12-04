import numpy as np
from day_template import read_input


x_test = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""


def parse_input(in_str):
    lines = in_str.split('\n\n')
    calls = np.array(lines[0].split(','), int)
    board_strs = [line.split('\n') for line in lines[1:]]
    boards = np.array(
        [np.array([b.split() for b in board], int) for board in board_strs]
    )
    return {'calls': calls, 'boards': boards}


def part_01(x):
    calls = x['calls']
    boards = x['boards']
    n = boards.shape[1]
    ind = np.zeros_like(boards, dtype=bool)
    board_ind = np.zeros(boards.shape[0], dtype=bool)
    call = 0
    for call in calls:
        ind |= boards == call
        new_cols = np.any(ind.sum(axis=1) == n, axis=1)
        new_rows = np.any(ind.sum(axis=2) == n, axis=1)
        if np.any(new_cols):
            board_ind = new_cols
            break
        if np.any(new_rows):
            board_ind = new_rows
            break
    return np.sum(
        boards[board_ind, ...] * (1 - ind[board_ind, ...])
    ) * call


def part_02(x):
    calls = x['calls']
    boards = x['boards']
    n = boards.shape[1]
    ind = np.zeros_like(boards, dtype=bool)
    board_ind = np.zeros(boards.shape[0], dtype=bool)
    boards_won = np.zeros(boards.shape[0], dtype=bool)
    call = 0
    for call in calls:
        ind |= boards == call
        new_cols = np.any(ind.sum(axis=1) == n, axis=1) & ~boards_won
        new_rows = np.any(ind.sum(axis=2) == n, axis=1) & ~boards_won
        if np.any(new_cols):
            board_ind = new_cols
            boards_won |= board_ind
        if np.any(new_rows):
            board_ind = new_rows
            boards_won |= board_ind
        if np.all(boards_won):
            break
    return np.sum(
        boards[board_ind, ...] * (1 - ind[board_ind, ...])
    ) * call


if __name__ == '__main__':
    x = parse_input(read_input(4))
    print(f'Part 1: {part_01(x)}')
    print(f'Part 2: {part_02(x)}')
