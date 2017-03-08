n, total = map(int, raw_input().split())

dist = 0
for i in xrange(n):
	sign, val = raw_input().split()
	val = int(val)
	if sign == '+':
		total += val
	elif sign == '-':
		if total >= val:
			total -= val
		else:
			dist += 1
print total, dist