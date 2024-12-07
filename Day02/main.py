import unittest

def is_safe(report):
    diff = 0
    safe = True
    prev = report[0]

    for i in range(1, len(report)):
        cur = report[i] - prev
        if cur == 0 or abs(cur) > 3:
            safe = False
            break

        if diff < 0 and cur > 0 or diff > 0 and cur < 0:
            safe = False
            break

        prev = report[i]

        if diff == 0: 
            diff = -1 if cur < 0 else 1
    
    return safe

def part_one(reports):
    res = 0
    for report in reports:
        if is_safe(report):
            res += 1
    return res

def part_two(reports):
    res = 0
    for report in reports:
        if is_safe(report):
            res += 1
        else:
            for i in range(len(report)):
                temp = report[:i] + report[i+1:]
                if is_safe(temp):
                    res += 1
                    break

    return res

class TestSuite(unittest.TestCase):
    def setUp(self) -> None:
        filename = "test.txt"
        file = open(filename)

        self.reports = []

        for line in file.readlines():
            self.reports.append(list(map(int, line.strip().split(' '))))

    def test_part_one_happy_path_true(self):
        expected = 2
        self.assertEqual(part_one(self.reports), expected)
    def test_part_two_happy_path_true(self):
        expected = 4
        self.assertEqual(part_two(self.reports), expected)

if __name__ == "__main__":
    unittest.main()