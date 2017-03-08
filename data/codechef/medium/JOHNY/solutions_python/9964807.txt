t = int(raw_input())
for _ in xrange(t):
	n = int(raw_input())
	s = map(int,raw_input().split())
	j = int(raw_input())
	e = s[j-1]
	s.sort()
	print s.index(e)+1