from setuptools import setup, find_packages

setup(
    name="bin-txt-tools",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "bin-txt-tools=bin_txt_tools.main:main",
        ],
    },
    author="Gustavo",
    description="An open-source CLI suite for binary, text, and pixel art manipulation.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/gustavodavidecoutinho/bin-txt-tools",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
