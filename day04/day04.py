import re
from collections import defaultdict, Counter


def read_lines():
    with open('input.txt', 'r') as f:
        return [l.strip() for l in f.readlines()]


GUARD_PATTERN = re.compile(r'Guard #(\d+) begins shift')


def main(lines):
    lines.sort()
    sleepcounts = defaultdict(lambda: Counter())
    guard = None
    awake = True
    went_to_sleep = None
    for line in lines:
        dt = line[1:17]
        minute = int(dt[-2:])
        txt = line[19:]
        match = GUARD_PATTERN.match(txt)
        if awake and match is not None:
            guard = int(match.group(1))
        elif awake and guard is not None and txt == 'falls asleep':
            awake = False
            went_to_sleep = minute
        elif not awake and guard is not None and txt == 'wakes up':
            awake = True
            for m in range(went_to_sleep, minute):
                sleepcounts[guard][m] += 1
        else:
            raise RuntimeError("Oops: '%s'" % txt)

    max_sleep = 0
    for guard, counter in sleepcounts.items():
        sleepsum = sum(counter.values())
        if sleepsum > max_sleep:
            max_sleep = sleepsum
            most_sleepy = guard
    print("Most sleepy guard: %d (%d minutes)" % (guard, max_sleep))

    max_slept = max(sleepcounts[most_sleepy].values())
    sleepiest = [m for m, cnt in sleepcounts[most_sleepy].items() if cnt == max_slept]
    print("Slept most (%d) in minute(s) %s" % (max_slept, ', '.join(('%d' % m) for m in sleepiest)))

    print("Answer = %d" % (most_sleepy * sleepiest[0]))


if __name__ == '__main__':
    main(read_lines())
