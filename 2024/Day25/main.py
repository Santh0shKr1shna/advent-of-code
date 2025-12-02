import unittest

def solve(locks, keys):
    fits = 0
    for lock in locks:
        for key in keys:
            fit = True
            for i in range(5):
                if lock[i] + key[i] > 5:
                    fit = False
                    break
            if fit:
                fits += 1
    return fits

class TestSuite(unittest.TestCase):
    def setUp(self):
        filename = "test.txt"
        
        self.locks = []
        self.keys = []

        file = open(filename)
        schematics = file.read().split('\n\n')
        file.close()

        for scheme in schematics:
            lines = scheme.splitlines()
            if lines[0] == "#####":
                temp = []
                for i in range(5):
                    c = 0
                    for j in range(1,7):
                        if lines[j][i] == ".":
                            break
                        c += 1
                    temp.append(c)
                self.locks.append(temp)
            elif lines[-1] == "#####":
                temp = []
                for i in range(5):
                    c = 0
                    for j in range(5,-1,-1):
                        if lines[j][i] == ".":
                            break
                        c += 1
                    temp.append(c)
                self.keys.append(temp)
            else:
                raise ValueError("Schematic doesnt match a key or lock scheme")
    def test_solve_function(self):
        expected = 3
        self.assertEqual(solve(self.locks, self.keys), expected)


if __name__ == "__main__":
    unittest.main()