import math
import os
import sys
ref = 3.1415926536
n  =int(raw_input())
list2 = [0]*n
list2 = map(int,raw_input().split())
list2.sort()
ans = 0.0000000000
k=1
for x in xrange(0,n):
	ans = ans+ref*k*list2[x]*list2[x]
	k=k*-1
print abs(ans)