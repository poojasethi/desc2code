a, b, w, x, c = map(int, raw_input().split())
n = 0; m = 0
tb = b
while True:
	tb -= x
	n += 1
	if tb < 0:
		m += 1
		tb += w
	if tb == b:
		break
# print n, m
ans = 0
k = (c-a)/(n-m)
k = max(0, k-1)
ans += n*k
a -= m*k
c -= n*k
# print a, b, w, x, c
# print ans
while a < c:
	ans += 1
	c -= 1
	b -= x
	if b < 0:
		b += w
		a -= 1
print ans
