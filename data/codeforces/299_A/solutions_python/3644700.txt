n = input()
a = [int(x) for x in raw_input().split(' ')]
a.sort()

result = a[0]
for x in a[1:]:
	if result % x == 0:
		result = x
	elif x % result != 0:
		result = -1
		break
	if result == 1:
		break

print result