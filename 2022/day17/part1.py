import sys

data = sys.stdin.read().strip()
JETS = list(map({'<': -1, '>': 1}.get, list(data.strip())))
ROCKS = [
    [1, 1, 1, 1],
    [2, 7, 2],
    [1, 1, 7],
    [15],
    [3, 3]
]

N = 7
G = [0] * N


def can_move(rock, left, down):
    if down < 0:
        return False
    if left < 0 or left + len(rock) > N:
        return False
    if any(G[left + j] & (rock[j] << down) for j in range(len(rock))):
        return False
    return True


def do_move(rock, left, down):
    for j in range(len(rock)):
        G[left + j] |= rock[j] << down


epoch = 2022
ans = 0
height = 0
i = 1
ji = -1
ri = -1
memo = {}
while i <= epoch:
    down = height + 3
    ri = (ri + 1) % len(ROCKS)
    rock = ROCKS[ri]
    left = 2
    while True:
        ji = (ji + 1) % len(JETS)
        move = JETS[ji]
        if can_move(rock, left + move, down):
            left += move
        if can_move(rock, left, down - 1):
            down -= 1
        else:
            break
    do_move(rock, left, down)
    height = max(height, down + max(rock).bit_length())
    state = (ji, ri, tuple(height - G[j].bit_length() for j in range(N)))
    if state in memo:
        prev_i, prev_height = memo[state]
        cut_down_times = (epoch - i) // (i - prev_i)
        ans += cut_down_times * (height - prev_height)
        epoch -= cut_down_times * (i - prev_i)
    else:
        memo[state] = i, height
    i += 1

print(height + ans)
