def fact(number):
	product=1
	while number>=2:
		product=product*number
		number=number-1
	print product
def testcases(n):
	while n>=1:
		num=input()
	 	fact(num)
		n=n-1
NumberOfTestCases=input()
testcases(NumberOfTestCases)
