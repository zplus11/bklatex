import pandas as pd
import json
import os
import subprocess

def read_journals(project_name):
    while not os.path.exists(project_name):
        path = input("That file does not exist. Try again: ")
    with open(f"{project_name}\{project_name}_entries.json", "r") as file:
        return json.load(file)

def write_journals(project_name, entries):
    with open(f"{project_name}\{project_name}_entries.json", "w") as file:
        json.dump(entries, file)

def create_project(name):
    if not os.path.exists(name):
        empty = {"entries": []}
        os.mkdir(name)
        with open(f"{name}\{name}_entries.json", "w") as file:
            json.dump(empty, file)
        print(f"Made project with {name} name. An entries file was made in that folder with {name}_entries.json name.")
    else:
        print("Project with that name exists. Supply unique name or delete that project.")

def add_entry(project_name):
    add_date = input("Enter date of transaction: ")
    add_debit = input("Enter debited account names. Separate with comma if more than one: ")
    add_credit = input("Enter credited account names. Separate with comma if more than one: ")
    add_debit_amt = input("Add debited amounts in same order of accounts. Separate with comma: ")
    add_credit_amt = input("Add credited amounts in same order of accounts. Separate with comma: ")
    add_debit_folio = input("Add folio numbers for debit accounts. Enter none if NA. Separate with comma: ")
    add_credit_folio = input("Add folio numbers for credit accounts. Enter none if NA. Separate with comma: ")
    add_narration = input("Add narration: ")
    debit_accounts = [element.strip() for element in add_debit.split(",")]
    credit_accounts = [element.strip() for element in add_credit.split(",")]
    debit_amounts = [element.strip() for element in add_debit_amt.split(",")]
    credit_amounts = [element.strip() for element in add_credit_amt.split(",")]
    debit_folios = [element.strip() for element in add_debit_folio.split(",")]
    credit_folios = [element.strip() for element in add_credit_folio.split(",")]
    journals_data = read_journals(project_name)
    entry = [add_date, debit_accounts, credit_accounts, debit_amounts, credit_amounts, debit_folios, credit_folios, add_narration]
    journals_data["entries"].append(entry)
    print("The following entry was added:")
    print(f"{add_date}\t{debit_accounts}\t\t\t{debit_folios}\t{debit_amounts}\n\t\t\t{credit_accounts}\t\t\t{credit_folios}\t{credit_amounts}\n{add_narration}")
    write_journals(project_name, journals_data)

def print_journals(project_name):
    journals_data = read_journals(project_name)
    print(journals_data)
    journal_commands = "%%%%%%%%%%%%%%%%%%%%%%\n% JOURNAL ENTRIES\n%%%%%%%%%%%%%%%%%%%%%%\n\n\journal{\n\n"
    for entry in journals_data["entries"]:
        print(entry)
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
    with open(f"{project_name}\{project_name}_journal.tex", "w") as file:
        file.write(journal_commands)

def print_ledgers(project_name):
    ledger_commands = "%%%%%%%%%%%%%%%%%%%%%%\n% LEDGER ENTRIES\n%%%%%%%%%%%%%%%%%%%%%%\n\n"
    with open(f"{project_name}\{project_name}_ledger.tex", "w") as file:
        file.write(ledger_commands)
        
def fabricate(project_name):
    main_commands = f"% This is {project_name}_main.tex fabricated using https://github.com/zplus11/Bookkeeping-LaTeX.git\n"
    main_commands += f"\input{{preamble.tex}}\n\n"
    main_commands += f"\\begin{{document}}\n\t\\begin{{center}}\n\t\t{{\Huge Bookkeeping with \LaTeX}}\\\\[5pt]{{\LARGE Automation with Python}}\n\t\end{{center}}\n"
    main_commands += f"\t\section{{Journal}}\n\t\include{{{project_name}/{project_name}_journal.tex}}\n"
    main_commands += f"\t\section{{Ledger Posting}}\n\t\include{{{project_name}/{project_name}_ledger.tex}}\n"
    main_commands += f"\end{{document}}"
    with open(f"{project_name}\{project_name}_main.tex", "w") as file:
        file.write(main_commands)
    subprocess.run(['pdflatex', f"{project_name}\{project_name}_main.tex"])
