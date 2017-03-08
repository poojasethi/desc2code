n,m=map(int,raw_input().split())
grid=[]
for i in xrange(n):
	grid.append(raw_input().strip())
row=[r.count('*') for r in grid ]
col=[c.count('*') for c in zip(*grid)]
bomb=sum(row)
for i in xrange(n):
	for j in xrange(m):
		if row[i]+col[j]+(-1 if grid[i][j]=='*' else 0)==bomb:
			print "YES"
			print i+1,j+1
			exit()
print "NO"



