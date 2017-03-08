r=raw_input
l=[]
for i in range(int(r())):
	temp = map(int,r().split())
	l.append(temp)
l.sort()
ass = l[0][1]
for i in range(1,len(l)):
	if l[i][1] < ass:
		ass = l[i][0]
	else:
		ass = l[i][1]
print ass