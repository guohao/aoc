from helper import *

data = raw_data(2023, 15).strip()


def hash(s):
    val = 0
    for c in s:
        val += ord(c)
        val *= 17
        val %= 256
    return val


print(sum(hash(d) for d in data.split(',')))

boxes = [{} for _ in range(256)]
for part in data.split(','):
    label = next(re.finditer(r'\w+', part)).group()
    box = boxes[hash(label)]
    if '-' in part:
        if label not in box:
            continue
        (_, order) = box[label]
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
