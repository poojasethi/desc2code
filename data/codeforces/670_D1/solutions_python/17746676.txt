a = []
b = []

def Check(m,n,k):
    x = k
    for i in range(n):
        if m * a[i] <= b[i]:
            continue
        x -= (m * a[i] - b[i])
    return x >= 0



n,k = raw_input().split()
n=int(n)
k=int(k)
a=raw_input().split()
b=raw_input().split()
for i in range(n):
    a[i]=int(a[i])
    b[i]=int(b[i])


ini = 0;
fin = 10000000
while (ini + 1 < fin):
    mid = (ini + fin) / 2
    if (Check(mid,n,k)):
        ini = mid
    else:
        fin = mid - 1


if (Check(fin,n,k)):
    print(fin)
else:
    print(ini)
