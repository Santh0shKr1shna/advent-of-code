import re
import unittest

def part_one(data):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

    matches = re.findall(pattern, data)

    res = 0
    for match in matches:
        res += (int(match[0]) * int(match[1]))

    return res

def part_two(data):
    pattern = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"

    matches = re.findall(pattern, data)

    res = 0
    activate = 1

    for match in matches:
        if match[0] == "do()":
            activate = 1
        elif match[0] == "don't()":
            activate = 0
        else:
            res += (int(match[1]) * int(match[2]) * activate)

    return res

class TestSuite(unittest.TestCase):
    def setUp(self) -> None:
        file = open("test.txt")
        self.data = "".join(file.readlines())
        file.close()

    def test_part_one(self):
        expected = 161
        self.assertEqual(part_one(self.data), expected)

    def test_part_two(self):
        expected = 48
        self.assertEqual(part_two(self.data), expected)


if __name__ == "__main__":
    unittest.main()