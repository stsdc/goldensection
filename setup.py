#!/usr/bin/python3

import glob, os
from distutils.core import setup

install_data = [('share/applications', ['data/com.github.stsdc.goldensection.desktop']),
                ('share/metainfo', ['data/com.github.stsdc.goldensection.appdata.xml']),
                ('share/icons/hicolor/128x128/apps',['data/com.github.stsdc.goldensection.svg']),
                ('bin/goldensection',['goldensection/constants.py']),
                ('bin/goldensection',['goldensection/headerbar.py']),
                ('bin/goldensection',['goldensection/main.py']),
                ('bin/goldensection',['goldensection/welcome.py']),
                ('bin/goldensection',['goldensection/window.py']),
                ('bin/goldensection',['goldensection/__init__.py']),
                ('bin/goldensection/locale/it_IT/LC_MESSAGES',
                    ['goldensection/locale/it_IT/LC_MESSAGES/goldensection.mo']),
                ('bin/goldensection/locale/it_IT/LC_MESSAGES',
                    ['goldensection/locale/it_IT/LC_MESSAGES/goldensection.po'])]

setup(  name='Golden Section Algorithm',
        version='0.0.1',
        author='Stanisław Dac',
        description='Display result of Golden Section Algorithm',
        url='https://github.com/stsdc/goldensection',
        license='GNU GPL3',
        scripts=['com.github.stsdc.goldensection'],
        packages=['goldensection'],
        data_files=install_data)
