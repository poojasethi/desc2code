n=int(raw_input())
buttons=raw_input()
if len(buttons)==1:
	if buttons=="1":
		print "YES"
	else:
		print "NO"
else:
	if buttons.count("0")==1:
		print "YES"
	else:
		print "NO"