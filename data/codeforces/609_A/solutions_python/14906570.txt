n=input()
m=input()
a=[input() for _ in xrange(n)]
i=0
s=0
for e in reversed(sorted(a)):
    s+=e
    i+=1
    if s >= m: break
print i
