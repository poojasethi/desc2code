n = input()
a = map(int, raw_input().split())
b = sorted(a)
# count = 0
while (a != b):
	for i in xrange(n-1):
		if(a[i] > a[i+1]):
			print i+1, i+2
			# count += 1
			a[i], a[i+1] = a[i+1], a[i]

# print count

