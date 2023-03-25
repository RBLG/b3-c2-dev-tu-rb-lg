from src.parser import Payload
from src import parameters as pms

# parse:
# - doit traiter les nombres entier F
# - doit traiter les nombres a virgule F
# - doit traiter les nombres negatif F
# - doit traiter les chiffres F
# - doit traiter les nombres a plusieur digit F
# - si nombre donne trop grand, ecrit un message d'erreur et retourne None
# - si '(', enclenche un nouveau niveau de traitement
# 
# - si autre, retourne None F


def test_pms_parse_single_digit_number():
    line = "7+zzzzzzzzzz"
    pl: Payload = Payload(line)
    rtn = pms.parse(pl)

    assert pl.line == "+zzzzzzzzzz"
    assert rtn == 7

def test_pms_parse_10_digit_number():
    line = "1234567890+zzzzzzzzzz"
    pl: Payload = Payload(line)
    rtn = pms.parse(pl)

    assert pl.line == "+zzzzzzzzzz"
    assert rtn == 1234567890


def test_pms_parse_float():
    line = "7.89+zzzzzzzzzz"
    pl: Payload = Payload(line)
    rtn = pms.parse(pl)

    assert pl.line == "+zzzzzzzzzz"
    assert rtn == 7.89

def test_pms_parse_negative():
    line = "-3+zzzzzzzzzz"
    pl: Payload = Payload(line)
    rtn = pms.parse(pl)

    assert pl.line == "+zzzzzzzzzz"
    assert rtn == -3

def test_pms_parse_negative_float():
    line = "-9.14+zzzzzzzzzz"
    pl: Payload = Payload(line)
    rtn = pms.parse(pl)

    assert pl.line == "+zzzzzzzzzz"
    assert rtn == -9.14


def test_pms_parse_parenthesis():
    line = "(10)+zzzzzzzzzz"
    pl: Payload = Payload(line)
    rtn = pms.parse(pl)

    assert pl.line == "+zzzzzzzzzz"
    assert rtn == 10


def test_pms_parse_invalid():
    line = "zzzzzzzzzz"
    pl: Payload = Payload(line)
    rtn = pms.parse(pl)
    
    assert pl.line == line
    assert rtn is None


