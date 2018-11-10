from gi.repository import Gtk, Gdk, Granite, GdkPixbuf


class FunctionParameters:
    def __init__(self, function, algorithm, chart):
        self.function = function
        self.algorithm = algorithm
        self.chart = chart

        label_a = Gtk.Label("Parameter A", margin=5)
        label_b = Gtk.Label("Parameter B", margin=5)
        label_c = Gtk.Label("Parameter C", margin=5)

        param_a = Gtk.Entry(margin=5)
        param_a.set_tooltip_text("Parameter A")
        param_a.set_placeholder_text("Parameter A")
        param_a.set_text(str(self.function.param_a))
        param_a.connect("changed", self.on_activate_a)

        param_b = Gtk.Entry(margin=5)
        param_b.set_tooltip_text("Parameter B")
        param_b.set_placeholder_text("Parameter B")
        param_b.set_text(str(self.function.param_b))
        param_b.connect("changed", self.on_activate_b)

        param_c = Gtk.Entry(margin=5)
        param_c.set_tooltip_text("Parameter C")
        param_c.set_placeholder_text("Parameter C")
        param_c.set_text(str(self.function.param_c))
        param_c.connect("changed", self.on_activate_c)

        param_grid = Gtk.Grid()
        param_grid.attach(label_a, 0, 0, 1, 1)
        param_grid.attach(label_b, 0, 1, 1, 1)
        param_grid.attach(label_c, 0, 2, 1, 1)

        param_grid.attach(param_a, 1, 0, 1, 1)
        param_grid.attach(param_b, 1, 1, 1, 1)
        param_grid.attach(param_c, 1, 2, 1, 1)

        self.frame = Gtk.Frame(margin=20)
        self.frame.set_label("Function Parameters")
        self.frame.add(param_grid)

        self.chart.update(self.function, self.algorithm)

        self.recalculate()

    def on_activate_a(self, widget, event=None):
        self.function.update(widget.get_text(), 0, 0)
        self.recalculate()

    def on_activate_b(self, widget, event=None):
        self.function.update(0, widget.get_text(), 0)
        self.recalculate()

    def on_activate_c(self, widget, event=None):
        self.function.update(0, 0, widget.get_text())
        self.recalculate()

    def recalculate(self):
        self.algorithm.find_min()
        self.algorithm.f = self.function.f
        self.chart.update(self.function, self.algorithm)


    def to_float(self, string):
        if not string:
            return 0.0
        else:
            return float(string)
