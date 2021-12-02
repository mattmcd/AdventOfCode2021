import numpy as np

x_test = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""


def read_input():
    with open('day_02_input.txt', 'r') as f:
        return f.read()


def parse_input(in_str):
    lines = in_str.split('\n')
    direction = {
        'up': np.array([0, -1]),
        'down': np.array([0, 1]),
        'forward': np.array([1, 0])
    }
    steps = np.array([direction[line.split()[0]] * int(line.split()[1]) for line in lines])
    return steps


def part_01(steps):
    return np.prod(np.sum(steps, axis=0))


def part_02(steps):
    pos = np.array([0, 0, 0])  # horiz, depth, aim
    for step in steps:
        pos = pos + [step[0], step[0]*pos[2], step[1]]
    return pos[0]*pos[1]


if __name__ == '__main__':
    steps = parse_input(read_input())
    print(f'Part 1: {part_01(steps)}')
    print(f'Part 2: {part_02(steps)}')
