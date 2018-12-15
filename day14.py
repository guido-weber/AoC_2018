def step(receipes, elf1, elf2):
    elf1_score = receipes[elf1]
    elf2_score = receipes[elf2]
    receipes.extend((int(c) for c in "%d" % (elf1_score + elf2_score)))
    return (receipes,
            (elf1 + 1 + elf1_score) % len(receipes),
            (elf2 + 1 + elf2_score) % len(receipes))


def part1(after):
    receipes = [3, 7]
    elf1 = 0
    elf2 = 1
    while (len(receipes) < (after + 10)):
        receipes, elf1, elf2 = step(receipes, elf1, elf2)
    return ''.join(("%d" % r) for r in receipes[after:after + 10])


def part2(pattern):
    receipes = [3, 7]
    elf1 = 0
    elf2 = 1
    lp = len(pattern)
    while True:
        receipes, elf1, elf2 = step(receipes, elf1, elf2)
        last = ''.join(("%d" % r) for r in receipes[-lp - 1:])
        if last.startswith(pattern):
            return len(receipes) - lp - 1
        elif last.endswith(pattern):
            return len(receipes) - lp


if __name__ == '__main__':
    assert part1(9) == '5158916779'
    assert part1(5) == '0124515891'
    assert part1(18) == '9251071085'
    assert part1(2018) == '5941429882'
    print("Part 1: %s" % part1(920831))

    assert part2('51589') == 9
    assert part2('01245') == 5
    assert part2('92510') == 18
    assert part2('59414') == 2018
    print("Part 2: %d" % part2('920831'))
