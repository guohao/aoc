import hashlib
from collections import deque


def p1(data: str):
    pc = data.strip()
    start = (1, 1)
    target = (4, 4)
    ss = {''}
    while True:
        nss = set()
        for s in ss:
            x, y = start
            for c in s:
                match c:
                    case 'U':
                        x -= 1
                    case 'D':
                        x += 1
                    case 'L':
                        y -= 1
                    case 'R':
                        y += 1
                if (x, y) == target:
                    return s
            UDLR = hashlib.md5((pc + s).encode()).hexdigest()[:4]
            for i in range(len(UDLR)):
                if 'a' < UDLR[i] <= 'f':
                    nss.add(s + 'UDLR'[i])
        ss = nss


def p2(data: str):
    pc = data.strip()
    start = (1, 1)
    target = (4, 4)
    q = deque()
    q.append(('', start))
    ans = 0
    while q:
        path, (x, y) = q.popleft()
        if (x, y) == target:
            ans = max(ans, len(path))
            continue
        UDLR = hashlib.md5((pc + path).encode()).hexdigest()[:4]
        for i in range(4):
            if 'a' < UDLR[i] <= 'f':
                nx, ny = x, y
                if i == 0:
                    nx -= 1
                elif i == 1:
                    nx += 1
                elif i == 2:
                    ny -= 1
                elif i == 3:
                    ny += 1
                if 1 <= nx <= 4 and 1 <= ny <= 4:
                    q.append((path + 'UDLR'[i], (nx, ny)))
    return ans
