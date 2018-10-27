from matplotlib.backends.backend_gtk3agg import (FigureCanvasGTK3Agg as FigureCanvas)
from matplotlib.figure import Figure
import numpy as np
from gi.repository import Gtk, Gdk, Granite, GdkPixbuf

class Chart:
    def __init__(self):
        fig = Figure(figsize=(5, 4), dpi=100)
        a = fig.add_subplot(111)
        t = np.arange(0.0, 3.0, 0.01)
        s = np.sin(2*np.pi*t)

        a.plot(t, s)

        self.sw = Gtk.ScrolledWindow()
        # A scrolled window border goes outside the scrollbars and viewport
        canvas = FigureCanvas(fig)  # a Gtk.DrawingArea
        # canvas.set_size_request(800, 600)
        self.sw.add_with_viewport(canvas)
