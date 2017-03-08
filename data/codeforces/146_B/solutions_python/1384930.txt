a,b = map(int,raw_input().split())
b = str(b)
b = [i for i in b]
a += 1
p = []
while 1 == 1:
	t = str(a)
	p = [i for i in t if i == '4' or i == '7']	
	if p == b:
		break
	a += 1
print a
