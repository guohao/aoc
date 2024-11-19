import re

print(sum(int(x) for x in re.findall(r'-?\d+', input())))
