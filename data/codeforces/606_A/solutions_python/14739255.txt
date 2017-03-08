h=map(int,raw_input().split())
n=map(int,raw_input().split())
ans = 0
for i in range(3):
    l = h[i]-n[i]
    if l > 0:
        l //= 2
    ans += l
print "Yes" if ans >= 0 else "No"

