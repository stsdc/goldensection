from gi.repository import Gtk, Gdk, Granite, GdkPixbuf


class Function:
    def __init__(self, chart):
        self.label = Gtk.Label()
        self.label_text = ""

        self.chart = chart

        self.frame = Gtk.Frame(margin=20)
        self.frame.set_label("The function")
        self.frame.add(self.label)

        self.param_a = -4
        self.param_b = 2
        self.param_c = 6

        self.update(self.param_a, self.param_b, self.param_c)

        self.f = lambda x: self.param_a*x*x + self.param_b*x + self.param_c



    def update(self, param_A, param_B, param_C):
        print (param_A, param_B, param_C)

        if(param_A):
            self.param_a = int(param_A)
            self.label_builder(param_A, self.param_b, self.param_c)

        if(param_B):
            self.param_b = int(param_B)
            self.label_builder(self.param_a, param_B, self.param_c)

        if(param_C):
            self.param_c = int(param_C)
            self.label_builder(self.param_a, self.param_b, param_C)

        self.label.set_label(self.label_text)
        self.set_func()
        self.chart.update(self)
        print("Extrema:", -self.param_b / (2 * self.param_a))



    def label_builder(self, param_A, param_B, param_C):
        label = "f(x) = "
        if(param_A == "1"):
            label = label + "x\u00b2 + "
        elif(param_A == "0"):
            print("is zero")
            pass
        else:
            label = label + str(param_A) + "x\u00b2 + "

        if(param_B == "1"):
            label = label + "x "
        elif(param_B == "0"):
            pass
        else:
            label = label + str(param_B) + "x "

        if(param_C == "0"):
            pass
        else:
            label = label + "+ " + str(param_C)
        self.label_text = label

    def set_func(self):
        self.f = lambda x: self.param_a*x*x + self.param_b*x + self.param_c
