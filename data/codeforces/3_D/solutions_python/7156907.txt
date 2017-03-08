from heapq import *

s = list(raw_input());
ans, heap = 0, [];
b = 0
for i, v in enumerate(s):
  	if v == '(': 
		b += 1
	elif v == ')': 
	  	b -= 1
	else :
	  	b -= 1;
		x, y = map(int, raw_input().split());
		ans += y;
		s[i] = ')'
		heappush(heap, (x-y, i));
	if b < 0:
	  	if (not heap):
		  	print -1
			quit()
		b += 2;
		x, y = heappop(heap);
		ans += x;
		s[y] = '(';
if b: 
	print '-1';
else :
	print ans
	print ''.join(s)
