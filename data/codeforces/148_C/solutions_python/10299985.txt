n, a, b = map(int, raw_input().split())

l = [1]
if b > 0:
	for i in range(b):
		l.append(l[-1]*2)
else:
	if n >= 2:
		l.append(1)
	elif n == 1 and a == 0:
		pass
	else:
		l += [1]*n

for i in range(a):
	l.append(l[-1]+1)

if len(l) > n:
	print -1
else:
	l += [1]*(n-len(l))
	print ' '.join(map(str, l))

