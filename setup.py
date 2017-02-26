"""
Setup module
"""

from setuptools import setup, find_packages


setup(
    name="eagle_http",
    version="1.0.0",
    author="Rainforest Automation",
    packages=find_packages(),
    install_requires=["lxml>=3.4.2"]
)
