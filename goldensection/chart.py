from matplotlib.backends.backend_gtk3agg import (FigureCanvasGTK3Agg as FigureCanvas)
from matplotlib.figure import Figure
import numpy as np
from gi.repository import Gtk, Gdk, Granite, GdkPixbuf

class Chart:
    def __init__(self):
        self.figure = Figure()
        self.title="something"
        self.subplot = self.figure.add_subplot(111, ylabel="f(x)", xlabel="x", title=self.title)
        self.x = []
        self.y = []

        self.sw = Gtk.ScrolledWindow()
        # A scrolled window border goes outside the scrollbars and viewport
        canvas = FigureCanvas(self.figure)  # a Gtk.DrawingArea
        # canvas.set_size_request(800, 600)
        self.sw.add_with_viewport(canvas)

    def update(self, function):
        self.del_points()
        self.subplot.clear()
        self.generate_points(function)
        self.subplot.plot(self.x, self.y)

    def generate_points(self, f):
        for x in range(-50,50,1):
            self.x.append(x)
            self.y.append(f(x))

    def del_points(self):
        self.x = []
        self.y = []
