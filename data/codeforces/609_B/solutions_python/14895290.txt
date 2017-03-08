n, m = map(int, raw_input().split())

s = map(int, raw_input().split())

c = dict()

for key in s:
    if key in c:
        c[key] += 1
    else:
        c[key] = 1

ans = (n*n - n)/2

for key in c:
    ans -= (c[key]*c[key] - c[key])/2

print ans
