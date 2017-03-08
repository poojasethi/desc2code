import math
a = raw_input()
n = len(a)
k = int(raw_input())
mod = 1000000007
p2 = 1
s = 0
for i in range(n):
    if a[i] == '0' or a[i] == '5':
        s+=p2
    p2=(p2*2)%mod;
inv = pow(pow(2,n,mod)-1,mod-2,mod)
ans = s*(pow(2,n*k,mod)-1)*inv%mod
print ans
