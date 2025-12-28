import unittest

def rotate(pattern):
    height = len(pattern)
    width = len(pattern[0])
    return tuple(
        ''.join(pattern[height - 1 - i][j] for i in range(height))
        for j in range(width)
    )

def flip(pattern):
    return tuple(row[::-1] for row in pattern)

def part_one(data):
    res = 0

    patterns = [tuple(p.splitlines()[1:]) for p in data[:-1]]
    grid = []

    for line in data[-1].splitlines():
        dimensions_part, _, counts_part = line.partition(': ')
        width_height = tuple(map(int, dimensions_part.split('x')))
        counts = tuple(map(int, counts_part.split()))
        grid.append((width_height, counts))

    pattern_symmetries = []
    for p in patterns:
        symmetries = {p}
        for _ in range(2):
            for _ in range(4):
                p = rotate(p)
                symmetries.add(p)
            p = flip(p)
        pattern_symmetries.append(symmetries)

    pattern_counts = []
    for p in patterns:
        count = 0
        for row in p:
            count += row.count('#')
        pattern_counts.append(count)

    for ((height, width), required_counts) in grid:
        total_chars = 0
        for count, density in zip(required_counts, pattern_counts):
            total_chars += count * density
        
        if total_chars > height * width:
            continue
            
        if sum(required_counts) <= (height // 3) * (width // 3):
            res += 1
            
    print(f"Total valid arrangements: {res}")

    return res

def part_two():
    return "Merry Christmas"

class TestSuite(unittest.TestCase):
    def setUp(self) -> None:
        file = open("test.txt")
        file_data = file.read().splitlines()

        self.data = '\n'.join(file_data).split('\n\n')

        file.close()

    def test_part_one_solution(self):
        expected = 2
        self.assertEqual(part_one(self.data), expected)

    def test_part_two_solution(self):
        self.assertEqual(part_two(), "Merry Christmas")

if __name__ == "__main__":
    unittest.main()