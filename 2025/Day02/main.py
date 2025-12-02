import unittest

def part_one(id_ranges):
    res = 0

    for start, end in id_ranges:
        for id in range(start, end+1):
            id_str = str(id)
            l = len(id_str)

            if l % 2 == 0 and id_str[:l//2] == id_str[l//2:]:
                res += id

    return res

def part_two(id_ranges):
    res = 0
    for start, end in id_ranges:
        for id in range(start, end+1):
            id_str = str(id)
            l = len(id_str)

            for c in range(1, l//2 + 1):
                if l % c != 0:
                    continue
                if id_str[:c] * (l // c) == id_str:
                    res += id
                    break

    return res


class TestSuite(unittest.TestCase):
    def setUp(self) -> None:
        file = open("test.txt")

        id_ranges_unfilt = file.read().split(',')

        self.id_ranges = [] # (start, end)

        for id_range in id_ranges_unfilt:
            start, end = map(int, id_range.split('-'))
            self.id_ranges.append((start, end))

    def test_part_one_solution(self):
        expected = 1227775554
        self.assertEqual(part_one(self.id_ranges), expected)

    def test_part_two_solution(self):
        excepted = 4174379265
        self.assertEqual(part_two(self.id_ranges), excepted)

if __name__ == "__main__":
    unittest.main()