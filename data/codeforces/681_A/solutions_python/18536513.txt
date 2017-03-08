


tt = int(raw_input())
ans = 'NO'
for i in xrange(tt):
	a = map(str, raw_input().split())
	ini = int(a[1])
	fin = int(a[2])
	if ini >= 2400 and ini < fin:
		ans = 'YES'

print ans
