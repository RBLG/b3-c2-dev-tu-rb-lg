from ast import List
from src import args
from src import parser


input: str = args.get_input()

result: float = parser.compute(input)

print("resultat: " + str(result))
