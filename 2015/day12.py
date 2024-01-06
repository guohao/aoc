import json

from helper import *

data = raw_data(2015, 12)
lines = lines(data)

# print(sum(nums(data)))
jo = json.loads(data)


def dfs(j) -> int:
    if isinstance(j, list):
        return sum(dfs(child) for child in j)
    else:
        if isinstance(j, int):
            return j
        else:
            if isinstance(j, str):
                if j.isnumeric():
                    return int(j)
                else:
                    return 0
            if 'red' in j.values():
                return 0
            else:
                return sum(dfs(child) for child in j.values())


print(dfs(jo))
