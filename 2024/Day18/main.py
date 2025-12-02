import unittest
from heapq import heappop, heappush

def part_one(bytes, n):
    grid = [["." for _ in range(n)] for _ in range(n)]

    for b in bytes:
        x,y = b
        grid[y][x] = "#"

    dirs = [(0,-1), (-1,0), (0,1), (1,0)]

    pq = [(0,0,0)]
    vis = set()

    while pq:
        cost, x, y = heappop(pq)

        if (x,y) == (n-1,n-1):
            return cost

        vis.add((x,y))

        for dr,dc in dirs:
            nx,ny = x+dr, y+dc
            if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != "#" and (nx,ny) not in vis:
                heappush(pq, (cost+1, nx,ny))

    return -1

class TestSuite(unittest.TestCase):
    def setUp(self) -> None:
        filename = "test.txt"
        file = open(filename)

        self.bytes = []
        self.n = 7

        for line in file.read().splitlines():
            i,j = list(map(int, line.strip().split(',')))
            self.bytes.append((i,j))

        file.close()

    def test_part_one(self):
        expected = 22
        self.assertEqual(part_one(self.bytes, self.n), expected)


if __name__ == "__main__":
    unittest.main()