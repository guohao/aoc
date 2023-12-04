import re
from typing import List

from common import io_utils


def pr(lines: str):
    ans1 = max(sum(map(int, re.findall(r'\d+', line))) for line in lines.split('\n\n'))

    ans = []
    for line in lines.split('\n\n'):
        ans.append(sum(map(int, re.findall(r'\d+', line))))
    ans2 = sum(sorted(ans)[-3:])
    print(ans1)
    print(ans2)


def pl(lines: List[str]):
    ans1 = 0
    ans2 = 0
    for i, line in enumerate(lines):
        pass

    print(ans1)
    print(ans2)
    pass


if __name__ == '__main__':
    data = io_utils.get_data(2022, 1)
    pr(data)
