n = int(raw_input())
data = sorted([map(int, raw_input().split()) for i in xrange(n)])
ret = 0
i = 0
j = 0
head = 1
for i in xrange(n):
	ai, aj = data[i]
	head = max(i+1, head)
	for j in xrange(head, n):
		#print "hello"
		bi, bj = data[j]
		if not (ai < bi and aj > bj):
			break
		ret+=1
		head = j+1
print ret
