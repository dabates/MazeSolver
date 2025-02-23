import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Point import Point

class PointTestCases(unittest.TestCase):
    def test_point_eq(self):
        p1 = Point(1, 2)
        p2 = Point(1, 2)
        p3 = Point(1, 3)

        self.assertEqual(p1, p2)
        self.assertNotEqual(p1, p3)

    def test_point_coordinates(self):
        p1 = Point(3, 7)

        self.assertEqual(p1.x, 3)
        self.assertEqual(p1.y, 7)

if __name__ == '__main__':
    unittest.main()
