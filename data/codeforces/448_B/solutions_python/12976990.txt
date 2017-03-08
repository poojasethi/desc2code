'''
Created on Sep 12, 2015

@author: sshadmin
'''
import sys
from collections import Counter
s=list(raw_input())
t=list(raw_input())

j=0
for i in range(len(s)):
    if s[i]==t[j]:
        j+=1
    if j == len(t):
        print "automaton"
        sys.exit()
if sorted(s)==sorted(t):
    print "array"
    sys.exit()
cs,ct=Counter(s),Counter(t)
cs.subtract(ct)
for key in cs:
    if cs[key]<0:
        print "need tree"
        sys.exit()
print "both"
        
    
    