from sys import stdin,stdout
t = int(stdin.readline())
while t > 0:
	n = int(stdin.readline())
	s = map(int,stdin.readline().split())
	s.sort()
	min = s[1] - s[0]
	for i in xrange(1,len(s)-1):
		if s[i+1] - s[i] < min:
			min = s[i+1] - s[i]
	stdout.write(str(min)+"\n")
	t -= 1		