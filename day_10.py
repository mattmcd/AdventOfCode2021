import numpy as np
from day_template import read_input


x_test = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""


def parse_input(in_str):
    return in_str.split('\n')


def parse_line(line):
    count = {'(': 0, '[': 0, '{': 0, '<': 0}
    close_map = {')': '(', ']': '[', '}': '{', '>': '<'}
    corrupt_char = ''
    found_corrupt = False
    prev_open = []
    for el in line:
        if el in {'(', '[', '{', '<'}:
            count[el] += 1
            prev_open.append(el)
        else:
            count[close_map[el]] -= 1
            if prev_open[-1] != close_map[el]:
                corrupt_char = el
                break
    incomplete = np.any(np.array(list(count.values())) > 0)
    return corrupt_char, incomplete


def part_01(x):
    lines = parse_input(x)
    res = [parse_line(line) for line in lines]
    return res

def part_02(x):
    y = parse_input(x)
    return None


if __name__ == '__main__':
    p1 = part_01
    p2 = part_02
    print(f'Part 1 test: {p1(x_test)}, expected 26397')
    print(f'Part 2 test: {p2(x_test)}, expected ?')
    x = read_input(10)
    print(f'Part 1: {p1(x)}')
    print(f'Part 2: {p2(x)}')
