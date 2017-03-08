n = int(raw_input())

b = []
for i in xrange(2, 2 * n + 1):
    a = map(int, raw_input().split())
    for j in xrange(1, i):
        b.append([a[j - 1], i, j])

b.sort(reverse = True)
used = [False] * (2*n)
ans = [-1] * (2*n)
for v, i, j in b:
    if not used[i - 1] and not used[j - 1]:
        ans[i - 1] = j
        ans[j - 1] = i
        used[i - 1] = used[j - 1] = True
print " ".join(map(str, ans))
