# coding =utf-8
I = lambda:map(int,raw_input().split())
a,b,c = I()
ans =[]
for i in range(82):
	t = str(b*i**a+c)
	if int(t)<=0 or int(t)>1000000000:
		continue
	sum =0
	for j in t:
		sum += int(j)
	if sum==i:
		ans.append(int(t))
sorted(ans)
print len(ans)
for i in ans:
	print i,