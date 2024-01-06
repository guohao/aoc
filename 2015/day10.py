def las(s: str) -> str:
    r = ''
    i = 0
    while i < len(s):
        c = s[i]
        cnt = 1
        for j in range(i + 1, len(s)):
            if s[j] != c:
                break
            else:
                cnt += 1
        r += str(cnt) + c
        i += cnt
    return r


input = "1113122113"
for _ in range(40):
    print(len(input))
    input = las(input)
print(len(input))
for _ in range(10):
    input = las(input)
print(len(input))
