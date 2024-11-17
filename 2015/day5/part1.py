import string

r = 0
while True:
    s = input()
    if not s:
        break
    if 3 > sum(s.count(x) for x in 'aeiou'):
        continue
    if not any(x * 2 in s for x in string.ascii_lowercase):
        continue
    if any(x in s for x in ['ab', 'cd', 'pq', 'xy']):
        continue
    r += 1
print(r)
