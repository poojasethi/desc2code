import sys;
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")
n = int(input())
a = raw_input()
li = []
for i in xrange(n):
	if a[i] == '1':
		li.append(i);
l = len(li);
f = 1;
if l == 1 or l == 2:
	print "YES"
else:
	d = li[1] - li[0];
	for i in xrange(2, l):
		if d != li[i] - li[i-1]:
			f = 0;
			break;
	print "YES" if f else "NO";
