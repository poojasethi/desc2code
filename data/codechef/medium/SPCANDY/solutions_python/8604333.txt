tc = input()
while(tc):
	tc -= 1
	candles, student = map(int,raw_input().split())
	if(candles==0):
		print 0,0
	else:
		if(student==0):
			print 0,candles
		else:
			print candles/student,candles%student