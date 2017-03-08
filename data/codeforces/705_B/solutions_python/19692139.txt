
'''
tt = int(raw_input())
a = map(int, raw_input().split())
for i in xrange(tt):
a = map(int, (' '.join(n for n in raw_input())).split())
'''

tt = int(raw_input())
a = map(int, raw_input().split())
s = 0
for i in xrange(tt):
	s += a[i] - 1
	if s & 1 == 0:
		print '2'

	else:
		print '1'	