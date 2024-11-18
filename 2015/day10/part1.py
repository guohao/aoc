import re


def gen(s: str) -> str:
    new = ''
    for m in re.finditer(r'(\d)\1*', s):
        new += str(m.end() - m.start()) + m.group(1)
    return new


data = input()
for i in range(40):
    data = gen(data)
print(len(data))
