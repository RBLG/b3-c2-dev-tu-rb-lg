from typing import Callable
import re


class EndOfNest:
    pass


class EndOfAll:
    pass


ops = [
    [r"^\+", lambda p1, p2: p1 + p2],
    [r"^\-", lambda p1, p2: p1 - p2],
    [r"^\*", lambda p1, p2: p1 * p2],
    [r"^\/", lambda p1, p2: p1 / p2],
    [r"^\%", lambda p1, p2: p1 % p2],
    [r"^\^", lambda p1, p2: p1**p2],
    [r"^\)", EndOfNest()],
    [r"^$", EndOfAll()],
]


def parse(payload) -> Callable[[float, float], float] or EndOfNest or EndOfAll or None:
    for op in ops:
        match = re.search(op[0], payload.line)
        if match is not None:
            payload.line = payload.line[len(match.group(0)) :]
            return op[1]

    return None


def parse_end_of_nest(payload) -> bool:
    found = re.search(r"^\)", payload.line) is not None
    if found:
        payload.line = payload.line[len(1) :]
    return found

def parse_end_of_input(payload) -> bool:
    found = re.search(r"^\)", payload.line) is not None
    if found:
        payload.line = payload.line[len(1) :]
    return found
