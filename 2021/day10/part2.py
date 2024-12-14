import sys
from collections import deque

t = 0
lines = [l.strip() for l in sys.stdin.readlines()]

def score_of(line: str):
    q = deque()
    pairs = {'{': '}', '(': ')', '<': '>', '[': ']'}
    points = {'(': 1, '[': 2, '{': 3, '<': 4}
    for c in line:
        if c in '[{<(':
            q.append(c)
        else:
            if pairs[q[-1]] != c:
                return 0
            else:
                q.pop()
    ans = 0
    while q:
        ans = ans * 5 + points[q.pop()]
    print(ans)


seq = list(filter(lambda x: x > 0, map(score_of, lines)))
print(seq[len(seq) // 2])
