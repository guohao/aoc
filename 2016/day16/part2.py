import re

d = input()
n = 35651584
while len(d) < n:
    d = d + '0' + re.sub(r'\d', lambda m: str(1 - int(m.group())), d[::-1])

d = d[:n]
while True:
    d = re.sub(r'(\d)(\d)', lambda m: str(int(m.group(1) == m.group(2))), d)
    if len(d) % 2:
        print(d)
        break
