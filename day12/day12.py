TEST = """initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #
""".splitlines()


def read_lines():
    with open('input.txt', 'r') as f:
        return [l.strip() for l in f.readlines()]


def parse_lines(lines):
    initial_state = lines[0][15:]
    rules = {}
    for line in lines[2:]:
        pattern, _, result = line.partition(' => ')
        rules[pattern] = result
    return initial_state, rules


def step(state, rules):
    result = '..'
    for idx in range(len(state) - 4):
        c = rules.get(state[idx:idx + 5], '.')
        result += c
    return result + '..'


def value(state, offset):
    first = state.find('#')
    result = 0
    for i in range(first, len(state)):
        if state[i] == '#':
            result += (i + offset)
    return result


def shift(state, offset):
    idx = state.find('#')
    if idx < 5:
        state = ('.' * 10) + state
        offset -= 10
    elif idx > 15:
        state = state[10:]
        offset += 10
    idx = state.rfind('#')
    if idx > (len(state) - 5):
        state = state + ('.' * 10)
    elif idx < (len(state) - 15):
        state = state[:-10]
    return state, offset


def run(state, rules, steps):
    offset = 0
    for i in range(steps):
        state, offset = shift(state, offset)
        state = step(state, rules)
    return value(state, offset)


if __name__ == '__main__':
    # lines = TEST
    lines = read_lines()
    state, rules = parse_lines(lines)
    result = run(state, rules, 20)
    print("Part1: sum = %d" % result)

    # somewhere below 1000 the values get regular and repeat ...
    offset = run(state, rules, 1000)
    delta = run(state, rules, 2000) - offset
    steps = 50000000000
    print("Part2: steps = %d, sum = %d" % (steps, (steps / 1000 - 1) * delta + offset))
