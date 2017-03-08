n, m = map(int, raw_input().split())

city = []
imin = n-1
jmin = m-1
imax = 0
jmax = 0
for i in xrange(n):
    city.append(list(raw_input()))

    for j in xrange(m):
        if city[i][j] == "*":
            if i < imin:
                imin = i
            if j < jmin:
                jmin = j
            if i > imax:
                imax = i
            if j > jmax:
                jmax = j

if city[imin][jmin] != "*":
    print imin+1, jmin+1                
elif city[imin][jmax] != "*":
    print imin+1, jmax+1                
elif city[imax][jmin] != "*":
    print imax+1, jmin+1                
elif city[imax][jmax] != "*":
    print imax+1, jmax+1                
