from Maze import Maze
from window import Window

def main():
    width = 800
    height = 600
    win = Window(width, height)

    half_width = width * .5
    half_height = height * .5

    cell_size_x = 100
    cell_size_y = 100
    rows = 5
    cols = 5

    start_x = half_width - (cell_size_x * (cols / 2))
    start_y = half_height - (cell_size_y * (rows / 2))

    if start_x < 0:
        start_x = 0

    if start_y < 0:
        start_y = 0

    Maze(start_x, start_y, rows, cols, cell_size_x, cell_size_y, win)

    win.wait_for_close()

if __name__ == "__main__":
    main()
