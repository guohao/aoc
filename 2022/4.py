import re


def p1ss(line: str):
    a, b, c, d = list(map(int, re.findall(r'\d+', line)))
    return (a - c) * (d - b) >= 0


def p2ss(line: str):
    a, b, c, d = list(map(int, re.findall(r'\d+', line)))
    return a <= d and c <= b
