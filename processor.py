from functions import *

ch = input("Supply path of the entries file. Enter ""new"" to create a new database.\n")
if ch.lower().strip() == "new":
    name = input("Enter (unique) name for entries file: ")
    create_database(name)
else:
    if not os.path.exists(ch):
        print("That file does not exist.")
        sleep(3)
    else:
        journals_data = read_journals(ch)
        print(f"Loaded the data from {ch}. Printing it below:")
        print(journals_data)
