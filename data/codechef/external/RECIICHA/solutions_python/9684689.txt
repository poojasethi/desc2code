l=[0]*1000003
l[0]=1
for i in range(1,len(l)):
        l[i]=i*l[i-1]%1000003
for i in range(input()):
	n,x=map(int,raw_input().split())
	if n>=1000003:
                print "0"
	else:
                
                print ((l[n])*x)%1000003
