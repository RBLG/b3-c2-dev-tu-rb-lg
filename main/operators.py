from typing import Callable
import re


ops = [
    [r"^\+", lambda p1, p2: p1 + p2],
    [r"^\-", lambda p1, p2: p1 - p2],
    [r"^\*", lambda p1, p2: p1 * p2],
    [r"^\/", lambda p1, p2: p1 / p2],
    [r"^\%", lambda p1, p2: p1 % p2],
    [r"^\^", lambda p1, p2: p1**p2],
]


def parse(payload) -> Callable[[float, float], float] or None:
    for op in ops:
        match = re.search(op[0], payload.line)
        if match is not None:
            payload.line = payload.line[len(match.group(0)) :]
            return op[1]

    return None
