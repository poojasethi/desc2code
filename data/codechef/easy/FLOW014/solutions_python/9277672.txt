T = int(raw_input())

for i in range(T):
    h, c, t = raw_input().split()
    h = int(h)
    c = float(c)
    t = int(t)
    h = True if h>50 else False
    c = True if c<0.7 else False
    t = True  if t>5600 else False
    
    if h and c and t:
        print 10
    elif h and c:
        print 9
    elif c and t:
        print 8
    elif h and t:
        print 7
    elif h or c or t:
        print 6
    else:
        print 5
