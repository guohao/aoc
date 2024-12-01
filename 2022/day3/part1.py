import sys

lines = [line.strip() for line in sys.stdin.readlines()]
t = 0
for line in lines:
    n = len(line) // 2
    a = line[:n]
    b = line[n:]
    c = list(set(a) & set(b))[0]
    t += ord(c) + 1
    if 'a' <= c <= 'z':
        t -= ord('a')
    else:
        t -= ord('A')
        t += 26
print(t)
