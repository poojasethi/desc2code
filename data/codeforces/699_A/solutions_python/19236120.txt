n=int(raw_input())
s=raw_input()
x=map(int,raw_input().split())
d=10**10
for i in range(len(s)-1) : 
	if s[i]=='R' and s[i+1]=='L':
		d=min(d,(x[i+1]-x[i])/2)
	else:
		pass
if d!=10**10:
	print d
else:
	print -1			