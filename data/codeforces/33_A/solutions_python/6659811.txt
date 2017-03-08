n, m, k = map(int, raw_input().split())
viability = [10 ** 6 for i in xrange(m)]

for i in xrange(n):
    row, via = map(int, raw_input().split())
    viability[row-1] = min(viability[row-1], via)
print min(sum(viability), k)