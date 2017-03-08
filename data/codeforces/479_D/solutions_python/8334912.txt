par = map(int, raw_input().split(" "))
n, l, x, y = par[0], par[1], par[2], par[3]
a = map(int, raw_input().split(" "))

markx = set()
marky = set()


for item in a:
    if item -x >= 0:
        markx.add(item - x)
    if x + item <= l:
        markx.add(x + item)
    if item - y >= 0:
        marky.add(item - y)
    if y + item <= l:
        marky.add(y + item)

#print markx
#print marky

for item in a:
    if item in markx:
        markx = None
        break
for item in a:
    if item in marky:
        marky = None
        break

if markx == None and marky == None:
    print 0
elif markx == None:
    print 1
    print marky.pop()
elif marky == None:
    print 1
    print markx.pop()
else:
    intersect = (markx & marky)
    if len(intersect) == 0:
        print 2
        print markx.pop(), marky.pop()
    else:
        print 1
        print intersect.pop()
