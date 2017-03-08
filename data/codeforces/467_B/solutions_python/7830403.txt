
n,m,k = map(int, raw_input().split())

s = []
for i in xrange(m+1):
    s.append(int(raw_input()))


ans=0
for i in xrange(m):
    r=s[i]^s[m]
    cnt=0
    while r:
        if r%2:
            cnt += 1
        r/=2
    if cnt <= k:
        ans += 1

print ans
