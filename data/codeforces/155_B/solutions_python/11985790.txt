n = input()
d = [map(int,raw_input().split()) for x in xrange(n)]
c, s = 1, 0
for a, b in sorted(d, key=lambda x: (x[1], x[0]))[::-1]:
    s += a
    c += b
    c -= 1
    if c <= 0:
        break
print s
