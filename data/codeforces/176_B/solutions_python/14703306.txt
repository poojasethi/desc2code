import sys

start = raw_input()
end = raw_input()
k = int(raw_input())

dpA = [-1 for i in xrange(k+1)]
dpB = [-1 for i in xrange(k+1)]

def calculaA(n):
    global dpA, dpB
    if n == 0:
        return 0
    if dpA[n-1] == -1:
        calculaA(n-1)

    dpA[n] = dpA[n-1]*(A-1) + dpB[n-1]*A
    dpB[n] = dpA[n-1]*B     + dpB[n-1]*(B-1)

    return dpA[n]

if start == end and k == 0:
    print 1
    exit(0)

A = B = 0

if start != end:
    dpA[0] = 0
    dpB[0] = 1
else:
    dpA[0] = 1
    dpB[0] = 0


for i in xrange(len(start)):
    now = start[i:]+start[:i]
    
    if now == end:
        A += 1
    else:
        B += 1



for n in xrange(1, k+1):
    dpA[n] = (dpA[n-1]*(A-1) + dpB[n-1]*A)%1000000007
    dpB[n] = (dpA[n-1]*B     + dpB[n-1]*(B-1))%1000000007

print dpA[k]

