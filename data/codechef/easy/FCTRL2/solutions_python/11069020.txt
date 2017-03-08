test = int(input())
def fact(u):
	if u == 0:
		return 1
	return u * fact(u-1)	
while test:
	num = int(input())
	print(fact(num))
	test = test - 1