n = input();
a = map(int, raw_input().split());
if n == 1 or n == 2 or (n == 3 and a[0] == a[2]):
	print -1;
else:
	x = y = f = 0;
	for i in xrange(1, n-1):
		if a[i] > a[i-1] and a[i] > a[i+1]:
			f = 1;
			x = i-1 if a[i-1]<a[i+1] else i+1;
			y = i;
			break;
		elif a[i] < a[i-1] and a[i] < a[i+1]:
			f = 1;
			x = i-1 if a[i-1]>a[i+1] else i+1;
			y = i;
			break;
	if not f:
		if a == [a[0]]*n:
			print -1;
		elif a[n-1] != a[n-2]:
			print n-1, n;
		elif a[0] != a[1]:
			print 1, 2;
		else:
			print 1, n;
	else:
		if a[y+1] == a[y-1]:
			if y == 1:
				print 2, 3;
			else:
				print y, y+1;
		else:
			print x+1, y+1;

