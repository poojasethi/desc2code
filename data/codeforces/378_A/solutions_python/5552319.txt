a,b = [int(x) for x in raw_input().split()]

aw = 0
bw = 0
d = 0
for x in range(1,7):
	if abs(a-x) < abs(b-x):
		aw+=1
	elif abs(a-x) > abs(b-x):
		bw+=1
	else:
		d+=1
print(aw),
print(d),			
print(bw)
