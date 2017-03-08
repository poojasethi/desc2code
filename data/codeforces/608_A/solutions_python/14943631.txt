n,s=map(int,raw_input().split())
ft=[(0,0) for _ in xrange(n)]
for i in xrange(n):
    ft[i] = map(int,raw_input().split())
curf = s
curt = 0
for f,t in sorted(ft, key=lambda x: x[0], reverse=True):
    curt += curf-f
    curf = f
    if curt < t: curt = t
print curt + curf
