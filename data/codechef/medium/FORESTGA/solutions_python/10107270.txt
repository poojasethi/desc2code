from sys import stdin,stdout
n,w,l = map(int,stdin.readline().split(' '))
h = []
r = []
for i in xrange(n):
	a,b = map(int,stdin.readline().strip().split(' '))
	h.append(a)
	r.append(b)
tl = 0
th = 10000000000000000000
while tl <= th:
	cut = 0
	tm = (th+tl)/2
	for i in xrange(n):
		if (h[i] + r[i]*tm) >= l:
			cut += (h[i] + r[i]*tm)
		if cut > w:
			break
	if cut < w:
		tl = tm+1
	elif cut > w:
		th = tm-1
	else:
		break
cut = 0
for i in xrange(n):
		if (h[i] + r[i]*tm) >= l:
			cut += (h[i] + r[i]*tm)
if cut < w:
	tm += 1
stdout.write(str(tm))