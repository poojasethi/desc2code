N = input()
A = map(int,raw_input().split())
ans = 0
maxbits = 0
for x in A:
	maxbits = max(maxbits,len(bin(x)[2:]))

for x in xrange(1,maxbits+1):
	cur = 0
	for y in A:
		if len(bin(y)[2:]) >= x:
			cur += int(bin(y)[2:][-x])
	ans += ((2**(x-1))*(cur*(cur-1)))/2
print ans