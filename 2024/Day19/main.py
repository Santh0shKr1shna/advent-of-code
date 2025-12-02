import unittest

class TestSuite(unittest.TestCase):
    def setUp(self) -> None:
        filename = "test.txt"
        file = open(filename)


        towelData, patternData = file.read().split('\n\n')
        file.close()

        self.towels = list(map(lambda x : x.strip(), towelData.split(',')))
        self.patterns = list(map(lambda x : x.strip(), patternData.splitlines()))


    def test_part_one(self):
        pass

    def test_part_two(self):
        pass

if __name__ == "__main__":
    unittest.main()