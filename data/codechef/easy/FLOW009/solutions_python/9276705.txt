T = int(raw_input())

for i in range(T):
    q, p = map(int, raw_input().split())
    if q > 1000:
        print '%.6f' % (q * p * 0.9)
    else:
        print '%.6f' % (q * p * 1.0)
