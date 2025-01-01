import unittest

operation = {
    "AND": lambda x,y: x and y,
    "OR": lambda x,y: x or y,
    "XOR": lambda x,y: x ^ y
}

def part_one(initial, gates: list):
    while gates:
        for gate in gates:
            one, two, oper, tar = gate
            if one in initial and two in initial:
                tar_val = operation[oper](initial[one], initial[two])
                initial[tar] = tar_val
                gates.remove(gate)

    ans = 0
    for i in range(50):
        c = f"z{'0' if i < 10 else ''}{str(i)}"
        if c in initial:
            ans += pow(2, i) * int(initial[c])
        else:
            break

    return ans

def part_two(initial, gates, highest):
    wrong = set()
    wires = {}
    for gate in gates:
        one, two, oper, tar = gate
        if tar[0] == "z" and oper != "XOR" and tar != highest:
            wrong.add(tar)
        if (oper == "XOR"
            and tar[0] not in ["x", "y", "z"]
            and one[0] not in ["x", "y", "z"]
            and two[0] not in ["x", "y", "z"]
        ):
            wrong.add(tar)
        if oper == "AND" and "x00" not in [one, two]:
            for subop1, subop2, subop, subres in gates:
                if (tar == subop1 or tar == subop2) and subop != "OR":
                    wrong.add(tar)

        if oper == "XOR":
            for subop1, subop2, subop, subres in gates:
                if (tar == subop1 or tar == subop2) and subop == "OR":
                    wrong.add(tar)

    while gates:
        one, two, op, res = gates.pop(0)
        if one in wires and two in wires:
            wires[res] = operation[op](one, two)
        else:
            gates.append((one, two, op, res))

    bits = [str(wires[wire]) for wire in sorted(wires, reverse=True) if wire[0] == "z"]
    
    return ",".join(sorted(wrong))

class TestSuite(unittest.TestCase):
    def setUp(self) -> None:
        filename = "test.txt"
        file = open(filename)
        initial_data, gates_data = file.read().split('\n\n')
        file.close()

        self.initial = {}
        self.gates = []
        self.highest = "z00"

        for line in initial_data.splitlines():
            fro, to = line.split(':')
            self.initial[fro.strip()] = int(to.strip())

        for line in gates_data.splitlines():
            one, operand, two, _, target = line.split(" ")
            self.gates.append([one, two, operand, target])
            if target[0] == "z" and int(target[1:]) > int(self.highest[1:]):
                self.highest = target

    def test_part_one(self):
        expected = 2024
        self.assertEqual(part_one(self.initial, self.gates), expected)

    def test_part_two(self):
        expected = "aaa,aoc,bbb,ccc,eee,ooo,z24,z99"
        self.assertEqual(part_two(self.initial, self.gates, self.highest), expected)

if __name__ == "__main__":
    unittest.main()