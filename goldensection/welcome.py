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
import subprocess
import gi
import os
import locale
import gettext
gi.require_version('Gtk', '3.0')
gi.require_version('Granite', '1.0')
from gi.repository import Gtk, Gdk, Granite
import webbrowser

class Welcome(Gtk.Box):

    # Define variable for GTK global theme
    settings = Gtk.Settings.get_default()

    def __init__(self):
        Gtk.Box.__init__(self, False, 0)

        try:
            current_locale, encoding = locale.getdefaultlocale()
            locale_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
            translate = gettext.translation (cn.App.application_shortname, locale_path, [current_locale] )
            _ = translate.gettext
        except FileNotFoundError:
            _ = str

        # Create welcome widget
        welcome = Granite.WidgetsWelcome()
        welcome = welcome.new("Welcome", cn.App.application_description)

        # Welcome voices
        welcome.append("object-inverse", _('Find min of function'), _('Use Golden Section Algorithm'))
        welcome.append("help-contents", _('What is the Golden Section Algorithm'), _('Learn more about this algorithm'))

        welcome.connect("activated", self.on_welcome_activated)

        self.add(welcome)

    def on_welcome_activated(self, widget, index):
        if index == 0:
            # Use GTK Dark theme
            print("Start plot window etc")
        elif index == 1:
            # Open webpage
            webbrowser.open_new_tab("https://en.wikipedia.org/wiki/Golden-section_search")
        print("Index: "+str(index))
