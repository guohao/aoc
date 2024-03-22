import re


def p1ss(line: str):
    if re.search(r'\[\w*(\w)(?!\1)(\w)\2\1\w*]', line):
        return False
    if not re.search(r'(\w)(?!\1)(\w)\2\1', line):
        return False
    return True


def p2ss(line: str):
    for inner in re.findall(r'\[\w*]', line):
        for m in re.finditer(r'(?=(\w)(?!\1)(\w)\1)', inner):
            a, b = m.groups()
            bab = b + a + b
            if any(bab in outer for outer in re.split(r'\[\w*]', line)):
                return True
    return False
