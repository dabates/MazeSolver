from tkinter import Tk, BOTH, Canvas

from Line import Line

class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Window")
        self.root.geometry(f"{width}x{height}")
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=True)

        self.root.protocol("WM_DELETE_WINDOW", self.close)

        self.running = False

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False
        self.root.destroy()

    def draw_line(self, line: Line, fill_color):
        line.draw(self.canvas, fill_color)