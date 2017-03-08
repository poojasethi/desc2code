# coding =utf-8
I = lambda:map(int,raw_input().split())
a = []
b = []
x = [1,-1,0,0,0]
y = [0,0,1,-1,0]
for i in range(3):
	a.append(I())
for i in range(3):
	for j in range(3):
		sum =0
		for k in range(5):
			if i+x[k]>=0 and i+x[k]<=2 and j+y[k]>=0 and j+y[k]<=2:
				sum+=a[i+x[k]][j+y[k]]
		b.append((sum+1)%2)
print str(b[0])+str(b[1])+str(b[2])
print str(b[3])+str(b[4])+str(b[5])
print str(b[6])+str(b[7])+str(b[8])