n=raw_input()
if(int(n)%8==0):
	print "YES"
	print n
	exit(0)
else:
	for i in xrange(len(n)):
		for j in xrange(i+1,len(n)):
			for k in xrange(j+1,len(n)):
				ans=n[i]+n[j]+n[k]
				if(int(ans)%8==0):
					print "YES"
					print ans
					exit(0)
	for i in xrange(len(n)):
		for j in xrange(i+1,len(n)):
			ans=n[i]+n[j]
			if(int(ans)%8==0):
				print "YES"
				print ans
				exit(0)
	for i in xrange(len(n)):
		ans=n[i]
		if(int(ans)%8==0):
			print "YES"
			print ans
			exit(0)
print "NO"