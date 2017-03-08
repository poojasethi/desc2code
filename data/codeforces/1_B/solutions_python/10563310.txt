import re

for i in range(input()):
	s = raw_input()
	p = re.match(r'R(\d+)C(\d+)',s)
	if p:
		r = p.group(1)
		c = int(p.group(2))
		while c!=0:
			r = chr(ord('A')+ (c-1)%26)+r
			c = (c-1)/26
	else:
		p = re.match(r'(\D+)(\d+)',s)
		r = 'R'+p.group(2)+'C'
		c = 0
		for x in p.group(1):
			c = c*26 + ord(x)-ord('A')+1
		r = r + str(c)
	print r 