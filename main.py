from Cell import Cell
from Line import Line
from Point import Point
from window import Window

def main():
    win = Window(800, 600)

    c = Cell(win)
    c.has_right_wall= False
    c.draw(50, 50, 100, 100)

    c2 = Cell(win)
    c2.has_left_wall = False
    c2.draw(200, 50, 250, 100)

    c.draw_move(c2)

    win.wait_for_close()

if __name__ == "__main__":
    main()
