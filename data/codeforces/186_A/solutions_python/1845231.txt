__author__ = 'Aphrodite'

a = raw_input()
b = raw_input()

if len(a) != len(b):
    print 'NO'
    exit()

diff = 0
p = []
q = []
for i in range(len(a)):
    if a[i] != b[i]:
        diff += 1
        p.append(a[i])
        q.append(b[i])

if diff == 0 or (diff == 2 and p[0] == q[1] and p[1] == q[0]):
    print 'YES'
else:
    print 'NO'
