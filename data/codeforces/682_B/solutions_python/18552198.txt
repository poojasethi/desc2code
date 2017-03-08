

tt = int(raw_input())
a = map(int, raw_input().split())
a.sort()
j =  0
for i in xrange(tt):
	if a[i] == j:
		continue

	j += 1	
	a[i] == j
print j + 1	