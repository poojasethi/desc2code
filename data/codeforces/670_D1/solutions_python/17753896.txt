
I = lambda : map(int, raw_input().split())

n, k = I()
a = I()
b = I()
ratio = [b[i]/a[i] for i in xrange(n)]
flag = "initial"
while flag != "final":
	m = min(ratio)
	# print "\nratios:",ratio
	# print "k:",k
	for i in xrange(len(ratio)):
		if ratio[i] == m:
			x = a[i]*(ratio[i]+1)-b[i]
			# print "deducting:",x,
			if k < x:
				flag = "final"
				break
			else:
				k -= x
				ratio[i] += 1
				b[i] += x

print min(ratio)

# def case():
# 	n = random.randint(1,9)
# 	k = random.randint(0,30)
# 	print n,k
# 	for i in xrange(n):
# 		print random.randint(1,15),
# 	print
# 	for i in xrange(n):
# 		print random.randint(10,30),
# 	print