import re
from instructions import Instruction


def read_lines():
    with open('input.txt', 'r') as f:
        return [l.strip() for l in f.readlines()]


P_BEFORE = re.compile(r'Before:.*(\d+),\s*(\d+),\s*(\d+),\s*(\d+).*')
P_AFTER = re.compile(r'After:.*(\d+),\s*(\d+),\s*(\d+),\s*(\d+).*')


def extract_input(lines):
    lnum = 0
    samples = []
    while lines[lnum].startswith('Before'):
        before = [int(x) for x in P_BEFORE.match(lines[lnum]).group(1, 2, 3, 4)]
        instruction = [int(x) for x in lines[lnum + 1].split()]
        after = [int(x) for x in P_AFTER.match(lines[lnum + 2]).group(1, 2, 3, 4)]
        samples.append((before, instruction, after))
        assert lines[lnum + 3] == ''
        lnum += 4
    program = []
    while lines[lnum] == '':
        lnum += 1
    for line in lines[lnum:]:
        program.append([int(x) for x in line.split()])
    return samples, program


def possible_opcodes(sample):
    opcodes = set()
    for instruction in Instruction.ALL.values():
        i = instruction(*sample[1][1:])
        if i(sample[0]) == sample[2]:
            opcodes.add(instruction.__name__)
    return opcodes


def find_opcodes(samples):
    opcodes = {}
    for sample in samples:
        opcode_id = sample[1][0]
        opcode_names = possible_opcodes(sample)
        if opcode_id in opcodes:
            opcodes[opcode_id] &= opcode_names
        else:
            opcodes[opcode_id] = opcode_names
    work_done = True
    while work_done:
        definite = {k: v for k, v in opcodes.items() if len(v) == 1}
        definite_names = set().union(*definite.values())
        work_done = False
        for k, v in opcodes.items():
            if k not in definite:
                old = len(v)
                v -= definite_names
                if len(v) < old:
                    work_done = True
    assert len(definite) == len(Instruction.ALL)
    return {k: v.pop() for k, v in opcodes.items()}


if __name__ == '__main__':
    lines = read_lines()
    samples, program = extract_input(lines)

    part1 = 0
    for sample in samples:
        cnt = len(possible_opcodes(sample))
        if cnt >= 3:
            part1 += 1
    print("Part1: %s" % part1)

    opcodes = find_opcodes(samples)
    registers = [0, 0, 0, 0]
    for opcode, a, b, c in program:
        i = Instruction.ALL[opcodes[opcode]](a, b, c)
        registers = i(registers)
    print("Part2: register content is %s" % registers)
