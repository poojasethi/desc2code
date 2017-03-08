T = int(raw_input())

for i in range(T):
    R = int(raw_input())
    p1 = map(int, raw_input().split()) 
    p2 = map(int, raw_input().split()) 
    p3 = map(int, raw_input().split())
    count = 0
    if ((p1[0]-p2[0])**2 + (p1[1] - p2[1])**2) > R**2:
        count += 1
    if ((p2[0]-p3[0])**2 + (p2[1] - p3[1])**2) > R**2:
        count += 1
    if ((p1[0]-p3[0])**2 + (p1[1] - p3[1])**2) > R**2:
        count += 1
    print "yes" if count <= 1 else "no"
