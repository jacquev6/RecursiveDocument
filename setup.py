#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2013 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of RecursiveDocument. http://jacquev6.github.com/RecursiveDocument

# RecursiveDocument is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# RecursiveDocument is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with RecursiveDocument.  If not, see <http://www.gnu.org/licenses/>.

import setuptools
import textwrap
import subprocess
import shutil
import os.path

version = "0.1.0"


if __name__ == "__main__":
    setuptools.setup(
        name="RecursiveDocument",
        version=version,
        description="",
        author="Vincent Jacques",
        author_email="vincent@vincent-jacques.net",
        url="http://jacquev6.github.com/RecursiveDocument",
        long_description=textwrap.dedent("""\
            Reference documentation
            =======================

            See http://jacquev6.github.com/RecursiveDocument"""),
        packages=[
            "recdoc",
            "recdoc.tests",
        ],
        package_data={
            "recdoc": ["ReadMe.rst", "COPYING*"],
        },
        classifiers=[
            "Development Status :: 1 - Planning",
            "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
        ],
        test_suite="recdoc.tests.AllTests",
        use_2to3=True
    )
