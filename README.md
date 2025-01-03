# bklatex

Copyright (c) 2024-25 Naman Taggar

Typeset books of account with LaTeX easily using this python library.

`[!]` To run this program, you need to have the following installed:
- a LaTeX distribution with `pdflatex`. See [MiKTeX](https://miktex.org/)
- Python. See [Python](https://www.python.org/)

## Program
`bklatex` helps typeset accounting journals and ledgers using LaTeX and some programming. Rather than typesetting them yourself, you can use the classes and methods defined and use python to do it for you. Python will print the `*.tex` files using automated processes and compile them to fabricate `.pdf` files.

## Installation
To install the package, run

```
pip install git+"https://github.com/zplus11/bklatex"
```

## Usage

Type the following contents in any python file, say `trial.py`:

```py
from bklatex import *

# Make a document
doc = Document(name = "trial")

# Start adding accounts to this document
with doc.append(Journal()) as journal:
	
	# Add an entry to journal
	journal.entry(
		date = "1 Apr",
		debit_accounts = ["Cash"],
		credit_accounts = ["Capital"],
		debit_amounts = [100000],
		credit_amounts = [100000],
		debit_folios = [1],
		credit_folios = [1],
		narration = "being capital introduced"
	)
	
	# Or do so in a compact manner
	journal.entry(
		"2 Apr",
		["Purchases"],
		["Cash"],
		[10000],
		[10000],
		# Absense of folio fields is acceptable and will not invite errors
		narration = "being purchases made by cash"
	)

# Print PDF
doc.print(pdf=True)
```

This will print the PDF file for this document (see [illustrations/trial.pdf](illustrations/trial.pdf)). A `.tex` file can also be printed using

```py
doc.print(pdf=True, tex=True)
```

which will output a file that includes this:

```tex
\documentclass{article}
\usepackage[smallmargins]{E:/installs/Python/Lib/site-packages/bklatex/accountancy}
\begin{document}
\journal{
\jdr{1 Apr}{Cash}{1}{100000}
\jcr{Capital}{2}{100000}
\jnar{being capital introduced}
\jdr{2 Apr}{Purchases}{}{10000}
\jcr{Cash}{}{10000}
\jnar{being purchases made by cash}
}
\end{document}
```

Moreover, `.tex` files for single accounts (such as journal above) can also be printed by typing:

```py
with doc.append(Journal()) as journal:
	...
	journal.print_tex(name = "journal"))
```

## Illustrations
The above mentioned example and probably more illustrations are given in the `illustrations` directory.

`[!]` Keep in mind this is still a work in progress. A lot of things are to be added.


Thank you for reading this far.