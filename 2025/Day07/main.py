import unittest
import time

def mul(l):
    res = 1
    for i in l: res *= i
    return res


def part_one(grid):
    res = 0
    rows, cols = len(grid), len(grid[0])

    beams = set()

    for i,ch in enumerate(grid[0]):
        if ch == 'S':
            beams.add(i)
            break

    for r in range(1, rows):
        new_beams = []
        removed_beams = []

        for beam in beams:
            ch = grid[r][beam]
            if ch == '^':
                res += 1
                if beam-1 >= 0:
                    new_beams.append(beam-1)
                if beam+1 < cols:
                    new_beams.append(beam+1)

                removed_beams.append(beam)

        for nbeam in new_beams:
            beams.add(nbeam)
        for rbeam in removed_beams:
            beams.remove(rbeam)

    return res

def part_two(grid):
    res = 0
    dp = {}
    rows, cols = len(grid), len(grid[0])

    def dfs(x,y):
        total = 0

        if x == rows:
            return 1
        
        if grid[x][y] == '^':
            if (x,y) in dp:
                return dp[(x,y)]
            if y > 0: 
                total += dfs(x,y-1)
            if y != cols-1: 
                total += dfs(x,y+1)
            
            dp[(x,y)] = total
            return total

        return dfs(x+1,y)

    for i,ch in enumerate(grid[0]):
        if ch == 'S':
            res = dfs(0,i)
            break

    return res

class TestSuite(unittest.TestCase):
    def setUp(self) -> None:
        file = open("test.txt")

        self.grid = []

        for line in file.readlines():
            self.grid.append(line.strip())

    def test_part_one_solution(self):
        expected = 21
        self.assertEqual(part_one(self.grid), expected)

    def test_part_two_solution(self):
        expected = 40
        self.assertEqual(part_two(self.grid), expected)

if __name__ == "__main__":
    unittest.main()