import setuptools

setuptools.setup(
    name = "bklatex",
    version = "0.0.2",
    author = "Naman Taggar",
    description = "Typeset accounting journals and ledgers with Python & LaTeX",
    long_description = open("README.md").read(),
    long_description_content_type = "text/markdown",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Windows",
    ],
    python_requires = ">3.5",
    py_modules = ["bklatex"],
    include_package_data = True,
)
