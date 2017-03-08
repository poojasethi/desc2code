import sys
def GCD(A,B):
	if B==0:
		return A
	else:
		return GCD(B, A%B)


n= int(input())
while n>0:
	A,B= map(int, sys.stdin.readline().split())
	print GCD(A,B)
	n-= 1