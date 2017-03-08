s=raw_input()
p=[]
def hul(x,y):
	if x[0]>y[0]:
		return 1
	if x[0]==y[0]:
		return 0
	return -1
for i in range(len(s)):
	p.append([s[i],i])
cmin = -1
p.sort(cmp=hul, reverse=True)
# print p
ans=""
for i in p:
	if i[1]>cmin:
		cmin=i[1]
		ans+=i[0]
print ans