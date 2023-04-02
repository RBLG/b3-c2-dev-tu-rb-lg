from src import parser


# parser.compute:
# - gere les operations simples: +,-,*,/,% et ^
# - gere les chaines d'operations (pas de priorite d'operation)
#
# - gere les nombres entier ou a virgule
# - gere les nombres positif ou negatif
# - gere la profondeur (les chaines entre parentheses)
#
# - gere les caracteres blanc entre les differents items
# - gere les caracteres blanc si en debut ou fin de ligne
#
# - echoue si caractere invalide
# - echoue si deux operateur de suite (excluant le - des nombres negatifs)
# - echoue si deux nombres separe par un espace sans operateur
# - echoue si commence ou termine par une operation
# - echoue si parentheses vides
# - echoue si parentheses malformees
#
#
#
#


def test_compute_single_sum():
    input = "1+1"
    output = parser.compute(input)
    assert output == 2


def test_compute_single_sub():
    input = "7-4"
    output = parser.compute(input)
    assert output == 3


def test_compute_single_mul():
    input = "2*3"
    output = parser.compute(input)
    assert output == 6


def test_compute_single_div():
    input = "9/3"
    output = parser.compute(input)
    assert output == 3


def test_compute_single_mod():
    input = "10%7"
    output = parser.compute(input)
    assert output == 3


def test_compute_single_pow():
    input = "3^2"
    output = parser.compute(input)
    assert output == 9


def test_compute_op_chain():
    input = "1+1*2^2-1/2%3"
    output = parser.compute(input)
    assert output == 2


def test_compute_single_sub():
    input = "1-1"
    output = parser.compute(input)
    assert output == 2


def test_compute_single_sub():
    input = "1-1"
    output = parser.compute(input)
    assert output == 2


def test_compute_single_sub():
    input = "1-1"
    output = parser.compute(input)
    assert output == 2


def test_compute_single_sub():
    input = "1-1"
    output = parser.compute(input)
    assert output == 2
