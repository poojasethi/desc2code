s=raw_input()
n=int(raw_input())
for i in range(n):
    l,r,k = [int(x) for x in raw_input().split()]
    k %= (r-l+1)
    if k>0:
        s1 = s[l-1:r]
        s = s[:l-1] + s1[-k:] + s1[:-k] + s[r:]
print s
