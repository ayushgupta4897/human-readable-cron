"""
Setup script for human-readable-cron.
This file is kept for backwards compatibility with older tools.
For modern Python packaging, see pyproject.toml.
"""

from setuptools import setup, find_packages

# This setup.py is kept for backwards compatibility
# The actual configuration is in pyproject.toml
setup(
    name="human-readable-cron",
    version="0.1.0",
    author="Aayush Gupta",
    author_email="ayushgupta4897@gmail.com",
    description="A lightweight utility for converting human-readable schedules to cron expressions",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ayushgupta4897/human-readable-cron",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "human-readable-cron=human_readable_cron.cli:main",
        ],
    },
)
