# https://www.codechef.com/problems/PRPALIN

def checkPrime(num):
	i = 2
	if num%2==0:
		# print "failed 2",num
		return False
	i = 3
	while i<(num/2):
		if num%i==0:
			# print "failed ",i,num
			return False
		i += 2

	return True

def palin(num):
	num = str(num)
	if num == num[::-1]:
		return True
	return False

n = int(raw_input())
Flag = True
while Flag :
	if palin(n):
		if checkPrime(n):
			print n
			break;
	n+=1
