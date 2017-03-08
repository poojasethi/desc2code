__author__ = 'mowayao'

n = int(raw_input())

a = map(int,raw_input().split())

s = 0
ret = 0
id = 0
dir = 1
while s < n:
    if a[id] != -1 and s >= a[id]:
        a[id] = -1
        s += 1
    id += dir
    if s == n:
        break
    if id >= n:
        dir = -1
        id = n-1
        ret += 1
    if id < 0:
        dir = 1
        id = 0
        ret += 1
print ret