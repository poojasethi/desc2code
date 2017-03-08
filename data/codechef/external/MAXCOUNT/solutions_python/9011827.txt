import sys
T = raw_input()
for i in range(int(T)):
    N = raw_input()
    max = dict()
    lst = list()
    lst = map(int,sys.stdin.readline().split())
    for k in lst:
        max[k] = max.get(k,0) + 1
    count = []
    t = max.items()
    t.sort() 
    count = sorted(t,key=lambda x: x[1],reverse = True)
    for (k,v) in count[:1]:
        print k,v
