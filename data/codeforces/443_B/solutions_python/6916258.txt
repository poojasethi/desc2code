s = raw_input()
k = int(input());
l = len(s);
if k >= l:
	if (k + l) % 2:
		print k + l -1;
	else:
		print k + l;
else:
	cnt = 2 * k;
	for i in xrange(k+1, (l+k)/2+1):
	  	for j in xrange(0, l+k-i-i+1):
		  if j+i+i-1 > l:
		  	 if s[j:l-i] == s[j+i:l]:
		  		cnt = 2 * i;
		  else:
		  	 if s[j:j+i] == s[j+i:j+i+i]:
			 	cnt = 2 * i;
	print cnt
	  	
