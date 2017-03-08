n, k = map(int, raw_input().split())
f = sorted(list(map(int, raw_input().split())))[::-1]

total = 0
for i in xrange(0, n , k):
    total += 2*(f[i]-1)

print total
