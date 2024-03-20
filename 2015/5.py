import re


def p1ss(line: str):
    return (sum(line.count(c) for c in 'aeiou') >= 3 and re.search(r'(\w)\1', line) is not None
            and all(c not in line for c in ['ab', 'cd', 'pq', 'xy']))


def p2ss(line: str):
    return (re.search(r'(\w{2}).*\1', line) is not None
            and re.search(r'(\w)\w\1', line) is not None)
