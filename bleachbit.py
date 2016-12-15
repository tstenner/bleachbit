#!/usr/bin/env python
# vim: ts=4:sw=4:expandtab

# BleachBit
# Copyright (C) 2008-2016 Andrew Ziem
# https://www.bleachbit.org
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from __future__ import print_function

"""
Launcher
"""


import os
import sys

if 'nt' == os.name:
    from bleachbit.Windows import setup_environment
    setup_environment()

from bleachbit.GUI import Bleachbit

if 'posix' == os.name and os.path.isdir('/usr/share/bleachbit'):
    # This path contains bleachbit/{C,G}LI.py .  This section is
    # unnecessary if installing BleachBit in site-packages.
    sys.path.append('/usr/share/')

if 1 == len(sys.argv):
    app = Bleachbit()
    exit_status = app.run(sys.argv)
    sys.exit(exit_status)
else:
    import bleachbit.CLI
    bleachbit.CLI.process_cmd_line()
