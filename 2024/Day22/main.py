import unittest
from collections import defaultdict

def mix(num, secret):
    return num ^ secret

def prune(num):
    return num % 16777216

def gen_secrets(secret):
    res = secret * 64
    secret = prune(mix(res, secret))

    res = secret // 32
    secret = prune(mix(res, secret))

    res = secret * 2048
    secret = prune(mix(res, secret))

    return secret

def part_one(secrets: list):
    ans = 0

    for secret in secrets:
        for _ in range(2000):
            secret = gen_secrets(secret)
        ans += secret

    return ans

def part_two(secrets: list):

    accumulated = defaultdict(int)
    for secret in secrets:
        prices = []
        for _ in range(2000):
            secret = gen_secrets(secret)
            prices.append(secret % 10)
        
        changes = [prices[i+1] - prices[i] for i in range(len(prices)-1)]
        
        scores = {}
        for i in range(len(changes) - 3):
            pattern = (changes[i], changes[i+1], changes[i+2], changes[i+3])
            if pattern not in scores:
                scores[pattern] = prices[i+4]
        
        for k,v in scores.items():
            accumulated[k] += v

    max_score = max(accumulated.values())
    best_pattern = max(accumulated, key=accumulated.get)

    print(max_score, best_pattern)

    return max_score

class TestSuite(unittest.TestCase):
    def setUp(self) -> None:
        filename = "test.txt"
        file = open(filename)

        self.secrets = []
        for line in file.read().splitlines():
            self.secrets.append(int(line.strip()))
        file.close()

    def test_part_one(self):
        expected = 37327623
        self.assertEqual(part_one(self.secrets), expected)
    
    def test_part_two(self):
        expected = 24
        self.assertEqual(part_two(self.secrets), expected)

if __name__ == "__main__":
    unittest.main()