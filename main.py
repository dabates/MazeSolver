from Cell import Cell
from Line import Line
from Point import Point
from window import Window

def main():
    win = Window(800, 600)

    # win.draw_line(Line(Point(10, 10), Point(10, 400)), "red")
    # win.draw_line(Line(Point(30, 10), Point(30, 400)), "blue")
    # win.draw_line(Line(Point(50, 10), Point(50, 400)), "green")

    c = Cell(win)
    c.has_left_wall = False
    c.draw(50, 50, 100, 100)

    c = Cell(win)
    c.has_right_wall = False
    c.draw(125, 125, 200, 200)

    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(225, 225, 250, 250)

    c = Cell(win)
    c.has_top_wall = False
    c.draw(300, 300, 500, 500)

    win.wait_for_close()

if __name__ == "__main__":
    main()
