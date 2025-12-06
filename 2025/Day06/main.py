import unittest
import time

def mul(l):
    res = 1
    for i in l: res *= i
    return res


def part_one(inputs):
    res = 0

    rows, cols = len(inputs), len(inputs[0])
    
    for j in range(cols):
        col_res = None
        op = inputs[-1][j]
        for i in range(rows-1):
            if col_res:
                if op == "+":
                    col_res += int(inputs[i][j])
                else:
                    col_res *= int(inputs[i][j])
            else:
                col_res = int(inputs[i][j])

        res += col_res

    return res

def part_two(inputs: list):
    res = 0

    rows, cols = len(inputs), len(inputs[0])
    
    run = []
    for j in range(cols-1, -1, -1):
        t = ""
        for i in range(rows):
            c = inputs[i][j]
            if i == rows-1 and c in "+*":
                if c == "+":
                    res += sum(run)
                else:
                    res += mul(run)
                run.clear()

            t += c if c != " " else ""

            if i == rows-2:
                if not t: continue
                run.append(int(t))

    return res

class TestSuite(unittest.TestCase):
    def setUp(self) -> None:
        file = open("test.txt")

        self.inputs = []
        self.inputs_1 = []
        
        for line in file.readlines():
            self.inputs_1.append(line.split())
            self.inputs.append(line.strip('\n'))

    def test_part_one_solution(self):
        expected = 4277556
        self.assertEqual(part_one(self.inputs_1), expected)

    def test_part_two_solution(self):
        expected = 3263827
        self.assertEqual(part_two(self.inputs), expected)

if __name__ == "__main__":
    unittest.main()