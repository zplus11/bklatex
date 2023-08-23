import pandas as pd

journals_data = [
    ['2023'],
    ['1 march', ['cash', 'machinery', 'furniture'], ['capital'], [100000, 30000, 10000], [140000], ['1', '2', '3'], 'being cash, machinery and furniture introduced'],
    ['1 march', ['purchases'], ['cash'], [16000], [16000], ['5'], 'being goods purchased'],
    ['1 march', ['purchases'], ['cash'], [17000], [17000], ['6'], 'being goods purchased'],
    ['2 march', ['purchases'], ['amit'], [24000], [24000], ['8'], 'being goods purchased on credit'],
    ['5 march', ['purchases'], ['cash'], [35000], [35000], ['9'], 'being goods purchased'],
    ['10 march', ['amit'], ['purchase returns'], [8000], [8000], ['10'], 'being goods returned by Amit'],
    ['11 march', ['bank'], ['sales'], [36000], [36000], ['12'], 'being goods sold and bank increased'],
    ['13 march', ['cash'], ['sales'], [27000], [27000], ['13'], 'being goods sold'],
    ['15 march', ['pawan'], ['sales'], [18000], [18000], ['14'], 'being goods sold on credit'],
    ['19 march', ['yamini'], ['sales'], [23000], [23000], ['35'], 'being goods sold on credit'],
    ['22 march', ['bhupesh'], ['cash'], [10800], [10800], ['36'], 'being payment made to Bhupesh'],
    ['23 march', ['bank'], ['sales'], [47000], [47000], ['37'], 'being goods sold and bank increased'],
    ['23 march', ['sales returns'], ['aman'], [9000], [9000], ['40'], 'being goods returned by Aman']
]

journals = pd.DataFrame(journals_data, columns = ["date", "dr acc", "cr acc", "dr", "cr", "jf", "narrations"])

accounts_temp = set()
for entry in journals_data[1:]:
    dr_account = entry[2][0]
    cr_account = entry[3][0]
    accounts_temp.add(dr_account)
    accounts_temp.add(cr_account)

unique_accounts = list(accounts_temp)

accounts = {}
for account in unique_accounts:
    accounts[account] = {'debit': [], 'credit': []}
    
for account in list(accounts.keys()):
    for entry in journals_data[1:]:
        if account == entry[1]:
            accounts[account]["debit"].append([entry[0], entry[2], entry[4], entry[5]])
    for entry in journals_data[1:]:
        if account == entry[2]:
            accounts[account]["credit"].append([entry[0], entry[1], entry[3], entry[5]])

print("Below enter the name you want the file to have. For example, if you enter ""example"", then the files will be created with names ""example_journal.tex"" and ""example_ledger.tex""")
choice = input("Enter your desired name: ")

journal_commands = "\journal{\n\n"
for entry in journals_data:
    if len(entry) == 1:
        journal_commands = journal_commands + f"\t\jyear{{{entry[0]}}}\n\n"
    else:
        journal_commands = journal_commands + f"\t\jdr{{{entry[0].title()}}}{{{entry[1][0].title()}}}{{{entry[5][0]}}}{{{entry[3][0]}}}\n"
        if len(entry[1]) > 1:
            for i in range(1, len(entry[1])):
                journal_commands = journal_commands + f"\t\jdr{{}}{{{entry[1][i].title()}}}{{{entry[5][i]}}}{{{entry[3][i]}}}\n"
        journal_commands = journal_commands + f"\t\jcr{{{entry[2][0].title()}}}{{{entry[4][0]}}}\n"
        if len(entry[2]) > 1:
            for i in range(1, len(entry[1])):
                journal_commands = journal_commands + f"\t\jcr{{{entry[2][i].title()}}}{{{entry[4][i]}}}\n"
        journal_commands = journal_commands + f"\t\jnar{{{entry[6]}}}\n\n"
journal_commands = journal_commands + "}"

ledger_commands = "Work In Process"

with open(f"{choice}_journal.tex", "w") as file:
    file.write(journal_commands)
with open(f"{choice}_ledger.tex", "w") as file:
    file.write(ledger_commands)
