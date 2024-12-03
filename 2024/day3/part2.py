import sys
import re

lines = sys.stdin.readlines()
lines = [line.strip() for line in lines]
t = 0

e = True
for line in lines:
    for m in re.finditer(r"do\(\)|don't\(\)|mul\((\d+),(\d+)\)", line):
        if 'don' in m.group():
            e = False
        elif 'do' in m.group():
            e = True
        else:
            if e:
                t += int(m.group(1)) * int(m.group(2))

print(t)
