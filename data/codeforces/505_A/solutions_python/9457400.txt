def checkpal(inp):
	return inp == inp[::-1]

f=0
inp = raw_input()
for i in range(len(inp)+1):
	for j in range(26):
		c = chr(ord('a')+j)
		check = inp[:i]+c+inp[i:]
		if(checkpal(check)==1):
			print check
			f=1
			break
	if(f==1):
		break
if(f==0):
	print "NA"
