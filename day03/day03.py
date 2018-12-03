import re
from collections import Counter


def read_lines():
    with open('input.txt', 'r') as f:
        return [l.strip() for l in f.readlines()]


CLAIM_PATTERN = re.compile(r'(?P<id>#\d+)\s*@\s*(?P<x>\d+),(?P<y>\d+):\s*(?P<w>\d+)x(?P<h>\d+)')


class Claim(object):
    def __init__(self, id, x, y, w, h):
        self.id = id
        self.x = int(x)
        self.y = int(y)
        self.w = int(w)
        self.h = int(h)

    @property
    def coords(self):
        for x in range(self.x, self.x + self.w):
            for y in range(self.y, self.y + self.h):
                yield (x, y)


def parse_line(line):
    match = CLAIM_PATTERN.match(line)
    if match is not None:
        return Claim(**match.groupdict())


def main(lines):
    claims = [parse_line(line) for line in lines]
    counter = Counter((x, y) for claim in claims for (x, y) in claim.coords)

    collision_count = sum(1 for count in counter.values() if count > 1)
    print("#collisions = %d" % collision_count)

    intact_claims = [claim.id for claim in claims
                     if max(counter[(x, y)] for (x, y) in claim.coords) == 1]
    print("No collisions for %s" % (', '.join(intact_claims)))


if __name__ == '__main__':
    main(read_lines())
