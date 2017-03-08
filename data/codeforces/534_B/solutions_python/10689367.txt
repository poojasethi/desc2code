v1, v2 = map(int, raw_input().split())
t, d = map(int, raw_input().split())

l = [[v1, v1]]
for i in xrange(0, t - 2):
    l.append([l[-1][0] + d, 0])

l.append([v2, v2])

for i in xrange(t - 2, -1, -1):
    l[i][1] = l[i + 1][1] + d

ans = 0
for option in l:
    ans += min(option)

print ans
