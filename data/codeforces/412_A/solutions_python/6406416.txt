# Author:   Gilberto A. dos Santos
# Website:  http://codeforces.com/contest/412/problem/0

import sys

r = raw_input().split(" ")
k = int(r[0])
n = int(r[1])

slogan = raw_input()

left = 1
right = len(slogan)

def left_right():
    for i in range(right-1):
        print "PRINT " + slogan[i]
        print "RIGHT"
    else:
        print "PRINT " + slogan[right-1]

def right_left():
    for i in range(right-1,0,-1):
        print "PRINT " + slogan[i]
        print "LEFT "
    else:
        print "PRINT " + slogan[0]

if n == left:
    left_right()
elif n == right:
    right_left()
else:
    dist_left = abs(n - left)
    dist_right = abs(n - right)
    if dist_left < dist_right:
        for i in range(dist_left):
            print "LEFT"
        left_right()
    else:
        for i in range(dist_right):
            print "RIGHT"
        right_left()
