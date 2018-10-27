from gi.repository import Gtk, Gdk, Granite, GdkPixbuf


class Parameters:
    def __init__(self):
        label_xx = Gtk.Label(label="x^2+")
        label_x = Gtk.Label(label="x+")

        param_a = Gtk.Entry(margin=5)
        param_a.set_tooltip_text("Parameter A")
        param_a.set_placeholder_text("Parameter A")

        param_b = Gtk.Entry(margin=5)
        param_b.set_tooltip_text("Parameter B")
        param_b.set_placeholder_text("Parameter B")

        param_c = Gtk.Entry(margin=5)
        param_c.set_tooltip_text("Parameter C")
        param_c.set_placeholder_text("Parameter C")

        param_grid = Gtk.Grid()
        param_grid.attach(param_a, 0, 0, 1, 1)
        param_grid.attach(param_b, 0, 1, 1, 1)
        param_grid.attach(param_c, 0, 2, 1, 1)

        self.frame = Gtk.Frame(margin=20)
        self.frame.set_label("Golden Section Algorithm Parameters")
        self.frame.add(param_grid)
