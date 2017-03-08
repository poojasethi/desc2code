#http://codeforces.com/problemset/problem/659/C
n, m = map(int, raw_input().split())
t = map(int, raw_input().split())
used = set(t)
i = 1
total = 0
count = []
while True:
    if i not in used:
        total += i
        if total <= m: count.append(i)
        else:
            print len(count)
            for j in range(len(count)): print count[j],
            break
    i += 1
