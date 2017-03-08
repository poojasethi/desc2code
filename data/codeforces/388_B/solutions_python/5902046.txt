K = input()
N = 901
print N
g = [['N']*N for i in xrange(N)]
def cnn(u, v):
	g[u][v] = g[v][u] = 'Y'
# cnn(0, 2)
for i in xrange(2, 30):
	cnn(i, i+1)
cnn(30, 1)
for i in xrange(29):
	x = 31+i*(i+1)
	# cnn(0, x)
	# cnn(0, x+1)
	for j in xrange(i):
		a = x+j*2
		cnn(a, a+2)
		cnn(a, a+3)
		cnn(a+1, a+2)
		cnn(a+1, a+3)
	y = x+i*2
	if i < 28:
		cnn(y, 3+i)
		cnn(y+1, 3+i)
	else:
		cnn(y, 1)
		cnn(y+1, 1)

pow2 = [2**i for i in xrange(32)]
vis = []
for i in range(len(pow2))[::-1]:
	if K >= pow2[i]:
		K -= pow2[i]
		vis.append(i)

for x in vis:
	if x is 0:
		cnn(0, 2)
	else:
		xx = 31+(x-1)*x
		cnn(0, xx)
		cnn(0, xx+1)

for x in g:
	print "".join(x)
