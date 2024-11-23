import regex
import sys

lines = [line.strip() for line in sys.stdin.readlines()]
t = 0
for line in lines:
    t +=sum(map(int,regex.findall(r'(\d)\1', line + line[0], overlapped=True)))
print(t)
