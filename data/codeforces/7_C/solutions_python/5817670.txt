def extgcd(a, b):
	if b == 0:
		return 1, 0, a
	x, y, g = extgcd(b, a % b)
	return y, x - y * (a // b), g

a, b, c = map(int, raw_input().split())
x, y, g = extgcd(a, b)
if c % g != 0:
	print -1
else:
	t = c // g
	print -x * t, -y * t
