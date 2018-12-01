def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    data = [int(l.strip()) for l in lines if l.strip()]
    current = 0
    seen = set()
    idx = 0
    while current not in seen:
        seen.add(current)
        current += data[idx % len(data)]
        idx += 1

    print("saw %d twice after %d steps" % (current, idx))


if __name__ == '__main__':
    main()
