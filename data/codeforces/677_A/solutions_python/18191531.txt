

a = map(int, raw_input().split())
b = list(map(int, raw_input().split()))
ans = 0
for i in b:
	if i > a[1]:
		ans += 2

	else:
		ans += 1

print ans			