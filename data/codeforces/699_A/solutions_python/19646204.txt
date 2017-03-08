n=int(raw_input())
list1=raw_input()
list2=map(int,raw_input().split(" "))
times=[]

start=0
ntimes=list1.count("RL") 
if ntimes==0:
	print -1
else:
	for i in xrange(0,ntimes):
		index=list1.find("RL",start)
		times.append((list2[index+1]-list2[index])/2)
		start=index+2
	print sorted(times)[0]