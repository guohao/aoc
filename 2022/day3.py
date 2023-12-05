from typing import List

from common import io_utils


def pl(lines: List[str]):
    ans1 = 0
    ans2 = 0
    for i in range(0, len(lines), 3):
        a = lines[i]
        b = lines[i + 1]
        c = lines[i + 2]
        m = ord(list(set(a) & set(b) & set(c))[0])
        ans2 += m - ord('a') + 1 if ord('a') <= m <= ord('z') else 0
        ans2 += m - ord('A') + 27 if ord('A') <= m <= ord('Z') else 0

    for i, line in enumerate(lines):
        mid = len(line) // 2
        a = line[:mid]
        b = line[mid:]
        m = ord(list(set(a) & set(b))[0])
        ans1 += m - ord('a') + 1 if ord('a') <= m <= ord('z') else 0
        ans1 += m - ord('A') + 27 if ord('A') <= m <= ord('Z') else 0

    print(ans1)
    print(ans2)
    pass


if __name__ == '__main__':
    data = io_utils.get_data(2022, 3)
    data = io_utils.raw_str_to_lines(data)
    pl(data)
