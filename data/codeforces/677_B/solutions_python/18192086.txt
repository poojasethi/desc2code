I = lambda : map(int, raw_input().split())

n, h, k = I()

a = I()

rem = 0
i = 0
time = 0
while i < n:
	# print "i:",i,"rem",rem,"time:",time
	if rem+a[i] > h:
		time += 1
		rem = 0
	else:
		while i < n and rem+a[i] <= h:
			rem += a[i]
			i += 1
		time += rem/k
		rem %= k
	# print "i:",i,"rem",rem,"time:",time

if rem:
	time += 1
print time