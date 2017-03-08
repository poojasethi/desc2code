n = int(raw_input())
a = map(int,raw_input().split())
sa = sorted(a)
ans = []
for i in range(n):
    if a[i] != sa[i]:
        p = a[i:].index(sa[i])+i
        a[i],a[p] = a[p],a[i]
        ans.append([i,p])
print len(ans)
for line in ans:
    print " ".join(map(str,line))
