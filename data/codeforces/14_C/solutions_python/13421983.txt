T = 4
data2 = []
xs = []
ys = []
for i in xrange(0,T):
    j = map(int,raw_input().split())
    if j[0]!=j[2] and j[1]!=j[3]:
        print "NO"
        exit()
    if j[0] == j[1] == j[2] == j[3]:
        print "NO"
        exit()
    xs += [j[0], j[2]]
    ys += [j[1], j[3]]
    data2.append(set(((j[0],j[1]),(j[2], j[3]))))
for i in data2:
    if data2.count(i) != 1:
        print "NO"
        exit()
if len(set(xs)) != 2 or len(set(ys)) != 2:
    print "NO"
    exit()
print "YES"