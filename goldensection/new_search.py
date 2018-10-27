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
    import chart as ch
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
        chart = ch.Chart()
        hpaned = Gtk.Paned()
        hpaned.set_position(800)

        hpaned.add1(chart.sw)

        label = Gtk.Label(label="Right Pane")
        hpaned.add2(label)

        self.pack_start(hpaned, True, True, 0)

        print(parent.get_preferred_width())
