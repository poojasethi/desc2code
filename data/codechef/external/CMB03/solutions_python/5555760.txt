import sys
t=int(sys.stdin.readline())
while t!=0:
    s1,s2=raw_input().split()
    if s2 in s1:
        print 1
    else:
        print 0
    t-=1
