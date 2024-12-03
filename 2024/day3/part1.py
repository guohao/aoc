import math
import re
import sys

print(sum(math.prod(map(int, m)) for m in re.findall(r'mul\((\d+),(\d+)\)', sys.stdin.read())))
