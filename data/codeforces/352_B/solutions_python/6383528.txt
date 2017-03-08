# Author:   Gilberto A. dos Santos
# Website:  http://codeforces.com/problemset/problem/352/B

import sys

MAX = 100001

r = raw_input().split(" ")
n = int(r[0])
r = raw_input().split(" ")

values = [[] for i in range(MAX)]
for i in range(n):
     values[int(r[i])].append(i)

ans = []
for i in range(MAX):
    if len(values[i]) == 0: continue
    elif len(values[i]) == 1:
        ans.append([i,0])
        continue

    values[i].sort()
    x = values[i][1] - values[i][0]
    ok = True
    for j in range(1,len(values[i])):
        if values[i][j]-values[i][j-1] != x:
            ok = False
            break
    if ok:
        ans.append([i,x])

print len(ans)
for i in ans:
    print i[0], i[1]
