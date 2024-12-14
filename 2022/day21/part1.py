import sys

lines = [l.strip() for l in sys.stdin.readlines()]

nums = {}
ops = {}

for line in lines:
    name, op = line.split(':')
    if op.strip().isnumeric():
        nums[name] = int(op)
    else:
        a, op, b = op.split()
        ops[name] = (a, op, b)

while 'root' in ops:
    for name, op in ops.copy().items():
        a, op, b = op
        if a in nums and b in nums:
            if op == '+':
                nums[name] = nums[a] + nums[b]
            elif op == '-':
                nums[name] = nums[a] - nums[b]
            elif op == '*':
                nums[name] = nums[a] * nums[b]
            elif op == '/':
                nums[name] = nums[a] // nums[b]
            del ops[name]
print(nums['root'])
