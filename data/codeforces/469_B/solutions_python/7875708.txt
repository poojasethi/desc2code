
p,q,l,r=map(int, raw_input().split())

s = [0] * 2004

for i in xrange(p):
    a,b = map(int, raw_input().split())
    for x in xrange(a,b+1):
        s[x]=1

ans = 0
d = []
for _ in xrange(q):
    a,b = map(int, raw_input().split())
    d.append([a,b])

for i in xrange(l,r+1):
    flag = 0
    for a,b in d:
        if flag:break
        for x in xrange(a, b+1):
            if s[i+x]:
                ans += 1
                flag=1
                break

print ans
