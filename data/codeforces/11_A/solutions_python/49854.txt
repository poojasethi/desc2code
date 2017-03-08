n, d = map(int, raw_input().split())
seq = map(int, raw_input().split())
prev = seq[0] - 1
moves = 0
for s in seq:
    if s <= prev:
        m = (prev - s) / d + 1
        moves += m
        prev = s + d * m
    else:
        prev = s
print moves
