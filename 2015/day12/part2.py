import json
import re

d = str(json.loads(input(), object_hook=lambda o: {} if "red" in o.values() else o))
print(sum(map(int, re.findall(r'-?\d+', d))))
