def value(n):
	if n in v:
		return v[n]
	else:
		v1 = value(n / 2)
		v2 = value(n / 3)
		v3 = value(n / 4)
		ans = max(n, v1 + v2 + v3)
	v[n] = ans
	return v[n]


v = {0 : 0}
while True:
	try:
		n = int(raw_input())
	except EOFError:
		break
	print value(n)
#print v
