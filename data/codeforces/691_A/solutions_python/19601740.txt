n = int (raw_input())
numbers = map(int, raw_input().split())

if len(numbers) == 1 :
	if numbers[0] == 1 :
		print "YES"
	else :
		print "NO"
else :
	if numbers.count(0) == 1  :
		print "YES"
	else :
		print "NO"
