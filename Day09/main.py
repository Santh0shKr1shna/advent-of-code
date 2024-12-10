import unittest

def part_one(disk):
    n = len(disk)
    l,r = 0, n-1

    while l < r:
        while disk[l] != '.' and l < n:
            l += 1
        while disk[r] == '.' and r > 0:
            r -= 1

        if l < r:
            disk[l] = disk[r]
            disk[r] = '.'
            l += 1
            r -= 1
    
    res = 0
    for i,ele in enumerate(disk):
        if ele != '.':
            res += (i * ele)

    return res

def part_two(disk, space, blocks):
    for (bpos, bsz, id) in reversed(blocks):
        for isp, (spos, ssz) in enumerate(space):
            if ssz >= bsz and spos < bpos:
                for i in range(bsz):
                    disk[spos + i] = id
                    disk[bpos + i] = '.'
                space[isp] = [spos+bsz, ssz-bsz]
                break

    res = 0
    for i,ele in enumerate(disk):
        if ele != '.':
            res += (i * ele)

    return res

class TestSuite(unittest.TestCase):
    def setUp(self) -> None:
        filename = "test.txt"
        file = open(filename)

        data = file.read().strip('\n').strip()
        file.close()

        self.disk = []
        self.space = [] # pos, size
        self.blocks = [] # pos, size, fileID

        pos = 0

        for i, e in enumerate(data):
            if i % 2 == 0:
                self.disk.extend([i//2] * int(e))
                self.blocks.append([pos, int(e), i//2])
            else:
                self.disk.extend(['.'] * int(e))
                self.space.append([pos, int(e)])

            pos += int(e)

    def test_part_one(self):
        expected = 1928
        self.assertEqual(part_one(self.disk), expected)

    def test_part_two(self):
        expected = 2858
        self.assertEqual(part_two(self.disk, self.space, self.blocks), expected)

if __name__ == "__main__":
    unittest.main()