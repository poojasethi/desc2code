from heapq import *
n, s = map(int, raw_input().split())
a = map(int, raw_input().split())
q = [(-x, i) for (i, x) in enumerate(a) if x > 0]
heapify(q)
res = []
while q:
    (x, i) = heappop(q)
    if -x > len(q):
        print 'No'
        break
    for (y, j) in [heappop(q) for _ in xrange(-x)]:
        res.append((i + 1, j + 1))
        if y + 1: heappush(q, (y + 1, j))
else:
    print 'Yes'
    print len(res)
    for (i, j) in res: print i, j
