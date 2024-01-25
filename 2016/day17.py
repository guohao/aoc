import hashlib

D = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
DS = set(list('UDLR'))

passcode = 'lpvhkcbi'


def bfs(curr, path, shortest):
    if curr == (3, 3):
        return path
    x, y = curr
    if x < 0 or y < 0 or x > 3 or y > 3:
        return None

    door_states = hashlib.md5((passcode + path).encode()).hexdigest()[:4]
    opened = [d for d, s in zip('UDLR', door_states) if int(s, 16) > 10]

    ans = None
    for d in opened:
        dx, dy = D[d]
        sr = bfs((x + dx, y + dy), path + d, shortest)
        if not sr:
            continue
        if not ans:
            ans = sr
        if shortest:
            if len(sr) < len(ans):
                ans = sr
        else:
            if len(sr) > len(ans):
                ans = sr
    return ans


def p1():
    print(bfs((0, 0), '', True))


def p2():
    print(len(bfs((0, 0), '', False)))


p1()
p2()
