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

    def test_break_walls_r(self):
        for col in range(self.cols):
            for row in range(self.rows):
                # Reset all cells for tests
                self.maze._cells[col][row].visited = False
                self.maze._cells[col][row].has_left_wall = True
                self.maze._cells[col][row].has_right_wall = True
                self.maze._cells[col][row].has_top_wall = True
                self.maze._cells[col][row].has_bottom_wall = True

        self.maze._break_walls_r(0, 0)

        for col in range(self.cols):
            for row in range(self.rows):
                self.assertTrue(self.maze._cells[col][row].visited)

        wall_removed = any(
            not (cell.has_top_wall and cell.has_bottom_wall and cell.has_left_wall and cell.has_right_wall)
            for row in range(self.rows) for col in range(self.cols)
            for cell in [self.maze._cells[col][row]]
        )

        self.assertTrue(wall_removed, "No walls were removed, the maze is still fully blocked.")

if __name__ == '__main__':
    unittest.main()
