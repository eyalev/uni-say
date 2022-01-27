# -*- coding: utf-8 -*-
from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

packages = ["uni_say"]

package_data = {"": ["*"]}

install_requires = ["click>=8.0.3,<9.0.0"]

entry_points = {"console_scripts": ["uni-say = uni_say.cli:cli"]}

setup_kwargs = {
    "name": "uni-say",
    "version": "0.1.4",
    "description": "",
    "author": "Eyal Levin",
    "author_email": "eyalev@gmail.com",
    "maintainer": None,
    "maintainer_email": None,
    "url": None,
    "packages": packages,
    "package_data": package_data,
    "install_requires": install_requires,
    "entry_points": entry_points,
    "python_requires": ">=3.10,<4.0",
    "long_description": "long_description",
    "long_description_content_type": "text/markdown",
}


setup(**setup_kwargs)
