import sys

n = int(sys.stdin.readline())
f = sys.stdin.readline().split(' ')
n = len(f)
k = 0
m = {}
for item in f:
    k += 1
    m[int(item)] = k
ans = 0
for i in xrange(1, n):
    ans += abs(m[i + 1] - m[i])
print ans
