#!/usr/bin/python
import sys
cost = {}
mcost = 0

n = int(sys.stdin.next().strip())
qual = map(int, sys.stdin.next().strip().split (" "))
m = int(sys.stdin.next().strip())
mi = qual.index(max(qual))

for i in xrange(n):
    cost[i] = []
cost[mi].append(0)

for i in xrange(m):
    app = map(int, sys.stdin.next().strip().split (" "))
    cost[app[1] - 1].append(app[2])

for i in xrange(n):
    if not (len(cost[i]) > 0):
        print -1
        sys.exit(0)
    mcost += min(cost[i])

print mcost

    

