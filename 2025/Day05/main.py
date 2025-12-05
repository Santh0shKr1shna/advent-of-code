import unittest
import time

def part_one(id_ranges, input_ids):
    res = 0

    for id in input_ids:
        for start, end in id_ranges:
            if id >= start and id <= end:
                res += 1
                break
    
    return res

def part_two(id_ranges: list):
    res = 0
    
    id_ranges.sort(key = lambda x : x[0])

    merged = [id_ranges[0]]

    for start, end in id_ranges[1:]:
        prev_start, prev_end = merged[-1]
        if start <= prev_end:
            merged[-1] = (prev_start, max(prev_end, end))
        else:
            merged.append((start, end))

    for start,end in merged:
        res += (end - start + 1)

    return res

class TestSuite(unittest.TestCase):
    def setUp(self) -> None:
        file = open("test.txt")

        id_ranges_str, self.input_ids = file.read().split('\n\n')
        
        self.id_ranges = []
        for line in id_ranges_str.split('\n'):
            self.id_ranges.append(list(map(int, line.strip().split('-'))))

        self.input_ids = list(map(int, self.input_ids.split('\n')))

    def test_part_one_solution(self):
        expected = 3
        self.assertEqual(part_one(self.id_ranges, self.input_ids), expected)

    def test_part_two_solution(self):
        expected = 14
        self.assertEqual(part_two(self.id_ranges), expected)

if __name__ == "__main__":
    unittest.main()