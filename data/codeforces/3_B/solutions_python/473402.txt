n, v = map(int, raw_input().split())

d = [[], []]
for i in xrange(n):
    t, p = map(int, raw_input().split())
    d[t-1] += [(p, i)]

d[0].sort(key=lambda x: x[0])
d[1].sort(key=lambda x: x[0])

r, rn = 0, []
def take(k):
    global v, r, rn
    p, i = d[k].pop()
    v -= k+1
    r += p
    rn.append(str(i+1))

if v % 2 and d[0]:
    take(0)

while v > 1 and d[0] and d[1]:
    if len(d[0]) > 1 and d[0][-1][0]+d[0][-2][0] > d[1][-1][0]:
        take(0)
        take(0)
    elif len(d[0]) == 1 and d[0][-1][0] > d[1][-1][0]:
        take(0)
    else:
        take(1)

while v and d[0]:
    take(0)

while v > 1 and d[1]:
    take(1)

print r
print " ".join(rn)
