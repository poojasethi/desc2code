#Author: Gilberto A. dos Santos
#Website: http://codeforces.com/contest/492/problem/C

n, r, avg = map(int, raw_input("").split(" "))

total = 0
exams = []
for i in range(n):
    exams.append(map(int, raw_input("").split(" ")))
    total = total + exams[i][0]

exams = sorted(exams, key = lambda p: p[1])

if total >= avg * n:
    print 0
    exit(0)

ans = 0
for i in range(n):
    e = exams[i]
    dist = r - e[0]
    if total + dist >= avg * n:
        ans = ans + e[1] * (avg * n - total)
        break
    else:
        total = total + dist
        ans = ans + dist * e[1]
print ans
