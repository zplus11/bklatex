import subprocess
import os


class Object:
    def __init__(self):
        self.tex = []

class Document(Object):
    def __init__(self, name: str = None):
        if name is None:
            name = repr(self)[1:-1]
        self.name = name+".tex"
        super().__init__()
        self.accounts = []

    def append(self, account):
        assert isinstance(account, Account)
        self.accounts.append(account)
        return account

    def print(self, pdf: bool = True, tex: bool = False):
        pkg = os.path.join(os.path.realpath(__file__)[:-8], "accountancy").replace("\\", "/") # 8 = len('core.py') + 2
        if tex or pdf:
            self.tex += [
                "% This was printed using bklatex (https://github.com/zplus11/bklatex)",
                "% Copyright (c) 2024 Naman Taggar",
                "% namantaggar [dot) 11 (at] gmail (dot) com",
                Command("documentclass", "article"),
                Command("usepackage", options=["smallmargins"], arguments=[pkg]),
                Command("begin", "document")
            ]
            for account in self.accounts:
                self.tex += account.output()
            self.tex += [Command("end", "document")]
            with open(self.name, "w") as file:
                file.write("\n".join([str(cmd) for cmd in self.tex]))
        if pdf:
            subprocess.run(["pdflatex", self.name])
            os.remove(self.name[:-4]+".out")
            os.remove(self.name[:-4]+".aux")
            os.remove(self.name[:-4]+".log")
        if not tex:
            os.remove(self.name)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

class Account(Object):
    def __init__(self):
        super().__init__()

    def print_tex(self, name: str = None):
        tex = [
            "% This was printed using bklatex (https://github.com/zplus11/bklatex)",
            "% Copyright (c) 2024 Naman Taggar",
            "% namantaggar [dot) 11 (at] gmail (dot) com"
        ] + self.output()
        if name is None:
            name = repr(self)[1:-1]
        name = name+".tex"
        with open(name, "w") as file:
            file.write("\n".join([str(cmd) for cmd in tex]))


class Command:
    def __init__(self, name, arguments = None, options = None):
        if type(arguments) == str: arguments = [arguments]
        if type(options) == str: options = [options]
        self.name = name
        self.arguments = arguments
        self.options = options
        self.bs = "\\"

    def __str__(self):
        return self.bs \
               + self.name \
               + (parseops(self.options) if self.options else "") \
               + (parseargs(self.arguments) if self.arguments else "")


def parseops(args):
    args = list(args)
    for i, a in enumerate(args):
        if not isinstance(i, str):
            args[i] = str(a)
    return "[" + "][".join(args) + "]"

def parseargs(args):
    args = list(args)
    for i, a in enumerate(args):
        if not isinstance(i, str):
            args[i] = str(a)
    return "{" + "}{".join(args) + "}"

def parsemultops(args):
    args = list(args)
    for i, a in enumerate(args):
        if not isinstance(i, str):
            args[i] = str(a)
    return ",".join(args)
