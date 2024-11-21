import re

s = input()
for _ in range(40):
    s = re.sub(r'(\d)\1*', lambda m: str(m.end() - m.start()) + m.group(1), s)
print(len(s))
