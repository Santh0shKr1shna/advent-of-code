import unittest
from collections import deque
from pulp import LpVariable, LpProblem, LpInteger, LpMinimize, PULP_CBC_CMD, value

def part_one(parsed):
    res = 0

    for target, buttons, joltage in parsed:
        target_state = tuple(1 if ch == '#' else 0 for ch in target)
        initial = (0,) * len(target)

        queue = deque([(initial, 0)])
        vis = set()

        while queue:
            cur, dist = queue.popleft()

            if cur in vis:
                continue
            vis.add(cur)

            if cur == target_state:
                res += dist
                break

            for button in buttons:
                nex = list(cur)
                for idx in button:
                    nex[idx] = 1 - nex[idx]

                queue.append((tuple(nex), dist+1))

    return res

def part_two(parsed):
    res = 0

    for target, buttons, joltage in parsed:
        n1 = len(buttons)
        n2 = len(joltage)

        # First time using LP :-)
        buttonlpvars = [
            LpVariable(f"button_{i}", lowBound=0, cat=LpInteger)
            for i in range(n1)
        ]

        prob = LpProblem("Minimise_presses", LpMinimize)

        prob += sum(buttonlpvars)

        for idx in range(n2):
            rb = [
                buttonlpvars[btn_idx]
                for btn_idx, effect in enumerate(buttons)
                if idx in effect
            ]
            prob += sum(rb) == joltage[idx]

        prob.solve(PULP_CBC_CMD(msg=0))
        
        res += int(sum(value(x) for x in buttonlpvars))

    return res

class TestSuite(unittest.TestCase):
    def setUp(self) -> None:
        file = open("test.txt")

        self.parsed = []

        for line in file.readlines():
            line = line.strip()

            target = line[1 : line.find(']')]

            button_data = line[line.find('(') : line.find('{') - 1]
            buttons = []

            for b in button_data.strip().split():
                buttons.append(set(map(int, b[1:-1].split(','))))

            joltage = list(map(int, line[line.find('{')+1 : -1].split(',')))

            self.parsed.append((target, buttons, joltage))

        file.close()


    def test_part_one_solution(self):
        expected = 7
        self.assertEqual(part_one(self.parsed), expected)

    def test_part_two_solution(self):
        expected = 33
        self.assertEqual(part_two(self.parsed), expected)

if __name__ == "__main__":
    unittest.main()