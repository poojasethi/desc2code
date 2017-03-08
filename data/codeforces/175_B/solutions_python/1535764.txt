n=raw_input()
n=int(n)
score={}
result={}
for i in range(0,n):
	s=raw_input()
	s=s.split(' ')
	if s[0] not in score:
		score[s[0]]=int(s[1])
	elif int(s[1])>score[s[0]]:
		score[s[0]]=int(s[1])
#print score
for key in score.keys():
	minNum=0
	maxNum=0
	value=score[key]
	for val in score.values():
		if val<=value:
			maxNum=maxNum+1
		else:
			minNum=minNum+1
	if (float)(minNum)/len(score)>0.5:
		result[key]='noob'
	elif (float)(maxNum)/len(score)>=0.5 and (float)(minNum)/(float)(len(score))>0.2:
		result[key]='random'
	elif (float)(maxNum)/len(score)>=0.8 and (float)(minNum)/(float)(len(score))>0.1:
		result[key]='average'
	elif (float)(maxNum)/len(score)>=0.9 and (float)(minNum)/(float)(len(score))>0.01:
		result[key]='hardcore'
	elif (float)(maxNum)/len(score)>=0.9:
		result[key]='pro'
	
print len(score)

for k,v in result.iteritems():
	print k+' '+v

