from src import parser


def test_payload_init():  # check que payload garde bien la ligne
    line = "iurthziroz zerv"
    pl: parser.Payload = parser.Payload(line)
    assert pl.line == line
    assert pl.orline == line


def test_payload_getindex():  # check que get index retourne bien la quantite enlevee a line
    line = "ioeruvnev retvi"
    pl: parser.Payload = parser.Payload(line)
    pl.line = pl.line[6:]
    assert pl.get_index() == 6


def test_ignore_whitespace():
    line = "   ioeruvnev retvi"
    pl: parser.Payload = parser.Payload(line)
    parser.ignore_whitespace(pl)

    assert pl.get_index()==3
    assert pl.line=="ioeruvnev retvi"
