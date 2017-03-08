#http://codeforces.com/contest/525/problem/B
#problem solved by Benegripe
#/usr/bin/py
s = [x for x in raw_input()]
n = int(raw_input())
rev = [int(x)-1 for x in raw_input().split(' ')]
i,n,l,cont = 0,len(s),len(rev),0
rev = sorted(rev)
for x in range(n/2):
	while i < l and x == rev[i]:
			i += 1 
			cont += 1
	if 1 == cont % 2:
			s[x],s[n-x-1] = s[n-x-1],s[x]	
print "".join(s)
