import unittest

def part_one(inputs):
    res = 0
    cur = 50
    
    for dir, num in inputs:
        if num == 0: continue

        if dir == 'R':
            cur = (cur + num) % 100

        else:
            cur = (cur - num) % 100

        if cur == 0:
            res += 1

    return res

def part_two(inputs):
    res = 0
    cur = 50
    
    for dir, num in inputs:
        if num == 0: continue

        if dir == 'R':
            res += (cur + num) // 100 - cur // 100
            cur += num

        else:
            cur -= 1
            res += cur // 100 - (cur - num) // 100
            cur += 1
            cur -= num

    return res


class TestSuite(unittest.TestCase):
    def setUp(self) -> None:
        file = open("test.txt")

        self.inputs = [] # list of (direction, magnitude)

        for line in file:
            line = line.strip()

            dir = line[0]
            num = int(line[1:])

            self.inputs.append((dir, num))

    def test_part_one_solution(self):
        expected = 3
        self.assertEqual(part_one(self.inputs), expected)

    def test_part_two_solution(self):
        expected = 6
        self.assertEqual(part_two(self.inputs), expected)

if __name__ == "__main__":
    unittest.main()