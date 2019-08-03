#!/usr/bin/env python3

import setuptools

version = "1.0.0"
readme_file = "README.md"

with open(readme_file, "r") as f:
    long_description = f.read()

setuptools.setup(
    name="import_times",
    version=version,
    description="Print import times to stderr in 3.7 style",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/banool/import_times",
    license="MIT",
    author="banool",
    author_email="danielporteous1@gmail.com",
    packages=setuptools.find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
