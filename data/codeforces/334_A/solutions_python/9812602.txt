#!/usr/bin/python

def main():
	n=int(raw_input())
	maximum=n**2
	for i in range(0, (n**2)/2):
		print str(i+1)+' '+str(maximum-i)

if __name__=='__main__':
	main()