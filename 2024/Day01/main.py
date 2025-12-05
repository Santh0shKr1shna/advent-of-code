import unittest

def part_one(left, right):
    left.sort()
    right.sort()

    res = 0

    for i in range(len(left)):
        res += abs(left[i] - right[i])

    return res

def part_two(left, right):
    left_dict, right_dict = {}, {}
    for i in range(len(left)):
        if left[i] in left_dict: left_dict[left[i]] += 1
        else: left_dict[left[i]] = 1

        if right[i] in right_dict: right_dict[right[i]] += 1
        else: right_dict[right[i]] = 1

    res = 0

    for key, val in left_dict.items():
        if key in right_dict:
            res += key * right_dict[key] * val

    return res



class TestSuite(unittest.TestCase):
    def setUp(self) -> None:
        file = open("test.txt")

        self.left, self.right = [], []

        for line in file:
            l,r = list(map(int, line.split("   ")))

            self.left.append(l)
            self.right.append(r)

    def test_part_one_solution(self):
        expected = 11
        self.assertEqual(part_one(self.left, self.right), expected)

    def test_part_two_solution(self):
        expected = 31
        self.assertEqual(part_two(self.left, self.right), expected)

if __name__ == "__main__":
    unittest.main()