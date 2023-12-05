import re
from collections import defaultdict

from common import io_utils


def pr(lines: str):
    ans1 = 0
    ans2 = 0
    bs, ms = lines.split("\n\n")
    d = defaultdict(list)
    for i, line in enumerate(bs.splitlines()):
        for j, c in enumerate(line):
            d[j].append(c)

    for k, v in d.copy().items():
        if not v[-1].isalpha():
            del d[k]
        else:
            d[k] = list(reversed(v))

    for move in ms.splitlines():
        a, b, c = re.findall(r'\d+', move)
        for i in range(int(a)):
            d[int(c)].append(d[int(b)].pop())

    print(map(list[-1], d.values()))

    print(ans1)
    print(ans2)
    pass


if __name__ == '__main__':
    data = io_utils.get_data(2022, 5)
    data = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
    """
    pr(data)
    data = io_utils.raw_str_to_lines(data)
    pl(data)
