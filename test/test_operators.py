from types import FunctionType
from src.parser import Payload
from src import operators as ops


# parse:
# - si +, -, *, ^, /, %, l'enleve et retourne un Callable F
#
#
#


def test_op_parse_sum():  # check que op.parse trouve bien le +
    line = "+^zzzzzzzzzz"
    pl: Payload = Payload(line)
    rtn = ops.parse(pl)

    assert pl.line == "^zzzzzzzzzz"
    assert type(rtn) is FunctionType


def test_op_parse_minus():  # check que op.parse trouve bien le -
    line = "-+zzzzzzzzzz"
    pl: Payload = Payload(line)
    rtn = ops.parse(pl)

    assert pl.line == "+zzzzzzzzzz"
    assert type(rtn) is FunctionType


def test_op_parse_mult():  # check que op.parse trouve bien le *
    line = "*-zzzzzzzzzz"
    pl: Payload = Payload(line)
    rtn = ops.parse(pl)
    
    assert pl.line == "-zzzzzzzzzz"
    assert type(rtn) is FunctionType


def test_op_parse_modulo():  # check que op.parse trouve bien le %
    line = "%*zzzzzzzzzz"
    pl: Payload = Payload(line)
    rtn = ops.parse(pl)
    
    assert pl.line == "*zzzzzzzzzz"
    assert type(rtn) is FunctionType


def test_op_parse_pow():  # check que op.parse trouve bien le *
    line = "^-zzzzzzzzzz"
    pl: Payload = Payload(line)
    rtn = ops.parse(pl)
    
    assert pl.line == "-zzzzzzzzzz"
    assert type(rtn) is FunctionType


def test_op_parse_invalid():
    line = "zzzzzzzzzz"
    pl: Payload = Payload(line)
    rtn = ops.parse(pl)
    
    assert pl.line == "zzzzzzzzzz"
    assert rtn is None
