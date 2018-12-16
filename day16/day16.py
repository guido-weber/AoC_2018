import re
from instructions import Instruction


def read_lines():
    with open('input.txt', 'r') as f:
        return [l.strip() for l in f.readlines()]


P_BEFORE = re.compile(r'Before:.*(\d+),\s*(\d+),\s*(\d+),\s*(\d+).*')
P_AFTER = re.compile(r'After:.*(\d+),\s*(\d+),\s*(\d+),\s*(\d+).*')


def extract_samples(lines):
    lnum = 0
    samples = []
    while lines[lnum].startswith('Before'):
        before = [int(x) for x in P_BEFORE.match(lines[lnum]).group(1, 2, 3, 4)]
        instruction = [int(x) for x in lines[lnum + 1].split()]
        after = [int(x) for x in P_AFTER.match(lines[lnum + 2]).group(1, 2, 3, 4)]
        samples.append((before, instruction, after))
        assert lines[lnum + 3] == ''
        lnum += 4
    return samples


def count_possible_opcodes(sample):
    result = 0
    for instruction in Instruction.ALL.values():
        i = instruction(*sample[1][1:])
        if i(sample[0]) == sample[2]:
            result += 1
    return result


if __name__ == '__main__':
    lines = read_lines()
    part1 = 0
    for sample in extract_samples(lines):
        cnt = count_possible_opcodes(sample)
        if cnt >= 3:
            part1 += 1
    print("Part1: %s" % part1)
