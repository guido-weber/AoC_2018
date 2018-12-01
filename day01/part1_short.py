with open('input.txt', 'r') as f:
    print("result: %d" % sum([int(l.strip()) for l in f.readlines() if l.strip()]))
