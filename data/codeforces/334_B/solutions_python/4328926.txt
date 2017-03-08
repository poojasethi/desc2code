x = set()
y = set()
xy = set()
g = set()
for i in range(8):
    a,b = map(int,raw_input().split())
    x.add(a),y.add(b),xy.add((a,b))
x = sorted(list(x))
y = sorted(list(y))
if len(x)==3 and len(y)==3:
    for i in range(3):
        for j in range(3):
            if (i,j)!=(1,1):
                g.add((x[i],y[j]))
    if(xy==g):
        print "respectable"
    else:
        print "ugly"
else:
    print "ugly"
