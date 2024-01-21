import os
from .compiler import compiler


class account:
    def __init__(self, file_name: str, company_name: str = "", year: str = ""):
        self.file_name = file_name
        self.company_name = company_name
        self.year = year
        self.cwd = os.path.dirname(os.path.realpath(__file__))
        self.database = {}
        self.credit_natures = []

    def make_pdf(self, journals: bool = True, ledgers: bool = True, keep_tex: bool = False):
        tex_name = self.file_name + ".tex"
        com = compiler(tex_name, self.cwd, self.database, self.company_name, self.year, self.credit_natures)
        com.open_tex()
        if journals == True:
            com.write_journals()
        if ledgers == True:
            com.write_ledgers()
        com.close_tex()
        
        com.fabricate(keep_tex)

    def set_credit(self, accounts: list):
        self.credit_natures = accounts
