from functools import cache


def p1(data: str):
    pipes = []
    for line in data.splitlines():
        a, b = sorted(int(x) for x in line.split('/'))
        pipes.append((a, b))

    @cache
    def dfs(remain: frozenset, cur: int) -> int:
        if not remain:
            return 0
        ans = 0
        for p in remain:
            if cur in set(p):
                lst = list(set(p).difference({cur}))
                if len(lst) > 0:
                    ot = lst[0]
                else:
                    ot = cur
                ans = max(ans, sum(p) + dfs(remain - {p}, ot))
        return ans

    return dfs(frozenset(pipes), 0)


def p2(data: str):
    pipes = []
    for line in data.splitlines():
        a, b = sorted(int(x) for x in line.split('/'))
        pipes.append((a, b))

    @cache
    def dfs(remain: frozenset, cur: int) -> tuple[int, int]:
        if not remain:
            return 0, 0
        ans = 0, 0
        for p in remain:
            if cur in set(p):
                lst = list(set(p).difference({cur}))
                if len(lst) > 0:
                    ot = lst[0]
                else:
                    ot = cur
                sub_long, sub_strength = dfs(remain - {p}, ot)
                sub_long += 1
                sub_strength += sum(p)
                if sub_long > ans[0] or (sub_long == ans[0] and sub_strength > ans[1]):
                    ans = sub_long, sub_strength
        return ans

    return dfs(frozenset(pipes), 0)[1]
