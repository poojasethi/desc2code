import sys

n = int(input());
d = {};
for i in range (n):
	[s, a] = list(sys.stdin.readline().split());
	if s in d:
		d[s] = max (d[s], int(a));
	else:
		d[s] = int(a);

n = len(d);
print (n);
for i, iv in d.items():
	cnt = 0;
	for j, jv in d.items():
		if jv <= iv:
			cnt += 1;
	rt = float (cnt) / n;
	if rt >= 0.99:
		print (i + ' pro')
	elif rt >= 0.9:
		print (i + ' hardcore')
	elif rt >= 0.8:
		print (i + ' average')
	elif rt >= 0.5:
		print (i + ' random')
	elif rt < 0.5:
		print (i +  ' noob')
