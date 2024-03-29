# bklatex
Typeset accounting journals and ledgers with LaTeX easily using this python library.

`[!]` To run this program, you need to have the following installed:
- a LaTeX distribution with `pdflatex`. See [MiKTeX](https://miktex.org/)
- Python. See [Python](https://www.python.org/)

## Program
bklatex helps typeset accounting journals and ledgers using LaTeX and some programming. Rather than typesetting them yourself, you can use the classes and methods defined and use python to do it for you. Python will fabricate the TeX files by an automated process and compile them to create a Portable Document Format file.

## Installation
To install the package, run

```
pip install git+"https://github.com/zplus11/bklatex"
```

## Usage
Open your console in the desired directory, start python:

```
D:\python\accountancy\illustrations>python
Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
```

and import the package:

```
>>> from bklatex import *
This is bklatex v0.0.3
```

Now, begin an account:

```
>>> acc = account(file_name = "my_account", company_name = "Some Company Pvt. Ltd.", year = "2024") # for the year ending 2024
Account initiated with file name my_account
```

At this point, you are able to begin a month in this account and start adding entries:

```
>>> with acc.month("April", "2024") as apr:
...     apr.entry(
...     date = "01",
...     debit_accounts = ["Cash"],
...     credit_accounts = ["Capital"],
...     debit_amounts = [1000000],
...     credit_amounts = [1000000],
...     debit_folios = ["1"],
...     credit_folios = ["2"],
...     narration = "being capital introduced to business"
...     )
...
Created month April in the accounts
Recorded entry: By ['Cash'] ([1000000]); To ['Capital'] ([1000000])
```

or, do so in a compact manner:

```
>>> with acc.month("May", "2024") as may:
...     may.entry("05", ["Bank"], ["Cash"], [55000], [55000], narration = "being cash deposited to bank")
...
Created month May in the accounts
Recorded entry: By ['Bank'] ([55000]); To ['Cash'] ([55000])
```

Absence of folio numbers is acceptable and will not invite errors.

Finally, once you are satisfied, you can compile a pdf for your account `acc`:

```
>>> acc.make_pdf(keep_tex = True, journals = True, ledgers = True)
Compiler activated
[O]
[J] Printed 2 entries in the journal
[L] Printed 3 accounts in the ledger
[C]
[F] Calling pdflatex...
This is pdfTeX, Version 3.141592653-2.6-1.40.25 (MiKTeX 23.10) (preloaded format=pdflatex.fmt)
...
Transcript written on my_account.log.
Auxiliary files are removed
```

Auxiliary files are definitely removed and this can not be changed. Default values for above booleans are `keep_tex = True`, `journals = True`, `ledgers = True`.

After the compilation process has completed, you will receive two files: `my_account.tex` and `my_account.pdf`. `my_account.tex` will contain the TeX script that is used to compile `my_account.pdf`. The TeX file will look like this:

`my_account.tex`

```
% This is my_account.tex printed using https://github.com/zplus11/bklatex.git

\documentclass{article}
\usepackage[smallmargins]{E:/installs/Python/Lib/site-packages/bklatex/accountancy}
\begin{document}
	

	%%%%%%%%%%%%%%%%%%%%%%
	% JOURNAL ENTRIES
	%%%%%%%%%%%%%%%%%%%%%%

	\journal{Some Company Pvt. Ltd.}{2024}{
		\jyear{2024}
		\jdr{01 Apr}{Cash}{1}{1000000}
		\jcr{Capital}{2}{1000000}
		\jnar{being capital introduced to business}
		\jdr{05 May}{Bank}{}{55000}
		\jcr{Cash}{}{55000}
		\jnar{being cash deposited to bank}
	}

<<<...>>>

\end{document}
% End of my_account.tex
```

## Illustrations
The above mentioned example and a bigger illustration are both given in the `illustrations` directory.

`[!]` Keep in mind this is still a work in progress. In particular, printing ledgers needs more work.

## Version Tracker

**0.0.1:** Initial distributable (while not complete) release.

**0.0.2:** Changed `preamble.tex` into `accountancy.sty` usable as a standalone package.

**0.1.0:** Made entry class; some QoL changes like better logging.

Thank you for reading this far.