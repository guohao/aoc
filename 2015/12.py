import re
import json


def p1(data: str):
    return sum(map(int, re.findall(r'-?\d+', data)))


def p2(data: str):
    def sum_without_red(j):
        if isinstance(j, int):
            return int(j)
        if isinstance(j, str):
            return 0
        if isinstance(j, list):
            return sum(sum_without_red(i) for i in j)
        if isinstance(j, dict):
            if 'red' in j.values():
                return 0
            ans = 0
            for k, v in j.items():
                ans += sum_without_red(k)
                ans += sum_without_red(v)
            return ans

    return sum_without_red(json.loads(data))
