n, houses = int(raw_input()), map(int, raw_input().split())
m, l = houses[n-1], [0]
for i in xrange(n-2, -1, -1):
    l.append(0 if houses[i] > m else m + 1 - houses[i])
    m = max(m, houses[i])
print ' '.join(map(str, reversed(l)))
