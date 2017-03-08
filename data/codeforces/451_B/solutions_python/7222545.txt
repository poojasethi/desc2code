import sys

n = int(raw_input())
a = [int(x) for x in raw_input().split(' ')]

b = sorted(a)
f, t = 0, 0


for i in xrange(n):
    if a[i] != b[i]:
        f = i
        break
for i in xrange(n - 1, 0, -1):
    if a[i] != b[i]:
        t = i
        break
if a[:f] + a[f:t + 1][::-1] + a[t + 1:] == b:
    sys.stdout.write('yes\n%s %s' % (f + 1, t + 1))
else:
    sys.stdout.write('no')
