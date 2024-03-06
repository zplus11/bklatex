import os
from bklatex.compiler import compiler
from bklatex.month import month


class account:
    def __init__(self, file_name: str, company_name: str = None, year: str = None, credit_natures: list = None):
        self.file_name = file_name
        print(f"Account initiated with file name {self.file_name}")
        self.company_name = company_name
        self.year = year
        self.cwd = os.path.dirname(os.path.realpath(__file__))
        self.database = {}
        self.credit_natures = []
        if self.credit_natures:
            print(", ".join(self.credit_natures), "set to credit natured accounts")

    def month(self, name: str = None, year: str = None):
        assert name and len(name) >= 3, "Month name needs to be at least 3 characters long"
        newmonth = month(name, year)
        self.database[(name, year)] = newmonth
        return newmonth

    def make_pdf(self, journals: bool = True, ledgers: bool = True, keep_tex: bool = True):
        tex_name = self.file_name + ".tex"
        com = compiler(tex_name, self.cwd, self.database, self.company_name, self.year, self.credit_natures)
        com.open_tex()
        if journals == True:
            com.write_journals()
        if ledgers == True:
            com.write_ledgers()
        com.close_tex()
        
        com.fabricate(keep_tex)
