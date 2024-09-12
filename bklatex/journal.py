from bklatex.core import Account, Command


class Entry:
    """
    Entry class to store journal entries with their respective
    attributes.
    """

    def __init__(self, date, debit_accounts, credit_accounts, debit_amounts, credit_amounts, debit_folios, credit_folios, narration):
        """Initiates an entry in the journal."""
        
        self.date = date
        self.debit_accounts = debit_accounts
        self.credit_accounts = credit_accounts
        self.debit_amounts = debit_amounts
        self.credit_amounts = credit_amounts
        self.debit_folios = debit_folios
        self.credit_folios = credit_folios
        self.narration = narration

    def source(self):
        """Returns TeX source of the entry."""

        tex = [Command("jdr", arguments = [
            self.date.title(),
            self.debit_accounts[0].title(),
            self.debit_folios[0],
            self.debit_amounts[0]
        ])]
        if len(self.debit_accounts) > 1:
            for i in range(1, len(self.debit_accounts)):
                tex.append(Command("jdr", arguments = [
                    "",
                    self.debit_accounts[i].title(),
                    self.credit_folios[i],
                    self.credit_amounts[i]
                ]))
        tex.append(Command("jcr", arguments = [
            self.credit_accounts[0].title(),
            self.credit_folios[0],
            self.credit_amounts[0]
        ]))
        if len(self.credit_accounts) > 1:
            for i in range(1, len(self.credit_accounts)):
                tex.append(Command("jcr", arguments = [
                    "",
                    self.debit_accounts[i].title(),
                    self.credit_folios[i],
                    self.credit_amounts[i]
                ]))
        tex.append(Command("jnar", arguments = self.narration))
        return tex

class Journal(Account):
    """Class to represent a journal account."""

    def __init__(self):
        """Initialises a journal in the given book."""
        super().__init__()
        self.database = dict()

    def __clean(self, string):
        cleaned = ""
        for i in string:
            if i in r"&%$#_{}~^": cleaned += fr"\{i}"
            else: cleaned += i
        return cleaned

    def entry(
        self,
        date: str = "1",
        debit_accounts: list = ["cash"],
        credit_accounts: list = ["capital"],
        debit_amounts: list = [100000],
        credit_amounts: list = [100000],
        debit_folios: list = [],
        credit_folios: list = [],
        narration: str = "being capital introduced"
    ):
        """Writes an entry to the current month."""
        if not len(debit_folios): debit_folios = [""]*len(debit_accounts)
        if not len(credit_folios): credit_folios = [""]*len(credit_accounts)
        constituted = Entry(
            date = self.__clean(date), 
            debit_accounts = [self.__clean(name) for name in debit_accounts],
            credit_accounts = [self.__clean(name) for name in credit_accounts],
            debit_amounts = debit_amounts,
            credit_amounts = credit_amounts,
            debit_folios = debit_folios,
            credit_folios = credit_folios,
            narration = self.__clean(narration)
        )
        bool1 = (
                len(constituted.debit_accounts) == len(constituted.debit_amounts)
                and (len(constituted.debit_folios) == len(constituted.debit_accounts) or not len(constituted.debit_folios))
            ) and (
                len(constituted.credit_accounts) == len(constituted.credit_amounts)
                and (len(constituted.credit_folios) == len(constituted.credit_accounts) or not len(constituted.credit_folios))
            )
        bool2 = all(i > 0 for i in constituted.debit_amounts) and all(i > 0 for i in constituted.credit_amounts)
        for part in [
            constituted.debit_accounts,
            constituted.credit_accounts,
            constituted.debit_amounts,
            constituted.credit_amounts,
            constituted.debit_folios,
            constituted.credit_folios
        ]:
            assert type(part) == list, f"{part}: list expected, {type(part)} received"
        assert bool2, "Debit or credit amounts were not positive values"
        assert bool1, "Ensure debit (credit) accounts, amounts and folios are in lists and have equal lengths"

        self.tex += constituted.source()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def output(self):
        return ["\\journal{"] + self.tex + ["}"]
