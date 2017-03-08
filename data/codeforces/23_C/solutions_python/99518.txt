#!/usr/bin/python

T = input()

for k in xrange(T):
    n = input()
    boxes = list()
    for i in xrange(2*n-1):
        boxes.append(tuple(map(int, raw_input().split())) + (i+1,))
    
    boxes.sort(reverse=True)
    print "YES"
    print boxes[0][2],
    
    for i in xrange(1, len(boxes), 2):
        if boxes[i][1] < boxes[i+1][1]:
            print " ", boxes[i+1][2],
        else:
            print " ", boxes[i][2],
    print
    
