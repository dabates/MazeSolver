import time

from Cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []

        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        self.cells = []  ## Reset to new list

        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))

            self._cells.append(col_cells)

        if self._win is None:
            return

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        cell = self._cells[i][j]

        # Calculate the x/y position based on the values
        x1 = i * self._cell_size_x + self._x1
        y1 = j * self._cell_size_y + self._y1
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        cell.draw(x1, y1, x2, y2)

        self._animate()

    def _animate(self):
        if self._win is not  None:
            self._win.redraw()

        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._draw_cell(0, 0)

        self._cells[self._num_cols - 1][self._num_rows - 1].has_right_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)
