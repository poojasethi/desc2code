n, m = map(int, raw_input().split())
a = map(int, raw_input().split())
c = max(a)
rds = c / m
if c % m == 0:
    rds -= 1

print [(i, x) for (i, x) in enumerate(a) if x - rds*m > 0][-1][0] + 1
