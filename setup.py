from setuptools import setup, find_packages

setup(
    name="langchain",
    version="0.1",
    author="Prashant",
    author_email="vprashant5050@gmail.com",
    description="Modified version of langchain that fix the bug of langchain agent tool",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/vprashrex/chainlang.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
