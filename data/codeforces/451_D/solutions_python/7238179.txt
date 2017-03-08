def id(ch):
	return ord(ch)-ord('a')
s = raw_input()
N = len(s)
c = [[0 for i in xrange(2)] for i in xrange(2)]
ans = [0, 0]
for i in xrange(N):
	c[id(s[i])][i%2] += 1
	for j in xrange(2):
		ans[j] += c[id(s[i])][j == (i%2)]
print ' '.join(map(str, ans))
