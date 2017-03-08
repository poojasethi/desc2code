t = input()
s = raw_input()
s1 = sum(int(x) for x in s[:t/2])
s2 = sum(int(x) for x in s[t/2:])

if(s.translate(None,'47') == ''):
	if(s1 == s2):
		print "YES"
	else:
		print "NO"
else:
	print "NO"