import sys
import re

lines = sys.stdin.readlines()
lines = [line.strip() for line in lines]
t = 0

for line in lines:
    for m in re.finditer(r'mul\((\d+),(\d+)\)', line):
        t += int(m.group(1)) * int(m.group(2))
print(t)
