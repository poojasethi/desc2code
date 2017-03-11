# with open('data/code.txt') as f:
# 	vocab = set()
# 	for line in f:
# 		for word in line.split():
# 			vocab.add(word)

# 	print(len(vocab))

#Count average length of sentence
with open('data/code.txt') as f:
	totalWords = 0
	totalSentences = 0
	for line in f:
		totalWords += len(line.split())
		totalSentences += 1

	print(totalWords / totalSentences)