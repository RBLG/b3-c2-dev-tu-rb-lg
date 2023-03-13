import sys
import re
import operators
import parameters


######################################################################


def get_input() -> str:
    input: str = ""
    args = sys.argv.copy()
    args.pop(0)
    for arg in args:
        input += arg + " "

    return input


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


def compute(line: str) -> float:
    return parse_nest(Payload(line), False)


def ignore_whitespace(payload: Payload):
    match = re.search("^[\t ]+", payload.line)
    if match is not None:
        payload.line = payload.line[len(match.group(0)) :]


def parse_nest(payload: Payload, nested: bool) -> float:
    result = parameters.parse(payload)
    while True:
        ignore_whitespace(payload)
        op = operators.parse(payload)
        if op is None:
            raise Exception(
                "Syntaxe invalide: operateur attendu a " + str(payload.get_index())
            )
        if op is operators.EndOfAll:
            if nested:
                raise Exception("Syntaxe invalide: ')' attendu, fin trouvee")
            break
        if op is operators.EndOfNest:
            if not nested:
                raise Exception("Syntaxe invalide: fin attendue, ')' trouvee")
            break

        ignore_whitespace(payload)
        param2 = parameters.parse(payload)
        if param2 is None:
            raise Exception(
                "Syntaxe invalide: parametre attendu a " + str(payload.get_index())
            )
        # TODO handling priority there

        result = op(result, param2)

    return result
