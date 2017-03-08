ans = []
for i in range(26):
	ans.append([0]*26)
for i in range(input()):
	s = raw_input()
	l = len(s)
	count = [0]*26
	for j in range(l):
		count[ord(s[j])-ord('a')] += 1
	nonzero = 0
	temp1=''
	temp2=''
	for j in range(26):
		if(count[j]>0 and nonzero==0):
			nonzero+=1
			temp1=j
		elif(count[j]>0 and nonzero==1):
			nonzero+=1
			temp2=j
		elif(count[j]>0):
			nonzero+=1
	# print nonzero
	if(nonzero==1):
		for j in range(26):
			ans[j][temp1] += l
			ans[temp1][j] += l
		ans[temp1][temp1] -= l
	elif(nonzero==2):
		ans[temp1][temp2]+= l
		ans[temp2][temp1]+= l
# print ans
ansd = 0
for j in range(26):
	for k in range(26):
		ansd = max(ansd,ans[j][k])
print ansd