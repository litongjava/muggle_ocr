#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author: kerlomz <kerlomz@gmail.com>


#############################################
# File Name: setup.py
# Created Time:  2020-6-1 00:00:00
#############################################

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

data_files = [
    "muggle_ocr/ocr.pb",
    "muggle_ocr/ocr.yaml",
    "muggle_ocr/captcha.pb",
    "muggle_ocr/captcha.yaml"
]

setup(
    name="muggle-ocr",
    version="1.0.3",
    keywords=["pip", "muggle-ocr"],
    description="Take you on the free OCR bus.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT Licence",
    url="https://github.com/kerlomz/captcha_trainer",
    author="kerlomz",
    author_email="kerlomz@gmail.com",

    packages=find_packages(),
    py_modules=["muggle_ocr"],
    data_files=data_files,
    include_package_data=True,
    platforms="any",
    python_requires='>=3.6',
    install_requires=["tensorflow>=1.14", "numpy", "pillow", "opencv-python", "pyyaml"]
)
