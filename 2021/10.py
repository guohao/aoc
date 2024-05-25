from collections import deque

import util


def p1ss(line: str):
    q = deque()
    pairs = {'{': '}', '(': ')', '<': '>', '[': ']'}
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    for c in line:
        if c in '[{<(':
            q.append(c)
        else:
            if pairs[q[-1]] != c:
                return points[c]
            else:
                q.pop()
    return 0


def p2(data: str):
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
        return ans

    seq = filter(lambda x: x > 0, map(score_of, data.splitlines()))
    return myutil.median(seq)
