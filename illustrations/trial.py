from bklatex import *

# Make a document
doc = Document(name = "trial")

with doc.append(Journal()) as journal:
    # Add an entry to journal
    journal.entry(
        date = "1 Apr",
        debit_accounts = ["Cash"],
        credit_accounts = ["Capital"],
        debit_amounts = [100000],
        credit_amounts = [100000],
        debit_folios = [1],
        credit_folios = [2],
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
    # Print .tex for journal
    journal.print_tex("journal")

# Print .tex
doc.print(tex=True,pdf=True)
