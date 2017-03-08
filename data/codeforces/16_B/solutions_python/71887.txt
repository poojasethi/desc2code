#!/usr/bin/python
import sys

(n,m) = map(int, sys.stdin.next().strip().split (" "))
prof = 0
box = [0]*m

for ii in xrange(m):
    box[ii] = map(int, sys.stdin.next().strip().split (" "))

box.sort(key=lambda x: x[1])
box.reverse()

for ii in xrange(m):

    if not (n > 0):
        break

    if (n >= box[ii][0]):
        n -= box[ii][0]
        prof = prof + box[ii][0]*box[ii][1]
    else:
        prof = prof + n*box[ii][1]
        n = 0
        

print prof    
