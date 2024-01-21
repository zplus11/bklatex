from .account import account


class month:
    def __init__(self, acc, month, year):
        assert isinstance(acc, account), f"{account} is not an account class object"
        acc.database[(month, year)] = []
        self.entries = acc.database[(month, year)]
        self.month = month
        self.year = year

    def clean(self, string):
        cleaned = ""
        for i in string:
            if i in r"&%$#_{}~\\^": cleaned += fr"\{i}"
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
        if not len(debit_folios): debit_folios = [""]*len(debit_accounts)
        if not len(credit_folios): credit_folios = [""]*len(credit_accounts)
        constituted = [
            self.clean(date), 
            [self.clean(name) for name in debit_accounts],
            [self.clean(name) for name in credit_accounts],
            debit_amounts,
            credit_amounts,
            debit_folios,
            credit_folios,
            self.clean(narration)
        ]
        bool1 = (len(constituted[1]) == len(constituted[3]) and (len(constituted[5]) == len(constituted[3]) or not len(constituted[5]))) and (len(constituted[2]) == len(constituted[4]) and (len(constituted[6]) == len(constituted[4]) or not len(constituted[6])))
        bool2 = all(constituted[i][j] > 0 for i in [3, 4] for j in range(len(constituted[i])))
        assert bool2, "Debit or credit amounts were not integer values."
        assert all(isinstance(constituted[i], list) for i in [1, 2, 3, 4]) and bool1, "Ensure debit (credit) accounts, amounts and folios are in lists and have equal lengths."
        
        self.entries.append(constituted)
        
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass
