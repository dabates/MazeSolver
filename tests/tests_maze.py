import unittest

from Maze import Maze

class MazeTestSuite(unittest.TestCase):
    def setUp(self):
        self.cols = 5
        self.rows = 5
        self.maze = Maze(0, 0, self.rows, self.cols, 10, 10)

    def test_maze_create_cells(self):
        self.assertEqual(len(self.maze._cells), self.cols)
        self.assertEqual(len(self.maze._cells[0]), self.rows)

    def test_break_entrance_and_exit(self):
        self.maze._break_entrance_and_exit()

        self.assertFalse(self.maze._cells[0][0].has_left_wall)
        self.assertFalse(self.maze._cells[self.cols - 1][self.rows - 1].has_right_wall)

if __name__ == '__main__':
    unittest.main()
