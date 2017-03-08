
n, m, k = map(int, raw_input().split())

a = [0] + map(int, raw_input().split())

op = []

for i in xrange(m):
    op.append(map(int, raw_input().split()))

tsk = [0 for i in xrange(m+1)]

for i in xrange(k):

    rng = map(int, raw_input().split())
            
    if rng[1] < m:
        tsk[rng[1]] -= 1
    else:
        tsk[-1] += 1
        

    tsk[rng[0]-1] += 1


vec = [tsk[-1]]
for i in xrange(1, m):
    vec.append((-vec[i-1] + tsk[m-i])*-1)
    


vec.reverse()

diff = []
for i in xrange(1, n+1):
    diff.append(a[i]-a[i-1])
diff.append(a[n])


for i in xrange(m):
    
    soma = op[i][2] * vec[i]
            
    if op[i][1] < n:
        diff[op[i][1]] -= soma
    else:
        diff[-1] += soma        

    diff[op[i][0]-1] += soma



res = [diff[-1]]
for i in xrange(1, n):
    res.append((-res[i-1] + diff[n-i])*-1)

res.reverse()
print ' '.join(map(str, res))
