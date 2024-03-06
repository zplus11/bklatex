from bklatex.entry import entry


class month:
    def __init__(self, month, year):
        self.entries = []
        self.month = month
        self.year = year
        print(f"Created month {self.month} in the accounts")

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
        constituted = entry(
            date = self.clean(date), 
            debit_accounts = [self.clean(name) for name in debit_accounts],
            credit_accounts = [self.clean(name) for name in credit_accounts],
            debit_amounts = debit_amounts,
            credit_amounts = credit_amounts,
            debit_folios = debit_folios,
            credit_folios = credit_folios,
            narration = self.clean(narration)
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
        
        self.entries.append(constituted)
        print(f"Recorded entry: By {constituted.debit_accounts} ({constituted.debit_amounts}); To {constituted.credit_accounts} ({constituted.credit_amounts})")
        
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass
