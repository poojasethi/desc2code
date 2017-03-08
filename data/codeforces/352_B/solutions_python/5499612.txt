n = int(raw_input())
ar = [(int(x), i) for i, x in enumerate(raw_input().split())]
ar.sort()
idx = 0
#print ar
ans = []
while idx < len(ar):
    num = ar[idx][0]
    pos = ar[idx][1]
    diff = 0
    idx += 1
    if idx < len(ar) and num == ar[idx][0]:
        diff = ar[idx][1] - pos
    else:
        ans += [(num, diff)]
        continue

    idx += 1
    while idx < len(ar) and num == ar[idx][0]:
        if (ar[idx][1] - ar[idx-1][1]) != diff:
            diff = -1
        idx+=1

    if diff >= 0:
        ans += [(num, diff)]

print len(ans)
for n, p in ans:
    print n, p