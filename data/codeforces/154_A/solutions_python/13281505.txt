import os
import math
import random
s = raw_input()
s=s+' '
k = input()
list1={}
i=0
ans=0
for x in xrange(1,k+1):
	temp=raw_input()
	list1[temp[0]]=temp[1]
	list1[temp[1]]=temp[0]
while i<len(s):
	if s[i] in list1.keys():
		count={s[i]:0,list1[s[i]]:0}
		while s[i] in count.keys():
			count[s[i]]+=1
			i+=1
		ans+=min(count.values())
	else:
		i+=1
print ans