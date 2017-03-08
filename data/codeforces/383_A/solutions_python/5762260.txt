N = input()
a = map(int, raw_input().split())
tot = 0; ans = 0
for x in a:
	if x:
		tot += 1
	else:
		ans += tot
print ans
