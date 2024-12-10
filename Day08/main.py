import unittest
from collections import defaultdict

def part_one(grid):
    rows, cols = len(grid), len(grid[0])

    antennas = defaultdict(list)

    res = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != ".":
                c = grid[i][j]
                antennas[c].append((i,j))
    
    for key, val in antennas.items():
        n = len(val)
        for i in range(n-1):
            for j in range(i+1, n):
                one, two = val[i], val[j]

                mx = two[0] - one[0]
                my = two[1] - one[1]

                x1 = one[0] - mx
                y1 = one[1] - my

                if 0 <= x1 < rows and 0 <= y1 < cols:
                    if grid[x1][y1] != "#":
                        grid[x1][y1] = "#"
                        res += 1

                x2 = two[0] + mx
                y2 = two[1] + my

                if 0 <= x2 < rows and 0 <= y2 < cols:
                    if grid[x2][y2] != "#":
                        grid[x2][y2] = "#"
                        res += 1
    return res

def part_two(grid):
    rows, cols = len(grid), len(grid[0])

    antennas = defaultdict(list)

    res = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != ".":
                c = grid[i][j]
                antennas[c].append((i,j))
    
    for key, val in antennas.items():
        n = len(val)
        for i in range(n-1):
            for j in range(i+1, n):
                one, two = val[i], val[j]

                mx = two[0] - one[0]
                my = two[1] - one[1]

                x1 = one[0] - mx
                y1 = one[1] - my

                while 0 <= x1 < rows and 0 <= y1 < cols:
                    if grid[x1][y1] != "#":
                        grid[x1][y1] = "#"
                    x1 -= mx
                    y1 -= my

                x2 = two[0] + mx
                y2 = two[1] + my

                while 0 <= x2 < rows and 0 <= y2 < cols:
                    if grid[x2][y2] != "#":
                        grid[x2][y2] = "#"
                    x2 += mx
                    y2 += my
    
    ans = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != '.':
                ans += 1

    return ans

class TestSuite(unittest.TestCase):
    def setUp(self) -> None:
        filename = "test.txt"
        file = open(filename)

        self.grid = []
        for line in file.read().splitlines():
            self.grid.append(list(line.strip()))
        
        file.close()

    def test_part_one(self):
        expected = 14
        self.assertEqual(part_one(self.grid), expected)

    def test_part_two(self):
        expected = 34
        self.assertEqual(part_two(self.grid), expected)

if __name__ == "__main__":
    unittest.main()