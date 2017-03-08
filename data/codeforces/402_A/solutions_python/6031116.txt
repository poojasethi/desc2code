k, a, b, v = map(int, raw_input().split())
cnt = 0
while a > 0:
	section = 1
	if b >= k-1:
		section = k
		b -= (k - 1)
	else:
		section = b + 1
		b = 0
	a -= (v * section)
	cnt += 1
print cnt