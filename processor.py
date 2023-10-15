from functions import *

pname = input("Supply name of the project. Enter ""new"" to create a new project.\n")

if pname.lower().strip() == "new":
    pname = input("Enter (unique) name for your project: ")
    create_project(pname)
else:
    journals_data = read_journals(pname)
    print(f"Loaded the data from given path.")
   
print("____________E_D_I_T_O_R____________")
print("CAUTION: Add changes will be made to the database you chose above.")
print("Available options:\n1) add entry, x) close editor")
ech = input("Enter your choice: ").lower().strip()
while ech != "x":
    if ech == "1":
        start_year(pname)
    elif ech == "2":
        add_entry(pname)
    else:
        print("Invalid choice.")
    ech = input("Enter your next choice: ").lower().strip()

print("____________C_O_M_P_I_L_E_R____________")
print_journals(pname)
print_ledgers(pname)
fabricate(pname)
