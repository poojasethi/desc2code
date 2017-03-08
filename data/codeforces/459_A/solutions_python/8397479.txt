[x1,y1,x2,y2] = map(int, raw_input().split(" "))
x, y = abs(x1-x2), abs(y1-y2)

if x == 0:
    print x1+y, y1, x2+y, y2
elif y == 0:
    print x1, y1+x, x2, y2+x
elif x == y:
    print x1, y2, x2, y1
else:
    print -1