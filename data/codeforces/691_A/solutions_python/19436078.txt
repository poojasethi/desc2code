n=int(raw_input())
a=map(int,raw_input().split())
if n>1 and a.count(0)==1:
	print "YES"
	exit()
elif n==1 and a[0]==1:
	print "YES"
	exit() 	
print "NO"		

