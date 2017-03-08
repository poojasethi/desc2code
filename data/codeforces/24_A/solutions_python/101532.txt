#!/usr/bin/env python

n = int(raw_input())

l = []
cnt = [0]*n
for i in range(n):
    a, b, c = map(int, raw_input().split())
    a, b = a-1, b-1
    l.append([a, b, c])

other = l[0][1]
for i in range(1, n):
    for j in range(i, n):
        if l[j][0] == other or l[j][1] == other:
            if l[j][0] == other: other = l[j][1]
            else: other = l[j][0]
            l[i], l[j] = l[j], l[i]
#            print other
            break

#print l
dir = True
v = 0;
sug1 = l[0][2]
sug2 = 0
for i in range(1, n):
    if l[i][0] == l[i-1][1] or l[i][1] == l[i-1][0]: pass
    else: dir = not dir
    if dir: sug1 += l[i][2]
    else: sug2 += l[i][2]

print min(sug1, sug2)
