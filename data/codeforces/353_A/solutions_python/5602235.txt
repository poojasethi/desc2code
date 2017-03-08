N = input()
a = 0; b = 0; c = 0
for i in xrange(N):
	x, y = map(int, raw_input().split())
	a += x; b += y; c += (x+y)%2
print 0 if not a%2 and not b%2 else 1 if a%2 and b%2 and c else -1
