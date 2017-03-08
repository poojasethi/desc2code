n = int(raw_input())
s = raw_input()

f = 0
ans = 0
for i in s:
	if i == '1' and f == 0:
		if(ans > 0):
			ans += 1
		ans += 1
		f = 1
	elif i == '1' and f == 1:
		ans += 1
	elif i == '0':
		f = 0

print ans