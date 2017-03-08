#Manage maximum events given start date and duration for a case
def main():
	#f = open('C:\\Users\\GLCR3257\\Desktop\\pyLogics\\test.txt','r')
	N=int(raw_input())
	#print N
	E=[]
	for i in range(N):
		start,duration=map(int,raw_input().split())
		E.append([start+duration,start])
 
	E.sort()
	#print E
	x=E[0][0]
	#print x
	ans=1
 
	for i in range(1,N):
		if(E[i][1]>x):
			#print x
			ans=ans+1
			x=E[i][0]
 
	print(ans)
	
if __name__=='__main__':
	main()