# try:
import calcparser
import operators as ops

# except:
#    pass


class test_Payload:
    def test_init_line():  # check que payload garde bien la ligne
        line = "iurthziroz zerv"
        pl: parser.Payload = parser.Payload(line)
        assert pl.line == line
        assert pl.orline == line

    def test_init_getindex(): # check que get index retourne bien la quantite enlevee a line
        line = "ioeruvnev retvi"
        pl: parser.Payload = parser.Payload(line)
        pl.line = pl.line[6:]
        assert pl.get_index() == 6


def test_op_parse_sum(): # check que op.parse trouve bien le +
    line = "+^eaqr tetve"
    pl: parser.Payload = parser.Payload(line)
    ops.parse(pl)