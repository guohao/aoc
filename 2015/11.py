def p1(data: str):
    data = data.strip()
    atz = [chr(ord('a') + i) for i in range(26)]

    def is_valid(s: str) -> bool:
        increasings = [atz[i] + atz[i + 1] + atz[i + 2] for i in range(24)]
        pairs = [c * 2 for c in atz]
        if any(inc in s for inc in increasings):
            if not any(c in s for c in 'iol'):
                if any(a in s and b in s for a in pairs for b in pairs if a != b):
                    return True
        return False

    def gen(s: str) -> str:
        l = list(s)
        for i in range(len(s) - 1, 0, -1):
            l[i] = atz[(atz.index(l[i]) + 1) % 26]
            if l[i] != 'a':
                break
        return ''.join(l)

    while True:
        data = gen(data)
        if is_valid(data):
            return data


def p2(data):
    return p1(p1(data))
