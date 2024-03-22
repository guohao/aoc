import re


def p1ss(line: str):
    m = re.fullmatch(r'([a-z-]+)(\d+)\[(\w+)]', line)
    s, sid, cs = m.groups()
    s = s.replace('-', '')
    b = sorted(set(s), key=lambda x: (-s.count(x), x))[:5]
    if list(cs) == b:
        return int(sid)
    return 0


def p2(data: str):
    for line in data.splitlines():
        m = re.fullmatch(r'([a-z-]+)(\d+)\[(\w+)]', line)
        s, sid, cs = m.groups()
        offset = int(sid) % 26
        ans = ''
        for c in s:
            if c == '-':
                ans += ' '
            else:
                ans += chr(ord('a') + (ord(c) - ord('a') + offset) % 26)
        if 'northpole' in ans:
            return sid
