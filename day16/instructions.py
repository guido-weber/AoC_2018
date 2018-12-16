class Instruction(object):
    ALL = {}

    @classmethod
    def make_instruction(cls, name, base, mode_a, mode_b):
        assert name not in cls.ALL
        cls.ALL[name] = type(name, (base,), dict(mode_a=mode_a, mode_b=mode_b))

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __call__(self, registers):
        op_a = registers[self.a] if self.mode_a == 'register' else self.a
        op_b = registers[self.b] if self.mode_b == 'register' else self.b
        result = registers[:]
        result[self.c] = self.execute(op_a, op_b)
        return result


class Addition(Instruction):
    """
    addr (add register) stores into register C the result of adding register A and register B.
    addi (add immediate) stores into register C the result of adding register A and value B.
    """
    def execute(self, op_a, op_b):
        return op_a + op_b


Instruction.make_instruction('addr', Addition, 'register', 'register')
Instruction.make_instruction('addi', Addition, 'register', 'immediate')


class Multiplication(Instruction):
    """
    mulr (multiply register) stores into register C the result of multiplying register A and register B.
    muli (multiply immediate) stores into register C the result of multiplying register A and value B.
    """
    def execute(self, op_a, op_b):
        return op_a * op_b


Instruction.make_instruction('mulr', Multiplication, 'register', 'register')
Instruction.make_instruction('muli', Multiplication, 'register', 'immediate')


class BitwiseAND(Instruction):
    """
    banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
    bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
    """
    def execute(self, op_a, op_b):
        return op_a & op_b


Instruction.make_instruction('banr', BitwiseAND, 'register', 'register')
Instruction.make_instruction('bani', BitwiseAND, 'register', 'immediate')


class BitwiseOR(Instruction):
    """
    borr (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
    bori (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.
    """
    def execute(self, op_a, op_b):
        return op_a | op_b


Instruction.make_instruction('borr', BitwiseOR, 'register', 'register')
Instruction.make_instruction('bori', BitwiseOR, 'register', 'immediate')


class Assignment(Instruction):
    """
    setr (set register) copies the contents of register A into register C. (Input B is ignored.)
    seti (set immediate) stores value A into register C. (Input B is ignored.)
    """
    def execute(self, op_a, op_b):
        return op_a


Instruction.make_instruction('setr', Assignment, 'register', 'immediate')
Instruction.make_instruction('seti', Assignment, 'immediate', 'immediate')


class GreaterThanTesting(Instruction):
    """
    gtir (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.
    gtri (greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.
    gtrr (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.
    """
    def execute(self, op_a, op_b):
        return 1 if op_a > op_b else 0


Instruction.make_instruction('gtir', GreaterThanTesting, 'immediate', 'register')
Instruction.make_instruction('gtri', GreaterThanTesting, 'register', 'immediate')
Instruction.make_instruction('gtrr', GreaterThanTesting, 'register', 'register')


class EqualityTesting(Instruction):
    """
    eqir (equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.
    eqri (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.
    eqrr (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.
    """
    def execute(self, op_a, op_b):
        return 1 if op_a == op_b else 0


Instruction.make_instruction('eqir', EqualityTesting, 'immediate', 'register')
Instruction.make_instruction('eqri', EqualityTesting, 'register', 'immediate')
Instruction.make_instruction('eqrr', EqualityTesting, 'register', 'register')
