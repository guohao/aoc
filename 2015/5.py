import re


def p1ss(line: str):
    if sum(line.count(c) for c in 'aeiou') < 3:
        return 0
    if not re.search(r'(\w)\1', line):
        return 0
    if any(c in line for c in ['ab', 'cd', 'pq', 'xy']):
        return 0
    return 1


def p2ss(line: str):
    if not re.search(r'(\w{2}).*\1', line):
        return 0
    if not re.search(r'(\w)\w\1', line):
        return 0
    return 1
