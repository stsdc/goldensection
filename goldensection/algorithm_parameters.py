from gi.repository import Gtk, Gdk, Granite, GdkPixbuf


class AlgorithmParameters:
    def __init__(self, function, algorithm, chart):
        self.function = function
        self.algorithm = algorithm
        self.chart = chart

        label_a = Gtk.Label("Left guess", margin=5)
        label_b = Gtk.Label("Right guess", margin=5)
        label_tol = Gtk.Label("Tolerance", margin=5)

        self.constrain_a = Gtk.Entry(margin=5)
        self.constrain_a.set_tooltip_text("Constrain a")
        self.constrain_a.set_placeholder_text("Constrain a")
        self.constrain_a.set_text(str(self.algorithm.a))
        self.constrain_a.connect("changed", self.on_activate_constrain_a)

        self.constrain_b = Gtk.Entry(margin=5)
        self.constrain_b.set_tooltip_text("Constrain b")
        self.constrain_b.set_placeholder_text("Constrain b")
        self.constrain_b.set_text(str(self.algorithm.b))
        self.constrain_b.connect("changed", self.on_activate_constrain_b)

        tolerance = Gtk.Entry(margin=5)
        tolerance.set_tooltip_text("Tolerance")
        tolerance.set_placeholder_text("Tolerance")
        tolerance.set_text(str(self.algorithm.tolerance))
        tolerance.connect("changed", self.on_activate_tolerance)

        param_grid = Gtk.Grid()

        param_grid.attach(label_a, 0, 0, 1, 1)
        param_grid.attach(label_b, 0, 1, 1, 1)
        param_grid.attach(label_tol, 0, 2, 1, 1)

        param_grid.attach(self.constrain_a, 1, 0, 1, 1)
        param_grid.attach(self.constrain_b, 1, 1, 1, 1)
        param_grid.attach(tolerance, 1, 2, 1, 1)

        self.frame = Gtk.Frame(margin=20)
        self.frame.set_label("Golden Section Algorithm Parameters")
        self.frame.add(param_grid)

        self.chart.update(self.function, self.algorithm, self.to_float(self.constrain_a.get_text()), self.to_float(self.constrain_b.get_text()))

        self.recalculate()

    def on_activate_constrain_a(self, widget, event=None):
        self.algorithm.a = self.to_float(widget.get_text())
        self.recalculate()


    def on_activate_constrain_b(self, widget, event=None):
        self.algorithm.b = self.to_float(widget.get_text())
        self.recalculate()


    def on_activate_tolerance(self, widget, event=None):
        self.algorithm.tolerance = float(widget.get_text())
        self.recalculate()


    def recalculate(self):
        self.algorithm.a = self.to_float(self.constrain_a.get_text())
        self.algorithm.b = self.to_float(self.constrain_b.get_text())
        self.algorithm.find_min()
        self.algorithm.f = self.function.f
        self.chart.update(self.function, self.algorithm, self.to_float(self.constrain_a.get_text()), self.to_float(self.constrain_b.get_text()))


    def to_float(self, string):
        if not string:
            return 0.0
        else:
            return float(string)
