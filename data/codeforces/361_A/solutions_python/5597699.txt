N, K = map(int, raw_input().split())
for i in xrange(N):
	print ' '.join(map(str, [0]*i+[K]+[0]*(N-i-1)))
