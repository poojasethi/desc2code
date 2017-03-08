s = list(raw_input());
L = len(s);
even, odd = 0, 0;
ev, od = [0]*2, [0]*2;
for i in xrange(1, L+1):
  	t = 0 if s[i-1]=='a' else 1;
  	if i % 2 :
		od[t] += 1
		even += ev[t];
		odd += od[t]
	else :
	  	ev[t] += 1
		even += od[t]
		odd += ev[t]
print even, odd
