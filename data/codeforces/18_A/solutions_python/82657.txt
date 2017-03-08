#!/usr/bin/python
import sys

def newpoints (x,y):
    point = []
    point.append([x + 1, y])
    point.append([x - 1, y])
    point.append([x, y + 1])
    point.append([x, y - 1])
    return point

def isright(x1, y1, x2, y2, x3, y3):
    d1 = sdistance (x1, y1, x2, y2)
    d2 = sdistance (x1, y1, x3, y3)
    d3 = sdistance (x2, y2, x3, y3)
    l = sorted([d1, d2, d3])
    if (((y2 - y1)*(x3-x1) - (x2 - x1)*(y3- y1)) == 0):
        return 0
    if (l[2] == (l[0] + l[1])):
        return 1
    else:
        return 0

def sdistance (x1, y1, x2, y2):
    return ((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2))


(x1, y1, x2, y2, x3, y3) = map(int, sys.stdin.next().strip().split())

if (isright(x1, y1, x2, y2, x3, y3)):
    print "RIGHT"
    sys.exit(0)

npoints = newpoints(x1, y1)
for i in npoints:
    if (isright(i[0], i[1], x2, y2, x3, y3)):
        print "ALMOST"
        sys.exit(0)
        
npoints = newpoints(x2, y2)
for i in npoints:
    if (isright(x1, y1, i[0], i[1], x3, y3)):
        print "ALMOST"
        sys.exit(0)

npoints = newpoints(x3, y3)
for i in npoints:
    if (isright(x1, y1, x2, y2, i[0], i[1])):
        print "ALMOST"
        sys.exit(0)

print "NEITHER"


