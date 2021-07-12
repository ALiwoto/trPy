#!/usr/bin/env python
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="anilistWrapPY",
    version="0.0.1",
    description="Unofficial Anilist.co API Wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="The Unlicense",
    author="Dank-del",
    author_email="sayan@pokurt.me",
    url="https://github.com/Dank-del/anilistWrapPY",
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3.8",
    ],
    package_dir={"": "src"},
    install_requires=["httpx>=0.18.2"],
    python_requires=">=3.7",
)