from setuptools import setup, find_packages

setup(
    name="commons",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pymongo>=4.6.0",
        "python-dotenv",
    ],
    author="Satvik Tejas",
    description="Common utilities for ChatKart AI",
    license="MIT",
    url="https://github.com/satvik-1945/commons",
    python_requires=">=3.8",
)