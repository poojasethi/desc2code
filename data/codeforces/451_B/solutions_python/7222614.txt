N = input()
a = map(int, raw_input().split())
b = sorted(a)
x = 0
y = 0
for i in xrange(0, N):
	if a[i] != b[i]:
		x = i
		break
for i in range(0, N)[::-1]:
	if a[i] != b[i]:
		y = i
		break
c = a[:x]+a[x:y+1][::-1]+a[y+1:]
if b == c:
	print 'yes'
	print x+1, y+1
else:
	print 'no'
