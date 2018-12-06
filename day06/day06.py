from collections import deque, Counter


def read_lines():
    with open('input.txt', 'r') as f:
        return f.readlines()


class Main(object):
    def __init__(self, lines):
        coords = [(int(x), int(y)) for x, y in (line.split(',') for line in lines)]
        self.min_x = min(c[0] for c in coords) - 1
        self.max_x = max(c[0] for c in coords) + 1
        self.min_y = min(c[1] for c in coords) - 1
        self.max_y = max(c[1] for c in coords) + 1
        self.queue = deque((c, (idx, 0)) for idx, c in enumerate(coords))
        self.grid = {}
        self.infinite_areas = set()

    def is_inside(self, x, y):
        return (x >= self.min_x and x <= self.max_x and y >= self.min_y and y <= self.max_y)

    def expand(self, x, y, area, distance):
        for (nx, ny) in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
            if self.is_inside(nx, ny):
                self.queue.append(((nx, ny), (area, distance)))
            else:
                self.infinite_areas.add(area)

    def fill_grid(self):
        while len(self.queue) > 0:
            ((x, y), (area, distance)) = self.queue.popleft()
            g = self.grid.get((x, y))
            if g is None:
                self.grid[(x, y)] = (area, distance)
                self.expand(x, y, area, distance + 1)
            else:
                (g_area, g_distance) = g
                if distance < g_distance:
                    self.grid[(x, y)] = (area, distance)
                    self.expand(x, y, area, distance + 1)
                elif distance == g_distance and g_area not in ('.', area):
                    self.grid[(x, y)] = ('.', distance)
                    self.expand(x, y, '.', distance + 1)

    def biggest_finite_area(self):
        count = Counter(a for a, _ in self.grid.values()
                        if a != -1 and a not in self.infinite_areas)
        [(area, size)] = count.most_common(1)
        return (area, size)

    def print(self):
        for y in range(self.min_y, self.max_y + 1):
            line = ''
            for x in range(self.min_x, self.max_x + 1):
                line += ('%3s' % self.grid[(x, y)][0])
            print(line)


TEST = [
    '1, 1',
    '1, 6',
    '8, 3',
    '3, 4',
    '5, 5',
    '8, 9'
]

if __name__ == '__main__':
    main = Main(read_lines())
    # main = Main(TEST)
    main.fill_grid()
    (area, size) = main.biggest_finite_area()
    # main.print()
    print("Area %s has size %d" % (area, size))
