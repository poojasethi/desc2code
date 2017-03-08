n, m = map(int,raw_input().split())
s = [0 for i in range(n)]
res = []
for i in range(n):
    res += map(int,list(str(input())))
for i in range(m):
    cr = res[i::m];cm = max(cr)
    for i in range(n):
        if cr[i]==cm:
            s[i]=1          
print(sum(s))
