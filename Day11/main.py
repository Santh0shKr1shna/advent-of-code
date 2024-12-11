import unittest
from collections import Counter
import functools

@functools.cache
def count_stones(stone, steps):
    if steps == 0: return 1
    if len(str(stone)) % 2 == 0:
        c = str(stone)
        k = len(c) // 2
        return count_stones(int(c[:k]), steps-1) + count_stones(int(c[k:]), steps-1)
        
    if stone: return count_stones(stone*2024, steps-1)

    return count_stones(1, steps-1)


def blink(stones, steps):
    ans = 0
    for stone in stones:
        ans += count_stones(stone, steps)

    return ans

class TestSuite(unittest.TestCase):
    def setUp(self) -> None:
        self.stones = [125, 17]

    def test_part_one(self):
        expected = 55312
        self.assertEqual(blink(self.stones, 25), expected)

    def test_part_two(self):
        expected = 65601038650482
        self.assertEqual(blink(self.stones, 75), expected)


if __name__ == "__main__":
    unittest.main()