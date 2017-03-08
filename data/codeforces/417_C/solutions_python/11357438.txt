# Author:   Gilberto A. dos Santos
# Website:  http://codeforces.com/contest/417/problem/C

n, k = map(int, raw_input().split(" "))

if 2*k >= n:
    print -1
    exit(0)

matches = []
for i in range(n):
    qt = 0
    j = (i + 1) % n
    while qt < k:
        matches.append([i+1, j+1])
        j = (j + 1) % n
        qt += 1

print len(matches)
for i, j in matches: print i, j
