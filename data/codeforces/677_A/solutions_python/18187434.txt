I = lambda : map(int, raw_input().split())

n, k = I()
ans = 0
a = I()
for s in a:
	if s > k:
		ans += 2
	else:
		ans += 1
print ans