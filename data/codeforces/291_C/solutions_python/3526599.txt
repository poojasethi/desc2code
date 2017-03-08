
t = raw_input().split(' ')
n = int(t[0])
k = int(t[1])
A = [0 for _ in xrange(n)]
for i in xrange(n):
    t = raw_input().split('.')
    t = [int(_) for _ in t]
    t = (t[0] << 24) | (t[1] << 16) | (t[2] << 8) | (t[3] << 0)
    A[i] = t

p = 0
for i in xrange(31, -1, -1):
    p = p | (1 << i)
    s = set()
    for i in xrange(n):
        s.add(p & A[i])

    if len(s) == k:
        print str(p >> 24) + '.' + str((p >> 16) & ((1 << 8) - 1)) + '.'  + str(p >> 8 & ((1 << 8) - 1)) + '.' + str(p & ((1 << 8) - 1))
        exit()

print '-1'

