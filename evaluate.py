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

    for t in tuples:
        totalEditDistance += edit_distance(t[1], t[2])

    averageEditDistance = totalEditDistance * 1.0 / numOfTuples

    print("Average Edit Distance: " + averageEditDistance)

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
        print(getAverageEditDistance(tuples))

analyze()
