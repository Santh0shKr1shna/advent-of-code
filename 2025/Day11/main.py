import unittest

def part_one(graph):
    res = 0
    dp = {}
    
    def dfs(node):
        tot = 0
        if node == "out": return 1

        if node in dp: return dp[node]

        for nex in graph[node]:
            tot += dfs(nex)

        dp[node] = tot
        return tot

    res = dfs("you")

    return res

def part_two(graph):
    res = 0
    dp = {}
    
    def count_paths(node, target):
        if node == target:
            return 1
        
        if node not in graph:
            return 0
        
        if (node, target) in dp:
            return dp[(node, target)]

        paths = 0
        for nex in graph[node]:
            paths += count_paths(nex, target)

        dp[(node, target)] = paths
        return paths

    p1 = count_paths("svr", "fft")
    q1 = count_paths("fft", "dac")
    r1 = count_paths("dac", "out")
    res1 = p1 * q1 * r1

    p2 = count_paths("svr", "dac")
    q2 = count_paths("dac", "fft")
    r2 = count_paths("fft", "out")
    res2 = p2 * q2 * r2

    res = res1 + res2

    return res


class TestSuite(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_part_one_solution(self):
        file = open("test_1.txt")

        self.graph_1 = {}

        for line in file.readlines():
            src, dst = line.split(':')
            src = src.strip()
            dst = dst.strip().split()

            self.graph_1[src] = dst

        expected = 5
        self.assertEqual(part_one(self.graph_1), expected)

        file.close()

    def test_part_two_solution(self):
        file = open("test_2.txt")

        self.graph_2 = {}

        for line in file.readlines():
            src, dst = line.split(':')
            src = src.strip()
            dst = dst.strip().split()

            self.graph_2[src] = dst

        expected = 2
        self.assertEqual(part_two(self.graph_2), expected)

        file.close()

if __name__ == "__main__":
    unittest.main()