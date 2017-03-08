T = int(raw_input())
for i in range(T):
	n = int(raw_input())
	h = 1
	while n>=h:
		n = n - h
		h = h + 1
	print h-1