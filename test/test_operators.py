from types import FunctionType
from src.parser import Payload
from src import operators as ops


# parse:
# - si +, -, *, ^, /, %, l'enleve et retourne un Callable
#
#
#


def test_op_parse_sum():  # check que op.parse trouve bien le +
    line = "+^eaqr tetve"
    pl: Payload = Payload(line)
    rtn = ops.parse(pl)
    assert pl.get_index() == 1
    assert pl.line == "^eaqr tetve"
    assert rtn is not None
    assert type(rtn) is FunctionType


def test_op_parse_minus():  # check que op.parse trouve bien le -
    line = "-+eaqr tetve"
    pl: Payload = Payload(line)
    rtn = ops.parse(pl)
    assert pl.get_index() == 1
    assert pl.line == "+eaqr tetve"
    assert rtn is not None
    assert type(rtn) is FunctionType


def test_op_parse_mult():  # check que op.parse trouve bien le *
    line = "*-eaqr tetve"
    pl: Payload = Payload(line)
    rtn = ops.parse(pl)

    assert pl.get_index() == 1
    assert pl.line == "-eaqr tetve"
    assert rtn is not None
    assert type(rtn) is FunctionType


def test_op_parse_modulo():  # check que op.parse trouve bien le %
    line = "%*eaqr tetve"
    pl: Payload = Payload(line)
    rtn = ops.parse(pl)

    assert pl.get_index() == 1
    assert pl.line == "*eaqr tetve"
    assert rtn is not None
    assert type(rtn) is FunctionType


def test_op_parse_pow():  # check que op.parse trouve bien le *
    line = "^-eaqr tetve"
    pl: Payload = Payload(line)
    rtn = ops.parse(pl)

    assert pl.get_index() == 1
    assert pl.line == "-eaqr tetve"
    assert rtn is not None
    assert type(rtn) is FunctionType


def test_op_parse_invalid():
    line = "eaqr tetve"
    pl: Payload = Payload(line)
    rtn = ops.parse(pl)

    assert pl.get_index() == 0
    assert pl.line == "eaqr tetve"
    assert rtn is None
