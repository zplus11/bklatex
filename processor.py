from functions import *

def print_head(string):
    string_to_print = "_".join(list(string))
    n = 70 - len(string_to_print)
    if len(string_to_print) % 2 == 1: no = 1
    n += no
    cover = "_"*int(n/2)
    string_to_print = string_to_print.join([cover, cover])
    print("_"*(70 + no))
    print(string_to_print)
    
print_head("BOOKKEEPING LaTeX")
print("Typeset accounting journals easily using LaTeX and Python! Here each journal-ledger pair is referred to as a 'project'.")
pname = input("Supply name of the project. Enter ""new"" to create a new project.: ")

if pname.lower().strip() == "new":
    pname = input("Enter (unique) name for your project: ")
    create_project(pname)
    journals_data = read_journals(pname)
else:
    journals_data = read_journals(pname)
    print(f"Loaded the data from given path.")

def compiler(pname):
    print_head("COMPILER")
    cch = input("Would you like to keep the .tex files? y/n: ").lower().strip()
    print_journals(pname)
    print_ledgers(pname)
    fabricate(pname)
    try:
        os.remove(f"{pname}\\{pname}_main.log")
        os.remove(f"{pname}\\{pname}_main.aux")
        if cch == "n":
            os.remove(f"{pname}\\{pname}_main.tex")
            os.remove(f"{pname}\\{pname}_journal.tex")
            os.remove(f"{pname}\\{pname}_ledger.tex")
            print("The .tex and other files are removed.")
    except Exception as e:
        print(f"Issue encountered.\n[-] {e}")
    print("The pdf file has been generated in project's directory.")

print_head("EDITOR")
print("CAUTION: Add changes will be made to the database you chose above.")
options = "Available options:\n0) view all entries in compact form\n1) start new year\n2) add entry\n3) edit existing entry\n4) delete existing entry\np) compile pdf of current project (remember to return back here)\nx) close the editor"
print(options)
ech = input("Enter your choice: ").lower().strip()
while ech != "x":
    print("-"*30)
    if ech == "0":
        for entry in journals_data:
            print_entry(entry)
    elif ech == "1":
        start_year(pname)
    elif ech == "2":
        add_entry(pname)
    elif ech == "3":
        edit_entry(pname)
    elif ech == "4":
        delete_entry(pname)
    elif ech == "p":
        compiler(pname)
    else:
        print("Invalid choice.")
    print("-"*30)
    print(options)
    ech = input("Enter your next choice: ").lower().strip()
    journals_data = read_journals(pname)
