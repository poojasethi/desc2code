n = int(raw_input())
l = raw_input().split()

x = min(l.count('1'),l.count('2'),l.count('3'))
print x

if x != 0 :

	for y in range(0, x) :

		a = l.index('1')
		b = l.index('2')
		c = l.index('3')

		l[a] = l[b] = l[c] = ''

		print a+1, b+1, c+1