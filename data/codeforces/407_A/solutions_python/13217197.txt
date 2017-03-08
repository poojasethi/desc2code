import math
import os
import sys
a,b = map(int,raw_input().split())
#print a,b
def func(a):
    return list([i,j] for i in range(1,a) for j in range(1,a) if i*i+j*j==a*a)

p1=func(a)
p2=func(b)
flag1=0
for [a,b] in p1:
	if flag1==1:
		break
    	for [c,d] in p2:
        	if a*c==b*d:
        		if b!=d:
	            		print "YES\n"
	            		print "0 0"
	            		print -a,b
	            		print c,d
	            		flag1=1

if flag1==0:
	print("NO")
