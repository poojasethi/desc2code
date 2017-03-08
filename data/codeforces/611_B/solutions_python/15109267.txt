a,b = map(int,raw_input().split())
str_a = bin(a)[2:]
str_b = bin(b)[2:]
ans = 0
for x in xrange(len(str_a),len(str_b)+1):
	tmp = '1' * x
	for x in xrange(1,len(tmp)):
		if a <= int(tmp[:x] + '0' + tmp[x+1:],2) <= b:
			ans += 1
print ans