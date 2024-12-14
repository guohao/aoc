def fft(s: str):
    s = '0' + s
    out = ''
    cums = [0]
    for x in s:
        cums.append(cums[-1] + int(x))
    for i in range(len(s)):
        total = 0
        step = i + 1
        for j in range(0, len(s), 4 * step):
            total += cums[min(j + 2 * step, len(s))] - cums[min(j + step, len(s))]
            total -= cums[min(j + 4 * step, len(s))] - cums[min(j + 3 * step, len(s))]
        out += str(total)[-1]
    return out


import sys
data = sys.stdin.read().strip()

    data = data.strip()
    for _ in range(100):
        data = fft(data)
    return data[:8]


import sys
data = sys.stdin.read().strip()

    data = (data.strip() * 10000)[int(data[:7]):]

    def fft2(s: str):
        out = ''
        cum = 0
        for i in s[::-1]:
            cum += int(i)
            out = str(cum)[-1] + out
        return out

    for t in range(100):
        data = fft2(data)
    return data[:8]
