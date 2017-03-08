def getVote(n):
	if(n=="+"):
		return 1
	return -1

t = input()
while t:
	t -= 1
	votes = input()
	voteList,s = {},0
	while votes:
		votes-=1
		user, vote = raw_input().split()
		voteList[user] = getVote(vote)	
	for a in voteList:
		s += voteList[a]
	print s