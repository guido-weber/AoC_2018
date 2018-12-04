import re
from collections import defaultdict, Counter


def read_lines():
    with open('input.txt', 'r') as f:
        return [l.strip() for l in f.readlines()]


GUARD_PATTERN = re.compile(r'Guard #(\d+) begins shift')


def parse_events(lines):
    # Sorting the lines alphabetically is enough to bring them in the correct order
    lines.sort()
    # The result of this function is a mapping (guard, minute) -> #asleep
    result = defaultdict(Counter)
    guard = None
    awake = True
    went_to_sleep = None
    # For each sleep phase, add 1 to each minute of that phase for the guard.
    # Added additional checks to verify event ordering is plausible.
    for line in lines:
        minute = int(line[15:17])
        txt = line[19:]
        match = GUARD_PATTERN.match(txt)
        if awake and match is not None:
            guard = int(match.group(1))
        elif awake and guard is not None and txt == 'falls asleep':
            awake = False
            went_to_sleep = minute
        elif not awake and guard is not None and txt == 'wakes up':
            awake = True
            result[guard].update(range(went_to_sleep, minute))
        else:
            raise RuntimeError("Oops: %s" % line)
    return result


def part1(sleepcounts):
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

    print("Part 1 answer = %d" % (most_sleepy * sleepiest[0]))


def part2(sleepcounts):
    max_count = 0
    for guard, counter in sleepcounts.items():
        [(minute, cnt)] = counter.most_common(1)
        if cnt > max_count:
            the_guard = guard
            the_minute = minute
            max_count = cnt
    print("Part 2: guard = %d, minute = %d, answer = %d"
          % (the_guard, the_minute, the_guard * the_minute))


def main(lines):
    sleepcounts = parse_events(lines)
    part1(sleepcounts)
    part2(sleepcounts)


if __name__ == '__main__':
    main(read_lines())
