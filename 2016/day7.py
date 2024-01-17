from helper import *

data = raw_data(2016, 7)
lines = lines(data)


def is_abba(s: str):
    m = re.search(r'(\w)(\w)\2\1', s)
    return m and m.group(1) != m.group(2)


def p1():
    ans = 0
    for line in lines:
        if any(is_abba(x) for x in re.findall(r'\[(\w+)]', line)):
            continue
        if any(is_abba(x) for x in re.split(r'\[\w+]', line)):
            ans += 1
    print(ans)


def has_aba(line) -> bool:
    hns = re.findall(r'\[(\w+)]', line)
    sns = re.split(r'\[\w+]', line)
    for hn in hns:
        for i in range(len(hn) - 2):
            if hn[i] == hn[i + 2] and hn[i] != hn[i + 1]:
                if any(hn[i + 1] + hn[i] + hn[i + 1] in x for x in sns):
                    return True
    return False


def p2():
    ans = 0
    for line in lines:
        if has_aba(line):
            ans += 1
    print(ans)


p1()
p2()
