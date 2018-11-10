from gi.repository import Gtk, Gdk, Granite, GdkPixbuf


class Result:
    def __init__(self, function):

        function.connect("update", self.update_func)
        self.func_label = Gtk.Label(margin=5)
        self.range_label = Gtk.Label(margin=5)

        grid = Gtk.Grid()

        grid.attach(self.func_label, 0, 0, 1, 1)
        grid.attach(self.range_label, 0, 1, 1, 1)


        self.frame = Gtk.Frame(margin=20)
        self.frame.set_label("Result")
        self.frame.add(grid)

    def update_func(self, arg, text):
        self.func_label.set_label(text)
        # self.range_label.set_label(self.build_range_label_text(algorithm.c, algorithm.d))

    def build_range_label_text(self, c, d):
        return "Left "+ str(c)+ " Right" + str(d)
