
n = int(raw_input())
ans = 0
l = 0
ot = 0
for i in xrange(n):
    tmp = raw_input().split(' ')
    t = int(tmp[0])
    c = int(tmp[1])
    l -= (t - ot)
    ot = t
    if l < 0:
        l = 0
    l += c
    if l > ans:
        ans = l

print l + t, ans

