from collections import defaultdict

n = input()
if n > 26:
	print -1
else:
	a = raw_input()
	d = defaultdict(int)
	ans = 0
	for s in a:
		if d[s]:
			ans +=1
		else:
			d[s] = 1
	print ans