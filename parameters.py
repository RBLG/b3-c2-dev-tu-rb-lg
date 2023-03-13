import re
import args


params = [
    ["^[_0-9]+", lambda match, payload: float(match.group(0))],
    ["^\(", lambda match, payload: args.parse_nest(payload, True)],
]


def parse(payload) -> float or None:
    for param in params:
        match = re.search(param[0], payload.line)
        if match is not None:
            payload.line = payload.line[len(match.group(0)) :]
            return param[1](match, payload)

    return None
