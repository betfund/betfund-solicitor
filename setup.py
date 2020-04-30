"""A setuptools based setup module."""
from os import path
from setuptools import setup, find_packages
from io import open

with open( "README.md") as f:
    long_description = f.read()

setup(
    name="betfund_solicitor",
    version="0.0.1",
    description="Line voting solicitor for Betfund",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/betfund/betfund-solicitor",
    author="Michell Bregman, Leon Kozlowski",
    author_email="mitchbregs@gmail.com, leonkozlowski@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    keywords="betfund",
    packages=find_packages(),
    install_requires=[
        "betfund_logger @ git+https://github.com/betfund/betfund-logger.git@0.0.3",
        "boto3",
        "jsonschema",
        "sendgrid"
    ],
    tests_require=[
        "black",
        "pylint",
        "pytest",
        "pytest-cov"
    ]
)