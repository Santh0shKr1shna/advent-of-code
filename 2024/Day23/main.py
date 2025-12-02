import unittest
from collections import defaultdict

def part_one(conn: defaultdict):
    inter = set()
    for key, val in conn.items():
        if str(key).startswith('t'):
            for com1 in val:
                for com2 in conn[com1]:
                    if com2 == key:
                        continue
                    for com3 in conn[com2]:
                        if com3 == key:
                            temp = [key, com1, com2]
                            inter.add(tuple(sorted(temp)))

    return len(inter)

def part_two(conn: defaultdict):
    def bron_kerbosch(cur, poten, processed):
        if not poten and not processed:
            yield cur
        while poten:
            v = poten.pop()
            yield from bron_kerbosch(
                cur.union({v}),
                poten.intersection(conn[v]),
                processed.intersection(conn[v])
            )
            processed.add(v)
    
    all_cliques = bron_kerbosch(set(), set(conn.keys()), set())
    
    unique = set()

    for cliq in all_cliques:
        unique.add(tuple(sorted(list(cliq))))

    biggest = 0
    ans = None

    for cliq in unique:
        if len(cliq) > biggest:
            biggest = len(cliq)
            ans = cliq
    
    return ",".join(ans)

class TestSuite(unittest.TestCase):
    def setUp(self) -> None:
        filename = "test.txt"
        file = open(filename)

        self.conn = defaultdict(set)

        for line in file.read().splitlines():
            a,b = line.strip().split('-')
            self.conn[a].add(b)
            self.conn[b].add(a)

        file.close()

    def test_part_one(self):
        expected = 7
        self.assertEqual(part_one(self.conn), expected)

    def test_part_two(self):
        expected = "co,de,ka,ta"
        self.assertEqual(part_two(self.conn), expected)

if __name__ == "__main__":
    unittest.main()