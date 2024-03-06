import os
import subprocess


class compiler:
    def __init__(self, file_name, cwd, database, company_name, year, credit_natures):
        self.file_name = file_name
        self.cwd = cwd
        self.database = database
        self.company_name = company_name
        self.year = year
        self.credit_natures = credit_natures
        print("Compiler activated")
        
    def open_tex(self):
        print(f"[O]", end = " ")
        cwd = self.cwd.replace("\\", "/")
        opening_commands = f"% This is {self.file_name} printed using https://github.com/zplus11/bklatex.git\n\n"
        opening_commands += f"\\documentclass{{article}}\n\\usepackage[smallmargins]{{{cwd}/accountancy}}\n"
        opening_commands += f"\\begin{{document}}\n\t\n\n"

        with open(self.file_name, "w") as file:
            file.write(opening_commands)
        print()
        
    def write_journals(self):
        print(f"[J]", end = " ")
        journal_commands = f"\t%%%%%%%%%%%%%%%%%%%%%%\n\t% JOURNAL ENTRIES\n\t%%%%%%%%%%%%%%%%%%%%%%\n\n\t\\journal{{{self.company_name}}}{{{self.year}}}{{\n"
        current_year = ""

        print(self.database)
        for month in self.database:
            if month[1] != current_year:
                journal_commands += f"\t\t\\jyear{{{month[1]}}}\n"
                current_year = month[1]
            for entry in self.database[month].entries:
                journal_commands += f"\t\t\\jdr{{{entry.date.title() + " " + month[0][0:3]}}}{{{entry.debit_accounts[0].title()}}}{{{entry.debit_folios[0]}}}{{{entry.credit_amounts[0]}}}\n"
                if len(entry.debit_accounts) > 1:
                    for i in range(1, len(entry.debit_accounts)):
                        journal_commands += f"\t\t\\jdr{{}}{{{entry.debit_accounts[i].title()}}}{{{entry.credit_amounts[i]}}}{{{entry.credit_amounts[i]}}}\n"
                journal_commands += f"\t\t\\jcr{{{entry.credit_accounts[0].title()}}}{{{entry.credit_folios[0]}}}{{{entry.credit_amounts[0]}}}\n"
                if len(entry.credit_accounts) > 1:
                    for i in range(1, len(entry.credit_accounts)):
                        journal_commands += f"\t\t\\jcr{{{entry.credit_accounts[i].title()}}}{{{entry.credit_folios[i]}}}{{{entry.credit_amounts[i]}}}\n"
                journal_commands += f"\t\t\\jnar{{{entry.narration}}}\n"
        journal_commands += "\t}\n\n"
        print("Printed", sum([len(month) for month in self.database]), "entries in the journal") 

        with open(self.file_name, "a") as file:
            file.write(journal_commands)
        
    def write_ledgers(self):
        global unique_accounts, accounts

        print("[L]", end = " ")
        ledger_commands = f"\t%%%%%%%%%%%%%%%%%%%%%%\n\t% LEDGER POSTING\n\t%%%%%%%%%%%%%%%%%%%%%%\n\n\tLedger posting: W.I.P.\n\n"
        
        unique_accounts = set()
        for monthlog in self.database.values():
            for entry in monthlog.entries:
                for dacc in entry.debit_accounts:
                    unique_accounts.add(dacc)
                for cacc in entry.credit_accounts:
                    unique_accounts.add(cacc)
        
        accounts = {monthlog[0]: {account: {"nature": "d", "opening": 0, "debit": [], "credit": [], "closing": 0} for account in unique_accounts} for monthlog in self.database}

        for account in self.credit_natures:
            if account in unique_accounts:
                for monthlog in self.database:
                    accounts[monthlog[0]][account]["nature"] = "c"
        
        for account in unique_accounts:
            for monthlog in self.database:
                index = list(self.database).index(monthlog)
                accounts[monthlog[0]][account]["closing"] = accounts[monthlog[0]][account]["opening"]
                for entry in self.database[monthlog].entries:
                    for i in range(len(entry.debit_accounts)):
                        if account == entry.debit_accounts[i]:
                            accounts[monthlog[0]][account]["debit"].append([entry.date, entry.credit_accounts, entry.debit_amounts[i], entry.debit_folios])
                            accounts[monthlog[0]][account]["closing"] += entry.debit_amounts[i]
                    
                    for i in range(len(entry.credit_accounts)):
                        if account == entry.credit_accounts[i]:
                            accounts[monthlog[0]][account]["credit"].append([entry.date, entry.debit_accounts, entry.credit_amounts[i], entry.credit_folios])
                            accounts[monthlog[0]][account]["closing"] -= entry.credit_amounts[i]
                if index < len(self.database) - 1:
                    accounts[list(self.database)[index + 1][0]][account]["opening"] = accounts[monthlog[0]][account]["closing"]
                            
        for account in unique_accounts:
            ledger_commands += f"\t% {account.upper()} ACCOUNT \n"
            ledger_commands += f"\t\\ledger{{{account.title()} a/c}}{{\n"

            for month in accounts:
                ld = len(accounts[month][account]["debit"])
                lc = len(accounts[month][account]["credit"])
                nature = accounts[month][account]["nature"]

                opening_balance = accounts[month][account]["opening"]
                closing_balance = accounts[month][account]["closing"]
                
                if nature == "d":
                    ledger_commands += f"\t\t\\tobalbd{{1 {month[0:3]}}}{{{opening_balance}}}\n"

                for entry in accounts[month][account]["debit"]:
                    ledger_commands += f"\t\t\\ldr{{{entry[0] + " " + month[0:3].title()}}}{{{entry[1][0].title()}}}{{{entry[2]}}}{{{entry[3][0]}}}\n"

                if nature == "c":
                    ledger_commands += f"\t\t\\tobalcd{{30 {month[0:3]}}}{{{closing_balance}}}\n"

                ledger_commands += "\t\t\\mt\n\t\t"
                if ld < lc:
                    for i in range(lc - ld):
                        ledger_commands += "\\mt"
                        
                total_amt = opening_balance + sum([accounts[month][account]["debit"][i][2] for i in range(ld)])
                ledger_commands += f"\n\t\t\\total{{{total_amt}}}\n"
                        
            ledger_commands += "\n\t}{\n"
            
            for month in accounts:
                ld = len(accounts[month][account]["debit"])
                lc = len(accounts[month][account]["credit"])
                nature = accounts[month][account]["nature"]

                opening_balance = accounts[month][account]["opening"]
                closing_balance = accounts[month][account]["closing"]
                
                if nature == "c":
                    ledger_commands += f"\t\t\\bybalbd{{1 {month[0:3]}}}{{{opening_balance}}}\n"
                    
                for entry in accounts[month][account]["credit"]:
                    ledger_commands += f"\t\t\\lcr{{{entry[0] + " " + month[0:3].title()}}}{{{entry[1][0].title()}}}{{{entry[2]}}}{{{entry[3][0]}}}\n"

                if nature == "d":
                    ledger_commands += f"\t\t\\bybalcd{{30 {month[0:3]}}}{{{closing_balance}}}\n"

                ledger_commands += "\t\t\\mt\n\t\t"
                if lc < ld:
                    for i in range(ld - lc):
                        ledger_commands += "\\mt"
                        
                total_amt = closing_balance + sum([accounts[month][account]["credit"][i][2] for i in range(lc)])
                ledger_commands += f"\n\t\t\\total{{{total_amt}}}\n"
            
            ledger_commands += "\t}\n"

        with open(self.file_name, "a") as file:
            file.write(ledger_commands)
        print(f"Printed {len(unique_accounts)} accounts in the ledger")
        
    def close_tex(self):
        print(f"[C]", end = " ")
        compiler_commands = f"\\end{{document}}\n% End of {self.file_name}"

        with open(self.file_name, "a") as file:
            file.write(compiler_commands)
        print()
        
    def fabricate(self, keep_tex):
        print(f"[F]", end = " ")
        print("Calling pdflatex...")
        try:
            compiler_response = subprocess.run(
                ["pdflatex", self.file_name],
                stdout = subprocess.PIPE,
                text = True,
                check = True,
                creationflags = subprocess.CREATE_NO_WINDOW
            )
            compiler_response = f"{compiler_response.stdout}"
            
        except subprocess.CalledProcessError as e:
            print("[!] Encountered error.", end = " ")
            compiler_response = f"{e.output}"

        print(compiler_response)

        if keep_tex == False:
            os.remove(self.file_name)
            print("TeX file is removed")
        try:
            os.remove(self.file_name[:-4] + ".aux")
            os.remove(self.file_name[:-4] + ".log")
            os.remove(self.file_name[:-4] + ".out")
            print("Auxiliary files are removed")
        except FileNotFoundError:
            pass
