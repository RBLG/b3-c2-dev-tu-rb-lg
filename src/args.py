import sys

######################################################################

def get_input() -> str:
    input: str = ""
    args = sys.argv.copy()
    args.pop(0)
    for arg in args:
        input += arg + " "

    return input
