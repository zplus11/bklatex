import pandas as pd

journals_data = [
    ['2023'],
    ['1 march', ['cash', 'machinery', 'furniture'], ['capital', 'creditors'], [100000, 30000, 10000], [130000, 10000], ['1', '2', '3'], ['4', '5'], 'being cash, machinery and furniture introduced'],
    ['1 march', ['purchases'], ['cash'], [16000], [16000], ['6'], ['7'], 'being goods purchased'],
    ['1 march', ['purchases'], ['cash'], [17000], [17000], ['8'], ['9'], 'being goods purchased'],
    ['2 march', ['purchases'], ['amit'], [24000], [24000], ['10'], ['11'], 'being goods purchased on credit'],
    ['5 march', ['purchases'], ['cash'], [35000], [35000], ['12'], ['13'], 'being goods purchased'],
    ['10 march', ['amit'], ['purchase returns'], [8000], [8000], ['14'], ['15'], 'being goods returned by Amit'],
    ['11 march', ['bank'], ['sales'], [36000], [36000], ['16'], ['17'], 'being goods sold and bank increased'],
    ['13 march', ['cash'], ['sales'], [27000], [27000], ['18'], ['19'], 'being goods sold'],
    ['15 march', ['pawan'], ['sales'], [18000], [18000], ['20'], ['21'], 'being goods sold on credit'],
    ['19 march', ['yamini'], ['sales'], [23000], [23000], ['22'], ['23'], 'being goods sold on credit'],
    ['22 march', ['bhupesh'], ['cash'], [10800], [10800], ['24'], ['25'], 'being payment made to Bhupesh'],
    ['23 march', ['bank'], ['sales'], [47000], [47000], ['26'], ['27'], 'being goods sold and bank increased'],
    ['23 march', ['sales returns'], ['aman'], [9000], [9000], ['28'], ['29'], 'being goods returned by Aman']
]

journals = pd.DataFrame(journals_data, columns = ["date", "dr acc", "cr acc", "dr", "cr", "djf", "cjf", "narrations"])

accounts_temp = set()
for entry in journals_data:
    if len(entry) > 1:
        for i in range(len(entry[1])):
            dr_account = entry[1][i]
            accounts_temp.add(dr_account)
        for i in range(len(entry[2])):  
            cr_account = entry[2][i]
            accounts_temp.add(cr_account)

unique_accounts = list(accounts_temp)

accounts = {}
for account in unique_accounts:
    accounts[account] = {"debit": [], "credit": []}
    
for account in list(accounts.keys()):
    for entry in journals_data:
        if len(entry) == 1:
            accounts[account]["debit"].append(entry)
            accounts[account]["credit"].append(entry)
        else:
            for i in range(len(entry[1])):
                if account == entry[1][i]:
                    accounts[account]["debit"].append([entry[0], entry[2], entry[3][i], entry[5]])
            for i in range(len(entry[2])):
                if account == entry[2][i]:
                    accounts[account]["credit"].append([entry[0], entry[1], entry[4][i], entry[6]])
print(accounts)

journal_commands = "%%%%%%%%%%%%%%%%%%%%%%\n% JOURNAL ENTRIES\n%%%%%%%%%%%%%%%%%%%%%%\n\n\journal{\n\n"

for entry in journals_data:
    if len(entry) == 1:
        journal_commands = journal_commands + f"\t\jyear{{{entry[0]}}}\n\n"
    else:
        journal_commands = journal_commands + f"\t\jdr{{{entry[0].title()}}}{{{entry[1][0].title()}}}{{{entry[5][0]}}}{{{entry[3][0]}}}\n"
        if len(entry[1]) > 1:
            for i in range(1, len(entry[1])):
                journal_commands = journal_commands + f"\t\jdr{{}}{{{entry[1][i].title()}}}{{{entry[5][i]}}}{{{entry[3][i]}}}\n"
        journal_commands = journal_commands + f"\t\jcr{{{entry[2][0].title()}}}{{{entry[6][0]}}}{{{entry[4][0]}}}\n"
        if len(entry[2]) > 1:
            for i in range(1, len(entry[2])):
                journal_commands = journal_commands + f"\t\jcr{{{entry[2][i].title()}}}{{{entry[6][i]}}}{{{entry[4][i]}}}\n"
        journal_commands = journal_commands + f"\t\jnar{{{entry[7]}}}\n\n"
journal_commands = journal_commands + "}"

{'debit': [['1 march', ['capital', 'creditors'], 100000, ['1', '2', '3'], ['4', '5']], ['13 march', ['sales'], 27000, ['18'], ['19']]], 'credit': [['1 march', ['purchases'], 16000, ['6'], ['7']], ['1 march', ['purchases'], 17000, ['8'], ['9']], ['5 march', ['purchases'], 35000, ['12'], ['13']], ['22 march', ['bhupesh'], 10800, ['24'], ['25']]]}

ledger_commands = "%%%%%%%%%%%%%%%%%%%%%%\n% LEDGER ENTRIES\n%%%%%%%%%%%%%%%%%%%%%%\n\n"

for account in accounts.keys():
    ld = len(accounts[account]["debit"])
    lc = len(accounts[account]["credit"])
    ledger_commands = ledger_commands + f"% {account.upper()} ACCOUNT \n"
    ledger_commands = ledger_commands + f"\ledger{{{account.title()} a/c}}{{\n"
    for entry in accounts[account]["debit"]:
        if len(entry) == 1:
            ledger_commands = ledger_commands + f"\t\lyear{{{entry[0]}}}\n"
        else:
            ledger_commands = ledger_commands + f"\t\ldr{{{entry[0].title()}}}{{{entry[1][0].title()}}}{{{entry[2]}}}{{{entry[3][0]}}}\n"
    if ld < lc:
        ledger_commands = ledger_commands + "\t"
        for i in range(lc - ld):
            ledger_commands = ledger_commands + "\mt"
        ledger_commands = ledger_commands + "\n"
    ledger_commands = ledger_commands + "\t\mt\n}{\n"
    for entry in accounts[account]["credit"]:
        if len(entry) == 1:
            ledger_commands = ledger_commands + f"\t\lyear{{{entry[0]}}}\n"
        else:
            ledger_commands = ledger_commands + f"\t\lcr{{{entry[0].title()}}}{{{entry[1][0].title()}}}{{{entry[2]}}}{{{entry[3][0]}}}\n"
    if lc < ld:
        ledger_commands = ledger_commands + "\t"
        for i in range(ld - lc):
            ledger_commands = ledger_commands + "\mt"
        ledger_commands = ledger_commands + "\n"
    ledger_commands = ledger_commands + "\t\mt\n}\n\n"
    
"""print("Below enter the name you want the file to have. For example, if you enter ""example"", then the files will be created with names ""example_journal.tex"" and ""example_ledger.tex"" ")"""
choice = "illustration" #input("Enter your desired name: ")
print(f"Okay, the files are saved in the name of {choice}_journal.tex and {choice}_ledger.tex. Find them in the directory of this file.")

with open(f"{choice}_journal.tex", "w") as file:
    file.write(journal_commands)
with open(f"{choice}_ledger.tex", "w") as file:
    file.write(ledger_commands)
