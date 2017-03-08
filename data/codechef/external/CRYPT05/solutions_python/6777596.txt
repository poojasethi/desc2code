#! /usr/bin/env python

def genFibo(n):
	fibo=list()
	fibo.append(1)
	fibo.append(1)
	for i in range(2,n):
		fibo.append(fibo[i-1]+fibo[i-2])
	print fibo[n-1]
	
	
def main():
    sm=0
    
    n=input()
    while n:
    	genFibo(n)
    	n=input()

if __name__=="__main__":
    main()
