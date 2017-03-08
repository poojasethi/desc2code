#http://www.codechef.com/problems/DCE05/

x=int(raw_input())
while(x):
	t = int(raw_input())
	l = t
	l = l | (l >> 1)
	l = l | (l >> 2)
	l = l | (l >> 4)
	l = l | (l >> 8)
	l = l | (l >> 16)
	l = (l+1) >> 1
	print l
	x -= 1
	