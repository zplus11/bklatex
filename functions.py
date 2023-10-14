import pandas as pd
import json
import os

def read_journals(path):
    while not os.path.exists(path):
        path = input("That file does not exist. Try again: ")
    with open(path, "r") as file:
        return json.load(file)

def write_journals(path, entries):
    with open(path, "w") as file:
        json.dump(entries, file)

def create_database(filename):
    if not os.path.exists(filename):
        year = input("Current year: ")
        empty = {"entries": [[year]]}
        with open(f"{filename}_entries.json", "w") as file:
            json.dump(empty, file)
        print(f"Made entries database with {filename}_entries.json name.")
    else:
        print("File with that name exists. Supply unique name or delete that file.")

def add_entry(file):
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
    journals_data = read_journals(file)
    entry = [add_date, debit_accounts, credit_accounts, debit_amounts, credit_amounts, debit_folios, credit_folios, add_narration]
    journals_data["entries"].append(entry)
    print("The following entry was added:")
    print(f"{add_date}\t{debit_accounts}\t\t\t{debit_folios}\t{debit_amounts}\n\t\t\t{credit_accounts}\t\t\t{credit_folios}\t{credit_amounts}\n{add_narration}")
    write_journals(file, journals_data)

def print_journals(file_name, path):
    journals_data = read_journals(path)
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
    with open(f"{file_name}_journal.tex", "w") as file:
        file.write(journal_commands)
