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
    debit_amounts = [200000],
    credit_amounts = [200000],
    debit_folios = ["3"],
    credit_folios = ["4"],
    narration = "being cash deposited into bank"
)
dec.entry(
    "30",
    ["Furniture", "Computers", "Purchases"],
    ["Bank"],
    [20000, 10000, 20000],
    [50000],
    narration = "being furniture, computers and stock purchased"
)

jan = month(acc, "January", "2024")
jan.entry(
    "1",
    ["Cash", "Bank"],
    ["Sales"],
    [30000, 120000],
    [150000],
    ["9", "10"],
    ["11"],
    "being sales made to bank and cash"
)
    
acc.make_pdf(keep_tex = True)
