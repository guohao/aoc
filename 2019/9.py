import runner


def ic(data: str, fi):
    ns: list[int] = list(map(int, data.strip().split(','))) + [0 for _ in range(1000)]
    rb = 0

    def vo(mode: str, key: int):
        if mode == '0':
            return ns[key]
        elif mode == '1':
            return key
        elif mode == '2':
            return ns[key + rb]
        else:
            raise ValueError(f'{mode} {key}')

    def wo(mode: str, key: int):
        if mode == '0':
            return key
        else:
            return rb + key

    ans = 0
    i = 0
    while i < len(ns):
        op = ns[i] % 100
        if op == 99:
            break
        modes = str(ns[i] // 100).zfill(3)[::-1]
        if op == 1:
            a, b = [vo(modes[j], ns[i + j + 1]) for j in range(2)]
            c = wo(modes[2], ns[i + 3])
            ns[c] = a + b
            i += 4
        elif op == 2:
            a, b = [vo(modes[j], ns[i + j + 1]) for j in range(2)]
            c = wo(modes[2], ns[i + 3])
            ns[c] = a * b
            i += 4
        elif op == 3:
            c = wo(modes[0], ns[i + 1])
            ns[c] = fi
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
            a, b = [vo(modes[j], ns[i + j + 1]) for j in range(2)]
            c = wo(modes[2], ns[i + 3])
            ns[c] = int(a < b)
            i += 4
        elif op == 8:
            a, b = [vo(modes[j], ns[i + j + 1]) for j in range(2)]
            c = wo(modes[2], ns[i + 3])
            ns[c] = int(a == b)
            i += 4
        elif op == 9:
            rb += vo(modes[0], ns[i + 1])
            i += 2
        else:
            assert False
    return ans


def p1(data: str):
    return ic(data, 1)


def p2(data: str):
    return ic(data, 2)
