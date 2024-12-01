ns = [int(x) for x in input().split(',')]
ns[1] = 12
ns[2] = 2
i = 0
while True:
    if ns[i] == 99:
        break
    if ns[i] == 1:
        ns[ns[i + 3]] = ns[ns[i + 1]] + ns[ns[i + 2]]
    else:
        ns[ns[i + 3]] = ns[ns[i + 1]] * ns[ns[i + 2]]
    i += 4
print(ns[0])
