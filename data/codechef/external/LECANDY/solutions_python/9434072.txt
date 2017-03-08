for i in range(int(raw_input())):
	n,c = map(int, raw_input().split(' '))
	arr = map(int, raw_input().split(' '))
	sum1 = sum(arr)
	if sum1 <= c:
		print 'Yes'
	else:
		print 'No'
