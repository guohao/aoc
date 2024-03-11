from collections import deque


def p1(data: str):
    seq = deque(list(map(int, data.split())))

    def parse():
        cc = seq.popleft()
        mc = seq.popleft()
        ans = 0
        for _ in range(cc):
            ans += parse()
        for _ in range(mc):
            ans += seq.popleft()
        return ans

    return parse()


def p2(data: str):
    seq = deque(list(map(int, data.split())))

    def parse():
        cc = seq.popleft()
        mc = seq.popleft()
        children = [parse() for _ in range(cc)]
        mds = [seq.popleft() for _ in range(mc)]
        if cc == 0:
            return sum(mds)
        return sum(children[mi - 1] for mi in mds if mi in range(1, len(children) + 1))

    return parse()
