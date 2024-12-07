import unittest

def part_one(targets, queries):
    n = len(targets)

    def helper(target, arr, i, total):
        if i == len(arr):
            if total == target:
                return True
            return False
        if total > target: return False

        return helper(target, arr, i+1, total + arr[i]) or helper(target, arr, i+1, total * arr[i])

    res = 0
    for i in range(n):
        if helper(targets[i], queries[i], 1, queries[i][0]):
            res += targets[i]

    return res


def part_two(targets, queries):
    n = len(targets)

    def helper(target, arr, i, total):
        if i == len(arr):
            if total == target:
                return True
            return False
        if total > target: return False

        return helper(target, arr, i+1, total + arr[i]) or helper(target, arr, i+1, total * arr[i]) or helper(target, arr, i+1, int(str(total) + str(arr[i])))

    res = 0
    for i in range(n):
        if helper(targets[i], queries[i], 1, queries[i][0]):
            res += targets[i]

    return res


class TestSuite(unittest.TestCase):
    def setUp(self) -> None:
        filename = "test.txt"
        file = open(filename)
        self.targets = []
        self.queries = []

        for line in file.read().split('\n'):
            T,Q = line.split(':')
            self.targets.append(int(T.strip()))
            self.queries.append(list(map(int, Q.strip().split(' '))))

        file.close()

    def test_part_one(self):
        expected = 3749
        self.assertEqual(part_one(self.targets, self.queries), expected)

    def test_part_two(self):
        expected = 11387
        self.assertEqual(part_two(self.targets, self.queries), expected)


if __name__ == "__main__":
    unittest.main()