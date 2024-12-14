import sys
from collections import deque

t = 0
q = deque()
pairs = {'{': '}', '(': ')', '<': '>', '[': ']'}
points = {')': 3, ']': 57, '}': 1197, '>': 25137}
lines = [l.strip() for l in sys.stdin.readlines()]

for line in lines:
    for c in line:
        if c in '[{<(':
            q.append(c)
        else:
            if pairs[q[-1]] != c:
                t += points[c]
                break
            else:
                q.pop()
print(t)
