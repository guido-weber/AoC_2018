import unittest
from collections import Counter


def read_lines():
    with open('input.txt', 'r') as f:
        return [l.strip() for l in f.readlines()]


def common_letters(s1, s2):
    return ''.join(c1 for (c1, c2) in zip(s1, s2) if c1 == c2)


def first_off_by_one_char(lines):
    for i in range(len(lines) - 1):
        for j in range(i + 1, len(lines)):
            cl = common_letters(lines[i], lines[j])
            if len(cl) == len(lines[i]) - 1:
                return cl


class TestCommonLetters(unittest.TestCase):
    def test_empty(self):
        self.assertEqual('', common_letters('', ''))

    def test_equal_strings(self):
        s = 'afafaefv gsdg'
        self.assertEqual(s, common_letters(s, s))

    def test_different_strings(self):
        self.assertEqual('asfg', common_letters('asdfg', 'asxfg'))
        self.assertEqual('sdfg', common_letters('asdfg', 'xsdfg'))
        self.assertEqual('asdf', common_letters('asdfg', 'asdfx'))
        self.assertEqual('asfg', common_letters('xasdfgx', 'yasyfgy'))


class TestFirstOffByOneChar(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(None, first_off_by_one_char([]))

    def test_none(self):
        lines = [
            'asdfg',
            'asdfg',
            'asdfg',
            'asdfg',
        ]
        self.assertEqual(None, first_off_by_one_char(lines))

    def test_one(self):
        lines = [
            'asdfg',
            'ysxfg',
            'asdfg',
            'asdxg',
        ]
        self.assertEqual('asdg', first_off_by_one_char(lines))


if __name__ == '__main__':
    result = first_off_by_one_char(read_lines())
    print(result)
