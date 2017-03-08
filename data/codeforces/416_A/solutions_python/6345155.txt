n = int(input())
flag = 1
beg = -2 * (10**9)
end = 2 * (10**9)

for _ in xrange(n): 
	a = raw_input().split()
	#print a;
	if flag == 0:
		continue
	a[1] = int(a[1])
	if a[0] == '>=':
		if a[2] == 'Y':
			if a[1] > beg:
				beg = a[1]
		else:
			if a[1] <= end:
				end = a[1] - 1;
	elif a[0] == '>':
		if a[2] == 'Y':
			if a[1] >= beg:
				beg = a[1] + 1
		else:
			if a[1] < end:
				end = a[1]
	elif a[0] == '<=':
		if a[2] == 'Y':
			if a[1] < end:
				end = a[1]
		else:
			if a[1] >= beg:
				beg = a[1] + 1
	else:
		if a[2] == 'Y':
			if a[1] <= end:
				end = a[1] - 1;
		else:
			if a[1] > beg:
				beg = a[1]
	if beg > end:
		flag = 0;
print beg if flag else "Impossible"