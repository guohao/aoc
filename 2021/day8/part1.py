import sys

print(len(list(p for line in sys.stdin.readlines() for p in line.strip().split('|')[1].split() if len(p) in (2, 3, 4, 7))))
