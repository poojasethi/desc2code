
'''
tt = int(raw_input())
a = map(int, raw_input().split())
for i in xrange(tt):
a = map(int, (' '.join(n for n in raw_input())).split())
'''

tt = int(raw_input())
s = ''
for i in xrange(tt):
	if i & 1 == 0:
		s += 'I hate that '

	else:
		s += 'I love that '

s = s[:len(s) - 5]
print s + 'it'
