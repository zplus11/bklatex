from functions import *

jpath = input("Supply path of the entries file. Enter ""new"" to create a new database.\n")

if jpath.lower().strip() == "new":
    name = input("Enter (unique) name for entries file: ")
    create_database(name)
    name = name + "_entries.json"
    jpath = name
else:
    journals_data = read_journals(jpath)
    print(f"Loaded the data from given path.")
   
print("____________E_D_I_T_O_R____________")
print("CAUTION: Add changes will be made to the database you chose above.")
print("Available options:\n1) add entry, x) close editor")
ech = input("Enter your choice: ").lower().strip()
while ech != "x":
    if ech == "1":
        journals_data = read_journals(jpath)
        add_entry(jpath)
    else:
        print("Invalid choice.")
    ech = input("Enter your next choice: ").lower().strip()

print("____________C_O_M_P_I_L_E_R____________")
name = input("Enter below the name in which you want your files saved. If the files are already existing then supply the same name.\n").strip()
print_journals(name, jpath)
    
    
