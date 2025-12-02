import unittest

def part_one(grid):
    rows, cols = len(grid), len(grid[0])

    xmas = "XMAS"

    res = 0

    dirs = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "X":
                for dr,dc in dirs:
                    pos = 1
                    dx,dy = i+dr, j+dc

                    while 0 <= dx < rows and 0 <= dy < cols and pos < 4 and grid[dx][dy] == xmas[pos]:
                        pos += 1
                        dx += dr
                        dy += dc
                        if pos == 4:
                            res += 1
                            break

    return res

def part_two(grid):
    rows, cols = len(grid), len(grid[0])

    res = 0

    for i in range(1, rows-1):
        for j in range(1, cols-1):
            if grid[i][j] == 'A':
                if (grid[i-1][j-1] == "M" and grid[i+1][j+1] == "S") or (grid[i-1][j-1] == "S" and grid[i+1][j+1] == "M"):
                    if (grid[i-1][j+1] == "M" and grid[i+1][j-1] == "S") or (grid[i-1][j+1] == "S" and grid[i+1][j-1] == "M"):
                        res += 1

    return res


class TestSuite(unittest.TestCase):
    def setUp(self) -> None:
        filename = "test.txt"
        file = open(filename)

        self.grid = []

        for line in file.readlines():
            self.grid.append(list(line.strip("\n").strip(" ")))

        file.close()

    def test_part_one(self):
        expected = 18
        self.assertEqual(part_one(self.grid), expected)

    def test_part_two(self):
        expected = 9
        self.assertEqual(part_two(self.grid), expected)


if __name__ == "__main__":
    unittest.main()