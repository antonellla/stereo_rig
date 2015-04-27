"""
File: setup.py
Author: Yifei Zhang
Email: njzhangyifei@gmail.com
Github: https://github.com/njzhangyifei
Description: setup file for the package
"""

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

setup_args = generate_distutils_setup(
    packages=['stereo_param_configure'],
    package_dir={'':'src'},
)

setup(**setup_args)
