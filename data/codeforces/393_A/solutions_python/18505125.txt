word = str(raw_input())
wordDict = {}
# initalization
for letter in "nineteen":
	wordDict[letter] = 0;
# get input
for letter in word:
	if (letter in "nineteen"):
		wordDict[letter] += 1

letterCount = []
letterCount.append(wordDict['i']/1) 
letterCount.append(wordDict['t']/1) 
letterCount.append(wordDict['e']/3) 

mini =  min(letterCount)

# scope of sharing
if mini >=2 and wordDict['n'] > 0:
	print mini if (wordDict['n'] >= 2*mini + 1) else (wordDict['n'] - 1)/2
# no scope of sharing
else:
	print min(wordDict['n']/3, mini)



