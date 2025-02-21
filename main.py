from Line import Line
from Point import Point
from window import Window

def main():
    win = Window(800, 600)

    win.draw_line(Line(Point(10, 10), Point(10, 400)), "red")
    win.draw_line(Line(Point(30, 10), Point(30, 400)), "blue")
    win.draw_line(Line(Point(50, 10), Point(50, 400)), "green")

    win.wait_for_close()

if __name__ == "__main__":
    main()
