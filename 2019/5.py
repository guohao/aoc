def p1(data: str):
    ns = list(map(int, data.strip().split(',')))
    ii = 1
    i = 0

    def vo(mode: str, key: int):
        if mode == '0':
            return ns[key]
        else:
            return key

    ans = 0
    while i < len(ns):
        op = ns[i] % 100
        modes = str(ns[i] // 100).zfill(3)[::-1]
        if op == 1:
            ns[ns[i + 3]] = vo(modes[0], ns[i + 1]) + vo(modes[1], ns[i + 2])
            i += 4
        elif op == 2:
            ns[ns[i + 3]] = vo(modes[0], ns[i + 1]) * vo(modes[1], ns[i + 2])
            i += 4
        elif op == 3:
            ns[ns[i + 1]] = ii
            i += 2
        elif op == 4:
            ans = vo(modes[0], ns[i + 1])
            i += 2
        else:
            break
    return ans


def p2(data: str):
    ns: list[int] = list(map(int, data.strip().split(',')))
    ii = 5
    i = 0

    def vo(mode: str, key: int):
        if mode == '0':
            return ns[key]
        else:
            return key

    ans = 0
    while i < len(ns):
        op = ns[i] % 100
        modes = str(ns[i] // 100).zfill(3)[::-1]
        if op == 1:
            ns[ns[i + 3]] = vo(modes[0], ns[i + 1]) + vo(modes[1], ns[i + 2])
            i += 4
        elif op == 2:
            ns[ns[i + 3]] = vo(modes[0], ns[i + 1]) * vo(modes[1], ns[i + 2])
            i += 4
        elif op == 3:
            ns[ns[i + 1]] = ii
            i += 2
        elif op == 4:
            ans = vo(modes[0], ns[i + 1])
            i += 2
        elif op == 5:
            if vo(modes[0], ns[i + 1]):
                i = vo(modes[1], ns[i + 2])
            else:
                i += 3
        elif op == 6:
            if not vo(modes[0], ns[i + 1]):
                i = vo(modes[1], ns[i + 2])
            else:
                i += 3
        elif op == 7:
            ns[ns[i + 3]] = int(vo(modes[0], ns[i + 1]) < vo(modes[1], ns[i + 2]))
            i += 4
        elif op == 8:
            ns[ns[i + 3]] = int(vo(modes[0], ns[i + 1]) == vo(modes[1], ns[i + 2]))
            i += 4
        else:
            break
    return ans
