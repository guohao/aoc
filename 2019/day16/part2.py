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
print(data[:8])
