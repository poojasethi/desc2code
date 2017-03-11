# with open('data/code.txt') as f:
# 	vocab = set()
# 	for line in f:
# 		for word in line.split():
# 			vocab.add(word)

# 	print(len(vocab))
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np

num_bins = 10

def main():
	source_lengths = []
	target_lengths = []

	#Count average length of source sentence
	with open('data/description.txt') as f:
		totalWords = 0
		totalSentences = 0
		for line in f:
			sentenceLength = len(line.split())
			source_lengths.append(sentenceLength)
			totalWords += sentenceLength
			totalSentences += 1

		print 'Average description sentence length: ', totalWords / totalSentences

	#Count average length of target sentence
	with open('data/code.txt') as f:
		totalWords = 0
		totalSentences = 0
		for line in f:
			sentenceLength = len(line.split())
			target_lengths.append(sentenceLength)
			totalWords += sentenceLength
			totalSentences += 1

		print 'Average code sentence length: ', totalWords / totalSentences

	plot_histogram = False
	if plot_histogram:
		plot_histo_lengths("target lengths", target_lengths)
		plot_histo_lengths("source_lengths", source_lengths)
	else:
		plot_scatter_lengths("target vs source length", "source length",
			"target length", source_lengths, target_lengths)

# From: https://github.com/inikdom/neural-chatbot
def plot_scatter_lengths(title, x_title, y_title, x_lengths, y_lengths):
	plt.scatter(x_lengths, y_lengths)
	plt.title(title)
	plt.xlabel(x_title)
	plt.ylabel(y_title)
	plt.ylim(0, max(y_lengths))
	plt.xlim(0,max(x_lengths))
	plt.show()

# From: https://github.com/inikdom/neural-chatbot
def plot_histo_lengths(title, lengths):
	mu = np.std(lengths)
	sigma = np.mean(lengths)
	x = np.array(lengths)
	n, bins, patches = plt.hist(x,  num_bins, facecolor='green', alpha=0.5)
	y = mlab.normpdf(bins, mu, sigma)
	plt.plot(bins, y, 'r--')
	plt.title(title)
	plt.xlabel("Length")
	plt.ylabel("Number of Sequences")
	plt.xlim(0,max(lengths))
	plt.show()


if __name__=="__main__":
	main()
