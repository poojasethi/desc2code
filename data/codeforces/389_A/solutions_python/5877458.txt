N = input()
a = map(int, raw_input().split())
flag = 1
while (flag):
	flag = 0
	x = min(a)
	for i in xrange(len(a)):
		if a[i] > x:
			a[i] -= x
			flag = 1
print sum(a)
