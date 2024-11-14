from setuptools import setup, find_packages

setup(
    name="python-bitget",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "websockets",
        "python-dateutil",
        "ujson"
    ],
    author="WanBlave",
    description="Python Bitget API wrapper",
    url="https://github.com/WanBlave/python-bitget",
)
