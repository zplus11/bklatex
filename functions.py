import pandas as pd
import json
import os



def read_journals(path):
    with open(path, "r") as file:
        return json.load(file)

def create_database(filename):
    if not os.path.exists(filename):
        year = input("Current year: ")
        empty = {"entries": [[year]]}
        with open(f"{filename}_entries.json", "w") as file:
            json.dump(empty, file)
        print(f"Made entries database with {filename}_entries.json name.")
    else:
        print("File with that name exists. Supply unique name or delete that file.")
