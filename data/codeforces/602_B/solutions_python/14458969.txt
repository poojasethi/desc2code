n = int(input())
x = [int(_) for _ in raw_input().split()]

lmax = 0

last_i, last_d = 0, 0
cur_i, cur_d = 0, 0

for i in range(1, n):
    d = x[i] - x[i-1]
    if d == 0: continue
    if d == last_d or last_d == 0: # jump in same direction
        lmax = max(lmax, i - cur_i)
        cur_i, cur_d = last_i, last_d
    last_i, last_d = i, d

print max(lmax, n - cur_i)
