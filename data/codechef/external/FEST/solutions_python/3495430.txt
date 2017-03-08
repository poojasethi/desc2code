# your code goes here
mod=1000000007
def power(A,B):
	res=1
	while B>0:
	    if B&1:
		    res=(res*A)%mod
	    A=(A*A)%mod
	    B=B>>1
	return res    
	

t=input()

while t:
	A,B=raw_input().split(" ")
	A=int(A)
	B=int(B)
	print(power(A,B))
	t-=1