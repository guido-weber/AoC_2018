import re
from collections import defaultdict, Counter


def read_lines():
    with open('input.txt', 'r') as f:
        return [l.strip() for l in f.readlines()]


PATTERN = re.compile(r'Step (\w+) must be finished before step (\w+) can begin.')


def part1(reqs):
    all = set(r[0] for r in reqs) | set(r[1] for r in reqs)
    result = []
    while reqs:
        waiting = set(r[1] for r in reqs)
        next = sorted(all - waiting)[0]
        result.append(next)
        all.remove(next)
        reqs = [(p, g) for p, g in reqs if p != next]
    result.extend(sorted(all))
    print("Part 1: %s" % (''.join(result)))


def part2(reqs, workers, add_time):
    steps_to_do = set(r[0] for r in reqs) | set(r[1] for r in reqs)
    doing = set()
    current_time = 0
    running_tasks = defaultdict(set)
    while steps_to_do:
        completed = running_tasks.pop(current_time, None)
        if completed is not None:
            doing -= completed
            steps_to_do -= completed
            reqs = [(p, g) for p, g in reqs if p not in completed]
        free_workers = workers - len(doing)
        if free_workers > 0:
            possible = sorted(steps_to_do - doing - set(r[1] for r in reqs))
            next_steps = possible[:free_workers]
            for step in next_steps:
                done_time = current_time + ord(step) - ord('A') + 1 + add_time
                running_tasks[done_time].add(step)
                doing.add(step)
        if running_tasks:
            current_time = min(running_tasks.keys())
    print("Part 2: all done at %d" % current_time)


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
    # lines, workers, add_time = TEST, 2, 0
    lines, workers, add_time = read_lines(), 5, 60
    reqs = [match.group(1, 2) for match in (PATTERN.match(line) for line in lines)]
    part1(reqs[:])
    part2(reqs[:], workers, add_time)
