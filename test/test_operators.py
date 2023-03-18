from src.parser import Payload
from src import operators as ops


def test_op_parse_sum():  # check que op.parse trouve bien le +
    line = "+^eaqr tetve"
    pl: Payload = Payload(line)
    rtn=ops.parse(pl)
    assert pl.get_index()==1
    assert pl.line=="^eaqr tetve"
    assert rtn is not None

def test_op_parse_minus():  # check que op.parse trouve bien le -
    line = "-+eaqr tetve"
    pl: Payload = Payload(line)
    rtn=ops.parse(pl)
    assert pl.get_index()==1
    assert pl.line=="+eaqr tetve"
    assert rtn is not None

def test_op_parse_mult():  # check que op.parse trouve bien le *
    line = "*-eaqr tetve"
    pl: Payload = Payload(line)
    rtn=ops.parse(pl)

    assert pl.get_index()==1
    assert pl.line=="-eaqr tetve"
    assert rtn is not None

def test_op_parse_modulo():  # check que op.parse trouve bien le %
    line = "%*eaqr tetve"
    pl: Payload = Payload(line)
    rtn=ops.parse(pl)

    assert pl.get_index()==1
    assert pl.line=="*eaqr tetve"
    assert rtn is not None

def test_op_parse_pow():  # check que op.parse trouve bien le *
    line = "^-eaqr tetve"
    pl: Payload = Payload(line)
    rtn=ops.parse(pl)

    assert pl.get_index()==1
    assert pl.line=="-eaqr tetve"
    assert rtn is not None

