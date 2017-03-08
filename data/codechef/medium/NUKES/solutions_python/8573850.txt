a,n,k = map(int,raw_input().split())
index = 0
ans  = []
for i in xrange(k):
	index = i
	if a < 1 :
		break
	ans.append(a%(n+1))
	a = a/(n+1)

n = len(ans)
while n < k :
	ans.append(0)
	n+=1

a = ""
for i in ans :
	a+=str(i)+" "
print a