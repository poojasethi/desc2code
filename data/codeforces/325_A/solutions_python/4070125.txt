n = int(raw_input())

area = 0
for i in range(0,n):
    x1,y1,x2,y2 = map(int,raw_input().split())

    if (i == 0):
        minx = x1
        miny = y1
        maxx = x2
        maxy = y2
    else:
        minx = min(minx,x1)
        miny = min(miny,y1)
        maxx = max(maxx,x2)
        maxy = max(maxy,y2)

    area += (x2-x1)*(y2-y1)
    

dx = maxx - minx
dy = maxy - miny

if (dx != dy or dx*dy != area):
    print("NO")
else:
    print("YES")


    
    
