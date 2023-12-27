import helper

ans1 = 0
ans2 = 0
for part in helper.raw_data(2023, 13).strip().split('\n\n'):
    lines = helper.lines(part)
    for i in range(1, len(lines)):
        if i * 2 < len(lines):
            size = i
        else:
            size = len(lines) - i
        up = lines[i - size:i]
        down = lines[i:i + size][::-1]
        # if up == down:
        diff_count = 0
        for j in range(len(lines[0])):
            diff_count += sum(1 for k in range(size) if up[k][j] != down[k][j])
        if diff_count == 0:
            ans1 += 100 * i
        if diff_count == 1:
            ans2 += 100 * i

    for j in range(1, len(lines[0])):
        size = min(j, len(lines[0]) - j)
        diff_count = 0
        for i in range(len(lines)):
            left = lines[i][j - size:j]
            right = lines[i][j:j + size][::-1]
            diff_count += sum(1 for k in range(size) if left[k] != right[k])
        if diff_count == 0:
            ans1 += j
        if diff_count == 1:
            ans2 += j

print(ans1)
print(ans2)
