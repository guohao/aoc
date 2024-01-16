from collections import defaultdict

from helper import *

data = raw_data(2016, 4)


def decrypt(name, shift):
    return ''.join([chr((ord(ch) - ord('a') + shift) % 26 + ord('a')) for ch in name])


ans = 0
for line in lines(data):
    checksum = re.search(r'\[(\w+)]', line).group(1)
    sector_id = int(re.search(r'(\d+)', line).group(1))
    names = line[:line.rindex('-')].split('-')
    counter = defaultdict(lambda: 0)
    for name in names:
        for ch in name:
            counter[ch] += 1
    mc = list(counter.keys())
    mc.sort(key=lambda x: (-counter[x], x))
    mc = mc[:5]
    counts = [counter[x] for x in mc]
    if mc == list(checksum):
        ans += sector_id
    real_name = ' '.join(decrypt(name, sector_id) for name in names)
    if "pole" in real_name:
        print(sector_id)

print(ans)
