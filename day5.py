from typing import List

from common import io_utils


def pr(lines: str):
    ans1 = 0
    ans2 = 0

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
    data = io_utils.get_data(5)
    pr(data)
    data = io_utils.raw_str_to_lines(data)
    pl(data)
