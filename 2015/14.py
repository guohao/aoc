import re
from collections import Counter


def sec_record(data: str, sec):
    record = []
    for i, line in enumerate(data.splitlines()):
        s, rd, sd = list(map(int, re.findall(r'\d+', line)))
        distance = s * ((sec // (sd + rd) * rd) + min(sec % (sd + rd), rd))
        record.append((distance, i))
    record.sort(reverse=True, key=lambda x: x[0])
    return record


def p1(data: str):
    return sec_record(data, 2503)[0][0]


def p2(data: str):
    c = Counter()
    for sec in range(1, 2504):
        record = sec_record(data, sec)
        for d, i in record:
            if d == record[0][0]:
                c[i] += 1
    return max(c.values())
