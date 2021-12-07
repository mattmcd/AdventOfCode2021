import numpy as np
from day_template import read_input


x_test = "16,1,2,0,4,2,7,1,2,14"


def parse_input(in_str):
    return np.array(in_str.split(','), dtype=int).reshape((-1, 1))


def calc_min_fuel(crab_pos, fuel_cost=None):
    align_pos = np.arange(np.min(crab_pos), np.max(crab_pos)).reshape((-1, 1))
    pos_diff = np.abs(crab_pos - align_pos.T)
    fuel_diff = fuel_cost(pos_diff)
    min_pos = np.argmin(np.sum(fuel_diff, axis=0))
    min_fuel = fuel_diff[:, min_pos].sum()
    return min_fuel


def part_01(x):
    crab_pos = parse_input(x)
    fuel_cost = lambda d: d
    return calc_min_fuel(crab_pos, fuel_cost)


def part_02(x):
    crab_pos = parse_input(x)
    fuel_cost = lambda d: (d**2 + d) // 2  # Triangular numbers
    return calc_min_fuel(crab_pos, fuel_cost)


# From the reddit thread:
# part 1 is equivalent to minimizing the l1-norm => median
def part_01_v2(x):
    crab_pos = parse_input(x)
    x_min = int(np.median(crab_pos))
    return np.abs(crab_pos - x_min).sum()


# From the reddit thread:
# part 2 is equivalent to minimizing the l2-norm + extra linear term => mean and search
def part_02_v2(x):
    crab_pos = parse_input(x)
    x_min = np.mean(crab_pos)

    def fuel_cost(x_p, x0):
        y = np.abs(x_p - x0)
        return (y*(y+1) // 2).sum()

    return min(fuel_cost(crab_pos, x0) for x0 in [int(np.floor(x_min)), int(np.ceil(x_min))])


if __name__ == '__main__':
    p1 = part_01_v2
    p2 = part_02_v2
    print(f'Part 1 test: {p1(x_test)}, expected 37')
    print(f'Part 2 test: {p2(x_test)}, expected 168')
    x = read_input(7)
    print(f'Part 1: {p1(x)}')
    print(f'Part 2: {p2(x)}')
