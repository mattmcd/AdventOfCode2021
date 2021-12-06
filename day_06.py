import numpy as np
from day_template import read_input


x_test = """3,4,3,1,2"""


def parse_input(in_str):
    ages = np.array(in_str.split(','), int)
    return ages


def step(c_age):
    breed_count = c_age[0]
    c_age_next = np.roll(c_age, -1).copy()
    c_age_next[6] += breed_count
    return c_age_next


def pop_count(ages, n_step):
    age_count = np.zeros(9, dtype=int)
    for i in range(9):
        age_count[i] = np.sum(ages == i)

    for i in range(n_step):
        age_count = step(age_count)

    return np.sum(age_count)


def part_01(x):
    return pop_count(parse_input(x), 80)


def part_02(x):
    return pop_count(parse_input(x), 256)


if __name__ == '__main__':
    print(f'Part 1 test: {part_01(x_test)}')
    print(f'Part 2 test: {part_02(x_test)}')
    x = read_input(6)
    print(f'Part 1: {part_01(x)}')
    print(f'Part 2: {part_02(x)}')
