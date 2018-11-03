from matplotlib.backends.backend_gtk3agg import (FigureCanvasGTK3Agg as FigureCanvas)
from matplotlib.figure import Figure
import numpy as np
from gi.repository import Gtk, Gdk, Granite, GdkPixbuf

class Chart:
    def __init__(self):
        self.figure = Figure()
        self.subplot = self.figure.add_subplot(111, ylabel="f(x)", xlabel="x", title="function")
        self.x = []
        self.y = []

        self.color = (0.20392156862745098, 0.396078431372549, 0.6431372549019608)

        self.sw = Gtk.ScrolledWindow()
        # A scrolled window border goes outside the scrollbars and viewport
        canvas = FigureCanvas(self.figure)  # a Gtk.DrawingArea
        # canvas.set_size_request(800, 600)
        self.sw.add_with_viewport(canvas)

        self.f = None

    def update(self, function):
        self.f = function
        if not function:
            function = self.f
        print("CHART", self.color)
        self.del_points()
        self.subplot.clear()
        self.subplot.axhline(0, color='#d4d4d4', linestyle='--')
        self.subplot.axvline(0, color='#d4d4d4', linestyle='--')
        self.subplot.set_title(function.label_text)
        self.generate_points(function.f)
        self.subplot.plot(self.x, self.y, color=self.color)
        self.figure.canvas.draw()
        self.subplot.set_ylabel("f(x)")
        self.subplot.set_xlabel("x")


    def generate_points(self, f):
        print("Generating points")
        for x in range(-10,10,1):
            print("X, y", x, f(x))
            self.x.append(x)
            self.y.append(f(x))

    def del_points(self):
        print("Deleting points")
        self.x = []
        self.y = []
