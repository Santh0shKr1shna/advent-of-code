import unittest
import time

def part_one(grid):
    res = 0
    row, col = len(grid), len(grid[0])

    for i in range(row):
        for j in range(col):
            count = 0
            if grid[i][j] != '@': continue
            
            if i > 0:
                if grid[i-1][j] == '@': count += 1
                if j > 0 and grid[i-1][j-1] == '@': count += 1
                if j != col -1 and grid[i-1][j+1] == '@': count += 1
            
            if i != row-1:
                if grid[i+1][j] == '@': count += 1
                if j > 0 and grid[i+1][j-1] == '@': count += 1
                if j != col -1 and grid[i+1][j+1] == '@': count += 1
            
            if j > 0 and grid[i][j-1] == '@': count += 1
            if j != col -1 and grid[i][j+1] == '@': count += 1
        
            if count > 3: continue
            res += 1

    return res

def part_two(grid):
    res = 0
    row, col = len(grid), len(grid[0])

    flag = True
    while flag:
        flag = False

        for i in range(row):
            for j in range(col):
                count = 0
                if grid[i][j] != '@': continue
                
                if i > 0:
                    if grid[i-1][j] == '@': count += 1
                    if j > 0 and grid[i-1][j-1] == '@': count += 1
                    if j != col -1 and grid[i-1][j+1] == '@': count += 1
                
                if i != row-1:
                    if grid[i+1][j] == '@': count += 1
                    if j > 0 and grid[i+1][j-1] == '@': count += 1
                    if j != col -1 and grid[i+1][j+1] == '@': count += 1
                
                if j > 0 and grid[i][j-1] == '@': count += 1
                if j != col -1 and grid[i][j+1] == '@': count += 1
            
                if count > 3: continue
                else:
                    flag = True
                    res += 1
                    grid[i][j] = 'x'

    return res

class TestSuite(unittest.TestCase):
    def setUp(self) -> None:
        file = open("test.txt")

        self.grid = []

        for line in file.readlines():
            self.grid.append(list(line.strip()))

    def test_part_one_solution(self):
        expected = 13
        self.assertEqual(part_one(self.grid), expected)

    def test_part_two_solution(self):
        expected = 43
        self.assertEqual(part_two(self.grid), expected)

if __name__ == "__main__":
    unittest.main()