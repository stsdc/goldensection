#!/usr/bin/python3
'''
   Copyright 2017 Mirko Brombin (brombinmirko@gmail.com)

   This file is part of goldensection.

    goldensection is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    goldensection is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with goldensection.  If not, see <http://www.gnu.org/licenses/>.
'''

import constants as cn
import gi
import webbrowser
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class Headerbar(Gtk.HeaderBar):

    def __init__(self):

        Gtk.HeaderBar.__init__(self)

        self.parameters = None
        self.set_show_close_button(True)
        self.props.title = cn.App.application_name

        # color button
        self.hbar_color = Gtk.ColorButton.new_with_rgba(Gdk.RGBA(0.9294117647058824, 0.8313725490196079, 0.0, 1))
        print("Default color", self.hbar_color.get_rgba().to_string())
        self.hbar_color.connect("color_set", self.on_hbar_color_color_set)
        self.pack_end(self.hbar_color)

        self.switch = Gtk.Switch()
        self.switch.connect("notify::active", self.on_switch_activated)
        self.switch.set_active(False)
        self.switch.set_tooltip_text("Enable step-by-step mode")
        self.pack_end(self.switch)

        self.next_step_button = Gtk.Button.new_with_label("Next step")
        self.next_step_button.connect("clicked", self.on_next_step_button_clicked)
        self.pack_end(self.next_step_button)
        self.next_step_button.set_sensitive(False)



    def on_hbar_color_color_set(self, widget):
        print("Color change", widget.get_rgba().to_string())
        red = widget.get_rgba().red
        green = widget.get_rgba().green
        blue = widget.get_rgba().blue
        print (red, green, blue)
        self.parameters.chart.color = (red, green, blue)
        self.parameters.recalculate()

    def on_switch_activated(self, switch, gparam):
        if switch.get_active():
            self.next_step_button.set_sensitive(True)
        else:
            self.next_step_button.set_sensitive(False)

    def on_next_step_button_clicked(self, button):
        print('yay')
