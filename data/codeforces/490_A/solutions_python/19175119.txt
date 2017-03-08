n=int(raw_input())
s=raw_input().split()
dic={'1':[],'2':[],'3':[]}
[dic[n].append(i+1) for i,n in enumerate(s)]
w=min([len(dic[key]) for key in dic])
print w
if w>0:
	for i in range(w):
		print dic['1'][i], dic['2'][i],dic['3'][i]