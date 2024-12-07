import unittest
from collections import deque

def part_one(grid):
    rows,cols = len(grid), len(grid[0])
    q = deque()
    res = set()

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "^":
                q.append((i,j))
                break

    dirs = [(-1,0), (0,1), (1,0), (0,-1)]
    dir = 0

    while q:
        x,y = q.popleft()
        res.add((x,y))

        dr,dc = dirs[dir]
        nx,ny = x+dr, y+dc

        if nx < 0 or nx == rows or ny < 0 or ny == cols:
            break

        if grid[nx][ny] == "#":
            q.append((x,y))
            dir = (dir+1) % 4
        else:
            q.append((nx,ny))

    return len(res)


def part_two(grid):
    rows,cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "^":
                sr,sc = i,j
                break

    dirs = [(-1,0), (0,1), (1,0), (0,-1)]

    res = 0

    for i in range(rows):
        for j in range(cols):
            x,y = sr,sc
            dir = 0
            vis= set()

            while True:
                if (x,y,dir) in vis:
                    res += 1
                    break
                vis.add((x,y,dir))

                dr,dc = dirs[dir]

                nx,ny = x+dr, y+dc

                if nx < 0 or nx == rows or ny < 0 or ny == cols:
                    break

                if grid[nx][ny] == "#" or (nx == i and ny == j):
                    dir = (dir+1) % 4
                else:
                    x,y = nx,ny

    return res


class TestSuite(unittest.TestCase):
    def setUp(self) -> None:
        filename = "test.txt"
        file = open(filename)

        self.grid = []

        for line in file.readlines():
            self.grid.append(list(line.strip('\n').strip()))

        file.close()

    def test_part_one(self):
        expected = 41
        self.assertEqual(part_one(self.grid), expected)

    def test_part_two(self):
        expected = 6
        self.assertEqual(part_two(self.grid), expected)


if __name__ == "__main__":
    unittest.main()