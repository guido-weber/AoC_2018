from string import ascii_lowercase


def collapse(data):
    result = []
    for c in data:
        if len(result) == 0:
            result = [c]
        else:
            last = result[-1]
            if c.islower() != last.islower() and c.lower() == last.lower():
                result.pop()
            else:
                result.append(c)
    return result


def main(data):
    print("Part 1: remaining units %d" % len(collapse(data)))
    print("Part 2: shortest %d by removing %s" %
          min((len(collapse(c for c in data if c.lower() != u)), u) for u in ascii_lowercase))


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        data = f.read().strip()
    main(data)
