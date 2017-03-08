T = int(raw_input())
inputList = []
for i in range(0,T):
	listLength = int(raw_input())
	list1 = [int(x) for x in raw_input().split()]
	inputList.append(list1)
	
for list1 in inputList:
	prevCounter = 0
	tempCounter = 1
	total = [0]
	for index,value in enumerate(list1):
		if index > 0:
			if list1[index-1] > list1[index]:
				total.append(index)
	total.append(len(list1))
	totalAdd = 0
	i = 1
	while(i<len(total)):
		n1 = int(total[i-1]-total[i])
		tempSum = int(n1*(n1-1)/2)
		totalAdd = totalAdd + tempSum
		i+=1 
	print totalAdd