n=int(raw_input())
c=map(int,raw_input().split())
k=2*sum(c)/n
d=[]
for i in xrange(n):
	for j in xrange(n):
		if c[i]+c[j]==k and i!=j and i not in d and j not in d:
			d.append(i)
			d.append(j)
			print i+1, j+1
			break


