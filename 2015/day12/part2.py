import json


def sum_of(o):
    if isinstance(o, dict):
        if 'red' not in o.values():
            return sum(sum_of(x) for x in list(o.keys()) + list(o.values()))
    elif isinstance(o, list):
        return sum(sum_of(x) for x in o)
    elif isinstance(o, int):
        return int(o)
    return 0


print(sum_of(json.loads(input())))
