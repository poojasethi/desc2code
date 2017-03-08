# raw_input, split

n,k  = map(int, raw_input().split())
a = map(int ,raw_input().split())
a.sort(reverse=True)

i = 0
ans = 0
while i < n:
    ans += (a[i]-1)*2
    i += k

print ans
