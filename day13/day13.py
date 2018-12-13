from enum import Enum


TEST = r"""/->-\
|   |  /----\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/   """.splitlines()


TEST2 = r"""/>-<\
|   |
| /<+-\
| | | v
\>+</ |
  |   ^
  \<->/""".splitlines()


Direction = Enum('Direction', [('UP', '^'), ('DOWN', 'v'), ('LEFT', '<'), ('RIGHT', '>')])


RULES = {
    'UP': {
        'move': (0, -1),
        'direction': {
            '/': Direction.RIGHT,
            '\\': Direction.LEFT
        },
        'intersection': (Direction.LEFT, Direction.UP, Direction.RIGHT)
    },
    'DOWN': {
        'move': (0, 1),
        'direction': {
            '/': Direction.LEFT,
            '\\': Direction.RIGHT
        },
        'intersection': (Direction.RIGHT, Direction.DOWN, Direction.LEFT)
    },
    'LEFT': {
        'move': (-1, 0),
        'direction': {
            '/': Direction.DOWN,
            '\\': Direction.UP
        },
        'intersection': (Direction.DOWN, Direction.LEFT, Direction.UP)
    },
    'RIGHT': {
        'move': (1, 0),
        'direction': {
            '/': Direction.UP,
            '\\': Direction.DOWN
        },
        'intersection': (Direction.UP, Direction.RIGHT, Direction.DOWN)
    }
}


class Cart(object):
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.intersections = 0

    def move(self, tracks):
        rule = RULES[self.direction.name]
        self.x += rule['move'][0]
        self.y += rule['move'][1]
        t = tracks[self.y][self.x]
        if t == '+':
            self.direction = rule['intersection'][self.intersections]
            self.intersections = (self.intersections + 1) % 3
        elif t in rule['direction']:
            self.direction = rule['direction'][t]


def read_lines():
    with open('input.txt', 'r') as f:
        return [l.rstrip() for l in f.readlines()]


def extract_carts(lines):
    tracks = []
    carts = []
    dirmap = {d.value: d for d in Direction}
    for y, line in enumerate(lines):
        new_line = ''
        for x, c in enumerate(line):
            if c in dirmap:
                carts.append(Cart(x, y, dirmap[c]))
                if c in (Direction.UP.value, Direction.DOWN.value):
                    new_line += '|'
                else:
                    new_line += '-'
            else:
                new_line += c
        tracks.append(new_line)
    return tracks, carts


def tick(tracks, carts):
    d = {(cart.y, cart.x): cart for cart in carts}
    coords = sorted(d.keys())
    for (y, x) in coords:
        cart = d.pop((y, x))
        cart.move(tracks)
        if (cart.y, cart.x) in d:
            return True, (cart.y, cart.x)
        d[(cart.y, cart.x)] = cart
    return False, None


def tick2(tracks, carts):
    d = {(cart.y, cart.x): cart for cart in carts}
    coords = sorted(d.keys())
    for (y, x) in coords:
        cart = d.pop((y, x), None)
        if cart is None:
            continue
        cart.move(tracks)
        if (cart.y, cart.x) in d:
            d.pop((cart.y, cart.x))
        else:
            d[(cart.y, cart.x)] = cart
    return list(d.values())


if __name__ == '__main__':
    # lines = TEST
    lines = read_lines()
    tracks, carts = extract_carts(lines)
    crashed = False
    while not crashed:
        crashed, coords = tick(tracks, carts)
    (y, x) = coords
    print("Part1: crashed at %d,%d" % (x, y))

    # lines = TEST2
    lines = read_lines()
    tracks, carts = extract_carts(lines)
    while len(carts) > 1:
        carts = tick2(tracks, carts)
    print("Part2: last cart at %d,%d" % (carts[0].x, carts[0].y))
