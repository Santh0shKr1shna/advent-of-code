import unittest

from collections import defaultdict, deque

def part_one(order, pages):
    res = 0

    for page in pages:
        n = len(page)
        safe = True
        for i in range(n-1):
            x,y = page[i], page[i+1]
            if y not in order[x]:
                safe = False
                break
        
        if safe:
            res += page[n // 2]

    return res

def part_two(order, pages):
    res = 0

    for page in pages:
        n = len(page)
        safe = True
        for i in range(n-1):
            x,y = page[i], page[i+1]
            if y not in order[x]:
                safe = False
                break
        
        if not safe:
            for i in range(n-1):
                for j in range(i+1,n):
                    x,y = page[i], page[j]
                    if y not in order[x]:
                        page[i], page[j] = page[j], page[i]

            res += page[n // 2]

    return res


class TestSuite(unittest.TestCase):
    def setUp(self) -> None:
        file = open("test.txt")
        self.order = defaultdict(set)
        self.pages = []

        O,P = file.read().strip().split('\n\n')
        file.close()

        for o in O.split('\n'):
            x,y = list(map(int, o.split('|') ))
            self.order[x].add(y)

        for p in P.split('\n'):
            self.pages.append(list(map(int, p.strip(' ').split(','))))
    
    def test_part_one(self):
        expected = 143
        self.assertEqual(part_one(self.order, self.pages), expected)

    def test_part_two(self):
        expected = 123
        self.assertEqual(part_two(self.order, self.pages), expected)

if __name__ == "__main__":
    unittest.main()