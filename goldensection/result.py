from gi.repository import Gtk, Gdk, Granite, GdkPixbuf


class Result:
    def __init__(self, function, algorithm):

        function.connect("update", self.update_func)
        algorithm.connect("update", self.update_algo)
        self.func_label_desc = Gtk.Label("Function:", margin=5)
        self.range_r_label_desc = Gtk.Label("Left", margin=5)
        self.range_l_label_desc = Gtk.Label("Right", margin=5)

        self.func_label = Gtk.Label(margin=5)
        self.range_r_label = Gtk.Label(margin=5)
        self.range_l_label = Gtk.Label(margin=5)

        grid = Gtk.Grid()

        grid.attach(self.func_label_desc, 0, 0, 1, 1)
        grid.attach(self.range_l_label_desc, 0, 1, 1, 1)
        grid.attach(self.range_r_label_desc, 0, 2, 1, 1)

        grid.attach(self.func_label, 1, 0, 1, 1)
        grid.attach(self.range_l_label, 1, 1, 1, 1)
        grid.attach(self.range_r_label, 1, 2, 1, 1)

        self.frame = Gtk.Frame(margin=20)
        self.frame.set_label("Result")
        self.frame.add(grid)

    def update_func(self, arg, text):
        self.func_label.set_label(text)

    def update_algo(self, arg, c, d):
        self.range_l_label.set_label(str(c))
        self.range_r_label.set_label(str(d))
