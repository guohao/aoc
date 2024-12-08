import re
import sys


def h(s):
    v = 0
    for c in s:
        v += ord(c)
        v *= 17
        v %= 256
    return v


boxes = [{} for _ in range(256)]
for part in sys.stdin.read().split(','):
    label = re.findall(r'\w+', part)[0]
    box = boxes[h(label)]
    if '-' in part:
        if label not in box:
            continue
        _, order = box[label]
        del box[label]
        for other in box.keys():
            other_order = box[other][1]
            if other_order > order:
                box[other] = (box[other][0], other_order - 1)
    else:
        lens = int(next(re.finditer(r'\d+', part)).group())
        if label in box:
            box[label] = (lens, box[label][1])
        else:
            box[label] = (lens, len(box) + 1)
ans = 0
for i, box in enumerate(boxes, start=1):
    for label, (lens, order) in box.items():
        ans += lens * i * order
print(ans)
