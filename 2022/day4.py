from typing import List

import helper


def pl(lines: List[str]):
    ans1 = 0
    ans2 = 0
    for line in lines:
        a, b = line.split(',')
        a = list(map(int, a.split('-')))
        b = list(map(int, b.split('-')))
        if (a[0] - b[0]) * (a[1] - b[1]) <= 0:
            ans1 += 1
        if (a[0] - b[1]) * (a[1] - b[0]) <= 0:
            ans2 += 1

    print(ans1)
    print(ans2)
    pass


if __name__ == '__main__':
    data = helper.raw_data(2022, 4)
    data = helper.lines(data)
    pl(data)
