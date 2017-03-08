n=int(raw_input())
s=""
if n>4 or n==1:
   print n
   for i in xrange(1,n+1,2):
      s+=str(i)+" "
   for i in xrange(2,n+1,2):
      s+=str(i)+" "
else:
   if n==2:
      print '1'
      s='1'
   elif n==3:
      print '2'
      s='1 3'
   elif n==4:
      print 4
      s='3 1 4 2'
print s
