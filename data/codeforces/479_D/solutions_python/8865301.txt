n,l,x,y = 0,0,0,0
st,sx,sy = set(),set(),set()

flagx, flagy, one = False, False, False

entrada = [int(h) for h in raw_input().split()]
n = entrada[0]
l = entrada[1]
x = entrada[2]
y = entrada[3]
a = [0 for i in range(100100)]
entrada2 = [int(j) for j in raw_input().split()]

for i in range(n):
	a[i]=entrada2[i]
	st.add(a[i])
	if a[i]==x:
		flagx=True
	elif a[i]==y:
		flagy=True
	if a[i]>x and flagx==False:
		if (a[i]-x) in st:
			flagx = True
	if a[i]>y and flagy==False:
		if (a[i]-y) in st:
			flagy=True

if not flagx and flagy:
	print "1\n%d" % (x)
elif flagx and not flagy:
	print "1\n%d" % (y)
elif flagx and flagy:
	print 0
elif not flagx and not flagy:
	one = False
	com = -1
	
	for i in range(n):
		left = a[i]-x
		right = a[i]+x
		if left>=0:
			sx.add(left)
		if right<=l:
			sx.add(right)

	for i in range(n):
		if one:
			break
		left = a[i]-y
		right = a[i]+y
		if left>=0:
			if left in sx:
				one = True
				com = left
		if right<=l:
			if right in sx:
				one = True
				com = right
   
	if one:
		print "1\n%d" % (com)
	else:
		print "2\n%d %d" % (x,y)
