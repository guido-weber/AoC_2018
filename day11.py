def power_level(x, y, grid_sn):
    rack_id = x + 10
    result = rack_id * y + grid_sn
    result *= rack_id
    return (result % 1000 // 100) - 5


def create_grid(grid_sn):
    return [[power_level(x, y, grid_sn) for y in range(301)]
            for x in range(301)]


def best(grid_sn, sq):
    grid = create_grid(grid_sn)

    def compute():
        for x in range(1, 301 - sq):
            for y in range(1, 301 - sq):
                tp = sum(grid[xx][yy] for xx in range(x, x + sq) for yy in range(y, y + sq))
                yield (x, y, tp)
    return max(compute(), key=lambda tpl: tpl[2])


def all_best(grid_sn):
    def compute():
        grid = create_grid(grid_sn)
        for x in range(1, 301):
            for y in range(1, 301):
                yield (x, y, 1, grid[x][y])
        cur = create_grid(grid_sn)
        for sq in range(2, 301):
            for x in range(1, 301 - sq):
                for y in range(1, 301 - sq):
                    tp = (cur[x][y]
                          + sum(grid[xx][y + sq - 1] for xx in range(x, x + sq - 1))
                          + sum(grid[x + sq - 1][yy] for yy in range(y, y + sq - 1))
                          + grid[x + sq - 1][y + sq - 1])
                    cur[x][y] = tp
                    yield (x, y, sq, tp)
    return max(compute(), key=lambda tpl: tpl[3])


if __name__ == '__main__':
    assert power_level(122, 79, 57) == -5
    assert power_level(217, 196, 39) == 0
    assert power_level(101, 153, 71) == 4

    assert best(18, 3) == (33, 45, 29)
    assert best(42, 3) == (21, 61, 30)
    x, y, pwr = best(5235, 3)
    print("Part 1: %s at %d,%d" % (pwr, x, y))

    # assert all_best(18) == (90, 269, 16, 113)
    # assert all_best(42) == (232, 251, 12, 119)
    x, y, sq, pwr = all_best(5235)
    print("Part 2: %s at %d,%d,%d" % (pwr, x, y, sq))
