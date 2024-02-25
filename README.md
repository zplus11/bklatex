# bklatex
Typeset accounting journals and ledgers with LaTeX easily using this python library.

`[ ! ]` To run this program, you need to have the following installed:
- a LaTeX distribution with `pdflatex`. See [MiKTeX](https://miktex.org/)
- Python. See [Python](https://www.python.org/)

## Program
bklatex helps typeset accounting journals and ledgers using LaTeX and some programming. Rather than typesetting them yourself, you can use the classes and methods defined and create a Python script to easily have them typeset by Python.

## Installation
To install the package, run

```
pip install git+"https://github.com/zplus11/bklatex"
```

## Usage
Import the package in your python file, then begin a new account and start a month:

```
from bklatex import *

acc = account(file_name = "my_account", company_name = "Some Company Pvt. Ltd.", year = "2024") # for the year ending 2024
apr = month(acc, "April", "2023") # april month in acc account, for year 2023
```

Record entries in the month:

```
apr.entry(
	date = "01",
	debit_accounts = ["Cash"],
	credit_accounts = ["Capital"],
	debit_amounts = [1000000],
	credit_amounts = [1000000],
	debit_folios = ["1"],
	credit_folios = ["2"],
	narration = "being capital introduced to business"
) # records the entry in April month database
```

Start a new month and add another entry in the same way:

```
may = month(acc, "March", "2023")
may.entry("05", ["Bank"], ["Cash"], [55000], [55000], narration = "being cash deposited to bank")
```

Compile a pdf for this account:

```
acc.make_pdf(keep_tex = True, journals = True, ledgers = True)
```

default values for above booleans are `keep_tex = False`, `journals = True`, `ledgers = False`.

## Illustration
A bigger illustration is given in `illustrations` directory.

`[ ! ]` Keep in mind this is still a work in progress. In particular, printing ledgers needs more work.

## Version Tracker

**0.0.1:** Initial distributable (while not complete) release.

**0.0.2:** Changed `preamble.tex` into `accountancy.sty` usable as a standalone package.

Thank you for reading this far.