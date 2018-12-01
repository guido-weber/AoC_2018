def main():
    with open('input.txt', 'r') as f:
        lines = f.readlines()
    result = sum([int(l.strip()) for l in lines if l.strip()])
    print("result: %d" % result)


if __name__ == '__main__':
    main()
