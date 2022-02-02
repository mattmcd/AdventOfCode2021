import numpy as np
import tensorflow as tf
from day_template import read_input


x_test = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""


def parse_input(in_str):
    return np.array([np.array([el for el in line], dtype=np.int32) for line in in_str.split('\n')])


def step_cells(y):
    y_s = tf.constant(y, dtype=tf.int32, shape=(1, *y.shape, 1))
    neighbours = tf.reshape(
        tf.constant([[1, 1, 1], [1, 0, 1], [1, 1, 1]], dtype=tf.int32),
        (3, 3, 1, 1)
    )
    ind = tf.cast(y_s >= 10, tf.int32)
    inc = tf.nn.conv2d(ind, neighbours, 1, padding='SAME') * tf.cast(ind < 1, tf.int32)
    y_f = tf.minimum(y_s + inc, 10)
    return y_f.numpy()[0, ..., 0], np.sum(inc.numpy() > 0)


def step(y):
    y += 1
    n_flash = 0
    for i in range(9):
        y, new_flash = step_cells(y)
        n_flash += new_flash
    return y, n_flash


def part_01(x):
    y = parse_input(x)
    n_flash = 0
    for i in range(10):
        y, new_flash = step(y)
        print(y[0,...,0])
        print(i+1, n_flash)

    return n_flash


def part_02(x):
    y = parse_input(x)
    return None


if __name__ == '__main__':
    p1 = part_01
    p2 = part_02
    print(f'Part 1 test: {p1(x_test)}, expected 26397')
    print(f'Part 2 test: {p2(x_test)}, expected ?')
    x = read_input(11)
    print(f'Part 1: {p1(x)}')
    print(f'Part 2: {p2(x)}')
