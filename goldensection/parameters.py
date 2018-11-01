from gi.repository import Gtk, Gdk, Granite, GdkPixbuf


class Parameters:
    def __init__(self, function):
        self.function = function

        param_a = Gtk.Entry(margin=5)
        param_a.set_tooltip_text("Parameter A")
        param_a.set_placeholder_text("Parameter A")
        param_a.connect("activate", self.on_activate_a)
        param_a.connect("focus-out-event", self.on_activate_a)

        param_b = Gtk.Entry(margin=5)
        param_b.set_tooltip_text("Parameter B")
        param_b.set_placeholder_text("Parameter B")
        param_b.connect("activate", self.on_activate_b)
        param_b.connect("focus-out-event", self.on_activate_b)

        param_c = Gtk.Entry(margin=5)
        param_c.set_tooltip_text("Parameter C")
        param_c.set_placeholder_text("Parameter C")
        param_c.connect("activate", self.on_activate_c)
        param_c.connect("focus-out-event", self.on_activate_c)

        param_grid = Gtk.Grid()
        param_grid.attach(param_a, 0, 0, 1, 1)
        param_grid.attach(param_b, 0, 1, 1, 1)
        param_grid.attach(param_c, 0, 2, 1, 1)

        self.frame = Gtk.Frame(margin=20)
        self.frame.set_label("Golden Section Algorithm Parameters")
        self.frame.add(param_grid)

    def on_activate_a(self, widget, event=None):
        self.function.update(widget.get_text(), 0, 0)

    def on_activate_b(self, widget, event=None):
        self.function.update(0, widget.get_text(), 0)

    def on_activate_c(self, widget, event=None):
        self.function.update(0, 0, widget.get_text())
