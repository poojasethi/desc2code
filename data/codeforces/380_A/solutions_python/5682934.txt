N = input()
s = [tuple(map(int, raw_input().split())) for i in xrange(N)]
M = input()
q = map(int, raw_input().split())
a = 0; b = 0; ans = []; y = []
for x in s:
	if x[0] == 1:
		if len(y) < 100000:
			y += [x[1]]
		if b < M and q[b] == a+1:
			ans += [x[1]]
			b += 1
		a += 1
	else:
		for i in xrange(x[1]*x[2]):
			if len(y) < 100000:
				y += [y[i%x[1]]]
			else:
				break
		while b < M and q[b] <= a+x[1]*x[2]:
			ans += [y[(q[b]-a-1)%x[1]]]
			b += 1
		a += x[1]*x[2]
print ' '.join(map(str, ans))
