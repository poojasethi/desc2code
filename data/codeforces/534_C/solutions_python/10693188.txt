# coding =utf-8
n, a = map(int, raw_input().split())
ds = map(int, raw_input().split())
s = sum(ds)

for d in ds:
    x, y = a-n+1, a-s+d
    print d - min(x, d) + max(y, 1) - 1,