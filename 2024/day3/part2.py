import re
import sys

s = sys.stdin.read()
t = 0

e = True
for m in re.finditer(r"do\(\)|don't\(\)|mul\((\d+),(\d+)\)", s):
    if 'don' in m.group():
        e = False
    elif 'do' in m.group():
        e = True
    else:
        if e:
            t += int(m.group(1)) * int(m.group(2))

print(t)
