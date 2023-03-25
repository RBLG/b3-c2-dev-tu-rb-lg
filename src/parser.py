import re
from src import operators as ops
from src import parameters as pms

######################################################################


class Payload:
    orline: str
    orlen: int
    line: str

    def __init__(self, nline: str):
        self.orline = nline
        self.orlen = len(nline)
        self.line = nline

    def get_index(self) -> int:
        return self.orlen - len(self.line)


######################################################################


def compute(line: str) -> float:
    return parse_nest(Payload(line), False)


def parse_nest(pl: Payload, nested: bool) -> float:
    result = pms.parse(pl)
    while True:
        ignore_whitespace(pl)
        if parse_end_of_input(pl):
            if nested:
                raise Exception("Syntaxe invalide: ')' attendu,trouve fin")
            break
        if parse_end_of_nest(pl):
            if not nested:
                raise Exception("Syntaxe invalide: fin attendue, trouve ')'")
            break

        op = ops.parse(pl)
        if op is None:
            msg = "Syntaxe invalide: operateur attendu a " + str(pl.get_index())
            raise Exception(msg)

        ignore_whitespace(pl)
        param2 = pms.parse(pl)
        if param2 is None:
            msg = "Syntaxe invalide: parametre attendu a " + str(pl.get_index())
            raise Exception(msg)
        # TODO handling priority there

        result = op(result, param2)

    return result


######################################################################


def ignore_whitespace(payload: Payload):
    match = re.search(r"^[\t\r\n ]+", payload.line)
    if match is not None:
        payload.line = payload.line[len(match.group(0)) :]


def parse_end_of_nest(payload) -> bool:
    found = re.search(r"^\)", payload.line) is not None
    if found:
        payload.line = payload.line[1 :]
    return found


def parse_end_of_input(payload) -> bool:
    return re.search(r"^$", payload.line) is not None



