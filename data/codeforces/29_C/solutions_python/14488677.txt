from math import *
from Queue import *


n = int(raw_input())
nbr = dict()
cand = set()
for i in range(n):
    l = raw_input().split()
    if l[0] not in nbr:
        nbr[l[0]] = [l[1]]
        cand.add(l[0])
    else:
        nbr[l[0]].append(l[1])
        cand.remove(l[0])
    if l[1] not in nbr:
        nbr[l[1]] = [l[0]]
        cand.add(l[1])
    else:
        nbr[l[1]].append(l[0])
        cand.remove(l[1])
for v in cand:
    break
marked = set()
marked.add(v)
res = [v]
Q = [v]
while len(Q) > 0:
    v = Q.pop()
    for i in nbr[v]:
        if i not in marked:
            marked.add(i)
            res.append(i)
            Q.append(i)
print(" ".join(res))
    
