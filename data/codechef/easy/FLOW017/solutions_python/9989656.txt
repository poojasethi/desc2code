from sys import stdin,stdout
t = int(stdin.readline())
for _ in xrange(t):
	a,b,c = map(int,stdin.readline().split())
	if a < b < c or c < b < a:
		stdout.write(str(b)+"\n")
	if c < a < b or b < a < c:
		stdout.write(str(a)+"\n")
	if a < c < b or b < c < a:
		stdout.write(str(c)+"\n")