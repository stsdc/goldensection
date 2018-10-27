#!/usr/bin/python3
'''
   Copyright 2017 Mirko Brombin (brombinmirko@gmail.com)

   This file is part of Bottles.

    Bottles is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    Bottles is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with Bottles.  If not, see <http://www.gnu.org/licenses/>.
'''

import gi
import os
import locale
import gettext
import webbrowser
gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')
from gi.repository import Gtk, Gdk, Granite, GdkPixbuf
try:
    import constants as cn
    from matplotlib.backends.backend_gtk3agg import (FigureCanvasGTK3Agg as FigureCanvas)
    from matplotlib.figure import Figure
    import numpy as np
except ImportError:
    import bottles.constants as cn

class NewSearch(Gtk.Box):
    status = False

    def __init__(self, parent):
        Gtk.Box.__init__(self, False, 0)
        self.parent = parent

        try:
            current_locale, encoding = locale.getdefaultlocale()
            locale_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
            translate = gettext.translation (cn.App.application_shortname, locale_path, [current_locale] )
            _ = translate.gettext
        except FileNotFoundError:
            _ = str

        self.set_border_width(1)

        # f = Figure(figsize=(5, 4), dpi=100)
        # a = f.add_subplot(111)
        # t = np.arange(0.0, 3.0, 0.01)
        # s = np.sin(2*np.pi*t)
        # a.plot(t, s)
        #
        # sw = Gtk.ScrolledWindow()
        # self.add(sw)
        # # A scrolled window border goes outside the scrollbars and viewport
        # canvas = FigureCanvas(f)  # a Gtk.DrawingArea
        # canvas.set_size_request(800, 600)
        # sw.add_with_viewport(canvas)
        # self.grid = grid = Gtk.Grid()

        hpaned = Gtk.Paned()
        hpaned.set_position(300)

        label = Gtk.Label(label="Left Pane")
        hpaned.add1(label)

        label = Gtk.Label(label="Right Pane")
        hpaned.add2(label)

        self.pack_start(hpaned, True, True, 0)
