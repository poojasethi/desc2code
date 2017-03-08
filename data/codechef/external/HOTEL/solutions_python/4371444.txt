import sys

for t in xrange(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    s = [0] + map(int, sys.stdin.readline().split())
    f = [0] + map(int, sys.stdin.readline().split())
    times = [0]*1001
    for i in xrange(1, n+1):
        for j in xrange(s[i], f[i]):
            times[j] += 1
    
    sl = 0
    for k in times:
        sl = max(sl, k)
    print(sl)

