def compare(a,b):
	la = len(a)
	for i in xrange(la):
		if(ord(a[i])>ord(b[i])):
			return 1
		elif(ord(a[i])<ord(b[i])):
			return -1
	return 0
	
def increment(a):
	l = len(a)
	sol = list(a)
	for i in xrange(l):
		if(a[l-i-1]!='9'):
			sol[l-i-1] = chr(ord(a[l-1-i])+1)
			carry = 0
			break
		else:
			carry = 1
			sol[l-i-1] = '0'
	if(carry):
		sol = ['1'] + sol
	return ''.join(sol)

for _ in xrange(input()):
	q = raw_input()
	q = increment(q)
	l = len(q)
	if(l%2):
		central_elem = q[l/2]
		first_part = q[0:l/2]
		second_part = q[l/2+1:]
		if(central_elem=='9'):
			if compare(first_part[::-1], second_part) != -1:
				sol = first_part + central_elem + first_part[::-1]
			else:
				central_elem = '0'
				first_part = increment(first_part)
				sol = first_part + central_elem + first_part[::-1]
		else:
			if compare(first_part[::-1], second_part) != -1:
				sol = first_part + central_elem + first_part[::-1]
			else:
				central_elem = increment(central_elem)
				sol = first_part + central_elem + first_part[::-1]
	else:
		first_part = q[0:l/2]
		second_part = q[l/2:]
		if compare(first_part[::-1], second_part) != -1:
			sol = first_part + first_part[::-1]
		else:
			first_part = increment(first_part)
			sol = first_part + first_part[::-1]
	print sol