import sys
#sys.stdin = open("input.txt", 'r')
n = int(input())
a = map(int, raw_input().split())
d = 1005
x, y = 0, 0
for i in xrange(n):
	if abs(a[(i+1)%n] - a[i]) < d:
		x , y = (i+1)%n, i;
		d = abs(a[(i+1)%n] - a[i])
print x+1, y+1
