import sys

from distutils.core import setup

if sys.version_info >= (3, 0):
    try:
        from distutils.command.build_py import build_py_2to3 as build_py
        from distutils.command.build_scripts import build_scripts_2to3 as build_scripts
    except ImportError:
        raise ImportError("build_py_2to3 not found in distutils - it is required for Python 3.x")
    suffix = "-py3k"
else:
    from distutils.command.build_py import build_py
    from distutils.command.build_scripts import build_scripts
    suffix = ""


if sys.version < '2.3':
    # distutils that old can't cope with the "classifiers" or "download_url"
    # keywords and True/False constants and basestring are missing
    raise ValueError("Sorry Python versions older than 2.3 are no longer"
                     "supported - check http://pyserial.sf.net for older "
                     "releases or upgrade your Python installation.")

# importing version does not work with Python 3 as files have not yet been
# converted.
#~ import serial
#~ version = serial.VERSION

import re, os
version = re.search(
        "VERSION.*'(.+)'",
        open(os.path.join('pyBusPirateLite', '__init__.py')).read()).group(1)

setup(name='pyBusPirateLite' + suffix,
      version=version,
      description='Python BusPirate',
      author='Sean Nelson',
      author_email='audiohacked@gmail.com',
      url='',
      packages=['pyBusPirateLite'],
     )