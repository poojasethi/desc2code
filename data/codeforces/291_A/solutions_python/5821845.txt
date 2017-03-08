n = int(raw_input())
a = map(int, raw_input().split())
z = dict()
for q in a:
	if q not in z:
		z[q] = 0
	z[q] += 1
ans = 0
for (v, q) in z.items():
	if v != 0:
		if q > 2:
			ans = -1
			break
		if q == 2:
			ans += 1
print ans