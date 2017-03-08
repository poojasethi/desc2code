#http://codeforces.com/contest/545/problem/A

#!/usr/bin/python

n = input()
g = []
for i in range(1,n+1):
    for c in raw_input().split():
        if c in '13': break
    else: g += [`i`]

print len(g)
for i in g:
    print i,
print

