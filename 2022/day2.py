from typing import List

import helper


def pl(lines: List[str]):
    ans1 = 0
    ans2 = 0
    score = {(1, 2): 6, (2, 3): 6, (3, 1): 6,
             (1, 1): 3, (2, 2): 3, (3, 3): 3,
             (1, 3): 0, (3, 2): 0, (2, 1): 0}
    for line in lines:
        # 1 < 2 < 3
        a, b = map(ord, line.split())
        a = a - ord('A') + 1
        c = b - ord('X') + 1
        ans1 += score[(a, c)]
        ans1 += c

        d = (b - ord('X')) * 3
        for k, v in score.items():
            if v == d and k[0] == a:
                ans2 += v
                ans2 += k[1]
    print(ans1)
    print(ans2)


if __name__ == '__main__':
    data = helper.raw_data(2022, 2)
    data = helper.lines(data)
    pl(data)
