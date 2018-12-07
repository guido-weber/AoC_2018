import re
from collections import defaultdict, Counter


def read_lines():
    with open('input.txt', 'r') as f:
        return [l.strip() for l in f.readlines()]


PATTERN = re.compile(r'Step (\w+) must be finished before step (\w+) can begin.')


def part1(lines):
    reqs = [match.group(1, 2) for match in (PATTERN.match(line) for line in lines)]
    all = set(r[0] for r in reqs) | set(r[1] for r in reqs)
    result = []
    while reqs:
        waiting = set(r[1] for r in reqs)
        next = sorted(all - waiting)[0]
        result.append(next)
        all.remove(next)
        reqs = [(p, g) for p, g in reqs if p != next]
    result.extend(sorted(all))
    print(''.join(result))


TEST = [
    'Step C must be finished before step A can begin.',
    'Step C must be finished before step F can begin.',
    'Step A must be finished before step B can begin.',
    'Step A must be finished before step D can begin.',
    'Step B must be finished before step E can begin.',
    'Step D must be finished before step E can begin.',
    'Step F must be finished before step E can begin.'
]


if __name__ == '__main__':
    # part1(TEST)
    part1(read_lines())
