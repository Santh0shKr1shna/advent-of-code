import unittest
from functools import cache

def part_one(banks):
    res = 0

    for bank in banks:
        maxi = 0

        for i in range(len(bank) - 1):
            maxi = max(maxi, bank[i]*10 + max(bank[(i+1):]))
        
        res += maxi

    return res

def part_two(banks):
    res = 0
    
    for bank in banks:
        maxi = 0
        n = len(bank)

        @cache
        def get_max(i, d):
            if d <= 0 or i < 0: 
                return 0
            
            return max(get_max(i-1, d), get_max(i-1, d-1) * 10 + bank[i])
        
        maxi = get_max(n-1, 12)

        res += maxi
    
    return res


class TestSuite(unittest.TestCase):
    def setUp(self) -> None:
        file = open("test.txt")

        self.banks = []

        for line in file.readlines():
            self.banks.append(list(map(int, line.strip())))

    def test_part_one_solution(self):
        expected = 357
        self.assertEqual(part_one(self.banks), expected)

    def test_part_two_solution(self):
        expected = 3121910778619
        self.assertEqual(part_two(self.banks), expected)

if __name__ == "__main__":
    unittest.main()