from helper import *

data = raw_data(2023, 5)
lines = lines(data)


def mapping(prev: List[tuple[int, int]]):
    for part in data.split('\n\n')[1:]:
        cur = []
        for m in part.splitlines()[1:]:
            target, source, ranges = nums(m)
            for start, end in prev.copy():
                left = max(start, source)
                right = min(end, source + ranges)
                if left < right:
                    prev.remove((start, end))
                    cur.append((target + left - source, target + right - source))
                    if start < source:
                        prev.append((start, source))
                    if end > source + ranges:
                        prev.append((source + ranges, end))
        for changed in cur:
            prev.append(changed)
    print(min(map(lambda x: x[0], prev)))


seeds = nums(lines[0])
mapping([(x, x + 1) for x in seeds])
mapping([(seeds[i], seeds[i + 1] + seeds[i]) for i in range(0, len(seeds), 2)])
