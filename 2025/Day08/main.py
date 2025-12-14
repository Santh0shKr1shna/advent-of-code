import unittest
from collections import defaultdict

def part_one(points, connection_limit = 1000):
    n = len(points)
    edges = []

    for i in range(n):
        for j in range(i + 1, n):
            p1 = points[i]
            p2 = points[j]
            dist = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2
            edges.append((dist, i, j))

    edges.sort(key=lambda x: x[0])

    parent = list(range(n))

    def find(i):
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]

    for _, i, j in edges[:connection_limit]:
        if find(i) != find(j):
            parent[find(i)] = parent[find(j)]

    circuits = defaultdict(int)
    for i in range(n):
        circuits[find(i)] += 1

    sizes = list(circuits.values())
    sizes.sort(reverse=True)

    result = 1
    for i in sizes[:3]:
        result *= i

    return result


def part_two(points: list):
    n = len(points)
    edges = []

    for i in range(n):
        for j in range(i + 1, n):
            p1 = points[i]
            p2 = points[j]
            dist = (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2
            edges.append((dist, i, j))

    edges.sort(key=lambda x: x[0])

    parent = list(range(n))
    circuits = n

    def find(i):
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]

    def union(i, j):
        root_i = find(i)
        root_j = find(j)
        if root_i != root_j:
            parent[root_j] = root_i
            return True
        return False

    for _, u, v in edges:
        if union(u, v):
            circuits -= 1
            
            if circuits == 1:
                x1 = points[u][0]
                x2 = points[v][0]
                result = x1 * x2
                
                return result

    return None

class TestSuite(unittest.TestCase):
    def setUp(self) -> None:
        file = open("test.txt")
        self.points = []

        lines = file.read().strip().split('\n')
        for line in lines:
            if line.strip():
                coords = list(map(int, line.split(',')))
                self.points.append(coords)
        
        file.close()

    def test_part_one_solution(self):
        expected = 40
        self.assertEqual(part_one(self.points, 10), expected)

    def test_part_two_solution(self):
        expected = 25272
        self.assertEqual(part_two(self.points), expected)

if __name__ == "__main__":
    unittest.main()