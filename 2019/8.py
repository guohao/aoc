from collections import Counter


import sys
data = sys.stdin.read().strip()

    ns = data.strip()
    layers = len(ns) // (25 * 6)
    ans = 0
    zc = len(ns)
    for i in range(0, layers * 150, 150):
        c = Counter(ns[i:i + 150])
        if c['0'] < zc:
            zc = c['0']
            ans = c['1'] * c['2']
    print(ans)


import sys
data = sys.stdin.read().strip()

    ns = data.strip()
    layers = len(ns) // (25 * 6)
    img = ['2' for _ in range(150)]
    for i in range(layers):
        layer = ns[i * 150:(i + 1) * 150]
        for i in range(150):
            if img[i] == '2':
                img[i] = layer[i]
    for i in range(6):
        line = ''
        for c in img[i * 25:(i + 1) * 25]:
            if c == '0':
                line += ' '
            else:
                line += '#'
        print(line)
