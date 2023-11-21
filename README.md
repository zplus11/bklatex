# Bookkeeping-LaTeX [W-I-P]
This repository contains a basic program to typeset accounting journals and ledgers using LaTeX and some programming with Python.

⚠️ To run this program, you need to have the following installed:
- a LaTeX distribution with pdflatex. See [MiKTeX](https://miktex.org/)
- Python. See [Python](https://www.python.org/)
 - `json` module in Python. Install using `pip install json` in console.
 - `pandas` module in Python. Install using `pip install pandas` in console.

## Program
Bookkeeping-LaTeX helps typeset accounting journals and ledgers using LaTeX and some programming. Rather than typesetting them yourself, you can run the `processor.py` file which will start a menu-driven program, and create a new project (or open previous). Using the program you can create a database for your accountancy entries, which is stored in a `json` file.

This `json` file is then used by Python to iterate and appropriately print journal and ledger commands in LaTeX, in manners pre-defined in `preamble.tex`. Using this preamble, LaTeX compiles the pdf for your entries.

## Illustration
A project is available as illustration in the `illustration` directory. Open it to find `illustration_entries.json` where all the entries are stored. TeX files for Journal and ledger commands are what Python creates from scratch using looping. The final product of this project is available in `illustration_main.pdf`.

⚠️ Keep in mind this is still a work in progress. In particular, printing ledgers needs more work.

Thank you for reading this far.