import sys

inputs = sys.stdin.readline().split()
n = int(inputs[0])
m = int(inputs[1])
d = dict()

for i in xrange(m):
    l = sys.stdin.readline().split()
    l = [int(k) for k in l] 
    colors = [1,2,3]
    for j in xrange(3):
        ele = l[j]
        if ele in d:
            colors.remove(d[ele])
    for j in xrange(3):
        ele = l[j]
        if ele not in d:
            d[ele] = colors.pop(0)

for i in xrange(1, n+1):
    print d[i],
print




