import unittest

def part_one(points):
    res = 0
    n = len(points)

    for i in range(n-1):
        for j in range(i+1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]

            w = abs(x1-x2) + 1
            h = abs(y1-y2) + 1

            area = w * h
            res = max(area, res)

    return res

def part_two(points):
    res = 0

    n = len(points)

    edges = []
    for i in range(n):
        p1 = points[i]
        p2 = points[(i + 1) % n]
        edges.append((p1, p2))

    def centre(mix, max, miy, may):
        px = (mix + max) / 2.0
        py = (miy + may) / 2.0

        is_inside = False
        for (vx1, vy1), (vx2, vy2) in edges:
             if ((vy1 > py) != (vy2 > py)):
                intersect_x = (vx2 - vx1) * (py - vy1) / (vy2 - vy1) + vx1
                if px < intersect_x:
                    is_inside = not is_inside

        return is_inside
    
    def intersect(mix, maxi, miy, may):
        for (ex1, ey1), (ex2, ey2) in edges:
            e_min_x, e_max_x = min(ex1, ex2), max(ex1, ex2)
            e_min_y, e_max_y = min(ey1, ey2), max(ey1, ey2)

            if ex1 == ex2:
                if mix < ex1 and ex1 < maxi:
                    if max(miy, e_min_y) < min(may, e_max_y):
                        return True 
            else:
                if miy < ey1 and ey1 < may:
                    if max(mix, e_min_x) < min(maxi, e_max_x):
                        return True
        return False

    for i in range(n-1):
        for j in range(i+1, n):
            x1,y1 = points[i]
            x2,y2 = points[j]

            w = abs(x1-x2) + 1
            h = abs(y1-y2) + 1

            area = w * h
            
            if area < res: continue

            rx_min, rx_max = min(x1,x2), max(x1,x2)
            ry_min, ry_max = min(y1,y2), max(y1,y2)

            if not centre(rx_min, rx_max, ry_min, ry_max):
                continue
            
            if intersect(rx_min, rx_max, ry_min, ry_max):
                continue

            res = area

    return res

class TestSuite(unittest.TestCase):
    def setUp(self) -> None:
        file = open("test.txt")

        self.points = []
        
        for line in file.readlines():
            self.points.append(list(map(int, line.split(','))))

        file.close()

    def test_part_one_solution(self):
        expected = 50
        self.assertEqual(part_one(self.points), expected)

    def test_part_two_solution(self):
        expected = 24
        self.assertEqual(part_two(self.points), expected)

if __name__ == "__main__":
    unittest.main()