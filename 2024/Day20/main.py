import unittest

def get_starting_and_ending_pos(grid):
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == "S":
                si, sj = i, j
            if grid[i][j] == "E":
                ei, ej = i, j
    
    return (si, sj, ei, ej)

def get_og_path(grid):
    n = len(grid)

    dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    si, sj, ei, ej = get_starting_and_ending_pos(grid)

    path = [(si, sj)]

    while path[-1] != (ei, ej):
        curx, cury = path[-1]

        for dr,dc in dirs:
            nx ,ny = curx + dr, cury + dc
            if 0 <= nx < n and 0 <= ny < n:
                if len(path) > 1 and (nx, ny) == path[-2]:
                    continue
                if grid[nx][ny] == "#":
                    continue
                path.append((nx, ny))
                break
    
    return path

def count_cheats(grid, cheat_time, saved_time = 100):
    n = len(grid)
    
    path = get_og_path(grid)
    total = len(path) - 1

    time_to_reach = {}
    for t, coord in enumerate(path):
        time_to_reach[coord] = total - t
    
    ans = {}
    for t, coord in enumerate(path):
        i,j = coord
        for ni in range(i - cheat_time, i + cheat_time + 1):
            for nj in range(j - cheat_time, j + cheat_time + 1):
                time_used = abs(ni - i) + abs(nj - j)
                if 0 <= ni < n and 0 <= nj < n:
                    if time_used <= cheat_time and grid[ni][nj] != "#":
                        remaining = time_to_reach[(ni, nj)]
                        ans[(i, j, ni, nj)] = total - (t + remaining + time_used)

    res = 0
    for v in ans.values():
        if v >= saved_time:
            res += 1

    return res

class TestSuite(unittest.TestCase):
    def setUp(self) -> None:
        filename = "test.txt"
        file = open(filename)

        self.grid = []
        for line in file.read().splitlines():
            self.grid.append(list(line.strip()))
        
        file.close()

    def test_part_one(self):
        expected = 1

        cheat_time = 2
        saved_time = 50

        self.assertEqual(expected, count_cheats(self.grid, cheat_time, saved_time))

    def test_part_two(self):
        expected = 285

        cheat_time = 20
        saved_time = 50

        self.assertEqual(expected, count_cheats(self.grid, cheat_time, saved_time))

if __name__ == "__main__":
    unittest.main()