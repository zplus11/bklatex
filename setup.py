import setuptools

setuptools.setup(
    name = "bklatex",
    version = "0.1.0",
    author = "Naman Taggar",
    description = "Typeset accounting journals and ledgers with Python & LaTeX",
    long_description = open("README.md").read(),
    long_description_content_type = "text/markdown",
    packages = ["bklatex"],
    modules = ["account"],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows",
    ],
    python_requires = ">3.5",
    include_package_data = True
)
