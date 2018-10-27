from gi.repository import Gtk, Gdk, Granite, GdkPixbuf


class Function:
    def __init__(self):
        self.label = Gtk.Label()

        self.frame = Gtk.Frame(margin=20)
        self.frame.set_label("The function")
        self.frame.add(self.label)

        self.param_a = 1
        self.param_b = 2
        self.param_c = 3

        self.update(self.param_a, self.param_b, self.param_c)


    def update(self, param_A, param_B, param_C):
        print (param_A, param_B, param_C)

        if(param_A):
            self.param_a = param_A
            self.label.set_label(self.label_builder(param_A, self.param_b, self.param_c))

        if(param_B):
            self.param_b = param_B
            self.label.set_label(self.label_builder(self.param_a, param_B, self.param_c))

        if(param_C):
            self.param_c = param_C
            self.label.set_label(self.label_builder(self.param_a, self.param_b, param_C))


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
            label = label + "x + "
        elif(param_B == "0"):
            pass
        else:
            label = label + str(param_B) + "x + "

        if(param_C == "0"):
            pass
        else:
            label = label + str(param_C)
        return label
