I = lambda f: map(f, raw_input().split())
nKnights, nFights = I(int)
anext = [i + 1 for i in xrange(nKnights + 1)]
result = [-1] * nKnights
for _ in xrange(nFights):
	l, r, x = I(lambda s: int(s) - 1)
	i = l
	while i <= r:
		if result[i] == -1 and i != x:
			result[i] = x
		temp = anext[i]
		if i < x:
			anext[i] = x
		else:
			anext[i] = r + 1
		i = temp
print ' '.join([str(x + 1) for x in result])