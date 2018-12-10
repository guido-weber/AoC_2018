import re
from collections import defaultdict, Counter


def read_lines():
    with open('input.txt', 'r') as f:
        return [l.strip() for l in f.readlines()]


PATTERN = re.compile(r'position=<\s*(-?\d+),\s*(-?\d+)> velocity=<\s*(-?\d+),\s*(-?\d+)>')


def parse_lines(lines):
    return [(int(x), int(y), int(dx), int(dy))
            for x, y, dx, dy in (PATTERN.match(line).group(1, 2, 3, 4) for line in lines)]


def compute_bounds(points):
    return (
        min(p[0] for p in points), max(p[0] for p in points),
        min(p[1] for p in points), max(p[1] for p in points)
    )


def got_bigger(b1, b2):
    return b2[0] < b1[0] or b2[1] > b1[1] or b2[2] < b1[2] or b2[3] > b1[3]


def step(points):
    return [(x + dx, y + dy, dx, dy) for x, y, dx, dy in points]


def print_points(bounds, points):
    min_x, max_x, min_y, max_y = bounds
    pts = set((x, y) for (x, y, _, _) in points)
    for y in range(min_y, max_y + 1):
        line = ''.join('#' if (x, y) in pts else '.' for x in range(min_x, max_x + 1))
        print(line)


def run(points):
    old_points = points
    old_bounds = compute_bounds(points)
    steps = 0
    while True:
        new_points = step(old_points)
        new_bounds = compute_bounds(new_points)
        if got_bigger(old_bounds, new_bounds):
            print_points(old_bounds, old_points)
            break
        else:
            steps += 1
            old_points = new_points
            old_bounds = new_bounds
    print("Done after %d steps" % steps)


TEST = [
    'position=< 9,  1> velocity=< 0,  2>',
    'position=< 7,  0> velocity=<-1,  0>',
    'position=< 3, -2> velocity=<-1,  1>',
    'position=< 6, 10> velocity=<-2, -1>',
    'position=< 2, -4> velocity=< 2,  2>',
    'position=<-6, 10> velocity=< 2, -2>',
    'position=< 1,  8> velocity=< 1, -1>',
    'position=< 1,  7> velocity=< 1,  0>',
    'position=<-3, 11> velocity=< 1, -2>',
    'position=< 7,  6> velocity=<-1, -1>',
    'position=<-2,  3> velocity=< 1,  0>',
    'position=<-4,  3> velocity=< 2,  0>',
    'position=<10, -3> velocity=<-1,  1>',
    'position=< 5, 11> velocity=< 1, -2>',
    'position=< 4,  7> velocity=< 0, -1>',
    'position=< 8, -2> velocity=< 0,  1>',
    'position=<15,  0> velocity=<-2,  0>',
    'position=< 1,  6> velocity=< 1,  0>',
    'position=< 8,  9> velocity=< 0, -1>',
    'position=< 3,  3> velocity=<-1,  1>',
    'position=< 0,  5> velocity=< 0, -1>',
    'position=<-2,  2> velocity=< 2,  0>',
    'position=< 5, -2> velocity=< 1,  2>',
    'position=< 1,  4> velocity=< 2,  1>',
    'position=<-2,  7> velocity=< 2, -2>',
    'position=< 3,  6> velocity=<-1, -1>',
    'position=< 5,  0> velocity=< 1,  0>',
    'position=<-6,  0> velocity=< 2,  0>',
    'position=< 5,  9> velocity=< 1, -2>',
    'position=<14,  7> velocity=<-2,  0>',
    'position=<-3,  6> velocity=< 2, -1>'
]


if __name__ == '__main__':
    # lines = TEST
    lines = read_lines()
    run(parse_lines(lines))
