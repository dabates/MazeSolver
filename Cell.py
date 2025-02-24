from Line import Line
from Point import Point
from window import Window

class Cell:
    def __init__(self, win: Window):
        self.has_left_wall = True
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True

        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

        self.visited = False

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return

        self._x1, self._y1 = x1, y1
        self._x2, self._y2 = x2, y2

        if self.has_left_wall:
            self._win.draw_line(Line(Point(x1, y1), Point(x1, y2)))
        else:
            self._win.draw_line(Line(Point(x1, y1), Point(x1, y2)), "#d9d9d9")

        if self.has_top_wall:
            self._win.draw_line(Line(Point(x1, y1), Point(x2, y1)))
        else:
            self._win.draw_line(Line(Point(x1, y1), Point(x2, y1)), "#d9d9d9")

        if self.has_right_wall:
            self._win.draw_line(Line(Point(x2, y1), Point(x2, y2)))
        else:
            self._win.draw_line(Line(Point(x2, y1), Point(x2, y2)), "#d9d9d9")

        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(x1, y2), Point(x2, y2)))
        else:
            self._win.draw_line(Line(Point(x1, y2), Point(x2, y2)), "#d9d9d9")

    def draw_move(self, to_cell, undo=False):
        draw_color = "gray" if undo else "red"

        start_center = Point(self._x1 + (self._x2 - self._x1) / 2, self._y1 + (self._y2 - self._y1) / 2)
        end_center = Point(to_cell._x1 + (to_cell._x2 - to_cell._x1) / 2, to_cell._y1 + (to_cell._y2 - to_cell._y1) / 2)

        self._win.draw_line(Line(start_center, end_center), draw_color)
