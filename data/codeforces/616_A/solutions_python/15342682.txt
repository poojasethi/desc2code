a = raw_input().lstrip('0')
b = raw_input().lstrip('0')
flag = False

if len(a) > len(b):
	print '>'
elif len(a) < len(b):
	print '<'
else:
	tmp = len(a)
	for x in xrange(tmp):
		if a[x] > b[x]:
			flag = True
			print '>'
			break
		elif a[x] < b[x]:
			flag = True
			print '<'
			break
	if flag == False:
		print '='

