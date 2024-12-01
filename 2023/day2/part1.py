import re
import sys

lines = [line.strip() for line in sys.stdin.readlines()]
t = 0
c_max = {
    "blue": 14,
    "green": 13,
    "red": 12
}
for line in lines:
    cells = line.split(':')
    i = int(re.findall(r'-?\d+', cells[0])[0])
    for count, color in map(str.split, re.findall('|'.join(r'\d+ ' + x for x in c_max), cells[1])):
        if c_max[color] < int(count):
            break
    else:
        t += i

print(t)
