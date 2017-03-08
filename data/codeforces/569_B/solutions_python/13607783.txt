import sys

n = int(sys.stdin.readline())

arr = map(int, sys.stdin.readline().split())

ind = [0]*100000

to_move = []

for i in xrange(n):        
    if arr[i] > n or ind[arr[i]-1] == 1:
        to_move.append(i)
        continue
    ind[arr[i]-1] = 1

for j in xrange(n):
    if ind[j] == 1:
        continue
    arr[to_move.pop()] = j+1

print >> sys.stdout, " ".join(map(str, arr))