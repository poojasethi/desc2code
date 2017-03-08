#http://codeforces.com/contest/527/problem/B
#problem solved by Benegripe
#/usr/bin/py

n = int(raw_input())
s = [x for x in raw_input()]
t = [x for x in raw_input()]
ans = 0
ds = {}
dt = {}
for x in range(n):
	if s[x] != t[x]:
		ans += 1
		ds[(s[x],t[x])] = x
		dt[s[x]] = x
for x in range(n):
	if s[x] != t[x]:
		if (t[x],s[x]) in ds:
			print ans-2
			print x+1,ds[(t[x],s[x])]+1
			exit(0)
for x in range(n):
	if s[x] != t[x]:
		if t[x] in dt:
			print ans-1
			print x+1,dt[t[x]]+1
			exit(0)
print ans
print '-1 -1'
