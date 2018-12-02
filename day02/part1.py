from collections import Counter


def read_lines():
    with open('input.txt', 'r') as f:
        return f.readlines()


def main(lines):
    have2 = 0
    have3 = 0
    for line in lines:
        c = Counter(line)
        have2 += (1 if any((count == 2) for count in c.values()) else 0)
        have3 += (1 if any((count == 3) for count in c.values()) else 0)
    print("2s: %d, 3s: %d, checksum: %d" % (have2, have3, have2 * have3))


if __name__ == '__main__':
    main(read_lines())
