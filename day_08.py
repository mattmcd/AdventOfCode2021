import numpy as np
from day_template import read_input


x_test_simple = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"

x_test = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""


def parse_input(in_str):
    return [parse_line(line) for line in in_str.split('\n')]


def parse_line(in_str):
    example_str, display_str = in_str.split(' | ')
    examples = example_str.split(' ')
    display = display_str.split(' ')
    return {'examples': examples, 'display': display}


def count_1478(display):
    return np.sum([len(s) in {2, 4, 3, 7} for s in display])


def sort_str(s):
    return ''.join(sorted(list(s)))


def map_symbols(examples):
    digit_len_map = {2: 1, 3: 7, 4: 4, 7: 8}
    mapping = dict([(digit_len_map[len(s)], sort_str(s)) for s in examples if len(s) in digit_len_map])
    seg_A = sort_str(set(mapping[7]) - set(mapping[1]))
    mapping[3] = [sort_str(s) for s in examples if len(set(s) - set(mapping[1])) == 3 and len(s) == 5][0]
    seg_G = sort_str((set(mapping[3]) - set(mapping[4])) - set(seg_A))
    mapping[9] = sort_str(mapping[4] + seg_A + seg_G)
    seg_E = sort_str(set(mapping[8]) - set(mapping[9]))
    mapping[2] = [
        sort_str(s) for s in examples
        if len(s) == 5 and sort_str(s) not in mapping.values() and seg_E in s][0]
    mapping[5] = [
        sort_str(s) for s in examples
        if len(s) == 5 and sort_str(s) not in mapping.values()][0]
    seg_F = sort_str(set(mapping[1]) - set(mapping[5]))
    mapping[6] = sort_str(mapping[5] + seg_E)
    mapping[0] = [
        sort_str(s) for s in examples
        if len(s) == 6 and sort_str(s) not in mapping.values()][0]
    segs = {'A': seg_A, 'E': seg_E, 'G': seg_G, 'F': seg_F}
    str_to_digit = {v: k for k, v in mapping.items()}
    return str_to_digit


def part_01(x):
    y = parse_input(x)
    return np.sum([count_1478(e['display']) for e in y])


def part_02(x):
    y = parse_input(x)
    acc = 0
    for el in y:
        mapping = map_symbols(el['examples'])
        d = [sort_str(s) for s in el['display']]
        value = 1000 * mapping[d[0]] + 100 * mapping[d[1]] + 10 * mapping[d[2]] + mapping[d[3]]
        acc += value
    return acc


if __name__ == '__main__':
    p1 = part_01
    p2 = part_02
    print(f'Part 1 test: {p1(x_test)}, expected 26')
    print(f'Part 2 test: {p2(x_test)}, expected 61229')
    x = read_input(8)
    print(f'Part 1: {p1(x)}')
    print(f'Part 2: {p2(x)}')
