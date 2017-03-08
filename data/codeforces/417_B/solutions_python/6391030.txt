# Author:   Gilberto A. dos Santos
# Website:  http://codeforces.com/contest/417/problem/B

import sys

MAX = 100001

r = raw_input().split(" ")
n = int(r[0])
arr = [[0,0] for i in range(n)]
min_index = [0 for i in range(MAX)]

for i in range(n):
    r = raw_input().split(" ")
    arr[i] = [int(r[0]),int(r[1])]

def solve():
    for i in range(n):
        x = arr[i][0]
        index = arr[i][1]
        if x > min_index[index]:
            return False
        if min_index[index] < x+1:
            min_index[index] = x+1
    return True

ans = solve()
print "YES" if ans else "NO"
