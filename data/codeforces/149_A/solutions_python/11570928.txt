k = input()
num = map(int,raw_input().split())
num.sort(reverse = True)
ans = 0
for x in num:
	if k > 0:
		ans += 1
		k -= x
if k > 0:
	print '-1'
else:
	print ans
