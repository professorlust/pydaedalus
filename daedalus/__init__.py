#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
__init__.py
(c) Will Roberts  26 February, 2017

daedalus module.
'''

from __future__ import absolute_import
from codecs import open
from os import path

# Version. For each new release, the version number should be updated
# in the file VERSION.
try:
    # If a VERSION file exists, use it!
    with open(path.join(path.dirname(__file__), 'VERSION'),
              encoding='utf-8') as infile:
        __version__ = infile.read().strip()
except NameError:
    __version__ = 'unknown (running code interactively?)'
except IOError as ex:
    __version__ = "unknown (%s)" % ex

from ._maze import (Maze,
                    COLOR_WHITE, COLOR_BLACK,
                    ENTRANCE_CORNER, ENTRANCE_MIDDLE, ENTRANCE_BALANCED, ENTRANCE_RANDOM)
