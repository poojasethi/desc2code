import os
import sys
import glob
import itertools

# Get a pair of question, predicted output, and real output
def edit_distance(s1, s2):
	m=len(s1)+1
	n=len(s2)+1

	tbl = {}
	for i in range(m): tbl[i,0]=i
	for j in range(n): tbl[0,j]=j
	for i in range(1, m):
		for j in range(1, n):
			cost = 0 if s1[i-1] == s2[j-1] else 1
			tbl[i,j] = min(tbl[i, j-1]+1, tbl[i-1, j]+1, tbl[i-1, j-1]+cost)

	return tbl[i,j]

def getDescriptionsAndRealOutput(directory):
	result = []
	with open(directory + "/description.test.txt") as descriptionsFile:
		with open(directory + "/code.test.txt") as realOutputFile:
			descriptionsArray = descriptionsFile.readlines()
			realOutputArray = realOutputFile.readlines()

			for i in range(0, len(descriptionsArray)):
				result.append( ( descriptionsArray[i][:len(descriptionsArray[i])-2], realOutputArray[i][:len(realOutputArray[i])-2] ) )
	return result

def getPredictedOutput(directory, file):
	result = []
	with open(directory + "/" + file) as predictedOutputFile:
		predictedOutputArray = predictedOutputFile.readlines()

		i = 0
		while i < len(predictedOutputArray):
			result.append( predictedOutputArray[i+1] )
			i+= 2
	return result

def getOutputFiles(directory):
	# Get the output files in the directory
	directory = sys.argv[1]
	outputFiles = []
	for root, dirs, files in os.walk(directory, topdown=False):
		for f in files:
			if "output" in f and "swp" not in f:
				outputFiles.append(f)
	return outputFiles

def getAverageEditDistance(tuples):
	numOfTuples = len(tuples)
	totalEditDistance = 0

	for i in range(0, 100):
		t = tuples[i]
		if i % 10 == 0:
			print(i)
		totalEditDistance += edit_distance(t[1], t[2])
		print(str(totalEditDistance))

	averageEditDistance = totalEditDistance * 1.0 / 10
	#print(str(averageEditDistance))

	print("Average Edit Distance: " + str(averageEditDistance))

# Get the number of characters that appear in both the correct output
# and the predicted output
def getAverageNumberOfSimilarCharacters(tuples):
	numOfTuples = len(tuples)

	result = 0.0

	for t in tuples:
		description = tuples[0]
		realOutput = tuples[1]
		predictedOutput = tuples[2]

		temp = 0
		for c in realOutput:



def analyze():
	directory = sys.argv[1]

	for outputFile in getOutputFiles(directory):
		tuples = []

		#print(len(descriptionsAndRealOutputTuples))

		descriptionsAndRealOutputTuples = getDescriptionsAndRealOutput(directory)
		predictedOutputTuples = getPredictedOutput(directory, outputFile)

		for i in range(0, len(descriptionsAndRealOutputTuples)):
			tuples.append( (descriptionsAndRealOutputTuples[i][0], descriptionsAndRealOutputTuples[i][1], predictedOutputTuples[i]) )

		print(outputFile)
		print(str(getAverageEditDistance(tuples)))

analyze()
