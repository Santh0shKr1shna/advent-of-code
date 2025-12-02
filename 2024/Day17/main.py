import unittest
import math
    

def part_one(a,b,c, program):
    res = []
    i = 0
    n = len(program)

    def combo(num):
        if num < 4: return num
        if num == 4: return a
        if num == 5: return b
        if num == 6: return c
        return ValueError("not supported value")


    while i < n:
        opcode = program[i]
        operand = program[i+1]

        if opcode == 0:
            a = a // pow(2, combo(operand))
        elif opcode == 1:
            b = b ^ operand
        elif opcode == 2:
            b = combo(operand) % 8
        elif opcode == 3:
            if a != 0:
                i = operand
                continue
        elif opcode == 4:
            b = b ^ c
        elif opcode == 5:
            res.append(combo(operand) % 8)
        elif opcode == 6:
            b = a // pow(2, combo(operand))
        elif opcode == 0:
            c = a // pow(2, combo(operand))
        
        i += 2

    return res

def part_two(a, b, c, program):
    n = len(program)
    res = [None] * n

    i = n-1

    start, end = a, 100000000000

    def match_program(num):
        match_res = part_one(num, b, c, program)
        print(match_res)
        if match_res == program:
            return n
        count = 0
        print("n is:", n)
        print("mr is:", len(match_res))
        if n == len(match_res):
            for i in range(n-1, -1, -1):
                if program[i] == match_res[i]:
                    count += 1
                else:
                    break

        return count

    # start_match = match_program(start)
    prev_pos = 0
    prev_match = 0
    while start < end:
        cur = match_program(start)
        print(start, prev_match, cur)
        if cur == n:
            print("does match even work?")
            return start
        if prev_match >= n-2 and prev_match >= cur:
            for val in range(prev_pos, start):
                cur = match_program(val)
                if cur == n:
                    print(val)
                    return(val)
            # print("we are doomed")
            # break
        else:
            prev_pos = start
            prev_match = cur
            start += 20000



class TestSuite(unittest.TestCase):
    def setUp(self) -> None:
        filename = "test.txt"

        file = open(filename)
        rData, pData = file.read().split('\n\n')
        file.close()

        self.ra, self.rb, self.rc = list(map(lambda x: int(x.strip().split(':')[1].strip()), rData.split('\n')))

        self.program = list(map(int, pData.split(':')[1].strip().split(',')))

    
    # def test_part_one(self):
    #     expected = [4,0,4,7,1,2,7,1,6]
    #     self.assertEqual(part_one(self.ra, self.rb, self.rc, self.program), expected)

    def test_part_two(self):
        expected = 202322348616234
        self.assertEqual(part_two(self.ra, self.rb, self.rc, self.program), expected)

if __name__ == "__main__":
    unittest.main()