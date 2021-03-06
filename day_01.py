import numpy as np

x_test = np.array([199, 200, 208,210, 200, 207, 240, 269, 260, 263], dtype='int')


def read_input():
    with open('day_01_input.txt', 'r') as f:
        return np.array(f.read().split('\n'), dtype='int')


def part_01(x):
    # Number of increases
    return np.sum((x[1:] - x[0:-1]) > 0)


def part_02(x):
    # Number of increases of 3 element rolling window
    return part_01(np.convolve(x, np.ones(3), 'valid'))


if __name__ == '__main__':
    x = read_input()
    print(f'Part 1: {part_01(x)}')
    print(f'Part 2: {part_02(x)}')
