t = input()
arr = sum(list(map(int,raw_input().split())))
if(arr==(t*(t+1))/2):
	print "YES"
else:
	print "NO"