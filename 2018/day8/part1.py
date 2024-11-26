d = list(map(int, input().split()))

t = 0
i = 0


def dfs():
    global t
    global i
    cc = d[i]
    mc = d[i + 1]
    i += 2
    for _ in range(cc):
        dfs()
    t += sum(d[i:i + mc])
    i += mc


dfs()
print(t)
