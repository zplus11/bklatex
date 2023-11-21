from functions import *
from time import sleep

pname = input("Supply name of the project. Enter ""new"" to create a new project.\n")

if pname.lower().strip() == "new":
    pname = input("Enter (unique) name for your project: ")
    create_project(pname)
    journals_data = read_journals(pname)
else:
    journals_data = read_journals(pname)
    print(f"Loaded the data from given path.")
   
print("____________E_D_I_T_O_R____________")
print("CAUTION: Add changes will be made to the database you chose above.")
options = "Available options:\n0) view all entries in compact form\n1) start new year\n2) add entry\n3) edit existing entry\n4) delete existing entry\nx) close the editor (and compile current project)"
print(options)
ech = input("Enter your choice: ").lower().strip()
while ech != "x":
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
    else:
        print("Invalid choice.")
    print(options)
    ech = input("Enter your next choice: ").lower().strip()
    journals_data = read_journals(pname)

print("____________C_O_M_P_I_L_E_R____________")
cch = input("Would you like to keep the .tex files? y/n: ").lower().strip()
print_journals(pname)
print_ledgers(pname)
fabricate(pname)
if cch in ["n", 0]:
    try:
        os.remove(f"{pname}\{pname}_main.tex")
        os.remove(f"{pname}\{pname}_journal.tex")
        os.remove(f"{pname}\{pname}_ledger.tex")
        os.remove(f"{pname}\{pname}_main.log")
        os.remove(f"{pname}\{pname}_main.aux")
        print("The .tex and other files are removed.")
    except Exception as e:
        print("Issue encountered.", e)
print("The pdf file has been generated in project's directory.")
