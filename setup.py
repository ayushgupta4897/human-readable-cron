"""
Setup script for human-readable-cron.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="human-readable-cron",
    version="0.1.0",
    author="Aayush Gupta",
    author_email="your.email@example.com",
    description="A lightweight utility for converting human-readable schedules to cron expressions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/human-readable-cron",
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
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
    keywords="cron, schedule, time, parser, utility",
)
