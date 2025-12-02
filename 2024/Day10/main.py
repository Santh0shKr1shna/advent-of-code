import unittest

def solution(grid, part_one = True):
    rows, cols = len(grid), len(grid[0])
    heads = []

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                heads.append((i,j))

    def dfs(i, j, vis, cur):
        if part_one:
            if (i,j) in vis: return 0
            vis.add((i,j))

        if grid[i][j] == 9: return 1
        
        dirs = [(0,-1), (-1,0), (1,0), (0,1)]
        ans = 0

        for dr,dc in dirs:
            nx,ny = i+dr, j+dc
            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == cur + 1:
                    ans += dfs(nx, ny, vis, cur+1)
    
        return ans
    
    res = 0
    for (i,j) in heads:
        vis = set()
        res += dfs(i,j,vis,0)

    return res

class TestSuite(unittest.TestCase):
    def setUp(self) -> None:
        filename = "test.txt"
        file = open(filename)

        self.grid = []

        for line in file.read().splitlines():
            self.grid.append(list(map(int, line.strip())))

        file.close()

    def test_part_one(self):
        expected = 36
        self.assertEqual(solution(self.grid, True), expected)

    def test_part_two(self):
        expected = 81
        self.assertEqual(solution(self.grid, False), expected)

if __name__ == "__main__":
    unittest.main()