from typing import List

from day import Day


class Day3(Day):

    def __init__(self):
        super().__init__(day=3)

    def part_one(self, lines: List[str]) -> int:
        ret = 0
        for i in range(len(lines)):
            line = lines[i]
            n = 0
            j = 0
            while j < len(line):
                if line[j].isdigit():
                    st = j
                    while j < len(line) and line[j].isdigit():
                        n = n * 10 + int(line[j])
                        j = j + 1
                    end = j
                    cs = max(st - 1, 0)
                    ce = min(end + 1, len(line))
                    rs = max(i - 1, 0)
                    re = min(i + 2, len(lines))
                    valid = False
                    for k in range(rs, re):
                        if valid:
                            break
                        for m in range(cs, ce):
                            if k == i and (st <= m < end):
                                continue
                            if not lines[k][m].isdigit() and lines[k][m] != '.':
                                valid = True
                                break
                    if valid:
                        ret += n
                else:
                    n = 0
                    j = j + 1
        return ret

    def part_two(self, lines: List[str]) -> int:
        ret = 0
        d = dict()
        for i in range(len(lines)):
            line = lines[i]
            n = 0
            j = 0
            while j < len(line):
                if line[j].isdigit():
                    st = j
                    while j < len(line) and line[j].isdigit():
                        n = n * 10 + int(line[j])
                        j = j + 1
                    end = j
                    cs = max(st - 1, 0)
                    ce = min(end + 1, len(line))
                    rs = max(i - 1, 0)
                    re = min(i + 2, len(lines))
                    for k in range(rs, re):
                        for m in range(cs, ce):
                            if k == i and (st <= m < end):
                                continue
                            if not lines[k][m].isdigit() and lines[k][m] == '*':
                                key = (k, m)
                                if key not in d:
                                    d[key] = []
                                d[key].append(n)
                else:
                    n = 0
                    j = j + 1
        for k in d.keys():
            v = d[k]
            if len(v) == 2:
                ret += v[0] * v[1]
        return ret


if __name__ == '__main__':
    Day3().run()
