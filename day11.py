from collections import Counter


def power_level(x, y, grid_sn):
    rack_id = x + 10
    result = rack_id * y + grid_sn
    result *= rack_id
    return (result % 1000 // 100) - 5


def create_grid(grid_sn):
    return {(x, y): power_level(x, y, grid_sn)
            for x in range(1, 301)
            for y in range(1, 301)}


def total_power(grid, x, y, sq):
    return sum(grid[(xx, yy)]
               for xx in range(x, x + sq)
               for yy in range(y, y + sq))


def best(grid, sq):
    c = Counter({(x, y): total_power(grid, x, y, sq)
                 for x in range(1, 301 - sq)
                 for y in range(1, 301 - sq)})
    return c.most_common(1)[0]


def all_best(grid):
    i = ((sq, best(grid, sq)) for sq in range(1, 301))
    c = Counter({(x, y, sq): pwr for (sq, ((x, y), pwr)) in i})
    return c.most_common(1)[0]


if __name__ == '__main__':
    assert power_level(122, 79, 57) == -5
    assert power_level(217, 196, 39) == 0
    assert power_level(101, 153, 71) == 4

    assert best(create_grid(18), 3) == ((33, 45), 29)
    assert best(create_grid(42), 3) == ((21, 61), 30)
    ((x, y), pwr) = best(create_grid(5235), 3)
    print("Part 1: %s at %d,%d" % (pwr, x, y))

    print(all_best(create_grid(18)))
    #assert best(create_grid(18), 3) == ((33, 45), 29)
    #assert best(create_grid(18), 3) == ((33, 45), 29)

"""
For grid serial number 18, the largest total square (with a total power of 113) is 16x16 and has a top-left corner of 90,269, so its identifier is 90,269,16.
For grid serial number 42, the largest total square (with a total power of 119) is 12x12 and has a top-left corner of 232,251, so its identifier is 232,251,12.
"""
