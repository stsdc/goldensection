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
import headerbar as hb
import stack as sk

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class Window(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title=cn.App.application_name)

        hbar = hb.Headerbar()
        self.set_titlebar(hbar)

        self.stack = sk.Stack(self)
        hbar.func_parameters = self.stack.new_search.func_parameters
        hbar.algo_parameters = self.stack.new_search.algo_parameters
        self.add(self.stack)
