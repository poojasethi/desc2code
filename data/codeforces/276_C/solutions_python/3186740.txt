import sys
import collections
import bisect

n, q = map(int, sys.stdin.readline().split())
seq = map(int, sys.stdin.readline().split())

seq.sort(reverse=True)
temp = [0 for i in xrange(n + 2)]

seq.sort(reverse=True)
for i in xrange(q):
    start, end = map(int, sys.stdin.readline().split())
    temp[start] += 1
    temp[end + 1] -= 1


for i in xrange(1, n + 2):
    temp[i] += temp[i - 1]
#print temp
temp.sort(reverse=True)

i = 0
result = 0

while temp[i] > 0:
    result += seq[i] * temp[i]
    i += 1

print result
