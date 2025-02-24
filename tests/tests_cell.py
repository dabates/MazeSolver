import os
import sys
import unittest
from unittest.mock import MagicMock

from Cell import Cell
from Line import Line
from Point import Point
from window import Window

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Maze import Maze

class CellTestCases(unittest.TestCase):
    def setUp(self):
        """Setup the standard stuff for all tests"""
        self.mock_win = MagicMock(spec=Window)
        self.cell = Cell(self.mock_win)

    def test_default_walls(self):
        self.assertTrue(self.cell.has_left_wall)
        self.assertTrue(self.cell.has_right_wall)
        self.assertTrue(self.cell.has_top_wall)
        self.assertTrue(self.cell.has_bottom_wall)

    def test_draw_with_all_walls(self):
        self.cell.draw(0, 0, 10, 10)

        expected_calls = [
            ((Line(Point(0, 0), Point(0, 10))),),
            ((Line(Point(0, 0), Point(10, 0))),),
            ((Line(Point(10, 0), Point(10, 10))),),
            ((Line(Point(0, 10), Point(10, 10))),)
        ]

        actual_calls = [call[0] for call in self.mock_win.draw_line.call_args_list]
        self.assertEqual(len(actual_calls), len(expected_calls))

        for exp_call in expected_calls:
            self.assertIn(exp_call, actual_calls)

    def test_draw_with_some_walls(self):
        self.cell.has_left_wall = False
        self.cell.has_bottom_wall = False
        self.cell.draw(0, 0, 10, 10)

        expected_calls = [
            ((Line(Point(0, 0), Point(10, 0))),),
            ((Line(Point(0, 0), Point(10, 0))),),
            ((Line(Point(10, 0), Point(10, 10))),),
            ((Line(Point(0, 10), Point(10, 10))), "#d9d9d9")
        ]

        actual_calls = [call[0] for call in self.mock_win.draw_line.call_args_list]
        self.assertEqual(len(actual_calls), len(expected_calls))

        for exp_call in expected_calls:
            self.assertIn(exp_call, actual_calls)

    def test_draw_move(self):
        cell2 = Cell(self.mock_win)
        self.cell.draw(0, 0, 10, 10)
        cell2.draw(10, 0, 20, 10)

        self.cell.draw_move(cell2, undo=False)

        expected_calls = [
            Line(Point(5, 5), Point(15, 5)), "red"
        ]

        self.mock_win.draw_line.assert_called_with(*expected_calls)

    def test_draw_move_undo(self):
        cell2 = Cell(self.mock_win)
        self.cell.draw(0, 0, 10, 10)
        cell2.draw(10, 0, 20, 10)

        self.cell.draw_move(cell2, undo=True)

        expected_calls = [
            Line(Point(5, 5), Point(15, 5)), "gray"
        ]

        self.mock_win.draw_line.assert_called_with(*expected_calls)

if __name__ == '__main__':
    unittest.main()
