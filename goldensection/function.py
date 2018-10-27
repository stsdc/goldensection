from gi.repository import Gtk, Gdk, Granite, GdkPixbuf


class Function:
    def __init__(self):
        self.label = Gtk.Label()

        self.frame = Gtk.Frame(margin=20)
        self.frame.set_label("The function")
        self.frame.add(self.label)


    def update(self, param_A, param_B, param_C):
        print (param_A, param_B, param_C)
        self.label.set_label(self.label_builder(param_A, param_B, param_C))


    def label_builder(self, param_A, param_B, param_C):
        label = "f(x) = "
        if(param_A == 1):
            label = label + "x\u00b2 + "
        elif(param_A == 0):
            pass
        else:
            label = label + str(param_A) + "x\u00b2 + "

        if(param_B == 1):
            label = label + "x + "
        elif(param_B == 0):
            pass
        else:
            label = label + str(param_B) + "x + "

        if(param_B == 0):
            pass
        else:
            label = label + str(param_B)

        return label
