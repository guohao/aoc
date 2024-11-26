from collections import Counter

d = list(map(int, input().split()))

i = 0


def dfs() -> int:
    t = 0
    global i
    cc = d[i]
    mc = d[i + 1]
    i += 2
    children = [dfs() for _ in range(cc)]
    metadata = d[i:i + mc]
    c = Counter(metadata)
    if not cc:
        t += sum(metadata)
    else:
        t += sum(children[j] * c[j + 1] for j in range(cc) if (j + 1))
    i += mc
    return t


print(dfs())
