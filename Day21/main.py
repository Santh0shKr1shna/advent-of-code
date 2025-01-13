import unittest
from itertools import combinations
from functools import lru_cache


numeric_keys = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),

    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),

    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),

    "0": (3, 1),
    "A": (3, 2),
}

direction_keys = {
    "^": (0, 1),
    "A": (0, 2),

    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2),
}

dd = {
    ">": (0, 1),
    "<": (0, -1),
    "^": (-1, 0),
    "v": (1, 0)
}

def get_combos(ca, a, cb, b):
    for idx in combinations(range(a+b), r=a):
        res = [cb] * (a+b)
        for i in idx:
            res[i] = ca
        yield "".join(res)

@lru_cache
def generate_ways(a, b, keypad):
    keypad = direction_keys if keypad else numeric_keys

    cur_loc = keypad[a]
    next_loc = keypad[b]

    di = next_loc[0] - cur_loc[0]
    dj = next_loc[1] - cur_loc[1]

    moves = []
    if di > 0:
        moves += ["v", di]
    else:
        moves += ["^", -di]
    if dj > 0:
        moves += [">", dj]
    else:
        moves += ["<", -dj]

    raw_combos = list(set(["".join(x) + "A" for x in get_combos(*moves)]))
    combos = []

    for combo in raw_combos:
        ci,cj = cur_loc
        good = True
        for c in combo[:-1]:
            di, dj = dd[c]
            ci, cj = ci+di, cj+dj
            if not (ci,cj) in keypad.values():
                good = False
                break
        if good:
            combos.append(combo)

    return combos

@lru_cache(None)
def get_cost(a, b, keypad, depth=0):
    if depth == 0:
        return min([len(x) for x in generate_ways(a, b, True)])
    
    ways = generate_ways(a, b, keypad)
    best_cost = 1 << 60

    for seq in ways:
        seq = "A" + seq
        cost = 0
        for i in range(len(seq) - 1):
            a, b = seq[i], seq[i+1]
            cost += get_cost(a, b, True, depth-1)
        
        best_cost = min(best_cost, cost)

    return best_cost

def get_code_cost(code, depth):
    code = "A" + code
    cost = 0
    for i in range(len(code) - 1):
        a, b = code[i], code[i+1]
        cost += get_cost(a, b, False, depth-1)
    
    return cost

def get_final_cost(codes, depth):
    ans = 0
    for code in codes:
        ans += get_code_cost(code, depth) * int(code[:-1])

    return ans

class TestSuite(unittest.TestCase):
    def setUp(self) -> None:
        filename = "test.txt"
        file = open(filename)

        self.codes = []
        for line in file.read().splitlines():
            self.codes.append(line.strip())
        file.close()

    def test_part_one(self):
        expected = 126384
        depth = 3

        got = get_final_cost(self.codes, depth)

        self.assertEqual(got, expected)

    def test_part_two(self):
        expected = 258263972600402
        depth = 25

        got = get_final_cost(self.codes, depth)

        self.assertEqual(got, expected)

if __name__ == "__main__":
    unittest.main()