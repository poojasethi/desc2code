# Author:   Gilberto A. dos Santos
# Website:  http://codeforces.com/contest/417/problem/0

c, d = map(int, raw_input().split(" "))
n, m = map(int, raw_input().split(" "))
k = int(raw_input())

needed = (n * m) - k

numberOfProblems = 0
while needed > 0:
    if needed >= n:
        costAdd = d * n
        numberOfProblems += costAdd if costAdd < c else c
        needed -= n
    else:
        costAdd = d * needed
        numberOfProblems += costAdd if costAdd < c else c
        needed -= n

print numberOfProblems
