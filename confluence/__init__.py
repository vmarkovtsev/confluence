#!/usr/bin/env python
# Licensed to PSF under a Contributor Agreement.
# See http://www.python.org/psf/license for licensing details.

__author__ = "Vadim Markovtsev"
__copyright__ = "2015, Samsung Electronics Co.,Ltd."
__email__ = "v.markovtsev@samsung.com"
__status__ = "Beta"
from .version import __version__, __date__

from .confluence import Confluence

__all__ = ['confluence']

"""
Tendo is tested with Python 2.6-3.2
"""

import sys
if sys.hexversion < 0x02070000:
    sys.exit("Python 2.7 or newer is required by confluence module.")
