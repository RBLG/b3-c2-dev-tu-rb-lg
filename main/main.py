from ast import List
import args
import calcparser


input: str = args.get_input()

result: float = calcparser.compute(input)

print("resultat: " + str(result))
