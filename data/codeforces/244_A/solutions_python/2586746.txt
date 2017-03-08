#!/usr/bin/python
n, k = map(int, raw_input().split())
a = map(int, raw_input().split())
ans = range(1, n*k+1)
foo = []
for i in range(len(a)):
    ans.remove(a[i])

A = [[x] for x in a]

for j in range(k):
    for h in range(n-1):
        A[j].append(ans.pop())
    print ' '.join(map(str,A[j]))