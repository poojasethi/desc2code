n = int(raw_input())
s = map(int, raw_input().split())
c = 0
d = 0
q = 'YES'
for si in s:
	if si == 25: c += 1
	elif si == 50:
		d += 1
		c -= 1
	else:
		if d > 0: d -= 1
		else: c -= 2
		c -= 1
	if c < 0 or d < 0: q = 'NO'
print q