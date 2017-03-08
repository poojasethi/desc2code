# your code goes here
from sys import stdin, stdout
t = int(stdin.readline())
while t:
	t -= 1
	n = int(stdin.readline())
	a = map(int, stdin.readline().strip().split(' '))
	if n <= 2:
		stdout.write(str(n)+"\n")
	else:
		m = 2
		c = 2
		i = 2
		while i < n:
			if a[i] != a[i-1] + a[i-2]:
				m = max(c, m)
				c = 2
			else:
				c += 1
			i += 1
		m = max(c, m)
		stdout.write(str(m)+'\n')