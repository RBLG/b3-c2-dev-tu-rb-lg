from src import parser

# Payload:
# - orline doit etre la ligne tel que definit a le constructeur
# - line doit etre actualise a chaque changement
# - get_index retourne la quantité enlevee depuis le constructeur
#
def test_payload_init():
    line = "zzzzzzzzzz"
    pl: parser.Payload = parser.Payload(line)
    assert pl.line == line
    assert pl.orline == line
    assert pl.orlen == 10


def test_payload_getindex_valid():
    line = "zzzzzzzzzz"
    pl: parser.Payload = parser.Payload(line)
    pl.line = pl.line[6:]
    assert pl.get_index() == 6


# ignore_whitespace:
# - si espace(s), les enleve F
# - si \n, `\t, \r les enleve F
# - si n'importe quel autre caractere, ne fait rien F
# - si 1 caractere a enlever, en enleve 1 F
# -si 20 a enlever, en enleve 20 F
#
#
def test_ignore_whitespace_1_space():
    line = " zzzzzzzzzz"
    pl: parser.Payload = parser.Payload(line)
    parser.ignore_whitespace(pl)

    assert pl.get_index() == 1
    assert pl.line == "zzzzzzzzzz"


def test_ignore_whitespace_20_space():
    line = "                    zzzzzzzzzz"
    pl: parser.Payload = parser.Payload(line)
    parser.ignore_whitespace(pl)

    assert pl.get_index() == 20
    assert pl.line == "zzzzzzzzzz"


def test_ignore_whitespace_newline():
    line = "\nzzzzzzzzzz"
    pl: parser.Payload = parser.Payload(line)
    parser.ignore_whitespace(pl)

    assert pl.get_index() == 1
    assert pl.line == "zzzzzzzzzz"


def test_ignore_whitespace_tab():
    line = "\tzzzzzzzzzz"
    pl: parser.Payload = parser.Payload(line)
    parser.ignore_whitespace(pl)

    assert pl.get_index() == 1
    assert pl.line == "zzzzzzzzzz"


def test_ignore_whitespace_carriage_return():
    line = "\rzzzzzzzzzz"
    pl: parser.Payload = parser.Payload(line)
    parser.ignore_whitespace(pl)

    assert pl.get_index() == 1
    assert pl.line == "zzzzzzzzzz"


def test_ignore_whitespace_invalid():
    line = "zzzzzzzzzz"
    pl: parser.Payload = parser.Payload(line)
    parser.ignore_whitespace(pl)

    assert pl.get_index() == 0
    assert pl.line == "zzzzzzzzzz"


# parse_end_of_nest:
# - retourne vrai si parenthese fermante F
# - retourne faux si fin de ligne F
# - retourne faux si n'importe quel autre caractere F
#
def test_parse_end_of_nest_valid():
    line = ")zzzzzzzzzz"
    pl: parser.Payload = parser.Payload(line)
    parser.parse_end_of_nest(pl)

    assert pl.get_index() == 1
    assert pl.line == "zzzzzzzzzz"

def test_parse_end_of_nest_end_of_line():
    line = ""
    pl: parser.Payload = parser.Payload(line)
    assert not parser.parse_end_of_nest(pl)

def test_parse_end_of_nest_invalid():
    line = "zzzzzzzzzz"
    pl: parser.Payload = parser.Payload(line)
    assert not parser.parse_end_of_nest(pl)
    assert pl.get_index() == 0
    assert pl.line == "zzzzzzzzzz"


# parse_end_of_input:
# - retourne vrai si fin de ligne F
# - retourne faux sinon F
#
#
def test_parse_end_of_input_valid():
    pl: parser.Payload = parser.Payload("")
    assert parser.parse_end_of_input(pl)


def test_parse_end_of_input_invalid():
    pl: parser.Payload = parser.Payload("zzzzzzzzzz")
    assert not parser.parse_end_of_input(pl)
