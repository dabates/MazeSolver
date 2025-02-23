import os
import sys
import unittest
from unittest.mock import Mock

from Line import Line
from Point import Point

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class LineTestCases(unittest.TestCase):
    def test_line_eq(self):
        p1 = Point(0, 0)
        p2 = Point(10, 10)

        line1 = Line(p1, p2)
        line2 = Line(p1, p2)
        line3 = Line(p2, p1)

        self.assertEqual(line1, line2)
        self.assertNotEqual(line1, line3)

    def test_line_start_end(self):
        p1 = Point(2, 3)
        p2 = Point(4, 5)

        line = Line(p1, p2)

        self.assertEqual(line.start, p1)
        self.assertEqual(line.end, p2)

    def test_line_draw(self):
        mock_canvas = Mock()
        p1 = Point(1, 1)
        p2 = Point(4, 4)
        line = Line(p1, p2)

        line.draw(mock_canvas, "blue")

        mock_canvas.create_line.assert_called_with(1, 1, 4, 4, fill="blue")

if __name__ == '__main__':
    unittest.main()
