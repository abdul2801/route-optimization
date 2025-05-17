from setuptools import setup, find_packages
setup(
    name="route-optimizer-pro",
    version="0.1.0",
    packages=find_packages(where="."),
    install_requires=open("requirements.txt").read().splitlines(),
)