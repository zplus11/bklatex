import sys
sys.path.append("D:\\python\\accountancy\\bklatex")

from bklatex import *

acc = account(file_name = "illustration", company_name = "That Company Pvt. Ltd.", year = "2024")

dec = month(acc, "December", "2023")
dec.entry(
    date = "29",
    debit_accounts = ["Cash"],
    credit_accounts = ["Capital"],
    debit_amounts = [500000],
    credit_amounts = [500000],
    debit_folios = ["1"],
    credit_folios = ["2"],
    narration = "being capital introduced"
)
dec.entry(
    date = "29",
    debit_accounts = ["Bank"],
    credit_accounts = ["Cash"],
    debit_amounts = [100000],
    credit_amounts = [100000],
    debit_folios = ["3"],
    credit_folios = ["4"],
    narration = "being cash deposited into bank"
)
dec.entry(
    date = "29",
    debit_accounts = ["Furniture"],
    credit_accounts = ["Cash"],
    debit_amounts = [50000],
    credit_amounts = [50000],
    debit_folios = ["5"],
    credit_folios = ["6"],
    narration = "being furniture bought"
)
jan = month(acc, "January", "2024")
jan.entry(
    date = "5",
    debit_accounts = ["Cash"],
    credit_accounts = ["Bank"],
    debit_amounts = [50000],
    credit_amounts = [50000],
    debit_folios = ["7"],
    credit_folios = ["8"],
    narration = "being cash withdrawn from bank"
)

acc.make_pdf(keep_tex = True)
