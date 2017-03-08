N, M = map(int, raw_input().split())
t = [map(int, raw_input().split()) for i in xrange(N)]
d = []
add = 0
for i in xrange(N):
	add += t[i][0]
	d.append([add])
for j in xrange(1, M):
	for i in xrange(N):
		if i:
			d[i].append(max(d[i-1][j], d[i][j-1])+t[i][j])
		else:
			d[i].append(d[i][j-1]+t[i][j])
print ' '.join(map(str, [d[i][M-1] for i in xrange(N)]))
