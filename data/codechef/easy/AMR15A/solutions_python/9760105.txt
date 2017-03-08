N = int(raw_input())
counte = 0
counto = 0
temp = list()
temp = map(int,raw_input().split())
for x in temp:
	
	if x%2==0:
		counte = counte + 1
	else:
		counto = counto + 1
if counte > counto:
	print "READY FOR BATTLE"
else:
	print "NOT READY"