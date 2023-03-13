from ast import List
import args


input: str = args.get_input()

result: float = args.compute(input)

print("resultat: " + result)
