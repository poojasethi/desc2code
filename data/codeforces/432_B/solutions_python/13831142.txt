n = input()
xy = [map(int,raw_input().split()) for i in range(n)]
c = [0]*(10**5+1)
for x,y in xy:
    c[x] += 1
for x,y in xy:
    a = c[y]
    print n-1+a,n-1-a
